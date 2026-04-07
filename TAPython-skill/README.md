# TAPython Skills Collection

[中文版](README_CN.md) | English

A curated collection of [Copilot Skills](https://docs.github.com/en/copilot) for **Unreal Engine Python (TAPython)** script development.

## What Is This?

This repository hosts a set of AI-powered skills that help developers rapidly build editor tools for Unreal Engine 5.5+ using [TAPython](https://github.com/cgerchenhp/TAPython). Each skill encapsulates domain knowledge, best practices, and code-generation capabilities for specific aspects of UE Python tooling.

## Available Skills

| Skill | Role | Triggers |
|-------|------|----------|
| [tapython-generator](tapython-generator/) | Full-stack TAPython architect — generates `MenuConfig.json`, `UI.json`, and `Controller.py` from natural language with strict MVC architecture | `TAPython`, `Chameleon tool`, `Slate UI`, `UE5 tool` |
| [ue-api-navigator](ue-api-navigator/) | UE Python API navigator — splits the 37MB PythonStub into 15 domain modules (7,629 classes, 44,235 methods) for on-demand AI loading, eliminating API hallucination | `unreal API`, `UE native API`, `unreal.xxx`, `PythonStub` |

### How They Work Together

```
User: "Build a batch asset renaming tool"

  tapython-generator                 ue-api-navigator
  ─────────────────                  ────────────────────
  1. MenuConfig.json (menu entry)    3. Load modules/asset_management.md
  2. UI.json (Chameleon layout)      4. Provide exact unreal.EditorAssetLibrary signatures
  5. Controller.py (logic using verified signatures from step 4)
```

- **tapython-generator** owns the MVC scaffold (menu + UI + controller)
- **ue-api-navigator** provides precise `unreal.xxx` API signatures for the controller logic
- Neither guesses API parameters — signatures are extracted from your project's real PythonStub

## Quick Start

### 1. Add this repository as a skill source in GitHub Copilot

### 2. Trigger a skill

- **To build a TAPython tool** — mention `TAPython`, `Chameleon tool`, `Slate UI`, or `UE5 tool`
- **To look up UE native API** — mention `unreal API`, `unreal.xxx`, or `PythonStub`

### 3. (Optional) Regenerate API modules for your UE version

The `modules/` shipped in this repo are generated from UE 5.5. If you use a different version:

```bash
python ue-api-navigator/tools/generate_api_skills.py \
  "/path/to/YourProject/Intermediate/PythonStub/unreal.py"
```

This re-scans the stub and outputs updated domain modules into `ue-api-navigator/modules/`.

## Repository Structure

```
TAPython-skill/
├── README.md                  # This file
├── README_CN.md               # Chinese version
│
├── tapython-generator/        # Skill 1: TAPython full-stack code generation
│   ├── SKILL.md               # Skill definition & MVC instructions
│   ├── TAPython_docs/         # Official TAPython documentation references
│   ├── templates/             # Code templates (MenuConfig, UI, Controller)
│   ├── widgets/               # Slate widget catalog & usage examples
│   ├── patterns/              # Common implementation patterns
│   ├── pitfalls/              # Common pitfalls & solutions
│   ├── examples/              # Complete tool examples
│   └── guides/                # Troubleshooting, FAQ, performance tips
│
├── ue-api-navigator/          # Skill 2: UE Python API navigation
│   ├── SKILL.md               # Routing table & "Ask First" protocol
│   ├── README.md              # Detailed English documentation
│   ├── README_CN.md           # Detailed Chinese documentation
│   ├── modules/               # 15 domain-specific API signature files
│   │   ├── asset_management.md      92 classes    789 methods
│   │   ├── actor_level.md          607 classes  3,624 methods
│   │   ├── rendering.md            510 classes  3,680 methods
│   │   ├── animation.md            532 classes  2,631 methods
│   │   ├── blueprint.md            293 classes  1,912 methods
│   │   ├── ui_chameleon.md         136 classes  1,125 methods
│   │   ├── geometry_procedural.md  557 classes  3,636 methods
│   │   ├── input_camera.md         318 classes  2,734 methods
│   │   ├── editor_tools.md         244 classes  1,909 methods
│   │   ├── audio.md                178 classes  1,304 methods
│   │   ├── sequencer_movie.md      155 classes  1,043 methods
│   │   ├── physics_collision.md    165 classes    727 methods
│   │   ├── ai_navigation.md         79 classes    249 methods
│   │   ├── data_table.md            16 classes    111 methods
│   │   └── core_misc.md          3,747 classes 18,761 methods
│   └── tools/
│       └── generate_api_skills.py   # Stub → modules splitting script
│
└── .gitignore
```

## Contributing

Contributions are welcome! You can:

- **Add a new skill** — create a new subdirectory with a `SKILL.md` following the existing format.
- **Improve documentation** — expand the TAPython docs, add more examples, or refine templates.
- **Improve routing rules** — edit `ROUTING_RULES` in `generate_api_skills.py` and re-generate modules for better domain coverage.
- **Report issues** — open an issue if a generated tool has problems or if you'd like a new feature.

## License

This project is provided as-is for educational and development purposes.
