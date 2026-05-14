import json
import os
import time

import unreal


DATA_FILENAME = "PositionClipboardTool_slots.json"
DETAIL_PREVIEW_LIMIT = 80


class PositionClipboardToolController:

    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
        self.storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILENAME)
        self.slots = []
        self.selected_slot_index = -1
        self._initial_tick_handle = None
        self._load_slots()
        self._register_initial_ui_sync()

    def on_closed(self):
        global instance
        try:
            self._unregister_initial_ui_sync()
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool on_closed: {str(e)}")
        finally:
            if instance is self:
                instance = None

    def refresh_ui(self):
        try:
            self._load_slots()
            self._sync_slot_list()
            self._sync_selected_detail()
            self._set_status(self._summary_text())
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool refresh_ui: {str(e)}")
            self._set_status(f"刷新失败：{str(e)}")

    def capture_selection(self):
        try:
            actors = self._get_selected_actors()
            if not actors:
                self._set_status("请先在关卡中选择需要记录位置的 Actor。")
                return

            slot_name = self._get_slot_name_from_ui()
            if not slot_name:
                slot_name = self._generate_slot_name()

            records = []
            failed = 0
            for actor in actors:
                try:
                    records.append(self._actor_to_record(actor))
                except Exception as e:
                    failed += 1
                    unreal.log_warning(f"PositionClipboardTool: 记录 Actor 失败 - {str(e)}")

            if not records:
                self._set_status("没有可记录的 Actor。")
                return

            slot = {
                "name": slot_name,
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "actor_count": len(records),
                "actors": records,
            }
            self._upsert_slot(slot)
            self._save_slots()
            self.selected_slot_index = self._find_slot_index(slot_name)
            self._sync_slot_list()
            self._sync_selected_detail()
            self._safe_set_text("input_slot_name", slot_name)

            suffix = f"，跳过 {failed} 个失败项" if failed else ""
            self._set_status(f"已记录 {len(records)} 个 Actor 的位置到“{slot_name}”{suffix}。")
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool capture_selection: {str(e)}")
            self._set_status(f"记录失败：{str(e)}")

    def select_slot_actors(self):
        try:
            slot = self._get_selected_slot_or_warn()
            if slot is None:
                return
            actors, missing = self._resolve_slot_actors(slot)
            if not actors:
                self._set_status("槽位中的 Actor 当前都无法找到，可能已删除、重命名或关卡未加载。")
                return
            self._set_level_selection(actors)
            msg = f"已选中 {len(actors)} 个 Actor"
            if missing:
                msg += f"，{missing} 个未找到"
            self._set_status(msg + "。")
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool select_slot_actors: {str(e)}")
            self._set_status(f"选中失败：{str(e)}")

    def paste_slot_positions(self):
        try:
            self._paste_selected_slot(select_after_paste=False)
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool paste_slot_positions: {str(e)}")
            self._set_status(f"粘贴失败：{str(e)}")

    def select_and_paste_slot(self):
        try:
            self._paste_selected_slot(select_after_paste=True)
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool select_and_paste_slot: {str(e)}")
            self._set_status(f"选中并粘贴失败：{str(e)}")

    def delete_selected_slot(self):
        try:
            slot = self._get_selected_slot_or_warn()
            if slot is None:
                return
            name = slot.get("name", "Unnamed")
            self.slots.pop(self.selected_slot_index)
            if self.selected_slot_index >= len(self.slots):
                self.selected_slot_index = len(self.slots) - 1
            self._save_slots()
            self._sync_slot_list()
            self._sync_selected_detail()
            self._set_status(f"已删除槽位“{name}”。")
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool delete_selected_slot: {str(e)}")
            self._set_status(f"删除失败：{str(e)}")

    def clear_slot_name(self):
        try:
            self._safe_set_text("input_slot_name", "")
            self._set_status("已清空槽位名称。")
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool clear_slot_name: {str(e)}")

    def on_slot_selection_changed(self, item, index):
        try:
            self.selected_slot_index = int(index)
            self._sync_selected_detail()
            slot = self._get_selected_slot()
            if slot is not None:
                self._safe_set_text("input_slot_name", slot.get("name", ""))
                self._set_status(f"当前槽位：{slot.get('name', 'Unnamed')}。")
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool on_slot_selection_changed: {str(e)}")

    def _paste_selected_slot(self, select_after_paste):
        slot = self._get_selected_slot_or_warn()
        if slot is None:
            return

        pairs, missing = self._resolve_slot_actor_pairs(slot)
        if not pairs:
            self._set_status("槽位中的 Actor 当前都无法找到，无法粘贴。")
            return

        include_rotation = self._get_checkbox_checked("chk_include_rotation")
        include_scale = self._get_checkbox_checked("chk_include_scale")
        changed = 0
        failed = 0
        transaction_name = f"Position Clipboard Paste ({slot.get('name', 'Unnamed')})"

        try:
            with unreal.ScopedEditorTransaction(transaction_name):
                for actor, record in pairs:
                    actor_name = record.get("label") or record.get("name") or self._safe_actor_name(actor)
                    try:
                        if not self._mark_actor_transform_for_undo(actor, actor_name):
                            failed += 1
                            continue
                        transform = self._build_paste_transform(actor, record, include_rotation, include_scale)
                        actor.set_actor_transform(transform, False, False)
                        changed += 1
                    except Exception as e:
                        failed += 1
                        unreal.log_warning(f"PositionClipboardTool: 粘贴失败 {actor_name} - {str(e)}")
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool: 事务创建失败 - {str(e)}")
            self._set_status(f"粘贴失败：事务创建失败，已取消执行以避免不可撤销修改：{str(e)}")
            return

        if select_after_paste and pairs:
            self._set_level_selection([pair[0] for pair in pairs])

        msg = f"已粘贴 {changed} 个 Actor 的位置"
        if include_rotation:
            msg += "、旋转"
        if include_scale:
            msg += "、缩放"
        if missing:
            msg += f"；{missing} 个未找到"
        if failed:
            msg += f"；{failed} 个失败"
        self._set_status(msg + "。")

    def _actor_to_record(self, actor):
        location = actor.get_actor_location()
        rotation = actor.get_actor_rotation()
        scale = actor.get_actor_scale3d()
        return {
            "path": self._safe_actor_path(actor),
            "name": self._safe_actor_name(actor),
            "label": self._safe_actor_label(actor),
            "location": self._vector_to_list(location),
            "rotation": self._rotator_to_list(rotation),
            "scale": self._vector_to_list(scale),
        }

    def _build_paste_transform(self, actor, record, include_rotation, include_scale):
        location = self._list_to_vector(record.get("location"), actor.get_actor_location())
        if include_rotation:
            rotation = self._list_to_rotator(record.get("rotation"), actor.get_actor_rotation())
        else:
            rotation = actor.get_actor_rotation()
        if include_scale:
            scale = self._list_to_vector(record.get("scale"), actor.get_actor_scale3d())
        else:
            scale = actor.get_actor_scale3d()
        return unreal.Transform(location, rotation, scale)

    def _mark_actor_transform_for_undo(self, actor, actor_name):
        try:
            if actor.modify(True) is False:
                unreal.log_warning(f"PositionClipboardTool: Actor {actor_name} modify 返回 False")
                return False
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool: Actor {actor_name} modify 失败 - {str(e)}")
            return False

        root_component = None
        try:
            if hasattr(actor, "root_component"):
                root_component = actor.root_component()
            elif hasattr(actor, "get_root_component"):
                root_component = actor.get_root_component()
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool: 读取 RootComponent 失败 {actor_name} - {str(e)}")

        if root_component is not None:
            try:
                root_component.modify(True)
            except Exception as e:
                unreal.log_warning(f"PositionClipboardTool: RootComponent modify 失败 {actor_name} - {str(e)}")
        return True

    def _resolve_slot_actor_pairs(self, slot):
        pairs = []
        missing = 0
        for record in slot.get("actors", []):
            actor = self._resolve_actor(record)
            if actor is None:
                missing += 1
                continue
            pairs.append((actor, record))
        return pairs, missing

    def _resolve_slot_actors(self, slot):
        pairs, missing = self._resolve_slot_actor_pairs(slot)
        return [pair[0] for pair in pairs], missing

    def _resolve_actor(self, record):
        path = record.get("path") or ""
        name = record.get("name") or ""
        label = record.get("label") or ""

        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            if path:
                try:
                    actor = subsystem.get_actor_reference(path)
                    if actor is not None:
                        return actor
                except Exception:
                    pass
            all_actors = list(subsystem.get_all_level_actors())
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _resolve_actor subsystem: {str(e)}")
            all_actors = []

        for actor in all_actors:
            if path and self._safe_actor_path(actor) == path:
                return actor
        for actor in all_actors:
            if name and self._safe_actor_name(actor) == name:
                return actor
        for actor in all_actors:
            if label and self._safe_actor_label(actor) == label:
                return actor
        return None

    def _get_selected_actors(self):
        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            return list(subsystem.get_selected_level_actors())
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _get_selected_actors: {str(e)}")
            return []

    def _set_level_selection(self, actors):
        try:
            subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
            try:
                subsystem.set_selected_level_actors(actors)
                return True
            except Exception:
                pass
            try:
                subsystem.select_nothing()
            except Exception:
                pass
            for actor in actors:
                try:
                    subsystem.set_actor_selection_state(actor, True)
                except Exception:
                    continue
            return True
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _set_level_selection: {str(e)}")
            return False

    def _load_slots(self):
        try:
            if not os.path.exists(self.storage_path):
                self.slots = []
                self.selected_slot_index = -1
                return
            with open(self.storage_path, "r", encoding="utf-8") as file_obj:
                payload = json.load(file_obj)
            self.slots = list(payload.get("slots", []))
            if self.slots and self.selected_slot_index < 0:
                self.selected_slot_index = 0
            if self.selected_slot_index >= len(self.slots):
                self.selected_slot_index = len(self.slots) - 1
        except Exception as e:
            self.slots = []
            self.selected_slot_index = -1
            unreal.log_error(f"PositionClipboardTool _load_slots: {str(e)}")

    def _save_slots(self):
        try:
            payload = {"version": 1, "slots": self.slots}
            with open(self.storage_path, "w", encoding="utf-8") as file_obj:
                json.dump(payload, file_obj, ensure_ascii=False, indent=2)
        except Exception as e:
            unreal.log_error(f"PositionClipboardTool _save_slots: {str(e)}")
            self._set_status(f"保存槽位失败：{str(e)}")

    def _upsert_slot(self, slot):
        index = self._find_slot_index(slot.get("name", ""))
        if index >= 0:
            self.slots[index] = slot
        else:
            self.slots.insert(0, slot)

    def _find_slot_index(self, name):
        for index, slot in enumerate(self.slots):
            if slot.get("name") == name:
                return index
        return -1

    def _get_selected_slot_or_warn(self):
        slot = self._get_selected_slot()
        if slot is None:
            self._set_status("请先在列表中选择一个已保存的位置槽位。")
        return slot

    def _get_selected_slot(self):
        if not self.slots:
            return None
        if self.selected_slot_index < 0 or self.selected_slot_index >= len(self.slots):
            self.selected_slot_index = 0
        return self.slots[self.selected_slot_index]

    def _sync_slot_list(self):
        labels = []
        for index, slot in enumerate(self.slots):
            name = slot.get("name", "Unnamed")
            count = int(slot.get("actor_count", len(slot.get("actors", []))))
            labels.append(f"{index + 1:02d}. {name}  ({count} Actors)")
        self._set_list_view_items("list_slots", labels)
        if labels and 0 <= self.selected_slot_index < len(labels):
            self._set_list_view_selection("list_slots", [self.selected_slot_index])

    def _sync_selected_detail(self):
        slot = self._get_selected_slot()
        if slot is None:
            self._safe_set_text("text_detail", "尚未记录任何位置槽位。")
            return

        lines = []
        lines.append(f"槽位：{slot.get('name', 'Unnamed')}")
        lines.append(f"记录时间：{slot.get('created_at', '-')}")
        lines.append(f"Actor 数量：{len(slot.get('actors', []))}")
        lines.append("")
        for index, record in enumerate(slot.get("actors", [])[:DETAIL_PREVIEW_LIMIT], 1):
            label = record.get("label") or record.get("name") or "Unnamed"
            location = record.get("location", [0.0, 0.0, 0.0])
            lines.append(f"{index:03d}. {label}  X={location[0]:.2f}  Y={location[1]:.2f}  Z={location[2]:.2f}")
        hidden_count = len(slot.get("actors", [])) - DETAIL_PREVIEW_LIMIT
        if hidden_count > 0:
            lines.append(f"... 还有 {hidden_count} 个 Actor 未显示")
        self._safe_set_text("text_detail", "\n".join(lines))

    def _summary_text(self):
        if not self.slots:
            return "就绪：选择多个 Actor 后点击“记录当前选择”。"
        return f"就绪：当前有 {len(self.slots)} 个位置槽位。"

    def _set_list_view_items(self, aka, items):
        for method_name in ("set_list_view_items", "set_list_items"):
            fn = getattr(self.data, method_name, None)
            if fn is None:
                continue
            try:
                fn(aka, list(items))
                return True
            except Exception as e:
                unreal.log_warning(f"PositionClipboardTool _set_list_view_items {method_name}: {str(e)}")
        return False

    def _set_list_view_selection(self, aka, indexes):
        fn = getattr(self.data, "set_list_view_selections", None)
        if fn is None:
            return False
        try:
            fn(aka, list(indexes))
            return True
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _set_list_view_selection: {str(e)}")
            return False

    def _get_slot_name_from_ui(self):
        try:
            value = self.data.get_text("input_slot_name")
            text = str(value or "").strip()
            if text in ("None", "null"):
                return ""
            if text == "槽位名称（可留空自动生成）":
                return ""
            return text
        except Exception:
            return ""

    def _generate_slot_name(self):
        return f"位置记录 {time.strftime('%Y-%m-%d %H:%M:%S')}"

    def _get_checkbox_checked(self, aka):
        try:
            return bool(self.data.get_is_checked(aka))
        except Exception:
            return False

    def _safe_set_text(self, aka, text):
        try:
            self.data.set_text(aka, str(text))
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _safe_set_text {aka}: {str(e)}")

    def _set_status(self, text):
        self._safe_set_text("text_status", text)
        try:
            unreal.log(f"PositionClipboardTool: {text}")
        except Exception:
            pass

    def _safe_actor_path(self, actor):
        try:
            return actor.get_path_name()
        except Exception:
            return ""

    def _safe_actor_name(self, actor):
        try:
            return actor.get_name()
        except Exception:
            return str(actor)

    def _safe_actor_label(self, actor):
        try:
            return actor.get_actor_label()
        except Exception:
            return self._safe_actor_name(actor)

    def _vector_to_list(self, vector):
        return [float(vector.x), float(vector.y), float(vector.z)]

    def _rotator_to_list(self, rotator):
        return [float(rotator.roll), float(rotator.pitch), float(rotator.yaw)]

    def _list_to_vector(self, values, fallback):
        try:
            return unreal.Vector(float(values[0]), float(values[1]), float(values[2]))
        except Exception:
            return fallback

    def _list_to_rotator(self, values, fallback):
        try:
            return unreal.Rotator(float(values[0]), float(values[1]), float(values[2]))
        except Exception:
            return fallback

    def _register_initial_ui_sync(self):
        try:
            self._initial_tick_handle = unreal.register_slate_post_tick_callback(self._on_initial_tick)
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _register_initial_ui_sync: {str(e)}")

    def _unregister_initial_ui_sync(self):
        if self._initial_tick_handle is None:
            return
        try:
            unreal.unregister_slate_post_tick_callback(self._initial_tick_handle)
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _unregister_initial_ui_sync: {str(e)}")
        finally:
            self._initial_tick_handle = None

    def _on_initial_tick(self, delta_time):
        try:
            self._unregister_initial_ui_sync()
            self._sync_slot_list()
            self._sync_selected_detail()
            self._set_status(self._summary_text())
        except Exception as e:
            unreal.log_warning(f"PositionClipboardTool _on_initial_tick: {str(e)}")


def on_close():
    global instance
    if instance is not None:
        instance.on_closed()


instance = None