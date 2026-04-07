## Box Layout[¶](#box-layout)

This guide explains the Box layout in Chameleon.

## Overview[¶](#overview)

The Box layout is a simple layout that packs children into a single row or column.

## SBox[¶](#sbox)

### Basic Example[¶](#basic-example)

```json
{
    "SBox": {
        "WidthOverride": 200,
        "HeightOverride": 100,
        "Content": {
            "SButton": {
                "Text": "Click Me"
            }
        }
    }
}
```

## Box Types[¶](#box-types)

### Size Constraints[¶](#size-constraints)

- `WidthOverride`: Fixed width
- `HeightOverride`: Fixed height
- `MinWidth`: Minimum width
- `MinHeight`: Minimum height
- `MaxWidth`: Maximum width
- `MaxHeight`: Maximum height

### Content Alignment[¶](#content-alignment)

- `HAlign`: Horizontal alignment (Left, Center, Right, Fill)
- `VAlign`: Vertical alignment (Top, Center, Bottom, Fill)

## Use Cases[¶](#use-cases)

- Fixed-size panels
- Bounded containers
- Sized widgets

## Example[¶](#example)

```json
{
    "SBox": {
        "WidthOverride": 300,
        "HeightOverride": 200,
        "HAlign": "Center",
        "VAlign": "Center",
        "Content": {
            "SBorder": {
                "BorderImage": {
                    "Style": "FEditorStyle",
                    "Brush": "ToolPanel.DarkGroupBorder"
                },
                "Content": {
                    "STextBlock": {
                        "Text": "Centered Content"
                    }
                }
            }
        }
    }
}
```

 [Previous](grid_layout.html) [Next](canvas_layout.html)
