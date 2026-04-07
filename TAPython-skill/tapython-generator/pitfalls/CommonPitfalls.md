# Common Pitfalls & Solutions

This document catalogs the most common mistakes when developing TAPython tools and provides correct solutions with explanations.

## Critical Pitfalls

1. [Inline Python in UI Events](#pitfall-1-inline-python-in-ui-events)
2. [Missing Aka Fields](#pitfall-2-missing-aka-fields)
3. [No Singleton Pattern](#pitfall-3-no-singleton-pattern)
4. [Missing Error Handling](#pitfall-4-missing-error-handling)
5. [No Cleanup on Close](#pitfall-5-no-cleanup-on-close)
6. [UI Overflow / No Scrolling](#pitfall-6-ui-overflow--no-scrolling)
7. [No Auto-Reload During Development](#pitfall-7-no-auto-reload-during-development)
8. [UE5 Level API Compatibility Issues](#pitfall-8-ue5-level-api-compatibility-issues)
9. [Current-Level Filtering Is Too Fragile](#pitfall-9-current-level-filtering-is-too-fragile)
10. [Missing Menu Tooltip Descriptions](#pitfall-10-missing-menu-tooltip-descriptions)

---

## Pitfall 1: Inline Python in UI Events

### The Problem

Embedding Python code directly in UI event handlers breaks MVC separation and makes debugging difficult.

❌ **Wrong**:
```json
{
    "SButton": {
        "Text": "Click",
        "OnClick": "print('clicked')"
    }
}
```

### Why It's Wrong

1. **Breaks MVC architecture** - UI should not contain business logic
2. **Hard to debug** - No line numbers, no IDE support
3. **No error handling** - Exceptions crash silently
4. **Difficult to maintain** - Logic scattered between files
5. **Cannot test** - No way to unit test inline code

### The Solution

Use `Aka` identifiers and handle all logic in the Python controller.

✅ **Right**:
```json
{
    "SButton": {
        "Aka": "btn_click",
        "Text": "Click"
    }
}
```

```python
# In Python controller
def handle_click(self):
    try:
        print("Button clicked")
        # Business logic here
    except Exception as e:
        unreal.log_error(f"Click handler failed: {str(e)}")
```

### How to Apply

- **Never use**: `OnClick`, `OnValueChanged`, `OnCheckStateChanged` with inline Python
- **Always use**: `Aka` fields and handle in controller methods
- **Benefit**: Centralized logic, proper error handling, testable code

---

## Pitfall 2: Missing Aka Fields

### The Problem

Interactive widgets without `Aka` identifiers cannot be accessed from Python.

❌ **Wrong**:
```json
{
    "SEditableText": {
        "HintText": "Enter name"
    }
}
```

### Why It's Wrong

1. **Cannot read value** - No way to get user input
2. **Cannot set value** - Cannot update widget programmatically
3. **Cannot bind events** - No identifier to reference
4. **Breaks data flow** - UI becomes one-way only

### The Solution

Add unique `Aka` identifiers to all interactive widgets.

✅ **Right**:
```json
{
    "SEditableText": {
        "Aka": "name_input",
        "HintText": "Enter name"
    }
}
```

```python
# In Python controller
name = self.data.get_text("name_input")
self.data.set_text("name_input", "default value")
```

### How to Apply

**Widgets requiring Aka**:
- `SButton` - Action triggers
- `SEditableText` - Text input
- `SMultiLineEditableText` - Multi-line input
- `SCheckBox` - Boolean options
- `SComboBox` - Dropdown selection
- `SSpinBox` - Numeric input
- `STextBlock` - Dynamic status/labels
- `SListView` - List displays

**Naming Convention**:
- Use descriptive names: `prefix_input`, `btn_execute`, `status_label`
- Be consistent: `btn_` prefix for buttons, `_input` suffix for inputs
- Keep unique: No duplicate Aka values within a tool

---

## Pitfall 3: No Singleton Pattern

### The Problem

Creating multiple tool instances leads to memory leaks and unpredictable behavior.

❌ **Wrong**:
```json
{
    "InitPyCmd": "tool = MyTool.MyTool('%JsonPath')"
}
```

### Why It's Wrong

1. **Multiple instances** - Each tool open creates new instance
2. **Memory leaks** - Old instances not garbage collected
3. **Stale references** - ChameleonData connections become invalid
4. **Unpredictable behavior** - Multiple instances compete for resources

### The Solution

Use the singleton pattern with module-level instance storage.

✅ **Right**:
```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')"
}
```

```python
# In Python file (MyTool.py)
class MyTool:
    def __init__(self, json_path):
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)
        # ...

# Module-level singleton storage
instance = None
```

### How to Apply

**InitPyCmd pattern**:
```json
"InitPyCmd": "import [ModuleName]; [ModuleName].instance = [ModuleName].[ControllerClass]('%JsonPath')"
```

**OnClosePyCmd pattern**:
```json
"OnClosePyCmd": "[ModuleName].instance.cleanup(); [ModuleName].instance = None"
```

**Python file**:
```python
# At bottom of file
instance = None  # Module-level singleton storage
```

---

## Pitfall 4: Missing Error Handling

### The Problem

Unreal Engine API calls can fail for many reasons. Unhandled errors crash the tool and leave users confused.

❌ **Wrong**:
```python
def process(self):
    assets = unreal.PythonBPLib.get_selected_assets()
    # Process assets without error checking
    for asset in assets:
        asset.rename("new_name")
```

### Why It's Wrong

1. **Silent failures** - User doesn't know what failed
2. **Tool crashes** - Unhandled exceptions break the tool
3. **No debugging info** - No error logs to investigate
4. **Poor UX** - User has no feedback on failure
5. **Partial completion** - Some assets processed, others not

### The Solution

Wrap ALL `unreal.xxx` calls in try-except blocks and provide user feedback.

✅ **Right**:
```python
def process(self):
    try:
        assets = unreal.PythonBPLib.get_selected_assets()

        if not assets:
            self.data.set_text("status", "No assets selected")
            return

        processed = 0
        failed = 0

        for asset in assets:
            try:
                # Attempt operation
                asset.rename("new_name")
                processed += 1

            except Exception as e:
                failed += 1
                unreal.log_error(f"Failed to rename {asset.get_name()}: {str(e)}")
                continue

        # Report results
        self.data.set_text("status", f"Processed: {processed}, Failed: {failed}")

    except Exception as e:
        unreal.log_error(f"Process failed: {str(e)}")
        self.data.set_text("status", f"Error: {str(e)}")
```

### How to Apply

**Error handling levels**:

1. **Method level** - Wrap entire method
```python
def method(self):
    try:
        # Method logic
        pass
    except Exception as e:
        unreal.log_error(f"Method failed: {str(e)}")
        self.data.set_text("status", f"Error: {str(e)}")
```

2. **Operation level** - Wrap individual operations
```python
for asset in assets:
    try:
        # Process single asset
        pass
    except Exception as e:
        unreal.log_error(f"Asset failed: {str(e)}")
        continue  # Continue processing others
```

3. **User feedback** - Always inform the user
```python
self.data.set_text("status", "Error description")
self.data.set_text_color("status", [1.0, 0.3, 0.3, 1.0])  # Red
```

---

## Pitfall 5: No Cleanup on Close

### The Problem

Failing to clean up resources when tool closes leads to memory leaks and stale references.

❌ **Wrong**:
```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')"
}
```

No `OnClosePyCmd` defined.

### Why It's Wrong

1. **Memory leaks** - Resources remain allocated
2. **Stale references** - ChameleonData connections invalid
3. **Event handlers** - Callbacks still registered
4. **File handles** - Open files not closed
5. **Timers** - Background timers continue running

### The Solution

Define cleanup method in controller and call it from `OnClosePyCmd`.

✅ **Right**:
```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')",
    "OnClosePyCmd": "MyTool.instance.cleanup(); MyTool.instance = None"
}
```

```python
# In Python controller
def cleanup(self):
    """Cleanup resources on tool close."""
    try:
        # Release resources
        if hasattr(self, 'timer_handle'):
            # Clear timers
            pass

        if hasattr(self, 'file_handle'):
            # Close files
            self.file_handle.close()

        # Clear large data structures
        self.large_data = None

    except Exception as e:
        unreal.log_error(f"Cleanup failed: {str(e)}")
```

### How to Apply

**Common resources to clean up**:
- Timers and background tasks
- File handles and streams
- Network connections
- Large data structures
- Event subscriptions
- Actor references

**Pattern**:
```python
# Define cleanup method
def cleanup(self):
    try:
        # Release all resources
        pass
    except Exception as e:
        unreal.log_error(f"Cleanup failed: {str(e)}")

# Clear singleton reference
# OnClosePyCmd: "MyTool.instance.cleanup(); MyTool.instance = None"
```

---

## Pitfall 6: UI Overflow / No Scrolling

### The Problem

Content extends beyond window bounds and becomes inaccessible when not wrapped in scrollable container.

❌ **Wrong**:
```json
{
    "Root": {
        "SVerticalBox": {
            "Slots": [
                /* 50 widgets - content extends beyond window */
            ]
        }
    }
}
```

### Why It's Wrong

1. **Content clipped** - Widgets beyond window bounds invisible
2. **No access** - Cannot interact with hidden widgets
3. **Poor UX** - User cannot see all options
4. **Window resize doesn't help** - Content fixed to initial size

### The Solution

Wrap root widget in `SScrollBox` or constrain with `SBox`.

✅ **Right**:
```json
{
    "Root": {
        "SScrollBox": {
            "Slots": [
                {
                    "SVerticalBox": {
                        "Slots": [
                            /* widgets - now scrollable */
                        ]
                    }
                }
            ]
        }
    }
}
```

### How to Apply

**For dynamic/long content**:
```json
"Root": {
    "SScrollBox": {
        "Slots": [/* content */]
    }
}
```

**For fixed-size content**:
```json
"Root": {
    "SBox": {
        "WidthOverride": 400,
        "HeightOverride": 300,
        "Content": {/* widgets */}
    }
}
```

**Best practice**:
- Default to `SScrollBox` for tools with multiple sections
- Use `SBox` for simple, fixed-size dialogs
- Always test with different window sizes

---

## Pitfall 7: No Auto-Reload During Development

### The Problem

Without auto-reload, code changes require editor restart, making development slow.

❌ **Wrong (for development)**:
```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')"
}
```

### Why It's Wrong

1. **Slow iteration** - Must restart editor for every change
2. **Lost state** - Editor state reset on restart
3. **Time wasted** - Restarting UE5 takes minutes
4. **Testing difficult** - Cannot quickly test changes

### The Solution

Use `importlib.reload()` during development for hot reloading.

✅ **Right (for development)**:
```json
{
    "InitPyCmd": "import importlib, MyTool; importlib.reload(MyTool); MyTool.instance = MyTool.MyTool('%JsonPath')"
}
```

### How to Apply

**Development version**:
```json
"InitPyCmd": "import importlib, MyTool; importlib.reload(MyTool); MyTool.instance = MyTool.MyTool('%JsonPath')"
```

**Production version** (remove auto-reload):
```json
"InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')"
```

**When to use**:
- **Use auto-reload during**: Active development, testing, debugging
- **Remove auto-reload for**: Production, shipping tools, stable releases

**Note**: Auto-reload can cause issues with complex state management. Remove before shipping.

---

## Pitfall 8: UE5 Level API Compatibility Issues

### The Problem

During SceneSelectTool development, level lookup failed intermittently across environments:

- `'World' object has no attribute 'persistent_level'`
- `Failed to find property 'current_level' for attribute 'current_level' on 'World'`

### Why It's Wrong

Relying on a single world property is fragile because UE5 Python bindings differ by version and runtime context.

1. Some properties are unavailable in specific engine builds
2. Direct attribute access may fail even when editor property exists
3. Tool behavior becomes non-deterministic across machines

### The Solution

Implement multi-step fallback for current level resolution:

1. Try `unreal.EditorLevelLibrary.get_current_level()` first
2. Fallback to `world.get_editor_property(...)` for `current_level` and `persistent_level`
3. Final fallback to `getattr(world, ...)`
4. If all fail, degrade gracefully (scan all levels + warning)

### How to Apply

Use a dedicated resolver method (for example: `_resolve_current_level`) and never hardcode a single property path.

---

## Pitfall 9: Current-Level Filtering Is Too Fragile

### The Problem

Filtering actors by comparing `actor.get_outer()` with current level can fail for some actor types or editor contexts.

### Why It's Wrong

1. `get_outer()` is not always the authoritative level reference
2. Different actor wrappers may expose level differently
3. Filtering returns false negatives and misses valid actors

### The Solution

Use layered actor-level detection:

1. Prefer `actor.get_level()`
2. Fallback to `actor.get_editor_property("level")`
3. Last fallback to `actor.get_outer()`

Then compare the resolved actor level with resolved current level.

### How to Apply

Encapsulate this in helper methods (for example: `_get_actor_level`, `_safe_get_editor_property`) and keep `execute_select()` focused on business logic.

---

## Pitfall 10: Missing Menu Tooltip Descriptions

### The Problem

Newly added tools were visible in Chameleon Tools menu, but users could not quickly understand each tool's purpose without opening them.

### Why It's Wrong

1. Poor discoverability in multi-tool menus
2. Increases trial-and-error clicks
3. Slows team onboarding and handoff

### The Solution

Add concise Chinese `tooltip` descriptions for each menu item in `MenuConfig.json`, aligned with naming style used by Scene Selection Tool.

### How to Apply

For each `OnToolBarChameleon.items` entry:

1. Keep `name` as product/UI naming requirement (e.g., English)
2. Add/maintain `tooltip` in Chinese describing intent + scope
3. Keep tooltip short and action-oriented

---

## Summary: Quick Reference
| Pitfall | Solution |
|---------|----------|
| Inline Python in UI | Use `Aka` + controller methods |
| Missing Aka fields | Add unique identifiers to all interactive widgets |
| No singleton pattern | Store instance in `Module.instance` |
| Missing error handling | Wrap all `unreal.xxx` calls in try-except |
| No cleanup on close | Add `OnClosePyCmd` with cleanup method |
| UI overflow | Wrap root in `SScrollBox` |
| No auto-reload | Use `importlib.reload()` during development |
| UE5 level API compatibility | Multi-step level resolution + graceful fallback |
| Fragile current-level filtering | Resolve actor level via layered API fallback |
| Missing menu tooltips | Add concise Chinese `tooltip` to each tool item |

---

## Prevention Checklist

Before deploying a TAPython tool, verify:

- [ ] No inline Python in UI (OnClick, OnValueChanged, etc.)
- [ ] All interactive widgets have unique Aka fields
- [ ] Singleton pattern implemented (Module.instance)
- [ ] All unreal.xxx calls wrapped in try-except
- [ ] Cleanup method defined and called from OnClosePyCmd
- [ ] Root widget wrapped in SScrollBox or SBox
- [ ] Auto-reload removed for production builds
- [ ] User feedback provided for all operations
- [ ] Edge cases handled (empty selections, invalid input)
- [ ] Error messages logged to unreal.log_error()

---

For correct implementation patterns, see [Common Patterns](../patterns/CommonPatterns.md).
