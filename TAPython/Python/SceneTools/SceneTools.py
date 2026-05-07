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
        self._last_align_distribution_plan = []
        self._last_align_distribution_report = {}
        self._align_axis_updating = False
        self._frame_tick_handle = None
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
    # Visibility 功能：批量隐藏 / 显示
    # ------------------------------------------------------------------

    def execute_hide(self):
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            selected_actors = actor_subsystem.get_selected_level_actors()

            if not selected_actors:
                self.data.set_text("txt_status", "提示：没有选中的物件。")
                return

            hidden_count = 0
            for actor in selected_actors:
                try:
                    if self._set_actor_editor_visibility(actor, False):
                        hidden_count += 1
                except Exception as e:
                    unreal.log_warning(f"SceneTools: 隐藏 Actor {actor.get_name()} 失败 - {str(e)}")

            msg = f"已隐藏 {hidden_count} / {len(selected_actors)} 个物件。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")

        except Exception as e:
            error_msg = f"隐藏失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_hide: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_show(self):
        try:
            actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            selected_actors = actor_subsystem.get_selected_level_actors()

            if not selected_actors:
                self.data.set_text("txt_status", "提示：没有选中的物件。")
                return

            shown_count = 0
            for actor in selected_actors:
                try:
                    if self._set_actor_editor_visibility(actor, True):
                        shown_count += 1
                except Exception as e:
                    unreal.log_warning(f"SceneTools: 显示 Actor {actor.get_name()} 失败 - {str(e)}")

            msg = f"已显示 {shown_count} / {len(selected_actors)} 个物件。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")

        except Exception as e:
            error_msg = f"显示失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_show: {error_msg}")
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

            updated = 0
            for actor in selected_actors:
                try:
                    if self._apply_actor_transform_mode(actor, mode):
                        updated += 1
                except Exception as e:
                    unreal.log_warning(f"SceneTools: 重置变换失败 {actor.get_name()} - {str(e)}")

            mode_label = {
                "location": "位置归零",
                "rotation": "旋转归零",
                "scale": "缩放归一",
                "all": "全变换重置",
            }.get(mode, mode)
            msg = f"{mode_label}完成：{updated} / {len(selected_actors)}"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"重置变换失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_reset_transform: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_apply_layer_group(self):
        """将图层与分组应用到已选 Actor（Tag 由专用「设置 Tag」按钮负责）。"""
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            layer_name = str(self.data.get_text("input_layer")).strip()
            group_name = str(self.data.get_text("input_group")).strip()
            if not layer_name and not group_name:
                self.data.set_text("txt_status", "提示：请至少填写图层或分组名称。")
                return

            layer_applied = 0
            group_applied = 0

            for actor in selected_actors:
                try:
                    if layer_name and self._apply_layer_to_actor(actor, layer_name):
                        layer_applied += 1

                    if group_name and self._apply_group_to_actor(actor, group_name):
                        group_applied += 1

                except Exception as e:
                    unreal.log_warning(f"SceneTools: 应用图层/分组失败 {actor.get_name()} - {str(e)}")

            msg = f"应用完成：图层 {layer_applied}，分组 {group_applied}，对象 {len(selected_actors)}。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"应用图层/分组失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_apply_layer_group: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_clear_group(self):
        try:
            selected_actors = self._get_selected_actors_or_warn()
            if not selected_actors:
                return

            cleared = 0
            for actor in selected_actors:
                try:
                    actor.set_folder_path("")
                    cleared += 1
                except Exception as e:
                    unreal.log_warning(f"SceneTools: 清除分组失败 {actor.get_name()} - {str(e)}")

            msg = f"已清除分组：{cleared} / {len(selected_actors)}"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"清除分组失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_clear_group: {error_msg}")
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

        actor.set_actor_location(location, False, False)
        actor.set_actor_rotation(rotation, False)
        actor.set_actor_scale3d(scale)
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
        if self._frame_tick_handle is not None:
            return True
        try:
            self._frame_tick_handle = unreal.register_slate_post_tick_callback(self._on_frame_tick)
            return True
        except Exception as e:
            unreal.log_warning(f"SceneTools: Slate tick 注册失败，回退同步执行 - {str(e)}")
            return False

    def _unregister_frame_tick(self):
        if self._frame_tick_handle is None:
            return
        try:
            unreal.unregister_slate_post_tick_callback(self._frame_tick_handle)
        except Exception as e:
            unreal.log_warning(f"SceneTools: Slate tick 注销失败 - {str(e)}")
        finally:
            self._frame_tick_handle = None

    def _on_frame_tick(self, _delta_time):
        try:
            if self._frame_task is None:
                self._unregister_frame_tick()
                return
            if self._frame_task.get("kind") == "ground_snap":
                self._process_ground_snap_frame_task(self._frame_task)
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
            if actor.modify() is False:
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
                root_component.modify()
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

        if not changes:
            return report

        action_name = f"SceneTools Render Properties ({len(changes)} Changes)"
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_render_property_changes(changes, report)
        except Exception as e:
            if report["changed"] == 0 and not report["snapshots"]:
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
        report["skipped"] = max(0, report["total"] - report["changed"] - report["failed"])
        return report

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

        if not move_items:
            return report

        action_name = f"SceneTools Align Distribute ({mode}, {len(move_items)} Actors)"
        try:
            with unreal.ScopedEditorTransaction(action_name):
                self._apply_align_distribution_items(move_items, report)
        except Exception as e:
            if report["changed"] == 0 and not report["snapshots"]:
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
        return report

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

    def _apply_layer_to_actor(self, actor, layer_name):
        # 优先尝试静态库 API
        try:
            unreal.LayersBlueprintLibrary.add_actor_to_layer(actor, layer_name)
            return True
        except Exception:
            pass

        # 回退到 LayersSubsystem
        try:
            layers_subsystem = unreal.get_editor_subsystem(unreal.LayersSubsystem)
            layers_subsystem.add_actor_to_layer(actor, layer_name)
            return True
        except Exception:
            unreal.log_warning(f"SceneTools: 图层接口不可用，跳过 {actor.get_name()} -> {layer_name}")
            return False

    def _apply_group_to_actor(self, actor, group_name):
        # 以 Outliner 文件夹路径作为轻量分组方式
        try:
            actor.set_folder_path(group_name)
            return True
        except Exception:
            unreal.log_warning(f"SceneTools: 分组接口不可用，跳过 {actor.get_name()} -> {group_name}")
            return False

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
