## Extend an Assets Editor[¶](#extend-an-assets-editor)

This guide explains how to extend the Asset Editor in Unreal Engine using Python.

## Overview[¶](#overview)

TAPython allows you to extend the Asset Editor with custom tabs and functionality.

## Creating an Asset Editor Extension[¶](#creating-an-asset-editor-extension)

### Step 1: Register the Extension[¶](#step-1-register-the-extension)

```python
# Register your custom tab with the asset editor
unreal.PythonBPLib.register_asset_editor_tab()
```

### Step 2: Define the UI[¶](#step-2-define-the-ui)

Create a Chameleon UI for your extension:

```json
{
    "TabLabel": "My Asset Tool",
    "Root": {
        "SVerticalBox": {
            "Slots": []
        }
    }
}
```

### Step 3: Handle Asset Changes[¶](#step-3-handle-asset-changes)

Listen for asset selection changes:

```python
def on_asset_selected(self, asset):
    # Handle asset selection
    pass
```

## Use Cases[¶](#use-cases)

- Custom asset preview tools
- Asset batch processing
- Property editors
- Validation tools

## Examples[¶](#examples)

The built-in Object Detail Viewer is an example of an Asset Editor extension.

 [Previous](learning_unreal_engine_with_python.html) [Next](how_to_debug_python_in_ue.html)
