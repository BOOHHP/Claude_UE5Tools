## Using Rich Text[¶](#using-rich-text)

This guide explains how to use rich text in Chameleon UI.

## Overview[¶](#overview)

Rich text allows formatted text with multiple styles in a single block.

## SRichTextBlock[¶](#srichtextblock)

### Basic Example[¶](#basic-example)

```json
{
    "SRichTextBlock": {
        "Text": "This is [b]bold[/b] and this is [i]italic[/i]"
    }
}
```

## Rich Text Syntax[¶](#rich-text-syntax)

### Basic Formatting[¶](#basic-formatting)

- `[b]text[/b]` - Bold
- `[i]text[/i]` - Italic
- `[u]text[/u]` - Underline
- `[s]text[/s]` - Strikethrough

### Colors[¶](#colors)

```json
{
    "SRichTextBlock": {
        "Text": "This is [color=#FF0000]red[/color] text"
    }
}
```

### Hyperlinks[¶](#hyperlinks)

```json
{
    "SRichTextBlock": {
        "Text": "Visit [url=https://example.com]our site[/url]"
    }
}
```

## Styling[¶](#styling)

### Default Style[¶](#default-style)

```json
{
    "SRichTextBlock": {
        "Text": "Rich text content",
        "TextStyle": "Normal"
    }
}
```

### Custom Decorator[¶](#custom-decorator)

Create custom text decorators for special formatting.

## Use Cases[¶](#use-cases)

- Formatted messages
- Documentation displays
- Dynamic content with mixed styles

 [Previous](using_texts.html) [Next](using_drag_and_drop_area.html)
