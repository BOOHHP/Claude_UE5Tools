## Canvas Layout[¶](#canvas-layout)

This guide explains the Canvas layout in Chameleon.

## Overview[¶](#overview)

The Canvas layout allows free-form positioning of child widgets using absolute coordinates.

## SCanvas[¶](#scanvas)

### Basic Example[¶](#basic-example)

```json
{
    "SCanvas": {
        "Slots": [
            {
                "SButton": {
                    "Text": "Positioned Button"
                },
                "Position": [100, 50],
                "Size": [120, 40]
            }
        ]
    }
}
```

## Slot Properties[¶](#slot-properties)

### Position[¶](#position)

- `Position`: [X, Y] coordinates
- Position is relative to canvas top-left

### Size[¶](#size)

- `Size`: [Width, Height] dimensions
- Optional - widget can size itself

### Anchors[¶](#anchors)

- `Anchors`: Anchor position for responsive layouts
- `Alignment`: Alignment within anchor zone

## Use Cases[¶](#use-cases)

- Free-form tool windows
- Drag-and-drop interfaces
- Custom overlays

## Example[¶](#example)

```json
{
    "SCanvas": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Top Left"
                },
                "Position": [10, 10]
            },
            {
                "STextBlock": {
                    "Text": "Bottom Right"
                },
                "Position": [300, 200]
            },
            {
                "SButton": {
                    "Text": "Centered Button"
                },
                "Position": [150, 100],
                "Size": [100, 30]
            }
        ]
    }
}
```

 [Previous](box_layout.html) [Next](expandable_area.html)
