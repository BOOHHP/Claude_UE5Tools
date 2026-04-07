## Chameleon Tool[¶](#chameleon-tool)

This page provides an overview of the Chameleon Tool system.

## Overview[¶](#overview)

The Chameleon Tool is TAPython's UI system for creating editor tools using JSON and Python.

## Tool Lifecycle[¶](#tool-lifecycle)

A Chameleon Tool goes through three phases during its lifetime:

- **Init**: The JSON file is loaded and the UI is created. The `InitPyCmd` command runs, which typically imports a module and creates the Python controller instance. This is where you set up initial state and store a reference to the `ChameleonData` object.
- **Use**: The user interacts with the UI. Event callbacks such as `OnClick`, `OnSelectionChanged`, `OnTextCommitted`, etc. invoke Python methods on the controller instance to handle logic.
- **Close**: When the tool tab is closed, `OnClosePyCmd` runs. Use this to release references, save state, or perform any necessary cleanup.

To define a close callback, add `OnClosePyCmd` to your JSON:

```json
{
    "TabLabel": "My Tool",
    "InitPyCmd": "import MyTool; tool = MyTool.MyTool(%JsonPath)",
    "OnClosePyCmd": "tool.on_close()",
    "Root": {
        "SVerticalBox": {
            "Slots": []
        }
    }
}
```

For more details, see [Execute Order of Python Code in Chameleon Tool](Execute Order of Python Code in Chameleon Tool.md) and [On Close Callbacks](On Close Callbacks.md).

## Creating a Chameleon Tool[¶](#creating-a-chameleon-tool)

### Step 1: Create JSON File[¶](#step-1-create-json-file)

Create a JSON file defining the UI:

```json
{
    "TabLabel": "My Tool",
    "InitPyCmd": "import MyTool; tool = MyTool.MyTool(%JsonPath)",
    "Root": {
        "SVerticalBox": {
            "Slots": []
        }
    }
}
```

### Step 2: Create Python Class[¶](#step-2-create-python-class)

```python
class MyTool:
    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
```

### Step 3: Launch the Tool[¶](#step-3-launch-the-tool)

```python
unreal.ChameleonData.launch_chameleon_tool("path/to/tool.json")
```

### Step 4: Register in Menu[¶](#step-4-register-in-menu)

To make your tool accessible from the editor menu, register it in `MenuConfig.json`:

```json
{
    "name": "TA Python",
    "items": [
        {"name": "My Tool", "ChameleonTools": "MyTool/MyTool.json"}
    ]
}
```

This adds a "My Tool" entry under the "TA Python" menu that launches your Chameleon Tool when clicked.

## Key Features[¶](#key-features)

- JSON-based UI definition
- Python callbacks for interactivity
- Reusable UI components
- External JSON support

## How ChameleonData Connects UI to Python[¶](#how-chameleondata-connects-ui-to-python)

`ChameleonData` is the bridge between UI widgets defined in JSON and your Python code. To reference a widget from Python, give it an `Aka` (alias) field in the JSON definition:

```json
{
    "SEditableTextBox": {
        "Aka": "MyTextInput",
        "HintText": "Enter a value..."
    }
}
```

Then use the `ChameleonData` object to **get** widget values:

```python
text_value = self.data.get_text("MyTextInput")
is_checked = self.data.get_checkbox_state("MyCheckbox")
selected_index = self.data.get_combo_box_selected_item("MyDropdown")
```

Or **set** widget values:

```python
self.data.set_text("MyTextInput", "Hello World")
self.data.set_visible("MyPanel", True)
self.data.set_checkbox_state("MyCheckbox", True)
self.data.set_enabled("MyButton", False)
```

For a complete reference, see [Get Value from Slate](Get Value from Slate.md) and [Modifying Slate Though Python](Modifying Slate Though Python.md).

## Advanced Usage Patterns[¶](#advanced-usage-patterns)

### Multi-Window Tools[¶](#multi-window-tools)

You can open additional Chameleon Tool windows at runtime using `launch_chameleon_tool()`. This is useful for tools that spawn secondary panels or dialogs:

```python
unreal.ChameleonData.launch_chameleon_tool("path/to/secondary_panel.json")
```

### Dynamic UI Updates[¶](#dynamic-ui-updates)

Modify widget visibility, enabled state, and content dynamically in response to user actions:

```python
def on_mode_changed(self, mode):
    self.data.set_visible("AdvancedOptions", mode == "Advanced")
    self.data.set_text("StatusLabel", f"Mode: {mode}")
    self.data.set_enabled("RunButton", mode != "Disabled")
```

### Singleton Pattern[¶](#singleton-pattern)

Use a module-level variable to maintain a reliable reference to your tool instance. This prevents the instance from being garbage-collected and allows other scripts to access it:

```python
instance = None

class MyTool:
    def __init__(self, json_path):
        global instance
        instance = self
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

    def on_close(self):
        global instance
        instance = None
```

## File Structure[¶](#file-structure)

```
Tools/
├── MyTool/
│   ├── MyTool.json
│   └── MyTool.py
└── MenuConfig.json
```

## Resources[¶](#resources)

- [Chameleon Gallery](https://www.tacolor.xyz/tapython/chameleon_gallery.html)
- [Variable Placeholder](https://www.tacolor.xyz/tapython/variable_placeholder.html)
- [Execute Order of Python Code in Chameleon Tool](Execute Order of Python Code in Chameleon Tool.md)
- [On Close Callbacks](On Close Callbacks.md)
- [Reload Tool](Reload Tool.md)
- [Variable Placeholder](Variable Placeholder.md)
- [Get Value from Slate](Get Value from Slate.md)
- [Modifying Slate Though Python](Modifying Slate Though Python.md)

 [Previous](modal_window.html) [Next](variable_placeholder.html)
