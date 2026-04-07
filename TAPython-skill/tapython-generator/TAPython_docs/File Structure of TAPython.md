## File Structure of TAPython[¶](#file-structure-of-tapython)

This page describes the file structure of a TAPython project.

## Overview[¶](#overview)

A TAPython project has a specific folder structure that the plugin expects.

## Default Structure[¶](#default-structure)

```
<Your_Project>/
└── TA/
    └── TAPython/
        └── Python/
            ├── MenuConfig.json
            ├── Tools/
            │   ├── MyTool.py
            │   └── MyTool.json
            └── Utils/
                └── helpers.py
```

## Key Files[¶](#key-files)

### MenuConfig.json[¶](#menuconfigjson)

Configuration file for menu items. Defines:
- Menu structure
- Menu items and commands
- Keyboard shortcuts

### Python Modules[¶](#python-modules)

Your Python code files:
- Tool classes
- Utility functions
- Helper modules

### JSON Files[¶](#json-files)

Chameleon UI definitions for your tools.

## Customizing Structure[¶](#customizing-structure)

You can customize the folder structure in the TAPython settings.

## Best Practices[¶](#best-practices)

- Keep tools organized in subfolders
- Use descriptive names
- Separate UI (JSON) from logic (Python)

 [Previous](auto_complete_for_tapython.html) [Next](configs_of_tapython.html)
