# TAPython ChameleonData API

## Overview

ChameleonData is the core communication bridge between Python controller code and JSON-defined Slate UI in TAPython. It enables reading widget values, updating UI state, and controlling widget visibility — all without direct Slate access from Python.

Every interactive Chameleon tool uses ChameleonData to:
- **Read** user input from text fields, checkboxes, combo boxes, and spin boxes
- **Write** status messages, populate lists, and update display widgets
- **Control** widget visibility and enabled state dynamically
- **Store** custom variables for inter-widget communication

Widgets are identified by their `Aka` name (set in the JSON UI definition). All ChameleonData methods use this `Aka` string as the first parameter to target a specific widget.

---

## Initialization

### Getting a ChameleonData Instance

ChameleonData is obtained via `unreal.PythonBPLib.get_chameleon_data()`, typically in the controller's `__init__` method:

```python
import unreal

class MyToolController:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
```

### The %JsonPath Placeholder

In the JSON UI definition, `%JsonPath` is a special placeholder that gets replaced at runtime with the actual path to the JSON file. It must appear in `InitPyCmd`:

```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyToolController('%JsonPath')"
}
```

The `json_path` parameter received by the constructor is this resolved path. It uniquely identifies the tool instance and is required to obtain the correct ChameleonData object.

---

## Text Operations (读写文本)

### get_text(aka_name) → str

Retrieves the current text content of a text widget.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the target widget.

**Returns:** `str` — The current text content of the widget.

**Compatible Widgets:** `SEditableText`, `SMultiLineEditableText`, `STextBlock`

```python
# Get single-line input
name = self.data.get_text("input_name")

# Get multi-line text
description = self.data.get_text("description")

# Get display label text
current_status = self.data.get_text("status_label")
```

### set_text(aka_name, value)

Sets the text content of a text widget.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the target widget.
- `value` (str): The text to set.

**Compatible Widgets:** `SEditableText`, `SMultiLineEditableText`, `STextBlock`

```python
# Set input field value
self.data.set_text("input_name", "new value")

# Set multi-line content
self.data.set_text("description", "Line 1\nLine 2\nLine 3")

# Update status label
self.data.set_text("status_label", "Processing complete")
```

### set_text_color(aka_name, color)

Sets the text color of a text widget using RGBA values.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the target widget.
- `color` (list[float]): RGBA color as `[R, G, B, A]`, each value from `0.0` to `1.0`.

**Compatible Widgets:** `STextBlock`

```python
# Red — for errors
self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])

# Green — for success
self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])

# Yellow/Orange — for warnings
self.data.set_text_color("status_label", [1.0, 0.7, 0.3, 1.0])

# Gray — for neutral/ready state
self.data.set_text_color("status_label", [0.7, 0.7, 0.7, 1.0])
```

---

## Checkbox Operations (复选框)

### get_checkbox_state(aka_name) → bool

Retrieves the checked state of a checkbox.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the checkbox.

**Returns:** `bool` — `True` if checked, `False` if unchecked.

**Compatible Widgets:** `SCheckBox`

```python
is_checked = self.data.get_checkbox_state("option_enabled")
if is_checked:
    # Perform action when option is enabled
    pass
```

### set_checkbox_state(aka_name, state)

Sets the checked state of a checkbox.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the checkbox.
- `state` (bool): `True` to check, `False` to uncheck.

**Compatible Widgets:** `SCheckBox`

```python
# Check the box
self.data.set_checkbox_state("option_enabled", True)

# Uncheck the box
self.data.set_checkbox_state("option_enabled", False)
```

---

## ComboBox Operations (下拉选择)

### get_combo_box_selection(aka_name) → str

Retrieves the currently selected item from a dropdown.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the combo box.

**Returns:** `str` — The text of the currently selected item.

**Compatible Widgets:** `SComboBox`

```python
selected_mode = self.data.get_combo_box_selection("mode_selector")
if selected_mode == "Option A":
    # Handle Option A
    pass
```

### set_combo_box_selection(aka_name, item)

Sets the currently selected item in a dropdown.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the combo box.
- `item` (str): The text of the item to select. Must match an existing option.

**Compatible Widgets:** `SComboBox`

```python
self.data.set_combo_box_selection("mode_selector", "Option B")
```

---

## SpinBox Operations (数值输入)

### get_spin_box_value(aka_name) → float

Retrieves the current numeric value from a spin box.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the spin box.

**Returns:** `float` — The current numeric value.

**Compatible Widgets:** `SSpinBox`

```python
count = self.data.get_spin_box_value("count_input")
spawn_count = int(self.data.get_spin_box_value("spawn_count"))
```

### set_spin_box_value(aka_name, value)

Sets the numeric value of a spin box.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the spin box.
- `value` (float or int): The numeric value to set.

**Compatible Widgets:** `SSpinBox`

```python
self.data.set_spin_box_value("count_input", 25)
self.data.set_spin_box_value("threshold", 0.75)
```

---

## Button Operations (按钮)

### get_button_click(aka_name) → bool

Checks whether a button has been clicked (polling method).

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the button.

**Returns:** `bool` — `True` if the button was clicked.

**Compatible Widgets:** `SButton`

```python
if self.data.get_button_click("btn_execute"):
    self.execute_action()
```

> **Note:** Buttons are typically wired via `OnClick` in the JSON definition or through the `Aka`-based controller pattern. Use `get_button_click` for polling scenarios.

---

## List Operations (列表)

### set_list_items(aka_name, items)

Sets the items displayed in a list view.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the list view.
- `items` (list[str]): List of string items to display.

**Compatible Widgets:** `SListView`

```python
results = ["Item 1", "Item 2", "Item 3"]
self.data.set_list_items("results_list", results)
```

### get_selected_items(aka_name)

Retrieves the currently selected items from a list view.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the list view.

**Returns:** The selected item(s) from the list.

**Compatible Widgets:** `SListView`

```python
selected = self.data.get_selected_items("results_list")
```

### refresh_list(aka_name)

Refreshes a list view to reflect data changes.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the list view.

**Compatible Widgets:** `SListView`

```python
self.data.refresh_list("results_list")
```

---

## Widget Visibility & State

### set_visible(aka_name, visible)

Shows or hides a widget.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the widget.
- `visible` (bool): `True` to show, `False` to hide.

**Compatible Widgets:** Any widget with an `Aka`

```python
# Show a widget
self.data.set_visible("advanced_options", True)

# Hide a widget
self.data.set_visible("advanced_options", False)
```

### set_enabled(aka_name, enabled)

Enables or disables a widget (grayed out when disabled).

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the widget.
- `enabled` (bool): `True` to enable, `False` to disable.

**Compatible Widgets:** Any widget with an `Aka`

```python
# Disable button during processing
self.data.set_enabled("btn_execute", False)

# Re-enable after completion
self.data.set_enabled("btn_execute", True)
```

### set_focus(aka_name)

Sets keyboard focus to a widget.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the widget.

**Compatible Widgets:** Any focusable widget (text inputs, buttons, etc.)

```python
self.data.set_focus("input_name")
```

---

## Variable Operations (变量)

### get_var(name) → str

Retrieves the value of a built-in placeholder or custom variable.

**Parameters:**
- `name` (str): The variable name. Built-in placeholders start with `%`.

**Returns:** `str` — The variable value.

**Built-in Placeholders:**
| Placeholder | Description |
|---|---|
| `%toolPath` | The tool's runtime path |
| `%widgetPath` | The source widget's path (SButton OnClick only) |
| `%selectedObjects` | Currently selected objects in the editor |

```python
# Get built-in placeholder
tool_path = self.data.get_var("%toolPath")
widget_path = self.data.get_var("%widgetPath")

# Get custom variable
value = self.data.get_var("myVar")
```

### set_var(name, value)

Sets a custom variable value for inter-widget communication.

**Parameters:**
- `name` (str): The variable name.
- `value` (str): The value to store.

```python
self.data.set_var("myVar", "myValue")
```

---

## Refresh Operations (刷新)

### refresh(tool_path)

Performs a full UI refresh of the tool.

**Parameters:**
- `tool_path` (str): The path of the tool to refresh.

```python
self.data.refresh(self.json_path)
```

### refresh_widget(aka_name)

Refreshes a single widget.

**Parameters:**
- `aka_name` (str): The `Aka` identifier of the widget to refresh.

```python
self.data.refresh_widget("results_list")
```

---

## Snapshot Operations (快照)

These are static methods on `unreal.ChameleonData` for capturing tool window screenshots.

### snapshot_chameleon_window(json_path, override_window_size)

Captures a screenshot of a Chameleon tool window.

```python
saved_path = unreal.ChameleonData.snapshot_chameleon_window(json_path, override_window_size=(800, 600))
```

### get_chameleon_window_size(json_path)

Gets the current window size of a Chameleon tool.

```python
current_size = unreal.ChameleonData.get_chameleon_window_size(json_path)
```

### get_top_scroll_box_offsets(json_path)

Gets scroll offsets for calculating full content height (useful for full-page snapshots).

```python
offsets = self.data.get_top_scroll_box_offsets(self.json_path)
# Returns dict with "ScrollOffsetOfEnd", "viewFraction", etc.
```

> **Note:** The maximum interface length capturable in Unreal Engine is 16384 pixels. See [Take UI Snapshot](Take%20UI%20Snapshot.md) for a full example.

---

## Error Handling Patterns

**CRITICAL:** All ChameleonData calls that interact with `unreal.xxx` must be wrapped in `try-except` blocks.

### Basic Pattern

```python
def execute_action(self):
    try:
        input_value = self.data.get_text("input_field")

        if not input_value:
            self.data.set_text("status_label", "Error: Input required")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        # ... business logic ...

        self.data.set_text("status_label", "Success!")
        self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        unreal.log_error(error_msg)
        self.data.set_text("status_label", error_msg)
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

### Nested Error Handling for Batch Operations

```python
def process_assets(self):
    try:
        assets = unreal.PythonBPLib.get_selected_assets()

        if not assets:
            self.data.set_text("status", "No assets selected")
            return

        processed = 0
        failed = 0

        for asset in assets:
            try:
                asset_name = asset.get_name()
                # Process individual asset...
                processed += 1
            except Exception as e:
                failed += 1
                unreal.log_error(f"Failed: {asset.get_name()}: {str(e)}")
                continue

        self.data.set_text("status", f"Processed: {processed}, Failed: {failed}")

    except Exception as e:
        unreal.log_error(f"Process failed: {str(e)}")
        self.data.set_text("status", f"Error: {str(e)}")
```

---

## Common Patterns

### Reading Form Input → Processing → Updating Status

```python
def rename_assets(self):
    try:
        prefix = self.data.get_text("prefix_input").strip()
        remove_existing = self.data.get_checkbox_state("remove_prefix_check")

        if not prefix:
            self.data.set_text("status_label", "Error: Prefix required")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        selected_assets = unreal.PythonBPLib.get_selected_assets()

        if not selected_assets:
            self.data.set_text("status_label", "Error: No assets selected")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        # ... process assets ...

        self.data.set_text("status_label", f"Renamed {len(selected_assets)} assets")
        self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])

    except Exception as e:
        self.data.set_text("status_label", f"Error: {str(e)}")
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

### Reading Multiple Widget Types

```python
def spawn_actors(self):
    try:
        blueprint_name = self.data.get_combo_box_selection("blueprint_selector")
        spawn_count = int(self.data.get_spin_box_value("spawn_count"))
        random_rotation = self.data.get_checkbox_state("random_rotation_check")
        # ... use all values together ...
    except Exception as e:
        unreal.log_error(str(e))
```

### Populating Dropdowns and Lists Dynamically

```python
def search_assets(self):
    try:
        search_query = self.data.get_text("search_input").strip().lower()
        type_filter = self.data.get_combo_box_selection("type_filter")

        # ... gather results ...

        results = ["Asset_A", "Asset_B", "Asset_C"]
        self.data.set_list_items("results_list", results)

        self.data.set_text("status_label", f"Found {len(results)} assets")
        self.data.set_text_color("status_label", [0.7, 0.7, 0.7, 1.0])

    except Exception as e:
        self.data.set_text("status_label", f"Error: {str(e)}")
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

### Persisting and Restoring Settings

```python
def save_settings(self):
    try:
        config = {
            "output_path": self.data.get_text("setting_output_path"),
            "prefix": self.data.get_text("setting_prefix"),
            "auto_save": self.data.get_checkbox_state("setting_auto_save")
        }
        # Save config to file...

    except Exception as e:
        self.data.set_text("status_label", f"Error: {str(e)}")

def load_settings(self, config):
    try:
        self.data.set_text("setting_output_path", config.get("output_path", "/Game/Output/"))
        self.data.set_text("setting_prefix", config.get("prefix", "SM_"))
        self.data.set_checkbox_state("setting_auto_save", config.get("auto_save", False))

        self.data.set_text("status_label", "Settings loaded")
        self.data.set_text_color("status_label", [0.7, 0.7, 0.7, 1.0])

    except Exception as e:
        self.data.set_text("status_label", f"Error: {str(e)}")
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

### Toggling UI Elements Based on State

```python
def toggle_advanced_options(self):
    show_advanced = self.data.get_checkbox_state("show_advanced")
    self.data.set_visible("advanced_panel", show_advanced)
    self.data.set_enabled("btn_advanced_action", show_advanced)
```

---

## Quick Reference Table

| Method | Compatible Widgets | Direction | Return Type |
|---|---|---|---|
| `get_text(aka)` | SEditableText, SMultiLineEditableText, STextBlock | Read | `str` |
| `set_text(aka, value)` | SEditableText, SMultiLineEditableText, STextBlock | Write | None |
| `set_text_color(aka, rgba)` | STextBlock | Write | None |
| `get_checkbox_state(aka)` | SCheckBox | Read | `bool` |
| `set_checkbox_state(aka, state)` | SCheckBox | Write | None |
| `get_combo_box_selection(aka)` | SComboBox | Read | `str` |
| `set_combo_box_selection(aka, item)` | SComboBox | Write | None |
| `get_spin_box_value(aka)` | SSpinBox | Read | `float` |
| `set_spin_box_value(aka, value)` | SSpinBox | Write | None |
| `get_button_click(aka)` | SButton | Read | `bool` |
| `set_list_items(aka, items)` | SListView | Write | None |
| `get_selected_items(aka)` | SListView | Read | list |
| `refresh_list(aka)` | SListView | Write | None |
| `set_visible(aka, visible)` | Any widget | Write | None |
| `set_enabled(aka, enabled)` | Any widget | Write | None |
| `set_focus(aka)` | Focusable widgets | Write | None |
| `get_var(name)` | N/A (variables) | Read | `str` |
| `set_var(name, value)` | N/A (variables) | Write | None |
| `refresh(tool_path)` | N/A (full UI) | Write | None |
| `refresh_widget(aka)` | Any widget | Write | None |

---

## Resources

- [Full ChameleonData API Reference](https://www.tacolor.xyz/pages/ChameleonDataAPI.html) — Official online documentation
- [Python Editor Extended API](https://www.tacolor.xyz/tapython/pythonlib_api.html)
- [Chameleon Gallery](https://www.tacolor.xyz/tapython/chameleon_gallery.html)

## See Also

- [Get Value from Slate](Get%20Value%20from%20Slate.md) — Reading widget values
- [Modifying Slate Though Python](Modifying%20Slate%20Though%20Python.md) — Updating widgets from Python
- [Variable Placeholder](Variable%20Placeholder.md) — Built-in and custom variables
- [Using List View](Using%20List%20View.md) — List view details
- [Widget Catalog](../widgets/Catalog.md) — All available widgets with JSON definitions
