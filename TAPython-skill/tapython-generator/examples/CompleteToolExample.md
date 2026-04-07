# Complete Tool Example: Batch Renamer

This example demonstrates the complete workflow of creating a TAPython tool from natural language requirements.

---

## User Input

```
"Create a tool to batch rename selected assets with a prefix"
```

---

## Step 1: Architecture Brief

**Tool Purpose**: Rename selected Content Browser assets by adding a user-provided prefix.

**Architecture**:
- **Menu Entry**: TA Python > Tools > Batch Renamer
- **UI**: Simple interface with prefix input and execute button
- **Controller**: Rename all selected assets with error handling
- **Feedback**: Status updates for success/failure

**Files to Generate**:
1. `MenuConfig.json` - Menu registration
2. `BatchRenamer/BatchRenamer.json` - UI definition
3. `BatchRenamer/BatchRenamer.py` - Controller logic

---

## Step 2: MenuConfig.json

**Location**: `<Project>/TA/TAPython/Python/MenuConfig.json`

```json
{
    "name": "TA Python",
    "items": [
        {
            "name": "Tools",
            "items": [
                {
                    "name": "Batch Renamer",
                    "ChameleonTools": "BatchRenamer/BatchRenamer.json"
                }
            ]
        }
    ]
}
```

**Explanation**:
- Creates menu section "TA Python" with submenu "Tools"
- Registers tool at path "BatchRenamer/BatchRenamer.json"
- Display name in menu: "Batch Renamer"

---

## Step 3: BatchRenamer.json

**Location**: `<Project>/TA/TAPython/Python/BatchRenamer/BatchRenamer.json`

```json
{
    "TabLabel": "Batch Renamer",
    "InitTabSize": [350, 200],

    "InitPyCmd": "import BatchRenamer; importlib.reload(BatchRenamer); BatchRenamer.instance = BatchRenamer.BatchRenamerController('%JsonPath')",

    "Root": {
        "SScrollBox": {
            "Slots": [
                {
                    "SVerticalBox": {
                        "Slots": [
                            {
                                "STextBlock": {
                                    "Text": "Batch Rename Tool",
                                    "Font": ["Segoe UI", "14", "Bold"]
                                }
                            },
                            {
                                "SBox": {
                                    "HeightOverride": 16
                                }
                            },
                            {
                                "STextBlock": {
                                    "Text": "Prefix to add:"
                                }
                            },
                            {
                                "SEditableText": {
                                    "Aka": "prefix_input",
                                    "HintText": "Enter prefix (e.g., 'TEST_')"
                                }
                            },
                            {
                                "SBox": {
                                    "HeightOverride": 8
                                }
                            },
                            {
                                "SButton": {
                                    "Aka": "btn_execute",
                                    "Text": "Rename Selected Assets",
                                    "HAlign": "Center"
                                }
                            },
                            {
                                "SBox": {
                                    "HeightOverride": 8
                                }
                            },
                            {
                                "STextBlock": {
                                    "Aka": "status_label",
                                    "Text": "Ready - Select assets in Content Browser",
                                    "ColorAndOpacity": [0.7, 0.7, 0.7, 1.0]
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

**Key Elements**:

1. **Window Setup**:
   - `TabLabel`: Window title "Batch Renamer"
   - `InitTabSize`: 350x200 pixels

2. **Initialization**:
   - `InitPyCmd`: Creates singleton instance
   - `importlib.reload()`: Auto-reload for development (remove for production)
   - `%JsonPath`: Required placeholder for ChameleonData

3. **UI Layout**:
   - `SScrollBox` root: Prevents overflow
   - `SVerticalBox`: Stacks widgets vertically
   - `SBox` with only height: Creates spacing

4. **Interactive Widgets** (all have `Aka`):
   - `prefix_input`: Text input for prefix
   - `btn_execute`: Execute button
   - `status_label`: Status display

5. **User Feedback**:
   - Hint text guides user
   - Initial status message
   - Gray color for neutral status

---

## Step 4: BatchRenamer.py

**Location**: `<Project>/TA/TAPython/Python/BatchRenamer/BatchRenamer.py`

```python
import unreal
import importlib

class BatchRenamerController:
    """
    Controller for Batch Renamer tool.
    Renames selected assets with a user-provided prefix.
    """

    def __init__(self, json_path: str):
        """
        Initialize controller with ChameleonData bridge.

        Args:
            json_path: Path to the tool's JSON file
        """
        self.json_path = json_path
        self.data = unreal.PythonBPLib.get_chameleon_data(json_path)

        # Initialize UI state
        self._setup_ui()

    def _setup_ui(self):
        """Set initial UI state."""
        try:
            self.data.set_text("status_label", "Ready - Select assets in Content Browser")
        except Exception as e:
            unreal.log_error(f"UI setup failed: {str(e)}")

    def rename_assets(self):
        """
        Rename all selected assets with the provided prefix.
        """
        try:
            # Get prefix from UI
            prefix = self.data.get_text("prefix_input").strip()

            if not prefix:
                self.data.set_text("status_label", "Error: Please enter a prefix")
                self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
                return

            # Get selected assets
            selected_assets = unreal.PythonBPLib.get_selected_assets()

            if not selected_assets:
                self.data.set_text("status_label", "Error: No assets selected")
                self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])
                return

            # Process assets
            renamed_count = 0
            failed_count = 0
            errors = []

            for asset in selected_assets:
                try:
                    asset_name = asset.get_name()
                    new_name = f"{prefix}{asset_name}"

                    # Rename asset
                    asset_path = asset.get_path_name()
                    success = unreal.EditorAssetLibrary.rename_asset(asset_path, new_name)

                    if success:
                        renamed_count += 1
                    else:
                        failed_count += 1
                        errors.append(f"Failed to rename: {asset_name}")

                except Exception as e:
                    failed_count += 1
                    errors.append(f"Error renaming {asset.get_name()}: {str(e)}")
                    unreal.log_error(f"Rename error: {str(e)}")
                    continue

            # Update UI with results
            if failed_count == 0:
                status_msg = f"✓ Successfully renamed {renamed_count} assets"
                self.data.set_text_color("status_label", [0.3, 1.0, 0.3, 1.0])  # Green
            else:
                status_msg = f"⚠ Renamed {renamed_count}, failed {failed_count}"
                self.data.set_text_color("status_label", [1.0, 0.7, 0.3, 1.0])  # Yellow

                # Log errors for debugging
                for error in errors:
                    unreal.log_warning(error)

            self.data.set_text("status_label", status_msg)

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            unreal.log_error(error_msg)
            self.data.set_text("status_label", error_msg)
            self.data.set_text_color("status_label", [1.0, 0.3, 0.3, 1.0])  # Red

# Module-level instance for singleton pattern
instance = None
```

**Key Elements**:

1. **Initialization**:
   - Stores `json_path` for reference
   - Initializes `ChameleonData` bridge
   - Calls `_setup_ui()` for initial state

2. **Error Handling**:
   - Wraps entire method in try-except
   - Wraps each asset operation in nested try-except
   - Logs errors with `unreal.log_error()`
   - Provides user feedback via status label

3. **Input Validation**:
   - Checks for empty prefix
   - Checks for empty asset selection
   - Provides clear error messages

4. **Processing Logic**:
   - Gets prefix from UI
   - Gets selected assets
   - Iterates with error handling
   - Tracks success/failure counts

5. **User Feedback**:
   - Color-coded status (green=success, yellow=partial, red=error)
   - Clear success/failure counts
   - Detailed error logging for debugging

6. **Singleton Pattern**:
   - Module-level `instance = None`
   - Matches InitPyCmd pattern

---

## Step 5: File Structure

```
<Project>/
└── TA/
    └── TAPython/
        └── Python/
            ├── MenuConfig.json
            └── BatchRenamer/
                ├── BatchRenamer.json
                └── BatchRenamer.py
```

---

## Step 6: Usage Instructions

1. **Open Tool**:
   - Navigate to menu: TA Python > Tools > Batch Renamer
   - Tool window opens with UI

2. **Use Tool**:
   - Select assets in Content Browser
   - Enter prefix in text field (e.g., "TEST_")
   - Click "Rename Selected Assets"

3. **View Results**:
   - Status label shows success/failure
   - Green = all renamed successfully
   - Yellow = some failed (see Output Log for details)
   - Red = error occurred

---

## Step 7: Testing Checklist

- [ ] Tool appears in menu
- [ ] Window opens with correct size
- [ ] UI displays correctly
- [ ] Can enter text in prefix field
- [ ] Button is clickable
- [ ] No assets selected: Shows error message
- [ ] Empty prefix: Shows error message
- [ ] Valid selection + prefix: Assets renamed
- [ ] Success message displayed
- [ ] Failed operations logged to Output Log
- [ ] Window can be closed without errors
- [ ] Tool can be reopened (singleton works)

---

## Validation Results

**MenuConfig.json**:
- ✅ Valid JSON syntax
- ✅ Contains name and items
- ✅ Path is relative

**BatchRenamer.json**:
- ✅ Valid JSON syntax
- ✅ Contains TabLabel and InitPyCmd
- ✅ InitPyCmd includes %JsonPath
- ✅ Singleton pattern in InitPyCmd
- ✅ All interactive widgets have Aka
- ✅ NO inline Python code
- ✅ Root wrapped in SScrollBox

**BatchRenamer.py**:
- ✅ Class name matches file name
- ✅ __init__ accepts json_path
- ✅ Initializes ChameleonData
- ✅ Module-level instance = None
- ✅ ALL unreal.xxx calls in try-except
- ✅ Errors logged
- ✅ User feedback provided
- ✅ Edge cases handled

---

## Next Steps

**For Production**:
1. Remove `importlib.reload()` from InitPyCmd
2. Add `OnClosePyCmd` for cleanup
3. Add more validation (invalid characters, name conflicts)
4. Add undo support if possible
5. Add unit tests

**For Enhancement**:
1. Add suffix option
2. Add find/replace option
3. Add preview before executing
4. Add filter by asset type
5. Add batch undo

---

This example demonstrates all best practices for TAPython tool development. Apply these patterns to create robust, maintainable tools.
