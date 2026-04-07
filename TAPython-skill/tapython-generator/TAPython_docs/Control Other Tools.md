## Control Other Tools[¶](#control-other-tools)

This guide explains how to control other Chameleon Tools from Python.

## LaunchChameleonTool[¶](#launchchameleontool)

Open another Chameleon Tool:

```python
unreal.ChameleonData.launch_chameleon_tool("ChameleonGallery/auto_gen/border_brushes_Gallery.json")
```

Note:
This is a static method of ChameleonData, not an instance method.

## RequestClose[¶](#requestclose)

Close a Chameleon Tool:

```python
unreal.ChameleonData.request_close('/Example/ChameleonExample.json')
```

## SetChameleonWindowSize[¶](#setchameleonwindowsize)

Set window size:

```python
new_size = unreal.Vector2D(800, 600)
unreal.ChameleonData.set_chameleon_window_size("ChameleonGallery/ChameleonGallery.json", new_size)
```

Get current size:

```python
current_size = unreal.ChameleonData.get_chameleon_window_size("ChameleonGallery/ChameleonGallery.json")
```

Note:
Can set window size of other tools or current tool.

## SetChameleonWindowPosition[¶](#setchameleonwindowposition)

Set window position:

```python
new_position = unreal.Vector2D(100, 100)
unreal.ChameleonData.set_chameleon_window_position(tools_path, new_position)
```

## FlashChameleonWindow[¶](#flashchameleontoolwindow)

Flash window to prompt user attention:

```python
unreal.ChameleonData.flash_chameleon_window("ChameleonGallery/ChameleonGallery.json")
```

## SnapshotChameleonWindow[¶](#snapshotchameleontoolwindow)

Capture screenshot:

```python
saved_file_path = unreal.ChameleonData.snapshot_chameleon_window(tools_path, override_size, output_file_path)
```

 [Previous](reload_tool.html) [Next](take_ui_snapshot.html)
