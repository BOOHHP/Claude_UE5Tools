import unreal

class BatchRenameController:
    def __init__(self, jsonPath):
        # 【修复核心】使用 PythonBPLib 获取已存在的 ChameleonData 实例，而不是直接实例化
        self.data = unreal.PythonBPLib.get_chameleon_data(jsonPath)

    def execute_rename(self):
        try:
            # 1. 从界面获取用户输入的前缀
            prefix = self.data.get_text('input_prefix')
            if not prefix:
                self.data.set_text('txt_status', "警告: 前缀不能为空！")
                unreal.log_warning("BatchRenameTool: Prefix is empty.")
                return

            # 2. 获取 Content Browser 中当前选中的资产
            selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
            if not selected_assets:
                self.data.set_text('txt_status', "提示: 未选中任何资产。请先在浏览器中框选。")
                unreal.log_warning("BatchRenameTool: No assets selected.")
                return

            success_count = 0
            total_count = len(selected_assets)

            # 3. 遍历资产执行重命名逻辑
            for asset in selected_assets:
                old_name = asset.get_name()
                old_path = asset.get_path_name()
                
                # 拼接新名称
                new_name = prefix + old_name
                
                # 获取所在包的目录并生成新的完整资产路径
                package_path = unreal.Paths.get_path(old_path)
                new_path = f"{package_path}/{new_name}.{new_name}"
                
                # 执行引擎重命名操作
                is_renamed = unreal.EditorAssetLibrary.rename_asset(old_path, new_path)
                if is_renamed:
                    success_count += 1
                else:
                    unreal.log_error(f"BatchRenameTool: 无法重命名资产 {old_name}")

            # 4. 将执行结果反馈给 UI 面板
            result_msg = f"完成! 成功重命名了 {success_count} / {total_count} 个资产。"
            self.data.set_text('txt_status', result_msg)
            unreal.log(f"BatchRenameTool: {result_msg}")

        except Exception as e:
            # 防御性后备：捕获一切异常输出至引擎 Log，并同步给 UI
            error_msg = f"错误异常: {str(e)}"
            unreal.log_error(f"BatchRenameTool Exception: {error_msg}")
            self.data.set_text('txt_status', error_msg)