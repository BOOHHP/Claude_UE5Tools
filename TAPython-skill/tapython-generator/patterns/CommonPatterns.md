# Common TAPython Patterns

This document catalogs common implementation patterns for TAPython tools, providing ready-to-use templates for typical use cases.

## Pattern Categories

1. [Asset Processing Tool](#pattern-1-asset-processing-tool) - Batch operations on selected assets
2. [Actor Spawner Tool](#pattern-2-actor-spawner-tool) - Spawn actors with custom parameters
3. [Asset Browser/Filter Tool](#pattern-3-asset-browserfilter-tool) - Search and filter assets
4. [Settings/Configuration Tool](#pattern-4-settingsconfiguration-tool) - Manage tool/project settings

---

## Pattern 1: Asset Processing Tool

**Use Case**: Perform batch operations on selected assets (rename, move, modify properties).

**Common Operations**:
- Batch rename
- Batch move to folder
- Batch property modification
- Asset validation/fixing

### UI Components

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Batch Asset Processor",
                    "Font": ["Segoe UI", "14", "Bold"]
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": { "Text": "Prefix:" }
            },
            {
                "SEditableText": {
                    "Aka": "prefix_input",
                    "HintText": "Enter prefix to add..."
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SCheckBox": {
                    "Aka": "remove_prefix_check",
                    "Content": {
                        "STextBlock": { "Text": "Remove existing prefix" }
                    }
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SButton": {
                    "Aka": "btn_process",
                    "Text": "Process Selected Assets",
                    "HAlign": "Center"
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": {
                    "Aka": "status_label",
                    "Text": "Ready - Select assets in Content Browser",
                    "ColorAndOpacity": [0.7, 0.7, 0.7, 1.0]
                }
            }
        ]
    }
}
```

### Python Logic

```python
def process_assets(self):
    """Process all selected assets with the provided parameters."""
    try:
        # Get UI parameters
        prefix = self.data.get_text("prefix_input").strip()
        remove_existing = self.data.get_checkbox_state("remove_prefix_check")

        if not prefix:
            self.data.set_text("status_label", "Error: Prefix required")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        # Get selected assets
        assets = unreal.PythonBPLib.get_selected_assets()

        if not assets:
            self.data.set_text("status_label", "Error: No assets selected")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        # Process assets
        processed_count = 0
        failed_count = 0

        for asset in assets:
            try:
                asset_name = asset.get_name()

                # Remove existing prefix if requested
                if remove_existing:
                    # Remove common prefixes
                    for common_prefix in ["SM_", "M_", "T_", "Mtrl_"]:
                        if asset_name.startswith(common_prefix):
                            asset_name = asset_name[len(common_prefix):]
                            break

                # Apply new prefix
                new_name = f"{prefix}{asset_name}"

                # Rename asset
                asset_path = asset.get_path_name()
                success = unreal.EditorAssetLibrary.rename_asset(asset_path, new_name)

                if success:
                    processed_count += 1
                else:
                    failed_count += 1

            except Exception as e:
                failed_count += 1
                unreal.log_error(f"Failed to process {asset.get_name()}: {str(e)}")
                continue

        # Report results
        if failed_count == 0:
            status_msg = f"✓ Successfully processed {processed_count} assets"
            self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])
        else:
            status_msg = f"⚠ Processed: {processed_count}, Failed: {failed_count}"
            self.data.set_text_color("status_label", [1.0, 0.7, 0.3, 1.0])

        self.data.set_text("status_label", status_msg)

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        unreal.log_error(error_msg)
        self.data.set_text("status_label", error_msg)
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

---

## Pattern 2: Actor Spawner Tool

**Use Case**: Spawn actors in the level with custom parameters (position, rotation, scale).

**Common Operations**:
- Spawn from blueprint
- Random positioning
- Grid arrangement
- Random rotation/scale

### UI Components

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Actor Spawner",
                    "Font": ["Segoe UI", "14", "Bold"]
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": { "Text": "Blueprint Class:" }
            },
            {
                "SComboBox": {
                    "Aka": "blueprint_selector",
                    "Options": [
                        "BP_StaticMesh",
                        "BP_PointLight",
                        "BP_ParticleSystem"
                    ],
                    "SelectedItem": "BP_StaticMesh"
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "STextBlock": { "Text": "Spawn Count:" }
            },
            {
                "SSpinBox": {
                    "Aka": "spawn_count",
                    "Value": 10,
                    "MinValue": 1,
                    "MaxValue": 100
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SCheckBox": {
                    "Aka": "random_rotation_check",
                    "Content": {
                        "STextBlock": { "Text": "Random Rotation" }
                    }
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SButton": {
                    "Aka": "btn_spawn",
                    "Text": "Spawn Actors",
                    "HAlign": "Center"
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": {
                    "Aka": "status_label",
                    "Text": "Ready",
                    "ColorAndOpacity": [0.7, 0.7, 0.7, 1.0]
                }
            }
        ]
    }
}
```

### Python Logic

```python
import random
import math

def spawn_actors(self):
    """Spawn actors based on UI parameters."""
    try:
        # Get UI parameters
        blueprint_name = self.data.get_combo_box_selection("blueprint_selector")
        spawn_count = int(self.data.get_spin_box_value("spawn_count"))
        random_rotation = self.data.get_checkbox_state("random_rotation_check")

        # Load blueprint class
        blueprint_path = f"/Game/Blueprints/{blueprint_name}"
        actor_class = unreal.EditorAssetLibrary.load_blueprint_class(blueprint_path)

        if not actor_class:
            self.data.set_text("status_label", f"Error: Blueprint not found: {blueprint_name}")
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
            return

        # Spawn actors in a grid pattern
        spawned = []
        grid_size = int(math.ceil(math.sqrt(spawn_count)))
        spacing = 200.0  # 200 units between actors

        for i in range(spawn_count):
            try:
                # Calculate grid position
                row = i // grid_size
                col = i % grid_size

                location = unreal.Vector(
                    col * spacing,
                    row * spacing,
                    0.0
                )

                # Random rotation if enabled
                if random_rotation:
                    rotation = unreal.Rotator(
                        0.0,
                        random.uniform(0.0, 360.0),
                        0.0
                    )
                else:
                    rotation = unreal.Rotator(0.0, 0.0, 0.0)

                # Spawn actor
                actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
                    actor_class, location, rotation
                )

                if actor:
                    spawned.append(actor)

            except Exception as e:
                unreal.log_error(f"Failed to spawn actor {i}: {str(e)}")
                continue

        # Report results
        status_msg = f"✓ Spawned {len(spawned)} actors"
        self.data.set_text("status_label", status_msg)
        self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        unreal.log_error(error_msg)
        self.data.set_text("status_label", error_msg)
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

---

## Pattern 3: Asset Browser/Filter Tool

**Use Case**: Search and filter assets by criteria (name, type, path).

**Common Operations**:
- Search by name pattern
- Filter by asset type
- Filter by path
- Display results in list

### UI Components

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Asset Browser",
                    "Font": ["Segoe UI", "14", "Bold"]
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "SHorizontalBox": {
                    "Slots": [
                        {
                            "SEditableText": {
                                "Aka": "search_input",
                                "HintText": "Search assets...",
                                "MinDesiredWidth": 200
                            }
                        },
                        {
                            "SBox": { "WidthOverride": 8 }
                        },
                        {
                            "SComboBox": {
                                "Aka": "type_filter",
                                "Options": ["All", "StaticMesh", "Texture", "Material"],
                                "SelectedItem": "All"
                            }
                        }
                    ]
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SButton": {
                    "Aka": "btn_search",
                    "Text": "Search",
                    "HAlign": "Center"
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": { "Text": "Results:" }
            },
            {
                "SListView": {
                    "Aka": "results_list",
                    "ItemHeight": 20
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "STextBlock": {
                    "Aka": "status_label",
                    "Text": "Ready",
                    "ColorAndOpacity": [0.7, 0.7, 0.7, 1.0]
                }
            }
        ]
    }
}
```

### Python Logic

```python
def search_assets(self):
    """Search and filter assets based on criteria."""
    try:
        # Get search parameters
        search_query = self.data.get_text("search_input").strip().lower()
        type_filter = self.data.get_combo_box_selection("type_filter")

        # Get all assets
        all_assets = unreal.EditorAssetLibrary.list_assets("/Game/", recursive=True)

        # Filter assets
        results = []

        for asset_path in all_assets:
            try:
                # Filter by search query
                if search_query and search_query not in asset_path.lower():
                    continue

                # Filter by type
                if type_filter != "All":
                    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
                    if not asset:
                        continue

                    asset_class = asset.get_class().get_name()

                    # Map filter to class names
                    type_map = {
                        "StaticMesh": "StaticMesh",
                        "Texture": "Texture2D",
                        "Material": "Material"
                    }

                    expected_class = type_map.get(type_filter)
                    if expected_class and expected_class not in asset_class:
                        continue

                results.append(asset_path)

            except Exception as e:
                unreal.log_warning(f"Failed to process {asset_path}: {str(e)}")
                continue

        # Update results list
        self.data.set_list_items("results_list", results)

        # Update status
        status_msg = f"Found {len(results)} assets"
        self.data.set_text("status_label", status_msg)
        self.data.set_text_color("status_label", [0.7, 0.7, 0.7, 1.0])

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        unreal.log_error(error_msg)
        self.data.set_text("status_label", error_msg)
        self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

---

## Pattern 4: Settings/Configuration Tool

**Use Case**: Manage tool or project settings with save/load functionality.

**Common Operations**:
- Edit settings
- Save to config file
- Load from config file
- Apply settings

### UI Components

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Tool Settings",
                    "Font": ["Segoe UI", "14", "Bold"]
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": { "Text": "Output Path:" }
            },
            {
                "SEditableText": {
                    "Aka": "setting_output_path",
                    "HintText": "/Game/Output/"
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "STextBlock": { "Text": "Default Prefix:" }
            },
            {
                "SEditableText": {
                    "Aka": "setting_prefix",
                    "HintText": "SM_"
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            },
            {
                "SCheckBox": {
                    "Aka": "setting_auto_save",
                    "Content": {
                        "STextBlock": { "Text": "Auto-save on change" }
                    }
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "SHorizontalBox": {
                    "Slots": [
                        {
                            "SButton": {
                                "Aka": "btn_save",
                                "Text": "Save",
                                "HAlign": "Center"
                            }
                        },
                        {
                            "SBox": { "WidthOverride": 8 }
                        },
                        {
                            "SButton": {
                                "Aka": "btn_load",
                                "Text": "Load",
                                "HAlign": "Center"
                            }
                        }
                    ]
                }
            },
            {
                "SBox": { "HeightOverride": 16 }
            },
            {
                "STextBlock": {
                    "Aka": "status_label",
                    "Text": "Ready",
                    "ColorAndOpacity": [0.7, 0.7, 0.7, 1.0]
                }
            }
        ]
    }
}
```

### Python Logic

```python
import json
import os

class SettingsToolController:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

        # Determine config path (same directory as tool)
        self.config_path = os.path.join(
            os.path.dirname(json_path),
            "config.json"
        )

        # Load saved settings on init
        self.load_settings()

    def save_settings(self):
        """Save current settings to config file."""
        try:
            config = {
                "output_path": self.data.get_text("setting_output_path"),
                "prefix": self.data.get_text("setting_prefix"),
                "auto_save": self.data.get_checkbox_state("setting_auto_save")
            }

            # Write to config file
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4)

            self.data.set_text("status_label", "Settings saved")
            self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])

        except Exception as e:
            error_msg = f"Failed to save settings: {str(e)}"
            unreal.log_error(error_msg)
            self.data.set_text("status_label", error_msg)
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])

    def load_settings(self):
        """Load settings from config file."""
        try:
            if not os.path.exists(self.config_path):
                # No config file exists, use defaults
                self.data.set_text("setting_output_path", "/Game/Output/")
                self.data.set_text("setting_prefix", "SM_")
                self.data.set_checkbox_state("setting_auto_save", False)
                return

            # Read config file
            with open(self.config_path, 'r') as f:
                config = json.load(f)

            # Apply to UI
            self.data.set_text("setting_output_path", config.get("output_path", "/Game/Output/"))
            self.data.set_text("setting_prefix", config.get("prefix", "SM_"))
            self.data.set_checkbox_state("setting_auto_save", config.get("auto_save", False))

            self.data.set_text("status_label", "Settings loaded")
            self.data.set_text_color("status_label", [0.7, 0.7, 0.7, 1.0])

        except Exception as e:
            error_msg = f"Failed to load settings: {str(e)}"
            unreal.log_error(error_msg)
            self.data.set_text("status_label", error_msg)
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
```

---

## Additional Patterns

### Pattern 5: Validation Tool

**Use Case**: Validate assets against naming conventions, standards, or requirements.

**Structure**:
- Select assets
- Define validation rules
- Run validation
- Display results

### Pattern 6: Batch Export Tool

**Use Case**: Export assets to external formats (FBX, OBJ, etc.).

**Structure**:
- Select assets
- Choose export format
- Configure export settings
- Export to directory

### Pattern 7: One-Click Action Tool

**Use Case**: Single-action tool with no UI parameters (just execute button).

**Structure**:
- Simple status display
- Execute button
- Progress/results feedback

---

## Best Practices

1. **Always validate input** - Check for empty/invalid values before processing
2. **Provide progress feedback** - Update status label during long operations
3. **Handle errors gracefully** - Use try-except and provide user feedback
4. **Log errors for debugging** - Use `unreal.log_error()` for debugging
5. **Use color coding** - Green for success, yellow for warnings, red for errors
6. **Process in batches** - For large operations, consider batching with progress updates

---

For more implementation examples, see [Complete Tool Example](../examples/CompleteToolExample.md).
