# MenuConfig.json Template

## Basic Structure

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "Tools",
            "items": [
                {
                    "name": "[Tool Display Name]",
                    "ChameleonTools": "[ToolName]/[ToolName].json"
                }
            ]
        }
    ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Display text in menu |
| `ChameleonTools` | Yes | Relative path to tool JSON from Python directory |
| `command` | No | Direct Python command instead of opening tool |
| `shortcut` | No | Keyboard shortcut (e.g., "Ctrl+Shift+T") |
| `separator` | No | Add visual separator before this item |

## Menu Placement Options

Menu items can be placed at various anchor points in the Unreal Editor. The most common anchor is `"OnToolBarChameleon"`, which adds items to the main toolbar.

### Example: Multi-Level Menu

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "Asset Tools",
            "items": [
                {
                    "name": "Batch Renamer",
                    "ChameleonTools": "BatchRenamer/BatchRenamer.json"
                },
                {
                    "name": "Asset Organizer",
                    "ChameleonTools": "AssetOrganizer/AssetOrganizer.json"
                }
            ]
        },
        {
            "name": "Level Tools",
            "items": [
                {
                    "name": "Actor Spawner",
                    "ChameleonTools": "ActorSpawner/ActorSpawner.json"
                }
            ]
        }
    ]
}
```

### Example: Menu with Shortcuts and Separators

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "Quick Rename",
            "ChameleonTools": "BatchRenamer/BatchRenamer.json",
            "shortcut": "Ctrl+Shift+R"
        },
        {
            "separator": true
        },
        {
            "name": "Settings",
            "ChameleonTools": "Settings/Settings.json"
        }
    ]
}
```

## Validation Checklist

- [ ] Valid JSON syntax (no trailing commas, proper quoting)
- [ ] Contains `"name"` field for menu section
- [ ] Contains `"items"` array
- [ ] Each item has either `"ChameleonTools"` or `"command"`
- [ ] Paths are relative to `<Project>/TA/TAPython/Python/` directory
- [ ] No absolute paths used
