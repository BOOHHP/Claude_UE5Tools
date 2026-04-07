# UI.json Template

## Basic Structure

```json
{
    "TabLabel": "[Tool Display Name]",
    "InitTabSize": [400, 500],

    "InitPyCmd": "import [ToolName]; importlib.reload([ToolName]); [ToolName].instance = [ToolName].[ToolName]Controller('%JsonPath')",

    "Root": {
        "SScrollBox": {
            "Slots": [
                {
                    "SVerticalBox": {
                        "Slots": [
                            {
                                "STextBlock": {
                                    "Text": "Input Section",
                                    "Font": ["Segoe UI", "12"]
                                }
                            },
                            {
                                "SEditableText": {
                                    "Aka": "input_field",
                                    "HintText": "Enter value..."
                                }
                            },
                            {
                                "SHorizontalBox": {
                                    "Slots": [
                                        {
                                            "SButton": {
                                                "Aka": "btn_execute",
                                                "Text": "Execute",
                                                "HAlign": "Center"
                                            }
                                        },
                                        {
                                            "SButton": {
                                                "Aka": "btn_cancel",
                                                "Text": "Cancel"
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "STextBlock": {
                                    "Aka": "status_label",
                                    "Text": "Ready",
                                    "ColorAndOpacity": [0.8, 0.8, 0.8, 1.0]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
```

## Critical Fields

| Field | Purpose | Required |
|-------|---------|----------|
| `TabLabel` | Window title | Yes |
| `InitTabSize` | [width, height] in pixels | Yes |
| `InitPyCmd` | Python initialization command with `%JsonPath` | Yes |
| `Aka` | Unique identifier for each interactive widget | Yes (for interactive widgets) |

## InitPyCmd Pattern

The initialization command MUST follow this pattern:

```json
"InitPyCmd": "import [ToolName]; importlib.reload([ToolName]); [ToolName].instance = [ToolName].[ToolName]Controller('%JsonPath')"
```

**Components:**
1. `import [ToolName]` - Import the module
2. `importlib.reload([ToolName])` - Auto-reload for development (remove for production)
3. `[ToolName].instance = [ToolName].[ToolName]Controller('%JsonPath')` - Create singleton instance
4. `'%JsonPath'` - Placeholder for JSON file path (REQUIRED)

## Root Container Pattern

Always wrap the root in a container widget to prevent overflow:

### Option 1: SScrollBox (Recommended)
```json
"Root": {
    "SScrollBox": {
        "Slots": [ /* widgets */ ]
    }
}
```

### Option 2: SBox (Size-constrained)
```json
"Root": {
    "SBox": {
        "WidthOverride": 300,
        "HeightOverride": 200,
        "Content": {
            /* widgets */
        }
    }
}
```

### Option 3: SVerticalBox (Simple layouts)
```json
"Root": {
    "SVerticalBox": {
        "Slots": [ /* widgets */ ]
    }
}
```

## Common Layout Patterns

### Input Form Layout
```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "STextBlock": {
                    "Text": "Field Label",
                    "Font": ["Segoe UI", "10"]
                }
            },
            {
                "SEditableText": {
                    "Aka": "input_field",
                    "HintText": "Enter value..."
                }
            },
            {
                "SBox": { "HeightOverride": 8 }
            }
        ]
    }
}
```

### Button Row Layout
```json
{
    "SHorizontalBox": {
        "Slots": [
            {
                "SButton": {
                    "Aka": "btn_ok",
                    "Text": "OK",
                    "HAlign": "Center"
                }
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

### Grid Layout
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
            }
        ]
    }
}
```

## OnClosePyCmd Pattern (Optional but Recommended)

Add cleanup when tool window closes:

```json
{
    "InitPyCmd": "import MyTool; MyTool.instance = MyTool.MyTool('%JsonPath')",
    "OnClosePyCmd": "MyTool.instance.cleanup(); MyTool.instance = None"
}
```

## Validation Checklist

- [ ] Valid JSON syntax
- [ ] Contains `"TabLabel"` for window title
- [ ] Contains `"InitPyCmd"` with `%JsonPath` placeholder
- [ ] InitPyCmd creates singleton instance: `Module.instance = Module.Controller('%JsonPath')`
- [ ] Every interactive widget has `"Aka"` field (buttons, inputs, checkboxes, etc.)
- [ ] **NO inline Python code** in `"OnClick"`, `"OnValueChanged"`, etc.
- [ ] Root widget is container type (SScrollBox, SBox, SVerticalBox, etc.)
- [ ] All Aka values are unique within the tool
- [ ] Optional: Auto-reload in InitPyCmd for development: `importlib.reload(Module)`
