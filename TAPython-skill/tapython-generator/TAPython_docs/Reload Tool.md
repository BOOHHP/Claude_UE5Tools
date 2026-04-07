## Reload Tool[¶](#reload-tool)

This guide explains how to reload Python logic in Chameleon Tools.

## Automatically Reload Python Logic[¶](#automatically-reload-python-logic)

Use InitCmd to reload Python module each time the tool starts:

```json
{
    "InitPyCmd": "import importlib, your_tools_module; importlib.reload(your_tools_module); your_tool_inst = your_tools_module.Tool(%jsonPath)"
}
```

Remove the reload statement once development is complete.

## How importlib.reload() Works[¶](#how-importlibreload-works)

Python caches every imported module in `sys.modules`. When you call `import my_module` a second time, Python returns the cached version instead of re-reading the file.

`importlib.reload()` re-executes the module source code and updates the existing module object in place. This means any new functions, classes, or variables defined in the updated file become available immediately.

**Important:** `importlib.reload()` only reloads the single module you pass to it. Dependencies are NOT automatically reloaded. If module A imports module B, reloading A does **not** reload B. You must reload B first, then reload A so that A picks up the changes from the new B.

```python
import importlib
import my_utils
import my_tool
importlib.reload(my_utils)  # Reload dependency first
importlib.reload(my_tool)   # Then reload the main module
```

## Reload Through Buttons or Menus[¶](#reload-through-buttons-or-menus)

Add a temporary button to reload:

```json
{
    "SButton": {
        "Text": "Reload",
        "HAlign": "Center",
        "VAlign": "Center",
        "OnClick": "import your_utils, importlib; importlib.reload(your_utils)"
    }
}
```

For code involving interface logic, update when reopening the interface through quickly updating Python logic.

## Hot Reload Without Restart[¶](#hot-reload-without-restart)

Use this method to reload Python without reopening the interface:

Reference: [Reload Python without relaunch Chameleon Tool](https://www.tacolor.xyz/TipsOfDay/Reload_Python_without_relaunch_Chameleon_Tool.html)

## Hot Reload Best Practices[¶](#hot-reload-best-practices)

- Always reload dependencies before the modules that use them. If `my_tool` imports `my_utils`, reload `my_utils` first.
- Use `importlib.reload()` in `InitPyCmd` during development for fast iteration, but remove these calls for production builds.
- Keep reload buttons visible during development so you can quickly test changes without reopening the tool.
- Test thoroughly after reload — some module-level state may not reset properly and can cause unexpected behavior.

## Common Issues During Reload[¶](#common-issues-during-reload)

- **Stale references**: Old objects may still reference the previous module version. Re-create instances after reload to ensure they use the updated class definitions.
- **Singleton re-initialization**: If your module uses a module-level pattern like `instance = None`, make sure `InitPyCmd` re-assigns it after reload so the new code path is used.
- **Cached imports**: Sub-modules may not reload because Python cached them in `sys.modules`. You must explicitly call `importlib.reload()` on each sub-module that changed.
- **Class identity**: `isinstance()` checks may fail after reload because the class object in the new module is a different object than the one used to create existing instances.

## Development vs Production[¶](#development-vs-production)

**Development**: Use `importlib.reload()` in `InitPyCmd` for fast iteration. Add reload buttons to the UI so you can test changes without reopening the tool.

**Production**: Remove all `importlib.reload()` calls and reload buttons. Rely on editor restart to pick up updates.

Development InitPyCmd with reload:

```json
{
    "InitPyCmd": "import importlib, my_tool; importlib.reload(my_tool); inst = my_tool.Tool(%jsonPath)"
}
```

Production InitPyCmd without reload:

```json
{
    "InitPyCmd": "import my_tool; inst = my_tool.Tool(%jsonPath)"
}
```

## See Also[¶](#see-also)

- [Execute Order of Python Code in Chameleon Tool](Execute Order of Python Code in Chameleon Tool.md)
- [Chameleon Tool](Chameleon Tool.md)
- [On Close Callbacks](On Close Callbacks.md)

 [Previous](tab_context_menu.html) [Next](control_other_tools.html)
