## Welcome To TAPython[¶](#welcome-to-tapython)

TAPython is a plugin for Unreal Engine that allows you to use Python to develop tools, UI, and automation in the Unreal Editor.

## What is TAPython?[¶](#what-is-tapython)

TAPython (TA Python) is a plugin that enables Python scripting within the Unreal Engine editor. It provides:

- Python integration with Unreal Engine's editor APIs
- A UI framework called "Chameleon" for creating editor tools
- Access to 200+ extended editor Python interfaces

## Key Features[¶](#key-features)

- **Python in UE**: Write Python code to interact with Unreal Engine
- **Chameleon Tool**: Create custom editor UI using JSON and Python
- **Extended APIs**: Access to many editor functionalities through Python

## Key Concepts[¶](#key-concepts)

**Chameleon Tool**: TAPython's core system for building editor UI. You define the interface layout in a JSON file using Slate widget descriptions, and handle all logic in a Python class. The JSON describes what the UI looks like, and Python callbacks handle user interactions. See [Chameleon Tool](Chameleon Tool.md).

**ChameleonData**: The bridge between your UI and Python code. ChameleonData lets you read and write widget values — such as text fields, checkboxes, and sliders — directly from Python. This is how your Python logic communicates with the UI layer. See [TA Python ChameleonData API](TA Python ChameleonData API.md).

**Extended Python APIs**: TAPython provides 200+ additional Python APIs for editor operations. These cover asset management, material editing, mesh processing, landscape manipulation, and more. See [Python Editor Extended API](Python Editor Extended API.md).

**MVC Pattern**: TAPython encourages separating UI (JSON) from logic (Python), following a Model-View-Controller approach. The JSON file acts as the View, your Python class acts as the Controller, and your data/state serves as the Model.

## Getting Started[¶](#getting-started)

Check out these resources to get started:

- [How to install TAPython](https://www.tacolor.xyz/tapython/how_to_install_tapython.html)
- [Open Unreal Python Project in IDE](https://www.tacolor.xyz/tapython/open_unreal_python_project_in_ide.html)
- [Execute Python Command in Unreal Engine](https://www.tacolor.xyz/tapython/execute_python_command_in_unreal_engine.html)

## Quick Start Path[¶](#quick-start-path)

Follow this recommended learning path to get productive with TAPython:

1. Install TAPython — [How to install TAPython](How to install TAPython.md)
2. Learn the file structure — [File Structure of TAPython](File Structure of TAPython.md)
3. Create your first tool — [Chameleon Tool](Chameleon Tool.md)
4. Learn UI basics — [Using Slate to Add Interface for Python Tools](Using Slate to Add Interface for Python Tools.md)
5. Explore the API — [Python Editor Extended API](Python Editor Extended API.md)
6. Debug your code — [How to Debug Python in UE](How to Debug Python in UE.md)

## Documentation[¶](#documentation)

This documentation covers:

- Installation and setup
- UI development with Chameleon
- Editor automation
- Debugging Python in UE

## What TAPython Can Do[¶](#what-tapython-can-do)

- Create custom editor windows and panels with native Slate UI
- Automate asset workflows (batch rename, import/export, validation)
- Edit materials, meshes, landscapes, physics assets programmatically
- Build custom menus and toolbars — [Add Menu Items to Unreal Editor](Add Menu Items to Unreal Editor.md)
- Create test automation — [Write Test Case](Write Test Case.md)

## What TAPython Cannot Do[¶](#what-tapython-cannot-do)

- **Runtime/game logic** — TAPython is editor-only, not for shipping with packaged games
- **Modifying C++ engine code** — it wraps existing APIs but cannot add new engine features
- **Blueprint visual scripting** — TAPython is Python-based, not a Blueprint replacement

 [Next](how_to_install_tapython.html)
