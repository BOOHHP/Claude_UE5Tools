## Pre-defined Menu Entry[¶](#pre-defined-menu-entry)

This page documents pre-defined menu entries available in TAPython.

## Overview[¶](#overview)

TAPython provides several built-in menu entries that you can use in your MenuConfig.json.

## Available Entries[¶](#available-entries)

### Python Console[¶](#python-console)

Opens the Python console:

```json
{
    "name": "Python Console",
    "command": "unreal.PythonBPLib.toggle_python_console()"
}
```

### Chameleon Gallery[¶](#chameleon-gallery)

Opens the Chameleon Gallery:

```json
{
    "name": "Chameleon Gallery",
    "ChameleonTools": "ChameleonGallery/ChameleonGallery.json"
}
```

### Reload Python[¶](#reload-python)

Reloads Python modules:

```json
{
    "name": "Reload Python",
    "command": "import importlib; importlib.reload(unreal)"
}
```

## Customizing[¶](#customizing)

You can mix pre-defined entries with custom ones:

```json
{
    "items": [
        {
            "name": "Python Console",
            "command": "unreal.PythonBPLib.toggle_python_console()"
        },
        {
            "name": "My Tool",
            "command": "import my_tool; my_tool.run()"
        }
    ]
}
```

 [Previous](use_3rd_python_package.html) [Next](menu_tools_anchor.html)
