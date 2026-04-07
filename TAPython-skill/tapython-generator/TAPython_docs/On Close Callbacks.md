## OnClose Callbacks[¶](#onclose-callbacks)

This guide explains how to handle callbacks when events occur in Chameleon Tools.

## OnMapChangedCmd[¶](#onmapchangedcmd)

Execute Python commands when changing maps:

```json
{
    "OnMapChangedCmd": "chameleon_objectDetailViewer.on_map_changed(%map_change_type)"
}
```

### Parameters[¶](#parameters)

- `%world`: Get the world of map operation
- `%map_change_type`: Operation type - "LoadMap", "SaveMap", "NewMap", or "TearDownWorld"

### Use Cases[¶](#use-cases)

- Clean references when unloading map
- Avoid memory leaks
- Sync UI when changing map

### Example[¶](#example)

```python
def on_map_changed(self, map_change_type_str):
    if map_change_type_str == "TearDownWorld":
        self.reset(bResetParameter=False)
    else:
        pass  # skip: LoadMap, SaveMap, NewMap
```

## OnClosePyCmd[¶](#onclosepycmd)

Execute Python command when user closes Chameleon Tool:

```json
{
    "TabLabel": "KeypadCommunicator",
    "InitTabSize": [200, 80],
    "InitPyCmd": "import MidiCommander; import importlib; importlib.reload(MidiCommander); chameleon_midi = MidiCommander.MidiListener.MidiListener(%JsonPath); chameleon_midi.open()",
    "OnClosePyCmd": "chameleon_midi.on_ui_close()",
    "Root": {...}
}
```

 [Previous](write_test_case.html) [Next Topic](manipulate_material_expression_nodes_of_material_with_python_in_ue.html)
