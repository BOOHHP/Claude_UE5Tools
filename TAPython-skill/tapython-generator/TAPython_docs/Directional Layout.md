## Directional Layout[¶](#directional-layout)

This guide explains directional layouts in Chameleon.

## Overview[¶](#overview)

Directional layouts arrange widgets in a single direction - horizontal or vertical.

## SHorizontalBox[¶](#shorizontalbox)

Arranges widgets horizontally (left to right).

### Example[¶](#example)

```json
{
    "SHorizontalBox": {
        "Slots": [
            {
                "SButton": {
                    "Text": "Button 1"
                }
            },
            {
                "SButton": {
                    "Text": "Button 2"
                }
            }
        ]
    }
}
```

## SVerticalBox[¶](#sverticalbox)

Arranges widgets vertically (top to bottom).

### Example[¶](#example)

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Line 1"
                }
            },
            {
                "STextBlock": {
                    "Text": "Line 2"
                }
            }
        ]
    }
}
```

## Slot Properties[¶](#slot-properties)

### Size Rules[¶](#size-rules)

- `SizeCoefficient`: Relative size
- `AutoHeight`: Automatic height
- `MaxHeight`: Maximum height

### Alignment[¶](#alignment)

- `HAlign`: Horizontal alignment
- `VAlign`: Vertical alignment

## Use Cases[¶](#use-cases)

- Toolbars (HorizontalBox)
- Lists (VerticalBox)
- Forms

 [Previous](cpp_to_json.html) [Next](splitter_layout.html)
