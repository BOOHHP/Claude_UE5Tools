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

        # True = 所有关卡，False = 当前关卡（Python 端维护状态，不回读 UI）
        self.scope_all = False
        # 防止 set_checkbox_state 触发 OnCheckStateChanged 引起回调循环
        self._scope_updating = False

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
