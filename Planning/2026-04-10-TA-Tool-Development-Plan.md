# TA Tool Development Plan (2026-04-10)

English | [中文版](2026-04-10-TA-Tool-Development-Plan_CN.md)

## Objective

Reorganize the 11 candidate scripts you provided by production scenarios, forming an executable development backlog with clear keep/drop decisions and performance optimization direction.

## Classification and Selection Overview

- Scene production acceleration (high-frequency level operations): 01, 02, 03, 05, 06, 07, 11
- Asset governance and standards (high-frequency content library governance): 04, 08, 09
- Data export and audit (low-cost mandatory utilities): 10

Selection result:
- P0 (immediate): 03, 04, 05, 09, 11
- P1 (second wave): 01, 02, 06, 08
- P2 (research/conditional): 07, 10

## Development Backlog (same structure)

### A. Scene Production Acceleration

#### P0-1 03_ActorGroundingCheck.py
- Purpose: Detect whether selected Actors are floating and automatically move them up/down to ground using raycast results (supports StaticMeshActor and Blueprint Actor).
- Input: selected Actors in the level.
- Output: corrected Actor positions, console statistics, and popup summary.
- Scenario usage: post-layout bulk correction, fast cleanup after level merge, outsource delivery QA.
- Performance tuning plan:
	- Use frame-sliced processing (N Actors per frame) to avoid editor stalls.
	- Make raycast channel configurable (WorldStatic/custom) to reduce invalid hits.
	- Add incremental mode: process only objects whose Z offset exceeds a threshold.

#### P0-2 05_BatchToggleReceivesDecals.py
- Purpose: Batch enable/disable Receives Decals, supporting both level instances and source Blueprint class updates.
- Input: selected Actors in level, or selected Blueprints in Content Browser.
- Output: unified decal receiving state across components, Blueprint auto-compile and save.
- Scenario usage: art style switching, quickly disabling decals before performance tests, phase-wide standardization.
- Performance tuning plan:
	- Preview impacted object count before apply.
	- Process Blueprint edits through a batch queue; merge compile/save operations.
	- Skip unchanged components to reduce dirty flags and redundant saves.

#### P0-3 11_DecalToPlaneMesh.py
- Purpose: Batch convert selected DecalActors to Plane static meshes, preserving decal materials and correcting size/orientation.
- Input: selected DecalActors in the level.
- Output: new Plane Actors (named OriginalName_Plane).
- Scenario usage: mobile optimization, effect baking, converting decals into controllable geometry.
- Performance tuning plan:
	- Use shared material instance cache to avoid duplicate MI creation.
	- Disable realtime refresh during batch conversion and redraw once at end.
	- Record original DecalActor mapping for rollback.

### B. Asset Governance and Standards

#### P0-4 04_FixNonPOTTextures.py
- Purpose: Scan Texture2D under /Game, detect and fix non-power-of-two textures with safety filters.
- Input: textures under /Game (no manual selection required).
- Output: updated max_texture_size and saved assets.
- Scenario usage: pre-release checks, platform adaptation (mobile/console), outsourced asset intake validation.
- Performance tuning plan:
	- Split into scan and apply phases (report first, then write).
	- Use asset registry filtering (path/size threshold) to avoid full loading.
	- Save in batches (for example every 50 textures) to reduce blocking.

#### P0-5 09_AutoAssetOrganization.py
- Purpose: Create per-mesh subfolders by Static Mesh name and organize related materials/textures, including redirector fixup and save.
- Input: selected Static Mesh assets in Content Browser.
- Output: asset relocation, reference redirect fix, auto-save.
- Scenario usage: milestone directory cleanup, asset handoff, normalized content intake.
- Performance tuning plan:
	- Build and preview a Move Plan first (conflicts and naming collisions).
	- Cache dependency traversal to avoid repeated graph walks.
	- Execute Fixup Redirectors once at the end to reduce repeated scans.

### C. Second Wave (medium-high value)

#### P1-1 01_SMToBlueprintActorBatch.py
- Purpose: Batch create Blueprint Actors from selected Static Meshes (BP_ prefix) and auto-attach same-name StaticMeshComponent.
- Input: selected Static Mesh assets in Content Browser.
- Output: newly created Blueprint assets in the same directory.
- Scenario usage: rapid blueprinting for interactive assets, standardization for level reuse.
- Performance tuning plan: reuse a Blueprint template + unified save at end of batch.

#### P1-2 02_BlueprintSplitToStaticMeshes.py
- Purpose: Split selected Blueprint Actors into multiple StaticMeshActors while preserving hierarchy, materials, Tags, and folder structure.
- Input: selected Blueprint Actors in the level.
- Output: new StaticMeshActors; original Blueprint hidden.
- Scenario usage: convert blueprints back to editable scene elements, de-blueprinting before performance analysis.
- Performance tuning plan: component snapshot + deferred spawn to avoid one-shot spawn hitches.

#### P1-3 06_FoliageAndSMBidirectionalConvert.py
- Purpose: Bidirectional conversion between foliage and static mesh actors (non-merge version).
- Input: selected InstancedFoliageActor or StaticMeshActor in level.
- Output: converted Actors or foliage instances.
- Scenario usage: foliage editing rollback, local manual refinement then write-back to instances.
- Performance tuning plan: bucket by mesh type to reduce instance write-back cost.

#### P1-4 08_MergeDuplicateTextures.py
- Purpose: Detect duplicate Texture2D under /Game by name, keep the best copy, and run Consolidate.
- Input: textures under /Game (no manual selection required).
- Output: duplicate textures removed, references redirected to retained texture.
- Scenario usage: legacy project slimming, package size governance, post-merge deduplication.
- Performance tuning plan:
	- Two-stage matching: name grouping, then compare size/reference count.
	- Run by directory chunks in large projects to avoid heavy one-shot consolidate.
	- Output a non-auto-merge candidate list for manual confirmation.

### D. Research and Conditional Rollout

#### P2-1 07_FoliageAndSMBidirectionalConvert_Merge.py
- Purpose: Same as 06, but supports same-type mesh merge during foliage extraction and generates new assets.
- Input: selected foliage or static mesh actors in level.
- Output: conversion results plus merged assets (default /Game/Foliage_Merged).
- Scenario usage: large-scene draw call reduction, far-view batch optimization.
- Performance tuning plan:
	- Make merge tasks asynchronous with progress and cancel support.
	- Add merge thresholds (min instance count, max vertex count).
	- Enforce preview of merge gains (draw call delta) before apply.
- Selection note: higher risk than 06; roll out after base bidirectional conversion is stable.

#### P2-2 10_ActorTagExport.py
- Purpose: Export selected Actor outliner names and all tags to a text file.
- Input: selected Actors in level.
- Output: UE_Actor_Tag_Export.txt on desktop by default.
- Scenario usage: external review, design annotation sync, quick audit.
- Performance tuning plan: prioritize CSV/UTF-8 path configuration and overwrite confirmation.
- Selection note: low implementation cost but limited strategic impact; can be a filler task.

## Unified Implementation Requirements (applies to all)

- Must support preview/apply dual modes.
- Must output execution report (success, failed, skipped, duration).
- For write tools, provide rollback data at minimum (old path/old property).
- For large jobs, use chunked execution + progress feedback to avoid long editor freeze.

## Iteration Suggestion (two-week cadence)

- Sprint 1: 03, 04 (fast delivery, validate preview-apply framework)
- Sprint 2: 05, 09 (high-frequency governance tools, solidify batch framework)
- Sprint 3: 11, 01, 02 (scene production acceleration)
- Sprint 4: 06, 08 (medium-risk asset governance)
- Sprint 5: 07, 10 (research and completion)
