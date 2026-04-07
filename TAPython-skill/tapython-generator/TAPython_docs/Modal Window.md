## Modal Window[¶](#modal-window)

This guide explains how to create modal windows in Chameleon.

## Overview[¶](#overview)

Modal windows are dialog boxes that block interaction with the rest of the UI until closed.

## Creating a Modal[¶](#creating-a-modal)

### Using SWindow[¶](#using-swindow)

```json
{
    "SWindow": {
        "Title": "Confirm Action",
        "Size": [400, 200],
        "Content": {
            "SVerticalBox": {
                "Slots": [
                    {
                        "STextBlock": {
                            "Text": "Are you sure?"
                        }
                    },
                    {
                        "SHorizontalBox": {
                            "Slots": [
                                {
                                    "SButton": {
                                        "Text": "Yes",
                                        "OnClick": "tool.on_yes()"
                                    }
                                },
                                {
                                    "SButton": {
                                        "Text": "No",
                                        "OnClick": "tool.on_no()"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

## Modal Properties[¶](#modal-properties)

### Title[¶](#title)

Window title:

```json
{
    "Title": "My Dialog"
}
```

### Size[¶](#size)

```json
{
    "Size": [400, 300]
}
```

### Modal[¶](#modal)

```json
{
    "bModal": true
}
```

## Closing the Modal[¶](#closing-the-modal)

### From Python[¶](#from-python)

```python
data.request_close()
```

## Use Cases[¶](#use-cases)

- Confirmations
- Settings dialogs
- Input forms

 [Previous](using_list_view.html) [Next](chameleon_tool.html)
