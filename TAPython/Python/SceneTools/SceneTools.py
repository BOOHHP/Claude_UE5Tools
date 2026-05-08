import os

import unreal

# 类型 Aka 与对应 unreal 类的映射表（求值时延迟处理，避免启动期找不到类）
_TYPE_CLASS_MAP = {
    "chk_static_mesh": "unreal.StaticMeshActor",
    "chk_point_light": "unreal.PointLight",
    "chk_spot_light":  "unreal.SpotLight",
    "chk_dir_light":   "unreal.DirectionalLight",
    "chk_rect_light":  "unreal.RectLight",
    "chk_sky_light":   "unreal.SkyLight",
    "chk_decal":       "unreal.DecalActor",
    "chk_camera":      "unreal.CameraActor",
    "chk_trigger":     "unreal.TriggerVolume",
}

# 全部 Aka（含 blueprint，用于 select_all_types 遍历）
_ALL_TYPE_AKAS = [
    "chk_static_mesh", "chk_blueprint",
    "chk_point_light", "chk_spot_light",
    "chk_dir_light",   "chk_rect_light",
    "chk_sky_light",   "chk_decal",
    "chk_camera",      "chk_trigger",
]

_FRAME_TASK_CHUNK_SIZE = 50
_FRAME_TASK_INTERVAL_SECONDS = 0.03
_DECAL_TO_PLANE_SIZE_MULTIPLIER = 2.0


class SceneToolsController:

    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

        self.ui_scrollbox = "scene_tools_scroll"
        self.min_window_width = 360
        self.min_window_height = 300
        self.max_window_height = 720

        # True = 所有关卡，False = 当前关卡（Python 端维护状态，不回读 UI）
        self.scope_all = False
        # 防止 set_checkbox_state 触发 OnCheckStateChanged 引起回调循环
        self._scope_updating = False
        self._last_ground_snap_plan = []
        self._last_ground_snap_snapshot = []
        self._last_ground_snap_execution_report = {}
        self._last_render_property_plan = []
        self._last_render_property_report = {}
        self._last_receives_decals_plan = []
        self._last_receives_decals_report = {}
        self._last_decal_to_plane_plan = []
        self._last_decal_to_plane_report = {}
        self._last_invalid_actor_plan = []
        self._last_invalid_actor_report = {}
        self._invalid_actor_level_entries = []
        self._invalid_actor_selected_level_indexes = []
        self._last_align_distribution_plan = []
        self._last_align_distribution_report = {}
        self._align_axis_updating = False
        self._frame_tick_handle = None
        self._frame_timer_handle = None
        self._frame_task = None

    # ------------------------------------------------------------------
    # 生命周期 / 分帧任务清理
    # ------------------------------------------------------------------

    def on_closed(self):
        global instance
        try:
            self._unregister_frame_tick()
            self._frame_task = None
        except Exception as e:
            unreal.log_warning(f"SceneTools on_closed: {str(e)}")
        finally:
            if instance is self:
                instance = None

    # ------------------------------------------------------------------
    # 选择范围互斥逻辑
    # ------------------------------------------------------------------

    def on_scope_current_changed(self, checked):
        if self._scope_updating:
            return
        self._scope_updating = True
        try:
            if checked:
                self.scope_all = False
                self._set_checkbox_checked("chk_scope_all", False)
            else:
                if not self.scope_all:
                    # 防止两个都变为未选中 —— 强制保持当前关卡选中
                    self._set_checkbox_checked("chk_scope_current", True)
        except Exception as e:
            unreal.log_error(f"SceneTools scope_current: {str(e)}")
        finally:
            self._scope_updating = False

    def on_scope_all_changed(self, checked):
        if self._scope_updating:
            return
        self._scope_updating = True
        try:
            if checked:
                self.scope_all = True
                self._set_checkbox_checked("chk_scope_current", False)
            else:
                if self.scope_all:
                    # 防止两个都变为未选中 —— 强制保持所有关卡选中
                    self._set_checkbox_checked("chk_scope_all", True)
        except Exception as e:
            unreal.log_error(f"SceneTools scope_all: {str(e)}")
        finally:
            self._scope_updating = False

    # ------------------------------------------------------------------
    # 全选 / 全不选
    # ------------------------------------------------------------------

    def select_all_types_true(self):
        """全选所有物件类型"""
        try:
            for aka in _ALL_TYPE_AKAS:
                self._set_checkbox_checked(aka, True)
        except Exception as e:
            unreal.log_error(f"SceneTools select_all_types_true: {str(e)}")

    def select_all_types_false(self):
        """全不选所有物件类型"""
        try:
            for aka in _ALL_TYPE_AKAS:
                self._set_checkbox_checked(aka, False)
        except Exception as e:
            unreal.log_error(f"SceneTools select_all_types_false: {str(e)}")

    def clear_selection(self):
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            actor_subsystem.set_selected_level_actors([])

            msg = "已取消当前所有已选物件。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"取消选择失败：{str(e)}"
            unreal.log_error(f"SceneTools clear_selection: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # 主功能：批量选择
    # ------------------------------------------------------------------

    def execute_select(self):
        try:
            # 1. 收集被勾选的 Aka
            checked_akas = [
                aka for aka in _ALL_TYPE_AKAS
                if self.data.get_is_checked(aka)
            ]
            if not checked_akas:
                self.data.set_text("txt_status", "提示：请至少勾选一种物件类型。")
                return

            # 2. 获取候选 Actor 列表
            candidates = self._get_actors()
            if candidates is None:
                return  # _get_actors 内部已设状态

            # 3. 构建类型列表（延迟解析，拿不到的类静默跳过）
            target_classes = []
            check_blueprint = "chk_blueprint" in checked_akas
            for aka, class_str in _TYPE_CLASS_MAP.items():
                if aka in checked_akas:
                    try:
                        cls = eval(class_str)
                        target_classes.append(cls)
                    except Exception:
                        unreal.log_warning(f"SceneTools: 类 {class_str} 不可用，已跳过。")

            # 4. 过滤
            selected = []
            for actor in candidates:
                if self._matches_type(actor, target_classes, check_blueprint):
                    selected.append(actor)

            # 5. 执行选中
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            actor_subsystem.set_selected_level_actors(selected)

            # 6. 更新状态栏
            scope_label = "所有关卡" if self.scope_all else "当前关卡"
            if selected:
                msg = f"已选中 {len(selected)} / {len(candidates)} 个物件（{scope_label}）。"
            else:
                msg = f"未找到匹配的物件（扫描了 {len(candidates)} 个，范围：{scope_label}）。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")

        except Exception as e:
            error_msg = f"错误：{str(e)}"
            unreal.log_error(f"SceneTools execute_select: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 1：变换、标签图层、导出
    # ------------------------------------------------------------------

    def execute_reset_location(self):
        self._execute_reset_transform("location")

    def execute_reset_rotation(self):
        self._execute_reset_transform("rotation")

    def execute_normalize_scale(self):
        self._execute_reset_transform("scale")

    def execute_reset_all_transform(self):
        self._execute_reset_transform("all")

    def _execute_reset_transform(self, mode):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            mode_label = {
                "location": "位置归零",
                "rotation": "旋转归零",
                "scale": "缩放归一",
                "all": "全变换重置",
            }.get(mode, mode)
            updated = 0
            failed = 0
            action_name = f"SceneTools Reset Transform ({mode}, {len(selected_actors)} Actors)"
            try:
                with unreal.ScopedEditorTransaction(action_name):
                    for actor in selected_actors:
                        actor_name = self._safe_actor_name(actor)
                        try:
                            if not self._mark_actor_transform_for_undo(actor, actor_name):
                                failed += 1
                                continue
                            if self._apply_actor_transform_mode(actor, mode):
                                updated += 1
                        except Exception as e:
                            failed += 1
                            unreal.log_warning(f"SceneTools: 重置变换失败 {actor_name} - {str(e)}")
            except Exception as e:
                error_msg = f"{mode_label}失败：事务创建失败，已取消执行以避免不可撤销修改：{str(e)}"
                unreal.log_error(f"SceneTools execute_reset_transform: {error_msg}")
                self.data.set_text("txt_status", error_msg)
                return

            msg = f"{mode_label}完成（事务版）：修改 {updated}，失败 {failed}，共 {len(selected_actors)}。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"重置变换失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_reset_transform: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_export_actor_tags(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            export_path = str(self.data.get_text("input_export_path")).strip()
            if not export_path:
                export_path = os.path.join(os.path.expanduser("~"), "Desktop", "UE_Actor_Tag_Export.csv")

            actor_count = len(selected_actors)
            rows = ["ActorName,Tag"]
            for actor in selected_actors:
                actor_name = actor.get_name()
                tags = [str(tag) for tag in getattr(actor, "tags", [])]
                if tags:
                    for tag in tags:
                        rows.append(f"{actor_name},{tag}")
                else:
                    rows.append(f"{actor_name},")

            self._export_rows_to_text_or_csv(export_path, rows)

            msg = f"导出完成：{actor_count} 个 Actor -> {export_path}"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"导出失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_export_actor_tags: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 2：Actor 落地检测
    # ------------------------------------------------------------------

    def preview_ground_snap(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            plan, summary = self._build_ground_snap_plan(selected_actors)
            self._last_ground_snap_plan = plan

            preview_text = self._format_ground_snap_preview(plan, summary)
            self.data.set_text("txt_ground_snap_preview", preview_text)

            msg = (
                f"落地预览完成：需修正 {summary['ready']}，已贴地 {summary['within_threshold']}，"
                f"未命中 {summary['missed']}，失败 {summary['failed']}，共 {summary['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"落地预览失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_ground_snap: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_ground_snap(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            plan, summary = self._build_ground_snap_plan(selected_actors)
            self._last_ground_snap_plan = plan

            if self._start_ground_snap_frame_task(selected_actors, plan, summary):
                return

            report = self._execute_ground_snap_plan(plan, summary)
            self._last_ground_snap_snapshot = report["snapshots"]
            self._last_ground_snap_execution_report = report

            result_msg = (
                f"落地执行完成：修正 {report['changed']}，已贴地 {report['skipped']}，"
                f"未命中 {report['missed']}，失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", result_msg)
            unreal.log(f"SceneTools: {result_msg}")

            refreshed_plan, refreshed_summary = self._build_ground_snap_plan(selected_actors)
            self._last_ground_snap_plan = refreshed_plan
            preview_text = self._format_ground_snap_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_ground_snap_preview", preview_text + "\n\n" + self._format_ground_snap_execution_report(report))
        except Exception as e:
            error_msg = f"落地执行失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_ground_snap: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 2：G-11 批量修改物体渲染属性
    # ------------------------------------------------------------------

    def preview_render_property_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_render_property_settings()
            if not settings["enabled"]:
                msg = "提示：请至少勾选一项要修改的渲染属性。"
                self.data.set_text("txt_status", msg)
                self.data.set_text("txt_render_property_preview", msg)
                return

            plan, summary = self._build_render_property_plan(selected_actors, settings)
            self._last_render_property_plan = plan
            self.data.set_text("txt_render_property_preview", self._format_render_property_preview(plan, summary))

            msg = (
                f"渲染属性预览完成：待修改 {summary['changes']} 项，"
                f"无变化 Actor {summary['unchanged_actors']}，错误 {summary['errors']}，共 {summary['actors']} 个 Actor。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"渲染属性预览失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_render_property_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_render_property_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_render_property_settings()
            if not settings["enabled"]:
                msg = "提示：请至少勾选一项要修改的渲染属性。"
                self.data.set_text("txt_status", msg)
                self.data.set_text("txt_render_property_preview", msg)
                return

            plan, summary = self._build_render_property_plan(selected_actors, settings)
            self._last_render_property_plan = plan
            if self._start_render_property_frame_task(selected_actors, settings, plan, summary):
                return

            report = self._execute_render_property_plan(plan, summary)
            self._last_render_property_report = report

            refreshed_plan, refreshed_summary = self._build_render_property_plan(selected_actors, settings)
            self._last_render_property_plan = refreshed_plan
            preview_text = self._format_render_property_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_render_property_preview", preview_text + "\n\n" + self._format_render_property_report(report))

            msg = (
                f"渲染属性执行完成：修改 {report['changed']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']} 项。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"渲染属性执行失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_render_property_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 3：05 批量开关接受贴花（关卡实例 v1）
    # ------------------------------------------------------------------

    def preview_receives_decals_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_receives_decals_settings()
            plan, summary = self._build_receives_decals_plan(selected_actors, settings)
            self._last_receives_decals_plan = plan
            self.data.set_text("txt_receives_decals_preview", self._format_receives_decals_preview(plan, summary))

            msg = (
                f"接受贴花预览完成：待修改 {summary['changes']} 项，"
                f"无变化组件 {summary['unchanged_components']}，无组件 Actor {summary['no_component_actors']}，"
                f"错误 {summary['errors']}，共 {summary['actors']} 个 Actor。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"接受贴花预览失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_receives_decals_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_receives_decals_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_receives_decals_settings()
            plan, summary = self._build_receives_decals_plan(selected_actors, settings)
            self._last_receives_decals_plan = plan
            if self._start_receives_decals_frame_task(selected_actors, settings, plan, summary):
                return

            report = self._execute_receives_decals_plan(plan, summary)
            self._last_receives_decals_report = report

            refreshed_plan, refreshed_summary = self._build_receives_decals_plan(selected_actors, settings)
            self._last_receives_decals_plan = refreshed_plan
            preview_text = self._format_receives_decals_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_receives_decals_preview", preview_text + "\n\n" + self._format_receives_decals_report(report))

            msg = (
                f"接受贴花执行完成：修改 {report['changed']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']} 项。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"接受贴花执行失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_receives_decals_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 3：11 贴花转平面模型（v1）
    # ------------------------------------------------------------------

    def preview_decal_to_plane_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_decal_to_plane_settings()
            plan, summary = self._build_decal_to_plane_plan(selected_actors, settings)
            self._last_decal_to_plane_plan = plan
            self.data.set_text("txt_decal_to_plane_preview", self._format_decal_to_plane_preview(plan, summary))

            msg = (
                f"贴花转平面预览完成：可转换 {summary['ready']}，跳过 {summary['skipped']}，"
                f"错误 {summary['errors']}，共 {summary['total']} 个 Actor。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"贴花转平面预览失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_decal_to_plane_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_decal_to_plane_batch(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            settings = self._read_decal_to_plane_settings()
            plan, summary = self._build_decal_to_plane_plan(selected_actors, settings)
            self._last_decal_to_plane_plan = plan
            if self._start_decal_to_plane_frame_task(selected_actors, settings, plan, summary):
                return

            report = self._execute_decal_to_plane_plan(plan, summary, settings)
            self._last_decal_to_plane_report = report

            preview_text = self._format_decal_to_plane_preview(plan, summary)
            self.data.set_text("txt_decal_to_plane_preview", preview_text + "\n\n" + self._format_decal_to_plane_report(report))

            msg = (
                f"贴花转平面执行完成：生成 {report['created']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"贴花转平面执行失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_decal_to_plane_batch: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 3：G-14 场景无效 Actor 清理
    # ------------------------------------------------------------------

    def preview_invalid_actor_cleanup(self):
        try:
            settings = self._read_invalid_actor_cleanup_settings()
            scan_actors = self._get_invalid_actor_scan_actors_or_warn(settings)
            if not scan_actors:
                return

            plan, summary = self._build_invalid_actor_cleanup_plan(scan_actors, settings)
            self._last_invalid_actor_plan = plan
            self.data.set_text("txt_invalid_actor_preview", self._format_invalid_actor_preview(plan, summary))

            msg = (
                f"无效 Actor 扫描完成（{summary['scope_label']}）：待标记 {summary['mark']}，已标记 {summary['already_marked']}，"
                f"跳过 {summary['skip']}，错误 {summary['errors']}，共 {summary['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"无效 Actor 扫描失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_invalid_actor_cleanup: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_mark_invalid_actors(self):
        try:
            settings = self._read_invalid_actor_cleanup_settings()
            scan_actors = self._get_invalid_actor_scan_actors_or_warn(settings)
            if not scan_actors:
                return

            plan, summary = self._build_invalid_actor_cleanup_plan(scan_actors, settings)
            self._last_invalid_actor_plan = plan

            report = self._execute_invalid_actor_mark_plan(plan, summary, settings)
            self._last_invalid_actor_report = report

            refreshed_plan, refreshed_summary = self._build_invalid_actor_cleanup_plan(scan_actors, settings)
            self._last_invalid_actor_plan = refreshed_plan
            preview_text = self._format_invalid_actor_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_invalid_actor_preview", preview_text + "\n\n" + self._format_invalid_actor_report(report))

            msg = (
                f"无效 Actor 标记完成（{summary['scope_label']}）：标记 {report['marked']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"无效 Actor 标记失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_mark_invalid_actors: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_soft_delete_invalid_actors(self):
        try:
            settings = self._read_invalid_actor_cleanup_settings()
            scan_actors = self._get_invalid_actor_scan_actors_or_warn(settings)
            if not scan_actors:
                return

            plan, summary = self._build_invalid_actor_cleanup_plan(scan_actors, settings)
            self._last_invalid_actor_plan = plan

            report = self._execute_invalid_actor_soft_delete_plan(plan, summary, settings)
            self._last_invalid_actor_report = report

            refreshed_plan, refreshed_summary = self._build_invalid_actor_cleanup_plan(scan_actors, settings)
            self._last_invalid_actor_plan = refreshed_plan
            preview_text = self._format_invalid_actor_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_invalid_actor_preview", preview_text + "\n\n" + self._format_invalid_actor_soft_delete_report(report))

            msg = (
                f"无效 Actor 软删除完成（{summary['scope_label']}）：处理 {report['soft_deleted']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"无效 Actor 软删除失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_soft_delete_invalid_actors: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def select_last_invalid_actor_results(self):
        try:
            targets = [
                item.get("actor") for item in self._last_invalid_actor_plan
                if item.get("action") in ("mark", "already_marked") and item.get("actor") is not None
            ]
            if not targets:
                msg = "没有可选中的无效 Actor 结果，请先执行预览扫描。"
                self.data.set_text("txt_status", msg)
                return

            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            actor_subsystem.set_selected_level_actors(targets)
            msg = f"已选中最近扫描结果中的 {len(targets)} 个无效 Actor。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"选中无效 Actor 结果失败：{str(e)}"
            unreal.log_error(f"SceneTools select_last_invalid_actor_results: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def refresh_invalid_actor_level_list(self, show_status=True):
        try:
            old_selected_entries = self._get_selected_invalid_actor_level_entries(refresh_if_missing=False)
            old_selected_keys = set()
            for entry in old_selected_entries:
                old_selected_keys.update(entry.get("keys", []))

            entries = self._build_invalid_actor_level_entries()
            self._invalid_actor_level_entries = entries
            items = [entry["display"] for entry in entries]
            self._set_list_view_items("list_invalid_actor_levels", items)

            if not entries:
                self._invalid_actor_selected_level_indexes = []
                self._clear_invalid_actor_scan_results("当前世界没有可用的已加载关卡。")
                if show_status:
                    self.data.set_text("txt_status", "未找到已加载关卡。")
                return

            selected_indexes = self._resolve_invalid_actor_selected_level_indexes(old_selected_keys)
            self._set_invalid_actor_selected_level_indexes(selected_indexes, update_selection=True)

            info = self._format_invalid_actor_selected_levels_info()
            self.data.set_text("txt_invalid_actor_level_info", info)
            self._clear_invalid_actor_scan_results()
            if show_status:
                self.data.set_text("txt_status", f"已刷新关卡列表：{len(entries)} 个已加载关卡。{info}")
        except Exception as e:
            error_msg = f"刷新无效 Actor 关卡列表失败：{str(e)}"
            unreal.log_error(f"SceneTools refresh_invalid_actor_level_list: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def on_invalid_actor_level_selection_changed(self, item=None, index=None):
        try:
            selected_indexes = self._get_list_view_selected_indexes("list_invalid_actor_levels")
            if not selected_indexes:
                fallback_index = self._get_single_list_view_selected_index("list_invalid_actor_levels", index)
                if fallback_index >= 0:
                    selected_indexes = [fallback_index]
            selected_indexes = [i for i in selected_indexes if 0 <= i < len(self._invalid_actor_level_entries)]
            if not selected_indexes:
                # SListView 在按钮获得焦点时可能发出一次空选择事件；不要用它清空已有扫描关卡缓存。
                return

            self._set_invalid_actor_selected_level_indexes(selected_indexes, update_selection=False)
            info = self._format_invalid_actor_selected_levels_info()
            self.data.set_text("txt_invalid_actor_level_info", info)
            self._clear_invalid_actor_scan_results()
            self.data.set_text("txt_status", info)
        except Exception as e:
            error_msg = f"更新扫描关卡失败：{str(e)}"
            unreal.log_error(f"SceneTools on_invalid_actor_level_selection_changed: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def on_invalid_actor_level_double_click(self, item=None, index=None):
        try:
            try:
                selected_index = int(index)
            except Exception:
                selected_index = self._get_single_list_view_selected_index("list_invalid_actor_levels", None)
            if selected_index < 0 or selected_index >= len(self._invalid_actor_level_entries):
                return

            selected_indexes = list(self._invalid_actor_selected_level_indexes)
            if selected_index not in selected_indexes:
                selected_indexes.append(selected_index)
            self._set_invalid_actor_selected_level_indexes(selected_indexes, update_selection=True)
            info = self._format_invalid_actor_selected_levels_info()
            self.data.set_text("txt_invalid_actor_level_info", info)
            self._clear_invalid_actor_scan_results()
            self.data.set_text("txt_status", f"已激活扫描关卡：{self._invalid_actor_level_entries[selected_index]['name']}。{info}")
        except Exception as e:
            error_msg = f"双击激活扫描关卡失败：{str(e)}"
            unreal.log_error(f"SceneTools on_invalid_actor_level_double_click: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def select_all_invalid_actor_levels(self):
        try:
            if not self._invalid_actor_level_entries:
                self.refresh_invalid_actor_level_list(show_status=False)
            if not self._invalid_actor_level_entries:
                msg = "未找到可选择的已加载关卡。"
                self.data.set_text("txt_status", msg)
                self.data.set_text("txt_invalid_actor_level_info", msg)
                return

            selected_indexes = list(range(len(self._invalid_actor_level_entries)))
            self._set_invalid_actor_selected_level_indexes(selected_indexes, update_selection=True)
            info = self._format_invalid_actor_selected_levels_info()
            self.data.set_text("txt_invalid_actor_level_info", info)
            self._clear_invalid_actor_scan_results()
            self.data.set_text("txt_status", f"已选择所有已加载关卡。{info}")
        except Exception as e:
            error_msg = f"选择所有扫描关卡失败：{str(e)}"
            unreal.log_error(f"SceneTools select_all_invalid_actor_levels: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # Iteration 2：G-15 批量对齐 / 阵列 / 分布
    # ------------------------------------------------------------------

    def preview_align_to_first(self):
        self._preview_align_distribution("align")

    def execute_align_to_first(self):
        self._execute_align_distribution("align")

    def preview_distribute_even(self):
        self._preview_align_distribution("distribute")

    def execute_distribute_even(self):
        self._execute_align_distribution("distribute")

    def preview_array_by_step(self):
        self._preview_align_distribution("array")

    def execute_array_by_step(self):
        self._execute_align_distribution("array")

    def on_align_axis_x_changed(self, checked):
        self._on_align_axis_changed("X", checked)

    def on_align_axis_y_changed(self, checked):
        self._on_align_axis_changed("Y", checked)

    def on_align_axis_z_changed(self, checked):
        self._on_align_axis_changed("Z", checked)

    def _on_align_axis_changed(self, axis_name, checked):
        if self._align_axis_updating:
            return
        self._align_axis_updating = True
        try:
            is_checked = self._coerce_checkbox_value(checked)
            if not is_checked and not self._any_align_axis_checked():
                self._set_checkbox_checked(f"chk_align_axis_{axis_name.lower()}", True)
        except Exception as e:
            unreal.log_error(f"SceneTools align_axis: {str(e)}")
        finally:
            self._align_axis_updating = False

    def _preview_align_distribution(self, mode):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            plan, summary = self._build_align_distribution_plan(selected_actors, mode)
            self._last_align_distribution_plan = plan
            self.data.set_text("txt_align_preview", self._format_align_distribution_preview(plan, summary, mode))

            msg = (
                f"对齐/分布预览完成：待移动 {summary['changes']}，"
                f"无变化 {summary['unchanged']}，错误 {summary['errors']}，共 {summary['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"对齐/分布预览失败：{str(e)}"
            unreal.log_error(f"SceneTools preview_align_distribution: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def _execute_align_distribution(self, mode):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            plan, summary = self._build_align_distribution_plan(selected_actors, mode)
            self._last_align_distribution_plan = plan
            if self._start_align_distribution_frame_task(selected_actors, plan, summary, mode):
                return

            report = self._execute_align_distribution_plan(plan, summary, mode)
            self._last_align_distribution_report = report

            refreshed_plan, refreshed_summary = self._build_align_distribution_plan(selected_actors, mode)
            self._last_align_distribution_plan = refreshed_plan
            preview_text = self._format_align_distribution_preview(refreshed_plan, refreshed_summary, mode)
            self.data.set_text("txt_align_preview", preview_text + "\n\n" + self._format_align_distribution_report(report))

            msg = (
                f"对齐/分布执行完成：移动 {report['changed']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"对齐/分布执行失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_align_distribution: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def on_panel_expansion_changed(self, _is_expanded):
        self._resize_window_to_content()

    def _resize_window_to_content(self):
        current_size = unreal.ChameleonData.get_chameleon_window_size(self.json_path)
        if not current_size:
            return

        target_width = max(int(round(current_size.x)), self.min_window_width)
        target_height = self._calculate_target_window_height(current_size)

        if int(round(current_size.x)) == target_width and int(round(current_size.y)) == target_height:
            return

        unreal.ChameleonData.set_chameleon_window_size(
            self.json_path,
            unreal.Vector2D(target_width, target_height)
        )

    def _calculate_target_window_height(self, current_size):
        try:
            offsets = self.data.get_scroll_box_offsets(self.ui_scrollbox)
            view_fraction = offsets.get("viewFraction", 1.0)
            scroll_end = offsets.get("ScrollOffsetOfEnd", 0.0)

            if view_fraction <= 0.0 or view_fraction >= 1.0:
                content_height = current_size.y
            else:
                content_height = scroll_end / (1.0 - view_fraction)

            padded_height = int(round(content_height + 56))
            return max(self.min_window_height, min(padded_height, self.max_window_height))
        except Exception as e:
            unreal.log_warning(f"SceneTools resize fallback: {str(e)}")
            return max(int(round(current_size.y)), self.min_window_height)

    # ------------------------------------------------------------------
    # 内部工具方法
    # ------------------------------------------------------------------

    def _get_actors(self):
        """返回候选 Actor 列表；出错时更新状态栏并返回 None。"""
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            all_actors = actor_subsystem.get_all_level_actors()

            if self.scope_all:
                return list(all_actors)

            current_level = self._resolve_current_level()
            if current_level is None:
                self.data.set_text("txt_status", "无法识别当前关卡，已回退为扫描所有关卡。")
                unreal.log_warning("SceneTools: 无法识别当前关卡，已回退为扫描所有关卡。")
                return list(all_actors)

            return [a for a in all_actors if self._get_actor_level(a) == current_level]

        except Exception as e:
            error_msg = f"获取 Actor 列表失败：{str(e)}"
            unreal.log_error(f"SceneTools _get_actors: {error_msg}")
            self.data.set_text("txt_status", error_msg)
            return None

    def _get_selected_actors_or_warn(self):
        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        selected_actors = actor_subsystem.get_selected_level_actors()
        if not selected_actors:
            self.data.set_text("txt_status", "提示：没有选中的物件。")
            return []
        return selected_actors

    def _get_selected_actors(self):
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            return list(actor_subsystem.get_selected_level_actors())
        except Exception:
            return []

    def _export_rows_to_text_or_csv(self, export_path, rows):
        export_dir = os.path.dirname(export_path)
        if export_dir and not os.path.exists(export_dir):
            os.makedirs(export_dir, exist_ok=True)

        with open(export_path, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(row + "\n")

    def _apply_actor_transform_mode(self, actor, mode):
        location = actor.get_actor_location()
        rotation = actor.get_actor_rotation()
        scale = actor.get_actor_scale3d()

        if mode in ("location", "all"):
            location = unreal.Vector(0.0, 0.0, 0.0)
        if mode in ("rotation", "all"):
            rotation = unreal.Rotator(0.0, 0.0, 0.0)
        if mode in ("scale", "all"):
            scale = unreal.Vector(1.0, 1.0, 1.0)

        new_transform = unreal.Transform(location, rotation, scale)
        actor.set_actor_transform(new_transform, False, False)
        return True

    def _build_ground_snap_plan(self, actors):
        profile_name = str(self.data.get_text("input_ground_profile")).strip() or "BlockAll"
        max_distance = self._get_float_from_ui("input_ground_max_distance", 5000.0, 1.0)
        threshold = self._get_float_from_ui("input_ground_threshold", 1.0, 0.0)
        ground_offset = self._get_float_from_ui("input_ground_offset", 0.0, -100000.0)
        start_offset = self._get_float_from_ui("input_ground_start_offset", 50.0, 0.0)

        plan = []
        for actor in actors:
            try:
                trace_result = self._line_trace_actor_to_ground(actor, profile_name, max_distance, start_offset)
                if not trace_result["hit"]:
                    plan.append({
                        "action": "miss",
                        "actor": actor,
                        "name": actor.get_name(),
                        "reason": "未命中地面",
                    })
                    continue

                bottom_z = trace_result["bottom_z"]
                target_bottom_z = trace_result["hit_z"] + ground_offset
                delta_z = target_bottom_z - bottom_z
                action = "snap" if abs(delta_z) > threshold else "ok"
                plan.append({
                    "action": action,
                    "actor": actor,
                    "name": actor.get_name(),
                    "bottom_z": bottom_z,
                    "hit_z": trace_result["hit_z"],
                    "delta_z": delta_z,
                    "hit_source": trace_result.get("source", "trace"),
                    "reason": "" if action == "snap" else "阈值内",
                })
            except Exception as e:
                actor_name = self._safe_actor_name(actor)
                plan.append({
                    "action": "error",
                    "actor": actor,
                    "name": actor_name,
                    "reason": str(e),
                })

        return plan, self._summarize_ground_snap_plan(plan)

    def _line_trace_actor_to_ground(self, actor, profile_name, max_distance, start_offset):
        world = unreal.EditorLevelLibrary.get_editor_world()
        origin, extent = actor.get_actor_bounds(False, True)
        start_z = origin.z + extent.z + start_offset
        bottom_z = origin.z - extent.z
        end_z = bottom_z - max_distance
        start = unreal.Vector(origin.x, origin.y, start_z)
        end = unreal.Vector(origin.x, origin.y, end_z)

        hit = unreal.SystemLibrary.line_trace_single_by_profile(
            world,
            start,
            end,
            unreal.Name(profile_name),
            False,
            [actor],
            unreal.DrawDebugTrace.NONE,
            True,
        )
        if not hit:
            return self._find_bounds_ground_below_actor(actor, origin, extent, bottom_z)

        blocking_hit = self._safe_get_editor_property(hit, "blocking_hit")
        if not blocking_hit:
            return self._find_bounds_ground_below_actor(actor, origin, extent, bottom_z)

        impact_point = self._safe_get_editor_property(hit, "impact_point")
        if impact_point is None:
            impact_point = self._safe_get_editor_property(hit, "location")
        if impact_point is None:
            return self._find_bounds_ground_below_actor(actor, origin, extent, bottom_z)

        return {"hit": True, "bottom_z": bottom_z, "hit_z": impact_point.z, "source": "trace"}

    def _find_bounds_ground_below_actor(self, actor, origin, extent, bottom_z):
        best_top_z = None
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            candidates = actor_subsystem.get_all_level_actors()
        except Exception:
            candidates = []

        for candidate in candidates:
            if candidate == actor:
                continue

            try:
                candidate_origin, candidate_extent = candidate.get_actor_bounds(False, True)
                if not self._bounds_overlap_xy(origin, extent, candidate_origin, candidate_extent):
                    continue

                candidate_top_z = candidate_origin.z + candidate_extent.z
                if candidate_top_z > bottom_z + 1.0:
                    continue

                if best_top_z is None or candidate_top_z > best_top_z:
                    best_top_z = candidate_top_z
            except Exception:
                continue

        if best_top_z is None:
            return {"hit": False, "bottom_z": bottom_z, "hit_z": 0.0, "source": "bounds"}

        return {"hit": True, "bottom_z": bottom_z, "hit_z": best_top_z, "source": "bounds"}

    def _bounds_overlap_xy(self, origin_a, extent_a, origin_b, extent_b):
        overlap_x = abs(origin_a.x - origin_b.x) <= (extent_a.x + extent_b.x)
        overlap_y = abs(origin_a.y - origin_b.y) <= (extent_a.y + extent_b.y)
        return overlap_x and overlap_y

    def _summarize_ground_snap_plan(self, plan):
        summary = {
            "total": len(plan),
            "ready": 0,
            "within_threshold": 0,
            "missed": 0,
            "failed": 0,
        }
        for item in plan:
            if item["action"] == "snap":
                summary["ready"] += 1
            elif item["action"] == "ok":
                summary["within_threshold"] += 1
            elif item["action"] == "miss":
                summary["missed"] += 1
            elif item["action"] == "error":
                summary["failed"] += 1
        return summary

    def _format_ground_snap_preview(self, plan, summary):
        lines = []
        lines.append("=== Actor Ground Snap Preview ===")
        lines.append(
            f"Snap: {summary['ready']} | OK: {summary['within_threshold']} | Miss: {summary['missed']} | Error: {summary['failed']} | Total: {summary['total']}"
        )
        lines.append("")

        if not plan:
            lines.append("No selected actors.")
            return "\n".join(lines)

        max_rows = 120
        for index, item in enumerate(plan[:max_rows], 1):
            if item["action"] == "snap":
                lines.append(
                    f"{index:03d}. [SNAP] {item['name']}  deltaZ={item['delta_z']:.2f}  groundZ={item['hit_z']:.2f}  source={item.get('hit_source', 'trace')}"
                )
            elif item["action"] == "ok":
                lines.append(f"{index:03d}. [OK]   {item['name']}  deltaZ={item['delta_z']:.2f}")
            elif item["action"] == "miss":
                lines.append(f"{index:03d}. [MISS] {item['name']}  {item['reason']}")
            else:
                lines.append(f"{index:03d}. [ERR]  {item['name']}  {item['reason']}")

        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... {len(plan) - max_rows} more rows omitted")

        return "\n".join(lines)

    def _execute_ground_snap_plan(self, plan, summary):
        report = self._create_ground_snap_report(plan, summary)

        snap_items = [item for item in plan if item["action"] == "snap"]
        if not snap_items:
            return report

        action_name = f"SceneTools Ground Snap ({len(snap_items)} Actors)"
        self._apply_ground_snap_transaction(snap_items, report, action_name)
        return report

    def _create_ground_snap_report(self, plan, summary):
        report = {
            "total": summary["total"],
            "requested": summary["ready"],
            "changed": 0,
            "skipped": summary["within_threshold"],
            "missed": summary["missed"],
            "failed": summary["failed"],
            "snapshots": [],
            "failures": [],
        }
        for item in plan:
            if item["action"] == "error":
                report["failures"].append({"name": item["name"], "reason": item.get("reason", "")})
        return report

    def _apply_ground_snap_transaction(self, snap_items, report, action_name):
        changed_before = report["changed"]
        snapshot_count_before = len(report["snapshots"])
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_ground_snap_items(snap_items, report)
        except Exception as e:
            if report["changed"] == changed_before and len(report["snapshots"]) == snapshot_count_before:
                report["failed"] += len(snap_items)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
                unreal.log_warning(f"SceneTools: 事务创建失败，已取消落地执行 - {str(e)}")
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
                unreal.log_warning(f"SceneTools: 事务结束异常，已保留当前执行结果 - {str(e)}")

    def _start_ground_snap_frame_task(self, selected_actors, plan, summary):
        snap_items = [item for item in plan if item["action"] == "snap"]
        if len(snap_items) <= _FRAME_TASK_CHUNK_SIZE:
            return False
        if self._frame_task is not None:
            msg = "已有分帧任务正在执行，请等待当前任务完成后再执行。"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
            return True

        report = self._create_ground_snap_report(plan, summary)
        self._frame_task = {
            "kind": "ground_snap",
            "actors": list(selected_actors),
            "plan": plan,
            "summary": summary,
            "snap_items": snap_items,
            "index": 0,
            "report": report,
        }
        if not self._register_frame_tick():
            self._frame_task = None
            return False

        msg = f"落地分帧执行开始：每帧处理 {_FRAME_TASK_CHUNK_SIZE} 个，待修正 {len(snap_items)} 个。"
        self.data.set_text("txt_status", msg)
        self.data.set_text("txt_ground_snap_preview", self._format_ground_snap_preview(plan, summary) + "\n\n" + msg)
        unreal.log(f"SceneTools: {msg}")
        return True

    def _register_frame_tick(self):
        if self._frame_timer_handle is not None or self._frame_tick_handle is not None:
            return True
        try:
            self._frame_timer_handle = unreal.PythonBPLib.set_timer(
                self._on_frame_timer,
                _FRAME_TASK_INTERVAL_SECONDS,
                True,
            )
            return True
        except Exception as e:
            unreal.log_warning(f"SceneTools: Timer 注册失败，尝试 Slate tick 分帧 - {str(e)}")

        try:
            self._frame_tick_handle = unreal.register_slate_post_tick_callback(self._on_frame_tick)
            return True
        except Exception as e:
            unreal.log_warning(f"SceneTools: Slate tick 注册失败，回退同步执行 - {str(e)}")
            return False

    def _unregister_frame_tick(self):
        if self._frame_timer_handle is not None:
            try:
                unreal.PythonBPLib.clear_timer(self._frame_timer_handle)
            except Exception as e:
                unreal.log_warning(f"SceneTools: Timer 注销失败 - {str(e)}")
            finally:
                self._frame_timer_handle = None

        try:
            if self._frame_tick_handle is not None:
                unreal.unregister_slate_post_tick_callback(self._frame_tick_handle)
        except Exception as e:
            unreal.log_warning(f"SceneTools: Slate tick 注销失败 - {str(e)}")
        finally:
            self._frame_tick_handle = None

    def _on_frame_timer(self):
        self._process_frame_task()

    def _on_frame_tick(self, _delta_time):
        self._process_frame_task()

    def _process_frame_task(self):
        try:
            if self._frame_task is None:
                self._unregister_frame_tick()
                return
            if self._frame_task.get("kind") == "ground_snap":
                self._process_ground_snap_frame_task(self._frame_task)
            elif self._frame_task.get("kind") == "render_property":
                self._process_render_property_frame_task(self._frame_task)
            elif self._frame_task.get("kind") == "receives_decals":
                self._process_receives_decals_frame_task(self._frame_task)
            elif self._frame_task.get("kind") == "decal_to_plane":
                self._process_decal_to_plane_frame_task(self._frame_task)
            elif self._frame_task.get("kind") == "align_distribution":
                self._process_align_distribution_frame_task(self._frame_task)
        except Exception as e:
            unreal.log_error(f"SceneTools frame task: {str(e)}")
            self.data.set_text("txt_status", f"分帧任务失败：{str(e)}")
            self._frame_task = None
            self._unregister_frame_tick()

    def _process_ground_snap_frame_task(self, task):
        snap_items = task["snap_items"]
        start_index = task["index"]
        end_index = min(start_index + _FRAME_TASK_CHUNK_SIZE, len(snap_items))
        chunk = snap_items[start_index:end_index]
        action_name = f"SceneTools Ground Snap Frame ({start_index + 1}-{end_index}/{len(snap_items)})"
        self._apply_ground_snap_transaction(chunk, task["report"], action_name)
        task["index"] = end_index

        if end_index >= len(snap_items):
            self._finish_ground_snap_frame_task(task)
            return

        msg = f"落地分帧执行中：{end_index}/{len(snap_items)} 已处理。"
        self.data.set_text("txt_status", msg)

    def _finish_ground_snap_frame_task(self, task):
        report = task["report"]
        selected_actors = task["actors"]
        self._last_ground_snap_snapshot = report["snapshots"]
        self._last_ground_snap_execution_report = report

        result_msg = (
            f"落地分帧执行完成：修正 {report['changed']}，已贴地 {report['skipped']}，"
            f"未命中 {report['missed']}，失败 {report['failed']}，共 {report['total']}。"
        )
        self.data.set_text("txt_status", result_msg)
        unreal.log(f"SceneTools: {result_msg}")

        refreshed_plan, refreshed_summary = self._build_ground_snap_plan(selected_actors)
        self._last_ground_snap_plan = refreshed_plan
        preview_text = self._format_ground_snap_preview(refreshed_plan, refreshed_summary)
        self.data.set_text("txt_ground_snap_preview", preview_text + "\n\n" + self._format_ground_snap_execution_report(report))

        self._frame_task = None
        self._unregister_frame_tick()

    def _apply_ground_snap_items(self, snap_items, report):
        for item in snap_items:
            actor = item["actor"]
            try:
                old_location = actor.get_actor_location()
                new_location = unreal.Vector(old_location.x, old_location.y, old_location.z + item["delta_z"])
                if not self._mark_actor_transform_for_undo(actor, item["name"]):
                    report["failed"] += 1
                    report["failures"].append({
                        "name": item["name"],
                        "reason": "modify() 失败，已跳过以避免不可撤销修改",
                    })
                    continue
                snapshot = {
                    "name": item["name"],
                    "old_location": (old_location.x, old_location.y, old_location.z),
                    "new_location": (new_location.x, new_location.y, new_location.z),
                    "delta_z": item["delta_z"],
                    "ground_z": item["hit_z"],
                    "hit_source": item.get("hit_source", "trace"),
                }
                actor.set_actor_location(new_location, False, False)
                report["changed"] += 1
                report["snapshots"].append(snapshot)
            except Exception as e:
                report["failed"] += 1
                report["failures"].append({"name": item["name"], "reason": str(e)})
                unreal.log_warning(f"SceneTools: 落地修正失败 {item['name']} - {str(e)}")

    def _mark_actor_transform_for_undo(self, actor, actor_name):
        try:
            if actor.modify(True) is False:
                unreal.log_warning(f"SceneTools: Actor {actor_name} modify 返回 False")
                return False
        except Exception as e:
            unreal.log_warning(f"SceneTools: Actor {actor_name} modify 失败 - {str(e)}")
            return False

        root_component = None
        try:
            root_component = actor.get_root_component()
        except Exception:
            root_component = self._safe_get_editor_property(actor, "root_component")

        if root_component is not None:
            try:
                root_component.modify(True)
            except Exception as e:
                unreal.log_warning(f"SceneTools: Actor {actor_name} root component modify 失败 - {str(e)}")

        return True

    def _format_ground_snap_execution_report(self, report):
        lines = []
        lines.append("=== Last Ground Snap Execution ===")
        lines.append(
            f"Changed: {report['changed']} | Skipped: {report['skipped']} | Missed: {report['missed']} | Failed: {report['failed']} | Total: {report['total']}"
        )
        lines.append("")

        max_rows = 80
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            lines.append(
                f"{index:03d}. [MOVED] {snapshot['name']}  deltaZ={snapshot['delta_z']:.2f}  source={snapshot['hit_source']}"
            )

        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more moved rows omitted")

        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:20]:
                lines.append(f"- {failure['name']}: {failure['reason']}")

        return "\n".join(lines)

    def _read_render_property_settings(self):
        settings = {
            "actor_hidden": {
                "enabled": self._get_checkbox_checked("chk_render_actor_hidden_enabled"),
                "value": self._get_checkbox_checked("chk_render_actor_hidden_value"),
                "label": "Actor Hidden In Game",
            },
            "component_hidden": {
                "enabled": self._get_checkbox_checked("chk_render_component_hidden_enabled"),
                "value": self._get_checkbox_checked("chk_render_component_hidden_value"),
                "label": "Component Hidden In Game",
            },
            "component_visible": {
                "enabled": self._get_checkbox_checked("chk_render_component_visible_enabled"),
                "value": self._get_checkbox_checked("chk_render_component_visible_value"),
                "label": "Component Visibility",
            },
            "cast_shadow": {
                "enabled": self._get_checkbox_checked("chk_render_cast_shadow_enabled"),
                "value": self._get_checkbox_checked("chk_render_cast_shadow_value"),
                "label": "Cast Shadow",
            },
            "draw_distance": {
                "enabled": self._get_checkbox_checked("chk_render_draw_distance_enabled"),
                "value": self._get_float_from_ui("input_render_draw_distance", 0.0, 0.0),
                "label": "Max Draw Distance",
            },
        }
        settings["enabled"] = any(value["enabled"] for value in settings.values())
        return settings

    def _build_render_property_plan(self, actors, settings):
        plan = []
        for actor in actors:
            item = {
                "actor": actor,
                "name": self._safe_actor_name(actor),
                "changes": [],
                "errors": [],
            }
            try:
                if settings["actor_hidden"]["enabled"]:
                    self._add_actor_hidden_change(item, settings["actor_hidden"]["value"])

                scene_components = self._get_actor_components_by_class(actor, unreal.SceneComponent)
                primitive_components = self._get_actor_components_by_class(actor, unreal.PrimitiveComponent)

                if settings["component_hidden"]["enabled"]:
                    for component in scene_components:
                        self._add_component_bool_change(
                            item,
                            component,
                            "component_hidden",
                            "Component Hidden In Game",
                            self._get_component_hidden_in_game,
                            settings["component_hidden"]["value"],
                        )

                if settings["component_visible"]["enabled"]:
                    for component in scene_components:
                        self._add_component_bool_change(
                            item,
                            component,
                            "component_visible",
                            "Component Visibility",
                            self._get_component_visible,
                            settings["component_visible"]["value"],
                        )

                if settings["cast_shadow"]["enabled"]:
                    for component in primitive_components:
                        self._add_component_bool_change(
                            item,
                            component,
                            "cast_shadow",
                            "Cast Shadow",
                            self._get_component_cast_shadow,
                            settings["cast_shadow"]["value"],
                        )

                if settings["draw_distance"]["enabled"]:
                    for component in primitive_components:
                        self._add_component_float_change(
                            item,
                            component,
                            "draw_distance",
                            "Max Draw Distance",
                            self._get_component_max_draw_distance,
                            settings["draw_distance"]["value"],
                        )
            except Exception as e:
                item["errors"].append(str(e))
            plan.append(item)

        return plan, self._summarize_render_property_plan(plan)

    def _add_actor_hidden_change(self, item, target_value):
        actor = item["actor"]
        old_value = self._get_actor_hidden_in_game(actor)
        if old_value is None:
            item["errors"].append("无法读取 Actor Hidden In Game")
            return
        if bool(old_value) == bool(target_value):
            return
        item["changes"].append({
            "kind": "actor_hidden",
            "target": actor,
            "target_name": item["name"],
            "label": "Actor Hidden In Game",
            "old": bool(old_value),
            "new": bool(target_value),
        })

    def _add_component_bool_change(self, item, component, kind, label, getter, target_value):
        old_value = getter(component)
        component_name = self._safe_object_name(component)
        if old_value is None:
            item["errors"].append(f"{component_name}: 无法读取 {label}")
            return
        if bool(old_value) == bool(target_value):
            return
        item["changes"].append({
            "kind": kind,
            "target": component,
            "target_name": component_name,
            "owner_name": item["name"],
            "label": label,
            "old": bool(old_value),
            "new": bool(target_value),
        })

    def _add_component_float_change(self, item, component, kind, label, getter, target_value):
        old_value = getter(component)
        component_name = self._safe_object_name(component)
        if old_value is None:
            item["errors"].append(f"{component_name}: 无法读取 {label}")
            return
        if abs(float(old_value) - float(target_value)) <= 0.01:
            return
        item["changes"].append({
            "kind": kind,
            "target": component,
            "target_name": component_name,
            "owner_name": item["name"],
            "label": label,
            "old": float(old_value),
            "new": float(target_value),
        })

    def _summarize_render_property_plan(self, plan):
        summary = {
            "actors": len(plan),
            "actors_with_changes": 0,
            "unchanged_actors": 0,
            "changes": 0,
            "errors": 0,
        }
        for item in plan:
            change_count = len(item["changes"])
            error_count = len(item["errors"])
            summary["changes"] += change_count
            summary["errors"] += error_count
            if change_count:
                summary["actors_with_changes"] += 1
            elif not error_count:
                summary["unchanged_actors"] += 1
        return summary

    def _execute_render_property_plan(self, plan, summary):
        changes, report = self._collect_render_property_changes(plan, summary)

        if not changes:
            return report

        action_name = f"SceneTools Render Properties ({len(changes)} Changes)"
        self._apply_render_property_transaction(changes, report, action_name)
        report["skipped"] = max(0, report["total"] - report["changed"] - report["failed"])
        return report

    def _collect_render_property_changes(self, plan, summary):
        changes = []
        report = {
            "total": summary["changes"],
            "changed": 0,
            "skipped": 0,
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
        }
        for item in plan:
            changes.extend(item["changes"])
            for error in item["errors"]:
                report["failures"].append({"name": item["name"], "reason": error})
        return changes, report

    def _apply_render_property_transaction(self, changes, report, action_name):
        changed_before = report["changed"]
        snapshot_count_before = len(report["snapshots"])
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_render_property_changes(changes, report)
        except Exception as e:
            if report["changed"] == changed_before and len(report["snapshots"]) == snapshot_count_before:
                report["failed"] += len(changes)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
                unreal.log_warning(f"SceneTools: 渲染属性事务创建失败，已取消执行 - {str(e)}")
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
                unreal.log_warning(f"SceneTools: 渲染属性事务结束异常，已保留当前执行结果 - {str(e)}")

    def _start_render_property_frame_task(self, selected_actors, settings, plan, summary):
        changes, report = self._collect_render_property_changes(plan, summary)
        if len(changes) <= _FRAME_TASK_CHUNK_SIZE:
            return False
        if self._frame_task is not None:
            msg = "已有分帧任务正在执行，请等待当前任务完成后再执行。"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
            return True

        self._frame_task = {
            "kind": "render_property",
            "actors": list(selected_actors),
            "settings": settings,
            "plan": plan,
            "summary": summary,
            "changes": changes,
            "index": 0,
            "report": report,
        }
        if not self._register_frame_tick():
            self._frame_task = None
            return False

        msg = f"渲染属性分帧执行开始：每帧处理 {_FRAME_TASK_CHUNK_SIZE} 项，待修改 {len(changes)} 项。"
        self.data.set_text("txt_status", msg)
        self.data.set_text("txt_render_property_preview", self._format_render_property_preview(plan, summary) + "\n\n" + msg)
        unreal.log(f"SceneTools: {msg}")
        return True

    def _process_render_property_frame_task(self, task):
        changes = task["changes"]
        start_index = task["index"]
        end_index = min(start_index + _FRAME_TASK_CHUNK_SIZE, len(changes))
        chunk = changes[start_index:end_index]
        action_name = f"SceneTools Render Properties Frame ({start_index + 1}-{end_index}/{len(changes)})"
        self._apply_render_property_transaction(chunk, task["report"], action_name)
        task["index"] = end_index

        if end_index >= len(changes):
            self._finish_render_property_frame_task(task)
            return

        msg = f"渲染属性分帧执行中：{end_index}/{len(changes)} 已处理。"
        self.data.set_text("txt_status", msg)

    def _finish_render_property_frame_task(self, task):
        report = task["report"]
        report["skipped"] = max(0, report["total"] - report["changed"] - report["failed"])
        selected_actors = task["actors"]
        settings = task["settings"]
        self._last_render_property_report = report

        msg = (
            f"渲染属性分帧执行完成：修改 {report['changed']}，跳过 {report['skipped']}，"
            f"失败 {report['failed']}，共 {report['total']} 项。"
        )
        self.data.set_text("txt_status", msg)
        unreal.log(f"SceneTools: {msg}")

        refreshed_plan, refreshed_summary = self._build_render_property_plan(selected_actors, settings)
        self._last_render_property_plan = refreshed_plan
        preview_text = self._format_render_property_preview(refreshed_plan, refreshed_summary)
        self.data.set_text("txt_render_property_preview", preview_text + "\n\n" + self._format_render_property_report(report))

        self._frame_task = None
        self._unregister_frame_tick()

    def _apply_render_property_changes(self, changes, report):
        for change in changes:
            try:
                if not self._mark_object_for_undo(change["target"], change["target_name"]):
                    report["failed"] += 1
                    report["failures"].append({
                        "name": change["target_name"],
                        "reason": "modify() 失败，已跳过以避免不可撤销修改",
                    })
                    continue

                self._apply_render_property_change(change)
                report["changed"] += 1
                report["snapshots"].append({
                    "name": change["target_name"],
                    "owner": change.get("owner_name", ""),
                    "label": change["label"],
                    "old": change["old"],
                    "new": change["new"],
                })
            except Exception as e:
                report["failed"] += 1
                report["failures"].append({"name": change["target_name"], "reason": str(e)})
                unreal.log_warning(f"SceneTools: 渲染属性写入失败 {change['target_name']} - {str(e)}")

    def _apply_render_property_change(self, change):
        target = change["target"]
        new_value = change["new"]
        kind = change["kind"]
        if kind == "actor_hidden":
            try:
                target.set_actor_hidden_in_game(bool(new_value))
                return
            except Exception:
                target.set_actor_hidden(bool(new_value))
                return
        if kind == "component_hidden":
            target.set_hidden_in_game(bool(new_value), True)
            return
        if kind == "component_visible":
            target.set_visibility(bool(new_value), True)
            return
        if kind == "cast_shadow":
            target.set_cast_shadow(bool(new_value))
            return
        if kind == "draw_distance":
            target.set_editor_property("ld_max_draw_distance", float(new_value))
            return
        raise RuntimeError(f"未知渲染属性类型：{kind}")

    def _format_render_property_preview(self, plan, summary):
        lines = []
        lines.append("=== Render Property Preview ===")
        lines.append(
            f"Changes: {summary['changes']} | Actors: {summary['actors_with_changes']} / {summary['actors']} | Unchanged Actors: {summary['unchanged_actors']} | Errors: {summary['errors']}"
        )
        lines.append("")

        max_rows = 140
        row_count = 0
        for item in plan:
            for change in item["changes"]:
                row_count += 1
                if row_count > max_rows:
                    continue
                owner = change.get("owner_name", item["name"])
                lines.append(
                    f"{row_count:03d}. [CHANGE] {owner} :: {change['target_name']}  {change['label']}: {change['old']} -> {change['new']}"
                )
            for error in item["errors"]:
                row_count += 1
                if row_count <= max_rows:
                    lines.append(f"{row_count:03d}. [ERR] {item['name']}  {error}")

        if row_count == 0:
            lines.append("No changes needed.")
        elif row_count > max_rows:
            lines.append("")
            lines.append(f"... {row_count - max_rows} more rows omitted")

        return "\n".join(lines)

    def _format_render_property_report(self, report):
        lines = []
        lines.append("=== Last Render Property Execution ===")
        lines.append(
            f"Changed: {report['changed']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total: {report['total']}"
        )
        lines.append("")

        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            owner_prefix = f"{snapshot['owner']} :: " if snapshot.get("owner") else ""
            lines.append(
                f"{index:03d}. [SET] {owner_prefix}{snapshot['name']}  {snapshot['label']}: {snapshot['old']} -> {snapshot['new']}"
            )

        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more changed rows omitted")

        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")

        return "\n".join(lines)

    def _read_receives_decals_settings(self):
        return {
            "target_value": self._get_checkbox_checked("chk_receives_decals_value"),
            "label": "Receives Decals",
        }

    def _build_receives_decals_plan(self, actors, settings):
        plan = []
        for actor in actors:
            item = {
                "actor": actor,
                "name": self._safe_actor_name(actor),
                "changes": [],
                "unchanged": 0,
                "errors": [],
                "component_count": 0,
            }
            try:
                primitive_components = self._get_actor_components_by_class(actor, unreal.PrimitiveComponent)
                item["component_count"] = len(primitive_components)
                if not primitive_components:
                    plan.append(item)
                    continue

                for component in primitive_components:
                    self._add_receives_decals_change(item, component, settings["target_value"])
            except Exception as e:
                item["errors"].append(str(e))
            plan.append(item)

        return plan, self._summarize_receives_decals_plan(plan)

    def _add_receives_decals_change(self, item, component, target_value):
        component_name = self._safe_object_name(component)
        old_value = self._get_component_receives_decals(component)
        if old_value is None:
            item["errors"].append(f"{component_name}: 无法读取 Receives Decals")
            return
        if bool(old_value) == bool(target_value):
            item["unchanged"] += 1
            return
        item["changes"].append({
            "kind": "receives_decals",
            "target": component,
            "target_name": component_name,
            "owner_name": item["name"],
            "label": "Receives Decals",
            "old": bool(old_value),
            "new": bool(target_value),
        })

    def _summarize_receives_decals_plan(self, plan):
        summary = {
            "actors": len(plan),
            "actors_with_changes": 0,
            "components": 0,
            "changes": 0,
            "unchanged_components": 0,
            "no_component_actors": 0,
            "errors": 0,
        }
        for item in plan:
            change_count = len(item["changes"])
            summary["changes"] += change_count
            summary["components"] += item.get("component_count", 0)
            summary["unchanged_components"] += item.get("unchanged", 0)
            summary["errors"] += len(item["errors"])
            if item.get("component_count", 0) == 0:
                summary["no_component_actors"] += 1
            if change_count:
                summary["actors_with_changes"] += 1
        return summary

    def _execute_receives_decals_plan(self, plan, summary):
        changes, report = self._collect_receives_decals_changes(plan, summary)
        if not changes:
            return report

        action_name = f"SceneTools Receives Decals ({len(changes)} Components)"
        self._apply_receives_decals_transaction(changes, report, action_name)
        report["skipped"] = max(0, report["total"] - report["changed"] - report["failed"])
        return report

    def _collect_receives_decals_changes(self, plan, summary):
        changes = []
        report = {
            "total": summary["changes"],
            "changed": 0,
            "skipped": summary["unchanged_components"] + summary["no_component_actors"],
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
        }
        for item in plan:
            changes.extend(item["changes"])
            for error in item["errors"]:
                report["failures"].append({"name": item["name"], "reason": error})
        return changes, report

    def _apply_receives_decals_transaction(self, changes, report, action_name):
        changed_before = report["changed"]
        snapshot_count_before = len(report["snapshots"])
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_receives_decals_changes(changes, report)
        except Exception as e:
            if report["changed"] == changed_before and len(report["snapshots"]) == snapshot_count_before:
                report["failed"] += len(changes)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
                unreal.log_warning(f"SceneTools: 接受贴花事务创建失败，已取消执行 - {str(e)}")
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
                unreal.log_warning(f"SceneTools: 接受贴花事务结束异常，已保留当前执行结果 - {str(e)}")

    def _start_receives_decals_frame_task(self, selected_actors, settings, plan, summary):
        changes, report = self._collect_receives_decals_changes(plan, summary)
        if len(changes) <= _FRAME_TASK_CHUNK_SIZE:
            return False
        if self._frame_task is not None:
            msg = "已有分帧任务正在执行，请等待当前任务完成后再执行。"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
            return True

        self._frame_task = {
            "kind": "receives_decals",
            "actors": list(selected_actors),
            "settings": settings,
            "plan": plan,
            "summary": summary,
            "changes": changes,
            "index": 0,
            "report": report,
        }
        if not self._register_frame_tick():
            self._frame_task = None
            return False

        msg = f"接受贴花分帧执行开始：每帧处理 {_FRAME_TASK_CHUNK_SIZE} 项，待修改 {len(changes)} 项。"
        self.data.set_text("txt_status", msg)
        self.data.set_text("txt_receives_decals_preview", self._format_receives_decals_preview(plan, summary) + "\n\n" + msg)
        unreal.log(f"SceneTools: {msg}")
        return True

    def _process_receives_decals_frame_task(self, task):
        changes = task["changes"]
        start_index = task["index"]
        end_index = min(start_index + _FRAME_TASK_CHUNK_SIZE, len(changes))
        chunk = changes[start_index:end_index]
        action_name = f"SceneTools Receives Decals Frame ({start_index + 1}-{end_index}/{len(changes)})"
        self._apply_receives_decals_transaction(chunk, task["report"], action_name)
        task["index"] = end_index

        if end_index >= len(changes):
            self._finish_receives_decals_frame_task(task)
            return

        msg = f"接受贴花分帧执行中：{end_index}/{len(changes)} 已处理。"
        self.data.set_text("txt_status", msg)

    def _finish_receives_decals_frame_task(self, task):
        report = task["report"]
        report["skipped"] = max(0, report["total"] - report["changed"] - report["failed"])
        selected_actors = task["actors"]
        settings = task["settings"]
        self._last_receives_decals_report = report

        msg = (
            f"接受贴花分帧执行完成：修改 {report['changed']}，跳过 {report['skipped']}，"
            f"失败 {report['failed']}，共 {report['total']} 项。"
        )
        self.data.set_text("txt_status", msg)
        unreal.log(f"SceneTools: {msg}")

        refreshed_plan, refreshed_summary = self._build_receives_decals_plan(selected_actors, settings)
        self._last_receives_decals_plan = refreshed_plan
        preview_text = self._format_receives_decals_preview(refreshed_plan, refreshed_summary)
        self.data.set_text("txt_receives_decals_preview", preview_text + "\n\n" + self._format_receives_decals_report(report))

        self._frame_task = None
        self._unregister_frame_tick()

    def _apply_receives_decals_changes(self, changes, report):
        for change in changes:
            try:
                if not self._mark_object_for_undo(change["target"], change["target_name"]):
                    report["failed"] += 1
                    report["failures"].append({
                        "name": change["target_name"],
                        "reason": "modify() 失败，已跳过以避免不可撤销修改",
                    })
                    continue

                self._apply_receives_decals_change(change)
                report["changed"] += 1
                report["snapshots"].append({
                    "name": change["target_name"],
                    "owner": change.get("owner_name", ""),
                    "label": change["label"],
                    "old": change["old"],
                    "new": change["new"],
                })
            except Exception as e:
                report["failed"] += 1
                report["failures"].append({"name": change["target_name"], "reason": str(e)})
                unreal.log_warning(f"SceneTools: 接受贴花写入失败 {change['target_name']} - {str(e)}")

    def _apply_receives_decals_change(self, change):
        target = change["target"]
        new_value = bool(change["new"])
        if hasattr(target, "set_receives_decals"):
            target.set_receives_decals(new_value)
            return
        target.set_editor_property("receives_decals", new_value)

    def _format_receives_decals_preview(self, plan, summary):
        lines = []
        lines.append("=== Receives Decals Preview ===")
        lines.append(
            f"Changes: {summary['changes']} | Actors: {summary['actors_with_changes']} / {summary['actors']} | Components: {summary['components']} | Unchanged Components: {summary['unchanged_components']} | No Component Actors: {summary['no_component_actors']} | Errors: {summary['errors']}"
        )
        lines.append("")

        max_rows = 140
        row_count = 0
        for item in plan:
            if item.get("component_count", 0) == 0:
                row_count += 1
                if row_count <= max_rows:
                    lines.append(f"{row_count:03d}. [SKIP] {item['name']}  no PrimitiveComponent")
            for change in item["changes"]:
                row_count += 1
                if row_count <= max_rows:
                    owner = change.get("owner_name", item["name"])
                    lines.append(
                        f"{row_count:03d}. [CHANGE] {owner} :: {change['target_name']}  {change['label']}: {change['old']} -> {change['new']}"
                    )
            for error in item["errors"]:
                row_count += 1
                if row_count <= max_rows:
                    lines.append(f"{row_count:03d}. [ERR] {item['name']}  {error}")

        if row_count == 0:
            lines.append("No changes needed.")
        elif row_count > max_rows:
            lines.append("")
            lines.append(f"... {row_count - max_rows} more rows omitted")

        return "\n".join(lines)

    def _format_receives_decals_report(self, report):
        lines = []
        lines.append("=== Last Receives Decals Execution ===")
        lines.append(
            f"Changed: {report['changed']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total: {report['total']}"
        )
        lines.append("")

        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            owner_prefix = f"{snapshot['owner']} :: " if snapshot.get("owner") else ""
            lines.append(
                f"{index:03d}. [SET] {owner_prefix}{snapshot['name']}  {snapshot['label']}: {snapshot['old']} -> {snapshot['new']}"
            )

        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more changed rows omitted")

        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")

        return "\n".join(lines)

    def _read_invalid_actor_cleanup_settings(self):
        marker_tag = str(self.data.get_text("input_invalid_actor_marker_tag")).strip()
        if not marker_tag:
            marker_tag = "SceneTools_InvalidActor"
        soft_delete_folder = str(self.data.get_text("input_invalid_actor_soft_delete_folder")).strip()
        if not soft_delete_folder:
            soft_delete_folder = "_SceneTools_InvalidActors"
        target_level_entries = self._get_selected_invalid_actor_level_entries(refresh_if_missing=True)
        return {
            "marker_tag": marker_tag,
            "soft_delete_folder": soft_delete_folder,
            "target_level_entries": target_level_entries,
            "scan_scope_label": self._format_invalid_actor_scan_scope_label(target_level_entries),
            "check_empty_actor": self._get_checkbox_checked("chk_invalid_empty_actor"),
            "check_missing_static_mesh": self._get_checkbox_checked("chk_invalid_missing_static_mesh"),
        }

    def _format_invalid_actor_scan_scope_label(self, target_level_entries):
        if not target_level_entries:
            return "未选择关卡"
        names = [entry["name"] for entry in target_level_entries]
        if len(names) <= 3:
            return "关卡扫描: " + ", ".join(names)
        return "关卡扫描: " + ", ".join(names[:3]) + f" ... +{len(names) - 3}"

    def _get_invalid_actor_scan_actors_or_warn(self, settings):
        target_level_entries = settings.get("target_level_entries") or []
        if not target_level_entries:
            msg = "提示：请先在关卡扫描列表中选择一个或多个关卡。"
            self.data.set_text("txt_status", msg)
            return []

        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        all_actors = list(actor_subsystem.get_all_level_actors())
        target_keys = set()
        target_names = []
        for entry in target_level_entries:
            target_keys.update(entry.get("keys", []))
            target_names.append(entry.get("name", "<UnknownLevel>"))

        matched_actors = [actor for actor in all_actors if self._actor_matches_level_keys(actor, target_keys)]
        if not matched_actors:
            msg = f"所选关卡中没有可扫描的 Actor：{', '.join(target_names[:5])}"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
        return matched_actors

    def _actor_matches_level_keys(self, actor, target_keys):
        if not target_keys:
            return False
        level = self._get_actor_level(actor)
        actor_keys = set(self._get_level_identity_candidates(level))
        return bool(actor_keys and target_keys and actor_keys.intersection(target_keys))

    def _format_loaded_level_names(self, actors):
        names = []
        for actor in actors:
            level = self._get_actor_level(actor)
            candidates = self._get_level_name_candidates(level)
            display_name = candidates[0] if candidates else "<UnknownLevel>"
            if display_name not in names:
                names.append(display_name)
        if not names:
            return "无"
        return ", ".join(names[:20]) + (f" ... +{len(names) - 20}" if len(names) > 20 else "")

    def _build_invalid_actor_level_entries(self):
        levels_by_key = {}
        actor_counts = {}

        for level in self._get_loaded_editor_levels():
            entry = self._make_invalid_actor_level_entry(level)
            if entry is not None:
                levels_by_key[entry["primary_key"]] = entry

        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        for actor in list(actor_subsystem.get_all_level_actors()):
            level = self._get_actor_level(actor)
            entry = self._make_invalid_actor_level_entry(level)
            if entry is None:
                continue
            if entry["primary_key"] not in levels_by_key:
                levels_by_key[entry["primary_key"]] = entry
            actor_counts[entry["primary_key"]] = actor_counts.get(entry["primary_key"], 0) + 1

        current_level = self._resolve_current_level()
        current_keys = set(self._get_level_identity_candidates(current_level))
        entries = list(levels_by_key.values())
        for entry in entries:
            entry["actor_count"] = actor_counts.get(entry["primary_key"], 0)
            entry["is_current"] = bool(current_keys and current_keys.intersection(set(entry["keys"])))
            prefix = "[Current] " if entry["is_current"] else ""
            entry["display"] = f"{prefix}{entry['name']}  ({entry['actor_count']} Actors)"

        entries.sort(key=lambda item: (not item.get("is_current", False), item["name"].lower()))
        return entries

    def _get_loaded_editor_levels(self):
        levels = []
        try:
            world = unreal.EditorLevelLibrary.get_editor_world()
            for level in list(unreal.EditorLevelUtils.get_levels(world)):
                if level is not None and level not in levels:
                    levels.append(level)
        except Exception as e:
            unreal.log_warning(f"SceneTools: EditorLevelUtils.get_levels 不可用，使用 Actor 关卡回退 - {str(e)}")

        current_level = self._resolve_current_level()
        if current_level is not None and current_level not in levels:
            levels.append(current_level)
        return levels

    def _make_invalid_actor_level_entry(self, level):
        if level is None:
            return None
        keys = self._get_level_identity_candidates(level)
        if not keys:
            return None
        return {
            "level": level,
            "name": self._get_level_display_name(level),
            "keys": keys,
            "primary_key": keys[0],
            "actor_count": 0,
            "is_current": False,
            "display": "",
        }

    def _get_level_display_name(self, level):
        candidates = self._get_level_name_candidates(level)
        if candidates:
            return candidates[0]
        return "<UnknownLevel>"

    def _get_selected_invalid_actor_level_entries(self, refresh_if_missing=False):
        self._sync_invalid_actor_selected_levels_from_view()
        if refresh_if_missing and not self._invalid_actor_level_entries:
            self.refresh_invalid_actor_level_list(show_status=False)
        entries = []
        for index in self._invalid_actor_selected_level_indexes:
            if 0 <= index < len(self._invalid_actor_level_entries):
                entries.append(self._invalid_actor_level_entries[index])
        return entries

    def _resolve_invalid_actor_selected_level_indexes(self, old_selected_keys):
        selected_indexes = []
        if old_selected_keys:
            for index, entry in enumerate(self._invalid_actor_level_entries):
                if old_selected_keys.intersection(set(entry.get("keys", []))):
                    selected_indexes.append(index)
            if selected_indexes:
                return selected_indexes
        for index, entry in enumerate(self._invalid_actor_level_entries):
            if entry.get("is_current"):
                return [index]
        return [0] if self._invalid_actor_level_entries else []

    def _set_invalid_actor_selected_level_indexes(self, indexes, update_selection):
        unique_indexes = []
        for index in indexes:
            index = int(index)
            if 0 <= index < len(self._invalid_actor_level_entries) and index not in unique_indexes:
                unique_indexes.append(index)
        self._invalid_actor_selected_level_indexes = unique_indexes
        if update_selection:
            self._set_list_view_selection("list_invalid_actor_levels", unique_indexes)

    def _sync_invalid_actor_selected_levels_from_view(self):
        selected_indexes = [
            index for index in self._get_list_view_selected_indexes("list_invalid_actor_levels")
            if 0 <= index < len(self._invalid_actor_level_entries)
        ]
        if selected_indexes:
            self._invalid_actor_selected_level_indexes = selected_indexes

    def _format_invalid_actor_selected_levels_info(self):
        entries = self._get_selected_invalid_actor_level_entries(refresh_if_missing=False)
        if not entries:
            return "未选择扫描关卡。点击“刷新关卡列表”后选择一个或多个关卡。"
        total_actors = sum(entry.get("actor_count", 0) for entry in entries)
        names = [entry["name"] for entry in entries]
        if len(names) <= 3:
            level_text = ", ".join(names)
        else:
            level_text = ", ".join(names[:3]) + f" ... +{len(names) - 3}"
        return f"已选择 {len(entries)} 个扫描关卡，Actor 数：{total_actors}。{level_text}"

    def _clear_invalid_actor_scan_results(self, message=""):
        self._last_invalid_actor_plan = []
        self._last_invalid_actor_report = {}
        if message:
            self.data.set_text("txt_invalid_actor_preview", message)
        else:
            self.data.set_text("txt_invalid_actor_preview", "关卡选择已变化，请重新预览无效 Actor。")

    def _get_level_identity_candidates(self, level):
        if level is None:
            return []
        candidates = []
        for getter_name in ("get_path_name", "get_name"):
            try:
                getter = getattr(level, getter_name)
                value = getter()
                if value:
                    candidates.append(str(value))
            except Exception:
                pass
        try:
            value = str(level)
            if value:
                candidates.append(value)
        except Exception:
            pass
        unique_candidates = []
        for candidate in candidates:
            if candidate and candidate not in unique_candidates:
                unique_candidates.append(candidate)
        return unique_candidates

    def _get_level_name_candidates(self, level):
        if level is None:
            return []
        candidates = []
        for getter_name in ("get_name", "get_path_name"):
            try:
                getter = getattr(level, getter_name)
                value = getter()
                if value:
                    candidates.append(str(value))
            except Exception:
                pass
        try:
            value = str(level)
            if value:
                candidates.append(value)
        except Exception:
            pass

        unique_candidates = []
        for candidate in candidates:
            if candidate and candidate not in unique_candidates:
                unique_candidates.append(candidate)
        return unique_candidates

    def _build_invalid_actor_cleanup_plan(self, actors, settings):
        plan = []
        for actor in actors:
            item = {
                "actor": actor,
                "name": self._safe_actor_name(actor),
                "action": "skip",
                "reason": "未命中无效规则",
                "details": [],
                "errors": [],
                "already_marked": False,
            }
            try:
                reasons = self._detect_invalid_actor_reasons(actor, settings)
                item["details"] = reasons
                item["already_marked"] = self._actor_has_marker_tag(actor, settings["marker_tag"])
                if reasons:
                    if item["already_marked"]:
                        item["action"] = "already_marked"
                        item["reason"] = f"已存在标记 Tag: {settings['marker_tag']}"
                    else:
                        item["action"] = "mark"
                        item["reason"] = "; ".join(reasons)
            except Exception as e:
                item["action"] = "error"
                item["reason"] = str(e)
                item["errors"].append(str(e))
            plan.append(item)
        summary = self._summarize_invalid_actor_cleanup_plan(plan)
        summary["scope_label"] = settings.get("scan_scope_label", "关卡扫描")
        summary["source_actor_count"] = len(actors)
        return plan, summary

    def _detect_invalid_actor_reasons(self, actor, settings):
        reasons = []
        if settings.get("check_missing_static_mesh"):
            missing_mesh_reason = self._detect_missing_static_mesh_reason(actor)
            if missing_mesh_reason:
                reasons.append(missing_mesh_reason)
        if settings.get("check_empty_actor"):
            empty_reason = self._detect_empty_actor_reason(actor)
            if empty_reason:
                reasons.append(empty_reason)
        return reasons

    def _detect_missing_static_mesh_reason(self, actor):
        try:
            if isinstance(actor, unreal.StaticMeshActor):
                component = self._get_static_mesh_component(actor)
                mesh = self._get_static_mesh_from_component(component)
                if mesh is None:
                    return "StaticMeshActor 缺失 Static Mesh"
        except Exception as e:
            return f"StaticMeshActor 检测失败: {str(e)}"
        return ""

    def _detect_empty_actor_reason(self, actor):
        try:
            if self._is_actor_type_exempt_from_empty_check(actor):
                return ""
            components = self._get_actor_components_by_class(actor, unreal.ActorComponent)
            if not components:
                return "Actor 无组件"
            if self._has_meaningful_actor_component(actor, components):
                return ""
            return "Actor 仅包含空 Scene 组件或无有效渲染/灯光/相机/贴花组件"
        except Exception as e:
            return f"空 Actor 检测失败: {str(e)}"

    def _is_actor_type_exempt_from_empty_check(self, actor):
        exempt_class_names = (
            "WorldSettings",
            "LevelScriptActor",
            "DefaultPhysicsVolume",
            "Brush",
            "Volume",
            "WorldDataLayers",
            "DataLayer",
            "DataLayerInstance",
            "HLOD",
            "LevelInstance",
            "PackedLevelActor",
            "Landscape",
            "LandscapeStreamingProxy",
            "FoliageActor",
            "InstancedFoliageActor",
            "LightmassImportanceVolume",
            "LightmassCharacterIndirectDetailVolume",
            "LightmassPortal",
            "PostProcessVolume",
            "SkyAtmosphere",
            "ExponentialHeightFog",
            "VolumetricCloud",
            "ReflectionCapture",
            "SphereReflectionCapture",
            "BoxReflectionCapture",
            "PlanarReflection",
        )
        try:
            class_name = actor.get_class().get_name()
        except Exception:
            class_name = actor.__class__.__name__
        return any(name in str(class_name) for name in exempt_class_names)

    def _has_meaningful_actor_component(self, actor, components):
        for component in components:
            if component is None:
                continue
            if self._is_meaningful_component(component):
                return True
        try:
            child_actors = actor.get_attached_actors()
            if child_actors:
                return True
        except Exception:
            pass
        return False

    def _is_meaningful_component(self, component):
        if isinstance(component, unreal.StaticMeshComponent):
            return self._get_static_mesh_from_component(component) is not None
        meaningful_classes = []
        for class_name in (
            "SkeletalMeshComponent",
            "InstancedStaticMeshComponent",
            "HierarchicalInstancedStaticMeshComponent",
            "LightComponent",
            "LocalLightComponent",
            "DirectionalLightComponent",
            "PointLightComponent",
            "SpotLightComponent",
            "RectLightComponent",
            "SkyLightComponent",
            "LightmassPortalComponent",
            "CameraComponent",
            "DecalComponent",
            "SplineComponent",
            "AudioComponent",
            "NiagaraComponent",
            "ParticleSystemComponent",
            "PostProcessComponent",
            "SkyAtmosphereComponent",
            "ExponentialHeightFogComponent",
            "VolumetricCloudComponent",
            "ReflectionCaptureComponent",
            "SphereReflectionCaptureComponent",
            "BoxReflectionCaptureComponent",
            "PlanarReflectionComponent",
            "LandscapeComponent",
            "LandscapeHeightfieldCollisionComponent",
            "FoliageInstancedStaticMeshComponent",
            "InstancedFoliageActorComponent",
            "BrushComponent",
            "BillboardComponent",
            "MaterialBillboardComponent",
            "TextRenderComponent",
            "ArrowComponent",
            "ChildActorComponent",
        ):
            component_class = getattr(unreal, class_name, None)
            if component_class is not None:
                meaningful_classes.append(component_class)
        for component_class in meaningful_classes:
            try:
                if isinstance(component, component_class):
                    return True
            except Exception:
                continue
        return False

    def _get_static_mesh_from_component(self, component):
        if component is None:
            return None
        try:
            mesh_attr = component.static_mesh
            if callable(mesh_attr):
                return mesh_attr()
            return mesh_attr
        except Exception:
            return self._safe_get_editor_property(component, "static_mesh")

    def _summarize_invalid_actor_cleanup_plan(self, plan):
        summary = {
            "total": len(plan),
            "mark": 0,
            "already_marked": 0,
            "skip": 0,
            "errors": 0,
        }
        for item in plan:
            action = item.get("action")
            if action == "mark":
                summary["mark"] += 1
            elif action == "already_marked":
                summary["already_marked"] += 1
            elif action == "error":
                summary["errors"] += 1
            else:
                summary["skip"] += 1
        return summary

    def _execute_invalid_actor_mark_plan(self, plan, summary, settings):
        report = {
            "total": summary["mark"],
            "marked": 0,
            "skipped": summary["skip"] + summary["already_marked"],
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
            "marker_tag": settings["marker_tag"],
        }
        targets = [item for item in plan if item.get("action") == "mark"]
        for item in plan:
            if item.get("action") == "error":
                report["failures"].append({"name": item["name"], "reason": item.get("reason", "未知错误")})
        if not targets:
            return report

        changed_before = report["marked"]
        try:
            with unreal.ScopedEditorTransaction(f"SceneTools Mark Invalid Actors ({len(targets)} Actors)"):
                for item in targets:
                    self._apply_invalid_actor_marker(item, settings, report)
        except Exception as e:
            if report["marked"] == changed_before:
                report["failed"] += len(targets)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
            unreal.log_warning(f"SceneTools: 无效 Actor 标记事务异常 - {str(e)}")
        return report

    def _execute_invalid_actor_soft_delete_plan(self, plan, summary, settings):
        targets = [item for item in plan if item.get("action") in ("mark", "already_marked")]
        report = {
            "total": len(targets),
            "soft_deleted": 0,
            "skipped": summary["skip"],
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
            "marker_tag": settings["marker_tag"],
            "folder": settings["soft_delete_folder"],
        }
        for item in plan:
            if item.get("action") == "error":
                report["failures"].append({"name": item["name"], "reason": item.get("reason", "未知错误")})
        if not targets:
            return report

        changed_before = report["soft_deleted"]
        try:
            with unreal.ScopedEditorTransaction(f"SceneTools Soft Delete Invalid Actors ({len(targets)} Actors)"):
                for item in targets:
                    self._apply_invalid_actor_soft_delete(item, settings, report)
        except Exception as e:
            if report["soft_deleted"] == changed_before:
                report["failed"] += len(targets)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
            unreal.log_warning(f"SceneTools: 无效 Actor 软删除事务异常 - {str(e)}")
        return report

    def _apply_invalid_actor_marker(self, item, settings, report):
        actor = item["actor"]
        actor_name = item["name"]
        marker_tag = settings["marker_tag"]
        try:
            if not self._mark_object_for_undo(actor, actor_name):
                report["failed"] += 1
                report["failures"].append({"name": actor_name, "reason": "modify() 失败，已跳过以避免不可撤销修改"})
                return
            old_tags = self._get_actor_tag_strings(actor)
            if marker_tag in old_tags:
                report["skipped"] += 1
                return
            new_tags = old_tags + [marker_tag]
            tag_names = [unreal.Name(tag) for tag in new_tags]
            try:
                actor.tags = tag_names
            except Exception:
                actor.set_editor_property("tags", tag_names)
            report["marked"] += 1
            report["snapshots"].append({
                "name": actor_name,
                "tag": marker_tag,
                "reason": item.get("reason", ""),
                "old_tags": old_tags,
                "new_tags": new_tags,
            })
        except Exception as e:
            report["failed"] += 1
            report["failures"].append({"name": actor_name, "reason": str(e)})
            unreal.log_warning(f"SceneTools: 无效 Actor 标记失败 {actor_name} - {str(e)}")

    def _apply_invalid_actor_soft_delete(self, item, settings, report):
        actor = item["actor"]
        actor_name = item["name"]
        marker_tag = settings["marker_tag"]
        folder_path = settings["soft_delete_folder"]
        try:
            if not self._mark_object_for_undo(actor, actor_name):
                report["failed"] += 1
                report["failures"].append({"name": actor_name, "reason": "modify() 失败，已跳过以避免不可撤销修改"})
                return

            old_tags = self._get_actor_tag_strings(actor)
            old_folder = self._get_actor_folder_path(actor)
            new_tags = list(old_tags)
            if marker_tag not in new_tags:
                new_tags.append(marker_tag)
                tag_names = [unreal.Name(tag) for tag in new_tags]
                try:
                    actor.tags = tag_names
                except Exception:
                    actor.set_editor_property("tags", tag_names)

            try:
                actor.set_folder_path(unreal.Name(folder_path))
            except Exception:
                actor.set_folder_path(folder_path)

            hidden = self._set_actor_editor_visibility(actor, False)
            if not hidden:
                raise RuntimeError("编辑器隐藏接口不可用")

            report["soft_deleted"] += 1
            report["snapshots"].append({
                "name": actor_name,
                "tag": marker_tag,
                "folder": folder_path,
                "old_folder": old_folder,
                "reason": item.get("reason", "; ".join(item.get("details", []))),
                "old_tags": old_tags,
                "new_tags": new_tags,
            })
        except Exception as e:
            report["failed"] += 1
            report["failures"].append({"name": actor_name, "reason": str(e)})
            unreal.log_warning(f"SceneTools: 无效 Actor 软删除失败 {actor_name} - {str(e)}")

    def _actor_has_marker_tag(self, actor, marker_tag):
        try:
            return bool(actor.actor_has_tag(unreal.Name(marker_tag)))
        except Exception:
            return marker_tag in self._get_actor_tag_strings(actor)

    def _get_actor_tag_strings(self, actor):
        try:
            tags = actor.tags()
        except Exception:
            tags = self._safe_get_editor_property(actor, "tags") or []
        result = []
        for tag in tags or []:
            tag_text = str(tag)
            if tag_text and tag_text not in result:
                result.append(tag_text)
        return result

    def _get_actor_folder_path(self, actor):
        try:
            return str(actor.get_folder_path())
        except Exception:
            value = self._safe_get_editor_property(actor, "folder_path")
            return str(value) if value is not None else ""

    def _format_invalid_actor_preview(self, plan, summary):
        lines = []
        lines.append("=== Invalid Actor Cleanup Preview ===")
        lines.append(f"Scope: {summary.get('scope_label', '关卡扫描')} | Source Actors: {summary.get('source_actor_count', summary['total'])}")
        lines.append(
            f"Mark: {summary['mark']} | Already Marked: {summary['already_marked']} | Skip: {summary['skip']} | Errors: {summary['errors']} | Total: {summary['total']}"
        )
        lines.append("")
        max_rows = 140
        for index, item in enumerate(plan[:max_rows], 1):
            action = item.get("action", "skip")
            if action == "mark":
                lines.append(f"{index:03d}. [MARK] {item['name']}  {item['reason']}")
            elif action == "already_marked":
                detail_text = "; ".join(item.get("details", []))
                lines.append(f"{index:03d}. [TAGGED] {item['name']}  {detail_text}")
            elif action == "error":
                lines.append(f"{index:03d}. [ERR] {item['name']}  {item.get('reason', '')}")
            else:
                lines.append(f"{index:03d}. [SKIP] {item['name']}  {item.get('reason', '')}")
        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... {len(plan) - max_rows} more rows omitted")
        return "\n".join(lines)

    def _format_invalid_actor_report(self, report):
        lines = []
        lines.append("=== Last Invalid Actor Mark Execution ===")
        lines.append(
            f"Marked: {report['marked']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total Targets: {report['total']} | Tag: {report['marker_tag']}"
        )
        lines.append("")
        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            lines.append(f"{index:03d}. [TAG] {snapshot['name']}  +{snapshot['tag']}  reason={snapshot['reason']}")
        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more tagged rows omitted")
        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")
        return "\n".join(lines)

    def _format_invalid_actor_soft_delete_report(self, report):
        lines = []
        lines.append("=== Last Invalid Actor Soft Delete Execution ===")
        lines.append(
            f"Soft Deleted: {report['soft_deleted']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total Targets: {report['total']} | Folder: {report['folder']} | Tag: {report['marker_tag']}"
        )
        lines.append("")
        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            lines.append(
                f"{index:03d}. [SOFT_DELETE] {snapshot['name']}  folder={snapshot['folder']}  +{snapshot['tag']}  reason={snapshot['reason']}"
            )
        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more soft deleted rows omitted")
        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")
        return "\n".join(lines)

    def _read_decal_to_plane_settings(self):
        suffix = str(self.data.get_text("input_decal_plane_suffix")).strip()
        if not suffix:
            suffix = "_Plane"
        return {
            "suffix": suffix,
            "copy_material": self._get_checkbox_checked("chk_decal_plane_copy_material"),
            "hide_source": self._get_checkbox_checked("chk_decal_plane_hide_source"),
            "plane_asset_path": "/Engine/BasicShapes/Plane.Plane",
        }

    def _build_decal_to_plane_plan(self, actors, settings):
        plan = []
        for actor in actors:
            actor_name = self._safe_actor_name(actor)
            try:
                if not isinstance(actor, unreal.DecalActor):
                    plan.append({
                        "action": "skip",
                        "actor": actor,
                        "name": actor_name,
                        "reason": "不是 DecalActor",
                    })
                    continue

                decal_component = self._get_decal_component(actor)
                if decal_component is None:
                    plan.append({
                        "action": "error",
                        "actor": actor,
                        "name": actor_name,
                        "reason": "无法获取 DecalComponent",
                    })
                    continue

                decal_size = self._get_decal_size(decal_component)
                if decal_size is None:
                    plan.append({
                        "action": "error",
                        "actor": actor,
                        "name": actor_name,
                        "reason": "无法读取 Decal Size",
                    })
                    continue

                material = self._get_decal_material(actor, decal_component) if settings["copy_material"] else None
                material_mode = self._describe_decal_plane_material_mode(material)
                location, rotation, scale, dimensions = self._make_decal_plane_transform(actor, decal_component, decal_size)
                label = self._make_decal_plane_label(actor, settings["suffix"])
                plan.append({
                    "action": "convert",
                    "actor": actor,
                    "name": actor_name,
                    "label": label,
                    "decal_size": decal_size,
                    "location": location,
                    "rotation": rotation,
                    "scale": scale,
                    "dimensions": dimensions,
                    "material": material,
                    "material_name": self._safe_object_name(material) if material is not None else "<None>",
                    "material_mode": material_mode,
                })
            except Exception as e:
                plan.append({"action": "error", "actor": actor, "name": actor_name, "reason": str(e)})

        return plan, self._summarize_decal_to_plane_plan(plan)

    def _summarize_decal_to_plane_plan(self, plan):
        summary = {"total": len(plan), "ready": 0, "skipped": 0, "errors": 0}
        for item in plan:
            if item["action"] == "convert":
                summary["ready"] += 1
            elif item["action"] == "skip":
                summary["skipped"] += 1
            elif item["action"] == "error":
                summary["errors"] += 1
        return summary

    def _execute_decal_to_plane_plan(self, plan, summary, settings):
        convert_items = [item for item in plan if item["action"] == "convert"]
        report = self._create_decal_to_plane_report(plan, summary)
        if not convert_items:
            return report

        action_name = f"SceneTools Decal To Plane ({len(convert_items)} Decals)"
        self._apply_decal_to_plane_transaction(convert_items, report, settings, action_name)
        return report

    def _create_decal_to_plane_report(self, plan, summary):
        report = {
            "total": summary["total"],
            "created": 0,
            "skipped": summary["skipped"],
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
        }
        for item in plan:
            if item["action"] == "error":
                report["failures"].append({"name": item["name"], "reason": item.get("reason", "")})
        return report

    def _apply_decal_to_plane_transaction(self, convert_items, report, settings, action_name):
        created_before = report["created"]
        snapshot_count_before = len(report["snapshots"])
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_decal_to_plane_items(convert_items, report, settings)
        except Exception as e:
            if report["created"] == created_before and len(report["snapshots"]) == snapshot_count_before:
                report["failed"] += len(convert_items)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
                unreal.log_warning(f"SceneTools: 贴花转平面事务创建失败，已取消执行 - {str(e)}")
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
                unreal.log_warning(f"SceneTools: 贴花转平面事务结束异常，已保留当前执行结果 - {str(e)}")

    def _start_decal_to_plane_frame_task(self, selected_actors, settings, plan, summary):
        convert_items = [item for item in plan if item["action"] == "convert"]
        if len(convert_items) <= _FRAME_TASK_CHUNK_SIZE:
            return False
        if self._frame_task is not None:
            msg = "已有分帧任务正在执行，请等待当前任务完成后再执行。"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
            return True

        self._frame_task = {
            "kind": "decal_to_plane",
            "actors": list(selected_actors),
            "settings": settings,
            "plan": plan,
            "summary": summary,
            "convert_items": convert_items,
            "index": 0,
            "report": self._create_decal_to_plane_report(plan, summary),
        }
        if not self._register_frame_tick():
            self._frame_task = None
            return False

        msg = f"贴花转平面分帧执行开始：每帧处理 {_FRAME_TASK_CHUNK_SIZE} 个，待转换 {len(convert_items)} 个。"
        self.data.set_text("txt_status", msg)
        self.data.set_text("txt_decal_to_plane_preview", self._format_decal_to_plane_preview(plan, summary) + "\n\n" + msg)
        unreal.log(f"SceneTools: {msg}")
        return True

    def _process_decal_to_plane_frame_task(self, task):
        convert_items = task["convert_items"]
        start_index = task["index"]
        end_index = min(start_index + _FRAME_TASK_CHUNK_SIZE, len(convert_items))
        chunk = convert_items[start_index:end_index]
        action_name = f"SceneTools Decal To Plane Frame ({start_index + 1}-{end_index}/{len(convert_items)})"
        self._apply_decal_to_plane_transaction(chunk, task["report"], task["settings"], action_name)
        task["index"] = end_index

        if end_index >= len(convert_items):
            self._finish_decal_to_plane_frame_task(task)
            return

        msg = f"贴花转平面分帧执行中：{end_index}/{len(convert_items)} 已处理。"
        self.data.set_text("txt_status", msg)

    def _finish_decal_to_plane_frame_task(self, task):
        report = task["report"]
        self._last_decal_to_plane_report = report

        msg = (
            f"贴花转平面分帧执行完成：生成 {report['created']}，跳过 {report['skipped']}，"
            f"失败 {report['failed']}，共 {report['total']}。"
        )
        self.data.set_text("txt_status", msg)
        unreal.log(f"SceneTools: {msg}")
        self.data.set_text(
            "txt_decal_to_plane_preview",
            self._format_decal_to_plane_preview(task["plan"], task["summary"]) + "\n\n" + self._format_decal_to_plane_report(report),
        )

        self._frame_task = None
        self._unregister_frame_tick()

    def _apply_decal_to_plane_items(self, convert_items, report, settings):
        plane_mesh = self._load_plane_mesh(settings["plane_asset_path"])
        if plane_mesh is None:
            raise RuntimeError(f"无法加载 Plane StaticMesh：{settings['plane_asset_path']}")

        for item in convert_items:
            try:
                source_actor = item["actor"]
                if not self._mark_object_for_undo(source_actor, item["name"]):
                    report["failed"] += 1
                    report["failures"].append({"name": item["name"], "reason": "源 Actor modify() 失败"})
                    continue

                plane_actor = self._spawn_plane_actor_from_item(item, plane_mesh)
                if plane_actor is None:
                    raise RuntimeError("生成 Plane Actor 失败")

                plane_component = self._get_static_mesh_component(plane_actor)
                if plane_component is None:
                    raise RuntimeError("生成的 Actor 缺少 StaticMeshComponent")

                self._mark_object_for_undo(plane_actor, item["label"])
                self._mark_object_for_undo(plane_component, f"{item['label']} StaticMeshComponent")

                material_to_apply = None
                material_applied = False
                material_apply_name = "<None>"
                material_apply_mode = "none"
                material_note = ""
                if item.get("material") is not None:
                    material_to_apply, material_apply_mode, material_note = self._resolve_decal_plane_material(item["material"])
                    material_apply_name = self._safe_object_name(material_to_apply) if material_to_apply is not None else "<None>"
                    if material_to_apply is not None:
                        material_applied = self._apply_material_to_plane_component(plane_component, material_to_apply)

                if settings["hide_source"]:
                    self._set_actor_editor_visibility(source_actor, False)

                report["created"] += 1
                report["snapshots"].append({
                    "source": item["name"],
                    "created": item["label"],
                    "source_material": item["material_name"],
                    "material": material_apply_name,
                    "material_mode": material_apply_mode,
                    "material_note": material_note,
                    "material_applied": material_applied,
                    "scale": (item["scale"].x, item["scale"].y, item["scale"].z),
                    "dimensions": item["dimensions"],
                    "hidden_source": bool(settings["hide_source"]),
                })
            except Exception as e:
                report["failed"] += 1
                report["failures"].append({"name": item["name"], "reason": str(e)})
                unreal.log_warning(f"SceneTools: 贴花转平面失败 {item['name']} - {str(e)}")

    def _spawn_plane_actor_from_item(self, item, plane_mesh):
        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        plane_actor = actor_subsystem.spawn_actor_from_object(plane_mesh, item["location"], item["rotation"], False)
        if plane_actor is None:
            return None
        try:
            plane_actor.set_actor_label(item["label"], True)
        except Exception:
            pass
        plane_actor.set_actor_scale3d(item["scale"])
        return plane_actor

    def _apply_material_to_plane_component(self, plane_component, material):
        try:
            plane_component.set_material(0, material)
        except Exception as e:
            unreal.log_warning(f"SceneTools: set_material 贴花材质失败 - {str(e)}")

        try:
            plane_component.set_editor_property("override_materials", [material])
        except Exception:
            pass

        try:
            current_material = plane_component.get_material(0)
            if current_material is not None and self._safe_object_name(current_material) == self._safe_object_name(material):
                return True
        except Exception:
            pass

        return False

    def _describe_decal_plane_material_mode(self, material):
        if material is None:
            return "none"
        return "direct-source"

    def _resolve_decal_plane_material(self, material):
        if material is None:
            return None, "none", ""
        note = "source Decal material assigned directly"
        return material, "direct-source", note

    def _load_plane_mesh(self, plane_asset_path):
        try:
            plane_mesh = unreal.load_asset(plane_asset_path)
            if plane_mesh is not None:
                return plane_mesh
        except Exception:
            pass
        try:
            return unreal.EditorAssetLibrary.load_asset(plane_asset_path)
        except Exception:
            return None

    def _get_decal_component(self, actor):
        try:
            return actor.decal()
        except Exception:
            return self._safe_get_editor_property(actor, "decal")

    def _get_decal_size(self, decal_component):
        try:
            return decal_component.decal_size()
        except Exception:
            return self._safe_get_editor_property(decal_component, "decal_size")

    def _get_decal_material(self, actor, decal_component):
        material = self._safe_get_editor_property(decal_component, "decal_material")
        if material is not None:
            return material
        try:
            return actor.get_decal_material()
        except Exception:
            pass
        try:
            return decal_component.get_decal_material()
        except Exception:
            pass
        try:
            return decal_component.decal_material()
        except Exception:
            return self._safe_get_editor_property(decal_component, "decal_material")

    def _get_static_mesh_component(self, actor):
        try:
            if isinstance(actor, unreal.StaticMeshActor):
                component_attr = actor.static_mesh_component
                if callable(component_attr):
                    return component_attr()
                return component_attr
        except Exception:
            pass
        components = self._get_actor_components_by_class(actor, unreal.StaticMeshComponent)
        return components[0] if components else None

    def _make_decal_plane_transform(self, actor, decal_component, decal_size):
        source_location = actor.get_actor_location()
        component_scale = self._get_decal_component_world_scale(actor, decal_component)

        depth = max(abs(float(decal_size.x) * abs(float(component_scale.x))), 1.0)
        decal_width = max(abs(float(decal_size.y) * abs(float(component_scale.y))), 1.0)
        decal_height = max(abs(float(decal_size.z) * abs(float(component_scale.z))), 1.0)

        surface_location = unreal.Vector(float(source_location.x), float(source_location.y), float(source_location.z))
        right, up = self._get_decal_component_surface_axes(actor, decal_component)
        plane_width, plane_height = self._estimate_zero_rotation_plane_size(right, up, decal_width, decal_height)
        size_source = "component_world_scale"
        size_multiplier = _DECAL_TO_PLANE_SIZE_MULTIPLIER
        if plane_width is not None and plane_height is not None:
            plane_width *= size_multiplier
            plane_height *= size_multiplier
        if plane_width is None or plane_height is None:
            plane_width, plane_height, size_source = self._get_decal_bounds_plane_size(actor)
            size_multiplier = 1.0
        if plane_width is None or plane_height is None:
            plane_width = decal_width
            plane_height = decal_height
            size_source = "decal_size_world_fallback"
            size_multiplier = 1.0
        plane_rotation = unreal.Rotator(0.0, 0.0, 0.0)
        plane_scale = unreal.Vector(plane_width / 100.0, plane_height / 100.0, 1.0)
        return surface_location, plane_rotation, plane_scale, {
            "depth": depth,
            "decal_width": decal_width,
            "decal_height": decal_height,
            "width": plane_width,
            "height": plane_height,
            "size_source": size_source,
            "size_multiplier": size_multiplier,
            "world_scale": (component_scale.x, component_scale.y, component_scale.z),
        }

    def _get_decal_component_world_scale(self, actor, decal_component):
        try:
            scale = decal_component.get_world_scale()
            if scale is not None:
                return scale
        except Exception:
            pass
        try:
            scale = decal_component.relative_scale3d()
            actor_scale = actor.get_actor_scale3d()
            return unreal.Vector(
                float(scale.x) * float(actor_scale.x),
                float(scale.y) * float(actor_scale.y),
                float(scale.z) * float(actor_scale.z),
            )
        except Exception:
            return actor.get_actor_scale3d()

    def _get_decal_component_surface_axes(self, actor, decal_component):
        try:
            return decal_component.get_right_vector(), decal_component.get_up_vector()
        except Exception:
            source_rotation = actor.get_actor_rotation()
            return unreal.MathLibrary.get_right_vector(source_rotation), unreal.MathLibrary.get_up_vector(source_rotation)

    def _get_decal_bounds_plane_size(self, actor):
        try:
            _origin, extent = actor.get_actor_bounds(False, True)
            width = abs(float(extent.x)) * 2.0
            height = abs(float(extent.y)) * 2.0
            if width >= 1.0 and height >= 1.0:
                return width, height, "actor_bounds"
        except Exception as e:
            unreal.log_warning(f"SceneTools: 读取 DecalActor Bounds 失败 {self._safe_actor_name(actor)} - {str(e)}")
        return None, None, "decal_size_projection"

    def _estimate_zero_rotation_plane_size(self, decal_right, decal_up, decal_width, decal_height):
        width_axis = self._scale_vector(decal_right, decal_width)
        height_axis = self._scale_vector(decal_up, decal_height)

        plane_width = abs(float(width_axis.x)) + abs(float(height_axis.x))
        plane_height = abs(float(width_axis.y)) + abs(float(height_axis.y))

        if plane_width < 1.0 or plane_height < 1.0:
            return decal_width, decal_height
        return max(plane_width, 1.0), max(plane_height, 1.0)

    def _make_plane_rotation_from_decal_axes(self, source_rotation, decal_right, decal_up):
        try:
            return unreal.MathLibrary.make_rot_from_xy(decal_right, self._negate_vector(decal_up))
        except Exception:
            try:
                return unreal.MathLibrary.compose_rotators(source_rotation, unreal.Rotator(0.0, 90.0, 0.0))
            except Exception:
                return source_rotation

    def _scale_vector(self, vector, scale):
        return unreal.Vector(float(vector.x) * scale, float(vector.y) * scale, float(vector.z) * scale)

    def _add_vectors(self, first, second):
        return unreal.Vector(float(first.x) + float(second.x), float(first.y) + float(second.y), float(first.z) + float(second.z))

    def _negate_vector(self, vector):
        return unreal.Vector(-float(vector.x), -float(vector.y), -float(vector.z))

    def _make_decal_plane_label(self, actor, suffix):
        try:
            base_name = actor.get_actor_label(True)
        except Exception:
            base_name = self._safe_actor_name(actor)
        return f"{base_name}{suffix}"

    def _format_decal_to_plane_preview(self, plan, summary):
        lines = []
        lines.append("=== Decal To Plane Preview ===")
        lines.append(
            f"Convert: {summary['ready']} | Skip: {summary['skipped']} | Error: {summary['errors']} | Total: {summary['total']}"
        )
        lines.append("")

        if not plan:
            lines.append("No selected actors.")
            return "\n".join(lines)

        max_rows = 120
        for index, item in enumerate(plan[:max_rows], 1):
            if item["action"] == "convert":
                size = item["decal_size"]
                scale = item["scale"]
                dimensions = item["dimensions"]
                lines.append(
                    f"{index:03d}. [CONVERT] {item['name']} -> {item['label']}  decalSize=({size.x:.2f}, {size.y:.2f}, {size.z:.2f})  planeWH=({dimensions['width']:.2f}, {dimensions['height']:.2f})  sizeSource={dimensions.get('size_source', 'unknown')}  sizeMul={dimensions.get('size_multiplier', 1.0):.1f}  scale=({scale.x:.2f}, {scale.y:.2f}, {scale.z:.2f})  rotation=(0,0,0)  material={item['material_name']} [{item.get('material_mode', 'none')}]"
                )
            elif item["action"] == "skip":
                lines.append(f"{index:03d}. [SKIP] {item['name']}  {item.get('reason', '')}")
            else:
                lines.append(f"{index:03d}. [ERR] {item['name']}  {item.get('reason', '')}")

        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... {len(plan) - max_rows} more rows omitted")

        return "\n".join(lines)

    def _format_decal_to_plane_report(self, report):
        lines = []
        lines.append("=== Last Decal To Plane Execution ===")
        lines.append(
            f"Created: {report['created']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total: {report['total']}"
        )
        lines.append("")

        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            scale = snapshot["scale"]
            dimensions = snapshot.get("dimensions", {})
            hidden_text = " hidden_source=True" if snapshot.get("hidden_source") else ""
            material_text = "applied" if snapshot.get("material_applied") else "not-applied"
            note_text = f" note={snapshot.get('material_note')}" if snapshot.get("material_note") else ""
            lines.append(
                f"{index:03d}. [CREATED] {snapshot['source']} -> {snapshot['created']}  sourceMat={snapshot.get('source_material', '<None>')}  planeMat={snapshot['material']} [{snapshot.get('material_mode', 'none')}] ({material_text})  planeWH=({dimensions.get('width', 0.0):.2f}, {dimensions.get('height', 0.0):.2f})  sizeSource={dimensions.get('size_source', 'unknown')}  sizeMul={dimensions.get('size_multiplier', 1.0):.1f}  scale=({scale[0]:.2f}, {scale[1]:.2f}, {scale[2]:.2f}){hidden_text}{note_text}"
            )

        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more created rows omitted")

        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")

        return "\n".join(lines)

    def _build_align_distribution_plan(self, actors, mode):
        axis_names = self._read_align_axes()
        step = self._get_float_from_ui("input_align_step", 100.0)
        plan = []

        if len(actors) < 2:
            actor_name = self._safe_actor_name(actors[0]) if actors else "<None>"
            plan.append({
                "action": "error",
                "actor": actors[0] if actors else None,
                "name": actor_name,
                "reason": "至少需要选择 2 个 Actor",
            })
            return plan, self._summarize_align_distribution_plan(plan)

        try:
            if mode == "align":
                plan = self._build_align_to_first_plan(actors, axis_names)
            elif mode == "distribute":
                plan = self._build_distribute_even_plan(actors, axis_names)
            elif mode == "array":
                plan = self._build_array_by_step_plan(actors, axis_names, step)
            else:
                plan.append({"action": "error", "actor": None, "name": "<Mode>", "reason": f"未知模式：{mode}"})
        except Exception as e:
            plan.append({"action": "error", "actor": None, "name": "<Plan>", "reason": str(e)})

        return plan, self._summarize_align_distribution_plan(plan)

    def _build_align_to_first_plan(self, actors, axis_names):
        reference_location = actors[0].get_actor_location()
        target_axis_values = self._get_vector_axis_values(reference_location, axis_names)
        plan = []
        for actor in actors:
            plan.append(self._build_actor_move_item(actor, axis_names, target_axis_values, "align"))
        return plan

    def _build_distribute_even_plan(self, actors, axis_names):
        primary_axis = axis_names[0]
        ordered_actors = sorted(actors, key=lambda actor: self._get_vector_axis_value(actor.get_actor_location(), primary_axis))
        first_values = self._get_vector_axis_values(ordered_actors[0].get_actor_location(), axis_names)
        last_values = self._get_vector_axis_values(ordered_actors[-1].get_actor_location(), axis_names)
        steps = {}
        for axis_name in axis_names:
            if len(ordered_actors) == 1:
                steps[axis_name] = 0.0
            else:
                steps[axis_name] = (last_values[axis_name] - first_values[axis_name]) / float(len(ordered_actors) - 1)

        plan = []
        for index, actor in enumerate(ordered_actors):
            target_axis_values = {}
            for axis_name in axis_names:
                target_axis_values[axis_name] = first_values[axis_name] + steps[axis_name] * index
            plan.append(self._build_actor_move_item(actor, axis_names, target_axis_values, "distribute"))
        return plan

    def _build_array_by_step_plan(self, actors, axis_names, step):
        start_location = actors[0].get_actor_location()
        start_values = self._get_vector_axis_values(start_location, axis_names)
        plan = []
        for index, actor in enumerate(actors):
            target_axis_values = {}
            for axis_name in axis_names:
                target_axis_values[axis_name] = start_values[axis_name] + step * index
            plan.append(self._build_actor_move_item(actor, axis_names, target_axis_values, "array"))
        return plan

    def _build_actor_move_item(self, actor, axis_names, target_axis_values, mode):
        actor_name = self._safe_actor_name(actor)
        try:
            old_location = actor.get_actor_location()
            old_axis_values = self._get_vector_axis_values(old_location, axis_names)
            new_location = self._copy_vector_with_axes(old_location, target_axis_values)
            deltas = {}
            action = "ok"
            for axis_name in axis_names:
                deltas[axis_name] = target_axis_values[axis_name] - old_axis_values[axis_name]
                if abs(deltas[axis_name]) > 0.01:
                    action = "move"
            return {
                "action": action,
                "actor": actor,
                "name": actor_name,
                "mode": mode,
                "axis": "/".join(axis_names),
                "axes": list(axis_names),
                "old_location": old_location,
                "new_location": new_location,
                "old_axis_values": old_axis_values,
                "new_axis_values": dict(target_axis_values),
                "deltas": deltas,
                "reason": "" if action == "move" else "无变化",
            }
        except Exception as e:
            return {"action": "error", "actor": actor, "name": actor_name, "reason": str(e)}

    def _summarize_align_distribution_plan(self, plan):
        summary = {"total": len(plan), "changes": 0, "unchanged": 0, "errors": 0}
        for item in plan:
            if item["action"] == "move":
                summary["changes"] += 1
            elif item["action"] == "ok":
                summary["unchanged"] += 1
            elif item["action"] == "error":
                summary["errors"] += 1
        return summary

    def _execute_align_distribution_plan(self, plan, summary, mode):
        move_items = [item for item in plan if item["action"] == "move"]
        report = self._create_align_distribution_report(plan, summary)

        if not move_items:
            return report

        action_name = f"SceneTools Align Distribute ({mode}, {len(move_items)} Actors)"
        self._apply_align_distribution_transaction(move_items, report, action_name)
        return report

    def _create_align_distribution_report(self, plan, summary):
        report = {
            "total": summary["changes"],
            "changed": 0,
            "skipped": summary["unchanged"],
            "failed": summary["errors"],
            "snapshots": [],
            "failures": [],
        }
        for item in plan:
            if item["action"] == "error":
                report["failures"].append({"name": item["name"], "reason": item.get("reason", "")})
        return report

    def _apply_align_distribution_transaction(self, move_items, report, action_name):
        changed_before = report["changed"]
        snapshot_count_before = len(report["snapshots"])
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_align_distribution_items(move_items, report)
        except Exception as e:
            if report["changed"] == changed_before and len(report["snapshots"]) == snapshot_count_before:
                report["failed"] += len(move_items)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
                unreal.log_warning(f"SceneTools: 对齐/分布事务创建失败，已取消执行 - {str(e)}")
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
                unreal.log_warning(f"SceneTools: 对齐/分布事务结束异常，已保留当前执行结果 - {str(e)}")

    def _start_align_distribution_frame_task(self, selected_actors, plan, summary, mode):
        move_items = [item for item in plan if item["action"] == "move"]
        if len(move_items) <= _FRAME_TASK_CHUNK_SIZE:
            return False
        if self._frame_task is not None:
            msg = "已有分帧任务正在执行，请等待当前任务完成后再执行。"
            self.data.set_text("txt_status", msg)
            unreal.log_warning(f"SceneTools: {msg}")
            return True

        self._frame_task = {
            "kind": "align_distribution",
            "actors": list(selected_actors),
            "mode": mode,
            "plan": plan,
            "summary": summary,
            "move_items": move_items,
            "index": 0,
            "report": self._create_align_distribution_report(plan, summary),
        }
        if not self._register_frame_tick():
            self._frame_task = None
            return False

        msg = f"对齐/分布分帧执行开始：每帧处理 {_FRAME_TASK_CHUNK_SIZE} 个，待移动 {len(move_items)} 个。"
        self.data.set_text("txt_status", msg)
        self.data.set_text("txt_align_preview", self._format_align_distribution_preview(plan, summary, mode) + "\n\n" + msg)
        unreal.log(f"SceneTools: {msg}")
        return True

    def _process_align_distribution_frame_task(self, task):
        move_items = task["move_items"]
        start_index = task["index"]
        end_index = min(start_index + _FRAME_TASK_CHUNK_SIZE, len(move_items))
        chunk = move_items[start_index:end_index]
        action_name = f"SceneTools Align Distribute Frame ({start_index + 1}-{end_index}/{len(move_items)})"
        self._apply_align_distribution_transaction(chunk, task["report"], action_name)
        task["index"] = end_index

        if end_index >= len(move_items):
            self._finish_align_distribution_frame_task(task)
            return

        msg = f"对齐/分布分帧执行中：{end_index}/{len(move_items)} 已处理。"
        self.data.set_text("txt_status", msg)

    def _finish_align_distribution_frame_task(self, task):
        report = task["report"]
        selected_actors = task["actors"]
        mode = task["mode"]
        self._last_align_distribution_report = report

        msg = (
            f"对齐/分布分帧执行完成：移动 {report['changed']}，跳过 {report['skipped']}，"
            f"失败 {report['failed']}，共 {report['total']}。"
        )
        self.data.set_text("txt_status", msg)
        unreal.log(f"SceneTools: {msg}")

        refreshed_plan, refreshed_summary = self._build_align_distribution_plan(selected_actors, mode)
        self._last_align_distribution_plan = refreshed_plan
        preview_text = self._format_align_distribution_preview(refreshed_plan, refreshed_summary, mode)
        self.data.set_text("txt_align_preview", preview_text + "\n\n" + self._format_align_distribution_report(report))

        self._frame_task = None
        self._unregister_frame_tick()

    def _apply_align_distribution_items(self, move_items, report):
        for item in move_items:
            actor = item["actor"]
            try:
                if not self._mark_actor_transform_for_undo(actor, item["name"]):
                    report["failed"] += 1
                    report["failures"].append({
                        "name": item["name"],
                        "reason": "modify() 失败，已跳过以避免不可撤销修改",
                    })
                    continue
                actor.set_actor_location(item["new_location"], False, False)
                report["changed"] += 1
                report["snapshots"].append({
                    "name": item["name"],
                    "axis": item["axis"],
                    "axes": item["axes"],
                    "mode": item["mode"],
                    "old_axis_values": item["old_axis_values"],
                    "new_axis_values": item["new_axis_values"],
                    "deltas": item["deltas"],
                })
            except Exception as e:
                report["failed"] += 1
                report["failures"].append({"name": item["name"], "reason": str(e)})
                unreal.log_warning(f"SceneTools: 对齐/分布移动失败 {item['name']} - {str(e)}")

    def _format_align_distribution_preview(self, plan, summary, mode):
        lines = []
        lines.append(f"=== Align / Distribute Preview ({mode}) ===")
        lines.append(
            f"Move: {summary['changes']} | OK: {summary['unchanged']} | Error: {summary['errors']} | Total: {summary['total']}"
        )
        lines.append("")

        if not plan:
            lines.append("No selected actors.")
            return "\n".join(lines)

        max_rows = 120
        for index, item in enumerate(plan[:max_rows], 1):
            if item["action"] == "move":
                lines.append(
                    f"{index:03d}. [MOVE] {item['name']}  {self._format_axis_changes(item['axes'], item['old_axis_values'], item['new_axis_values'], item['deltas'])}"
                )
            elif item["action"] == "ok":
                lines.append(f"{index:03d}. [OK]   {item['name']}  {item.get('reason', '')}")
            else:
                lines.append(f"{index:03d}. [ERR]  {item['name']}  {item.get('reason', '')}")

        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... {len(plan) - max_rows} more rows omitted")

        return "\n".join(lines)

    def _format_align_distribution_report(self, report):
        lines = []
        lines.append("=== Last Align / Distribute Execution ===")
        lines.append(
            f"Changed: {report['changed']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total: {report['total']}"
        )
        lines.append("")

        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            lines.append(
                f"{index:03d}. [MOVED] {snapshot['name']}  {self._format_axis_changes(snapshot['axes'], snapshot['old_axis_values'], snapshot['new_axis_values'], snapshot['deltas'])}"
            )

        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more moved rows omitted")

        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")

        return "\n".join(lines)

    def _read_align_axes(self):
        axis_names = []
        for candidate in ("X", "Y", "Z"):
            if self._get_checkbox_checked(f"chk_align_axis_{candidate.lower()}"):
                axis_names.append(candidate)
        if not axis_names:
            axis_names.append("X")
            self._set_checkbox_checked("chk_align_axis_x", True)
        return axis_names

    def _any_align_axis_checked(self):
        return any(
            self._get_checkbox_checked(f"chk_align_axis_{candidate.lower()}")
            for candidate in ("X", "Y", "Z")
        )

    def _get_vector_axis_value(self, vector, axis_name):
        if axis_name == "X":
            return float(vector.x)
        if axis_name == "Y":
            return float(vector.y)
        return float(vector.z)

    def _get_vector_axis_values(self, vector, axis_names):
        values = {}
        for axis_name in axis_names:
            values[axis_name] = self._get_vector_axis_value(vector, axis_name)
        return values

    def _copy_vector_with_axis(self, vector, axis_name, axis_value):
        if axis_name == "X":
            return unreal.Vector(float(axis_value), vector.y, vector.z)
        if axis_name == "Y":
            return unreal.Vector(vector.x, float(axis_value), vector.z)
        return unreal.Vector(vector.x, vector.y, float(axis_value))

    def _copy_vector_with_axes(self, vector, axis_values):
        return unreal.Vector(
            float(axis_values.get("X", vector.x)),
            float(axis_values.get("Y", vector.y)),
            float(axis_values.get("Z", vector.z)),
        )

    def _format_axis_changes(self, axis_names, old_values, new_values, deltas):
        parts = []
        for axis_name in axis_names:
            parts.append(
                f"{axis_name}: {old_values[axis_name]:.2f} -> {new_values[axis_name]:.2f}  delta={deltas[axis_name]:.2f}"
            )
        return " | ".join(parts)

    def _get_actor_components_by_class(self, actor, component_class):
        try:
            components = actor.get_components_by_class(component_class)
            return list(components or [])
        except Exception as e:
            unreal.log_warning(f"SceneTools: 获取组件失败 {self._safe_actor_name(actor)} - {str(e)}")
            return []

    def _get_actor_hidden_in_game(self, actor):
        try:
            return bool(actor.hidden())
        except Exception:
            value = self._safe_get_editor_property(actor, "hidden")
            return bool(value) if value is not None else None

    def _get_component_hidden_in_game(self, component):
        try:
            return bool(component.hidden_in_game())
        except Exception:
            value = self._safe_get_editor_property(component, "hidden_in_game")
            return bool(value) if value is not None else None

    def _get_component_visible(self, component):
        try:
            return bool(component.is_visible())
        except Exception:
            value = self._safe_get_editor_property(component, "visible")
            return bool(value) if value is not None else None

    def _get_component_cast_shadow(self, component):
        try:
            return bool(component.cast_shadow())
        except Exception:
            value = self._safe_get_editor_property(component, "cast_shadow")
            return bool(value) if value is not None else None

    def _get_component_max_draw_distance(self, component):
        try:
            return float(component.ld_max_draw_distance())
        except Exception:
            value = self._safe_get_editor_property(component, "ld_max_draw_distance")
            return float(value) if value is not None else None

    def _get_component_receives_decals(self, component):
        try:
            return bool(component.receives_decals())
        except Exception:
            value = self._safe_get_editor_property(component, "receives_decals")
            return bool(value) if value is not None else None

    def _mark_object_for_undo(self, obj, object_name):
        try:
            if obj.modify() is False:
                unreal.log_warning(f"SceneTools: {object_name} modify 返回 False")
                return False
            return True
        except Exception as e:
            unreal.log_warning(f"SceneTools: {object_name} modify 失败 - {str(e)}")
            return False

    def _get_float_from_ui(self, aka, default_value, min_value=None):
        try:
            raw_value = str(self.data.get_text(aka)).strip()
            value = float(raw_value) if raw_value else float(default_value)
        except Exception:
            value = float(default_value)
        if min_value is not None and value < min_value:
            return float(min_value)
        return value

    def _safe_actor_name(self, actor):
        try:
            return actor.get_name()
        except Exception:
            return "<UnknownActor>"

    def _safe_object_name(self, obj):
        try:
            return obj.get_name()
        except Exception:
            try:
                return str(obj)
            except Exception:
                return "<UnknownObject>"

    def _resolve_current_level(self):
        try:
            level = unreal.EditorLevelLibrary.get_current_level()
            if level is not None:
                return level
        except Exception:
            pass

        try:
            world = unreal.EditorLevelLibrary.get_editor_world()
        except Exception:
            return None

        for prop_name in ("current_level", "persistent_level"):
            level = self._safe_get_editor_property(world, prop_name)
            if level is not None:
                return level

            try:
                level = getattr(world, prop_name)
                if level is not None:
                    return level
            except Exception:
                pass

        return None

    def _get_actor_level(self, actor):
        try:
            return actor.get_level()
        except Exception:
            pass

        level = self._safe_get_editor_property(actor, "level")
        if level is not None:
            return level

        try:
            return actor.get_outer()
        except Exception:
            return None

    def _safe_get_editor_property(self, obj, prop_name):
        try:
            return obj.get_editor_property(prop_name)
        except Exception:
            return None

    def _set_checkbox_checked(self, aka, checked):
        """设置复选框状态，兼容不同 TAPython 版本 API。"""
        try:
            self.data.set_is_checked(aka, checked)
            return
        except Exception:
            pass

        # 旧版 TAPython API（保留回退）
        self.data.set_check_boxe_is_checked(aka, checked)

    def _get_checkbox_checked(self, aka):
        try:
            return bool(self.data.get_is_checked(aka))
        except Exception:
            pass

        try:
            state = self.data.get_checkbox_state(aka)
            if isinstance(state, str):
                return state.lower() in ("checked", "true", "1")
            return bool(state)
        except Exception:
            return False

    def _set_list_view_items(self, aka, items):
        for method_name in ("set_list_view_items", "set_list_items"):
            fn = getattr(self.data, method_name, None)
            if fn is None:
                continue
            try:
                fn(aka, list(items))
                return True
            except Exception as e:
                unreal.log_warning(f"SceneTools _set_list_view_items {method_name}: {str(e)}")
        return False

    def _get_list_view_selected_indexes(self, aka):
        fn = getattr(self.data, "get_list_view_items", None)
        if fn is None:
            return []
        try:
            ret = fn(aka)
            if isinstance(ret, tuple) and len(ret) >= 2 and ret[1] is not None:
                indexes = []
                for index in ret[1]:
                    try:
                        indexes.append(int(index))
                    except Exception:
                        continue
                return indexes
        except Exception as e:
            unreal.log_warning(f"SceneTools _get_list_view_selected_indexes: {str(e)}")
        return []

    def _get_single_list_view_selected_index(self, aka, fallback_index=None):
        indexes = self._get_list_view_selected_indexes(aka)
        if indexes:
            return indexes[0]
        try:
            if fallback_index is not None:
                return int(fallback_index)
        except Exception:
            pass
        return -1

    def _set_list_view_selection(self, aka, indexes):
        fn = getattr(self.data, "set_list_view_selections", None)
        if fn is None:
            return False
        try:
            fn(aka, list(indexes))
            return True
        except Exception as e:
            unreal.log_warning(f"SceneTools _set_list_view_selection: {str(e)}")
            return False

    def _coerce_checkbox_value(self, value):
        if isinstance(value, str):
            return value.strip().lower() in ("checked", "true", "1")
        return bool(value)

    def _set_actor_editor_visibility(self, actor, visible):
        """设置 Actor 在编辑器中的可见性，兼容不同 UE5 Python 绑定。"""
        hidden = not visible

        # 优先使用编辑器临时隐藏接口
        try:
            actor.set_is_temporarily_hidden_in_editor(hidden)
            return True
        except Exception:
            pass

        # 次选：通用 Actor 隐藏接口
        try:
            actor.set_actor_hidden(hidden)
            return True
        except Exception:
            pass

        # 最后回退：编辑器属性设置
        for prop_name in ("is_temporarily_hidden_in_editor", "is_hidden_ed"):
            try:
                actor.set_editor_property(prop_name, hidden)
                return True
            except Exception:
                continue

        unreal.log_warning(f"SceneTools: Actor {actor.get_name()} 不支持可见性切换。")
        return False

    def _matches_type(self, actor, target_classes, check_blueprint):
        """判断 actor 是否属于目标类型之一。"""
        # Blueprint 实例：类名以 _C 结尾（UE5 蓝图派生类命名惯例）
        if check_blueprint and actor.get_class().get_name().endswith("_C"):
            return True
        # isinstance 匹配各原生类型
        for cls in target_classes:
            if isinstance(actor, cls):
                return True
        return False


# 模块级单例
def on_close():
    if instance is not None:
        instance.on_closed()


instance = None
