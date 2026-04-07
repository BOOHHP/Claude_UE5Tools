## Slate Overview[¶](#slate-overview)

This page provides an overview of the Slate UI framework used in TAPython.

## What is Slate?[¶](#what-is-slate)

Slate is the UI framework used by Unreal Engine for the editor interface. It provides:

- Declarative UI definition
- Rich widget library
- Customizable styling

## Slate in TAPython[¶](#slate-in-tapython)

TAPython uses JSON to define Slate UIs:

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "SButton": {
                    "Text": "Click Me"
                }
            }
        ]
    }
}
```

## Core Concepts[¶](#core-concepts)

### Widgets[¶](#widgets)

UI elements like buttons, text, images.

### Slots[¶](#slots)

Define content placement in containers.

### Attributes[¶](#attributes)

Configure widget properties.

## Common Widgets[¶](#common-widgets)

### Containers[¶](#containers)
- SVerticalBox
- SHorizontalBox
- SGridPanel
- SCanvas

### Controls[¶](#controls)
- SButton
- SCheckBox
- SComboBox

### Display[¶](#display)
- STextBlock
- SImage
- SBorder

## Layouts[¶](#layouts)

- [Directional Layout](https://www.tacolor.xyz/tapython/directional_layout.html)
- [Grid Layout](https://www.tacolor.xyz/tapython/grid_layout.html)
- [Canvas Layout](https://www.tacolor.xyz/tapython/canvas_layout.html)

## Next Steps[¶](#next-steps)

- [Box Layout](https://www.tacolor.xyz/tapython/box_layout.html)
- [Using Buttons](https://www.tacolor.xyz/tapython/using_buttons.html)

 [Previous](context_menus_for_slate_widget.html) [Next](cpp_to_json.html)
