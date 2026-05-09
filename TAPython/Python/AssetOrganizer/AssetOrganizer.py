import os
import re
import time

import unreal

from AssetOrganizer.AssetPathProxy import AssetPathProxy


class AssetOrganizerController:

    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
        self._last_non_pot_texture_plan = []
        self._last_non_pot_texture_report = {}
        self._non_pot_texture_result_entries = []
        self._non_pot_texture_selected_result_indexes = []
        self._non_pot_texture_scan_stats = []
        self._non_pot_texture_scan_paths = ["/Game"]
        self._non_pot_texture_scan_path = "/Game"
        self.asset_path_proxy = None
        self._path_details_tick_handle = None
        self._path_details_bound = False

        try:
            self.asset_path_proxy = unreal.new_object(AssetPathProxy)
            self._set_proxy_non_pot_texture_paths(self._non_pot_texture_scan_paths)
        except Exception as e:
            unreal.log_error(f"AssetOrganizer: 创建资产路径代理失败: {str(e)}")

        self._register_path_details_tick()

    # ------------------------------------------------------------------
    # 生命周期
    # ------------------------------------------------------------------

    def _register_path_details_tick(self):
        try:
            if self._path_details_tick_handle is None:
                self._path_details_tick_handle = unreal.register_slate_post_tick_callback(self._bind_path_details_on_tick)
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: 资产路径 DetailsView 绑定 tick 注册失败 - {str(e)}")

    def _unregister_path_details_tick(self):
        try:
            if self._path_details_tick_handle is not None:
                unreal.unregister_slate_post_tick_callback(self._path_details_tick_handle)
                self._path_details_tick_handle = None
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: 资产路径 DetailsView 绑定 tick 注销失败 - {str(e)}")

    def _bind_path_details_on_tick(self, _delta_time):
        if self._path_details_bound:
            self._unregister_path_details_tick()
            return
        self._bind_non_pot_texture_path_details_view()
        self._path_details_bound = True
        self._unregister_path_details_tick()

    def on_closed(self):
        global instance
        try:
            self._unregister_path_details_tick()
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer on_closed: {str(e)}")
        finally:
            if instance is self:
                instance = None

    # ------------------------------------------------------------------
    # 04：修复非 POT 纹理
    # ------------------------------------------------------------------

    def preview_non_pot_textures(self):
        try:
            self._apply_non_pot_texture_paths_from_proxy(clear_results=False, show_status=False)
            settings = self._read_non_pot_texture_settings()
            plan, summary = self._build_non_pot_texture_plan(settings)
            self._last_non_pot_texture_plan = plan
            self._last_non_pot_texture_report = {}
            self._refresh_non_pot_texture_result_list(plan, summary)
            self.data.set_text("txt_non_pot_texture_preview", self._format_non_pot_texture_preview(plan, summary))

            msg = (
                f"非 POT 纹理扫描完成：待修复 {summary['fix']}，合规 {summary['ok']}，"
                f"跳过 {summary['skip']}，错误 {summary['errors']}，共 {summary['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"AssetOrganizer: {msg}")
        except Exception as e:
            error_msg = f"非 POT 纹理扫描失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer preview_non_pot_textures: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def execute_fix_non_pot_textures(self):
        try:
            self._apply_non_pot_texture_paths_from_proxy(clear_results=False, show_status=False)
            settings = self._read_non_pot_texture_settings()
            plan, summary = self._build_non_pot_texture_plan(settings)
            self._last_non_pot_texture_plan = plan
            self._refresh_non_pot_texture_result_list(plan, summary)

            report = self._execute_non_pot_texture_plan(plan, summary, settings)
            self._last_non_pot_texture_report = report

            refreshed_plan, refreshed_summary = self._build_non_pot_texture_plan(settings)
            self._last_non_pot_texture_plan = refreshed_plan
            self._refresh_non_pot_texture_result_list(refreshed_plan, refreshed_summary)
            preview_text = self._format_non_pot_texture_preview(refreshed_plan, refreshed_summary)
            self.data.set_text("txt_non_pot_texture_preview", preview_text + "\n\n" + self._format_non_pot_texture_report(report))

            msg = (
                f"非 POT 纹理修复完成：修改 {report['fixed']}，跳过 {report['skipped']}，"
                f"失败 {report['failed']}，共 {report['total']}。"
            )
            self.data.set_text("txt_status", msg)
            unreal.log(f"AssetOrganizer: {msg}")
        except Exception as e:
            error_msg = f"非 POT 纹理修复失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer execute_fix_non_pot_textures: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def select_selected_non_pot_texture_results(self):
        try:
            selected_indexes = self._get_list_view_selected_indexes("list_non_pot_texture_results")
            if selected_indexes:
                self._set_non_pot_texture_selected_result_indexes(selected_indexes, update_selection=False)
            entries = self._get_selected_non_pot_texture_result_entries()
            if not entries:
                msg = "请先在非 POT 纹理结果列表中选择一个或多个纹理。"
                self.data.set_text("txt_status", msg)
                return
            asset_paths = [entry.get("asset_path") for entry in entries if entry.get("asset_path")]
            if not asset_paths:
                msg = "所选结果没有可同步到内容浏览器的资产路径。"
                self.data.set_text("txt_status", msg)
                return
            unreal.EditorAssetLibrary.sync_browser_to_objects(asset_paths)
            msg = f"已在内容浏览器中同步 {len(asset_paths)} 个纹理资产。"
            self.data.set_text("txt_status", msg)
            unreal.log(f"AssetOrganizer: {msg}")
        except Exception as e:
            error_msg = f"同步非 POT 纹理结果失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer select_selected_non_pot_texture_results: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def use_content_browser_non_pot_texture_path(self):
        self.add_content_browser_non_pot_texture_paths()

    def add_content_browser_non_pot_texture_paths(self):
        try:
            paths = self._get_content_browser_selected_content_paths()
            if not paths:
                msg = "请先在内容浏览器中选中一个文件夹，或选中该文件夹下的任意资产。"
                self.data.set_text("txt_status", msg)
                return

            merged_paths = self._merge_content_paths(self._get_proxy_non_pot_texture_paths(), paths)
            self._set_proxy_non_pot_texture_paths(merged_paths)
            self._sync_non_pot_texture_path_to_ui(merged_paths)
            self.data.set_text("txt_status", f"已添加 {len(paths)} 个内容浏览器路径到列表。确认列表后点击“应用路径列表”。")
        except Exception as e:
            error_msg = f"读取内容浏览器路径失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer add_content_browser_non_pot_texture_paths: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def apply_non_pot_texture_path_list(self):
        try:
            paths = self._apply_non_pot_texture_paths_from_proxy(clear_results=True, show_status=False)
            self.data.set_text("txt_status", f"已应用 {len(paths)} 个扫描目录。点击预览开始扫描。")
        except Exception as e:
            error_msg = f"应用扫描路径列表失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer apply_non_pot_texture_path_list: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def reset_non_pot_texture_path_list(self):
        try:
            paths = ["/Game"]
            self._set_proxy_non_pot_texture_paths(paths)
            self._apply_non_pot_texture_paths(paths, clear_results=True)
            self.data.set_text("txt_status", "已重置扫描目录为 /Game。")
        except Exception as e:
            error_msg = f"重置扫描路径列表失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer reset_non_pot_texture_path_list: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def focus_non_pot_texture_scan_path_in_content_browser(self):
        try:
            settings = self._read_non_pot_texture_settings()
            scan_paths = settings.get("scan_paths") or [settings.get("scan_path", "/Game")]
            scan_path = scan_paths[0] if scan_paths else "/Game"
            python_bp_lib = getattr(unreal, "PythonBPLib", None)
            if python_bp_lib and hasattr(python_bp_lib, "set_selected_folder"):
                python_bp_lib.set_selected_folder([scan_path])
                self.data.set_text("txt_status", f"已在内容浏览器定位目录：{scan_path}")
                return
            if python_bp_lib and hasattr(python_bp_lib, "set_selected_folder_path"):
                python_bp_lib.set_selected_folder_path(unreal.Name(scan_path))
                self.data.set_text("txt_status", f"已在内容浏览器定位目录：{scan_path}")
                return
            self.data.set_text("txt_status", "当前 TAPython 版本未提供内容浏览器目录定位接口。")
        except Exception as e:
            error_msg = f"定位内容浏览器目录失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer focus_non_pot_texture_scan_path_in_content_browser: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def on_non_pot_texture_result_selection_changed(self, item=None, index=None):
        try:
            selected_indexes = self._get_list_view_selected_indexes("list_non_pot_texture_results")
            if not selected_indexes:
                fallback_index = self._get_single_list_view_selected_index("list_non_pot_texture_results", index)
                if fallback_index >= 0:
                    selected_indexes = [fallback_index]
            selected_indexes = [i for i in selected_indexes if 0 <= i < len(self._non_pot_texture_result_entries)]
            if not selected_indexes:
                return
            self._set_non_pot_texture_selected_result_indexes(selected_indexes, update_selection=False)
            self.data.set_text("txt_status", f"已选择 {len(selected_indexes)} 条非 POT 纹理结果，可同步到内容浏览器。")
        except Exception as e:
            error_msg = f"更新非 POT 纹理结果选择失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer on_non_pot_texture_result_selection_changed: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def on_non_pot_texture_result_double_click(self, item=None, index=None):
        try:
            try:
                selected_index = int(index)
            except Exception:
                selected_index = self._get_single_list_view_selected_index("list_non_pot_texture_results", None)
            if selected_index < 0 or selected_index >= len(self._non_pot_texture_result_entries):
                return
            self._set_non_pot_texture_selected_result_indexes([selected_index], update_selection=True)
            self.select_selected_non_pot_texture_results()
        except Exception as e:
            error_msg = f"双击同步非 POT 纹理失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer on_non_pot_texture_result_double_click: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    def export_non_pot_texture_report(self):
        try:
            if not self._last_non_pot_texture_plan:
                msg = "没有可导出的非 POT 纹理扫描结果，请先执行预览扫描。"
                self.data.set_text("txt_status", msg)
                return
            summary = self._summarize_non_pot_texture_plan(self._last_non_pot_texture_plan)
            summary["scope_label"] = self._read_non_pot_texture_settings().get("scope_label", "/Game")
            batch_report = self._build_non_pot_texture_batch_report(self._last_non_pot_texture_plan, summary)
            report_text = self._format_batch_report_text(batch_report, max_rows=1000)
            if self._last_non_pot_texture_report:
                report_text += "\n\n" + self._format_non_pot_texture_report(self._last_non_pot_texture_report)
            file_path = self._export_batch_report_text("NonPOTTextureReport", report_text)
            msg = f"非 POT 纹理报告已导出：{file_path}"
            self.data.set_text("txt_status", msg)
            unreal.log(f"AssetOrganizer: {msg}")
        except Exception as e:
            error_msg = f"导出非 POT 纹理报告失败：{str(e)}"
            unreal.log_error(f"AssetOrganizer export_non_pot_texture_report: {error_msg}")
            self.data.set_text("txt_status", error_msg)

    # ------------------------------------------------------------------
    # 路径代理与内容浏览器
    # ------------------------------------------------------------------

    def _read_non_pot_texture_settings(self):
        scan_paths = self._normalize_content_path_list(self._non_pot_texture_scan_paths)
        if not scan_paths:
            scan_paths = self._normalize_content_path_list(self._get_proxy_non_pot_texture_paths())
        if not scan_paths:
            scan_paths = ["/Game"]
        self._non_pot_texture_scan_paths = scan_paths
        self._non_pot_texture_scan_path = scan_paths[0]
        scope_label = self._format_non_pot_texture_scope_label(scan_paths)
        return {
            "scan_path": self._non_pot_texture_scan_path,
            "scan_paths": scan_paths,
            "scope_label": scope_label,
            "recursive": self._get_checkbox_checked("chk_non_pot_texture_recursive"),
            "save_after_fix": self._get_checkbox_checked("chk_non_pot_texture_save"),
        }

    def _bind_non_pot_texture_path_details_view(self):
        try:
            if self.asset_path_proxy is not None:
                self.data.set_object("details_non_pot_texture_paths", self.asset_path_proxy)
                self._sync_non_pot_texture_path_to_ui(self._non_pot_texture_scan_paths)
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: 绑定非 POT 纹理路径 DetailsView 失败 - {str(e)}")

    def _set_proxy_non_pot_texture_paths(self, paths):
        if self.asset_path_proxy is None:
            return
        normalized_paths = self._normalize_content_path_list(paths)
        try:
            self.asset_path_proxy.set_editor_property("scan_paths", [unreal.Name(path) for path in normalized_paths])
        except Exception:
            try:
                self.asset_path_proxy.scan_paths = [unreal.Name(path) for path in normalized_paths]
            except Exception as e:
                unreal.log_warning(f"AssetOrganizer: 写入非 POT 纹理路径代理失败 - {str(e)}")

    def _get_proxy_non_pot_texture_paths(self):
        if self.asset_path_proxy is None:
            return []
        try:
            raw_paths = self.asset_path_proxy.get_editor_property("scan_paths")
        except Exception:
            try:
                raw_paths = self.asset_path_proxy.scan_paths
            except Exception:
                raw_paths = []
        return self._normalize_content_path_list(raw_paths or [])

    def _apply_non_pot_texture_paths_from_proxy(self, clear_results, show_status):
        paths = self._get_proxy_non_pot_texture_paths()
        if not paths:
            paths = ["/Game"]
            self._set_proxy_non_pot_texture_paths(paths)
        self._apply_non_pot_texture_paths(paths, clear_results=clear_results)
        if show_status:
            self.data.set_text("txt_status", f"已应用 {len(paths)} 个扫描目录。")
        return paths

    def _apply_non_pot_texture_paths(self, paths, clear_results):
        normalized_paths = self._normalize_content_path_list(paths)
        if not normalized_paths:
            normalized_paths = ["/Game"]
        old_label = self._format_non_pot_texture_scope_label(self._non_pot_texture_scan_paths)
        new_label = self._format_non_pot_texture_scope_label(normalized_paths)
        self._non_pot_texture_scan_paths = normalized_paths
        self._non_pot_texture_scan_path = normalized_paths[0]
        self._sync_non_pot_texture_path_to_ui(normalized_paths)
        if clear_results and old_label != new_label:
            self._clear_non_pot_texture_scan_results(f"已应用扫描目录：{new_label}。点击预览开始扫描。")

    def _sync_non_pot_texture_path_to_ui(self, paths=None):
        normalized_paths = self._normalize_content_path_list(paths or self._non_pot_texture_scan_paths)
        label = self._format_non_pot_texture_scope_label(normalized_paths)
        count_label = f"当前扫描目录：{len(normalized_paths)} 个"
        try:
            self.data.set_text("input_non_pot_texture_path", label)
        except Exception:
            pass
        try:
            self.data.set_text("txt_non_pot_texture_path_info", count_label)
        except Exception:
            pass

    def _merge_content_paths(self, base_paths, new_paths):
        return self._normalize_content_path_list(list(base_paths or []) + list(new_paths or []))

    def _normalize_content_path_list(self, paths):
        normalized_paths = []
        for path in paths or []:
            normalized = self._normalize_content_path(path)
            if normalized and normalized not in normalized_paths:
                normalized_paths.append(normalized)
        return normalized_paths

    def _format_non_pot_texture_scope_label(self, paths):
        normalized_paths = self._normalize_content_path_list(paths)
        if not normalized_paths:
            return "/Game"
        if len(normalized_paths) <= 3:
            return ", ".join(normalized_paths)
        return ", ".join(normalized_paths[:3]) + f" ... (+{len(normalized_paths) - 3})"

    def _clear_non_pot_texture_scan_results(self, message=""):
        self._last_non_pot_texture_plan = []
        self._last_non_pot_texture_report = {}
        self._non_pot_texture_result_entries = []
        self._non_pot_texture_selected_result_indexes = []
        self._set_list_view_items("list_non_pot_texture_results", [])
        self._set_non_pot_texture_result_info("无扫描结果。")
        self.data.set_text("txt_non_pot_texture_preview", message or "扫描目录已变化，请重新预览非 POT 纹理。")

    def _get_content_browser_selected_content_paths(self):
        paths = []
        for source_paths in (
            self._get_editor_utility_selected_folder_paths(),
            self._get_python_bplib_selected_folder_paths(),
            self._get_selected_asset_parent_paths(),
            self._get_current_content_browser_item_path(),
        ):
            for path in source_paths:
                normalized = self._normalize_content_browser_path(path)
                if normalized and normalized not in paths:
                    paths.append(normalized)
            if paths:
                return paths
        return paths

    def _get_editor_utility_selected_folder_paths(self):
        paths = []
        for method_name in ("get_selected_folder_paths", "get_selected_path_view_folder_paths"):
            fn = getattr(unreal.EditorUtilityLibrary, method_name, None)
            if fn is None:
                continue
            try:
                for path in list(fn() or []):
                    if path:
                        paths.append(str(path))
            except Exception as e:
                unreal.log_warning(f"AssetOrganizer: {method_name} 读取内容浏览器目录失败 - {str(e)}")
        return paths

    def _get_python_bplib_selected_folder_paths(self):
        python_bp_lib = getattr(unreal, "PythonBPLib", None)
        if python_bp_lib is None:
            return []
        fn = getattr(python_bp_lib, "get_selected_folder", None)
        if fn is None:
            return []
        try:
            return [str(path) for path in list(fn() or []) if path]
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: PythonBPLib.get_selected_folder 失败 - {str(e)}")
            return []

    def _get_selected_asset_parent_paths(self):
        paths = []
        try:
            selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
        except Exception:
            selected_assets = []
        for asset in selected_assets or []:
            object_path = self._get_loaded_asset_object_path(asset)
            package_path = self._object_path_to_package_path(object_path)
            if package_path and package_path not in paths:
                paths.append(package_path)
        python_bp_lib = getattr(unreal, "PythonBPLib", None)
        fn = getattr(python_bp_lib, "get_selected_assets_paths", None) if python_bp_lib else None
        if fn:
            try:
                for object_path in list(fn() or []):
                    package_path = self._object_path_to_package_path(object_path)
                    if package_path and package_path not in paths:
                        paths.append(package_path)
            except Exception as e:
                unreal.log_warning(f"AssetOrganizer: PythonBPLib.get_selected_assets_paths 失败 - {str(e)}")
        return paths

    def _get_current_content_browser_item_path(self):
        fn = getattr(unreal.EditorUtilityLibrary, "get_current_content_browser_item_path", None)
        if fn is None:
            return []
        try:
            item_path = fn()
            if item_path is None:
                return []
            internal_path = ""
            try:
                internal_path = str(item_path.get_internal_path())
            except Exception:
                pass
            virtual_path = ""
            try:
                virtual_path = str(item_path.get_virtual_path())
            except Exception:
                pass
            return [path for path in (internal_path, virtual_path) if path and path != "None"]
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: get_current_content_browser_item_path 失败 - {str(e)}")
            return []

    def _get_loaded_asset_object_path(self, asset):
        try:
            return unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
        except Exception:
            pass
        try:
            return asset.get_path_name()
        except Exception:
            return ""

    def _object_path_to_package_path(self, object_path):
        text = str(object_path or "").replace("\\", "/")
        if not text:
            return ""
        if "." in text:
            text = text.rsplit(".", 1)[0]
        if "/" in text:
            text = text.rsplit("/", 1)[0]
        return text

    def _normalize_content_browser_path(self, path):
        text = str(path or "").replace("\\", "/").strip()
        if not text or text == "None":
            return ""
        for marker in ("/Game/", "/Game"):
            index = text.find(marker)
            if index >= 0:
                text = text[index:]
                break
        if text.startswith("/All/Game"):
            text = "/Game" + text[len("/All/Game"):]
        elif text.startswith("/All/Content"):
            text = "/Game" + text[len("/All/Content"):]
        elif text.startswith("/Content"):
            text = "/Game" + text[len("/Content"):]
        elif text.startswith("Content/"):
            text = "/Game/" + text[len("Content/"):]
        if "." in text:
            text = self._object_path_to_package_path(text)
        return self._normalize_content_path(text)

    def _normalize_content_path(self, path):
        text = str(path or "/Game").replace("\\", "/").strip()
        if not text:
            return "/Game"
        if not text.startswith("/"):
            text = "/" + text
        return text.rstrip("/") or "/Game"

    # ------------------------------------------------------------------
    # 扫描与修复逻辑
    # ------------------------------------------------------------------

    def _build_non_pot_texture_plan(self, settings):
        scan_paths = self._normalize_content_path_list(settings.get("scan_paths") or [settings.get("scan_path", "/Game")])
        recursive = bool(settings.get("recursive", True))
        asset_records = self._get_texture_asset_records_by_paths(scan_paths, recursive)
        plan = []

        with unreal.ScopedSlowTask(len(asset_records), "Scan Non-POT Textures") as slow_task:
            slow_task.make_dialog(True)
            for record in asset_records:
                should_cancel = getattr(slow_task, "should_cancel", None)
                if callable(should_cancel) and should_cancel():
                    break
                asset_data = record.get("asset_data")
                asset_path = record.get("asset_path", "<UnknownAsset>")
                slow_task.enter_progress_frame(1, asset_path)
                plan.append(self._build_non_pot_texture_plan_item(asset_data, asset_path))

        summary = self._summarize_non_pot_texture_plan(plan)
        summary["scope_label"] = settings.get("scope_label") or self._format_non_pot_texture_scope_label(scan_paths)
        summary["scan_stats"] = list(self._non_pot_texture_scan_stats)
        return plan, summary

    def _get_texture_asset_records_by_paths(self, scan_paths, recursive):
        self._non_pot_texture_scan_stats = []
        texture_records = []
        seen_asset_paths = set()
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        normalized_paths = self._normalize_content_path_list(scan_paths or ["/Game"])
        try:
            registry.scan_paths_synchronous(normalized_paths, False, False)
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: 非 POT 纹理扫描路径刷新失败 {normalized_paths} - {str(e)}")
        path_names = [unreal.Name(path) for path in normalized_paths]
        try:
            assets = registry.get_assets_by_paths(path_names, recursive, False) or []
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: get_assets_by_paths 失败，回退逐路径扫描 - {str(e)}")
            assets = []
            for scan_path in normalized_paths:
                try:
                    assets.extend(registry.get_assets_by_path(unreal.Name(scan_path), recursive, False) or [])
                except Exception as path_error:
                    unreal.log_warning(f"AssetOrganizer: get_assets_by_path 失败 {scan_path} - {str(path_error)}")

        stat_by_path = self._make_non_pot_texture_scan_stat_map(normalized_paths, recursive)
        for asset_data in assets:
            asset_path = self._asset_data_to_object_path(asset_data)
            owner_path = self._find_non_pot_texture_owner_scan_path(asset_path, normalized_paths)
            stat = stat_by_path.get(owner_path)
            if stat is not None:
                stat["registry_raw"] += 1
                if len(stat["samples"]) < 5:
                    stat["samples"].append(f"{asset_path} class={self._get_asset_data_class_text(asset_data)}")
            if not self._is_texture2d_asset_data(asset_data):
                continue
            if stat is not None:
                stat["registry_textures"] += 1
            key = asset_path.lower()
            if key in seen_asset_paths:
                continue
            seen_asset_paths.add(key)
            texture_records.append({"asset_data": asset_data, "asset_path": asset_path})
        self._non_pot_texture_scan_stats = list(stat_by_path.values())
        texture_records.sort(key=lambda item: item.get("asset_path", "").lower())
        return texture_records

    def _make_non_pot_texture_scan_stat_map(self, scan_paths, recursive):
        return {
            path: {
                "path": path,
                "recursive": bool(recursive),
                "registry_raw": 0,
                "registry_textures": 0,
                "samples": [],
            }
            for path in scan_paths
        }

    def _find_non_pot_texture_owner_scan_path(self, asset_path, scan_paths):
        package_path = self._object_path_to_package_path(asset_path)
        for scan_path in sorted(scan_paths, key=len, reverse=True):
            if package_path == scan_path or package_path.startswith(scan_path + "/"):
                return scan_path
        return scan_paths[0] if scan_paths else "/Game"

    def _is_texture2d_asset_data(self, asset_data):
        class_text = self._get_asset_data_class_text(asset_data)
        return class_text == "Texture2D" or class_text.endswith(".Texture2D") or class_text.endswith("/Texture2D") or "Texture2D" in class_text

    def _get_asset_data_class_text(self, asset_data):
        parts = []
        for attr_name in ("asset_class", "asset_class_path"):
            try:
                value = getattr(asset_data, attr_name)
                value = value() if callable(value) else value
                if value is not None:
                    parts.append(str(value))
            except Exception:
                pass
        return " | ".join(parts)

    def _asset_data_to_object_path(self, asset_data):
        if asset_data is None:
            return "<UnknownAsset>"
        try:
            package_value = getattr(asset_data, "package_name")
            asset_value = getattr(asset_data, "asset_name")
            package_name = str(package_value() if callable(package_value) else package_value)
            asset_name = str(asset_value() if callable(asset_value) else asset_value)
            if package_name and asset_name:
                return f"{package_name}.{asset_name}"
        except Exception:
            pass
        soft_path = self._asset_data_to_soft_object_path_text(asset_data)
        if soft_path:
            return soft_path
        return "<UnknownAsset>"

    def _asset_data_to_soft_object_path_text(self, asset_data):
        for getter in (
            lambda: asset_data.to_soft_object_path(),
            lambda: unreal.AssetRegistryHelpers.to_soft_object_path(asset_data),
        ):
            try:
                soft_path = getter()
            except Exception:
                continue
            for method_name in ("get_asset_path_string", "to_string", "get_long_package_name"):
                try:
                    method = getattr(soft_path, method_name, None)
                    if method is None:
                        continue
                    text = str(method())
                    if text and text != "None" and not text.startswith("<Struct"):
                        return text
                except Exception:
                    pass
            text = str(soft_path)
            if text and text != "None" and not text.startswith("<Struct"):
                return text
        return ""

    def _build_non_pot_texture_plan_item(self, asset_data, asset_path):
        item = {
            "asset_data": asset_data,
            "asset_path": asset_path,
            "texture": None,
            "name": self._asset_path_to_display_name(asset_path),
            "width": 0,
            "height": 0,
            "current_power_mode": "",
            "target_power_mode": "",
            "current_max_texture_size": 0,
            "recommended_max_texture_size": 0,
            "action": "skip",
            "reason": "未检测",
            "details": [],
            "errors": [],
        }
        try:
            width, height = self._get_texture2d_size_from_asset_data(asset_data)
            texture = None
            if width <= 0 or height <= 0:
                texture = self._load_texture2d_asset(asset_data, asset_path)
                item["texture"] = texture
                item["name"] = self._safe_object_name(texture) if texture is not None else item["name"]
                if texture is None:
                    item["action"] = "error"
                    item["reason"] = "资产加载失败，且 AssetRegistry 未提供尺寸元数据"
                    return item
                if not isinstance(texture, unreal.Texture2D):
                    item["action"] = "skip"
                    item["reason"] = "非 Texture2D 资产"
                    return item
                width, height = self._get_texture2d_size(texture)
            item["width"] = width
            item["height"] = height
            if texture is not None:
                item["current_power_mode"] = self._get_texture_power_of_two_mode_text(texture)
                item["current_max_texture_size"] = self._get_texture_max_texture_size(texture)
            else:
                item["current_power_mode"] = "<MetadataOnly>"
                item["details"].append("sizeSource=AssetRegistryTag")
            item["recommended_max_texture_size"] = self._next_power_of_two(max(width, height))

            if width <= 0 or height <= 0:
                item["action"] = "error"
                item["reason"] = f"无法读取有效尺寸：{width}x{height}"
                return item
            if self._is_power_of_two(width) and self._is_power_of_two(height):
                item["action"] = "ok"
                item["reason"] = f"尺寸已为 POT：{width}x{height}"
                return item

            target_mode = self._resolve_texture_power_of_two_mode()
            if target_mode is not None:
                if texture is None:
                    texture = self._load_texture2d_asset(asset_data, asset_path)
                    item["texture"] = texture
                    if texture is not None:
                        item["name"] = self._safe_object_name(texture)
                if texture is not None:
                    item["current_power_mode"] = self._get_texture_power_of_two_mode_text(texture)
                    item["current_max_texture_size"] = self._get_texture_max_texture_size(texture)
                    if self._is_texture_power_mode(texture, target_mode):
                        display_width = self._next_power_of_two(width)
                        display_height = self._next_power_of_two(height)
                        item["action"] = "ok"
                        item["reason"] = (
                            f"源尺寸非 POT：{width}x{height}，但已设置延展到 2 的幂；"
                            f"预计显示：{display_width}x{display_height}"
                        )
                        item["details"].append(f"power_of_two_mode: {item['current_power_mode']}")
                        return item
            if target_mode is not None:
                item["target_power_mode"] = str(target_mode)
                item["action"] = "fix"
                item["reason"] = f"非 POT 尺寸：{width}x{height}，建议延展到 2 的幂"
                item["details"].append(f"power_of_two_mode: {item['current_power_mode']} -> {target_mode}")
            else:
                item["action"] = "error"
                item["reason"] = "当前 UE Python 未暴露 TexturePowerOfTwoSetting.STRETCH_TO_POWER_OF_TWO"
                item["details"].append("请用探针确认 TexturePowerOfTwoSetting 枚举名后再启用自动修复")
        except Exception as e:
            item["action"] = "error"
            item["reason"] = str(e)
            item["errors"].append(str(e))
        return item

    def _load_texture2d_asset(self, asset_data, asset_path):
        try:
            texture = unreal.AssetRegistryHelpers.get_asset(asset_data)
            if texture is not None:
                return texture
        except Exception:
            pass
        try:
            return unreal.EditorAssetLibrary.load_asset(asset_path)
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: 纹理加载失败 {asset_path} - {str(e)}")
            return None

    def _asset_path_to_display_name(self, asset_path):
        text = str(asset_path or "<UnknownTexture>")
        if "." in text:
            text = text.rsplit(".", 1)[-1]
        elif "/" in text:
            text = text.rsplit("/", 1)[-1]
        return text or "<UnknownTexture>"

    def _get_texture2d_size_from_asset_data(self, asset_data):
        if asset_data is None:
            return 0, 0
        for tag_name in ("ImportedSize", "Dimensions", "TextureSize", "SourceSize", "Size"):
            tag_value = self._get_asset_data_tag_value(asset_data, tag_name)
            width, height = self._parse_texture_size_text(tag_value)
            if width > 0 and height > 0:
                return width, height
        return 0, 0

    def _get_asset_data_tag_value(self, asset_data, tag_name):
        try:
            value = asset_data.get_tag_value(unreal.Name(tag_name))
            if value:
                return str(value)
        except Exception:
            pass
        try:
            value = unreal.AssetRegistryHelpers.get_tag_value(asset_data, unreal.Name(tag_name))
            if value:
                return str(value)
        except Exception:
            pass
        return ""

    def _parse_texture_size_text(self, text):
        numbers = re.findall(r"\d+", str(text or ""))
        if len(numbers) < 2:
            return 0, 0
        try:
            return int(numbers[0]), int(numbers[1])
        except Exception:
            return 0, 0

    def _get_texture2d_size(self, texture):
        try:
            width = int(texture.blueprint_get_size_x())
            height = int(texture.blueprint_get_size_y())
            return width, height
        except Exception:
            width = self._safe_get_editor_property(texture, "size_x") or 0
            height = self._safe_get_editor_property(texture, "size_y") or 0
            return int(width or 0), int(height or 0)

    def _get_texture_power_of_two_mode_text(self, texture):
        value = self._safe_get_editor_property(texture, "power_of_two_mode")
        return str(value) if value is not None else "<Unknown>"

    def _is_texture_power_mode(self, texture, target_mode):
        value = self._safe_get_editor_property(texture, "power_of_two_mode")
        if value is None:
            return False
        if value == target_mode:
            return True
        return str(value).lower() == str(target_mode).lower()

    def _get_texture_max_texture_size(self, texture):
        value = self._safe_get_editor_property(texture, "max_texture_size")
        try:
            return int(value or 0)
        except Exception:
            return 0

    def _resolve_texture_power_of_two_mode(self):
        enum_class = getattr(unreal, "TexturePowerOfTwoSetting", None)
        if enum_class is None:
            return None
        for name in (
            "STRETCH_TO_POWER_OF_TWO",
            "StretchToPowerOfTwo",
            "TPO_STRETCH_TO_POWER_OF_TWO",
            "STRETCH_TO_POWER_OF2",
        ):
            value = getattr(enum_class, name, None)
            if value is not None:
                return value
        return None

    def _summarize_non_pot_texture_plan(self, plan):
        summary = {"total": len(plan), "fix": 0, "ok": 0, "skip": 0, "errors": 0}
        for item in plan:
            action = item.get("action")
            if action == "fix":
                summary["fix"] += 1
            elif action == "ok":
                summary["ok"] += 1
            elif action == "error":
                summary["errors"] += 1
            else:
                summary["skip"] += 1
        return summary

    def _execute_non_pot_texture_plan(self, plan, summary, settings):
        targets = [item for item in plan if item.get("action") == "fix"]
        report = {
            "total": len(targets),
            "fixed": 0,
            "skipped": summary.get("ok", 0) + summary.get("skip", 0),
            "failed": summary.get("errors", 0),
            "snapshots": [],
            "failures": [],
            "save_after_fix": settings.get("save_after_fix", True),
        }
        for item in plan:
            if item.get("action") == "error":
                report["failures"].append({"name": item.get("name", item.get("asset_path", "<Unknown>")), "reason": item.get("reason", "未知错误")})
        if not targets:
            return report

        changed_before = report["fixed"]
        try:
            with unreal.ScopedEditorTransaction(f"AssetOrganizer Fix Non-POT Textures ({len(targets)} Textures)"):
                for item in targets:
                    self._apply_non_pot_texture_fix(item, settings, report)
        except Exception as e:
            if report["fixed"] == changed_before:
                report["failed"] += len(targets)
                report["failures"].append({
                    "name": "ScopedEditorTransaction",
                    "reason": f"事务创建失败，已取消执行以避免不可撤销修改：{str(e)}",
                })
            else:
                report["failed"] += 1
                report["failures"].append({"name": "ScopedEditorTransaction", "reason": str(e)})
            unreal.log_warning(f"AssetOrganizer: 非 POT 纹理修复事务异常 - {str(e)}")
        return report

    def _apply_non_pot_texture_fix(self, item, settings, report):
        texture = item.get("texture")
        asset_path = item.get("asset_path", "")
        name = item.get("name", asset_path)
        try:
            if texture is None:
                texture = self._load_texture2d_asset(item.get("asset_data"), asset_path)
            if texture is None:
                raise RuntimeError("纹理资产加载失败")
            target_mode = self._resolve_texture_power_of_two_mode()
            if target_mode is None:
                raise RuntimeError("TexturePowerOfTwoSetting.STRETCH_TO_POWER_OF_TWO 不可用")
            undo_ready = self._prepare_texture_asset_for_edit(texture, name)

            old_power_mode = self._get_texture_power_of_two_mode_text(texture)
            try:
                texture.set_editor_property("power_of_two_mode", target_mode)
            except Exception:
                texture.power_of_two_mode(target_mode)
            dirty_marked = self._mark_asset_dirty(texture)

            saved = False
            if settings.get("save_after_fix", True):
                saved = bool(unreal.EditorAssetLibrary.save_loaded_asset(texture, True))

            report["fixed"] += 1
            report["snapshots"].append({
                "name": name,
                "asset_path": asset_path,
                "size": f"{item.get('width', 0)}x{item.get('height', 0)}",
                "old_power_mode": old_power_mode,
                "new_power_mode": str(target_mode),
                "undo_ready": undo_ready,
                "dirty_marked": dirty_marked,
                "saved": saved,
            })
        except Exception as e:
            report["failed"] += 1
            report["failures"].append({"name": name, "reason": str(e)})
            unreal.log_warning(f"AssetOrganizer: 非 POT 纹理修复失败 {name} - {str(e)}")

    def _prepare_texture_asset_for_edit(self, texture, name):
        try:
            modify_result = texture.modify()
            if modify_result is False:
                unreal.log_warning(f"AssetOrganizer: {name} modify 返回 False，继续按资产属性写入并标脏")
                return False
            return True
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer: {name} modify 异常，继续按资产属性写入并标脏 - {str(e)}")
            return False

    def _mark_asset_dirty(self, asset):
        try:
            editor_asset_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
            return bool(editor_asset_subsystem.set_dirty_flag(asset, True))
        except Exception:
            pass
        try:
            package = unreal.EditorAssetLibrary.get_package_for_object(asset)
            if package is not None:
                package.set_dirty_flag(True)
                return True
        except Exception:
            pass
        return False

    # ------------------------------------------------------------------
    # 结果列表与报告
    # ------------------------------------------------------------------

    def _refresh_non_pot_texture_result_list(self, plan, summary):
        entries = self._build_non_pot_texture_result_entries(plan)
        self._non_pot_texture_result_entries = entries
        self._non_pot_texture_selected_result_indexes = []
        self._set_list_view_items("list_non_pot_texture_results", [entry["display"] for entry in entries])
        self._set_non_pot_texture_result_info(self._format_non_pot_texture_result_info(entries, summary))

    def _build_non_pot_texture_result_entries(self, plan):
        entries = []
        for plan_index, item in enumerate(plan):
            if item.get("action") not in ("fix", "error"):
                continue
            entries.append({
                "plan_index": plan_index,
                "asset_path": item.get("asset_path", ""),
                "name": item.get("name", "<UnknownTexture>"),
                "action": item.get("action", "skip"),
                "display": self._format_non_pot_texture_result_display(item, len(entries) + 1),
            })
        return entries

    def _format_non_pot_texture_result_display(self, item, row_index):
        status = "FIX" if item.get("action") == "fix" else "ERR"
        return f"{row_index:03d}. [{status}] {item.get('name', '<UnknownTexture>')}  {item.get('width', 0)}x{item.get('height', 0)}  {item.get('reason', '')}"

    def _format_non_pot_texture_result_info(self, entries, summary):
        return (
            f"结果明细：待修复 {summary.get('fix', 0)}，错误 {summary.get('errors', 0)}，"
            f"合规 {summary.get('ok', 0)}，跳过 {summary.get('skip', 0)}，扫描 {summary.get('total', 0)}。"
        )

    def _set_non_pot_texture_result_info(self, text):
        try:
            self.data.set_text("txt_non_pot_texture_result_info", text)
        except Exception:
            pass

    def _set_non_pot_texture_selected_result_indexes(self, indexes, update_selection):
        unique_indexes = []
        for index in indexes:
            try:
                index = int(index)
            except Exception:
                continue
            if 0 <= index < len(self._non_pot_texture_result_entries) and index not in unique_indexes:
                unique_indexes.append(index)
        self._non_pot_texture_selected_result_indexes = unique_indexes
        if update_selection:
            self._set_list_view_selection("list_non_pot_texture_results", unique_indexes)

    def _get_selected_non_pot_texture_result_entries(self):
        entries = []
        for index in self._non_pot_texture_selected_result_indexes:
            if 0 <= index < len(self._non_pot_texture_result_entries):
                entries.append(self._non_pot_texture_result_entries[index])
        return entries

    def _format_non_pot_texture_preview(self, plan, summary):
        lines = []
        lines.append("=== Non-POT Texture Preview ===")
        lines.append(f"Scope: {summary.get('scope_label', '/Game')}")
        lines.append(
            f"Fix: {summary['fix']} | OK: {summary['ok']} | Skip: {summary['skip']} | Errors: {summary['errors']} | Total: {summary['total']}"
        )
        scan_stats = summary.get("scan_stats") or []
        if scan_stats:
            lines.append("")
            lines.append("Scan Diagnostics:")
            for stat in scan_stats:
                lines.append(
                    f"- {stat.get('path', '/Game')} recursive={stat.get('recursive', True)} "
                    f"registry={stat.get('registry_raw', 0)} assets/{stat.get('registry_textures', 0)} Texture2D"
                )
                samples = stat.get("samples") or []
                if samples and stat.get("registry_textures", 0) == 0:
                    lines.append("  Samples:")
                    for sample in samples:
                        lines.append(f"  - {sample}")
        lines.append("")
        max_rows = 160
        for index, item in enumerate(plan[:max_rows], 1):
            action = item.get("action", "skip")
            if action == "fix":
                lines.append(f"{index:03d}. [FIX] {item['asset_path']}  {item['width']}x{item['height']}  {item['reason']}")
            elif action == "ok":
                lines.append(f"{index:03d}. [OK]  {item['asset_path']}  {item['width']}x{item['height']}")
            elif action == "error":
                lines.append(f"{index:03d}. [ERR] {item['asset_path']}  {item.get('reason', '')}")
            else:
                lines.append(f"{index:03d}. [SKIP] {item['asset_path']}  {item.get('reason', '')}")
        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... {len(plan) - max_rows} more rows omitted")
        return "\n".join(lines)

    def _format_non_pot_texture_report(self, report):
        lines = []
        lines.append("=== Last Non-POT Texture Fix Execution ===")
        lines.append(
            f"Fixed: {report['fixed']} | Skipped: {report['skipped']} | Failed: {report['failed']} | Total Targets: {report['total']} | Save: {report['save_after_fix']}"
        )
        lines.append("")
        max_rows = 100
        for index, snapshot in enumerate(report["snapshots"][:max_rows], 1):
            lines.append(
                f"{index:03d}. [FIXED] {snapshot['asset_path']}  size={snapshot['size']}  "
                f"{snapshot['old_power_mode']} -> {snapshot['new_power_mode']}  "
                f"dirty={snapshot.get('dirty_marked', False)}  undo={snapshot.get('undo_ready', False)}  saved={snapshot['saved']}"
            )
        if len(report["snapshots"]) > max_rows:
            lines.append(f"... {len(report['snapshots']) - max_rows} more fixed rows omitted")
        if report["failures"]:
            lines.append("")
            lines.append("Failures:")
            for failure in report["failures"][:30]:
                lines.append(f"- {failure['name']}: {failure['reason']}")
        return "\n".join(lines)

    def _build_non_pot_texture_batch_report(self, plan, summary):
        counters = {
            "Fix": summary.get("fix", 0),
            "OK": summary.get("ok", 0),
            "Skip": summary.get("skip", 0),
            "Errors": summary.get("errors", 0),
        }
        report = self._make_batch_report(
            "Non-POT Texture Preview",
            scope=summary.get("scope_label", "/Game"),
            total=summary.get("total", len(plan)),
            counters=counters,
        )
        for item in plan:
            action = item.get("action", "skip")
            status = {"fix": "FIX", "ok": "OK", "error": "ERR"}.get(action, "SKIP")
            reason = item.get("reason", "")
            if action == "error":
                report.setdefault("failures", []).append({"name": item.get("asset_path", "<Unknown>"), "reason": reason})
            self._add_batch_report_row(
                report,
                status,
                item.get("asset_path", "<UnknownTexture>"),
                reason=reason,
                details=item.get("details", []),
            )
        return report

    def _make_batch_report(self, title, scope="", total=0, counters=None):
        return {
            "title": title,
            "scope": scope,
            "total": int(total or 0),
            "counters": dict(counters or {}),
            "rows": [],
            "failures": [],
            "warnings": [],
            "export_path": "",
        }

    def _add_batch_report_row(self, report, status, name, reason="", details=None):
        row = {
            "status": str(status or "INFO"),
            "name": str(name or "<Unknown>"),
            "reason": str(reason or ""),
            "details": list(details or []),
        }
        report.setdefault("rows", []).append(row)
        return row

    def _format_batch_report_text(self, report, max_rows=300):
        lines = []
        lines.append(f"=== {report.get('title', 'Batch Report')} ===")
        scope = report.get("scope", "")
        if scope:
            lines.append(f"Scope: {scope}")
        lines.append(f"Total: {report.get('total', 0)}")
        counter_text = self._format_batch_report_counters(report.get("counters", {}))
        if counter_text:
            lines.append(counter_text)
        lines.append("")

        rows = list(report.get("rows", []))
        for index, row in enumerate(rows[:max_rows], 1):
            lines.append(f"{index:03d}. [{row.get('status', 'INFO')}] {row.get('name', '<Unknown>')}  {row.get('reason', '')}")
            for detail in (row.get("details") or [])[:5]:
                lines.append(f"      - {detail}")
        if len(rows) > max_rows:
            lines.append("")
            lines.append(f"... {len(rows) - max_rows} more rows omitted")

        warnings = report.get("warnings") or []
        if warnings:
            lines.append("")
            lines.append("Warnings:")
            for warning in warnings[:50]:
                lines.append(f"- {warning}")

        failures = report.get("failures") or []
        if failures:
            lines.append("")
            lines.append("Failures:")
            for failure in failures[:50]:
                name = failure.get("name", "<Unknown>") if isinstance(failure, dict) else "<Unknown>"
                reason = failure.get("reason", str(failure)) if isinstance(failure, dict) else str(failure)
                lines.append(f"- {name}: {reason}")
        return "\n".join(lines)

    def _format_batch_report_counters(self, counters):
        return " | ".join([f"{key}: {value}" for key, value in counters.items()])

    def _export_batch_report_text(self, file_prefix, report_text):
        export_dir = self._get_asset_organizer_export_dir()
        if not os.path.isdir(export_dir):
            os.makedirs(export_dir)
        safe_prefix = self._sanitize_export_file_prefix(file_prefix)
        file_name = f"{safe_prefix}_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        file_path = os.path.join(export_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)
        return file_path

    def _sanitize_export_file_prefix(self, file_prefix):
        text = str(file_prefix or "AssetOrganizerReport").strip()
        safe_chars = []
        for char in text:
            if char.isalnum() or char in ("_", "-"):
                safe_chars.append(char)
        return "".join(safe_chars) or "AssetOrganizerReport"

    def _get_asset_organizer_export_dir(self):
        try:
            saved_dir = unreal.Paths.project_saved_dir()
            if saved_dir:
                return os.path.join(saved_dir, "AssetOrganizer")
        except Exception:
            pass
        return os.path.join(os.getcwd(), "Saved", "AssetOrganizer")

    # ------------------------------------------------------------------
    # 通用 UI / 安全读取
    # ------------------------------------------------------------------

    def _is_power_of_two(self, value):
        value = int(value or 0)
        return value > 0 and (value & (value - 1)) == 0

    def _next_power_of_two(self, value):
        value = int(value or 0)
        if value <= 1:
            return 1
        return 1 << (value - 1).bit_length()

    def _safe_get_editor_property(self, obj, prop_name):
        try:
            return obj.get_editor_property(prop_name)
        except Exception:
            return None

    def _safe_object_name(self, obj):
        try:
            return obj.get_name()
        except Exception:
            try:
                return str(obj)
            except Exception:
                return "<UnknownObject>"

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
                unreal.log_warning(f"AssetOrganizer _set_list_view_items {method_name}: {str(e)}")
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
            unreal.log_warning(f"AssetOrganizer _get_list_view_selected_indexes: {str(e)}")
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
            unreal.log_warning(f"AssetOrganizer _set_list_view_selection: {str(e)}")
            return False


instance = None


def on_close():
    global instance
    if instance is not None:
        try:
            instance.on_closed()
        except Exception as e:
            unreal.log_warning(f"AssetOrganizer on_close: {str(e)}")
        finally:
            instance = None
