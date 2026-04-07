## Grid Layout[¶](#grid-layout)

This guide explains how to use the Grid layout in Chameleon.

## Overview[¶](#overview)

The Grid layout arranges widgets in a grid with rows and columns.

## SGridPanel[¶](#sgridpanel)

### Basic Example[¶](#basic-example)

```json
{
    "SGridPanel": {
        "Slots": [
            {
                "Row": 0,
                "Column": 0,
                "STextBlock": {
                    "Text": "Cell 0,0"
                }
            },
            {
                "Row": 0,
                "Column": 1,
                "STextBlock": {
                    "Text": "Cell 0,1"
                }
            }
        ]
    }
}
```

## Slot Properties[¶](#slot-properties)

### Positioning[¶](#positioning)

- `Row`: Row index (0-based)
- `Column`: Column index (0-based)
- `RowSpan`: Number of rows to span
- `ColumnSpan`: Number of columns to span

### Size[¶](#size)

- `SizeCoefficient`: Relative size

## Use Cases[¶](#use-cases)

- Forms with labels and inputs
- Dashboard layouts
- Matrix displays

## Example[¶](#example)

```json
{
    "SGridPanel": {
        "FillRow": 1,
        "Slots": [
            {
                "Row": 0,
                "Column": 0,
                "STextBlock": {"Text": "Name:"}
            },
            {
                "Row": 0,
                "Column": 1,
                "SEditableText": {"Text": ""}
            },
            {
                "Row": 1,
                "Column": 0,
                "STextBlock": {"Text": "Email:"}
            },
            {
                "Row": 1,
                "Column": 1,
                "SEditableText": {"Text": ""}
            }
        ]
    }
}
```

 [Previous](splitter_layout.html) [Next](box_layout.html)
