## Tab Context Menu[¶](#tab-context-menu)

This guide explains how to add context menus to Chameleon Tool tabs.

## Overview[¶](#overview)

You can add global or per-tool context menus to Chameleon Tools.

## Global Context Menu[¶](#global-context-menu)

Add to MenuConfig.json:

```json
{
    "OnTabContextMenu": {
        "name": "TA Python Tab",
        "items": [
            {
                "name": "Reload This Tool",
                "command": "unreal.ChameleonData.request_close(%tool_path); unreal.ChameleonData.launch_chameleon_tool(%tool_path)"
            }
        ]
    }
}
```

## Individual Context Menu[¶](#individual-context-menu)

Each Chameleon Tool can add its own context menu:

```json
{
    "TabLabel": "Example",
    "InitTabSize": [200, 123],
    "InitPyCmd": "import Example; chameleon_example = Example.MinimalExample.MinimalExample(%JsonPath)",
    "Root": {...},
    "OnTabContextMenu": {
        "items": [
            {
                "name": "Reset Click Count",
                "command": "chameleon_example.reset_click_count()"
            }
        ]
    }
}
```

## OnOutlineMenu[¶](#onoutlinemenu)

```json
{
    "OnOutlineMenu": {
        "name": "Python Menu On OutlineMenu",
        "items": [
            {
                "name": "Print selected actors",
                "command": "print(unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_selected_level_actors())"
            }
        ]
    }
}
```

Note:
- These new context menus only support UE5
- OnTabContextMenu also supports sub menu items

 [Previous](external_json.html) [Next](reload_tool.html)
