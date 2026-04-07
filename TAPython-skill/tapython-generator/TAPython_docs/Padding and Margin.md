## Padding and Margin[¶](#padding-and-margin)

This guide explains how to use padding and margin in Chameleon layouts.

## Overview[¶](#overview)

Padding and margin control the spacing around and between UI elements.

## Padding[¶](#padding)

Padding creates space inside a widget, between its content and its border.

### Setting Padding[¶](#setting-padding)

```json
{
    "SBorder": {
        "Padding": [10, 10, 10, 10],
        "Content": {
            "STextBlock": {
                "Text": "Padded Text"
            }
        }
    }
}
```

### Padding Format[¶](#padding-format)

- Single value: All sides same
- Two values: [Horizontal, Vertical]
- Four values: [Left, Top, Right, Bottom]

## Margin[¶](#margin)

Margin creates space outside a widget, between it and adjacent widgets.

### Setting Margin[¶](#setting-margin)

In slots:

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "SButton": {
                    "Text": "Button 1"
                },
                "Padding": [5, 5, 5, 5]
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

## Common Use Cases[¶](#common-use-cases)

### Button Spacing[¶](#button-spacing)

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "SButton": {"Text": "Button 1"},
                "Padding": [0, 0, 0, 5]
            },
            {
                "SButton": {"Text": "Button 2"}
            }
        ]
    }
}
```

### Card Padding[¶](#card-padding)

```json
{
    "SBorder": {
        "BorderImage": {"Style": "FEditorStyle", "Brush": "ToolPanel.DarkGroupBorder"},
        "Padding": 10,
        "Content": {...}
    }
}
```

## Best Practices[¶](#best-practices)

- Use consistent spacing values
- Use multiples of 4 or 8 for alignment
- Consider accessibility for touch targets

 [Previous](expandable_area.html) [Next](editor_style.html)
