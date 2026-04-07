## Execute Order of Python Code in Chameleon Tool[¶](#execute-order-of-python-code-in-chameleon-tool)

This guide explains the order in which Python code executes in Chameleon tools.

## Overview[¶](#overview)

Understanding the execution order helps you properly initialize and manage your tools.

## Execution Sequence[¶](#execution-sequence)

### 1. JSON Loading[¶](#1-json-loading)

The JSON file is parsed and UI is created.

### 2. InitPyCmd[¶](#2-initpycmd)

The Python command specified in `InitPyCmd` runs first:

```json
{
    "InitPyCmd": "import MyTool; tool = MyTool.MyTool(%JsonPath)"
}
```

This is where you initialize your Python class.

### 3. Event Callbacks[¶](#3-event-callbacks)

After initialization, event handlers can be triggered:
- Button clicks
- Selection changes
- Other UI events

## InitPyCmd[¶](#initpycmd)

### Purpose[¶](#purpose)

Initialize the tool and store reference to ChameleonData.

### Best Practice[¶](#best-practice)

```python
class MyTool:
    def __init__(self, json_path):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
        # Additional initialization
```

## Late Initialization[¶](#late-initialization)

Use `LateInitPyCmd` for code that needs to run after UI is fully created:

```json
{
    "LateInitPyCmd": "tool.late_init()"
}
```

## Reload Logic[¶](#reload-logic)

### Auto-reload[¶](#auto-reload)

To auto-reload when tool opens:

```json
{
    "InitPyCmd": "import importlib, MyTool; importlib.reload(MyTool); tool = MyTool.MyTool(%JsonPath)"
}
```

 [Previous](modifying_slate_though_python.html) [Next](external_json.html)
