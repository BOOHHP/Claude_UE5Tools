# Widget Catalog

TAPython provides a comprehensive set of Slate widgets for building Unreal Editor tools. This catalog covers the most commonly used widgets with examples and Python integration.

## Widget Categories

- [Input Widgets](#input-widgets) - User input controls
- [Display Widgets](#display-widgets) - Information display
- [Action Widgets](#action-widgets) - User interaction
- [Container Widgets](#container-widgets) - Layout and organization

---

## Input Widgets

### SEditableText - Single-line text input

**Purpose**: Single-line text input field for user data entry.

**JSON Definition**:
```json
{
    "SEditableText": {
        "Aka": "input_name",
        "HintText": "Enter name...",
        "Text": "default value"
    }
}
```

**Python Access**:
```python
# Get value
text = self.data.get_text("input_name")

# Set value
self.data.set_text("input_name", "new value")
```

**Common Properties**:
- `Aka` (required): Unique identifier
- `HintText`: Placeholder text when empty
- `Text`: Default/initial value
- `IsReadOnly`: Make read-only
- `Font`: Font specification ["FontName", "Size"]

---

### SMultiLineEditableText - Multi-line text area

**Purpose**: Multi-line text input for longer content.

**JSON Definition**:
```json
{
    "SMultiLineEditableText": {
        "Aka": "description",
        "HintText": "Enter description..."
    }
}
```

**Python Access**:
```python
text = self.data.get_text("description")
self.data.set_text("description", "Multi-line\ntext content")
```

---

### SCheckBox - Checkbox/toggle

**Purpose**: Boolean option toggle.

**JSON Definition**:
```json
{
    "SCheckBox": {
        "Aka": "option_enabled",
        "IsChecked": false
    }
}
```

**Python Access**:
```python
# Get state
is_checked = self.data.get_checkbox_state("option_enabled")

# Set state
self.data.set_checkbox_state("option_enabled", True)
```

---

### SComboBox - Dropdown selector

**Purpose**: Single-selection dropdown from predefined options.

**JSON Definition**:
```json
{
    "SComboBox": {
        "Aka": "mode_selector",
        "Options": ["Option A", "Option B", "Option C"],
        "SelectedItem": "Option A"
    }
}
```

**Python Access**:
```python
# Get selection
selected = self.data.get_combo_box_selection("mode_selector")

# Set selection
self.data.set_combo_box_selection("mode_selector", "Option B")
```

---

### SSpinBox - Numeric input with spinner

**Purpose**: Numeric value input with increment/decrement buttons.

**JSON Definition**:
```json
{
    "SSpinBox": {
        "Aka": "count_input",
        "Value": 10,
        "MinValue": 0,
        "MaxValue": 100,
        "MinSliderValue": 0,
        "MaxSliderValue": 50
    }
}
```

**Python Access**:
```python
# Get value
count = self.data.get_spin_box_value("count_input")

# Set value
self.data.set_spin_box_value("count_input", 25)
```

---

## Display Widgets

### STextBlock - Static text

**Purpose**: Display static or dynamic text labels.

**JSON Definition**:
```json
{
    "STextBlock": {
        "Aka": "status_label",
        "Text": "Ready",
        "ColorAndOpacity": [1.0, 1.0, 1.0, 1.0],
        "Font": ["Segoe UI", "12"]
    }
}
```

**Python Access**:
```python
# Set text
self.data.set_text("status_label", "Processing...")

# Set text color (RGBA 0.0-1.0)
self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])  # Red
```

**Common Properties**:
- `Text`: Display text
- `ColorAndOpacity`: RGBA color [R, G, B, A]
- `Font`: Font specification ["FontName", "Size", "Style"]
- `Justification`: Text alignment (Left, Center, Right)

---

### SImage - Icon/image display

**Purpose**: Display icons or images.

**JSON Definition**:
```json
{
    "SImage": {
        "Aka": "icon_preview",
        "Image": "EditorStyleSet.PropertyEditor.Standalone"
    }
}
```

**Common Icon Sources**:
- `EditorStyleSet.PropertyEditor.Standalone`
- `EditorStyleSet.Icon.Font`
- `EditorStyleSet.Icon.Level`
- `EditorStyleSet.Icon.Settings`

---

### SSeparator - Visual separator

**Purpose**: Horizontal or vertical line separator.

**JSON Definition**:
```json
{
    "SSeparator": {
        "Orientation": "Horizontal",
        "Thickness": 1.0
    }
}
```

---

## Action Widgets

### SButton - Button control

**Purpose**: Trigger actions on click.

**JSON Definition**:
```json
{
    "SButton": {
        "Aka": "btn_execute",
        "Text": "Execute",
        "HAlign": "Center",
        "VAlign": "Center"
    }
}
```

**Python Access**:
```python
# Check if clicked (polling method)
if self.data.get_button_click("btn_execute"):
    self.execute_action()
```

**Common Properties**:
- `Text`: Button label
- `HAlign`: Horizontal alignment (Left, Center, Right, Fill)
- `VAlign`: Vertical alignment (Top, Center, Bottom, Fill)
- `ButtonStyle`: Visual style override

**CRITICAL**: Do NOT use inline Python in `OnClick`. Always use `Aka` and handle in controller.

---

### SHyperlink - Clickable link

**Purpose**: Navigate to external resources or documentation.

**JSON Definition**:
```json
{
    "SHyperlink": {
        "Text": "Open Documentation",
        "NavigateURL": "https://docs.example.com"
    }
}
```

---

## Container Widgets

### SVerticalBox - Vertical stack layout

**Purpose**: Stack child widgets vertically.

**JSON Definition**:
```json
{
    "SVerticalBox": {
        "Slots": [
            { "STextBlock": { "Text": "Item 1" } },
            { "STextBlock": { "Text": "Item 2" } },
            { "STextBlock": { "Text": "Item 3" } }
        ]
    }
}
```

---

### SHorizontalBox - Horizontal row layout

**Purpose**: Arrange child widgets horizontally.

**JSON Definition**:
```json
{
    "SHorizontalBox": {
        "Slots": [
            { "SButton": { "Text": "OK" } },
            { "SButton": { "Text": "Cancel" } }
        ]
    }
}
```

---

### SScrollBox - Scrollable container

**Purpose**: Make content scrollable when it exceeds viewport.

**JSON Definition**:
```json
{
    "SScrollBox": {
        "Slots": [
            { /* widgets */ }
        ]
    }
}
```

**Common Usage**: Wrap root widget in SScrollBox to prevent content overflow.

---

### SBox - Size-constrained container

**Purpose**: Constrain widget dimensions.

**JSON Definition**:
```json
{
    "SBox": {
        "WidthOverride": 300,
        "HeightOverride": 200,
        "Content": {
            "STextBlock": { "Text": "Content" }
        }
    }
}
```

**Properties**:
- `WidthOverride`: Fixed width in pixels
- `HeightOverride`: Fixed height in pixels
- `MinDesiredWidth`: Minimum width
- `MinDesiredHeight`: Minimum height
- `MaxDesiredWidth`: Maximum width
- `MaxDesiredHeight`: Maximum height

---

### SGridPanel - Grid layout

**Purpose**: Arrange widgets in a grid with row/column positioning.

**JSON Definition**:
```json
{
    "SGridPanel": {
        "Slots": [
            {
                "STextBlock": { "Text": "Label:" },
                "Row": 0, "Column": 0
            },
            {
                "SEditableText": {
                    "Aka": "input_value",
                    "HintText": "Value..."
                },
                "Row": 0, "Column": 1
            },
            {
                "STextBlock": { "Text": "Count:" },
                "Row": 1, "Column": 0
            },
            {
                "SSpinBox": {
                    "Aka": "count_input",
                    "Value": 10
                },
                "Row": 1, "Column": 1
            }
        ]
    }
}
```

---

### SBorder - Bordered container

**Purpose**: Add border around content.

**JSON Definition**:
```json
{
    "SBorder": {
        "BorderImage": "EditorStyleSet.PropertyEditor.Standalone",
        "Content": {
            "STextBlock": { "Text": "Bordered content" }
        }
    }
}
```

---

### SOverlay - Stacked layers

**Purpose**: Stack widgets on top of each other.

**JSON Definition**:
```json
{
    "SOverlay": {
        "Slots": [
            {
                "SImage": {
                    "Image": "BackgroundImage"
                }
            },
            {
                "STextBlock": {
                    "Text": "Overlay text"
                }
            }
        ]
    }
}
```

---

### SSplitter - Resizable panels

**Purpose**: Create resizable split panels.

**JSON Definition**:
```json
{
    "SSplitter": {
        "Orientation": "Horizontal",
        "Slots": [
            {
                "SVerticalBox": {
                    "Slots": [/* Left panel content */]
                },
                "Size": 0.3
            },
            {
                "SVerticalBox": {
                    "Slots": [/* Right panel content */]
                },
                "Size": 0.7
            }
        ]
    }
}
```

---

## Widget Styling

### Font Specification

Format: `["FontName", "Size", "Style"]`

```json
"Font": ["Segoe UI", "12"]          // Name, Size
"Font": ["Segoe UI", "12", "Bold"]  // Name, Size, Style
```

### Color Specification

Format: `[R, G, B, A]` where values are 0.0-1.0

```json
"ColorAndOpacity": [1.0, 1.0, 1.0, 1.0]  // White
"ColorAndOpacity": [1.0, 0.3, 0.3, 1.0]  // Red
"ColorAndOpacity": [0.3, 1.0, 0.3, 1.0]  // Green
```

### Alignment Values

**Horizontal**: `Left`, `Center`, `Right`, `Fill`
**Vertical**: `Top`, `Center`, `Bottom`, `Fill`

```json
{
    "SButton": {
        "Text": "Centered",
        "HAlign": "Center",
        "VAlign": "Center"
    }
}
```

---

## Common Patterns

### Spacing Between Widgets

Use `SBox` with only height/width for spacing:

```json
{
    "SBox": {
        "HeightOverride": 8
    }
}
```

### Labeled Input Group

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Input Label:",
                    "Font": ["Segoe UI", "10"]
                }
            },
            {
                "SEditableText": {
                    "Aka": "input_field",
                    "HintText": "Enter value..."
                }
            }
        ]
    }
}
```

### Button Group

```json
{
    "SHorizontalBox": {
        "Slots": [
            {
                "SButton": {
                    "Aka": "btn_ok",
                    "Text": "OK"
                }
            },
            {
                "SBox": { "WidthOverride": 4 }
            },
            {
                "SButton": {
                    "Aka": "btn_cancel",
                    "Text": "Cancel"
                }
            }
        ]
    }
}
```

---

## Best Practices

1. **Always add Aka to interactive widgets** - Required for data binding
2. **Use containers for layout** - Never position widgets without containers
3. **Wrap root in SScrollBox** - Prevents content overflow
4. **Use SBox for spacing** - Consistent spacing between elements
5. **Group related inputs** - Use SVerticalBox for logical grouping
6. **Provide visual feedback** - Use text color changes for status updates

---

For complete widget reference, see [Slate Overview](../TAPython_docs/Slate Overview.md).
