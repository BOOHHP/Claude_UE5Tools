## Menu Tools Anchor[¶](#menu-tools-anchor)

This page explains how to use menu tools anchor in TAPython.

## Overview[¶](#overview)

Menu tools anchor determines where menu items appear in the Unreal Editor menu.

## Using Anchors[¶](#using-anchors)

### Default Anchor[¶](#default-anchor)

Menu items appear under the TA Python menu by default.

### Custom Anchors[¶](#custom-anchors)

You can place menu items in different locations:

```json
{
    "name": "My Tool",
    "command": "import my_tool; my_tool.run()",
    "menu": "File"
}
```

## Available Anchors[¶](#available-anchors)

- **File**: File menu
- **Edit**: Edit menu
- **View**: View menu
- **Window**: Window menu
- **Help**: Help menu

## Examples[¶](#examples)

Adding to the File menu:

```json
{
    "items": [
        {
            "name": "My Custom Tool",
            "command": "import my_tool; my_tool.run()",
            "menu": "File"
        }
    ]
}
```

 [Previous](pre-defined_menu_entry.html) [Next](context_menus_for_slate_widget.html)
