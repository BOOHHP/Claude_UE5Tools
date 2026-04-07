## Variable Placeholder[¶](#variable-placeholder)

This guide explains variable placeholders in Chameleon.

## Overview[¶](#overview)

Variable placeholders are special values that get replaced with runtime data when the UI is generated.

## Common Placeholders[¶](#common-placeholders)

### %JsonPath[¶](#jsonpath)

The path to the current JSON file:

```python
self.json_path = json_path  # Receives %JsonPath
```

### %toolPath[¶](#toolpath)

The tool's path:

```python
# Available in callbacks
tool_path = data.get_var("%toolPath")
```

### %widgetPath[¶](#widgetpath)

The widget's path (for SButton OnClick):

```python
def on_click(self):
    widget_path = data.get_var("%widgetPath")
```

### %selectedObjects[¶](#selectedobjects)

Selected objects in the editor:

```python
# In a callback
selected = data.get_var("%selectedObjects")
```

## Using Placeholders[¶](#using-placeholders)

### In JSON[¶](#in-json)

```json
{
    "OnClick": "tool.handle_click(%widgetPath)"
}
```

### In Python[¶](#in-python)

```python
widget_path = data.get_var("%widgetPath")
```

## Custom Variables[¶](#custom-variables)

### Setting Variables[¶](#setting-variables)

```python
data.set_var("myVar", "myValue")
```

### Getting Variables[¶](#getting-variables)

```python
value = data.get_var("myVar")
```

 [Previous](chameleon_tool.html) [Next](get_value_from_slate.html)
