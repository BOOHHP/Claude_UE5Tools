## Context Menus for Slate Widget[¶](#context-menus-for-slate-widget)

This guide explains how to add context menus to Slate widgets in Chameleon.

## Overview[¶](#overview)

Context menus provide quick access to actions when right-clicking on UI elements.

## Adding Context Menus[¶](#adding-context-menus)

### JSON Configuration[¶](#json-configuration)

Add a context menu to any widget:

```json
{
    "SButton": {
        "Text": "Click Me",
        "ContextMenu": {
            "items": [
                {
                    "name": "Action 1",
                    "command": "tool.do_action_1()"
                },
                {
                    "name": "Action 2",
                    "command": "tool.do_action_2()"
                }
            ]
        }
    }
}
```

## Menu Item Types[¶](#menu-item-types)

### Simple Command[¶](#simple-command)

Execute a Python command:

```json
{
    "name": "Print Message",
    "command": "print('Hello!')"
}
```

### Submenu[¶](#submenu)

Create nested menus:

```json
{
    "name": "Submenu",
    "items": [
        {
            "name": "Sub Action",
            "command": "tool.sub_action()"
        }
    ]
}
```

## Use Cases[¶](#use-cases)

- Quick actions on buttons
- Context-specific options
- Navigation menus

 [Previous](menu_tools_anchor.html) [Next](slate_overview.html)
