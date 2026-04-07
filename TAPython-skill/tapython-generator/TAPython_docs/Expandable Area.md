## Expandable Area[¶](#expandable-area)

This guide explains the Expandable Area widget in Chameleon.

## Overview[¶](#overview)

The Expandable Area widget provides a collapsible section that can be expanded or collapsed by clicking its header.

## SExpandableArea[¶](#sexpandablearea)

### Basic Example[¶](#basic-example)

```json
{
    "SExpandableArea": {
        "AreaTitle": "Advanced Options",
        "AreaTitleFont": {
            "FontObject": "/Engine/EngineFonts/Roboto",
            "Size": 14
        },
        "BorderBackgroundColor": {
            "R": 0.1,
            "G": 0.1,
            "B": 0.1,
            "A": 1.0
        },
        "OnExpansionChanged": "tool.on_expansion_changed()",
        "BodyContent": {
            "SVerticalBox": {
                "Slots": [
                    {
                        "STextBlock": {
                            "Text": "Hidden content here"
                        }
                    }
                ]
            }
        }
    }
}
```

## Configuration[¶](#configuration)

### Area Title[¶](#area-title)

- `AreaTitle`: Text displayed in the header
- `AreaTitleFont`: Font for the title

### Collapsed State[¶](#collapsed-state)

- `InitiallyCollapsed`: Start in collapsed state
- `CollapseOnExpand`: Auto-collapse when other areas expand

### Styling[¶](#styling)

- `BorderBackgroundColor`: Background color
- `BorderImage`: Custom border image
- `HeaderPadding`: Padding around header content

## Callbacks[¶](#callbacks)

### OnExpansionChanged[¶](#onexpansionchanged)

Called when the area is expanded or collapsed:

```python
def on_expansion_changed(self, is_expanded):
    if is_expanded:
        print("Area expanded")
    else:
        print("Area collapsed")
```

## Use Cases[¶](#use-cases)

- Collapsible settings panels
- Advanced options sections
- Grouped content

 [Previous](canvas_layout.html) [Next](padding_and_margin.html)
