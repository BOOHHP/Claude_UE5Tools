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

        # 非交集列表状态：items 与选中 Tag 集合
        self._ni_items_cache = []
        self._ni_selected_tags = set()

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
        """读取已选 Actor 的 Tag 交集写入代理对象，并刷新非交集列表。"""
        try:
            selected = self._get_selected_actors()

            if not selected:
                self._set_proxy_tags([])
                self._update_ni_list([], selected_count=0)
                self.data.set_text("text_selection_info", "当前未选中任何 Actor。")
                self.data.set_text("text_status", "就绪。选中 Actor 后将自动读取 Tag 交集到列表。")
                return

            tag_sets = [set(str(t) for t in getattr(a, "tags", [])) for a in selected]
            common = tag_sets[0].copy()
            union = set()
            for s in tag_sets:
                union |= s
            for s in tag_sets[1:]:
                common &= s
            non_intersect = union - common

            sorted_common = sorted(common)
            self._set_proxy_tags(sorted_common)
            self._update_ni_list(sorted(non_intersect), selected_count=len(selected))

            info = f"已选中 {len(selected)} 个 Actor，共有 Tag {len(sorted_common)} 个（交集），非共有 Tag {len(non_intersect)} 个。"
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

    def _update_ni_list(self, ni_tags, selected_count):
        """刷新非交集 Tag 列表 UI 与提示文字。"""
        items = [str(t) for t in ni_tags]
        # 缓存一份；仅保留仍然存在于新 items 中的选中项
        self._ni_items_cache = items
        self._ni_selected_tags = {t for t in self._ni_selected_tags if t in items}
        ok = False
        for method_name in ("set_list_view_items", "set_list_items"):
            fn = getattr(self.data, method_name, None)
            if fn is None:
                continue
            try:
                fn("list_ni_tags", items)
                ok = True
                break
            except Exception as e:
                unreal.log_warning(f"BatchTagTool _update_ni_list {method_name}: {str(e)}")
        if not ok:
            unreal.log_warning("BatchTagTool: 未找到可用的 set_list_view_items API")
        try:
            if selected_count == 0:
                hint = "选中 2 个及以上 Actor 后，此处将列出非共有的 Tag。"
            elif selected_count == 1:
                hint = "仅选中 1 个 Actor，无非共有 Tag（可改为按上方列表中的 Tag 反向选中场景物体）。"
            elif not ni_tags:
                hint = f"已选中 {selected_count} 个 Actor，所有 Tag 均为共有，无非交集 Tag。"
            else:
                hint = f"已选中 {selected_count} 个 Actor，共 {len(ni_tags)} 个非共有 Tag。双击或选中后点击下方按钮可反向选中场景中持有该 Tag 的 Actor。"
            self.data.set_text("text_ni_info", hint)
        except Exception:
            pass

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

    def on_select_by_tag(self, *args, **kwargs):
        """读取非交集列表中所选 Tag，反向选中场景中所有持有该 Tag 的 Actor。"""
        try:
            selected_tags = self._get_selected_ni_tags()
            if not selected_tags:
                self.data.set_text(
                    "text_status",
                    "⚠️ 请先在下方非交集列表中选中至少一个 Tag。",
                )
                return

            all_actors = self._get_all_level_actors()
            if not all_actors:
                self.data.set_text("text_status", "⚠️ 当前关卡内未发现任何 Actor。")
                return

            tag_set = set(selected_tags)
            matched = []
            for a in all_actors:
                try:
                    actor_tags = set(str(t) for t in (getattr(a, "tags", []) or []))
                except Exception:
                    continue
                if actor_tags & tag_set:
                    matched.append(a)

            if not matched:
                self.data.set_text(
                    "text_status",
                    f"⚠️ 未找到持有 Tag {sorted(tag_set)} 的 Actor。",
                )
                return

            self._set_level_selection(matched)
            tag_label = ", ".join(sorted(tag_set))
            self.data.set_text(
                "text_status",
                f"✅ 已按 Tag [{tag_label}] 选中 {len(matched)} 个 Actor。",
            )
            unreal.log(
                f"BatchTagTool: select_by_tag tags={sorted(tag_set)} matched={len(matched)}"
            )
        except Exception as e:
            unreal.log_error(f"BatchTagTool on_select_by_tag: {str(e)}")
            try:
                self.data.set_text("text_status", f"❌ 按 Tag 选择失败：{str(e)}")
            except Exception:
                pass

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

    def _get_all_level_actors(self):
        """获取所有已加载关卡 Actor，带多级 API 回退。"""
        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            actors = subsystem.get_all_level_actors()
            if actors is not None:
                return list(actors)
        except Exception:
            pass
        try:
            return list(unreal.EditorLevelLibrary.get_all_level_actors())
        except Exception:
            return []

    def _set_level_selection(self, actors):
        """将关卡选择替换为给定 Actor 列表，带 API 回退。"""
        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            try:
                subsystem.set_selected_level_actors(actors)
                return True
            except Exception:
                pass
            # 回退：先清空再逐个加入
            try:
                subsystem.select_nothing()
            except Exception:
                pass
            for a in actors:
                try:
                    subsystem.set_actor_selection_state(a, True)
                except Exception:
                    continue
            return True
        except Exception as e:
            unreal.log_warning(f"BatchTagTool _set_level_selection: {str(e)}")
            return False

    def _get_selected_ni_tags(self):
        """返回用户在非交集列表中选中的 Tag（由 OnSelectionChanged 维护）。"""
        return [t for t in self._ni_items_cache if t in self._ni_selected_tags]

    # ------------------------------------------------------------------
    # SListView 事件回调
    # ------------------------------------------------------------------

    def on_ni_selection_changed(self, item=None, index=None):
        """列表选择变化时调用；%item 为当前点击项，%index 为其下标（-1 表示取消）。

        TAPython SListView 会为每次选择变化触发一次，我们在这里用
        get_list_view_items() 拿到全量选中下标，避免单/多选下标不同步。
        """
        try:
            indexes = []
            fn = getattr(self.data, "get_list_view_items", None)
            if fn is not None:
                try:
                    ret = fn("list_ni_tags")
                    if isinstance(ret, tuple) and len(ret) >= 2 and ret[1] is not None:
                        indexes = list(ret[1])
                except Exception:
                    pass

            if indexes:
                selected = set()
                for i in indexes:
                    try:
                        idx = int(i)
                    except Exception:
                        continue
                    if 0 <= idx < len(self._ni_items_cache):
                        selected.add(self._ni_items_cache[idx])
                self._ni_selected_tags = selected
            else:
                # 单选模式下老版本可能不返回 indexes：退化用 %item
                if item is None or item == "":
                    self._ni_selected_tags = set()
                else:
                    s = str(item)
                    if s in self._ni_items_cache:
                        self._ni_selected_tags = {s}

            self.data.set_text(
                "text_ni_info",
                self._build_ni_info_text(),
            )
        except Exception as e:
            unreal.log_warning(f"BatchTagTool on_ni_selection_changed: {str(e)}")

    def on_ni_double_click(self, item=None, index=None):
        """双击某项 → 以该单个 Tag 执行选择。"""
        if item is not None and str(item).strip():
            self._ni_selected_tags = {str(item)}
        self.on_select_by_tag()

    def _build_ni_info_text(self):
        n_sel = len(self._ni_selected_tags)
        n_total = len(self._ni_items_cache)
        if n_total == 0:
            return "选中 2 个及以上 Actor 后，此处将列出非共有的 Tag。"
        if n_sel == 0:
            return f"共 {n_total} 个非共有 Tag。在上方列表中点击选中后，点下方按钮反向选中 Actor。"
        return f"共 {n_total} 个非共有 Tag，已选中 {n_sel} 个。点下方按钮反向选中场景中持有这些 Tag 的 Actor。"


# 模块级单例
instance = None
