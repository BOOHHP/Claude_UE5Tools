## Editor Style[¶](#editor-style)

This guide explains how to use editor styles in Chameleon.

## Overview[¶](#overview)

Unreal Editor provides a set of built-in styles that you can use to make your tools match the editor's look and feel.

## Using Editor Styles[¶](#using-editor-styles)

### In JSON[¶](#in-json)

```json
{
    "SBorder": {
        "BorderImage": {
            "Style": "FEditorStyle",
            "Brush": "ToolPanel.DarkGroupBorder"
        }
    }
}
```

## Available Brushes[¶](#available-brushes)

### Panel Brushes[¶](#panel-brushes)

- `ToolPanel.DarkGroupBorder` - Dark panel border
- `ToolPanel.LightGroupBorder` - Light panel border
- `ToolPanel.GroupBorder` - Default group border

### Button Brushes[¶](#button-brushes)

- `Button` - Default button
- `Button.Primary` - Primary button
- `Button.Success` - Success button

### Common Brushes[¶](#common-brushes)

- `Border` - Simple border
- `WhiteBrush` - Solid white
- `NoBorder` - No border

## Custom Styles[¶](#custom-styles)

You can also create custom styles and reference them.

## Best Practices[¶](#best-practices)

- Use FEditorStyle brushes for consistency
- Match editor dark/light theme
- Test with different editor themes

## Resources[¶](#resources)

- [Chameleon Gallery](https://www.tacolor.xyz/tapython/chameleon_gallery.html) - Style examples
- [Colors in TAPython](https://www.tacolor.xyz/tapython/colors_in_tapython.html)

 [Previous](padding_and_margin.html) [Next](colors_in_tapython.html)
