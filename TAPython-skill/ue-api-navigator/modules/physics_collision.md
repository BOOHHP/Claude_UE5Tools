# Unreal Python API — Physics Collision

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AIDamageEvent(StructBase)`

```python
unreal.AIDamageEvent.__init__(amount: float = 0.000000, location: Vector = [0.000000, 0.000000, 0.000000], hit_location: Vector = [0.000000, 0.000000, 0.000000], damaged_actor: Actor = None, instigator: Actor = None, tag: Name = "None") -> None
unreal.AIDamageEvent.amount(value: float) -> None
unreal.AIDamageEvent.damaged_actor(value: Actor) -> None
unreal.AIDamageEvent.hit_location(value: Vector) -> None
unreal.AIDamageEvent.instigator(value: Actor) -> None
unreal.AIDamageEvent.location(value: Vector) -> None
unreal.AIDamageEvent.tag(value: Name) -> None
```

## `unreal.AISenseConfig_Damage(AISenseConfig)`

```python
unreal.AISenseConfig_Damage.implementation() -> Class
```

## `unreal.AISenseEvent_Damage(AISenseEvent)`

```python
unreal.AISenseEvent_Damage.event(value: AIDamageEvent) -> None
```

## `unreal.AISense_Damage(AISense)`

```python
unreal.AISense_Damage.report_damage_event(world_context_object: Object, damaged_actor: Actor, instigator: Actor, damage_amount: float, event_location: Vector, hit_location: Vector, tag: Name = "None") -> None
```

## `unreal.AesAssetCollisionData(StructBase)`

```python
unreal.AesAssetCollisionData.__init__(collision_type: AesAssetCollisionType = AesAssetCollisionType.BOUNDS_NO_CAP, component_class: SoftClassPath = [""]) -> None
unreal.AesAssetCollisionData.collision_type(value: AesAssetCollisionType) -> None
unreal.AesAssetCollisionData.component_class(value: SoftClassPath) -> None
```

## `unreal.AesCollisionAssetInfo(TableRowBase)`

```python
unreal.AesCollisionAssetInfo.__init__(tile_assets: Array[SoftObjectPath] = [], base_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], tile_id: IntVector = [0, 0, 0], layer_name: Name = "None") -> None
unreal.AesCollisionAssetInfo.base_transform(value: Transform) -> None
unreal.AesCollisionAssetInfo.layer_name(value: Name) -> None
unreal.AesCollisionAssetInfo.tile_assets(value: Array[SoftObjectPath]) -> None
unreal.AesCollisionAssetInfo.tile_id(value: IntVector) -> None
```

## `unreal.AesCollisionComponent(AesCollisionComponentBase)`

```python
unreal.AesCollisionComponent.index_buffer(value: Array[int]) -> None
unreal.AesCollisionComponent.local_bounds(value: BoxSphereBounds) -> None
unreal.AesCollisionComponent.override_wireframe_color() -> bool
unreal.AesCollisionComponent.vertex_buffer(value: Array[Vector3f]) -> None
unreal.AesCollisionComponent.wireframe_color_override() -> Color
```

## `unreal.AesCollisionLayerInfo(StructBase)`

```python
unreal.AesCollisionLayerInfo.__init__() -> None
```

## `unreal.AngularDriveConstraint(StructBase)`

```python
unreal.AngularDriveConstraint.__init__() -> None
```

## `unreal.AsyncPhysicsInputComponent(ActorComponent)`

```python
unreal.AsyncPhysicsInputComponent.get_data_to_consume() -> AsyncPhysicsData
unreal.AsyncPhysicsInputComponent.get_data_to_write() -> AsyncPhysicsData
```

## `unreal.BodyInstanceAsyncPhysicsTickHandle(StructBase)`

```python
unreal.BodyInstanceAsyncPhysicsTickHandle.__init__() -> None
```

## `unreal.CRSimSoftCollision(StructBase)`

```python
unreal.CRSimSoftCollision.__init__() -> None
```

## `unreal.CameraCollisionData(StructBase)`

```python
unreal.CameraCollisionData.__init__(collision_mode: CameraCollisionMode = CameraCollisionMode.CCM_NO_COLLISION, collision_profile: Name = "None", custom_points: Array[Vector] = [], ground_position_mode: GroundPositionMode = GroundPositionMode.GPM_NO_COLLISION) -> None
unreal.CameraCollisionData.collision_mode(value: CameraCollisionMode) -> None
unreal.CameraCollisionData.collision_profile(value: Name) -> None
unreal.CameraCollisionData.custom_points(value: Array[Vector]) -> None
unreal.CameraCollisionData.ground_position_mode(value: GroundPositionMode) -> None
```

## `unreal.ChaosBreakEvent(StructBase)`

```python
unreal.ChaosBreakEvent.__init__(component: PrimitiveComponent = None, location: Vector = [0.000000, 0.000000, 0.000000], velocity: Vector = [0.000000, 0.000000, 0.000000], angular_velocity: Vector = [0.000000, 0.000000, 0.000000], extents: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, index: int = 0, from_crumble: bool = False) -> None
unreal.ChaosBreakEvent.angular_velocity() -> Vector
unreal.ChaosBreakEvent.component() -> PrimitiveComponent
unreal.ChaosBreakEvent.extents() -> Vector
unreal.ChaosBreakEvent.from_crumble() -> bool
unreal.ChaosBreakEvent.index() -> int
unreal.ChaosBreakEvent.location() -> Vector
unreal.ChaosBreakEvent.mass() -> float
unreal.ChaosBreakEvent.velocity() -> Vector
```

## `unreal.ChaosBreakingEventData(StructBase)`

```python
unreal.ChaosBreakingEventData.__init__(location: Vector = [0.000000, 0.000000, 0.000000], velocity: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000) -> None
unreal.ChaosBreakingEventData.location() -> Vector
unreal.ChaosBreakingEventData.mass() -> float
unreal.ChaosBreakingEventData.velocity() -> Vector
```

## `unreal.ChaosBreakingEventRequestSettings(StructBase)`

```python
unreal.ChaosBreakingEventRequestSettings.__init__(max_number_of_results: int = 0, min_radius: float = 0.000000, min_speed: float = 0.000000, min_mass: float = 0.000000, max_distance: float = 0.000000, sort_method: ChaosBreakingSortMethod = ChaosBreakingSortMethod.SORT_NONE) -> None
unreal.ChaosBreakingEventRequestSettings.max_distance(value: float) -> None
unreal.ChaosBreakingEventRequestSettings.max_number_of_results(value: int) -> None
unreal.ChaosBreakingEventRequestSettings.min_mass(value: float) -> None
unreal.ChaosBreakingEventRequestSettings.min_radius(value: float) -> None
unreal.ChaosBreakingEventRequestSettings.min_speed(value: float) -> None
unreal.ChaosBreakingEventRequestSettings.sort_method(value: ChaosBreakingSortMethod) -> None
```

## `unreal.ChaosCacheManager(Actor)`

```python
unreal.ChaosCacheManager.enable_playback(index: int, enable: bool) -> None
unreal.ChaosCacheManager.enable_playback_by_cache(cache_name: Name, enable: bool) -> None
unreal.ChaosCacheManager.reset_all_component_transforms() -> None
unreal.ChaosCacheManager.reset_single_transform(index: int) -> None
unreal.ChaosCacheManager.set_cache_collection(cache_collection: ChaosCacheCollection) -> None
unreal.ChaosCacheManager.set_current_time(current_time: float) -> None
unreal.ChaosCacheManager.start_time(value: float) -> None
unreal.ChaosCacheManager.trigger_all() -> None
unreal.ChaosCacheManager.trigger_component(component: PrimitiveComponent) -> None
unreal.ChaosCacheManager.trigger_component_by_cache(cache_name: Name) -> None
```

## `unreal.ChaosCollisionEventData(StructBase)`

```python
unreal.ChaosCollisionEventData.__init__(location: Vector = [0.000000, 0.000000, 0.000000], normal: Vector = [0.000000, 0.000000, 0.000000], velocity1: Vector = [0.000000, 0.000000, 0.000000], velocity2: Vector = [0.000000, 0.000000, 0.000000], mass1: float = 0.000000, mass2: float = 0.000000, impulse: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.ChaosCollisionEventData.impulse() -> Vector
unreal.ChaosCollisionEventData.location() -> Vector
unreal.ChaosCollisionEventData.mass1() -> float
unreal.ChaosCollisionEventData.mass2() -> float
unreal.ChaosCollisionEventData.normal() -> Vector
unreal.ChaosCollisionEventData.velocity1() -> Vector
unreal.ChaosCollisionEventData.velocity2() -> Vector
```

## `unreal.ChaosCollisionEventRequestSettings(StructBase)`

```python
unreal.ChaosCollisionEventRequestSettings.__init__(max_number_results: int = 0, min_mass: float = 0.000000, min_speed: float = 0.000000, min_impulse: float = 0.000000, max_distance: float = 0.000000, sort_method: ChaosCollisionSortMethod = ChaosCollisionSortMethod.SORT_NONE) -> None
unreal.ChaosCollisionEventRequestSettings.max_distance(value: float) -> None
unreal.ChaosCollisionEventRequestSettings.max_number_results(value: int) -> None
unreal.ChaosCollisionEventRequestSettings.min_impulse(value: float) -> None
unreal.ChaosCollisionEventRequestSettings.min_mass(value: float) -> None
unreal.ChaosCollisionEventRequestSettings.min_speed(value: float) -> None
unreal.ChaosCollisionEventRequestSettings.sort_method(value: ChaosCollisionSortMethod) -> None
```

## `unreal.ChaosCrumblingEvent(StructBase)`

```python
unreal.ChaosCrumblingEvent.__init__(component: PrimitiveComponent = None, location: Vector = [0.000000, 0.000000, 0.000000], orientation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], linear_velocity: Vector = [0.000000, 0.000000, 0.000000], angular_velocity: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, local_bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], children: Array[int] = []) -> None
unreal.ChaosCrumblingEvent.angular_velocity() -> Vector
unreal.ChaosCrumblingEvent.children() -> Array[int]
unreal.ChaosCrumblingEvent.component() -> PrimitiveComponent
unreal.ChaosCrumblingEvent.linear_velocity() -> Vector
unreal.ChaosCrumblingEvent.local_bounds() -> Box
unreal.ChaosCrumblingEvent.location() -> Vector
unreal.ChaosCrumblingEvent.mass() -> float
unreal.ChaosCrumblingEvent.orientation() -> Quat
```

## `unreal.ChaosDebugSubstepControl(StructBase)`

```python
unreal.ChaosDebugSubstepControl.__init__() -> None
```

## `unreal.ChaosDestructionListener(SceneComponent)`

```python
unreal.ChaosDestructionListener.add_chaos_solver_actor(chaos_solver_actor: ChaosSolverActor) -> None
unreal.ChaosDestructionListener.add_geometry_collection_actor(geometry_collection_actor: GeometryCollectionActor) -> None
unreal.ChaosDestructionListener.breaking_event_request_settings() -> ChaosBreakingEventRequestSettings
unreal.ChaosDestructionListener.chaos_solver_actors() -> Set[ChaosSolverActor]
unreal.ChaosDestructionListener.collision_event_request_settings() -> ChaosCollisionEventRequestSettings
unreal.ChaosDestructionListener.geometry_collection_actors() -> Set[GeometryCollectionActor]
unreal.ChaosDestructionListener.is_breaking_event_listening_enabled() -> bool
unreal.ChaosDestructionListener.is_collision_event_listening_enabled() -> bool
unreal.ChaosDestructionListener.is_event_listening() -> bool
unreal.ChaosDestructionListener.is_removal_event_listening_enabled() -> bool
unreal.ChaosDestructionListener.is_trailing_event_listening_enabled() -> bool
unreal.ChaosDestructionListener.on_breaking_events(value: OnChaosBreakingEvents) -> None
unreal.ChaosDestructionListener.on_collision_events(value: OnChaosCollisionEvents) -> None
unreal.ChaosDestructionListener.on_removal_events(value: OnChaosRemovalEvents) -> None
unreal.ChaosDestructionListener.on_trailing_events(value: OnChaosTrailingEvents) -> None
unreal.ChaosDestructionListener.removal_event_request_settings() -> ChaosRemovalEventRequestSettings
unreal.ChaosDestructionListener.remove_chaos_solver_actor(chaos_solver_actor: ChaosSolverActor) -> None
unreal.ChaosDestructionListener.remove_geometry_collection_actor(geometry_collection_actor: GeometryCollectionActor) -> None
unreal.ChaosDestructionListener.set_breaking_event_enabled(is_enabled: bool) -> None
unreal.ChaosDestructionListener.set_breaking_event_request_settings(settings: ChaosBreakingEventRequestSettings) -> None
unreal.ChaosDestructionListener.set_collision_event_enabled(is_enabled: bool) -> None
unreal.ChaosDestructionListener.set_collision_event_request_settings(settings: ChaosCollisionEventRequestSettings) -> None
unreal.ChaosDestructionListener.set_removal_event_enabled(is_enabled: bool) -> None
unreal.ChaosDestructionListener.set_removal_event_request_settings(settings: ChaosRemovalEventRequestSettings) -> None
unreal.ChaosDestructionListener.set_trailing_event_enabled(is_enabled: bool) -> None
unreal.ChaosDestructionListener.set_trailing_event_request_settings(settings: ChaosTrailingEventRequestSettings) -> None
unreal.ChaosDestructionListener.sort_breaking_events(breaking_events: Array[ChaosBreakingEventData], sort_method: ChaosBreakingSortMethod) -> Array[ChaosBreakingEventData]
unreal.ChaosDestructionListener.sort_collision_events(collision_events: Array[ChaosCollisionEventData], sort_method: ChaosCollisionSortMethod) -> Array[ChaosCollisionEventData]
unreal.ChaosDestructionListener.sort_removal_events(removal_events: Array[ChaosRemovalEventData], sort_method: ChaosRemovalSortMethod) -> Array[ChaosRemovalEventData]
unreal.ChaosDestructionListener.sort_trailing_events(trailing_events: Array[ChaosTrailingEventData], sort_method: ChaosTrailingSortMethod) -> Array[ChaosTrailingEventData]
unreal.ChaosDestructionListener.trailing_event_request_settings() -> ChaosTrailingEventRequestSettings
```

## `unreal.ChaosEventRelay(Object)`

```python
unreal.ChaosEventRelay.on_break_event(value: BreakEventSignature) -> None
unreal.ChaosEventRelay.on_collision_event(value: CollisionEventSignature) -> None
unreal.ChaosEventRelay.on_crumbling_event(value: CrumblingEventSignature) -> None
unreal.ChaosEventRelay.on_removal_event(value: RemovalEventSignature) -> None
```

## `unreal.ChaosPhysicsCollisionInfo(StructBase)`

```python
unreal.ChaosPhysicsCollisionInfo.__init__(component: PrimitiveComponent = None, other_component: PrimitiveComponent = None, location: Vector = [0.000000, 0.000000, 0.000000], normal: Vector = [0.000000, 0.000000, 0.000000], accumulated_impulse: Vector = [0.000000, 0.000000, 0.000000], velocity: Vector = [0.000000, 0.000000, 0.000000], other_velocity: Vector = [0.000000, 0.000000, 0.000000], angular_velocity: Vector = [0.000000, 0.000000, 0.000000], other_angular_velocity: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, other_mass: float = 0.000000) -> None
unreal.ChaosPhysicsCollisionInfo.accumulated_impulse(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.angular_velocity(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.component(value: PrimitiveComponent) -> None
unreal.ChaosPhysicsCollisionInfo.location(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.mass(value: float) -> None
unreal.ChaosPhysicsCollisionInfo.normal(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.other_angular_velocity(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.other_component(value: PrimitiveComponent) -> None
unreal.ChaosPhysicsCollisionInfo.other_mass(value: float) -> None
unreal.ChaosPhysicsCollisionInfo.other_velocity(value: Vector) -> None
unreal.ChaosPhysicsCollisionInfo.velocity(value: Vector) -> None
```

## `unreal.ChaosPhysicsSettings(StructBase)`

```python
unreal.ChaosPhysicsSettings.__init__() -> None
```

## `unreal.ChaosRemovalEvent(StructBase)`

```python
unreal.ChaosRemovalEvent.__init__(component: PrimitiveComponent = None, location: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000) -> None
unreal.ChaosRemovalEvent.component() -> PrimitiveComponent
unreal.ChaosRemovalEvent.location() -> Vector
unreal.ChaosRemovalEvent.mass() -> float
```

## `unreal.ChaosRemovalEventData(StructBase)`

```python
unreal.ChaosRemovalEventData.__init__(location: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, particle_index: int = 0) -> None
unreal.ChaosRemovalEventData.location(value: Vector) -> None
unreal.ChaosRemovalEventData.mass(value: float) -> None
unreal.ChaosRemovalEventData.particle_index(value: int) -> None
```

## `unreal.ChaosRemovalEventRequestSettings(StructBase)`

```python
unreal.ChaosRemovalEventRequestSettings.__init__(max_number_of_results: int = 0, min_mass: float = 0.000000, max_distance: float = 0.000000, sort_method: ChaosRemovalSortMethod = ChaosRemovalSortMethod.SORT_NONE) -> None
unreal.ChaosRemovalEventRequestSettings.max_distance(value: float) -> None
unreal.ChaosRemovalEventRequestSettings.max_number_of_results(value: int) -> None
unreal.ChaosRemovalEventRequestSettings.min_mass(value: float) -> None
unreal.ChaosRemovalEventRequestSettings.sort_method(value: ChaosRemovalSortMethod) -> None
```

## `unreal.ChaosSolverConfiguration(StructBase)`

```python
unreal.ChaosSolverConfiguration.__init__() -> None
```

## `unreal.ChaosTrailingEventData(StructBase)`

```python
unreal.ChaosTrailingEventData.__init__(location: Vector = [0.000000, 0.000000, 0.000000], velocity: Vector = [0.000000, 0.000000, 0.000000], angular_velocity: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, particle_index: int = 0) -> None
unreal.ChaosTrailingEventData.angular_velocity(value: Vector) -> None
unreal.ChaosTrailingEventData.location(value: Vector) -> None
unreal.ChaosTrailingEventData.mass(value: float) -> None
unreal.ChaosTrailingEventData.particle_index(value: int) -> None
unreal.ChaosTrailingEventData.velocity(value: Vector) -> None
```

## `unreal.ChaosTrailingEventRequestSettings(StructBase)`

```python
unreal.ChaosTrailingEventRequestSettings.__init__(max_number_of_results: int = 0, min_mass: float = 0.000000, min_speed: float = 0.000000, min_angular_speed: float = 0.000000, max_distance: float = 0.000000, sort_method: ChaosTrailingSortMethod = ChaosTrailingSortMethod.SORT_NONE) -> None
unreal.ChaosTrailingEventRequestSettings.max_distance(value: float) -> None
unreal.ChaosTrailingEventRequestSettings.max_number_of_results(value: int) -> None
unreal.ChaosTrailingEventRequestSettings.min_angular_speed(value: float) -> None
unreal.ChaosTrailingEventRequestSettings.min_mass(value: float) -> None
unreal.ChaosTrailingEventRequestSettings.min_speed(value: float) -> None
unreal.ChaosTrailingEventRequestSettings.sort_method(value: ChaosTrailingSortMethod) -> None
```

## `unreal.ChaosVDSkySphereInterface(Interface)`

```python
unreal.ChaosVDSkySphereInterface.refresh() -> None
unreal.ChaosVDSkySphereInterface.set_directional_light_source(new_light_source: DirectionalLight) -> None
```

## `unreal.ClosestPhysicsObjectResult(StructBase)`

```python
unreal.ClosestPhysicsObjectResult.__init__() -> None
```

## `unreal.CollisionChaosEvent(StructBase)`

```python
unreal.CollisionChaosEvent.__init__(location: Vector = [0.000000, 0.000000, 0.000000], accumulated_impulse: Vector = [0.000000, 0.000000, 0.000000], normal: Vector = [0.000000, 0.000000, 0.000000], penetration_depth: float = 0.000000, body1: CollisionChaosEventBodyInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 0.000000, None, None, 0, "None"], body2: CollisionChaosEventBodyInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 0.000000, None, None, 0, "None"]) -> None
unreal.CollisionChaosEvent.accumulated_impulse() -> Vector
unreal.CollisionChaosEvent.body1() -> CollisionChaosEventBodyInfo
unreal.CollisionChaosEvent.body2() -> CollisionChaosEventBodyInfo
unreal.CollisionChaosEvent.location() -> Vector
unreal.CollisionChaosEvent.normal() -> Vector
unreal.CollisionChaosEvent.penetration_depth() -> float
```

## `unreal.CollisionChaosEventBodyInfo(StructBase)`

```python
unreal.CollisionChaosEventBodyInfo.__init__(velocity: Vector = [0.000000, 0.000000, 0.000000], delta_velocity: Vector = [0.000000, 0.000000, 0.000000], angular_velocity: Vector = [0.000000, 0.000000, 0.000000], mass: float = 0.000000, phys_material: PhysicalMaterial = None, component: PrimitiveComponent = None, body_index: int = 0, bone_name: Name = "None") -> None
unreal.CollisionChaosEventBodyInfo.angular_velocity() -> Vector
unreal.CollisionChaosEventBodyInfo.body_index() -> int
unreal.CollisionChaosEventBodyInfo.bone_name() -> Name
unreal.CollisionChaosEventBodyInfo.component() -> PrimitiveComponent
unreal.CollisionChaosEventBodyInfo.delta_velocity() -> Vector
unreal.CollisionChaosEventBodyInfo.mass() -> float
unreal.CollisionChaosEventBodyInfo.phys_material() -> PhysicalMaterial
unreal.CollisionChaosEventBodyInfo.velocity() -> Vector
```

## `unreal.CollisionEventSignature(MulticastDelegateBase)`

```python
unreal.CollisionEventSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CollisionProfileName(StructBase)`

```python
unreal.CollisionProfileName.__init__(name: Name = "None") -> None
unreal.CollisionProfileName.name() -> Name
```

## `unreal.CollisionQueryTaskData(StructBase)`

```python
unreal.CollisionQueryTaskData.__init__(ignored_actors: Array[Actor] = []) -> None
unreal.CollisionQueryTaskData.ignored_actors(value: Array[Actor]) -> None
```

## `unreal.CollisionResponse(StructBase)`

```python
unreal.CollisionResponse.__init__() -> None
```

## `unreal.CollisionResponseContainer(StructBase)`

```python
unreal.CollisionResponseContainer.__init__(world_static: CollisionResponseType = CollisionResponseType.ECR_IGNORE, world_dynamic: CollisionResponseType = CollisionResponseType.ECR_IGNORE, pawn: CollisionResponseType = CollisionResponseType.ECR_IGNORE, visibility: CollisionResponseType = CollisionResponseType.ECR_IGNORE, camera: CollisionResponseType = CollisionResponseType.ECR_IGNORE, physics_body: CollisionResponseType = CollisionResponseType.ECR_IGNORE, vehicle: CollisionResponseType = CollisionResponseType.ECR_IGNORE, destructible: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel1: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel2: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel3: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel4: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel5: CollisionResponseType = CollisionResponseType.ECR_IGNORE, engine_trace_channel6: CollisionResponseType = CollisionResponseType.ECR_IGNORE, ecc_projectile: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel2: CollisionResponseType = CollisionResponseType.ECR_IGNORE, ecc_custom_api: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel4: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel5: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel6: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel7: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel8: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel9: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel10: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel11: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel12: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel13: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel14: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel15: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel16: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel17: CollisionResponseType = CollisionResponseType.ECR_IGNORE, game_trace_channel18: CollisionResponseType = CollisionResponseType.ECR_IGNORE) -> None
unreal.CollisionResponseContainer.camera() -> CollisionResponseType
unreal.CollisionResponseContainer.destructible() -> CollisionResponseType
unreal.CollisionResponseContainer.dynamic() -> CollisionResponseType
unreal.CollisionResponseContainer.ecc_custom_api() -> CollisionResponseType
unreal.CollisionResponseContainer.ecc_projectile() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel1() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel2() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel3() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel4() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel5() -> CollisionResponseType
unreal.CollisionResponseContainer.engine_trace_channel6() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel10() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel11() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel12() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel13() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel14() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel15() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel16() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel17() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel18() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel2() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel4() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel5() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel6() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel7() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel8() -> CollisionResponseType
unreal.CollisionResponseContainer.game_trace_channel9() -> CollisionResponseType
unreal.CollisionResponseContainer.pawn() -> CollisionResponseType
unreal.CollisionResponseContainer.physics_body() -> CollisionResponseType
unreal.CollisionResponseContainer.rigid_body() -> CollisionResponseType
unreal.CollisionResponseContainer.static() -> CollisionResponseType
unreal.CollisionResponseContainer.vehicle() -> CollisionResponseType
unreal.CollisionResponseContainer.visibility() -> CollisionResponseType
unreal.CollisionResponseContainer.world_dynamic() -> CollisionResponseType
unreal.CollisionResponseContainer.world_static() -> CollisionResponseType
```

## `unreal.ComponentCollisionSettingsChangedSignature(MulticastDelegateBase)`

```python
unreal.ComponentCollisionSettingsChangedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ComponentPhysicsStateChanged(MulticastDelegateBase)`

```python
unreal.ComponentPhysicsStateChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ConeConstraint(ConstraintBaseParams)`

```python
unreal.ConeConstraint.__init__() -> None
```

## `unreal.Constraint(StructBase)`

```python
unreal.Constraint.__init__() -> None
```

## `unreal.ConstraintBaseParams(StructBase)`

```python
unreal.ConstraintBaseParams.__init__() -> None
```

## `unreal.ConstraintBrokenSignature(MulticastDelegateBase)`

```python
unreal.ConstraintBrokenSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ConstraintDescription(StructBase)`

```python
unreal.ConstraintDescription.__init__(translation: bool = False, rotation: bool = False, scale: bool = False, parent: bool = False, translation_axes: FilterOptionPerAxis = [True, True, True], rotation_axes: FilterOptionPerAxis = [True, True, True], scale_axes: FilterOptionPerAxis = [True, True, True]) -> None
unreal.ConstraintDescription.parent(value: bool) -> None
unreal.ConstraintDescription.rotation(value: bool) -> None
unreal.ConstraintDescription.rotation_axes(value: FilterOptionPerAxis) -> None
unreal.ConstraintDescription.scale(value: bool) -> None
unreal.ConstraintDescription.scale_axes(value: FilterOptionPerAxis) -> None
unreal.ConstraintDescription.translation(value: bool) -> None
unreal.ConstraintDescription.translation_axes(value: FilterOptionPerAxis) -> None
```

## `unreal.ConstraintDrive(StructBase)`

```python
unreal.ConstraintDrive.__init__() -> None
```

## `unreal.ConstraintInstance(ConstraintInstanceBase)`

```python
unreal.ConstraintInstance.__init__() -> None
```

## `unreal.ConstraintInstanceAccessor(StructBase)`

```python
unreal.ConstraintInstanceAccessor.__init__() -> None
```

## `unreal.ConstraintInstanceBase(StructBase)`

```python
unreal.ConstraintInstanceBase.__init__() -> None
```

## `unreal.ConstraintParent(StructBase)`

```python
unreal.ConstraintParent.__init__(item: RigElementKey = [RigElementType.NONE, "None"], weight: float = 0.000000) -> None
unreal.ConstraintParent.item(value: RigElementKey) -> None
unreal.ConstraintParent.weight(value: float) -> None
```

## `unreal.ConstraintProfileProperties(StructBase)`

```python
unreal.ConstraintProfileProperties.__init__() -> None
```

## `unreal.ConstraintTarget(StructBase)`

```python
unreal.ConstraintTarget.__init__(filter: TransformFilter = [[True, True, True], [True, True, True], [True, True, True]]) -> None
unreal.ConstraintTarget.filter() -> TransformFilter
```

## `unreal.ConstraintsManager(Object)`

```python
unreal.ConstraintsManager.on_constraint_added_bp(value: OnConstraintAdded) -> None
unreal.ConstraintsManager.on_constraint_removed_bp(value: OnConstraintRemoved) -> None
```

## `unreal.ConstraintsManager_OnConstraintAdded(MulticastDelegateBase)`

```python
unreal.ConstraintsManager_OnConstraintAdded.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ConstraintsManager_OnConstraintRemoved(MulticastDelegateBase)`

```python
unreal.ConstraintsManager_OnConstraintRemoved.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ConstraintsScriptingLibrary(BlueprintFunctionLibrary)`

```python
unreal.ConstraintsScriptingLibrary.add_constraint(world: World, parent_handle: TransformableHandle, child_handle: TransformableHandle, constraint: TickableTransformConstraint, maintain_offset: bool) -> bool
unreal.ConstraintsScriptingLibrary.create_from_type(world: World, type: TransformConstraintType) -> TickableTransformConstraint
unreal.ConstraintsScriptingLibrary.create_transformable_component_handle(world: World, scene_component: SceneComponent, socket_name: Name) -> TransformableComponentHandle
unreal.ConstraintsScriptingLibrary.create_transformable_handle(world: World, object: Object, attachment_name: Name = "None") -> TransformableHandle
unreal.ConstraintsScriptingLibrary.get_constraints_array(world: World) -> Array[TickableConstraint]
unreal.ConstraintsScriptingLibrary.remove_constraint(world: World, index: int) -> bool
unreal.ConstraintsScriptingLibrary.remove_this_constraint(world: World, tickable_constraint: TickableConstraint) -> bool
```

## `unreal.DamageEvent(StructBase)`

```python
unreal.DamageEvent.__init__() -> None
```

## `unreal.DamageType(Object)`

```python
unreal.DamageType.caused_by_world() -> bool
unreal.DamageType.damage_falloff() -> float
unreal.DamageType.damage_impulse() -> float
unreal.DamageType.destructible_damage_spread_scale() -> float
unreal.DamageType.destructible_impulse() -> float
unreal.DamageType.radial_damage_vel_change() -> bool
unreal.DamageType.scale_momentum_by_mass() -> bool
```

## `unreal.DataflowPhysicsSolverProxy(DataflowSimulationProxy)`

```python
unreal.DataflowPhysicsSolverProxy.__init__() -> None
```

## `unreal.EarthCollisionComponent(EarthCollisionComponentBase)`

```python
unreal.EarthCollisionComponent.index_buffer(value: Array[int]) -> None
unreal.EarthCollisionComponent.local_bounds(value: BoxSphereBounds) -> None
unreal.EarthCollisionComponent.override_wireframe_color() -> bool
unreal.EarthCollisionComponent.use_async_cook() -> bool
unreal.EarthCollisionComponent.vertex_buffer(value: Array[Vector3f]) -> None
unreal.EarthCollisionComponent.wireframe_color_override() -> Color
```

## `unreal.EarthCollisionData(StructBase)`

```python
unreal.EarthCollisionData.__init__(vertex_buffer: Array[Vector3f] = [], index_buffer: Array[int] = [], bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False]) -> None
unreal.EarthCollisionData.bounds(value: Box) -> None
unreal.EarthCollisionData.index_buffer(value: Array[int]) -> None
unreal.EarthCollisionData.vertex_buffer(value: Array[Vector3f]) -> None
```

## `unreal.EarthCollisionFragment(EarthOutputFragment)`

```python
unreal.EarthCollisionFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, collision_type: EarthCollisionType = EarthCollisionType.NONE, complex_collision: bool = False, has_cap: bool = False, component_class: Class = None, vertex_buffer: Array[Vector3f] = [], index_buffer: Array[int] = [], bounds_fragment: EarthBoundsFragment = [False, [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], False, False], tag_fragment: EarthTagFragment = [[], False, False]) -> None
unreal.EarthCollisionFragment.bounds_fragment(value: EarthBoundsFragment) -> None
unreal.EarthCollisionFragment.collision_type(value: EarthCollisionType) -> None
unreal.EarthCollisionFragment.complex_collision(value: bool) -> None
unreal.EarthCollisionFragment.component_class(value: Class) -> None
unreal.EarthCollisionFragment.has_cap(value: bool) -> None
unreal.EarthCollisionFragment.index_buffer(value: Array[int]) -> None
unreal.EarthCollisionFragment.tag_fragment(value: EarthTagFragment) -> None
unreal.EarthCollisionFragment.vertex_buffer(value: Array[Vector3f]) -> None
```

## `unreal.FBIKConstraintOption(StructBase)`

```python
unreal.FBIKConstraintOption.__init__(item: RigElementKey = [RigElementType.NONE, "None"]) -> None
unreal.FBIKConstraintOption.item() -> RigElementKey
```

## `unreal.GeometryCollectionCollisionParticleData(StructBase)`

```python
unreal.GeometryCollectionCollisionParticleData.__init__() -> None
```

## `unreal.GeometryCollectionCollisionTypeData(StructBase)`

```python
unreal.GeometryCollectionCollisionTypeData.__init__() -> None
```

## `unreal.GeometryCollectionComponent_NotifyGeometryCollectionPhysicsLoadingStateChange(MulticastDelegateBase)`

```python
unreal.GeometryCollectionComponent_NotifyGeometryCollectionPhysicsLoadingStateChange.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GeometryCollectionComponent_NotifyGeometryCollectionPhysicsStateChange(MulticastDelegateBase)`

```python
unreal.GeometryCollectionComponent_NotifyGeometryCollectionPhysicsStateChange.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GeometryCollectionDamagePropagationData(StructBase)`

```python
unreal.GeometryCollectionDamagePropagationData.__init__(enabled: bool = False, break_damage_propagation_factor: float = 0.000000, shock_damage_propagation_factor: float = 0.000000) -> None
unreal.GeometryCollectionDamagePropagationData.break_damage_propagation_factor(value: float) -> None
unreal.GeometryCollectionDamagePropagationData.enabled(value: bool) -> None
unreal.GeometryCollectionDamagePropagationData.shock_damage_propagation_factor(value: float) -> None
```

## `unreal.GeometryScriptCollisionFromMeshOptions(StructBase)`

```python
unreal.GeometryScriptCollisionFromMeshOptions.__init__(emit_transaction: bool = False, method: GeometryScriptCollisionGenerationMethod = GeometryScriptCollisionGenerationMethod.ALIGNED_BOXES, auto_detect_spheres: bool = False, auto_detect_boxes: bool = False, auto_detect_capsules: bool = False, min_thickness: float = 0.000000, simplify_hulls: bool = False, convex_hull_target_face_count: int = 0, max_convex_hulls_per_mesh: int = 0, convex_decomposition_search_factor: float = 0.000000, convex_decomposition_error_tolerance: float = 0.000000, convex_decomposition_min_part_thickness: float = 0.000000, swept_hull_simplify_tolerance: float = 0.000000, swept_hull_axis: GeometryScriptSweptHullAxis = GeometryScriptSweptHullAxis.X, remove_fully_contained_shapes: bool = False, max_shape_count: int = 0) -> None
unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_boxes(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_capsules(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_spheres(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_error_tolerance(value: float) -> None
unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_min_part_thickness(value: float) -> None
unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_search_factor(value: float) -> None
unreal.GeometryScriptCollisionFromMeshOptions.convex_hull_target_face_count(value: int) -> None
unreal.GeometryScriptCollisionFromMeshOptions.emit_transaction(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.max_convex_hulls_per_mesh(value: int) -> None
unreal.GeometryScriptCollisionFromMeshOptions.max_shape_count(value: int) -> None
unreal.GeometryScriptCollisionFromMeshOptions.method(value: GeometryScriptCollisionGenerationMethod) -> None
unreal.GeometryScriptCollisionFromMeshOptions.min_thickness(value: float) -> None
unreal.GeometryScriptCollisionFromMeshOptions.remove_fully_contained_shapes(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.simplify_hulls(value: bool) -> None
unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_axis(value: GeometryScriptSweptHullAxis) -> None
unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_simplify_tolerance(value: float) -> None
```

## `unreal.GeometryScriptMergeSimpleCollisionOptions(StructBase)`

```python
unreal.GeometryScriptMergeSimpleCollisionOptions.__init__(max_shape_count: int = 0, error_tolerance: float = 0.000000, min_thickness_tolerance: float = 0.000000, consider_all_possible_merges: bool = False, precomputed_negative_space: GeometryScriptSphereCovering = [], compute_negative_space: bool = False, compute_negative_space_options: ComputeNegativeSpaceOptions = [NegativeSpaceSampleMethod.UNIFORM, False, False, 128, 50, 1.000000, 2.000000, 10.000000], shape_to_hull_triangulation: GeometryScriptSimpleCollisionTriangulationOptions = [4, 5, 8, False]) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space(value: bool) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space_options(value: ComputeNegativeSpaceOptions) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.consider_all_possible_merges(value: bool) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.error_tolerance(value: float) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.max_shape_count(value: int) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.min_thickness_tolerance(value: float) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.precomputed_negative_space(value: GeometryScriptSphereCovering) -> None
unreal.GeometryScriptMergeSimpleCollisionOptions.shape_to_hull_triangulation(value: GeometryScriptSimpleCollisionTriangulationOptions) -> None
```

## `unreal.GeometryScriptSetSimpleCollisionOptions(StructBase)`

```python
unreal.GeometryScriptSetSimpleCollisionOptions.__init__(emit_transaction: bool = False) -> None
unreal.GeometryScriptSetSimpleCollisionOptions.emit_transaction(value: bool) -> None
```

## `unreal.GeometryScriptSimpleCollision(StructBase)`

```python
unreal.GeometryScriptSimpleCollision.__init__() -> None
unreal.GeometryScriptSimpleCollision.approximate_convex_hulls_with_simpler_collision_shapes(approximate_options: GeometryScriptConvexHullApproximationOptions, debug: GeometryScriptDebug = None) -> bool
unreal.GeometryScriptSimpleCollision.combine_simple_collision(append_collision: GeometryScriptSimpleCollision, debug: GeometryScriptDebug = None) -> None
unreal.GeometryScriptSimpleCollision.get_simple_collision_shape_count() -> int
unreal.GeometryScriptSimpleCollision.simplify_convex_hulls(simplify_options: GeometryScriptConvexHullSimplificationOptions, debug: GeometryScriptDebug = None) -> bool
```

## `unreal.GeometryScriptSimpleCollisionTriangulationOptions(StructBase)`

```python
unreal.GeometryScriptSimpleCollisionTriangulationOptions.__init__(sphere_steps_per_side: int = 0, capsule_hemisphere_steps: int = 0, capsule_circle_steps: int = 0, approximate_level_sets_with_cubes: bool = False) -> None
unreal.GeometryScriptSimpleCollisionTriangulationOptions.approximate_level_sets_with_cubes(value: bool) -> None
unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_circle_steps(value: int) -> None
unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_hemisphere_steps(value: int) -> None
unreal.GeometryScriptSimpleCollisionTriangulationOptions.sphere_steps_per_side(value: int) -> None
```

## `unreal.GeometryScript_Collision(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Collision.approximate_convex_hulls_with_simpler_collision_shapes(simple_collision: GeometryScriptSimpleCollision, approximate_options: GeometryScriptConvexHullApproximationOptions, debug: GeometryScriptDebug = None) -> Tuple[GeometryScriptSimpleCollision, bool]
unreal.GeometryScript_Collision.combine_simple_collision(collision_to_update: GeometryScriptSimpleCollision, append_collision: GeometryScriptSimpleCollision, debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.combine_simple_collision_array(simple_collision_array: Array[GeometryScriptSimpleCollision], debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.compute_navigable_convex_decomposition(target_mesh: DynamicMesh, options: NavigableConvexDecompositionOptions, debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.compute_negative_space(mesh_bvh: GeometryScriptDynamicMeshBVH, negative_space_options: ComputeNegativeSpaceOptions, debug: GeometryScriptDebug = None) -> GeometryScriptSphereCovering
unreal.GeometryScript_Collision.conv_geometry_script_sphere_covering_to_sphere_array(sphere_covering: GeometryScriptSphereCovering) -> Array[Sphere]
unreal.GeometryScript_Collision.conv_sphere_array_to_geometry_script_sphere_covering(spheres: Array[Sphere]) -> GeometryScriptSphereCovering
unreal.GeometryScript_Collision.generate_collision_from_mesh(from_dynamic_mesh: DynamicMesh, options: GeometryScriptCollisionFromMeshOptions, debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.get_simple_collision_from_component(component: PrimitiveComponent, debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.get_simple_collision_from_static_mesh(static_mesh: StaticMesh, debug: GeometryScriptDebug = None) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.get_simple_collision_shape_count(simple_collision: GeometryScriptSimpleCollision) -> int
unreal.GeometryScript_Collision.merge_simple_collision_shapes(simple_collision: GeometryScriptSimpleCollision, merge_options: GeometryScriptMergeSimpleCollisionOptions, debug: GeometryScriptDebug = None) -> Tuple[GeometryScriptSimpleCollision, bool]
unreal.GeometryScript_Collision.reset_dynamic_mesh_collision(component: DynamicMeshComponent, emit_transaction: bool = False, debug: GeometryScriptDebug = None) -> None
unreal.GeometryScript_Collision.reset_simple_collision(simple_collision: GeometryScriptSimpleCollision) -> GeometryScriptSimpleCollision
unreal.GeometryScript_Collision.set_dynamic_mesh_collision_from_mesh(from_dynamic_mesh: DynamicMesh, to_dynamic_mesh_component: DynamicMeshComponent, options: GeometryScriptCollisionFromMeshOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Collision.set_simple_collision_of_dynamic_mesh_component(simple_collision: GeometryScriptSimpleCollision, dynamic_mesh_component: DynamicMeshComponent, options: GeometryScriptSetSimpleCollisionOptions, debug: GeometryScriptDebug = None) -> None
unreal.GeometryScript_Collision.set_simple_collision_of_static_mesh(simple_collision: GeometryScriptSimpleCollision, static_mesh: StaticMesh, options: GeometryScriptSetSimpleCollisionOptions, static_mesh_collision_options: GeometryScriptSetStaticMeshCollisionOptions = [True], debug: GeometryScriptDebug = None) -> None
unreal.GeometryScript_Collision.set_static_mesh_collision_from_component(static_mesh_asset: StaticMesh, source_component: PrimitiveComponent, options: GeometryScriptSetSimpleCollisionOptions = [True], static_mesh_collision_options: GeometryScriptSetStaticMeshCollisionOptions = [True], debug: GeometryScriptDebug = None) -> None
unreal.GeometryScript_Collision.set_static_mesh_collision_from_mesh(from_dynamic_mesh: DynamicMesh, to_static_mesh_asset: StaticMesh, options: GeometryScriptCollisionFromMeshOptions, static_mesh_collision_options: GeometryScriptSetStaticMeshCollisionOptions = [True], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Collision.set_static_mesh_custom_complex_collision(static_mesh_asset: StaticMesh, static_mesh_collision_asset: StaticMesh, emit_transaction: bool, mark_collision_as_customized: bool = True, debug: GeometryScriptDebug = None) -> bool
unreal.GeometryScript_Collision.simplify_convex_hulls(simple_collision: GeometryScriptSimpleCollision, simplify_options: GeometryScriptConvexHullSimplificationOptions, debug: GeometryScriptDebug = None) -> Tuple[GeometryScriptSimpleCollision, bool]
unreal.GeometryScript_Collision.static_mesh_has_customized_collision(static_mesh_asset: StaticMesh) -> bool
unreal.GeometryScript_Collision.transform_simple_collision_shapes(simple_collision: GeometryScriptSimpleCollision, transform: Transform, transform_options: GeometryScriptTransformCollisionOptions, debug: GeometryScriptDebug = None) -> Tuple[GeometryScriptSimpleCollision, bool]
```

## `unreal.HairBendConstraint(StructBase)`

```python
unreal.HairBendConstraint.__init__() -> None
```

## `unreal.HairCollisionConstraint(StructBase)`

```python
unreal.HairCollisionConstraint.__init__() -> None
```

## `unreal.HairGroupsPhysics(StructBase)`

```python
unreal.HairGroupsPhysics.__init__() -> None
```

## `unreal.HairSimulationConstraints(StructBase)`

```python
unreal.HairSimulationConstraints.__init__(bend_damping: float = 0.000000, bend_stiffness: float = 0.000000, stretch_damping: float = 0.000000, stretch_stiffness: float = 0.000000, static_friction: float = 0.000000, kinetic_friction: float = 0.000000, strands_viscosity: float = 0.000000, collision_radius: float = 0.000000) -> None
unreal.HairSimulationConstraints.bend_damping(value: float) -> None
unreal.HairSimulationConstraints.bend_stiffness(value: float) -> None
unreal.HairSimulationConstraints.collision_radius(value: float) -> None
unreal.HairSimulationConstraints.kinetic_friction(value: float) -> None
unreal.HairSimulationConstraints.static_friction(value: float) -> None
unreal.HairSimulationConstraints.strands_viscosity(value: float) -> None
unreal.HairSimulationConstraints.stretch_damping(value: float) -> None
unreal.HairSimulationConstraints.stretch_stiffness(value: float) -> None
```

## `unreal.HairStretchConstraint(StructBase)`

```python
unreal.HairStretchConstraint.__init__() -> None
```

## `unreal.InstancePointDamageSignature(MulticastDelegateBase)`

```python
unreal.InstancePointDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InstanceRadialDamageSignature(MulticastDelegateBase)`

```python
unreal.InstanceRadialDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InstigatedAnyDamageSignature(MulticastDelegateBase)`

```python
unreal.InstigatedAnyDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.LandscapeHeightfieldCollisionComponent(PrimitiveComponent)`

```python
unreal.LandscapeHeightfieldCollisionComponent.get_render_component() -> LandscapeComponent
```

## `unreal.LinearConstraint(ConstraintBaseParams)`

```python
unreal.LinearConstraint.__init__() -> None
```

## `unreal.LinearDriveConstraint(StructBase)`

```python
unreal.LinearDriveConstraint.__init__() -> None
unreal.LinearDriveConstraint.enable_position_drive(value: bool) -> None
```

## `unreal.MovieScene3DConstraintSection(MovieSceneSection)`

```python
unreal.MovieScene3DConstraintSection.get_constraint_binding_id() -> MovieSceneObjectBindingID
unreal.MovieScene3DConstraintSection.set_constraint_binding_id(constraint_binding_id: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneChaosCacheParams(MovieSceneBaseCacheParams)`

```python
unreal.MovieSceneChaosCacheParams.__init__() -> None
```

## `unreal.NetworkPhysicsSettings(StructBase)`

```python
unreal.NetworkPhysicsSettings.__init__() -> None
```

## `unreal.NetworkPhysicsSettingsDefaultReplication(StructBase)`

```python
unreal.NetworkPhysicsSettingsDefaultReplication.__init__() -> None
```

## `unreal.NetworkPhysicsSettingsNetworkPhysicsComponent(StructBase)`

```python
unreal.NetworkPhysicsSettingsNetworkPhysicsComponent.__init__() -> None
```

## `unreal.NetworkPhysicsSettingsPredictiveInterpolation(StructBase)`

```python
unreal.NetworkPhysicsSettingsPredictiveInterpolation.__init__() -> None
```

## `unreal.NetworkPhysicsSettingsResimulation(StructBase)`

```python
unreal.NetworkPhysicsSettingsResimulation.__init__() -> None
```

## `unreal.OnChaosBreakEvent(MulticastDelegateBase)`

```python
unreal.OnChaosBreakEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosBreakingEvents(MulticastDelegateBase)`

```python
unreal.OnChaosBreakingEvents.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosCollisionEvents(MulticastDelegateBase)`

```python
unreal.OnChaosCollisionEvents.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosCrumblingEvent(MulticastDelegateBase)`

```python
unreal.OnChaosCrumblingEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosPhysicsCollision(MulticastDelegateBase)`

```python
unreal.OnChaosPhysicsCollision.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosRemovalEvent(MulticastDelegateBase)`

```python
unreal.OnChaosRemovalEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosRemovalEvents(MulticastDelegateBase)`

```python
unreal.OnChaosRemovalEvents.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnChaosTrailingEvents(MulticastDelegateBase)`

```python
unreal.OnChaosTrailingEvents.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PCGCollisionShapeData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGCollisionShapeData.transform() -> Transform
```

## `unreal.PCGCreateCollisionDataSettings(PCGSettings)`

```python
unreal.PCGCreateCollisionDataSettings.collision_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGCreateCollisionDataSettings.collision_query_flag(value: PCGCollisionQueryFlag) -> None
unreal.PCGCreateCollisionDataSettings.synchronous_load(value: bool) -> None
unreal.PCGCreateCollisionDataSettings.warn_if_attribute_could_not_be_used(value: bool) -> None
```

## `unreal.ParticleCollisionSignature(MulticastDelegateBase)`

```python
unreal.ParticleCollisionSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PhysicsAsset(Object)`

```python
unreal.PhysicsAsset.get_constraint_by_bone_names(bone1_name: Name, bone2_name: Name) -> ConstraintInstanceAccessor
unreal.PhysicsAsset.get_constraint_by_name(constraint_name: Name) -> ConstraintInstanceAccessor
unreal.PhysicsAsset.get_constraints(includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
```

## `unreal.PhysicsAssetSolverSettings(StructBase)`

```python
unreal.PhysicsAssetSolverSettings.__init__(position_iterations: int = 0, velocity_iterations: int = 0, projection_iterations: int = 0, cull_distance: float = 0.000000, max_depenetration_velocity: float = 0.000000, fixed_time_step: float = 0.000000, use_linear_joint_solver: bool = False, use_manifolds: bool = False) -> None
unreal.PhysicsAssetSolverSettings.cull_distance(value: float) -> None
unreal.PhysicsAssetSolverSettings.fixed_time_step(value: float) -> None
unreal.PhysicsAssetSolverSettings.max_depenetration_velocity(value: float) -> None
unreal.PhysicsAssetSolverSettings.position_iterations(value: int) -> None
unreal.PhysicsAssetSolverSettings.projection_iterations(value: int) -> None
unreal.PhysicsAssetSolverSettings.use_linear_joint_solver(value: bool) -> None
unreal.PhysicsAssetSolverSettings.use_manifolds(value: bool) -> None
unreal.PhysicsAssetSolverSettings.velocity_iterations(value: int) -> None
```

## `unreal.PhysicsCollisionHandler(Object)`

```python
unreal.PhysicsCollisionHandler.default_impact_sound(value: SoundBase) -> None
unreal.PhysicsCollisionHandler.impact_re_fire_delay(value: float) -> None
unreal.PhysicsCollisionHandler.impact_threshold(value: float) -> None
```

## `unreal.PhysicsConstraintComponent(SceneComponent)`

```python
unreal.PhysicsConstraintComponent.break_constraint() -> None
unreal.PhysicsConstraintComponent.get_constrained_components() -> Tuple[PrimitiveComponent, Name, PrimitiveComponent, Name]
unreal.PhysicsConstraintComponent.get_constraint() -> ConstraintInstanceAccessor
unreal.PhysicsConstraintComponent.get_constraint_force() -> Tuple[Vector, Vector]
unreal.PhysicsConstraintComponent.get_current_swing1() -> float
unreal.PhysicsConstraintComponent.get_current_swing2() -> float
unreal.PhysicsConstraintComponent.get_current_twist() -> float
unreal.PhysicsConstraintComponent.is_broken() -> bool
unreal.PhysicsConstraintComponent.is_projection_enabled() -> bool
unreal.PhysicsConstraintComponent.on_constraint_broken(value: ConstraintBrokenSignature) -> None
unreal.PhysicsConstraintComponent.on_plastic_deformation(value: PlasticDeformationEventSignature) -> None
unreal.PhysicsConstraintComponent.set_angular_breakable(angular_breakable: bool, angular_break_threshold: float) -> None
unreal.PhysicsConstraintComponent.set_angular_drive_acceleration_mode(acceleration_mode: bool) -> None
unreal.PhysicsConstraintComponent.set_angular_drive_mode(drive_mode: AngularDriveMode) -> None
unreal.PhysicsConstraintComponent.set_angular_drive_params(position_strength: float, velocity_strength: float, force_limit: float) -> None
unreal.PhysicsConstraintComponent.set_angular_orientation_drive(enable_swing_drive: bool, enable_twist_drive: bool) -> None
unreal.PhysicsConstraintComponent.set_angular_orientation_target(pos_target: Rotator) -> None
unreal.PhysicsConstraintComponent.set_angular_plasticity(angular_plasticity: bool, angular_plasticity_threshold: float) -> None
unreal.PhysicsConstraintComponent.set_angular_swing1_limit(motion_type: AngularConstraintMotion, swing1_limit_angle: float) -> None
unreal.PhysicsConstraintComponent.set_angular_swing2_limit(motion_type: AngularConstraintMotion, swing2_limit_angle: float) -> None
unreal.PhysicsConstraintComponent.set_angular_twist_limit(constraint_type: AngularConstraintMotion, twist_limit_angle: float) -> None
unreal.PhysicsConstraintComponent.set_angular_velocity_drive(enable_swing_drive: bool, enable_twist_drive: bool) -> None
unreal.PhysicsConstraintComponent.set_angular_velocity_drive_slerp(enable_slerp: bool) -> None
unreal.PhysicsConstraintComponent.set_angular_velocity_drive_twist_and_swing(enable_twist_drive: bool, enable_swing_drive: bool) -> None
unreal.PhysicsConstraintComponent.set_angular_velocity_target(vel_target: Vector) -> None
unreal.PhysicsConstraintComponent.set_constrained_components(component1: PrimitiveComponent, bone_name1: Name, component2: PrimitiveComponent, bone_name2: Name) -> None
unreal.PhysicsConstraintComponent.set_constraint_reference_frame(frame: ConstraintFrame, ref_frame: Transform) -> None
unreal.PhysicsConstraintComponent.set_constraint_reference_orientation(frame: ConstraintFrame, pri_axis: Vector, sec_axis: Vector) -> None
unreal.PhysicsConstraintComponent.set_constraint_reference_position(frame: ConstraintFrame, ref_position: Vector) -> None
unreal.PhysicsConstraintComponent.set_contact_transfer_scale(contact_transfer_scale: float) -> None
unreal.PhysicsConstraintComponent.set_disable_collision(disable_collision: bool) -> None
unreal.PhysicsConstraintComponent.set_linear_breakable(linear_breakable: bool, linear_break_threshold: float) -> None
unreal.PhysicsConstraintComponent.set_linear_drive_acceleration_mode(acceleration_mode: bool) -> None
unreal.PhysicsConstraintComponent.set_linear_drive_params(position_strength: float, velocity_strength: float, force_limit: float) -> None
unreal.PhysicsConstraintComponent.set_linear_plasticity(linear_plasticity: bool, linear_plasticity_threshold: float, plasticity_type: ConstraintPlasticityType) -> None
unreal.PhysicsConstraintComponent.set_linear_position_drive(enable_drive_x: bool, enable_drive_y: bool, enable_drive_z: bool) -> None
unreal.PhysicsConstraintComponent.set_linear_position_target(pos_target: Vector) -> None
unreal.PhysicsConstraintComponent.set_linear_velocity_drive(enable_drive_x: bool, enable_drive_y: bool, enable_drive_z: bool) -> None
unreal.PhysicsConstraintComponent.set_linear_velocity_target(vel_target: Vector) -> None
unreal.PhysicsConstraintComponent.set_linear_x_limit(constraint_type: LinearConstraintMotion, limit_size: float) -> None
unreal.PhysicsConstraintComponent.set_linear_y_limit(constraint_type: LinearConstraintMotion, limit_size: float) -> None
unreal.PhysicsConstraintComponent.set_linear_z_limit(constraint_type: LinearConstraintMotion, limit_size: float) -> None
unreal.PhysicsConstraintComponent.set_orientation_drive_slerp(enable_slerp: bool) -> None
unreal.PhysicsConstraintComponent.set_orientation_drive_twist_and_swing(enable_twist_drive: bool, enable_swing_drive: bool) -> None
unreal.PhysicsConstraintComponent.set_projection_enabled(projection_enabled: bool) -> None
unreal.PhysicsConstraintComponent.set_projection_params(projection_linear_alpha: float, projection_angular_alpha: float, projection_linear_tolerance: float, projection_angular_tolerance: float) -> None
```

## `unreal.PhysicsFieldStatics(BlueprintFunctionLibrary)`

```python
unreal.PhysicsFieldStatics.eval_physics_integer_field(world_context_object: Object, world_position: Vector, integer_type: FieldIntegerType) -> int
unreal.PhysicsFieldStatics.eval_physics_scalar_field(world_context_object: Object, world_position: Vector, scalar_type: FieldScalarType) -> float
unreal.PhysicsFieldStatics.eval_physics_vector_field(world_context_object: Object, world_position: Vector, vector_type: FieldVectorType) -> Vector
```

## `unreal.PhysicsHandleComponent(ActorComponent)`

```python
unreal.PhysicsHandleComponent.angular_damping() -> float
unreal.PhysicsHandleComponent.angular_stiffness() -> float
unreal.PhysicsHandleComponent.get_grabbed_component() -> PrimitiveComponent
unreal.PhysicsHandleComponent.get_target_location_and_rotation() -> Tuple[Vector, Rotator]
unreal.PhysicsHandleComponent.grab_component(component: PrimitiveComponent, bone_name: Name, grab_location: Vector, constrain_rotation: bool) -> None
unreal.PhysicsHandleComponent.grab_component_at_location(component: PrimitiveComponent, bone_name: Name, grab_location: Vector) -> None
unreal.PhysicsHandleComponent.grab_component_at_location_with_rotation(component: PrimitiveComponent, bone_name: Name, location: Vector, rotation: Rotator) -> None
unreal.PhysicsHandleComponent.interpolate_target(value: bool) -> None
unreal.PhysicsHandleComponent.interpolation_speed() -> float
unreal.PhysicsHandleComponent.linear_damping() -> float
unreal.PhysicsHandleComponent.linear_stiffness() -> float
unreal.PhysicsHandleComponent.release_component() -> None
unreal.PhysicsHandleComponent.set_angular_damping(new_angular_damping: float) -> None
unreal.PhysicsHandleComponent.set_angular_stiffness(new_angular_stiffness: float) -> None
unreal.PhysicsHandleComponent.set_interpolation_speed(new_interpolation_speed: float) -> None
unreal.PhysicsHandleComponent.set_linear_damping(new_linear_damping: float) -> None
unreal.PhysicsHandleComponent.set_linear_stiffness(new_linear_stiffness: float) -> None
unreal.PhysicsHandleComponent.set_target_location(new_location: Vector) -> None
unreal.PhysicsHandleComponent.set_target_location_and_rotation(new_location: Vector, new_rotation: Rotator) -> None
unreal.PhysicsHandleComponent.set_target_rotation(new_rotation: Rotator) -> None
unreal.PhysicsHandleComponent.soft_angular_constraint() -> bool
unreal.PhysicsHandleComponent.soft_linear_constraint() -> bool
```

## `unreal.PhysicsPredictionSettings(StructBase)`

```python
unreal.PhysicsPredictionSettings.__init__() -> None
```

## `unreal.PhysicsReplicationResimulationSettings(StructBase)`

```python
unreal.PhysicsReplicationResimulationSettings.__init__() -> None
```

## `unreal.PhysicsSettings(PhysicsSettingsCore)`

```python
unreal.PhysicsSettings.get_physics_history_count() -> int
```

## `unreal.PhysicsSpringComponent(SceneComponent)`

```python
unreal.PhysicsSpringComponent.get_normalized_compression_scalar() -> float
unreal.PhysicsSpringComponent.get_spring_current_end_point() -> Vector
unreal.PhysicsSpringComponent.get_spring_direction() -> Vector
unreal.PhysicsSpringComponent.get_spring_resting_point() -> Vector
unreal.PhysicsSpringComponent.ignore_self(value: bool) -> None
unreal.PhysicsSpringComponent.spring_channel(value: CollisionChannel) -> None
unreal.PhysicsSpringComponent.spring_compression() -> float
unreal.PhysicsSpringComponent.spring_damping(value: float) -> None
unreal.PhysicsSpringComponent.spring_length_at_rest(value: float) -> None
unreal.PhysicsSpringComponent.spring_radius(value: float) -> None
unreal.PhysicsSpringComponent.spring_stiffness(value: float) -> None
```

## `unreal.PhysicsThreadLibrary(BlueprintFunctionLibrary)`

```python
unreal.PhysicsThreadLibrary.add_force(handle: BodyInstanceAsyncPhysicsTickHandle, force: Vector, accel_change: bool = False) -> None
```

## `unreal.PhysicsThruster(RigidBodyBase)`

```python
unreal.PhysicsThruster.thruster_component() -> PhysicsThrusterComponent
```

## `unreal.PhysicsThrusterComponent(SceneComponent)`

```python
unreal.PhysicsThrusterComponent.thrust_strength(value: float) -> None
```

## `unreal.PhysicsVolume(Volume)`

```python
unreal.PhysicsVolume.fluid_friction(value: float) -> None
unreal.PhysicsVolume.physics_on_contact(value: bool) -> None
unreal.PhysicsVolume.priority(value: int) -> None
unreal.PhysicsVolume.terminal_velocity(value: float) -> None
unreal.PhysicsVolume.water_volume(value: bool) -> None
```

## `unreal.PhysicsVolumeChanged(MulticastDelegateBase)`

```python
unreal.PhysicsVolumeChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PointDamageEvent(DamageEvent)`

```python
unreal.PointDamageEvent.__init__() -> None
```

## `unreal.PyTestStructDelegate_OnNameCollisionDelegate(MulticastDelegateBase)`

```python
unreal.PyTestStructDelegate_OnNameCollisionDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PyTestVectorDelegate_OnNameCollisionDelegate(MulticastDelegateBase)`

```python
unreal.PyTestVectorDelegate_OnNameCollisionDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PythonPhysicsAssetLib(BlueprintFunctionLibrary)`

```python
unreal.PythonPhysicsAssetLib.add_constraints(physics_asset: PhysicsAsset, parent_body_index: int, child_bodies_indexes: Array[int]) -> Array[Name]
unreal.PythonPhysicsAssetLib.break_constraint_accessor(accessor: ConstraintInstanceAccessor) -> Optional[Tuple[Object, int]]
unreal.PythonPhysicsAssetLib.get_bodies_from_bone(physics_asset: PhysicsAsset, bone_index: int) -> Array[int]
unreal.PythonPhysicsAssetLib.get_bodies_hierarchy(physics_asset: PhysicsAsset) -> Tuple[Array[Name], Array[int]]
unreal.PythonPhysicsAssetLib.get_bodies_rotations(physics_asset: PhysicsAsset, body_index: int) -> Optional[Array[Rotator]]
unreal.PythonPhysicsAssetLib.get_body_center(physics_asset: PhysicsAsset, body_index: int) -> Optional[Vector]
unreal.PythonPhysicsAssetLib.get_body_length(physics_asset: PhysicsAsset, body_index: int) -> Optional[float]
unreal.PythonPhysicsAssetLib.get_body_radius(physics_asset: PhysicsAsset, body_index: int) -> Optional[float]
unreal.PythonPhysicsAssetLib.get_body_rotation(physics_asset: PhysicsAsset, body_index: int) -> Optional[Rotator]
unreal.PythonPhysicsAssetLib.get_body_size(physics_asset: PhysicsAsset, body_index: int) -> Optional[Vector]
unreal.PythonPhysicsAssetLib.get_bone_index_from_body(physics_asset: PhysicsAsset, body_index: int) -> int
unreal.PythonPhysicsAssetLib.get_bone_indexes_of_constraint(physics_asset: PhysicsAsset, constraint_index: int) -> Tuple[int, int]
unreal.PythonPhysicsAssetLib.get_constraint_instance_accessor(physics_asset: PhysicsAsset, constraint_index: int) -> ConstraintInstanceAccessor
unreal.PythonPhysicsAssetLib.get_constraint_name(physics_asset: PhysicsAsset, constraint_index: int) -> Name
unreal.PythonPhysicsAssetLib.get_constraints_names(physics_asset: PhysicsAsset) -> Array[Name]
unreal.PythonPhysicsAssetLib.get_edited_physics_assets() -> Array[PhysicsAsset]
unreal.PythonPhysicsAssetLib.get_physics_asset_from_top_window() -> PhysicsAsset
unreal.PythonPhysicsAssetLib.get_selected(physics_asset: PhysicsAsset) -> bool
unreal.PythonPhysicsAssetLib.get_selected_bodies_indexes(physics_asset: PhysicsAsset) -> Array[int]
unreal.PythonPhysicsAssetLib.get_selected_item_names(physics_asset: PhysicsAsset) -> Array[Name]
unreal.PythonPhysicsAssetLib.get_skeleton_hierarchy(physics_asset: PhysicsAsset) -> Tuple[Array[Name], Array[int]]
unreal.PythonPhysicsAssetLib.log_selected(physics_asset: PhysicsAsset) -> None
unreal.PythonPhysicsAssetLib.reset_constraint_properties(physics_asset: PhysicsAsset, constraint_index: int) -> None
unreal.PythonPhysicsAssetLib.rotate_selected_body(physics_asset: PhysicsAsset, rotation: Rotator) -> bool
unreal.PythonPhysicsAssetLib.rotate_selected_constraint(physics_asset: PhysicsAsset, rotation: Rotator) -> bool
unreal.PythonPhysicsAssetLib.scale_body(physics_asset: PhysicsAsset, body_index: int, scale: float) -> bool
unreal.PythonPhysicsAssetLib.select_body_by_name(physics_asset: PhysicsAsset, name_in: Name) -> bool
unreal.PythonPhysicsAssetLib.select_body_by_names(physics_asset: PhysicsAsset, names: Array[Name]) -> bool
unreal.PythonPhysicsAssetLib.select_constraint_by_name(physics_asset: PhysicsAsset, name_in: Name) -> bool
unreal.PythonPhysicsAssetLib.select_constraint_by_names(physics_asset: PhysicsAsset, names: Array[Name]) -> bool
unreal.PythonPhysicsAssetLib.select_shape_by_name(physics_asset: PhysicsAsset, name_in: Name) -> bool
unreal.PythonPhysicsAssetLib.select_shape_by_names(physics_asset: PhysicsAsset, names: Array[Name]) -> bool
unreal.PythonPhysicsAssetLib.set_body_center(physics_asset: PhysicsAsset, body_index: int, center: Vector) -> bool
unreal.PythonPhysicsAssetLib.set_body_length(physics_asset: PhysicsAsset, body_index: int, length: float) -> bool
unreal.PythonPhysicsAssetLib.set_body_radius(physics_asset: PhysicsAsset, body_index: int, radius: float) -> bool
unreal.PythonPhysicsAssetLib.set_body_rotation(physics_asset: PhysicsAsset, body_index: int, rotation: Rotator) -> bool
unreal.PythonPhysicsAssetLib.set_body_size(physics_asset: PhysicsAsset, body_index: int, size: Vector) -> bool
unreal.PythonPhysicsAssetLib.update_profile_instance(physics_asset: PhysicsAsset, constraint_index: int) -> None
```

## `unreal.RadialDamageEvent(DamageEvent)`

```python
unreal.RadialDamageEvent.__init__() -> None
```

## `unreal.RadialDamageParams(StructBase)`

```python
unreal.RadialDamageParams.__init__(base_damage: float = 0.000000, minimum_damage: float = 0.000000, inner_radius: float = 0.000000, outer_radius: float = 0.000000, damage_falloff: float = 0.000000) -> None
unreal.RadialDamageParams.base_damage(value: float) -> None
unreal.RadialDamageParams.damage_falloff(value: float) -> None
unreal.RadialDamageParams.inner_radius(value: float) -> None
unreal.RadialDamageParams.minimum_damage(value: float) -> None
unreal.RadialDamageParams.outer_radius(value: float) -> None
```

## `unreal.RigPhysicsElement(RigSingleParentElement)`

```python
unreal.RigPhysicsElement.__init__(key: RigElementKey = [RigElementType.NONE, "None"], index: int = 0, sub_index: int = 0, created_at_instruction_index: int = 0, selected: bool = False, solver: RigPhysicsSolverID = [[]], settings: RigPhysicsSettings = [1.000000]) -> None
unreal.RigPhysicsElement.settings() -> RigPhysicsSettings
unreal.RigPhysicsElement.solver() -> RigPhysicsSolverID
```

## `unreal.RigPhysicsSettings(StructBase)`

```python
unreal.RigPhysicsSettings.__init__(mass: float = 0.000000) -> None
unreal.RigPhysicsSettings.mass(value: float) -> None
```

## `unreal.RigPhysicsSolverDescription(StructBase)`

```python
unreal.RigPhysicsSolverDescription.__init__(id: RigPhysicsSolverID = [[]], name: Name = "None") -> None
unreal.RigPhysicsSolverDescription.id() -> RigPhysicsSolverID
unreal.RigPhysicsSolverDescription.name() -> Name
```

## `unreal.RigPhysicsSolverID(StructBase)`

```python
unreal.RigPhysicsSolverID.__init__(guid: Guid = []) -> None
unreal.RigPhysicsSolverID.guid() -> Guid
```

## `unreal.RigUnit_AimConstraint(RigUnitMutable)`

```python
unreal.RigUnit_AimConstraint.__init__(execute_context: ControlRigExecuteContext = [], joint: Name = "None", aim_mode: AimMode = AimMode.AIM_AT_TARGET, up_mode: AimMode = AimMode.AIM_AT_TARGET, aim_vector: Vector = [0.000000, 0.000000, 0.000000], up_vector: Vector = [0.000000, 0.000000, 0.000000], aim_targets: Array[AimTarget] = [], up_targets: Array[AimTarget] = []) -> None
unreal.RigUnit_AimConstraint.aim_mode(value: AimMode) -> None
unreal.RigUnit_AimConstraint.aim_targets(value: Array[AimTarget]) -> None
unreal.RigUnit_AimConstraint.aim_vector(value: Vector) -> None
unreal.RigUnit_AimConstraint.joint(value: Name) -> None
unreal.RigUnit_AimConstraint.up_mode(value: AimMode) -> None
unreal.RigUnit_AimConstraint.up_targets(value: Array[AimTarget]) -> None
unreal.RigUnit_AimConstraint.up_vector(value: Vector) -> None
```

## `unreal.RigUnit_AimConstraintLocalSpaceOffset(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_AimConstraintLocalSpaceOffset.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], aim_axis: Vector = [0.000000, 0.000000, 0.000000], up_axis: Vector = [0.000000, 0.000000, 0.000000], world_up: RigUnit_AimConstraint_WorldUp = [[0.000000, 0.000000, 1.000000], ControlRigVectorKind.DIRECTION, [RigElementType.NONE, "None"]], parents: Array[ConstraintParent] = [], advanced_settings: RigUnit_AimConstraint_AdvancedSettings = [[False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], EulerRotationOrder.XZY], weight: float = 0.000000) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.advanced_settings(value: RigUnit_AimConstraint_AdvancedSettings) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.aim_axis(value: Vector) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.child(value: RigElementKey) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.maintain_offset(value: bool) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.up_axis(value: Vector) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.weight(value: float) -> None
unreal.RigUnit_AimConstraintLocalSpaceOffset.world_up(value: RigUnit_AimConstraint_WorldUp) -> None
```

## `unreal.RigUnit_AimConstraint_AdvancedSettings(StructBase)`

```python
unreal.RigUnit_AimConstraint_AdvancedSettings.__init__(debug_settings: RigUnit_AimBone_DebugSettings = [False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], rotation_order_for_filter: EulerRotationOrder = EulerRotationOrder.XYZ) -> None
unreal.RigUnit_AimConstraint_AdvancedSettings.debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
unreal.RigUnit_AimConstraint_AdvancedSettings.rotation_order_for_filter(value: EulerRotationOrder) -> None
```

## `unreal.RigUnit_HierarchyAddPhysicsJoint(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddPhysicsJoint.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], solver: RigPhysicsSolverID = [[]], settings: RigPhysicsSettings = [1.000000]) -> None
unreal.RigUnit_HierarchyAddPhysicsJoint.settings(value: RigPhysicsSettings) -> None
unreal.RigUnit_HierarchyAddPhysicsJoint.solver(value: RigPhysicsSolverID) -> None
unreal.RigUnit_HierarchyAddPhysicsJoint.transform(value: Transform) -> None
```

## `unreal.RigUnit_HierarchyAddPhysicsSolver(RigUnit_DynamicHierarchyBaseMutable)`

```python
unreal.RigUnit_HierarchyAddPhysicsSolver.__init__(execute_context: ControlRigExecuteContext = [], name: Name = "None", solver: RigPhysicsSolverID = [[]]) -> None
unreal.RigUnit_HierarchyAddPhysicsSolver.name(value: Name) -> None
unreal.RigUnit_HierarchyAddPhysicsSolver.solver() -> RigPhysicsSolverID
```

## `unreal.RigUnit_ParentConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_ParentConstraint.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: TransformFilter = [[True, True, True], [True, True, True], [True, True, True]], parents: Array[ConstraintParent] = [], advanced_settings: RigUnit_ParentConstraint_AdvancedSettings = [ConstraintInterpType.AVERAGE, EulerRotationOrder.XZY], weight: float = 0.000000) -> None
unreal.RigUnit_ParentConstraint.advanced_settings(value: RigUnit_ParentConstraint_AdvancedSettings) -> None
unreal.RigUnit_ParentConstraint.child(value: RigElementKey) -> None
unreal.RigUnit_ParentConstraint.filter(value: TransformFilter) -> None
unreal.RigUnit_ParentConstraint.maintain_offset(value: bool) -> None
unreal.RigUnit_ParentConstraint.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_ParentConstraint.weight(value: float) -> None
```

## `unreal.RigUnit_ParentConstraintMath(RigUnit_HighlevelBase)`

```python
unreal.RigUnit_ParentConstraintMath.__init__(input: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parents: Array[ConstraintParent] = [], advanced_settings: RigUnit_ParentConstraintMath_AdvancedSettings = [ConstraintInterpType.AVERAGE], output: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ParentConstraintMath.advanced_settings(value: RigUnit_ParentConstraintMath_AdvancedSettings) -> None
unreal.RigUnit_ParentConstraintMath.input(value: Transform) -> None
unreal.RigUnit_ParentConstraintMath.output() -> Transform
unreal.RigUnit_ParentConstraintMath.parents(value: Array[ConstraintParent]) -> None
```

## `unreal.RigUnit_ParentConstraintMath_AdvancedSettings(StructBase)`

```python
unreal.RigUnit_ParentConstraintMath_AdvancedSettings.__init__(interpolation_type: ConstraintInterpType = ConstraintInterpType.AVERAGE) -> None
unreal.RigUnit_ParentConstraintMath_AdvancedSettings.interpolation_type(value: ConstraintInterpType) -> None
```

## `unreal.RigUnit_ParentConstraint_AdvancedSettings(StructBase)`

```python
unreal.RigUnit_ParentConstraint_AdvancedSettings.__init__(interpolation_type: ConstraintInterpType = ConstraintInterpType.AVERAGE, rotation_order_for_filter: EulerRotationOrder = EulerRotationOrder.XYZ) -> None
unreal.RigUnit_ParentConstraint_AdvancedSettings.interpolation_type(value: ConstraintInterpType) -> None
unreal.RigUnit_ParentConstraint_AdvancedSettings.rotation_order_for_filter(value: EulerRotationOrder) -> None
```

## `unreal.RigUnit_ParentSwitchConstraint(RigUnitMutable)`

```python
unreal.RigUnit_ParentSwitchConstraint.__init__(execute_context: ControlRigExecuteContext = [], subject: RigElementKey = [RigElementType.NONE, "None"], parent_index: int = 0, parents: RigElementKeyCollection = [[]], initial_global_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], switched: bool = False) -> None
unreal.RigUnit_ParentSwitchConstraint.initial_global_transform(value: Transform) -> None
unreal.RigUnit_ParentSwitchConstraint.parent_index(value: int) -> None
unreal.RigUnit_ParentSwitchConstraint.parents(value: RigElementKeyCollection) -> None
unreal.RigUnit_ParentSwitchConstraint.subject(value: RigElementKey) -> None
unreal.RigUnit_ParentSwitchConstraint.switched() -> bool
unreal.RigUnit_ParentSwitchConstraint.transform() -> Transform
unreal.RigUnit_ParentSwitchConstraint.weight(value: float) -> None
```

## `unreal.RigUnit_ParentSwitchConstraintArray(RigUnitMutable)`

```python
unreal.RigUnit_ParentSwitchConstraintArray.__init__(execute_context: ControlRigExecuteContext = [], subject: RigElementKey = [RigElementType.NONE, "None"], parent_index: int = 0, parents: Array[RigElementKey] = [], initial_global_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], switched: bool = False) -> None
unreal.RigUnit_ParentSwitchConstraintArray.initial_global_transform(value: Transform) -> None
unreal.RigUnit_ParentSwitchConstraintArray.parent_index(value: int) -> None
unreal.RigUnit_ParentSwitchConstraintArray.parents(value: Array[RigElementKey]) -> None
unreal.RigUnit_ParentSwitchConstraintArray.subject(value: RigElementKey) -> None
unreal.RigUnit_ParentSwitchConstraintArray.switched() -> bool
unreal.RigUnit_ParentSwitchConstraintArray.transform() -> Transform
unreal.RigUnit_ParentSwitchConstraintArray.weight(value: float) -> None
```

## `unreal.RigUnit_PositionConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_PositionConstraint.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], weight: float = 0.000000) -> None
unreal.RigUnit_PositionConstraint.child(value: RigElementKey) -> None
unreal.RigUnit_PositionConstraint.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_PositionConstraint.maintain_offset(value: bool) -> None
unreal.RigUnit_PositionConstraint.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_PositionConstraint.weight(value: float) -> None
```

## `unreal.RigUnit_PositionConstraintLocalSpaceOffset(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_PositionConstraintLocalSpaceOffset.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], weight: float = 0.000000) -> None
unreal.RigUnit_PositionConstraintLocalSpaceOffset.child(value: RigElementKey) -> None
unreal.RigUnit_PositionConstraintLocalSpaceOffset.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_PositionConstraintLocalSpaceOffset.maintain_offset(value: bool) -> None
unreal.RigUnit_PositionConstraintLocalSpaceOffset.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_PositionConstraintLocalSpaceOffset.weight(value: float) -> None
```

## `unreal.RigUnit_RotationConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_RotationConstraint.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], advanced_settings: RigUnit_RotationConstraint_AdvancedSettings = [ConstraintInterpType.AVERAGE, EulerRotationOrder.XZY], weight: float = 0.000000) -> None
unreal.RigUnit_RotationConstraint.advanced_settings(value: RigUnit_RotationConstraint_AdvancedSettings) -> None
unreal.RigUnit_RotationConstraint.child(value: RigElementKey) -> None
unreal.RigUnit_RotationConstraint.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_RotationConstraint.maintain_offset(value: bool) -> None
unreal.RigUnit_RotationConstraint.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_RotationConstraint.weight(value: float) -> None
```

## `unreal.RigUnit_RotationConstraintLocalSpaceOffset(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_RotationConstraintLocalSpaceOffset.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], advanced_settings: RigUnit_RotationConstraint_AdvancedSettings = [ConstraintInterpType.AVERAGE, EulerRotationOrder.XZY], weight: float = 0.000000) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.advanced_settings(value: RigUnit_RotationConstraint_AdvancedSettings) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.child(value: RigElementKey) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.maintain_offset(value: bool) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_RotationConstraintLocalSpaceOffset.weight(value: float) -> None
```

## `unreal.RigUnit_RotationConstraint_AdvancedSettings(StructBase)`

```python
unreal.RigUnit_RotationConstraint_AdvancedSettings.__init__(interpolation_type: ConstraintInterpType = ConstraintInterpType.AVERAGE, rotation_order_for_filter: EulerRotationOrder = EulerRotationOrder.XYZ) -> None
unreal.RigUnit_RotationConstraint_AdvancedSettings.interpolation_type(value: ConstraintInterpType) -> None
unreal.RigUnit_RotationConstraint_AdvancedSettings.rotation_order_for_filter(value: EulerRotationOrder) -> None
```

## `unreal.RigUnit_ScaleConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_ScaleConstraint.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], weight: float = 0.000000) -> None
unreal.RigUnit_ScaleConstraint.child(value: RigElementKey) -> None
unreal.RigUnit_ScaleConstraint.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_ScaleConstraint.maintain_offset(value: bool) -> None
unreal.RigUnit_ScaleConstraint.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_ScaleConstraint.weight(value: float) -> None
```

## `unreal.RigUnit_ScaleConstraintLocalSpaceOffset(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], maintain_offset: bool = False, filter: FilterOptionPerAxis = [True, True, True], parents: Array[ConstraintParent] = [], weight: float = 0.000000) -> None
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.child(value: RigElementKey) -> None
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.filter(value: FilterOptionPerAxis) -> None
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.maintain_offset(value: bool) -> None
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.parents(value: Array[ConstraintParent]) -> None
unreal.RigUnit_ScaleConstraintLocalSpaceOffset.weight(value: float) -> None
```

## `unreal.RigUnit_SplineConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_SplineConstraint.__init__(execute_context: ControlRigExecuteContext = [], items: Array[RigElementKey] = [], spline: ControlRigSpline = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], propagate_to_children: bool = False) -> None
unreal.RigUnit_SplineConstraint.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_SplineConstraint.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_SplineConstraint.maximum(value: float) -> None
unreal.RigUnit_SplineConstraint.minimum(value: float) -> None
unreal.RigUnit_SplineConstraint.primary_axis(value: Vector) -> None
unreal.RigUnit_SplineConstraint.propagate_to_children() -> bool
unreal.RigUnit_SplineConstraint.secondary_axis(value: Vector) -> None
unreal.RigUnit_SplineConstraint.spline(value: ControlRigSpline) -> None
```

## `unreal.RigidBodyErrorCorrection(StructBase)`

```python
unreal.RigidBodyErrorCorrection.__init__() -> None
```

## `unreal.SolverCollisionFilterSettings(StructBase)`

```python
unreal.SolverCollisionFilterSettings.__init__(filter_enabled: bool = False, min_mass: float = 0.000000, min_speed: float = 0.000000, min_impulse: float = 0.000000) -> None
unreal.SolverCollisionFilterSettings.filter_enabled(value: bool) -> None
unreal.SolverCollisionFilterSettings.min_impulse(value: float) -> None
unreal.SolverCollisionFilterSettings.min_mass(value: float) -> None
unreal.SolverCollisionFilterSettings.min_speed(value: float) -> None
```

## `unreal.TakeAnyDamageSignature(MulticastDelegateBase)`

```python
unreal.TakeAnyDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.TakePointDamageSignature(MulticastDelegateBase)`

```python
unreal.TakePointDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.TakeRadialDamageSignature(MulticastDelegateBase)`

```python
unreal.TakeRadialDamageSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.TakeRecorderChaosCacheSource(TakeRecorderSource)`

```python
unreal.TakeRecorderChaosCacheSource.chaos_cache_manager(value: ChaosCacheManager) -> None
```

## `unreal.TickableConstraint(Object)`

```python
unreal.TickableConstraint.active(value: bool) -> None
```

## `unreal.TickableLookAtConstraint(TickableTransformConstraint)`

```python
unreal.TickableLookAtConstraint.axis(value: Vector) -> None
```

## `unreal.TickableParentConstraint(TickableTransformConstraint)`

```python
unreal.TickableParentConstraint.offset_transform(value: Transform) -> None
unreal.TickableParentConstraint.scaling(value: bool) -> None
unreal.TickableParentConstraint.transform_filter(value: TransformFilter) -> None
```

## `unreal.TickableRotationConstraint(TickableTransformConstraint)`

```python
unreal.TickableRotationConstraint.axis_filter(value: FilterOptionPerAxis) -> None
unreal.TickableRotationConstraint.offset_rotation(value: Quat) -> None
```

## `unreal.TickableScaleConstraint(TickableTransformConstraint)`

```python
unreal.TickableScaleConstraint.axis_filter(value: FilterOptionPerAxis) -> None
unreal.TickableScaleConstraint.offset_scale(value: Vector) -> None
```

## `unreal.TickableTranslationConstraint(TickableTransformConstraint)`

```python
unreal.TickableTranslationConstraint.axis_filter(value: FilterOptionPerAxis) -> None
unreal.TickableTranslationConstraint.offset_translation(value: Vector) -> None
```

## `unreal.TwistConstraint(ConstraintBaseParams)`

```python
unreal.TwistConstraint.__init__() -> None
```

## `unreal.glTFRuntimePhysicsAssetAutoBodyConfig(StructBase)`

```python
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.__init__(collision_type: EglTFRuntimePhysicsAssetAutoBodyCollisionType = EglTFRuntimePhysicsAssetAutoBodyCollisionType.CAPSULE, min_bone_size: float = 0.000000, disable_overlapping_collisions: bool = False, disable_all_collisions: bool = False, collision_trace_flag: CollisionTraceFlag = CollisionTraceFlag.CTF_USE_DEFAULT, physics_type: PhysicsType = PhysicsType.PHYS_TYPE_DEFAULT, consider_for_bounds: bool = False, collision_scale: float = 0.000000) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_scale(value: float) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_trace_flag(value: CollisionTraceFlag) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.collision_type(value: EglTFRuntimePhysicsAssetAutoBodyCollisionType) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.consider_for_bounds(value: bool) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_all_collisions(value: bool) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.disable_overlapping_collisions(value: bool) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.min_bone_size(value: float) -> None
unreal.glTFRuntimePhysicsAssetAutoBodyConfig.physics_type(value: PhysicsType) -> None
```

## `unreal.glTFRuntimePhysicsBody(StructBase)`

```python
unreal.glTFRuntimePhysicsBody.__init__(collision_trace_flag: CollisionTraceFlag = CollisionTraceFlag.CTF_USE_DEFAULT, physics_type: PhysicsType = PhysicsType.PHYS_TYPE_DEFAULT, consider_for_bounds: bool = False, capsule_collisions: Array[glTFRuntimeCapsule] = [], sphere_collisions: Array[glTFRuntimeSphere] = [], box_collisions: Array[Box] = [], sphere_auto_collision: bool = False, box_auto_collision: bool = False, capsule_auto_collision: bool = False, collision_scale: float = 0.000000, disable_collision: bool = False) -> None
unreal.glTFRuntimePhysicsBody.box_auto_collision(value: bool) -> None
unreal.glTFRuntimePhysicsBody.box_collisions(value: Array[Box]) -> None
unreal.glTFRuntimePhysicsBody.capsule_auto_collision(value: bool) -> None
unreal.glTFRuntimePhysicsBody.capsule_collisions(value: Array[glTFRuntimeCapsule]) -> None
unreal.glTFRuntimePhysicsBody.collision_scale(value: float) -> None
unreal.glTFRuntimePhysicsBody.collision_trace_flag(value: CollisionTraceFlag) -> None
unreal.glTFRuntimePhysicsBody.consider_for_bounds(value: bool) -> None
unreal.glTFRuntimePhysicsBody.disable_collision(value: bool) -> None
unreal.glTFRuntimePhysicsBody.physics_type(value: PhysicsType) -> None
unreal.glTFRuntimePhysicsBody.sphere_auto_collision(value: bool) -> None
unreal.glTFRuntimePhysicsBody.sphere_collisions(value: Array[glTFRuntimeSphere]) -> None
```

## `unreal.glTFRuntimePhysicsConstraint(StructBase)`

```python
unreal.glTFRuntimePhysicsConstraint.__init__(constraint_bone1: str = "", constraint_bone2: str = "", constraint_pos1: Vector = [0.000000, 0.000000, 0.000000], constraint_pos2: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.glTFRuntimePhysicsConstraint.constraint_bone1(value: str) -> None
unreal.glTFRuntimePhysicsConstraint.constraint_bone2(value: str) -> None
unreal.glTFRuntimePhysicsConstraint.constraint_pos1(value: Vector) -> None
unreal.glTFRuntimePhysicsConstraint.constraint_pos2(value: Vector) -> None
```

