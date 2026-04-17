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

        # Tag 动态列表状态（_tag_count 为当前显示行数，最多 _TAG_MAX 行）
        self._TAG_MAX = 8
        self._tag_count = 0
        self._tag_mode = "indexed"  # indexed | mixed

        # 选中状态监听：通过 Slate tick 回调实时检测选择变化
        self._selection_hash = self._compute_selection_hash()
        self._tick_frame_counter = 0
        self._tick_interval = 15  # 约每 15 帧检测一次（~0.25s@60fps）
        self._tick_handle = None
        self._initial_sync_done = False  # 第一个 tick 强制同步（UI 尚未就绪时调用 set_visible 无效）
        try:
            self._tick_handle = unreal.register_slate_post_tick_callback(
                self._on_tick_check_selection
            )
        except Exception as e:
            unreal.log_warning(f"SceneTools: Slate tick 注册失败，需手动刷新 Tag: {str(e)}")

    # ------------------------------------------------------------------
    # 选中状态实时监听
    # ------------------------------------------------------------------

    def _on_tick_check_selection(self, delta_time):
        """Slate tick 回调，节流检测选中 Actor 变化自动刷新 Tag 面板。"""
        self._tick_frame_counter += 1
        if self._tick_frame_counter < self._tick_interval:
            return
        self._tick_frame_counter = 0

        try:
            # 第一次 tick：UI 已完成渲染，强制全量同步一次再去隐藏多余行
            if not self._initial_sync_done:
                self._initial_sync_done = True
                self._selection_hash = self._compute_selection_hash()
                self.sync_tag_ui_from_selection()
                return

            new_hash = self._compute_selection_hash()
            if new_hash != self._selection_hash:
                self._selection_hash = new_hash
                self.sync_tag_ui_from_selection()
        except Exception:
            pass

    def _compute_selection_hash(self):
        """计算当前选中 Actor 及其 Tag 的快速哈希，用于变化检测。"""
        try:
            selected = self._get_selected_actors()
            if not selected:
                return 0
            parts = []
            for a in selected:
                name = a.get_name()
                tags = ",".join(str(t) for t in getattr(a, "tags", []))
                parts.append(f"{name}:{tags}")
            parts.sort()
            return hash("|".join(parts))
        except Exception:
            return -1

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

    def add_tag_row(self):
        if self._tag_mode == "mixed":
            # mixed 模式：切换为 indexed 空列表，用户从头统一编辑
            self._tag_mode = "indexed"
            self._tag_count = 0
            self._fill_tag_rows([])
        if self._tag_count >= self._TAG_MAX:
            self.data.set_text("txt_status", f"最多支持 {self._TAG_MAX} 个 Tag。")
            return
        self._tag_count += 1
        self._refresh_tag_ui()

    def remove_tag_row(self, i):
        if self._tag_mode == "mixed" or i < 0 or i >= self._tag_count:
            return
        vals = [str(self.data.get_text(f"tag_val_{j}")) for j in range(self._tag_count)]
        vals.pop(i)
        self._tag_count -= 1
        self._fill_tag_rows(vals)
        self._refresh_tag_ui()

    def execute_sync_tag_state(self):
        self.sync_tag_ui_from_selection()

    def sync_tag_ui_from_selection(self):
        """按 UE 行为同步 Tag 展示：单选/多选一致显示索引；多选不一致显示“多个值”。"""
        try:
            selected = self._get_selected_actors()
            if not selected:
                self._tag_mode = "indexed"
                self._tag_count = 0
                self._fill_tag_rows([])
                self._refresh_tag_ui()
                return

            all_tag_lists = [self._get_actor_tags(a) for a in selected]
            first = all_tag_lists[0]
            all_same = all(t == first for t in all_tag_lists[1:])

            if all_same:
                self._tag_mode = "indexed"
                self._tag_count = min(len(first), self._TAG_MAX)
                self._fill_tag_rows(first)
                if len(first) > self._TAG_MAX:
                    self.data.set_text("txt_status",
                        f"Tag 数量超过 {self._TAG_MAX}，仅展示前 {self._TAG_MAX} 项。")
            else:
                self._tag_mode = "mixed"
                self._tag_count = 0
                self._fill_tag_rows([])

            self._refresh_tag_ui()
        except Exception as e:
            unreal.log_warning(f"SceneTools sync_tag_ui_from_selection: {str(e)}")

    def execute_set_tags_to_actors(self):
        """将面板 Tag 列表完整替换写入已选 Actor（Replace-All，对齐 UE5）。"""
        try:
            selected = self._get_selected_actors_or_warn()
            if not selected:
                return

            if self._tag_mode == "mixed":
                self.data.set_text("txt_status",
                    "Tag 不一致：请先点击「读取 Tag 状态」或「清空全部 Tag」。")
                return

            new_tags = self._collect_tag_values()
            applied = 0
            for actor in selected:
                if self._set_actor_tags(actor, new_tags):
                    applied += 1

            self.sync_tag_ui_from_selection()
            msg = f"Tag 已写入：{applied}/{len(selected)} 个 Actor，{len(new_tags)} 个 Tag。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"设置 Tag 失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_set_tags_to_actors: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_clear_tags_all(self):
        """清除已选 Actor 的全部 Tag 并刷新面板。"""
        try:
            selected = self._get_selected_actors_or_warn()
            if not selected:
                return

            cleared = 0
            for actor in selected:
                if self._set_actor_tags(actor, []):
                    cleared += 1

            self.sync_tag_ui_from_selection()
            msg = f"已清除 Tag：{cleared}/{len(selected)} 个 Actor。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"SceneTools: {msg}")
        except Exception as e:
            error_msg = f"清除 Tag 失败：{str(e)}"
            unreal.log_error(f"SceneTools execute_clear_tags_all: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def _refresh_tag_ui(self):
        """更新数量标签、mixed 提示行、各索引行 show/hide。"""
        try:
            selected_count = len(self._get_selected_actors())
            if self._tag_mode == "mixed":
                self.data.set_text("tag_count_label", "多个值")
            else:
                self.data.set_text("tag_count_label", f"{self._tag_count} 数组元素")

            try:
                if self._tag_mode == "mixed":
                    self.data.set_text("tag_mixed_hint", "多个 Actor 的 Tag 不一致（多个值）")
                else:
                    self.data.set_text("tag_mixed_hint", "")
            except Exception:
                pass

            self.data.set_enabled("btn_clear_tags_all", selected_count > 0)

            for i in range(self._TAG_MAX):
                visible = (self._tag_mode == "indexed") and (i < self._tag_count)
                self.data.set_visible(f"tag_row_{i}", visible)
                if visible:
                    self.data.set_text(f"tag_idx_{i}", f"索引[{i}]")
        except Exception as e:
            unreal.log_warning(f"SceneTools _refresh_tag_ui: {str(e)}")

    def _collect_tag_values(self):
        """读取所有可见 Tag 行的非空文本，返回列表。"""
        result = []
        for i in range(self._tag_count):
            v = str(self.data.get_text(f"tag_val_{i}")).strip()
            if v:
                result.append(v)
        return result

    def _collect_tags_from_ui(self):
        return self._collect_tag_values()

    def _fill_tag_rows(self, tags):
        """将 tags 写入 UI 各行（超出部分清空），不修改 _tag_count。"""
        for i in range(self._TAG_MAX):
            self.data.set_text(f"tag_val_{i}", tags[i] if i < len(tags) else "")

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

    def execute_apply_tags_layers(self):
        self.execute_apply_layer_group()

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

    def on_panel_expansion_changed(self, _is_expanded):
        self.sync_tag_ui_from_selection()
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

    def _get_actor_tags(self, actor):
        return [str(tag) for tag in getattr(actor, "tags", [])]

    def _set_actor_tags(self, actor, tags):
        """用 tags 列表完整替换 actor 的标签（replace-all 语义）。"""
        tag_names = [unreal.Name(t) for t in tags]
        try:
            actor.tags = tag_names
            return True
        except Exception:
            pass
        try:
            actor.set_editor_property("tags", tag_names)
            return True
        except Exception:
            unreal.log_warning(f"SceneTools: 无法设置 {actor.get_name()} 的 Tag")
            return False

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

    def _add_tag_to_actor(self, actor, tag_text):
        current_tags = [str(tag) for tag in getattr(actor, "tags", [])]
        if tag_text in current_tags:
            return False

        try:
            actor.tags.append(unreal.Name(tag_text))
            return True
        except Exception:
            pass

        # 兼容回退：通过 editor_property 重写 tags
        try:
            merged = list(current_tags)
            merged.append(tag_text)
            actor.set_editor_property("tags", merged)
            return True
        except Exception:
            unreal.log_warning(f"SceneTools: 无法给 {actor.get_name()} 添加 Tag: {tag_text}")
            return False

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
instance = None
