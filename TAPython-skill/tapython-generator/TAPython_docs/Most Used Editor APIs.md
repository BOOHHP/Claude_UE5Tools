## Most Used Editor APIs[¶](#most-used-editor-apis)

This page documents the most commonly used Unreal Editor Python APIs.

## Asset Management[¶](#asset-management)

### Getting Selected Assets[¶](#getting-selected-assets)

```python
import unreal

# Get selected assets
assets = unreal.PythonBPLib.get_selected_assets()
```

### Loading Assets[¶](#loading-assets)

```python
# Load an asset
asset = unreal.load_asset("/Game/MyFolder/MyAsset")
```

## Actor Management[¶](#actor-management)

### Getting Selected Actors[¶](#getting-selected-actors)

```python
# Get selected actors
actors = unreal.PythonBPLib.get_selected_actors()
```

### Creating Actors[¶](#creating-actors)

```python
# Spawn an actor
actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location)
```

## Editor Subsystems[¶](#editor-subsystems)

### Common Subsystems[¶](#common-subsystems)

```python
# Get editor subsystems
actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
asset_editor_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
```

## Viewport Operations[¶](#viewport-operations)

### Moving Camera[¶](#moving-camera)

```python
# Move camera to location
unreal.PythonBPLib.set_viewport_camera_to_location(location, rotation)
```

## Utility Functions[¶](#utility-functions)

### Getting Asset Paths[¶](#getting-asset-paths)

```python
# Get asset path
path = asset.get_path_name()
```

 [Previous](how_to_debug_python_in_ue.html) [Next](need_more_python_apis.html)
