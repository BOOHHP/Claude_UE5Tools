## Using Slate to Add Interface for Python Tools[¶](#using-slate-to-add-interface-for-python-tools)

This guide explains how to use Slate (the UI framework used by Unreal Engine) to create interfaces for your Python tools.

## What is Slate?[¶](#what-is-slate)

Slate is the UI framework used in the Unreal Engine editor. It provides:

- Rich UI capabilities
- Consistent editor look and feel
- Performance-optimized rendering

## TAPython Chameleon[¶](#tapython-chameleon)

TAPython provides "Chameleon" - a system to create UI using JSON files:

```json
{
    "TabLabel": "My Tool",
    "InitTabSize": [400, 300],
    "Root": {
        "SVerticalBox": {
            "Slots": [
                {
                    "SButton": {
                        "Text": "Click Me",
                        "OnClick": "print('Button clicked!')"
                    }
                }
            ]
        }
    }
}
```

## Getting Started[¶](#getting-started)

1. Create a JSON file defining your UI
2. Use the `unreal.ChameleonData.launch_chameleon_tool()` to open it
3. Connect Python callbacks to UI events

## Available Widgets[¶](#available-widgets)

TAPython supports many Slate widgets:

- SButton, SCheckBox, SComboBox
- STextBlock, SEditableText
- SVerticalBox, SHorizontalBox
- SScrollBox, SListView
- And many more...

## Next Steps[¶](#next-steps)

- [Polishing UI with Sketch](https://www.tacolor.xyz/tapython/polishing_ui_with_sketch.html)
- [Slate Overview](https://www.tacolor.xyz/tapython/slate_overview.html)
- [Built-in Tools](https://www.tacolor.xyz/tapython/built-in_tools.html)

 [Previous](add_menu_items_to_unreal_editor.html) [Next](polishing_ui_with_sketch.html)
