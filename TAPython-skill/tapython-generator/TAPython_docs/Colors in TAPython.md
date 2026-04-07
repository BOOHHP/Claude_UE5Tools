## Colors in TAPython[¶](#colors-in-tapython)

This guide explains how to use colors in TAPython Chameleon UI.

## Overview[¶](#overview)

You can specify colors in Chameleon using various color formats.

## Color Formats[¶](#color-formats)

### Linear Color[¶](#linear-color)

```json
{
    "BorderBackgroundColor": {
        "R": 1.0,
        "G": 0.5,
        "B": 0.0,
        "A": 1.0
    }
}
```

### RGBA Array[¶](#rgba-array)

```json
{
    "BorderBackgroundColor": [1.0, 0.5, 0.0, 1.0]
}
```

### Hex Color[¶](#hex-color)

```json
{
    "BorderBackgroundColor": "#FF8000FF"
}
```

## Predefined Colors[¶](#predefined-colors)

Common colors are predefined:
- `FLinearColor.White`
- `FLinearColor.Black`
- `FLinearColor.Red`
- `FLinearColor.Green`
- `FLinearColor.Blue`

## Using Colors[¶](#using-colors)

### Text Color[¶](#text-color)

```json
{
    "STextBlock": {
        "ColorAndOpacity": {
            "R": 1.0,
            "G": 1.0,
            "B": 1.0,
            "A": 1.0
        },
        "Text": "Hello"
    }
}
```

### Background Color[¶](#background-color)

```json
{
    "SBorder": {
        "BorderBackgroundColor": [0.1, 0.1, 0.1, 1.0],
        "Content": {...}
    }
}
```

## Best Practices[¶](#best-practices)

- Use consistent color schemes
- Test with both light and dark themes
- Use alpha for transparency

 [Previous](editor_style.html) [Next](using_buttons.html)
