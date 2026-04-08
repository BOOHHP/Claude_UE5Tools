# TA Workspace Guide (TAPython Plugin Project)

[中文版](README_CN.md) | English

This workspace is used to develop and maintain **Unreal Engine 5 + TAPython** editor tooling, including:

- `TAPython/`: plugin configs, Python tool scripts, and UI menu definitions
- `TAPython-skill/`: Copilot skill set for TAPython tool generation and API guidance
- `TAPython_UE5_Plugin.zip`: plugin distribution package for deployment

## 1. Workspace Layout

```text
TA/
├── TAPython/
│   ├── Config/
│   │   └── config.ini
│   ├── Python/
│   │   ├── BatchRenameTool/
│   │   ├── SceneSelectTool/
│   │   └── ...
│   └── UI/
│       └── MenuConfig.json
├── TAPython-skill/
│   ├── tapython-generator/
│   └── ue-api-navigator/
└── TAPython_UE5_Plugin.zip
```

## 2. Deploying the TAPython Plugin

Use the ZIP package:

1. Extract `TAPython_UE5_Plugin.zip`.
2. Copy the extracted `TAPython` folder to your target project plugin path.
3. Enable plugin(s) and restart UE5.

## 3. Core Configuration

Key file: `TAPython/Config/config.ini`

Current workspace essentials:

```ini
[Settings]
PythonContentFolder=TA/TAPython/Python
MenuConfigFilePath=TA/TAPython/UI/MenuConfig.json
```

Meaning:

- `PythonContentFolder`: root folder for Python tool scripts.
- `MenuConfigFilePath`: main menu configuration entry for tool registration.

Recommendations:

- When migrating to another project, verify these two paths first.
- If tools are not visible, validate `MenuConfig.json` syntax before debugging code.

### Alternative Setup (Configure Python Additional Paths in Project Settings)

After plugin deployment, you can also configure the script search path from UE Project Settings:

1. Open your UE project and go to `Project Settings -> Plugins -> Python`.
2. In `Additional Paths`, add an entry pointing to `TA/TAPython/Python`.
3. Restart the UE editor.
4. After restart, open Chameleon Sketch from the TAPython menu. If it shows `Python Path Ready.`, the path configuration is valid.

## 4. How Tools Are Loaded

- Menu registration is controlled by `TAPython/UI/MenuConfig.json`.
- `OnToolBarChameleon.items` is the main entry list for tool launchers (for example Batch Rename and Scene Selection Tool).
- A typical tool includes:
  - one UI JSON layout
  - one Python controller
  - optional `__init__.py` for module imports

Example:

- `TAPython/Python/SceneSelectTool/SceneSelectTool.json`
- `TAPython/Python/SceneSelectTool/SceneSelectTool.py`

## 5. Minimum Steps to Add a New Tool

1. Create a new folder under `TAPython/Python/<ToolName>/` with:
   - `<ToolName>.json`
   - `<ToolName>.py`
   - `__init__.py`
2. Add a menu item in `TAPython/UI/MenuConfig.json` under `OnToolBarChameleon.items` with:
   - `name`
   - `tooltip`
   - `ChameleonTools`
3. Reload tool(s) in UE or restart the editor for validation.

## 6. Working with TAPython-skill

`TAPython-skill/` supports AI-assisted development:

- `tapython-generator`: generates MenuConfig/UI/Controller scaffolding from requirements
- `ue-api-navigator`: provides verified UE Python API signatures from PythonStub modules

Recommended workflow:

1. Generate scaffold with `tapython-generator`.
2. Validate `unreal.xxx` signatures with `ue-api-navigator`.
3. Integrate outputs into `TAPython/Python` and `TAPython/UI/MenuConfig.json`.

## 7. Troubleshooting

### Menu item appears but tool errors on click

- Ensure `unreal` API calls in controller are wrapped with error handling.
- Verify event bindings in UI JSON point to valid controller instance methods.

### Current-level APIs fail in some environments

- Use layered fallback logic (for example `EditorLevelLibrary.get_current_level()` first, then fallback).
- Avoid relying on a single `World` property path.

### Tool purpose is unclear in menu

- Add concise `tooltip` text for each tool in `MenuConfig.json`.

## 8. Version Control Practices

After tool changes, commit related files together:

- `TAPython/Python/...`
- `TAPython/UI/MenuConfig.json`
- documentation updates when needed

Prefer one commit containing feature logic + menu config + docs for easier traceability.

## 9. TAPython Releases for Other UE5 Versions

If you need TAPython plugin packages for other UE5 versions, visit:

- https://github.com/cgerchenhp/UE_TAPython_Plugin_Release/releases
