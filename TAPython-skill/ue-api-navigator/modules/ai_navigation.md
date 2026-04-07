# Unreal Python API — AI Navigation

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AIController(Controller)`

```python
unreal.AIController.actions_comp() -> PawnActionsComponent
unreal.AIController.allow_strafe(value: bool) -> None
unreal.AIController.blackboard() -> BlackboardComponent
unreal.AIController.brain_component(value: BrainComponent) -> None
unreal.AIController.claim_task_resource(resource_class: Class) -> None
unreal.AIController.clear_focus() -> None
unreal.AIController.default_navigation_filter_class(value: Class) -> None
unreal.AIController.get_ai_perception_component() -> AIPerceptionComponent
unreal.AIController.get_focal_point() -> Vector
unreal.AIController.get_focal_point_on_actor(actor: Actor) -> Vector
unreal.AIController.get_focus_actor() -> Actor
unreal.AIController.get_immediate_move_destination() -> Vector
unreal.AIController.get_move_status() -> PathFollowingStatus
unreal.AIController.get_path_following_component() -> PathFollowingComponent
unreal.AIController.has_partial_path() -> bool
unreal.AIController.move_to_actor(goal: Actor, acceptance_radius: float = -1.000000, stop_on_overlap: bool = True, use_pathfinding: bool = True, can_strafe: bool = True, filter_class: Class = None, allow_partial_path: bool = True) -> PathFollowingRequestResult
unreal.AIController.move_to_location(dest: Vector, acceptance_radius: float = -1.000000, stop_on_overlap: bool = True, use_pathfinding: bool = True, project_destination_to_navigation: bool = False, can_strafe: bool = True, filter_class: Class = None, allow_partial_path: bool = True) -> PathFollowingRequestResult
unreal.AIController.on_using_black_board(blackboard_comp: BlackboardComponent, blackboard_asset: BlackboardData) -> None
unreal.AIController.receive_move_completed(value: AIMoveCompletedSignature) -> None
unreal.AIController.run_behavior_tree(bt_asset: BehaviorTree) -> bool
unreal.AIController.set_control_rotation_from_pawn_orientation(value: bool) -> None
unreal.AIController.set_focal_point(fp: Vector) -> None
unreal.AIController.set_focus(new_focus: Actor) -> None
unreal.AIController.set_move_block_detection(enable: bool) -> None
unreal.AIController.set_path_following_component(new_pf_component: PathFollowingComponent) -> None
unreal.AIController.skip_extra_los_checks(value: bool) -> None
unreal.AIController.start_ai_logic_on_possess(value: bool) -> None
unreal.AIController.stop_ai_logic_on_unposses(value: bool) -> None
unreal.AIController.unclaim_task_resource(resource_class: Class) -> None
unreal.AIController.use_blackboard(blackboard_asset: BlackboardData) -> Optional[BlackboardComponent]
unreal.AIController.wants_player_state(value: bool) -> None
```

## `unreal.BehaviorTree(Object)`

```python
unreal.BehaviorTree.get_blackboard_asset() -> BlackboardData
```

## `unreal.BehaviorTreeComponent(BrainComponent)`

```python
unreal.BehaviorTreeComponent.add_cooldown_tag_duration(cooldown_tag: GameplayTag, cooldown_duration: float, add_to_existing_duration: bool) -> None
unreal.BehaviorTreeComponent.default_behavior_tree_asset(value: BehaviorTree) -> None
unreal.BehaviorTreeComponent.get_tag_cooldown_end_time(cooldown_tag: GameplayTag) -> float
unreal.BehaviorTreeComponent.set_dynamic_subtree(inject_tag: GameplayTag, behavior_asset: BehaviorTree) -> None
```

## `unreal.BlackboardAssetProvider(Interface)`

```python
unreal.BlackboardAssetProvider.get_blackboard_asset() -> BlackboardData
```

## `unreal.BlackboardComponent(ActorComponent)`

```python
unreal.BlackboardComponent.clear_value(key_name: Name) -> None
unreal.BlackboardComponent.get_location_from_entry(key_name: Name) -> Optional[Vector]
unreal.BlackboardComponent.get_rotation_from_entry(key_name: Name) -> Optional[Rotator]
unreal.BlackboardComponent.get_value_as_bool(key_name: Name) -> bool
unreal.BlackboardComponent.get_value_as_class(key_name: Name) -> Class
unreal.BlackboardComponent.get_value_as_enum(key_name: Name) -> int
unreal.BlackboardComponent.get_value_as_float(key_name: Name) -> float
unreal.BlackboardComponent.get_value_as_int(key_name: Name) -> int
unreal.BlackboardComponent.get_value_as_name(key_name: Name) -> Name
unreal.BlackboardComponent.get_value_as_object(key_name: Name) -> Object
unreal.BlackboardComponent.get_value_as_rotator(key_name: Name) -> Rotator
unreal.BlackboardComponent.get_value_as_string(key_name: Name) -> str
unreal.BlackboardComponent.get_value_as_vector(key_name: Name) -> Vector
unreal.BlackboardComponent.is_vector_value_set(key_name: Name) -> bool
unreal.BlackboardComponent.set_value_as_bool(key_name: Name, bool_value: bool) -> None
unreal.BlackboardComponent.set_value_as_class(key_name: Name, class_value: Class) -> None
unreal.BlackboardComponent.set_value_as_enum(key_name: Name, enum_value: int) -> None
unreal.BlackboardComponent.set_value_as_float(key_name: Name, float_value: float) -> None
unreal.BlackboardComponent.set_value_as_int(key_name: Name, int_value: int) -> None
unreal.BlackboardComponent.set_value_as_name(key_name: Name, name_value: Name) -> None
unreal.BlackboardComponent.set_value_as_object(key_name: Name, object_value: Object) -> None
unreal.BlackboardComponent.set_value_as_rotator(key_name: Name, vector_value: Rotator) -> None
unreal.BlackboardComponent.set_value_as_string(key_name: Name, string_value: str) -> None
unreal.BlackboardComponent.set_value_as_vector(key_name: Name, vector_value: Vector) -> None
```

## `unreal.BlackboardEntry(StructBase)`

```python
unreal.BlackboardEntry.__init__() -> None
```

## `unreal.BlackboardKeySelector(StructBase)`

```python
unreal.BlackboardKeySelector.__init__(allowed_types: Array[BlackboardKeyType] = [], selected_key_name: Name = "None", selected_key_type: Class = None, selected_key_id: int = 0, none_is_allowed_value: bool = False) -> None
unreal.BlackboardKeySelector.allowed_types(value: Array[BlackboardKeyType]) -> None
unreal.BlackboardKeySelector.none_is_allowed_value(value: bool) -> None
unreal.BlackboardKeySelector.selected_key_id(value: int) -> None
unreal.BlackboardKeySelector.selected_key_name(value: Name) -> None
unreal.BlackboardKeySelector.selected_key_type(value: Class) -> None
```

## `unreal.CameraDirectorStateTreeEvaluationData(StructBase)`

```python
unreal.CameraDirectorStateTreeEvaluationData.__init__() -> None
```

## `unreal.CrowdFollowingComponent(PathFollowingComponent)`

```python
unreal.CrowdFollowingComponent.suspend_crowd_steering(suspend: bool) -> None
```

## `unreal.EQSParametrizedQueryExecutionRequest(StructBase)`

```python
unreal.EQSParametrizedQueryExecutionRequest.__init__() -> None
```

## `unreal.LandmassBrushEffectsList(StructBase)`

```python
unreal.LandmassBrushEffectsList.__init__(blurring: BrushEffectBlurring = [True, 2], curl_noise: BrushEffectCurlNoise = [0.000000, 0.000000, 16.000000, 3.000000], displacement: BrushEffectDisplacement = [0.000000, 0.000000, None, -128.000000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000], smooth_blending: BrushEffectSmoothBlending = [0.010000, 0.010000], terracing: BrushEffectTerracing = [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.LandmassBrushEffectsList.blurring(value: BrushEffectBlurring) -> None
unreal.LandmassBrushEffectsList.curl_noise(value: BrushEffectCurlNoise) -> None
unreal.LandmassBrushEffectsList.displacement(value: BrushEffectDisplacement) -> None
unreal.LandmassBrushEffectsList.smooth_blending(value: BrushEffectSmoothBlending) -> None
unreal.LandmassBrushEffectsList.terracing(value: BrushEffectTerracing) -> None
```

## `unreal.LandmassErosionBrushBase(LandscapeBlueprintBrushBase)`

```python
unreal.LandmassErosionBrushBase.actor_selection_changed(selected: bool) -> None
unreal.LandmassErosionBrushBase.get_landscape() -> Landscape
unreal.LandmassErosionBrushBase.set_target_landscape(owning_landscape: Landscape) -> None
```

## `unreal.LandmassFalloffSettings(StructBase)`

```python
unreal.LandmassFalloffSettings.__init__(falloff_mode: BrushFalloffMode = BrushFalloffMode.ANGLE, falloff_angle: float = 0.000000, falloff_width: float = 0.000000, edge_offset: float = 0.000000, z_offset: float = 0.000000) -> None
unreal.LandmassFalloffSettings.edge_offset(value: float) -> None
unreal.LandmassFalloffSettings.falloff_angle(value: float) -> None
unreal.LandmassFalloffSettings.falloff_mode(value: BrushFalloffMode) -> None
unreal.LandmassFalloffSettings.falloff_width(value: float) -> None
unreal.LandmassFalloffSettings.z_offset(value: float) -> None
```

## `unreal.LandmassManagerBase(LandscapeBlueprintBrushBase)`

```python
unreal.LandmassManagerBase.actor_selection_changed(selected: bool) -> None
unreal.LandmassManagerBase.add_brush_to_array(brush_to_add: LandmassActor) -> None
unreal.LandmassManagerBase.add_brush_to_tree(brush_to_add: LandmassActor, extents: Vector4, map_to_whole_landscape: bool) -> Tuple[Vector4, Array[LandmassActor], Array[int]]
unreal.LandmassManagerBase.brush_node_data(value: Array[BrushDataTree]) -> None
unreal.LandmassManagerBase.brush_tree_depth(value: int) -> None
unreal.LandmassManagerBase.consolidate_nodes() -> Array[int]
unreal.LandmassManagerBase.draw_brush_material(brush: LandmassActor, brush_material: MaterialInterface) -> None
unreal.LandmassManagerBase.get_actors_within_modified_nodes() -> Tuple[Array[LandmassActor], Array[int]]
unreal.LandmassManagerBase.get_landscape() -> Landscape
unreal.LandmassManagerBase.get_nodes_within_extents() -> Tuple[Array[int], Vector4]
unreal.LandmassManagerBase.landmass_brushes(value: Array[LandmassActor]) -> None
unreal.LandmassManagerBase.landscape_information(value: LandmassLandscapeInfo) -> None
unreal.LandmassManagerBase.launch_landmass_editor(brush_requesting_editor: LandmassActor) -> None
unreal.LandmassManagerBase.populate_node_tree() -> None
unreal.LandmassManagerBase.remove_brush_from_tree(brush_to_remove: LandmassActor) -> Array[int]
unreal.LandmassManagerBase.request_update_from_brush(brush_requesting_update: LandmassActor) -> None
unreal.LandmassManagerBase.set_capture_boundary_normals(capture_boundary_normals: bool) -> None
unreal.LandmassManagerBase.set_target_landscape(owning_landscape: Landscape) -> None
unreal.LandmassManagerBase.sort_brushes(brush_array_to_match: Array[LandmassActor], actors_to_sort: Array[LandmassActor]) -> Array[LandmassActor]
unreal.LandmassManagerBase.toggle_preview_mode(enable_preview_mode: bool) -> None
unreal.LandmassManagerBase.update_child_data_counts() -> None
```

## `unreal.LandmassTerrainCarvingSettings(StructBase)`

```python
unreal.LandmassTerrainCarvingSettings.__init__(blend_mode: BrushBlendType = BrushBlendType.ALPHA_BLEND, invert_shape: bool = False, falloff_settings: LandmassFalloffSettings = [BrushFalloffMode.ANGLE, 45.000000, 1024.000000, 0.000000, 0.000000], effects: LandmassBrushEffectsList = [[True, 2], [0.000000, 0.000000, 16.000000, 3.000000], [0.000000, 0.000000, None, -128.000000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000], [0.010000, 0.010000], [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]], priority: int = 0) -> None
unreal.LandmassTerrainCarvingSettings.blend_mode(value: BrushBlendType) -> None
unreal.LandmassTerrainCarvingSettings.effects(value: LandmassBrushEffectsList) -> None
unreal.LandmassTerrainCarvingSettings.falloff_settings(value: LandmassFalloffSettings) -> None
unreal.LandmassTerrainCarvingSettings.invert_shape(value: bool) -> None
unreal.LandmassTerrainCarvingSettings.priority(value: int) -> None
```

## `unreal.MassAgentComponent(ActorComponent)`

```python
unreal.MassAgentComponent.disable() -> None
unreal.MassAgentComponent.enable() -> None
unreal.MassAgentComponent.kill_entity(destroy_actor: bool) -> None
```

## `unreal.MassConstSharedFragment(StructBase)`

```python
unreal.MassConstSharedFragment.__init__() -> None
```

## `unreal.MassDistanceLODParameters(MassConstSharedFragment)`

```python
unreal.MassDistanceLODParameters.__init__() -> None
```

## `unreal.MassEntityConfig(StructBase)`

```python
unreal.MassEntityConfig.__init__() -> None
```

## `unreal.MassEntityTestFarmPlot(Actor)`

```python
unreal.MassEntityTestFarmPlot.harvest_icon_ismc() -> HierarchicalInstancedStaticMeshComponent
```

## `unreal.MassMovementParameters(MassConstSharedFragment)`

```python
unreal.MassMovementParameters.__init__() -> None
```

## `unreal.MassMovementStyleParameters(StructBase)`

```python
unreal.MassMovementStyleParameters.__init__() -> None
```

## `unreal.MassMovementStyleRef(StructBase)`

```python
unreal.MassMovementStyleRef.__init__() -> None
```

## `unreal.MassMovementStyleSpeedParameters(StructBase)`

```python
unreal.MassMovementStyleSpeedParameters.__init__() -> None
```

## `unreal.MassProcessingContext(StructBase)`

```python
unreal.MassProcessingContext.__init__() -> None
```

## `unreal.MassReplicationParameters(MassConstSharedFragment)`

```python
unreal.MassReplicationParameters.__init__() -> None
```

## `unreal.MassRepresentationParameters(MassConstSharedFragment)`

```python
unreal.MassRepresentationParameters.__init__() -> None
```

## `unreal.MassSimulationLODParameters(MassConstSharedFragment)`

```python
unreal.MassSimulationLODParameters.__init__() -> None
```

## `unreal.MassSimulationVariableTickParameters(MassConstSharedFragment)`

```python
unreal.MassSimulationVariableTickParameters.__init__() -> None
```

## `unreal.MassSmartObjectCandidateSlots(StructBase)`

```python
unreal.MassSmartObjectCandidateSlots.__init__() -> None
```

## `unreal.MassSpawnDataGenerator(StructBase)`

```python
unreal.MassSpawnDataGenerator.__init__(generator_instance: MassEntitySpawnDataGeneratorBase = None, proportion: float = 0.000000) -> None
unreal.MassSpawnDataGenerator.generator_instance(value: MassEntitySpawnDataGeneratorBase) -> None
unreal.MassSpawnDataGenerator.proportion(value: float) -> None
```

## `unreal.MassSpawnedEntityType(StructBase)`

```python
unreal.MassSpawnedEntityType.__init__(entity_config: MassEntityConfigAsset = None, proportion: float = 0.000000) -> None
unreal.MassSpawnedEntityType.entity_config(value: MassEntityConfigAsset) -> None
unreal.MassSpawnedEntityType.proportion(value: float) -> None
```

## `unreal.MassSpawner(Actor)`

```python
unreal.MassSpawner.clear_templates() -> None
unreal.MassSpawner.debug_clear() -> None
unreal.MassSpawner.debug_spawn() -> None
unreal.MassSpawner.do_despawning() -> None
unreal.MassSpawner.do_spawning() -> None
unreal.MassSpawner.entity_types(value: Array[MassSpawnedEntityType]) -> None
unreal.MassSpawner.get_count() -> int
unreal.MassSpawner.get_spawning_count_scale() -> float
unreal.MassSpawner.on_despawning_finished_event(value: MassSpawnerOnDespawningFinishedEvent) -> None
unreal.MassSpawner.on_spawning_finished_event(value: MassSpawnerOnSpawningFinishedEvent) -> None
unreal.MassSpawner.scale_spawning_count(scale: float) -> None
unreal.MassSpawner.unload_config() -> None
```

## `unreal.MassSpawnerOnDespawningFinishedEvent(MulticastDelegateBase)`

```python
unreal.MassSpawnerOnDespawningFinishedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MassSpawnerOnSpawningFinishedEvent(MulticastDelegateBase)`

```python
unreal.MassSpawnerOnSpawningFinishedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MassVisualizationLODParameters(MassConstSharedFragment)`

```python
unreal.MassVisualizationLODParameters.__init__() -> None
```

## `unreal.NavMeshResolutionParam(StructBase)`

```python
unreal.NavMeshResolutionParam.__init__() -> None
```

## `unreal.NavigationEvent(InputEvent)`

```python
unreal.NavigationEvent.__init__() -> None
```

## `unreal.NavigationFilterArea(StructBase)`

```python
unreal.NavigationFilterArea.__init__() -> None
```

## `unreal.NavigationFilterFlags(StructBase)`

```python
unreal.NavigationFilterFlags.__init__() -> None
```

## `unreal.NavigationLink(NavigationLinkBase)`

```python
unreal.NavigationLink.__init__(direction: NavLinkDirection = NavLinkDirection.BOTH_WAYS, left: Vector = [0.000000, 0.000000, 0.000000], right: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.NavigationLink.left(value: Vector) -> None
unreal.NavigationLink.right(value: Vector) -> None
```

## `unreal.NavigationLinkBase(StructBase)`

```python
unreal.NavigationLinkBase.__init__(direction: NavLinkDirection = NavLinkDirection.BOTH_WAYS) -> None
unreal.NavigationLinkBase.direction(value: NavLinkDirection) -> None
```

## `unreal.NavigationPath(Object)`

```python
unreal.NavigationPath.enable_debug_drawing(should_draw_debug_data: bool, path_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000]) -> None
unreal.NavigationPath.enable_recalculation_on_invalidation(do_recalculation: NavigationOptionFlag) -> None
unreal.NavigationPath.get_debug_string() -> str
unreal.NavigationPath.get_path_cost() -> float
unreal.NavigationPath.get_path_lenght() -> float
unreal.NavigationPath.get_path_length() -> float
unreal.NavigationPath.is_partial() -> bool
unreal.NavigationPath.is_string_pulled() -> bool
unreal.NavigationPath.is_valid() -> bool
unreal.NavigationPath.path_points() -> Array[Vector]
unreal.NavigationPath.path_updated_notifier(value: OnNavigationPathUpdated) -> None
unreal.NavigationPath.recalculate_on_invalidation() -> NavigationOptionFlag
```

## `unreal.NavigationSegmentLink(NavigationLinkBase)`

```python
unreal.NavigationSegmentLink.__init__(direction: NavLinkDirection = NavLinkDirection.BOTH_WAYS) -> None
```

## `unreal.NavigationSystemV1(NavigationSystemBase)`

```python
unreal.NavigationSystemV1.crowd_manager_class() -> Class
unreal.NavigationSystemV1.default_agent_name() -> Name
unreal.NavigationSystemV1.find_path_to_actor_synchronously(world_context_object: Object, path_start: Vector, goal_actor: Actor, tether_distance: float = 50.000000, pathfinding_context: Actor = None, filter_class: Class = None) -> NavigationPath
unreal.NavigationSystemV1.find_path_to_location_synchronously(world_context_object: Object, path_start: Vector, path_end: Vector, pathfinding_context: Actor = None, filter_class: Class = None) -> NavigationPath
unreal.NavigationSystemV1.get_navigation_system(world_context_object: Object) -> NavigationSystemV1
unreal.NavigationSystemV1.get_path_cost(world_context_object: Object, path_start: Vector, path_end: Vector, nav_data: NavigationData = None, filter_class: Class = None) -> Tuple[NavigationQueryResult, float]
unreal.NavigationSystemV1.get_path_length(world_context_object: Object, path_start: Vector, path_end: Vector, nav_data: NavigationData = None, filter_class: Class = None) -> Tuple[NavigationQueryResult, float]
unreal.NavigationSystemV1.get_random_location_in_navigable_radius(world_context_object: Object, origin: Vector, radius: float, nav_data: NavigationData = None, filter_class: Class = None) -> Optional[Vector]
unreal.NavigationSystemV1.get_random_point_in_navigable_radius(world_context_object: Object, origin: Vector, radius: float, nav_data: NavigationData = None, filter_class: Class = None) -> Optional[Vector]
unreal.NavigationSystemV1.get_random_reachable_point_in_radius(world_context_object: Object, origin: Vector, radius: float, nav_data: NavigationData = None, filter_class: Class = None) -> Optional[Vector]
unreal.NavigationSystemV1.is_navigation_being_built(world_context_object: Object) -> bool
unreal.NavigationSystemV1.is_navigation_being_built_or_locked(world_context_object: Object) -> bool
unreal.NavigationSystemV1.k2_replace_area_in_octree_data(object: Object, old_area: Class, new_area: Class) -> bool
unreal.NavigationSystemV1.navigation_raycast(world_context_object: Object, ray_start: Vector, ray_end: Vector, filter_class: Class = None, querier: Controller = None) -> Optional[Vector]
unreal.NavigationSystemV1.on_navigation_bounds_updated(nav_volume: NavMeshBoundsVolume) -> None
unreal.NavigationSystemV1.on_navigation_generation_finished_delegate(value: OnNavDataGenericEvent) -> None
unreal.NavigationSystemV1.project_point_to_navigation(world_context_object: Object, point: Vector, nav_data: NavigationData, filter_class: Class, query_extent: Vector = [0.000000, 0.000000, 0.000000]) -> Optional[Vector]
unreal.NavigationSystemV1.register_navigation_invoker(invoker: Actor, tile_generation_radius: float = 3000.000000, tile_removal_radius: float = 5000.000000) -> None
unreal.NavigationSystemV1.reset_max_simultaneous_tile_generation_jobs_count() -> None
unreal.NavigationSystemV1.set_geometry_gathering_mode(new_mode: NavDataGatheringModeConfig) -> None
unreal.NavigationSystemV1.set_max_simultaneous_tile_generation_jobs_count(max_number_of_jobs: int) -> None
unreal.NavigationSystemV1.unregister_navigation_invoker(invoker: Actor) -> None
```

## `unreal.OnNavigationPathUpdated(MulticastDelegateBase)`

```python
unreal.OnNavigationPathUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.RecastNavMesh(NavigationData)`

```python
unreal.RecastNavMesh.agent_max_step_height(value: float) -> None
unreal.RecastNavMesh.cell_height(value: float) -> None
unreal.RecastNavMesh.cell_size(value: float) -> None
unreal.RecastNavMesh.k2_replace_area_in_tile_bounds(bounds: Box, old_area: Class, new_area: Class, replace_links: bool = True) -> bool
```

## `unreal.RecastNavMeshTileGenerationDebug(StructBase)`

```python
unreal.RecastNavMeshTileGenerationDebug.__init__() -> None
```

## `unreal.SourceEffectEQSettings(StructBase)`

```python
unreal.SourceEffectEQSettings.__init__(eq_bands: Array[SourceEffectEQBand] = []) -> None
unreal.SourceEffectEQSettings.eq_bands(value: Array[SourceEffectEQBand]) -> None
```

## `unreal.StateTreeActiveStates(StructBase)`

```python
unreal.StateTreeActiveStates.__init__() -> None
```

## `unreal.StateTreeComponent(BrainComponent)`

```python
unreal.StateTreeComponent.get_state_tree_run_status() -> StateTreeRunStatus
unreal.StateTreeComponent.on_state_tree_run_status_changed(value: StateTreeRunStatusChanged) -> None
unreal.StateTreeComponent.send_state_tree_event(event: StateTreeEvent) -> None
unreal.StateTreeComponent.set_start_logic_automatically(start_logic_automatically: bool) -> None
```

## `unreal.StateTreeConditionItem(StateTreeEditorNode)`

```python
unreal.StateTreeConditionItem.__init__() -> None
```

## `unreal.StateTreeDataHandle(StructBase)`

```python
unreal.StateTreeDataHandle.__init__() -> None
```

## `unreal.StateTreeEditorColor(StructBase)`

```python
unreal.StateTreeEditorColor.__init__() -> None
```

## `unreal.StateTreeEditorColorRef(StructBase)`

```python
unreal.StateTreeEditorColorRef.__init__() -> None
```

## `unreal.StateTreeEvaluatorItem(StateTreeEditorNode)`

```python
unreal.StateTreeEvaluatorItem.__init__() -> None
```

## `unreal.StateTreeEvent(StructBase)`

```python
unreal.StateTreeEvent.__init__(tag: GameplayTag = ["None"], payload: InstancedStruct = [], origin: Name = "None") -> None
unreal.StateTreeEvent.origin(value: Name) -> None
unreal.StateTreeEvent.payload(value: InstancedStruct) -> None
unreal.StateTreeEvent.tag(value: GameplayTag) -> None
```

## `unreal.StateTreeEventDesc(StructBase)`

```python
unreal.StateTreeEventDesc.__init__() -> None
```

## `unreal.StateTreeExecutionFrame(StructBase)`

```python
unreal.StateTreeExecutionFrame.__init__() -> None
```

## `unreal.StateTreeHandle(StateTreeStateHandle)`

```python
unreal.StateTreeHandle.__init__() -> None
```

## `unreal.StateTreeIndex16(StructBase)`

```python
unreal.StateTreeIndex16.__init__() -> None
```

## `unreal.StateTreeIndex8(StructBase)`

```python
unreal.StateTreeIndex8.__init__() -> None
```

## `unreal.StateTreeItem(StateTreeEditorNode)`

```python
unreal.StateTreeItem.__init__() -> None
```

## `unreal.StateTreePropertyRef(StructBase)`

```python
unreal.StateTreePropertyRef.__init__() -> None
```

## `unreal.StateTreeReference(StructBase)`

```python
unreal.StateTreeReference.__init__() -> None
```

## `unreal.StateTreeReferenceOverrideItem(StructBase)`

```python
unreal.StateTreeReferenceOverrideItem.__init__() -> None
```

## `unreal.StateTreeReferenceOverrides(StructBase)`

```python
unreal.StateTreeReferenceOverrides.__init__() -> None
```

## `unreal.StateTreeRunStatusChanged(MulticastDelegateBase)`

```python
unreal.StateTreeRunStatusChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.StateTreeStateHandle(StructBase)`

```python
unreal.StateTreeStateHandle.__init__() -> None
```

## `unreal.StateTreeStateLink(StructBase)`

```python
unreal.StateTreeStateLink.__init__() -> None
```

## `unreal.StateTreeStateParameters(StructBase)`

```python
unreal.StateTreeStateParameters.__init__() -> None
```

## `unreal.StateTreeStructRef(StructBase)`

```python
unreal.StateTreeStructRef.__init__() -> None
```

## `unreal.StateTreeTaskItem(StateTreeEditorNode)`

```python
unreal.StateTreeTaskItem.__init__() -> None
```

## `unreal.StateTreeTransition(StructBase)`

```python
unreal.StateTreeTransition.__init__() -> None
```

## `unreal.StateTreeTransition2(StateTreeTransition)`

```python
unreal.StateTreeTransition2.__init__() -> None
```

## `unreal.StateTreeTransitionRequest(StructBase)`

```python
unreal.StateTreeTransitionRequest.__init__() -> None
```

## `unreal.StateTreeTransitionResult(StructBase)`

```python
unreal.StateTreeTransitionResult.__init__(next_active_frames: Array[StateTreeExecutionFrame] = [], current_run_status: StateTreeRunStatus = StateTreeRunStatus.RUNNING, source_state: StateTreeStateHandle = [], target_state: StateTreeStateHandle = [], current_state: StateTreeStateHandle = [], change_type: StateTreeStateChangeType = StateTreeStateChangeType.NONE, priority: StateTreeTransitionPriority = 0, source_state_tree: StateTree = None, source_root_state: StateTreeStateHandle = []) -> None
unreal.StateTreeTransitionResult.change_type() -> StateTreeStateChangeType
unreal.StateTreeTransitionResult.current_run_status() -> StateTreeRunStatus
unreal.StateTreeTransitionResult.current_state() -> StateTreeStateHandle
unreal.StateTreeTransitionResult.next_active_frames() -> Array[StateTreeExecutionFrame]
unreal.StateTreeTransitionResult.priority() -> StateTreeTransitionPriority
unreal.StateTreeTransitionResult.source_root_state() -> StateTreeStateHandle
unreal.StateTreeTransitionResult.source_state() -> StateTreeStateHandle
unreal.StateTreeTransitionResult.source_state_tree() -> StateTree
unreal.StateTreeTransitionResult.target_state() -> StateTreeStateHandle
```

## `unreal.SubmixEffectSubmixEQSettings(StructBase)`

```python
unreal.SubmixEffectSubmixEQSettings.__init__(eq_bands: Array[SubmixEffectEQBand] = []) -> None
unreal.SubmixEffectSubmixEQSettings.eq_bands(value: Array[SubmixEffectEQBand]) -> None
```

## `unreal.ValueOrBlackboardKeyBase(StructBase)`

```python
unreal.ValueOrBlackboardKeyBase.__init__() -> None
```

