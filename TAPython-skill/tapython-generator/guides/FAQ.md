# 常见问题 / Frequently Asked Questions

Practical answers to common TAPython development questions, with code examples and links to detailed docs.

---

## 安装与配置 / Installation & Setup

**Q: TAPython 支持哪些 UE 版本？**
A: TAPython targets Unreal Engine 5.x, with this skill specifically designed for UE 5.5. Check the [TAPython installation guide](../TAPython_docs/How%20to%20install%20TAPython.md) for version-specific notes.

**Q: 文件应该放在哪个目录？**
A: All TAPython files go under `<Project>/TA/TAPython/Python/`. The typical structure is:
```
<Project>/TA/TAPython/Python/
├── MenuConfig.json          # Menu registration
├── ToolName/
│   ├── ToolName.json        # UI definition
│   └── ToolName.py          # Controller logic
```
See [File Structure of TAPython](../TAPython_docs/File%20Structure%20of%20TAPython.md) for the full layout.

**Q: 如何验证 TAPython 安装成功？**
A: After installing, launch UE and check:
1. A **TA Python** menu appears in the editor menu bar
2. Open **TA Python → Python Console** — if it opens, the plugin is active
3. Check Output Log for any `TAPython` error messages on startup

---

## UI 开发 / UI Development

**Q: 如何选择合适的容器组件？**
A: Use this decision guide:

| Container | Use When |
|-----------|----------|
| `SVerticalBox` | Stacking widgets top-to-bottom (most common) |
| `SHorizontalBox` | Placing widgets side-by-side in a row |
| `SScrollBox` | Content may exceed window height (use as Root) |
| `SBox` | Need fixed dimensions or padding around a widget |
| `SGridPanel` | Arranging widgets in a grid layout |

See [Box Layout](../TAPython_docs/Box%20Layout.md) and [Grid Layout](../TAPython_docs/Grid%20Layout.md) for details.

**Q: Aka 字段命名有什么规范？**
A: Follow these conventions for consistency:
- Buttons: `btn_action` (e.g., `btn_execute`, `btn_search`)
- Text inputs: `input_purpose` (e.g., `input_prefix`, `input_search`)
- Status labels: `status_context` (e.g., `status_label`, `status_count`)
- Checkboxes: `chk_option` (e.g., `chk_recursive`, `chk_overwrite`)
- All Aka values must be unique within a single tool

**Q: 如何实现动态 UI（显示/隐藏组件）？**
A: Use `set_visibility` through ChameleonData:
```python
# Hide a widget
self.data.set_visibility("widget_aka", False)
# Show a widget
self.data.set_visibility("widget_aka", True)
```
The widget must have an `Aka` field. For more complex dynamic UI, see [ChameleonData API](../TAPython_docs/TA%20Python%20ChameleonData%20API.md).

**Q: 支持哪些 Slate 组件？**
A: TAPython supports a wide range of Slate widgets including `SButton`, `STextBlock`, `SEditableText`, `SMultiLineEditableText`, `SCheckBox`, `SComboBox`, `SSpinBox`, `SImage`, `SListView`, and all major container types. See the [Widget Catalog](../widgets/Catalog.md) for the complete list with usage examples.

---

## Python 控制器 / Controller

**Q: 为什么要用单例模式？**
A: The singleton pattern ensures only one controller instance exists per tool window. Without it:
- Re-opening the tool creates duplicate instances that leak memory
- Old `ChameleonData` connections become stale
- Multiple instances compete for the same UI widgets

The pattern: `Module.instance = Module.Controller('%JsonPath')` in `InitPyCmd`. See [Pitfall 3](../pitfalls/CommonPitfalls.md#pitfall-3-no-singleton-pattern) for details.

**Q: 如何在工具关闭时清理资源？**
A: Define a cleanup method and call it from `OnClosePyCmd`:
```json
{
    "OnClosePyCmd": "MyTool.instance.cleanup(); MyTool.instance = None"
}
```
```python
def cleanup(self):
    try:
        self.large_data = None
        # Release file handles, timers, etc.
    except Exception as e:
        unreal.log_error(f"Cleanup failed: {str(e)}")
```
See [On Close Callbacks](../TAPython_docs/On%20Close%20Callbacks.md) for the full lifecycle.

**Q: 如何访问当前选中的资产？**
A: Use the Unreal Python API:
```python
try:
    assets = unreal.PythonBPLib.get_selected_assets()
    if not assets:
        self.data.set_text("status_label", "No assets selected")
        return
    for asset in assets:
        unreal.log(f"Selected: {asset.get_name()}")
except Exception as e:
    unreal.log_error(f"Failed to get selection: {str(e)}")
```
See [Most Used Editor APIs](../TAPython_docs/Most%20Used%20Editor%20APIs.md) for more operations.

**Q: try-except 是否会影响性能？**
A: In normal execution (no exception raised), `try-except` has negligible overhead. The cost only matters when exceptions are actually thrown. Always use try-except around `unreal.xxx` calls — correctness and stability far outweigh any micro-performance concern. See [Pitfall 4](../pitfalls/CommonPitfalls.md#pitfall-4-missing-error-handling).

---

## 架构设计 / Architecture

**Q: 为什么不能在 UI JSON 中写内联 Python？**
A: Inline Python in UI events (e.g., `"OnClick": "print('hi')"`) breaks MVC separation, has no error handling, cannot be debugged with an IDE, and cannot be tested. Use `Aka` identifiers and handle all logic in the Python controller. See [Pitfall 1](../pitfalls/CommonPitfalls.md#pitfall-1-inline-python-in-ui-events) for the full explanation.

**Q: 一个工具能有多个窗口吗？**
A: Each `ChameleonTools` entry in `MenuConfig.json` creates one tool window. To have multiple windows, register multiple entries pointing to different JSON files. Each window should have its own controller instance and `InitPyCmd`.

**Q: 如何在多个工具之间共享逻辑？**
A: Extract shared logic into a separate Python module:
```python
# shared_utils.py
def validate_asset_selection():
    assets = unreal.PythonBPLib.get_selected_assets()
    return assets if assets else []

# ToolA.py
import shared_utils
assets = shared_utils.validate_asset_selection()
```
Place the shared module in the TAPython Python directory so all tools can import it.

---

## 开发效率 / Development

**Q: 如何实现热重载？**
A: Add `importlib.reload()` to your `InitPyCmd`:
```json
"InitPyCmd": "import importlib, MyTool; importlib.reload(MyTool); MyTool.instance = MyTool.MyToolController('%JsonPath')"
```
Close and reopen the tool tab to reload your Python changes without restarting UE. Remove `importlib.reload()` for production. See [Reload Tool](../TAPython_docs/Reload%20Tool.md) for more details.

**Q: 有没有调试 Python 的方法？**
A: Yes, multiple approaches:
1. **Output Log**: Use `unreal.log()`, `unreal.log_warning()`, `unreal.log_error()`
2. **Python Console**: Test snippets interactively via **TA Python → Python Console**
3. **VS Code + debugpy**: Attach a full debugger with breakpoints
4. **PyCharm Remote Debug**: Professional edition supports remote debugging

See [How to Debug Python in UE](../TAPython_docs/How%20to%20Debug%20Python%20in%20UE.md) for setup instructions.

**Q: JSON 格式错误如何快速定位？**
A: Three approaches:
1. Use VS Code or another editor with JSON validation — errors are highlighted in real-time
2. Check the UE Output Log on tool load for `JSONDecodeError` messages with line numbers
3. Use an online JSON validator (e.g., jsonlint.com) to find the exact error location

Common culprits: trailing commas, missing closing braces, unquoted keys. See the [Troubleshooting Guide](./Troubleshooting.md#ui-不渲染--ui-not-rendering) for more.

---

## 参考链接 / References

- [SKILL.md](../SKILL.md) — core architecture and workflow
- [Common Pitfalls](../pitfalls/CommonPitfalls.md) — mistakes to avoid
- [Common Patterns](../patterns/CommonPatterns.md) — implementation templates
- [Troubleshooting Guide](./Troubleshooting.md) — runtime issue diagnosis
- [Performance Guide](./Performance.md) — optimization tips
