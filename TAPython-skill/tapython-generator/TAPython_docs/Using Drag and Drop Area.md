## Using Drag and Drop Area[¶](#using-drag-and-drop-area)

This guide explains how to use the Drag and Drop Area widget in Chameleon.

## Overview[¶](#overview)

The Drag and Drop Area allows users to drag and drop files or data into your UI.

## SDragDropArea[¶](#sdragdroparea)

### Basic Example[¶](#basic-example)

```json
{
    "SDragDropArea": {
        "OnDragDetected": "tool.on_drag_detected()",
        "Content": {
            "STextBlock": {
                "Text": "Drop files here"
            }
        }
    }
}
```

## Handling Drag and Drop[¶](#handling-drag-and-drop)

### OnDragDetected[¶](#ondragdetected)

Called when files are dragged into the area:

```python
def on_drag_detected(self, files):
    for file in files:
        print(f"Dropped: {file}")
```

### Python Callback[¶](#python-callback)

```json
{
    "OnDragDetected": "tool.handle_drop(%drag_drop_payload)"
}
```

## Configuration[¶](#configuration)

### Allowed Types[¶](#allowed-types)

- `AllowDrop`: Enable drop functionality
- `DragGesture`: Mouse gesture for drag start

### Visual Feedback[¶](#visual-feedback)

- Hover effects
- Drop highlight

## Use Cases[¶](#use-cases)

- Asset importers
- File processors
- Data visualization tools

 [Previous](using_rich_text.html) [Next](using_list_view.html)
