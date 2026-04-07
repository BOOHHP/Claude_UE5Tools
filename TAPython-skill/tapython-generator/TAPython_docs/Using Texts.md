## Using Texts[¶](#using-texts)

This guide explains how to use text widgets in Chameleon UI.

## Overview[¶](#overview)

Text widgets display text content in various formats.

## STextBlock[¶](#stextblock)

### Basic Example[¶](#basic-example)

```json
{
    "STextBlock": {
        "Text": "Hello World"
    }
}
```

## Text Properties[¶](#text-properties)

### Font[¶](#font)

```json
{
    "STextBlock": {
        "Text": "Styled Text",
        "Font": {
            "FontObject": "/Engine/EngineFonts/Roboto",
            "Size": 14
        }
    }
}
```

### Color[¶](#color)

```json
{
    "STextBlock": {
        "Text": "Colored Text",
        "ColorAndOpacity": [1.0, 0.5, 0.0, 1.0]
    }
}
```

### Alignment[¶](#alignment)

```json
{
    "STextBlock": {
        "Text": "Aligned Text",
        "Justification": "Center"
    }
}
```

## Text Styling[¶](#text-styling)

### Bold, Italic, Underline[¶](#bold-italic-underline)

```json
{
    "STextBlock": {
        "Text": "Styled Text",
        "Font": {...},
        "StrikeBrush": {...}
    }
}
```

## Dynamic Text[¶](#dynamic-text)

### Updating Text from Python[¶](#updating-text-from-python)

```python
# Set text
data.set_text("TextBlockId", "New text")

# Get text
text = data.get_text("TextBlockId")
```

## Use Cases[¶](#use-cases)

- Labels
- Descriptions
- Status messages

 [Previous](use_images_and_image_brush.html) [Next](using_rich_text.html)
