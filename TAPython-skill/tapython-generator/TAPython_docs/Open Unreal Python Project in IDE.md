## Open Unreal Python Project in IDE[¶](#open-unreal-python-project-in-ide)

This guide explains how to set up and open your Python project in an IDE for TAPython development.

## Recommended IDE[¶](#recommended-ide)

The recommended IDE for TAPython development is **PyCharm** (Community or Professional).

## Setting Up PyCharm[¶](#setting-up-pycharm)

### 1. Install PyCharm[¶](#1-install-pycharm)

Download and install PyCharm from JetBrains:

- [PyCharm Community](https://www.jetbrains.com/pycharm/download/) (free)
- [PyCharm Professional](https://www.jetbrains.com/pycharm/download/) (paid, recommended)

### 2. Configure Python Interpreter[¶](#2-configure-python-interpreter)

To get autocomplete for Unreal Engine Python APIs:

1. Open PyCharm and go to **File > Settings > Project > Python Interpreter**
2. Add a new interpreter pointing to the Python bundled with Unreal Engine
3. The UE Python executable is located in:
   - UE4: `UE4_Version/Engine/Binaries/ThirdParty/Python3/Win64/python.exe`
   - UE5: `UE5_Version/Engine/Binaries/ThirdParty/Python3/Win64/python.exe`

### 3. Setup Source Folders[¶](#3-setup-source-folders)

Add your TAPython project folder as a source root:

1. Right-click your project folder in PyCharm
2. Select **Mark Directory as > Sources Root**

## Auto-Complete for TAPython[¶](#auto-complete-for-tapython)

For autocomplete to work with TAPython APIs:

1. Ensure the UE Python interpreter is configured
2. The TAPython plugin provides stub files for autocomplete
3. Restart PyCharm after configuring

## Debugging[¶](#debugging)

See also: [How to Debug Python in UE](https://www.tacolor.xyz/tapython/how_to_debug_python_in_ue.html)

## Tips[¶](#tips)

- Use virtual environments for project isolation
- Keep your Python version matching UE's Python version
- Configure PyCharm to recognize UE Python stubs

 [Previous](how_to_install_tapython.html) [Next](execute_python_command_in_unreal_engine.html)
