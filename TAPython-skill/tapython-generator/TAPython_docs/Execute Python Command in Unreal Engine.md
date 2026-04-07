## Execute Python Command in Unreal Engine[¶](#execute-python-command-in-unreal-engine)

This guide explains various ways to execute Python code in Unreal Engine using TAPython.

## Methods to Run Python[¶](#methods-to-run-python)

### 1. Python Console[¶](#1-python-console)

The easiest way to test Python code:

1. Open Unreal Editor
2. Go to **TA Python > Python Console** (or press `Tab + P`)
3. Type your Python code in the console
4. Press **Enter** to execute

### 2. Execute from File[¶](#2-execute-from-file)

Execute a Python script file:

```python
import unreal

# Execute a Python file
unreal.PythonBPLib.exec_python_file("path/to/your/script.py")
```

### 3. Execute Command[¶](#3-execute-command)

Run Python code directly:

```python
unreal.PythonBPLib.exec_python_command("print('Hello UE!')")
```

### 4. Python Editor Utility Widget[¶](#4-python-editor-utility-widget)

Create custom editor tools using Python:

1. Create a new Asset > Blueprint > Editor Utility Widget
2. In the graph, use Python to access editor APIs
3. Compile and open the widget in the editor

## Built-in Commands[¶](#built-in-commands)

TAPython provides several built-in commands:

- `unreal.PythonBPLib.get_editor_subsystem()` - Get editor subsystems
- `unreal.PythonBPLib.get_selected_assets()` - Get selected assets
- `unreal.PythonBPLib.get_selected_actors()` - Get selected actors

## Best Practices[¶](#best-practices)

- Use the Python Console for testing
- Save reusable code as Python modules
- Use proper error handling in production tools

## Next Steps[¶](#next-steps)

- [Add Menu Items to Unreal Editor](https://www.tacolor.xyz/tapython/add_menu_items_to_unreal_editor.html)
- [Using Slate to Add Interface](https://www.tacolor.xyz/tapython/using_slate_to_add_interface_for_python_tools.html)

 [Previous](open_unreal_python_project_in_ide.html) [Next](add_menu_items_to_unreal_editor.html)
