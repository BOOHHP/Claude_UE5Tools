## Modifying Slate Though Python[¶](#modifying-slate-though-python)

This guide explains how to modify Slate widgets from Python code.

## Overview[¶](#overview)

You can dynamically modify the UI by manipulating widgets from Python.

## Common Operations[¶](#common-operations)

### Show/Hide Widget[¶](#showhide-widget)

```python
# Show widget
data.set_visible("WidgetId", True)

# Hide widget
data.set_visible("WidgetId", False)
```

### Enable/Disable Widget[¶](#enabledisable-widget)

```python
# Enable widget
data.set_enabled("WidgetId", True)

# Disable widget
data.set_enabled("WidgetId", False)
```

### Set Focus[¶](#set-focus)

```python
data.set_focus("WidgetId")
```

## Dynamic Content[¶](#dynamic-content)

### Update Text[¶](#update-text)

```python
data.set_text("TextBlockId", "New text")
```

### Update List[¶](#update-list)

```python
data.set_list_items("ListViewId", ["Item 1", "Item 2", "Item 3"])
```

## Refresh UI[¶](#refresh-ui)

### Full Refresh[¶](#full-refresh)

```python
data.refresh("ToolPath")
```

### Widget Refresh[¶](#widget-refresh)

```python
data.refresh_widget("WidgetId")
```

## Use Cases[¶](#use-cases)

- Form validation feedback
- Loading states
- Dynamic content updates

 [Previous](get_value_from_slate.html) [Next](execute_order_of_python_code_in_chameleon_tool.html)
