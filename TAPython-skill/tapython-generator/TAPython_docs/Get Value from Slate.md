## Get Value from Slate[¶](#get-value-from-slate)

This guide explains how to get values from Slate widgets.

## Overview[¶](#overview)

You can retrieve values from user input widgets like text fields, checkboxes, and combo boxes.

## Getting Widget Values[¶](#getting-widget-values)

### Text Input[¶](#text-input)

```python
# Get text from SEditableText
text = data.get_text("TextInputId")
```

### Checkbox[¶](#checkbox)

```python
# Get checked state
is_checked = data.get_checkbox_state("CheckboxId")
```

### ComboBox[¶](#combobox)

```python
# Get selected item
selected = data.get_combo_box_selection("ComboBoxId")
```

## Setting Widget Values[¶](#setting-widget-values)

### Text Input[¶](#text-input)

```python
# Set text
data.set_text("TextInputId", "New text")
```

### Checkbox[¶](#checkbox)

```python
# Set checked state
data.set_checkbox_state("CheckboxId", True)
```

## Identifying Widgets[¶](#identifying-widgets)

Add IDs to widgets:

```json
{
    "SEditableText": {
        "Id": "TextInputId",
        "Text": ""
    }
}
```

## Use Cases[¶](#use-cases)

- Form submission
- Settings persistence
- User input handling

 [Previous](variable_placeholder.html) [Next](modifying_slate_though_python.html)
