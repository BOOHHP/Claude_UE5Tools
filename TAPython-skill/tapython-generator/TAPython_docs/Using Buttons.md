## Using Buttons[¶](#using-buttons)

This guide explains how to use buttons in Chameleon UI.

## Overview[¶](#overview)

Buttons are interactive widgets that trigger actions when clicked.

## SButton[¶](#sbutton)

### Basic Example[¶](#basic-example)

```json
{
    "SButton": {
        "Text": "Click Me",
        "OnClick": "print('Button clicked!')"
    }
}
```

## Button Properties[¶](#button-properties)

### Text[¶](#text)

```json
{
    "SButton": {
        "Text": "Button Text"
    }
}
```

### Tooltip[¶](#tooltip)

```json
{
    "SButton": {
        "Text": "Hover Me",
        "ToolTip": "This is a tooltip"
    }
}
```

### Styling[¶](#styling)

```json
{
    "SButton": {
        "Text": "Styled Button",
        "ButtonStyle": {
            "Style": "FEditorStyle",
            "Normal": "Button",
            "Hovered": "Button.Hovered",
            "Pressed": "Button.Pressed"
        }
    }
}
```

## Callbacks[¶](#callbacks)

### OnClick[¶](#onclick)

Called when button is clicked:

```python
def on_click(self):
    print("Clicked!")
```

### OnPressed / OnReleased[¶](#onpressed--onreleased)

```json
{
    "OnPressed": "tool.on_pressed()",
    "OnReleased": "tool.on_released()"
}
```

## Button Types[¶](#button-types)

- Regular buttons
- Toggle buttons
- Icon buttons

## Advanced[¶](#advanced)

### Using External JSON[¶](#using-external-json)

You can define button code in external JSON files for reuse.

 [Previous](colors_in_tapython.html) [Next](use_images_and_image_brush.html)
