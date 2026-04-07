## C++ to JSON[¶](#cpp-to-json)

This guide explains how to convert C++ Slate code to JSON for TAPython.

## Overview[¶](#overview)

If you have existing C++ Slate code, you can convert it to JSON for use with TAPython.

## Basic Conversion[¶](#basic-conversion)

### C++ Code[¶](#c++-code)

```cpp
SNew(SVerticalBox)
+ SVerticalBox::Slot()
[
    SNew(SButton)
    .Text(FText::FromString("Click Me"))
]
```

### JSON Equivalent[¶](#json-equivalent)

```json
{
    "SVerticalBox": {
        "Slots": [
            {
                "SButton": {
                    "Text": "Click Me"
                }
            }
        ]
    }
}
```

## Conversion Rules[¶](#conversion-rules)

1. **SNew()** → Object key
2. **Operators (+)** → Slots array
3. **Dot operators (.)** → Object properties
4. **FText::FromString()** → String value

## Examples[¶](#examples)

### Button with Click Handler[¶](#button-with-click-handler)

C++:
```cpp
SNew(SButton)
.OnClicked(FOnClicked::CreateLambda([](){ return EHandleResult::Handled; }))
```

JSON:
```json
{
    "SButton": {
        "OnClick": "print('clicked')"
    }
}
```

## Tool[¶](#tool)

Use the C++ to JSON converter in Chameleon Gallery for quick conversion.

 [Previous](slate_overview.html) [Next](directional_layout.html)
