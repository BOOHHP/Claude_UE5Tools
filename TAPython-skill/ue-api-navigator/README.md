# UE Python API Navigator

[中文版](README_CN.md) | English

A Copilot Skill that provides **precise, version-accurate** Unreal Engine Python API signatures to AI — eliminating API hallucination by replacing guesswork with verified method signatures extracted from your project's PythonStub.

## Problem

AI models frequently hallucinate UE Python API calls: wrong method names, incorrect parameters, or APIs that don't exist in the user's engine version. A 37MB `unreal.py` stub file is too large to feed into any LLM context window.

## Solution

Split the monolithic stub into **15 domain-specific modules** that AI can load on demand — only pulling in the exact API signatures needed for the current task.

**Coverage**: 7,629 classes, 44,235 methods across 15 domains.

## How It Works

```
User request → AI analyzes task domain → Loads relevant module(s) → Writes code with exact signatures
```

1. **Route** — SKILL.md contains a routing table mapping task types to module files
2. **Load** — AI reads only the relevant `modules/<domain>.md` (typically 26KB–438KB instead of 37MB)
3. **Implement** — Code is written using verified signatures, not training-data guesses

## Module Map

| Module | Domain | Classes | Methods |
|--------|--------|--------:|--------:|
| `asset_management.md` | Asset CRUD, factories, content browser | 92 | 789 |
| `actor_level.md` | Actors, levels, worlds, transforms | 607 | 3,624 |
| `rendering.md` | Materials, textures, meshes, Nanite, lighting | 510 | 3,680 |
| `animation.md` | Skeletons, animations, bones, montages | 532 | 2,631 |
| `blueprint.md` | Blueprint graphs, nodes, K2Node | 293 | 1,912 |
| `ui_chameleon.md` | TAPython UI, Slate widgets, toolbars | 136 | 1,125 |
| `geometry_procedural.md` | PCG, splines, landscape, foliage, water | 557 | 3,636 |
| `input_camera.md` | Input, camera, player, controllers | 318 | 2,734 |
| `editor_tools.md` | Editor utilities, settings, dev tools | 244 | 1,909 |
| `audio.md` | Audio, MetaSound, Quartz, synth | 178 | 1,304 |
| `sequencer_movie.md` | Sequencer, MovieScene, LevelSequence | 155 | 1,043 |
| `physics_collision.md` | Physics, collision, Chaos, rigid body | 165 | 727 |
| `ai_navigation.md` | AI, behavior tree, navigation, Mass | 79 | 249 |
| `data_table.md` | DataTables, curve tables, structs | 16 | 111 |
| `core_misc.md` | Module-level functions, PythonBPLib, misc | 3,747 | 18,761 |

## Directory Structure

```
ue-api-navigator/
├── SKILL.md                    # Skill definition: routing table + protocols
├── README.md                   # This file
├── README_CN.md                # Chinese version
├── modules/                    # 15 domain-specific API reference files
│   ├── asset_management.md
│   ├── actor_level.md
│   ├── rendering.md
│   ├── animation.md
│   ├── blueprint.md
│   ├── ui_chameleon.md
│   ├── geometry_procedural.md
│   ├── input_camera.md
│   ├── editor_tools.md
│   ├── audio.md
│   ├── sequencer_movie.md
│   ├── physics_collision.md
│   ├── ai_navigation.md
│   ├── data_table.md
│   ├── core_misc.md
│   └── _stats.json             # Module generation statistics
└── tools/
    └── generate_api_skills.py  # Script to regenerate modules from PythonStub
```

## Regenerating Modules

When your UE engine version changes or plugins are added/removed:

```bash
python tools/generate_api_skills.py "/path/to/YourProject/Intermediate/PythonStub/unreal.py"
```

This re-scans the stub and regenerates all domain modules with updated signatures.

## Integration with tapython-generator

This skill works alongside [tapython-generator](../tapython-generator/):

| Skill | Responsibility |
|-------|---------------|
| **tapython-generator** | MVC architecture: MenuConfig.json + UI.json + Logic.py |
| **ue-api-navigator** | Precise API signatures for the `unreal.xxx` calls inside Logic.py |

## Key Design Principles

- **"Ask First, Then Code"** — AI loads verified signatures before writing engine interaction code
- **Progressive Loading** — Only the relevant domain is loaded, keeping token usage minimal
- **hasattr Fallback** — When an API isn't in the modules, defensive `hasattr()` detection is used
- **Probe Scripts** — For truly unknown APIs, a lightweight introspection script is generated for the user to run in TAPython REPL
