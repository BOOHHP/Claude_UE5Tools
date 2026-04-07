## Configs of TAPython[¶](#configs-of-tapython)

This page documents the configuration options for TAPython.

## Overview[¶](#overview)

TAPython can be configured through various configuration files and settings.

## Configuration Files[¶](#configuration-files)

### MenuConfig.json[¶](#menuconfigjson)

Defines the menu structure and items:

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "My Tool",
            "command": "import my_tool; my_tool.run()"
        }
    ]
}
```

### Settings[¶](#settings)

Configure TAPython through the Editor Preferences:
- Python path
- Auto-reload settings
- Console settings

## Environment Variables[¶](#environment-variables)

- `TAPYTHON_PATH`: Custom Python path
- `TAPYTHON_DEBUG`: Enable debug mode

## Common Configurations[¶](#common-configurations)

### Auto-reload Python[¶](#auto-reload-python)

Enable automatic Python module reloading when tools are opened.

### Python Console Settings[¶](#python-console-settings)

Configure console behavior:
- Font size
- History size
- Auto-complete

 [Previous](file_structure_of_tapython.html) [Next](use_3rd_python_package.html)
