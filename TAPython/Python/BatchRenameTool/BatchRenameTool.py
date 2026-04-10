import unreal

class BatchRenameController:
    def __init__(self, jsonPath):
        self.data = unreal.PythonBPLib.get_chameleon_data(jsonPath)
        self._last_plan = []
        self._last_signature = None

    def preview_rename(self):
        try:
            plan, summary = self._build_plan_from_ui()
            self._last_plan = plan
            self._last_signature = self._build_signature_from_ui()

            preview_text = self._format_preview(plan, summary)
            self.data.set_text('txt_preview', preview_text)

            status_msg = (
                f"预览完成：可执行 {summary['ready']}，跳过 {summary['skipped']}，"
                f"冲突失败 {summary['conflict_error']}，共 {summary['total']}。"
            )
            self.data.set_text('txt_status', status_msg)
            unreal.log(f"BatchRenameTool: {status_msg}")
        except Exception as e:
            error_msg = f"预览失败：{str(e)}"
            unreal.log_error(f"BatchRenameTool preview exception: {error_msg}")
            self.data.set_text('txt_status', error_msg)

    def execute_rename(self):
        try:
            plan, summary = self._get_plan_for_execute()

            success_count = 0
            failed_count = 0
            skipped_count = summary['skipped']

            for item in plan:
                if item['action'] != 'rename':
                    continue

                is_renamed = unreal.EditorAssetLibrary.rename_asset(item['old_path'], item['new_path'])
                if is_renamed:
                    success_count += 1
                else:
                    failed_count += 1
                    unreal.log_error(
                        f"BatchRenameTool: 重命名失败 {item['old_name']} -> {item['new_name']}"
                    )

            result_msg = (
                f"执行完成：成功 {success_count}，失败 {failed_count}，跳过 {skipped_count}，"
                f"总计 {summary['total']}。"
            )
            self.data.set_text('txt_status', result_msg)
            unreal.log(f"BatchRenameTool: {result_msg}")

            # 执行后自动刷新预览，确保 UI 状态与当前资产状态一致
            self.preview_rename()

        except Exception as e:
            error_msg = f"执行失败：{str(e)}"
            unreal.log_error(f"BatchRenameTool execute exception: {error_msg}")
            self.data.set_text('txt_status', error_msg)

    def _get_plan_for_execute(self):
        signature = self._build_signature_from_ui()

        if self._last_plan and self._last_signature == signature:
            plan = list(self._last_plan)
            summary = self._summarize_plan(plan)
            return plan, summary

        plan, summary = self._build_plan_from_ui()
        self._last_plan = plan
        self._last_signature = signature
        return plan, summary

    def _build_plan_from_ui(self):
        prefix = str(self.data.get_text('input_prefix')).strip()
        if not prefix:
            raise ValueError("前缀不能为空")

        selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
        if not selected_assets:
            raise ValueError("未选中任何资产，请先在内容浏览器中选择目标资产")

        skip_prefixed = self.data.get_is_checked('chk_skip_prefixed')
        auto_resolve = self.data.get_is_checked('chk_auto_conflict')

        selected_paths = [asset.get_path_name() for asset in selected_assets]
        selected_set = set(selected_paths)
        reserved = set()
        plan = []

        for asset in selected_assets:
            old_name = asset.get_name()
            old_path = asset.get_path_name()
            package_path = unreal.Paths.get_path(old_path)

            if skip_prefixed and old_name.startswith(prefix):
                plan.append({
                    'action': 'skip',
                    'old_name': old_name,
                    'old_path': old_path,
                    'new_name': old_name,
                    'new_path': old_path,
                    'reason': '已带此前缀'
                })
                continue

            base_name = f"{prefix}{old_name}"
            candidate_name = base_name
            candidate_path = f"{package_path}/{candidate_name}.{candidate_name}"

            if candidate_path == old_path:
                plan.append({
                    'action': 'skip',
                    'old_name': old_name,
                    'old_path': old_path,
                    'new_name': old_name,
                    'new_path': old_path,
                    'reason': '名称未变化'
                })
                continue

            conflict = self._has_conflict(candidate_path, old_path, selected_set, reserved)

            if conflict and not auto_resolve:
                plan.append({
                    'action': 'conflict_error',
                    'old_name': old_name,
                    'old_path': old_path,
                    'new_name': candidate_name,
                    'new_path': candidate_path,
                    'reason': '目标名称冲突（未启用自动处理）'
                })
                continue

            if conflict and auto_resolve:
                solved_name, solved_path = self._resolve_conflict_name(
                    package_path, base_name, old_path, selected_set, reserved
                )
                if solved_path is None:
                    plan.append({
                        'action': 'conflict_error',
                        'old_name': old_name,
                        'old_path': old_path,
                        'new_name': candidate_name,
                        'new_path': candidate_path,
                        'reason': '自动处理冲突失败'
                    })
                    continue

                reserved.add(solved_path)
                plan.append({
                    'action': 'rename',
                    'old_name': old_name,
                    'old_path': old_path,
                    'new_name': solved_name,
                    'new_path': solved_path,
                    'reason': '冲突自动加后缀'
                })
                continue

            reserved.add(candidate_path)
            plan.append({
                'action': 'rename',
                'old_name': old_name,
                'old_path': old_path,
                'new_name': candidate_name,
                'new_path': candidate_path,
                'reason': ''
            })

        return plan, self._summarize_plan(plan)

    def _build_signature_from_ui(self):
        selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
        selected_paths = sorted([asset.get_path_name() for asset in selected_assets])
        prefix = str(self.data.get_text('input_prefix')).strip()
        skip_prefixed = self.data.get_is_checked('chk_skip_prefixed')
        auto_resolve = self.data.get_is_checked('chk_auto_conflict')
        return (prefix, skip_prefixed, auto_resolve, tuple(selected_paths))

    def _has_conflict(self, candidate_path, old_path, selected_set, reserved):
        if candidate_path in reserved:
            return True

        if candidate_path in selected_set and candidate_path != old_path:
            return True

        if unreal.EditorAssetLibrary.does_asset_exist(candidate_path) and candidate_path != old_path:
            return True

        return False

    def _resolve_conflict_name(self, package_path, base_name, old_path, selected_set, reserved):
        for idx in range(1, 1000):
            candidate_name = f"{base_name}_{idx:03d}"
            candidate_path = f"{package_path}/{candidate_name}.{candidate_name}"
            if not self._has_conflict(candidate_path, old_path, selected_set, reserved):
                return candidate_name, candidate_path
        return None, None

    def _summarize_plan(self, plan):
        summary = {
            'total': len(plan),
            'ready': 0,
            'skipped': 0,
            'conflict_error': 0,
        }
        for item in plan:
            if item['action'] == 'rename':
                summary['ready'] += 1
            elif item['action'] == 'skip':
                summary['skipped'] += 1
            elif item['action'] == 'conflict_error':
                summary['conflict_error'] += 1
        return summary

    def _format_preview(self, plan, summary):
        lines = []
        lines.append("=== 预览结果 ===")
        lines.append(
            f"可执行: {summary['ready']} | 跳过: {summary['skipped']} | 冲突失败: {summary['conflict_error']} | 总计: {summary['total']}"
        )
        lines.append("")

        if not plan:
            lines.append("无可处理资产。")
            return "\n".join(lines)

        max_rows = 120
        for i, item in enumerate(plan[:max_rows], 1):
            if item['action'] == 'rename':
                suffix = f" ({item['reason']})" if item['reason'] else ""
                lines.append(f"{i:03d}. [RENAME] {item['old_name']} -> {item['new_name']}{suffix}")
            elif item['action'] == 'skip':
                lines.append(f"{i:03d}. [SKIP]   {item['old_name']}  ({item['reason']})")
            else:
                lines.append(f"{i:03d}. [ERROR]  {item['old_name']}  ({item['reason']})")

        if len(plan) > max_rows:
            lines.append("")
            lines.append(f"... 其余 {len(plan) - max_rows} 条已省略")

        return "\n".join(lines)