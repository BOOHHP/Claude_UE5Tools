"""
BatchTagTool — 批量 Actor Tag 管理器（SDetailsView 原生数组编辑版）

设计思路（参考《Tag工具修改.md》方案）：
    1. 定义虚拟 UObject 代理（BatchTagProxy），只含一个 `edit_tags: Array<Name>` 属性
    2. 在 Chameleon 中放 SDetailsView，通过 set_object 绑定代理对象
    3. 原生 UE 数组编辑器接管 UI —— 加号、删除、拖拽排序、右键菜单完全原生体验
    4. 选中 Actor 变化时自动计算交集写回代理（SDetailsView 随即刷新）
    5. 用户在列表编辑完毕后点击「增量合并」或「完全覆盖」应用到已选 Actor
    6. 所有写入操作包裹在 ScopedEditorTransaction 中，支持 Ctrl+Z 撤销

注意：
    - BatchTagProxy 必须从独立模块导入（见 BatchTagProxy.py），避免 InitPyCmd
      的 importlib.reload 导致 @uclass 重复注册
    - 必须用 self 强引用 new_object 返回的代理对象，否则 GC 会回收导致 UE 闪退
"""

import unreal

from BatchTagTool.BatchTagProxy import BatchTagProxy


class BatchTagToolController:
    """BatchTagTool 的 MVC Controller。"""

    _TICK_INTERVAL = 15  # 约 15 帧检测一次选中变化（~0.25s@60fps）

    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

        # ⚠️ 用 self 强引用防止 GC 回收代理对象（会导致 UE 闪退）
        self.tag_proxy = None
        try:
            self.tag_proxy = unreal.new_object(BatchTagProxy)
        except Exception as e:
            unreal.log_error(f"BatchTagTool: 创建代理对象失败: {str(e)}")

        # Slate tick 节流状态
        self._tick_frame_counter = 0
        self._tick_handle = None
        self._initial_sync_done = False
        self._selection_hash = 0

        # 首次绑定代理到 SDetailsView（延迟到首次 tick —— 此时 UI 已就绪）
        try:
            self._tick_handle = unreal.register_slate_post_tick_callback(self._on_tick)
        except Exception as e:
            unreal.log_warning(f"BatchTagTool: Slate tick 注册失败: {str(e)}")

    # ------------------------------------------------------------------
    # 生命周期
    # ------------------------------------------------------------------

    def on_closed(self):
        try:
            if self._tick_handle is not None:
                unreal.unregister_slate_post_tick_callback(self._tick_handle)
                self._tick_handle = None
        except Exception as e:
            unreal.log_warning(f"BatchTagTool on_closed: {str(e)}")

    # ------------------------------------------------------------------
    # Slate tick：自动检测选中变化
    # ------------------------------------------------------------------

    def _on_tick(self, _delta_time):
        self._tick_frame_counter += 1
        if self._tick_frame_counter < self._TICK_INTERVAL:
            return
        self._tick_frame_counter = 0

        try:
            if not self._initial_sync_done:
                self._initial_sync_done = True
                # 首帧：UI 就绪，绑定代理并同步一次
                self._bind_proxy_to_details_view()
                self._selection_hash = self._compute_selection_hash()
                self._sync_proxy_from_selection()
                return

            new_hash = self._compute_selection_hash()
            if new_hash != self._selection_hash:
                self._selection_hash = new_hash
                self._sync_proxy_from_selection()
        except Exception:
            pass

    def _bind_proxy_to_details_view(self):
        try:
            if self.tag_proxy is not None:
                self.data.set_object("details_tags", self.tag_proxy)
        except Exception as e:
            unreal.log_error(f"BatchTagTool _bind_proxy_to_details_view: {str(e)}")

    def _compute_selection_hash(self):
        try:
            selected = self._get_selected_actors()
            if not selected:
                return 0
            parts = []
            for a in selected:
                tags = ",".join(str(t) for t in getattr(a, "tags", []))
                parts.append(f"{a.get_name()}:{tags}")
            parts.sort()
            return hash("|".join(parts))
        except Exception:
            return -1

    # ------------------------------------------------------------------
    # 交集计算：选中变化 -> 代理对象
    # ------------------------------------------------------------------

    def _sync_proxy_from_selection(self):
        """读取已选 Actor 的 Tag 交集写入代理对象，SDetailsView 会自动刷新。"""
        try:
            selected = self._get_selected_actors()

            if not selected:
                self._set_proxy_tags([])
                self.data.set_text("text_selection_info", "当前未选中任何 Actor。")
                self.data.set_text("text_status", "就绪。选中 Actor 后将自动读取 Tag 交集到列表。")
                return

            tag_sets = [set(str(t) for t in getattr(a, "tags", [])) for a in selected]
            common = tag_sets[0].copy()
            for s in tag_sets[1:]:
                common &= s

            sorted_common = sorted(common)
            self._set_proxy_tags(sorted_common)

            info = f"已选中 {len(selected)} 个 Actor，共有 Tag {len(sorted_common)} 个（交集）。"
            self.data.set_text("text_selection_info", info)
            self.data.set_text("text_status", "已载入交集到上方列表。可编辑后点击下方按钮应用。")
        except Exception as e:
            unreal.log_warning(f"BatchTagTool _sync_proxy_from_selection: {str(e)}")

    def _set_proxy_tags(self, tag_strs):
        """安全地写入代理对象的 edit_tags 属性。"""
        if self.tag_proxy is None:
            return
        try:
            names = [unreal.Name(str(t)) for t in tag_strs]
            self.tag_proxy.set_editor_property("edit_tags", names)
        except Exception:
            # 回退：直接赋值
            try:
                self.tag_proxy.edit_tags = [unreal.Name(str(t)) for t in tag_strs]
            except Exception as e:
                unreal.log_warning(f"BatchTagTool _set_proxy_tags: {str(e)}")

    def _get_proxy_tags_as_strs(self):
        """读取代理对象当前的 Tag 列表（字符串数组）。"""
        if self.tag_proxy is None:
            return []
        try:
            raw = self.tag_proxy.get_editor_property("edit_tags")
        except Exception:
            try:
                raw = self.tag_proxy.edit_tags
            except Exception:
                return []
        return [str(t) for t in (raw or []) if str(t).strip()]

    # ------------------------------------------------------------------
    # 按钮回调
    # ------------------------------------------------------------------

    def on_apply_merge(self):
        self._apply_to_actors(override=False)

    def on_apply_override(self):
        self._apply_to_actors(override=True)

    def on_reload_intersection(self):
        try:
            self._selection_hash = self._compute_selection_hash()
            self._sync_proxy_from_selection()
        except Exception as e:
            unreal.log_error(f"BatchTagTool on_reload_intersection: {str(e)}")

    def on_clear_proxy(self):
        try:
            self._set_proxy_tags([])
            self.data.set_text("text_status", "列表已清空（未影响 Actor）。")
        except Exception as e:
            unreal.log_error(f"BatchTagTool on_clear_proxy: {str(e)}")

    # ------------------------------------------------------------------
    # 核心：将代理列表写回选中 Actor
    # ------------------------------------------------------------------

    def _apply_to_actors(self, override):
        try:
            selected = self._get_selected_actors()
            if not selected:
                self.data.set_text("text_status", "⚠️ 当前未选中任何 Actor。")
                return

            target_strs = self._get_proxy_tags_as_strs()
            target_names = [unreal.Name(t) for t in target_strs]

            action_name = "Override Actor Tags" if override else "Merge Actor Tags"
            changed = 0

            try:
                with unreal.ScopedEditorTransaction(action_name):
                    changed = self._write_target_tags(selected, target_names, override)
            except Exception as e:
                # Transaction 构造失败 -> 退化为无事务
                unreal.log_warning(f"BatchTagTool: Transaction 失败，回退无事务执行: {str(e)}")
                changed = self._write_target_tags(selected, target_names, override)

            mode_label = "完全覆盖" if override else "增量合并"
            msg = (
                f"✅ [{mode_label}] 完成：{changed}/{len(selected)} 个 Actor 有变更，"
                f"当前列表含 {len(target_strs)} 个 Tag。"
            )
            self.data.set_text("text_status", msg)
            unreal.log(f"BatchTagTool: {msg}")

            # 刷新交集（写回之后状态已变）
            self._selection_hash = self._compute_selection_hash()
            self._sync_proxy_from_selection()
        except Exception as e:
            error_msg = f"❌ 应用失败：{str(e)}"
            unreal.log_error(f"BatchTagTool _apply_to_actors: {error_msg}")
            self.data.set_text("text_status", error_msg)

    def _write_target_tags(self, selected, target_names, override):
        """对每个 Actor 执行 merge / override，返回实际有变更的数量。"""
        changed = 0
        for actor in selected:
            try:
                current = list(getattr(actor, "tags", []) or [])

                if override:
                    # 以字符串集合比较，避免 FName 与 str 的差异导致误判变更
                    if [str(t) for t in current] != [str(t) for t in target_names]:
                        self._commit_actor_tags(actor, target_names)
                        changed += 1
                else:
                    current_strs = [str(t) for t in current]
                    merged = list(current)
                    added = False
                    for t in target_names:
                        if str(t) not in current_strs:
                            merged.append(t)
                            current_strs.append(str(t))
                            added = True
                    if added:
                        self._commit_actor_tags(actor, merged)
                        changed += 1
            except Exception as e:
                unreal.log_warning(
                    f"BatchTagTool: Actor {actor.get_name()} 写入失败 - {str(e)}"
                )
        return changed

    def _commit_actor_tags(self, actor, tag_names):
        """登记 Undo 并写入 actor.tags。"""
        try:
            actor.modify()
        except Exception:
            pass
        try:
            actor.tags = tag_names
        except Exception:
            actor.set_editor_property("tags", tag_names)

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def _get_selected_actors(self):
        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            return list(subsystem.get_selected_level_actors())
        except Exception:
            return []


# 模块级单例
instance = None
