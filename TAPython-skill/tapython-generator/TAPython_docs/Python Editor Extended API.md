## Python Editor Extended API[¶](#python-editor-extended-api)

This page documents the Python Editor Extended API provided by TAPython.

## Overview[¶](#overview)

TAPython extends 200+ Editor Python interfaces that are useful for creating Editor Tools.

If you want get/set content of widgets, use ChameleonData instead.

## API Libraries[¶](#api-libraries)

| Library | Description | Count |
|---------|-------------|-------|
| PythonBPLib | Editor interface collection | 103 |
| PythonControlRigLib | Editor interface for ControlRig | 1 |
| PythonDataTableLib | Editor interface for DataTable | 19 |
| PythonEnumLib | Editor interface for User Defined Enum | 12 |
| PythonLandscapeLib | Editor interface for Landscape | 12 |
| PythonLevelLib | Editor interface for Level Editor | 2 |
| PythonMaterialLib | Editor interface for Materials | 34 |
| PythonMeshLib | Editor interface for Meshes | 15 |
| PythonPhysicsAssetLib | Editor interface for Physics Assets | 38 |
| PythonStructLib | Editor interface for User Defined Struct | 14 |
| PythonTestLib | Editor interface for Testing | 5 |
| PythonTextureLib | Editor interface for Texture2D | 3 |

## Common API Examples[¶](#common-api-examples)

### PythonBPLib[¶](#pythonbplib)

PythonBPLib is the largest library with 103 interfaces covering general editor operations.

**Get selected assets in Content Browser:**

```python
import unreal

selected_assets = unreal.PythonBPLib.get_selected_assets()
for asset in selected_assets:
    unreal.log(f"Selected: {asset.get_full_name()}")
```

**Get selected actors in the viewport:**

```python
selected_actors = unreal.PythonBPLib.get_selected_actors()
for actor in selected_actors:
    unreal.log(f"Actor: {actor.get_name()} at {actor.get_actor_location()}")
```

**Show a popup dialog:**

```python
unreal.PythonBPLib.popup_message("Operation Complete", "Batch rename finished successfully.")
```

**Get and set clipboard text:**

```python
clipboard_text = unreal.PythonBPLib.get_clipboard_text()
unreal.PythonBPLib.set_clipboard_text("New clipboard content")
```

### PythonMaterialLib[¶](#pythonmateriallib)

PythonMaterialLib provides 34 interfaces for material editing automation.

**Get material expressions:**

```python
material = unreal.load_asset("/Game/Materials/M_Example")
expressions = unreal.PythonMaterialLib.get_material_expressions(material)
for expr in expressions:
    unreal.log(f"Expression: {expr.get_name()}")
```

**Set a material scalar parameter:**

```python
material_instance = unreal.load_asset("/Game/Materials/MI_Example")
unreal.PythonMaterialLib.set_material_instance_scalar_parameter(material_instance, "Roughness", 0.5)
```

### PythonMeshLib[¶](#pythonmeshlib)

PythonMeshLib offers 15 interfaces for mesh data access and modification.

**Get mesh vertex count:**

```python
mesh = unreal.load_asset("/Game/Meshes/SM_Example")
vertex_count = unreal.PythonMeshLib.get_mesh_vertex_count(mesh, lod_index=0)
unreal.log(f"Vertex count: {vertex_count}")
```

**Modify mesh LOD settings:**

```python
mesh = unreal.load_asset("/Game/Meshes/SM_Example")
unreal.PythonMeshLib.set_lod_num(mesh, 3)
```

## Common Use Cases[¶](#common-use-cases)

- **Asset management and batch operations** — Use PythonBPLib to iterate over selected or filtered assets and perform bulk renaming, moving, or property changes.
- **Material editing automation** — Use PythonMaterialLib to programmatically create, modify, or audit material instances and their parameters.
- **Mesh/geometry processing** — Use PythonMeshLib to inspect vertex data, adjust LODs, or batch-process static meshes.
- **DataTable manipulation** — Use PythonDataTableLib to read, write, and validate DataTable rows from Python scripts.
- **Custom enum management** — Use PythonEnumLib to create or modify user-defined enums used across Blueprints and data assets.
- **Level editor automation** — Use PythonLevelLib to automate actor placement, level streaming, or scene organization tasks.

## Error Handling[¶](#error-handling)

When calling Extended API functions, follow these practices:

**Wrap API calls in try/except:**

```python
try:
    result = unreal.PythonBPLib.get_selected_assets()
except Exception as e:
    unreal.log_error(f"Failed to get selected assets: {e}")
```

**Check return values before use:**

```python
actors = unreal.PythonBPLib.get_selected_actors()
if actors is None or len(actors) == 0:
    unreal.log_warning("No actors selected.")
    return
```

**Use `unreal.log_error()` for debugging:**

```python
unreal.log("Info message")
unreal.log_warning("Warning message")
unreal.log_error("Error message — check the Output Log in the editor")
```

## API vs ChameleonData[¶](#api-vs-chameleondata)

TAPython provides two complementary API surfaces:

| Aspect | Extended API (this page) | ChameleonData |
|--------|--------------------------|---------------|
| Purpose | Editor operations (assets, materials, meshes, etc.) | UI widget get/set (text fields, checkboxes, sliders, etc.) |
| Libraries | PythonBPLib, PythonMaterialLib, PythonMeshLib, etc. | ChameleonData |
| Typical use | Batch processing, automation, data queries | Reading and writing values in Chameleon tool UIs |
| Documentation | This page | [TA Python ChameleonData API](TA Python ChameleonData API.md) |

If you need to **read or write widget values** in a Chameleon UI (e.g., getting text from an input field), use [ChameleonData](TA Python ChameleonData API.md). If you need to **perform editor operations** (e.g., querying assets, editing materials), use the Extended APIs documented here.

## See Also[¶](#see-also)

- [Chameleon Gallery](https://www.tacolor.xyz/tapython/chameleon_gallery.html)
- [ChameleonDataAPI](https://www.tacolor.xyz/pages/ChameleonDataAPI.html)
- [Most Used Editor APIs](Most Used Editor APIs.md)
- [TA Python ChameleonData API](TA Python ChameleonData API.md)
- [Get Value from Slate](Get Value from Slate.md)
