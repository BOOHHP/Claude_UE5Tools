# Controller.py Template

## Basic Structure

```python
import unreal
import importlib

class [ToolName]Controller:
    """
    Controller for [ToolName] Chameleon tool.
    Handles UI interaction and Unreal Engine operations.
    """

    def __init__(self, json_path: str):
        """
        Initialize controller with ChameleonData bridge.

        Args:
            json_path: Path to the tool's JSON file (passed via %JsonPath)
        """
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

        # Initialize UI state
        self._setup_ui()

    def _setup_ui(self):
        """Set initial UI state."""
        try:
            self.data.set_text("status_label", "Ready")
        except Exception as e:
            unreal.log_error(f"UI setup failed: {str(e)}")

    def execute_action(self):
        """
        Main action handler. Replace this with your tool's functionality.
        """
        try:
            # Get input from UI
            input_value = self.data.get_text("input_field")

            if not input_value:
                self.data.set_text("status_label", "Error: Input required")
                return

            # Perform Unreal Engine operations
            selected_assets = unreal.PythonBPLib.get_selected_assets()

            if not selected_assets:
                self.data.set_text("status_label", "Error: No assets selected")
                return

            # Your business logic here
            processed_count = 0
            for asset in selected_assets:
                # Process each asset
                processed_count += 1

            # Update UI with result
            self.data.set_text("status_label", f"Processed {processed_count} assets")

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            unreal.log_error(error_msg)
            self.data.set_text("status_label", error_msg)

    def cleanup(self):
        """
        Cleanup method called when tool window closes.
        Override this to release resources.
        """
        try:
            # Release any held resources
            pass
        except Exception as e:
            unreal.log_error(f"Cleanup failed: {str(e)}")

# Module-level instance for singleton pattern
instance = None
```

## Required Elements

1. **Class initialization** with `json_path` parameter
2. **ChameleonData initialization**: `self.data = unreal.PythonBPLib.get_chameleon_data(json_path)`
3. **Try-except blocks** around ALL `unreal.xxx` calls
4. **User feedback** via `self.data.set_text()` calls
5. **Singleton instance** at module level: `instance = None`

## Error Handling Pattern

**CRITICAL**: All Unreal Engine API calls must be wrapped in try-except blocks.

### Example: Safe Asset Operation
```python
def process_assets(self):
    try:
        # Get selected assets
        assets = unreal.PythonBPLib.get_selected_assets()

        if not assets:
            self.data.set_text("status", "No assets selected")
            return

        # Process each asset with individual error handling
        processed = 0
        failed = 0

        for asset in assets:
            try:
                # Attempt operation on each asset
                asset_name = asset.get_name()
                # Your processing logic here
                processed += 1

            except Exception as e:
                failed += 1
                unreal.log_error(f"Failed to process {asset.get_name()}: {str(e)}")
                continue

        # Report results
        self.data.set_text("status", f"Processed: {processed}, Failed: {failed}")

    except Exception as e:
        unreal.log_error(f"Process failed: {str(e)}")
        self.data.set_text("status", f"Error: {str(e)}")
```

## Common UI Data Access Patterns

### Get Text Input
```python
text = self.data.get_text("input_field")
```

### Set Text Output
```python
self.data.set_text("status_label", "Processing complete")
```

### Set Text Color
```python
# RGBA format (0.0-1.0)
self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])  # Red
self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])  # Green
```

### Get Checkbox State
```python
is_checked = self.data.get_checkbox_state("option_enabled")
```

### Get ComboBox Selection
```python
selected_option = self.data.get_combo_box_selection("mode_selector")
```

### Get Button Click (Polling)
```python
if self.data.get_button_click("btn_execute"):
    self.execute_action()
```

### Set List Items
```python
items = ["Item 1", "Item 2", "Item 3"]
self.data.set_list_items("results_list", items)
```

## Common Unreal Engine API Patterns

### Get Selected Assets
```python
assets = unreal.PythonBPLib.get_selected_assets()
```

### Get Selected Actors
```python
actors = unreal.EditorLevelLibrary.get_selected_level_actors()
```

### Load Asset
```python
asset = unreal.EditorAssetLibrary.load_asset("/Game/Path/To/Asset")
```

### Rename Asset
```python
success = unreal.EditorAssetLibrary.rename_asset(old_path, new_name)
```

### Spawn Actor
```python
actor_class = unreal.EditorAssetLibrary.load_blueprint_class("/Game/Blueprints/MyActor")
location = unreal.Vector(0.0, 0.0, 0.0)
rotation = unreal.Rotator(0.0, 0.0, 0.0)
actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, rotation)
```

### List Assets in Path
```python
asset_paths = unreal.EditorAssetLibrary.list_assets("/Game/MyFolder")
```

### Log Messages
```python
unreal.log("Info message")
unreal.log_warning("Warning message")
unreal.log_error("Error message")
```

## Singleton Pattern

The tool must be initialized as a singleton to prevent multiple instances:

```python
# In InitPyCmd (UI.json)
"InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyToolController('%JsonPath')"

# In Python file (MyTool.py)
instance = None  # Module-level singleton storage
```

## Cleanup Pattern

Always clean up resources when tool closes:

```python
# In Controller
def cleanup(self):
    try:
        # Release resources
        # Clear references
        pass
    except Exception as e:
        unreal.log_error(f"Cleanup failed: {str(e)}")

# In UI.json
"OnClosePyCmd": "MyTool.instance.cleanup(); MyTool.instance = None"
```

## Validation Checklist

- [ ] Class name matches file name (without .py extension)
- [ ] `__init__` accepts `json_path` parameter
- [ ] Initializes `self.data = unreal.PythonBPLib.get_chameleon_data(json_path)`
- [ ] Module-level `instance = None` for singleton pattern
- [ ] ALL `unreal.xxx` API calls wrapped in try-except blocks
- [ ] Errors logged with `unreal.log_error()`
- [ ] User feedback provided via `self.data.set_text()` for status updates
- [ ] Handles edge cases (empty selections, missing assets, invalid input)
- [ ] No UI rendering code (no creating Slate widgets in Python)
