## Auto Complete for TAPython[¶](#auto-complete-for-tapython)

This guide explains how to set up autocomplete for TAPython in your IDE.

## Overview[¶](#overview)

Autocomplete helps you write code faster by suggesting completions as you type.

## PyCharm Setup[¶](#pycharm-setup)

### Configure Interpreter[¶](#configure-interpreter)

1. Go to **File > Settings > Project > Python Interpreter**
2. Add the Unreal Engine Python interpreter:
   - UE4: `UE4/Engine/Binaries/ThirdParty/Python3/Win64/python.exe`
   - UE5: `UE5/Engine/Binaries/ThirdParty/Python3/Win64/python.exe`

### Install Stub Files[¶](#install-stub-files)

TAPython provides stub files for autocomplete. Download from the TAPython repository.

## VS Code Setup[¶](#vs-code-setup)

### Configure Python Path[¶](#configure-python-path)

1. Install Python extension
2. Set Python path to UE Python
3. Add stub files to Python path

## Tips[¶](#tips)

- Restart IDE after configuration
- Keep stub files updated
- Use type hints where possible

## Troubleshooting[¶](#troubleshooting)

- Autocomplete not working? Check interpreter settings
- Missing APIs? Update stub files

 [Previous](need_more_python_apis.html) [Next](file_structure_of_tapython.html)
