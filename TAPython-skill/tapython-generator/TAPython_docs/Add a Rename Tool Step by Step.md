## Add a Rename Tool Step by Step[¶](#add-a-rename-tool-step-by-step)

This tutorial walks you through creating a simple rename tool using TAPython.

## Overview[¶](#overview)

In this tutorial, you'll create a tool that renames selected assets with a custom pattern.

## Step 1: Create the Tool Class[¶](#step-1-create-the-tool-class)

First, create a Python class for your tool:

```python
class RenameTool:
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
        self.data = unreal.PythonBPLib.get_chameleon_data(jsonPath)
```

## Step 2: Define the UI[¶](#step-2-define-the-ui)

Create a JSON file for your UI:

```json
{
    "TabLabel": "Rename Tool",
    "InitPyCmd": "import RenameTool; tool = RenameTool.RenameTool(%JsonPath)",
    "Root": {
        "SVerticalBox": {
            "Slots": [
                {
                    "STextBlock": {
                        "Text": "Rename Pattern"
                    }
                }
            ]
        }
    }
}
```

## Step 3: Add Rename Logic[¶](#step-3-add-rename-logic)

Add the rename functionality:

```python
def rename_assets(self, pattern):
    selected = unreal.PythonBPLib.get_selected_assets()
    for asset in selected:
        # Rename logic here
        pass
```

## Step 4: Connect UI to Python[¶](#step-4-connect-ui-to-python)

Link UI events to Python callbacks:

```json
{
    "OnClick": "tool.rename_assets(%pattern)"
}
```

## Next Steps[¶](#next-steps)

- [Extend an Assets Editor](https://www.tacolor.xyz/tapython/extend_an_assets_editor.html)
- [Chameleon Tool](https://www.tacolor.xyz/tapython/chameleon_tool.html)

 [Previous](chameleon_gallery.html) [Next](learning_unreal_engine_with_python.html)
