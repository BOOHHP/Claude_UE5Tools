## Add Menu Items to Unreal Editor[¶](#add-menu-items-to-unreal-editor)

This guide explains how to add custom menu items to the Unreal Editor using TAPython.

## Overview[¶](#overview)

TAPython allows you to add custom menu items to the Unreal Editor's menu bar. This is useful for creating custom tools and automation.

## Adding Menu Items[¶](#adding-menu-items)

### Using MenuConfig.json[¶](#using-menuconfigjson)

The easiest way to add menu items is through the `MenuConfig.json` file:

1. Locate the `MenuConfig.json` in your TAPython project
2. Add your menu entries following the JSON structure

```json
{
    "name": "My Menu",
    "items": [
        {
            "name": "My Tool",
            "command": "import my_module; my_module.run()"
        }
    ]
}
```

### Menu Entry Types[¶](#menu-entry-types)

- **Command**: Execute a Python command directly
- **ChameleonTools**: Open a Chameleon UI tool
- **Separator**: Add a separator line

## Example[¶](#example)

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "Chameleon Gallery",
            "ChameleonTools": "ChameleonGallery/ChameleonGallery.json"
        },
        {
            "name": "Python Console",
            "command": "unreal.PythonBPLib.exec_python_command('print(\"Hello!\")')"
        }
    ]
}
```

## Pre-defined Menu Entries[¶](#pre-defined-menu-entries)

TAPython provides several built-in menu entries. See [Pre-defined Menu Entry](https://www.tacolor.xyz/tapython/pre-defined_menu_entry.html) for more details.

## Next Steps[¶](#next-steps)

- [Using Slate to Add Interface](https://www.tacolor.xyz/tapython/using_slate_to_add_interface_for_python_tools.html)
- [Built-in Menu Items](https://www.tacolor.xyz/tapython/built-in_menu_items.html)

 [Previous](execute_python_command_in_unreal_engine.html) [Next](using_slate_to_add_interface_for_python_tools.html)
