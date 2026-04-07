## Use Images and Image Brush[¶](#use-images-and-image-brush)

This guide explains how to use images in Chameleon UI.

## Overview[¶](#overview)

Images can be displayed using SImage widget with an Image Brush.

## SImage[¶](#simage)

### Basic Example[¶](#basic-example)

```json
{
    "SImage": {
        "Image": {
            "Style": "FEditorStyle",
            "Brush": "Icons.Help"
        }
    }
}
```

## Image Brush[¶](#image-brush)

### From Style[¶](#from-style)

```json
{
    "Image": {
        "Style": "FEditorStyle",
        "Brush": "Icons.Help"
    }
}
```

### From Texture[¶](#from-texture)

```json
{
    "Image": {
        "Texture": "/Engine/EngineResources/DefaultTexture"
    }
}
```

## Image Properties[¶](#image-properties)

### Color[¶](#color)

```json
{
    "SImage": {
        "Image": {...},
        "ColorAndOpacity": [1.0, 1.0, 1.0, 1.0]
    }
}
```

### Size[¶](#size)

```json
{
    "SImage": {
        "Image": {...},
        "DesiredSizeOverride": [32, 32]
    }
}
```

## Use Cases[¶](#use-cases)

- Icons in buttons
- Panel backgrounds
- Decorative elements

## Best Practices[¶](#best-practices)

- Use editor style icons for consistency
- Consider DPI scaling
- Use appropriate image sizes

 [Previous](using_buttons.html) [Next](using_texts.html)
