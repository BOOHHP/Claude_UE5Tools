## Take UI Snapshot[¶](#take-ui-snapshot)

This guide explains how to take UI snapshots of Chameleon Tools.

## Overview[¶](#overview)

You can capture screenshots of Chameleon windows using Python.

## SnapshotChameleonWindow[¶](#snapshotchameleontoolwindow)

```python
saved_file_path = unreal.ChameleonData.snapshot_chameleon_window(json_path, override_window_size)
```

The advantage is that it can specify window size to capture complete content even if not fully displayed.

## Calculate Actual Window Size[¶](#calculate-actual-window-size)

### Get Current Size[¶](#get-current-size)

```python
current_size = unreal.ChameleonData.get_chameleon_window_size(json_path)
```

### Get ScrollBox Offsets[¶](#get-scrollbox-offsets)

```python
scrollbox_offsets = data.get_top_scroll_box_offsets(json_path)
```

### Calculate Full Size[¶](#calculate-full-size)

```python
def snapshot(json_path):
    data = unreal.PythonBPLib.get_chameleon_data(json_path)
    current_size = unreal.ChameleonData.get_chameleon_window_size(json_path)
    scrollbox_offsets = data.get_top_scroll_box_offsets(json_path)
    if scrollbox_offsets and "ScrollOffsetOfEnd" in scrollbox_offsets:
        height_full = scrollbox_offsets["ScrollOffsetOfEnd"] / (1.0 - scrollbox_offsets["viewFraction"])
        height_full += 48
        override_size = (current_size.x, round(height_full))
    else:
        override_size = (0, 0)
    r = unreal.ChameleonData.snapshot_chameleon_window(json_path, override_window_size=override_size)
    print(f"Save UI: {r}")
```

Caution:
The code above does not take into account DPI Scale (default is 1).

Note:
The maximum interface length that can be captured in Unreal Engine is 16384.

## Add Screenshot to All Tools[¶](#add-screenshot-to-all-tools)

Via MenuConfig.ini:

```json
{
    "OnTabContextMenu": {
        "name": "TA Python Tab",
        "items": [
            {
                "name": "Save UI Snapshot",
                "command": "import Utilities; Utilities.snapshot_chameleon.snapshot(%tool_path)"
            }
        ]
    }
}
```

## Capture Object Detail Panel[¶](#capture-object-detail-panel)

```python
unreal.PythonBPLib.snapshot_details(start_from_docking, override_window_size, image_file_path)
```

 [Previous](control_other_tools.html) [Next](write_test_case.html)
