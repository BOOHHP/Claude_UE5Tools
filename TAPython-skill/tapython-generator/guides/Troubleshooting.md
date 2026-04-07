# 故障排除指南 / Troubleshooting Guide

Common issues encountered during TAPython tool development and their solutions.

> This guide focuses on diagnosing and resolving runtime issues. For architectural mistakes and anti-patterns, see [Common Pitfalls](../pitfalls/CommonPitfalls.md).

---

## 工具不显示 / Tool Not Appearing

**Symptom**: Menu entry or tool window does not appear in the UE editor.

| Cause | Fix |
|-------|-----|
| `MenuConfig.json` not in correct directory | Place under `<Project>/TA/TAPython/Python/` |
| Path in `ChameleonTools` is wrong | Must be relative: `"ToolName/ToolName.json"`, not absolute |
| Missing or malformed `ChameleonTools` key | Ensure the key exists and points to a valid `.json` file |
| Menu anchor point not matching | Default anchor is `"OnToolBarChameleon"`; verify with [Menu Tools Anchor](../TAPython_docs/Menu%20Tools%20Anchor.md) |
| JSON syntax error in MenuConfig | Validate JSON — a single trailing comma prevents loading |

**Quick check**: Open the Output Log and search for `TAPython` or `Chameleon` errors on editor startup.

---

## UI 不渲染 / UI Not Rendering

**Symptom**: Tool window opens but is blank, partially rendered, or crashes immediately.

### JSON Syntax Errors
```
❌ Trailing comma:   "Slots": [ {"STextBlock": {"Text": "Hello"}}, ]
✅ Fixed:            "Slots": [ {"STextBlock": {"Text": "Hello"}} ]
```
Run your JSON through a validator before loading. Most editors (VS Code, PyCharm) highlight syntax errors.

### Missing Root Container
Every UI JSON must have a `"Root"` key with a container widget:
```json
{
    "Root": {
        "SScrollBox": {
            "Slots": [ /* widgets */ ]
        }
    }
}
```
Without `Root`, the tool window will be empty. See [templates/UI.json.md](../templates/UI.json.md) for the full template.

### Invalid Widget Names
Widget names are case-sensitive and must match Slate class names exactly:
```
❌ "STextblock"  →  ✅ "STextBlock"
❌ "Sbutton"     →  ✅ "SButton"
```
Refer to the [Widget Catalog](../widgets/Catalog.md) for valid names.

### InitPyCmd Errors
If `InitPyCmd` fails, the controller never initializes and no UI interactions work:
```json
"InitPyCmd": "import ToolName; importlib.reload(ToolName); ToolName.instance = ToolName.ToolNameController('%JsonPath')"
```
- Ensure the module name matches the `.py` filename exactly
- `%JsonPath` is required — do not hard-code paths
- Check the Output Log for import or syntax errors

---

## Python 报错 / Python Errors

### Module Import Failures
```
ModuleNotFoundError: No module named 'MyTool'
```
- Verify the `.py` file is in `<Project>/TA/TAPython/Python/` or a subdirectory on the Python path
- Check that the filename matches the `import` statement in `InitPyCmd`
- Ensure no circular imports between modules

### ChameleonData Initialization Errors
```python
# This fails if json_path is empty or wrong
self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
```
- `json_path` comes from `%JsonPath` — never hard-code it
- If `self.data` is `None`, all subsequent `get_text` / `set_text` calls will fail

### unreal API Not Available
```python
import unreal  # Only works inside UE editor context
```
- The `unreal` module is only available when Python runs inside the editor
- You cannot test TAPython scripts from a standalone terminal
- Use the [Python Console](../TAPython_docs/How%20to%20Debug%20Python%20in%20UE.md) inside UE for interactive testing

### Singleton Re-initialization Issues
When using `importlib.reload()`, the old instance is replaced. This is expected during development, but if other code holds a reference to the old instance, it becomes stale. Always access via `ModuleName.instance`.

---

## 数据桥接失败 / Data Bridge Failures

### Aka Name Mismatch
The `Aka` in the JSON must exactly match the string used in Python:
```json
{"SEditableText": {"Aka": "input_prefix"}}
```
```python
# ✅ Matches
text = self.data.get_text("input_prefix")

# ❌ Wrong name — returns empty or errors
text = self.data.get_text("prefix_input")
```

### get_text Returns Empty
- The widget may not have been initialized yet — check `InitPyCmd` ran successfully
- `STextBlock` with no default `"Text"` returns empty until set via `set_text`
- `SEditableText` returns empty until the user types something

### set_text Target Not Found
```python
self.data.set_text("status_label", "Done")  # Fails if "status_label" Aka doesn't exist
```
- Verify the Aka exists in the UI JSON
- Ensure the widget type supports `set_text` (works on `STextBlock`, `SEditableText`, `SMultiLineEditableText`)

---

## 调试工作流 / Debugging Workflow

### Step 1: Check the Output Log
Open **Window → Developer Tools → Output Log** in UE. Filter by `LogPython` to see Python-related messages.

### Step 2: Add Debug Logging
```python
unreal.log("Debug: reached this point")
unreal.log_warning(f"Variable value: {some_var}")
unreal.log_error("Something went wrong")
```
These appear in the Output Log with different severity colors.

### Step 3: Use the Python Console
Test code snippets interactively via **TA Python → Python Console** before integrating into your tool.

### Step 4: Breakpoint Debugging
For complex issues, attach a debugger (VS Code with `debugpy`, or PyCharm remote debug). See [How to Debug Python in UE](../TAPython_docs/How%20to%20Debug%20Python%20in%20UE.md) for setup instructions.

### Step 5: Validate JSON
Use an external JSON validator or your IDE's built-in checker. Common issues:
- Trailing commas after the last element
- Missing closing braces/brackets
- Unescaped special characters in strings

---

## 日志定位 / Log Analysis

### Where to Find Logs
- **Output Log** in UE editor (primary source)
- Project log files: `<Project>/Saved/Logs/`
- TAPython-specific messages are prefixed with `LogPython` or `LogTAPython`

### Common Error Patterns

| Log Message | Likely Cause |
|-------------|-------------|
| `ModuleNotFoundError` | Python file not on path or filename mismatch |
| `AttributeError: 'NoneType'` | `ChameleonData` not initialized (bad `json_path`) |
| `KeyError` in widget access | Aka name mismatch between JSON and Python |
| `JSONDecodeError` | Syntax error in UI JSON file |
| `No module named 'unreal'` | Running script outside UE editor context |

### Stack Trace Interpretation
Python stack traces in UE appear in the Output Log. Read from bottom to top:
1. **Last line**: The actual error message
2. **Lines above**: The call chain — find your code (not internal UE code) to locate the issue
3. **File paths**: Confirm the error is in your tool file, not a different module

---

## 参考链接 / References

- [Common Pitfalls](../pitfalls/CommonPitfalls.md) — architectural mistakes and prevention
- [How to Debug Python in UE](../TAPython_docs/How%20to%20Debug%20Python%20in%20UE.md) — debugger setup
- [Execute Order of Python Code](../TAPython_docs/Execute%20Order%20of%20Python%20Code%20in%20Chameleon%20Tool.md) — initialization sequence
- [Chameleon Tool](../TAPython_docs/Chameleon%20Tool.md) — core UI system reference
- [Widget Catalog](../widgets/Catalog.md) — valid widget names and properties
