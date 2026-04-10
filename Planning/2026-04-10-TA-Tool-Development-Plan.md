# TA Tool Development Plan (2026-04-10)

English | [中文版](2026-04-10-TA-Tool-Development-Plan_CN.md)

## Objective

Reorganize your 11 candidate scripts by production scenarios, then merge the image-derived tool pool into one executable backlog with clear selection decisions and performance optimization direction.

## Classification and Selection Overview

- Scene production acceleration (high-frequency level operations): 01, 02, 03, 05, 06, 07, 11
- Asset governance and standards (high-frequency content library governance): 04, 08, 09
- Data export and audit (low-cost mandatory utilities): 10

Selection result:
- P0 (immediate): 03, 04, 05, 09, 11
- P1 (second wave): 01, 02, 06, 08
- P2 (research/conditional): 07, 10

## Unified Development Backlog

Unified fields: Purpose, Input, Output, Scenario usage, Development logic, Performance tuning plan.

### A. Scene Production Acceleration

#### P0-1 03_ActorGroundingCheck.py
- Purpose: Detect whether selected Actors are floating and automatically move them up/down to ground using raycast results (supports StaticMeshActor and Blueprint Actor).
- Input: selected Actors in the level.
- Output: corrected Actor positions, console statistics, and popup summary.
- Scenario usage: post-layout bulk correction, fast cleanup after level merge, outsource delivery QA.
- Development logic: run detection-only preview first, then apply threshold-based position correction and generate a correction list.
- Performance tuning plan:
	- Use frame-sliced processing (N Actors per frame) to avoid editor stalls.
	- Make raycast channel configurable (WorldStatic/custom) to reduce invalid hits.
	- Add incremental mode: process only objects whose Z offset exceeds a threshold.

#### P0-2 05_BatchToggleReceivesDecals.py
- Purpose: Batch enable/disable Receives Decals, supporting both level instances and source Blueprint class updates.
- Input: selected Actors in level, or selected Blueprints in Content Browser.
- Output: unified decal receiving state across components, Blueprint auto-compile and save.
- Scenario usage: art style switching, quickly disabling decals before performance tests, phase-wide standardization.
- Development logic: split into instance mode and blueprint-source mode, estimate impact first, then write at component level with failure aggregation.
- Performance tuning plan:
	- Preview impacted object count before apply.
	- Process Blueprint edits through a batch queue; merge compile/save operations.
	- Skip unchanged components to reduce dirty flags and redundant saves.

#### P0-3 11_DecalToPlaneMesh.py
- Purpose: Batch convert selected DecalActors to Plane static meshes, preserving decal materials and correcting size/orientation.
- Input: selected DecalActors in the level.
- Output: new Plane Actors (named OriginalName_Plane).
- Scenario usage: mobile optimization, effect baking, converting decals into controllable geometry.
- Development logic: sample Decal parameters and build a conversion plan first, then generate Plane Actors and copy key material/transform data.
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
- Development logic: produce a violation report first, then apply configurable fixes and record before/after texture size parameters.
- Performance tuning plan:
	- Split into scan and apply phases (report first, then write).
	- Use asset registry filtering (path/size threshold) to avoid full loading.
	- Save in batches (for example every 50 textures) to reduce blocking.

#### P0-5 09_AutoAssetOrganization.py
- Purpose: Create per-mesh subfolders by Static Mesh name and organize related materials/textures, including redirector fixup and save.
- Input: selected Static Mesh assets in Content Browser.
- Output: asset relocation, reference redirect fix, auto-save.
- Scenario usage: milestone directory cleanup, asset handoff, normalized content intake.
- Development logic: build a Move Plan first (target path, conflicts, dependencies), confirm, then execute and run redirector fixup once at the end.
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
- Development logic: create assets through a Blueprint template factory, apply naming rules and component binding, then compile/save in one batch.
- Performance tuning plan: reuse a Blueprint template + unified save at end of batch.

#### P1-2 02_BlueprintSplitToStaticMeshes.py
- Purpose: Split selected Blueprint Actors into multiple StaticMeshActors while preserving hierarchy, materials, Tags, and folder structure.
- Input: selected Blueprint Actors in the level.
- Output: new StaticMeshActors; original Blueprint hidden.
- Scenario usage: convert blueprints back to editable scene elements, de-blueprinting before performance analysis.
- Development logic: traverse Blueprint components and snapshot first, then spawn StaticMeshActors from snapshot and restore hierarchy/tags.
- Performance tuning plan: component snapshot + deferred spawn to avoid one-shot spawn hitches.

#### P1-3 06_FoliageAndSMBidirectionalConvert.py
- Purpose: Bidirectional conversion between foliage and static mesh actors (non-merge version).
- Input: selected InstancedFoliageActor or StaticMeshActor in level.
- Output: converted Actors or foliage instances.
- Scenario usage: foliage editing rollback, local manual refinement then write-back to instances.
- Development logic: split into extract and write-back flows while sharing one instance data model and mapping record.
- Performance tuning plan: bucket by mesh type to reduce instance write-back cost.

#### P1-4 08_MergeDuplicateTextures.py
- Purpose: Detect duplicate Texture2D under /Game by name, keep the best copy, and run Consolidate.
- Input: textures under /Game (no manual selection required).
- Output: duplicate textures removed, references redirected to retained texture.
- Scenario usage: legacy project slimming, package size governance, post-merge deduplication.
- Development logic: cluster by name first, score the best retained copy, then run Consolidate and export non-auto-fix candidates.
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
- Development logic: add a merge stage after the extract flow in 06, and gate generation by merge gain evaluation.
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
- Development logic: collect Actor names and tag sequences in a stable order, then export to txt or csv.
- Performance tuning plan: prioritize CSV/UTF-8 path configuration and overwrite confirmation.
- Selection note: low implementation cost but limited strategic impact; can be a filler task.

## Image Tool Pool Merge (kept and unified)

Note: The 20 items from the image are merged into this plan. For overlapping capabilities, we use one shared backend capability with multiple business-facing entries, instead of duplicated implementations.

### E. Materials and Material Instance Workflows (core demand)

#### E-01 Batch Replace Parent Material for MI
- Purpose: batch replace Parent Material of MI with a target master material.
- Input: Material Instances in selected folders/assets.
- Output: updated MI assets and execution report.
- Scenario usage: material system upgrades, outsourced asset unification, style transition.
- Development logic: scan candidates and preview diffs first, then apply replacement and record old parent for rollback.
- Performance tuning plan: asset-registry filtering + chunked writes + batch save.

#### E-02 Batch Edit MI Parameters
- Purpose: batch edit MI parameters (scalar/vector/texture toggles and similar).
- Input: parameter rules and target MI set.
- Output: updated MI parameters and statistics.
- Scenario usage: rapid style iteration, version-wide parameter alignment, platform-specific tuning.
- Development logic: parameter-template driven; validate parameter existence first, then apply and export failures.
- Performance tuning plan: write only changed parameters and skip unchanged assets.

#### E-03 Repair MI with Missing Parent
- Purpose: repair MI with missing Parent links and rebuild valid associations.
- Input: invalid MI set and naming/path rules.
- Output: repair report (success/failed/manual review).
- Scenario usage: project migration and post-refactor repair.
- Development logic: candidate matching by rules; unmatched cases go to manual confirmation queue.
- Performance tuning plan: cache parent-material candidate index to avoid repeated full-library search.

#### E-04 Batch Create Material Instances
- Purpose: create MI in batches from master materials with optional texture-name-based naming.
- Input: target master material, naming rules, output folder.
- Output: newly created MI assets.
- Scenario usage: quickly completing MI layer after batch imports.
- Development logic: template-based creation + naming conflict checks + optional parameter initialization.
- Performance tuning plan: one transactional creation pass and single final save.

#### E-05 Batch Clear MI Parameter Overrides
- Purpose: reset manually overridden MI parameters back to inherited state.
- Input: target MI set and parameter filter rules.
- Output: restored MI and change report.
- Scenario usage: rollback tuning experiments and fix accidental edits.
- Development logic: preview override deltas first, then clear and keep change snapshots.
- Performance tuning plan: whitelist/blacklist parameter filtering to reduce unnecessary traversal.

### F. Mesh and Static Model Batch Processing

#### F-06 Batch Assign Materials to StaticMesh
- Purpose: assign materials to StaticMesh slots by name/keyword mapping rules.
- Input: StaticMesh set, matching rules, target material mapping.
- Output: updated mesh material slots.
- Scenario usage: fast material hookup after bulk import.
- Development logic: preview matching result first, then write updates and export unmatched items.
- Performance tuning plan: precompiled rule cache to reduce repeated matching costs.

#### F-07 Batch Generate/Rebuild Collision
- Purpose: clear old collision and rebuild using configured rules (including UCX/NDOP styles).
- Input: StaticMesh set and collision rule config.
- Output: rebuilt collision data and exception report.
- Scenario usage: outsourced mesh acceptance and collision standardization before optimization.
- Development logic: process by mesh complexity tiers and route abnormal meshes to manual review.
- Performance tuning plan: chunked execution plus separate queue for high-complexity meshes.

#### F-08 Batch Configure LOD and Reduction Ratio
- Purpose: batch set LOD levels, reduction ratio, and distance thresholds.
- Input: StaticMesh set and LOD strategy templates.
- Output: updated LOD configurations.
- Scenario usage: multi-platform adaptation, package-size optimization, render-budget control.
- Development logic: apply templates by asset category with rollback support.
- Performance tuning plan: template-based bulk apply and skip assets already compliant.

#### F-09 Batch Generate Lightmap UV
- Purpose: batch generate/fix Lightmap UV with unified resolution policy.
- Input: StaticMesh set and UV rules.
- Output: meshes with valid Lightmap UV.
- Scenario usage: pre-bake checks and lighting stability improvements.
- Development logic: verify UV validity first, then generate; export failed items for review.
- Performance tuning plan: process by polygon count tiers to avoid full heavy recompute.

#### F-10 Batch Replace Scene Static Meshes
- Purpose: batch replace StaticMeshActor in level by name/tag mapping rules.
- Input: selected actors or full-level scan scope plus replacement mapping.
- Output: replaced scene actors preserving location/rotation/scale.
- Scenario usage: art-version replacement and performance-model switching.
- Development logic: build replacement mapping preview first, then apply and record original mapping for rollback.
- Performance tuning plan: deferred scene refresh during replacement and one-time rebuild at end.

### G. Level and Scene Object Automation

#### G-11 Batch Edit Render Properties
- Purpose: batch set shadow/reflection/visibility/render-distance properties.
- Input: selected actors or rule-filtered actor set.
- Output: normalized actor render properties.
- Scenario usage: platform optimization, far-view tuning, rendering standardization.
- Development logic: property templates with diff preview and one-click rollback.
- Performance tuning plan: write only changed fields.

#### G-12 Batch Reset/Zero Object Transform
- Purpose: batch reset location/rotation or normalize scale.
- Input: selected actors in level.
- Output: actors with reset transforms.
- Scenario usage: level cleanup and standardized external-asset intake.
- Development logic: mode-based operations (rotation only/scale only/full reset) with original transform snapshot.
- Performance tuning plan: apply in chunks and finalize with one transaction commit.

#### G-13 Batch Add Tags/Layers/Groups
- Purpose: add tags and assign layers/groups to actors by rules.
- Input: target actor set and tag/layer rules.
- Output: updated actor organization structure.
- Scenario usage: level organization and future automation filtering.
- Development logic: validate conflicts and duplicates first, then write in bulk.
- Performance tuning plan: de-duplicated writes.

#### G-14 Invalid Actor Cleanup
- Purpose: cleanup empty nodes, actors without mesh, and invalid component references.
- Input: level scan scope.
- Output: cleanup report and action results.
- Scenario usage: milestone-level health check and pre-regression cleanup.
- Development logic: graded strategies (mark only/soft delete/hard delete) for safe rollout.
- Performance tuning plan: build issue index first, then cleanup to avoid repeated scans.

#### G-15 Batch Align/Array/Distribute Actors
- Purpose: align, evenly array, and region-distribute selected actors.
- Input: selected actors, axis choices, and distribution parameters.
- Output: arranged actor set.
- Scenario usage: faster scene dressing and road/ground placement workflows.
- Development logic: parameterized math rules (axis, step, count, bounds).
- Performance tuning plan: precompute target transforms and apply in batch.

### H. Asset Governance and Project Standards

#### H-16 Batch Asset Rename
- Purpose: unify asset naming by prefix/suffix/index/type rules.
- Input: selected assets and naming template.
- Output: rename results and conflict-handling report.
- Scenario usage: naming normalization and pre-delivery cleanup.
- Development logic: reuse existing BatchRenameTool preview/apply engine with template rule layer.
- Performance tuning plan: conflict pre-resolution + plan caching + chunked renaming.

#### H-17 Batch Move/Classify Assets
- Purpose: move textures/materials/meshes/audio into standardized folders by mapping rules.
- Input: asset set and folder mapping rules.
- Output: move results, redirector fixup, save report.
- Scenario usage: project structure governance and standardized handoff.
- Development logic: share Move Plan and conflict detection with 09_AutoAssetOrganization.
- Performance tuning plan: single Fixup Redirectors pass after batch move.

#### H-18 Batch Broken Reference Checker
- Purpose: scan broken references in materials/textures/blueprints and generate reports.
- Input: folder scope or selected assets.
- Output: broken-reference list and fix suggestions.
- Scenario usage: post-merge verification and post-upgrade stability checks.
- Development logic: read-only scan and grading first, then provide semi-automatic fix entry points.
- Performance tuning plan: reference-graph cache + incremental scan.

#### H-19 PBR Material Standard Checker
- Purpose: check metallic/roughness/texture channel and missing-texture compliance for PBR.
- Input: material/material instance set.
- Output: compliance report and remediation suggestions.
- Scenario usage: pre-release quality gate and outsource acceptance.
- Development logic: rules-engine driven and project-configurable thresholds.
- Performance tuning plan: short-circuit severe-rule failures to cut deep-check time.

#### H-20 Batch Light Baking Preprocess
- Purpose: batch configure lighting-related parameters to reduce bake preparation cost.
- Input: level/asset scope and preprocess templates.
- Output: standardized parameter results and preprocess report.
- Scenario usage: large-scale pre-bake standardization.
- Development logic: platform templates (PC/console/mobile) with one-click rollback.
- Performance tuning plan: minimum-change writes only for out-of-template fields.

## Unified Development Logic Backbone (recommended)

- Shared Core 1: preview-apply two-stage workflow (plan first, write second).
- Shared Core 2: ChangeSnapshot rollback snapshots (paths, properties, parameters).
- Shared Core 3: RuleEngine-driven rules (naming, filtering, mapping, thresholds).
- Shared Core 4: TaskQueue chunked execution (progress, cancel, retry).
- Shared Core 5: Reporter unified output (JSON/CSV with traceable failures).

## Capability Consolidation and No-Duplicate Execution Roadmap

### 1) Overlap consolidation (primary capability -> child tools)

- Naming governance primary capability
	- Primary tool: H-16 Batch Asset Rename
	- Child entries: existing BatchRenameTool and naming-related scenarios
	- Consolidation strategy: one naming template system, conflict pre-resolution, preview cache, and shared execution engine.

- Asset migration primary capability
	- Primary tool: P0-5 09_AutoAssetOrganization.py
	- Child entries: H-17 Batch Move/Classify Assets
	- Consolidation strategy: shared Move Plan, dependency analysis, and one-pass Fixup Redirectors closure.

- Reference repair primary capability
	- Primary tool: H-18 Batch Broken Reference Checker
	- Child entries: P1-4 08_MergeDuplicateTextures.py, E-03 Repair MI with Missing Parent
	- Consolidation strategy: one reference-graph scanner and one unified failure report format.

- Foliage conversion primary capability
	- Primary tool: P1-3 06_FoliageAndSMBidirectionalConvert.py
	- Child entries: P2-1 07_FoliageAndSMBidirectionalConvert_Merge.py
	- Consolidation strategy: stabilize bidirectional conversion first, then attach merge as an optional post-process module.

- Material instance governance primary capability
	- Primary tools: E-01/E-02/E-03/E-04/E-05
	- Child entries: project-specific rule panels
	- Consolidation strategy: one MI scanner, parameter accessor, parent-matching logic, and rollback snapshot pipeline.

- Scene batch-processing primary capability
	- Primary tools: P0-1, P0-2, P0-3, G-11, G-12, G-13, G-14, G-15
	- Child entries: level QA, performance optimization, placement automation
	- Consolidation strategy: one Actor filter, transform writer, frame-sliced scheduler, and batch report pipeline.

### 2) No-duplicate execution order (core first, tools second)

- Phase A: build shared core once
	- Preview-Apply engine
	- ChangeSnapshot rollback
	- RuleEngine config layer
	- Reporter output layer

- Phase B: wire high-reuse primary capabilities first
	- Naming governance (covers H-16 and BatchRenameTool)
	- Asset migration (covers P0-5 and H-17)
	- Reference repair (covers H-18/E-03/08)

- Phase C: wire scene batch capability group
	- Deliver P0-1, P0-2, P0-3 first
	- Then expand to G-11 through G-15

- Phase D: wire material and mesh capability groups
	- MI pipeline: E-01 through E-05
	- Mesh pipeline: F-06 through F-10

- Phase E: defer high-risk capabilities
	- P2-1 (foliage merge version)
	- H-20 (light baking preprocess)

### 3) Anti-duplication guardrails (execution constraints)

- Before approving any new tool, require a reuse declaration: which primary modules are reused.
- Do not duplicate scan/apply/report logic for same-category functions.
- Every new tool must integrate unified Reporter and rollback snapshots.
- Add review checklist item: verify reuse of existing primary capabilities.

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
