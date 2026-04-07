## Get Object in Unreal Engine Editor[¶](#get-object-in-unreal-engine-editor)

This guide explains how to access and manipulate objects in the Unreal Engine editor using TAPython.

## Overview[¶](#overview)

TAPython provides APIs to interact with various objects in the Unreal Editor, including assets, actors, and editor subsystems.

## Getting Selected Objects[¶](#getting-selected-objects)

### Get Selected Assets[¶](#get-selected-assets)

```python
import unreal

# Get currently selected assets
selected_assets = unreal.PythonBPLib.get_selected_assets()

for asset in selected_assets:
    print(asset.get_full_name())
```

### Get Selected Actors[¶](#get-selected-actors)

```python
import unreal

# Get currently selected actors
selected_actors = unreal.PythonBPLib.get_selected_actors()

for actor in selected_actors:
    print(actor.get_actor_label())
```

## Getting Editor Subsystems[¶](#getting-editor-subsystems)

```python
# Get editor subsystems
editor_subsystem = unreal.PythonBPLib.get_editor_subsystem(unreal.EditorActorSubsystem)

# Use the subsystem
selected_actors = editor_subsystem.get_selected_level_actors()
```

## Common Use Cases[¶](#common-use-cases)

- Processing selected assets in bulk
- Modifying actor properties
- Accessing editor views and viewports

## Best Practices[¶](#best-practices)

- Always check if objects are valid before processing
- Handle empty selections gracefully
- Use proper error handling

 [Previous](use_shortcut_keys.html) [Next](built-in_menu_items.html)
