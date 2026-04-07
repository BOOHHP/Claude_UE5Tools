## Splitter Layout[¶](#splitter-layout)

This guide explains how to use the Splitter layout in Chameleon.

## Overview[¶](#overview)

The Splitter layout allows users to resize panels by dragging a handle between them.

## SSplitter[¶](#ssplitter)

### Basic Example[¶](#basic-example)

```json
{
    "SSplitter": {
        "Orientation": "Horizontal",
        "Slots": [
            {
                "SButton": {
                    "Text": "Panel 1"
                }
            },
            {
                "SButton": {
                    "Text": "Panel 2"
                }
            }
        ]
    }
}
```

## Configuration[¶](#configuration)

### Orientation[¶](#orientation)

- `Horizontal`: Left-to-right split
- `Vertical`: Top-to-bottom split

### Slot Properties[¶](#slot-properties)

- `SizeCoefficient`: Initial size ratio
- `MinSize`: Minimum panel size

## Use Cases[¶](#use-cases)

- Resizable side panels
- Split views
- Multi-pane layouts

## Example[¶](#example)

```json
{
    "SSplitter": {
        "Orientation": "Horizontal",
        "Style": "Panel.Splitter",
        "Slots": [
            {
                "SizeCoefficient": 0.5,
                "SVerticalBox": {
                    "Slots": [
                        {"STextBlock": {"Text": "Left Panel"}}
                    ]
                }
            },
            {
                "SizeCoefficient": 0.5,
                "SVerticalBox": {
                    "Slots": [
                        {"STextBlock": {"Text": "Right Panel"}}
                    ]
                }
            }
        ]
    }
}
```

 [Previous](directional_layout.html) [Next](grid_layout.html)
