## Use Shortcut Keys[¶](#use-shortcut-keys)

This guide explains how to add keyboard shortcuts to your TAPython tools.

## Overview[¶](#overview)

TAPython allows you to bind keyboard shortcuts to Python commands in the Unreal Editor.

## Adding Shortcuts[¶](#adding-shortcuts)

### Through Menu Config[¶](#through-menu-config)

Add keyboard shortcuts through the MenuConfig.json:

```json
{
    "name": "My Menu",
    "items": [
        {
            "name": "Run Tool",
            "command": "import my_tool; my_tool.run()",
            "shortcut": "Ctrl+Shift+T"
        }
    ]
}
```

### Common Shortcut Formats[¶](#common-shortcut-formats)

- `Ctrl+C` - Control + C
- `Alt+S` - Alt + S
- `Ctrl+Shift+T` - Control + Shift + T
- `F5` - Function key F5

## Best Practices[¶](#best-practices)

- Use meaningful shortcut combinations
- Avoid conflicting with existing UE shortcuts
- Document your shortcuts for users

## Examples[¶](#examples)

```json
{
    "name": "Python Tools",
    "items": [
        {
            "name": "Quick Run",
            "command": "import quick_run; quick_run.execute()",
            "shortcut": "Ctrl+Alt+R"
        }
    ]
}
```

 [Previous](polishing_ui_with_sketch.html) [Next](get_object_in_unreal_engine_editor.html)
