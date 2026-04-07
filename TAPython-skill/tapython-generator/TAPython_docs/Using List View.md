## Using List View[¶](#using-list-view)

This guide explains how to use List View in Chameleon UI.

## Overview[¶](#overview)

List View displays a scrollable list of items that can be selected.

## SListView[¶](#slistview)

### Basic Example[¶](#basic-example)

```json
{
    "SListView": {
        "ItemsSource": "my_list",
        "OnGenerateRow": "tool.generate_row()",
        "OnSelectionChanged": "tool.on_selection_changed()"
    }
}
```

## Configuration[¶](#configuration)

### Items Source[¶](#items-source)

The data to display:

```python
self.my_list = ["Item 1", "Item 2", "Item 3"]
```

### Row Generation[¶](#row-generation)

Generate each row:

```python
def generate_row(self, item):
    # Return JSON for row widget
    return {"STextBlock": {"Text": item}}
```

### Selection Mode[¶](#selection-mode)

- `Single`: Single item selection
- `Multi`: Multiple item selection
- `None`: No selection

## Methods[¶](#methods)

### Refresh[¶](#refresh)

```python
data.refresh_list("ListViewId")
```

### Get Selected Items[¶](#get-selected-items)

```python
selected = data.get_selected_items("ListViewId")
```

## Use Cases[¶](#use-cases)

- Asset browsers
- File lists
- Data tables

 [Previous](using_drag_and_drop_area.html) [Next](modal_window.html)
