# TA 工作区说明（TAPython 插件工程）

中文版 | [English](README.md)

本目录用于管理 **Unreal Engine 5 + TAPython** 编辑器工具开发内容，包含：

- `TAPython/`：插件配置、Python 脚本工具、UI 菜单配置
- `TAPython-skill/`：Copilot 技能库（用于生成/辅助 TAPython 工具开发）
- `TAPython_UE5_Plugin.zip`：插件分发包（可用于部署到其他工程/机器）

## 1. 目录结构

```text
TA/
├── TAPython/
│   ├── Config/
│   │   └── config.ini
│   ├── Python/
│   │   ├── BatchRenameTool/
│   │   ├── SceneSelectTool/
│   │   └── ...
│   └── UI/
│       └── MenuConfig.json
├── TAPython-skill/
│   ├── tapython-generator/
│   └── ue-api-navigator/
└── TAPython_UE5_Plugin.zip
```

## 2. TAPython 插件部署

> 重要限制：该插件仅支持 **UE 项目全英文路径**（项目目录、父目录、用户名路径等均建议为英文且不含空格/中文/特殊字符）。
> 若路径包含中文或特殊字符，可能出现 Python 路径加载失败、菜单不显示或工具初始化异常。

使用压缩包部署：

1. 解压 `TAPython_UE5_Plugin.zip`。
2. 将解压后的 `TAPython` 目录放到目标工程插件目录。
3. 启用插件并重启 UE5。

## 3. 核心配置说明

关键配置文件：`TAPython/Config/config.ini`

当前工程使用的核心配置：

```ini
[Settings]
PythonContentFolder=TA/TAPython/Python
MenuConfigFilePath=TA/TAPython/UI/MenuConfig.json
```

含义：

- `PythonContentFolder`：工具 Python 脚本根目录。
- `MenuConfigFilePath`：编辑器菜单配置入口（工具注册总表）。

建议：

- 迁移到新工程时，优先检查这两个路径是否仍与目录结构一致。
- 若菜单不显示，先校验 `MenuConfig.json` 是否是合法 JSON。

### 另一种常用配置方式（项目设置内配置 Python 额外路径）

当插件部署完成后，也可以在 UE 项目内通过 Python 插件设置补充脚本路径：

1. 打开 UE 项目，进入 `项目设置 -> 插件 -> Python`。
2. 在 `额外路径`（Additional Paths）中新增一条索引，指向 `TA/TAPython/Python` 文件夹。
3. 重启 UE 编辑器。
4. 重启后打开 TAPython 菜单中的 Chameleon Sketch，若界面提示 `Python Path Ready.`，说明路径配置已生效。

## 4. 菜单与工具加载机制

- 菜单入口由 `TAPython/UI/MenuConfig.json` 管理。
- `OnToolBarChameleon.items` 是常用工具入口（如 Batch Rename、Scene Selection Tool）。
- 每个工具通常包含：
  - 一个 UI JSON（界面布局）
  - 一个 Python 控制器（逻辑）
  - 可选 `__init__.py`（模块导入）

示例：

- `TAPython/Python/SceneSelectTool/SceneSelectTool.json`
- `TAPython/Python/SceneSelectTool/SceneSelectTool.py`

## 5. 新增工具的最小流程

1. 在 `TAPython/Python/<ToolName>/` 下创建：
   - `<ToolName>.json`
   - `<ToolName>.py`
   - `__init__.py`
2. 在 `TAPython/UI/MenuConfig.json` 的 `OnToolBarChameleon.items` 增加菜单项：
   - `name`
   - `tooltip`
   - `ChameleonTools`
3. 在 UE 中重新加载工具或重启编辑器验证。

## 6. 与 TAPython-skill 的协作方式

`TAPython-skill/` 用于 AI 协作开发：

- `tapython-generator`：按需求生成 MenuConfig/UI/Controller 脚手架
- `ue-api-navigator`：按 UE PythonStub 提供精确 API 签名

推荐用法：

1. 先用 `tapython-generator` 生成结构。
2. 再用 `ue-api-navigator` 校验 `unreal.xxx` API 调用签名。
3. 最后将产物落地到 `TAPython/Python` 与 `TAPython/UI/MenuConfig.json`。

## 7. 常见排查

### 菜单项可见但点开报错

- 检查工具 Python 文件中的 `unreal` API 是否有异常处理。
- 检查 UI JSON 的事件绑定是否引用正确控制器实例。

### 当前关卡相关 API 在不同环境报错

- 使用多级回退策略（例如优先 `EditorLevelLibrary.get_current_level()`，失败再降级）。
- 避免只依赖单一 `World` 属性。

### 工具说明不清

- 在 `MenuConfig.json` 为每个工具添加简洁 `tooltip`，便于团队成员识别用途。

## 8. 版本管理建议

- 工具代码改动后，建议同步提交：
  - `TAPython/Python/...`
  - `TAPython/UI/MenuConfig.json`
  - 必要时文档（本 README 或技能文档）
- 保持“功能改动 + 菜单配置 + 文档”同一次提交，便于回溯。

## 9. TAPython 其它 UE5 版本下载指引

如需查找 TAPython 在其它 UE5 版本的插件发布包，请访问：

- https://github.com/cgerchenhp/UE_TAPython_Plugin_Release/releases
