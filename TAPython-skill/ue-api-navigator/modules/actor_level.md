# Unreal Python API — Actor Level

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AbilityTask_ApplyRootMotionMoveToActorForce(AbilityTask_ApplyRootMotion_Base)`

```python
unreal.AbilityTask_ApplyRootMotionMoveToActorForce.on_finished(value: ApplyRootMotionMoveToActorForceDelegate) -> None
```

## `unreal.AbilityTask_SpawnActor(AbilityTask)`

```python
unreal.AbilityTask_SpawnActor.did_not_spawn(value: SpawnActorDelegate) -> None
unreal.AbilityTask_SpawnActor.success(value: SpawnActorDelegate) -> None
```

## `unreal.Actor(Object)`

```python
unreal.Actor.acquire_editor_element_handle(allow_create: bool = True) -> ScriptTypedElementHandle
unreal.Actor.actor_guid() -> Guid
unreal.Actor.actor_has_tag(tag: Name) -> bool
unreal.Actor.actor_instance_guid() -> Guid
unreal.Actor.add_actor_local_offset(delta_location: Vector, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_local_rotation(delta_rotation: Rotator, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_local_transform(new_transform: Transform, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_world_offset(delta_location: Vector, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_world_rotation(delta_rotation: Rotator, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_world_transform(delta_transform: Transform, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_actor_world_transform_keep_scale(delta_transform: Transform, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.add_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
unreal.Actor.add_tick_prerequisite_component(prerequisite_component: ActorComponent) -> None
unreal.Actor.always_relevant(value: bool) -> None
unreal.Actor.attach_to_actor(parent_actor: Actor, socket_name: Name, location_rule: AttachmentRule, rotation_rule: AttachmentRule, scale_rule: AttachmentRule, weld_simulated_bodies: bool = True) -> bool
unreal.Actor.attach_to_component(parent: SceneComponent, socket_name: Name, location_rule: AttachmentRule, rotation_rule: AttachmentRule, scale_rule: AttachmentRule, weld_simulated_bodies: bool = True) -> bool
unreal.Actor.auto_destroy_when_finished(value: bool) -> None
unreal.Actor.can_be_damaged(value: bool) -> None
unreal.Actor.can_trigger_resimulation() -> bool
unreal.Actor.content_bundle_guid() -> Guid
unreal.Actor.create_input_component(input_component_to_create: Class) -> None
unreal.Actor.create_pcg_data_from_actor(parse_actor: bool = True) -> PCGData
unreal.Actor.custom_time_dilation(value: float) -> None
unreal.Actor.destroy_actor() -> None
unreal.Actor.detach_from_actor(location_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE, rotation_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE, scale_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE) -> None
unreal.Actor.disable_input(player_controller: PlayerController) -> None
unreal.Actor.enable_auto_lod_generation(value: bool) -> None
unreal.Actor.enable_input(player_controller: PlayerController) -> None
unreal.Actor.find_camera_component_when_view_target(value: bool) -> None
unreal.Actor.find_component_by_tag(component_class: Class = None, tag: Name = ...) -> ActorComponent
unreal.Actor.flush_net_dormancy() -> None
unreal.Actor.force_net_update() -> None
unreal.Actor.generate_overlap_events_during_level_streaming(value: bool) -> None
unreal.Actor.get_actor_bounds(only_colliding_components: bool, include_from_child_actors: bool = False) -> Tuple[Vector, Vector]
unreal.Actor.get_actor_bounds_pcg(ignore_pcg_created_components: bool = True) -> Box
unreal.Actor.get_actor_enable_collision() -> bool
unreal.Actor.get_actor_eyes_view_point() -> Tuple[Vector, Rotator]
unreal.Actor.get_actor_forward_vector() -> Vector
unreal.Actor.get_actor_label(create_if_none: bool = True) -> str
unreal.Actor.get_actor_local_bounds_pcg(ignore_pcg_created_components: bool = True) -> Box
unreal.Actor.get_actor_location() -> Vector
unreal.Actor.get_actor_relative_scale3d() -> Vector
unreal.Actor.get_actor_right_vector() -> Vector
unreal.Actor.get_actor_rotation() -> Rotator
unreal.Actor.get_actor_scale3d() -> Vector
unreal.Actor.get_actor_tick_interval() -> float
unreal.Actor.get_actor_time_dilation() -> float
unreal.Actor.get_actor_transform() -> Transform
unreal.Actor.get_actor_up_vector() -> Vector
unreal.Actor.get_all_child_actors(include_descendants: bool = True) -> Array[Actor]
unreal.Actor.get_attach_parent_actor() -> Actor
unreal.Actor.get_attach_parent_socket_name() -> Name
unreal.Actor.get_attached_actors(reset_array: bool = True, recursively_include_attached_actors: bool = False) -> Array[Actor]
unreal.Actor.get_component_by_class(component_class: Class = None) -> ActorComponent
unreal.Actor.get_components_by_class(component_class: Class = None) -> Array[ActorComponent]
unreal.Actor.get_components_by_interface(interface: Class) -> Array[ActorComponent]
unreal.Actor.get_components_by_tag(component_class: Class = None, tag: Name = ...) -> Array[ActorComponent]
unreal.Actor.get_default_actor_label() -> str
unreal.Actor.get_distance_to(other_actor: Actor) -> float
unreal.Actor.get_dot_product_to(other_actor: Actor) -> float
unreal.Actor.get_folder_path() -> Name
unreal.Actor.get_game_time_since_creation() -> float
unreal.Actor.get_horizontal_distance_to(other_actor: Actor) -> float
unreal.Actor.get_horizontal_dot_product_to(other_actor: Actor) -> float
unreal.Actor.get_instigator() -> Pawn
unreal.Actor.get_instigator_controller() -> Controller
unreal.Actor.get_level() -> Level
unreal.Actor.get_level_transform() -> Transform
unreal.Actor.get_life_span() -> float
unreal.Actor.get_local_role() -> NetRole
unreal.Actor.get_overlapping_actors(class_filter: Class = None) -> Array[Actor]
unreal.Actor.get_overlapping_components() -> Array[PrimitiveComponent]
unreal.Actor.get_owner() -> Actor
unreal.Actor.get_parent_actor() -> Actor
unreal.Actor.get_parent_component() -> ChildActorComponent
unreal.Actor.get_physics_replication_mode() -> PhysicsReplicationMode
unreal.Actor.get_ray_tracing_group_id() -> int
unreal.Actor.get_remote_role() -> NetRole
unreal.Actor.get_resimulation_threshold() -> float
unreal.Actor.get_squared_distance_to(other_actor: Actor) -> float
unreal.Actor.get_squared_horizontal_distance_to(other_actor: Actor) -> float
unreal.Actor.get_tickable_when_paused() -> bool
unreal.Actor.get_touching_actors(class_filter: Class = None) -> Array[Actor]
unreal.Actor.get_touching_components() -> Array[PrimitiveComponent]
unreal.Actor.get_velocity() -> Vector
unreal.Actor.get_vertical_distance_to(other_actor: Actor) -> float
unreal.Actor.has_authority() -> bool
unreal.Actor.has_tag(tag: Name) -> bool
unreal.Actor.hidden() -> bool
unreal.Actor.initial_life_span() -> float
unreal.Actor.instigator(value: Pawn) -> None
unreal.Actor.is_actor_being_destroyed() -> bool
unreal.Actor.is_actor_tick_enabled() -> bool
unreal.Actor.is_child_actor() -> bool
unreal.Actor.is_editable() -> bool
unreal.Actor.is_hidden_ed() -> bool
unreal.Actor.is_hidden_ed_at_startup() -> bool
unreal.Actor.is_overlapping_actor(other: Actor) -> bool
unreal.Actor.is_selectable() -> bool
unreal.Actor.is_temporarily_hidden_in_editor(include_parent: bool = False) -> bool
unreal.Actor.life_span() -> float
unreal.Actor.make_noise(loudness: float = 1.000000, noise_instigator: Pawn = None, noise_location: Vector = [0.000000, 0.000000, 0.000000], max_range: float = 0.000000, tag: Name = "None") -> None
unreal.Actor.min_net_update_frequency(value: float) -> None
unreal.Actor.net_cull_distance_squared(value: float) -> None
unreal.Actor.net_dormancy() -> NetDormancy
unreal.Actor.net_priority(value: float) -> None
unreal.Actor.net_update_frequency(value: float) -> None
unreal.Actor.net_use_owner_relevancy(value: bool) -> None
unreal.Actor.on_actor_begin_overlap(value: ActorBeginOverlapSignature) -> None
unreal.Actor.on_actor_end_overlap(value: ActorEndOverlapSignature) -> None
unreal.Actor.on_actor_hit(value: ActorHitSignature) -> None
unreal.Actor.on_actor_touch(value: ActorBeginOverlapSignature) -> None
unreal.Actor.on_actor_un_touch(value: ActorEndOverlapSignature) -> None
unreal.Actor.on_become_view_target(pc: PlayerController) -> None
unreal.Actor.on_begin_cursor_over(value: ActorBeginCursorOverSignature) -> None
unreal.Actor.on_clicked(value: ActorOnClickedSignature) -> None
unreal.Actor.on_destroyed(value: ActorDestroyedSignature) -> None
unreal.Actor.on_end_cursor_over(value: ActorEndCursorOverSignature) -> None
unreal.Actor.on_end_play(value: ActorEndPlaySignature) -> None
unreal.Actor.on_end_view_target(pc: PlayerController) -> None
unreal.Actor.on_input_touch_begin(value: ActorOnInputTouchBeginSignature) -> None
unreal.Actor.on_input_touch_end(value: ActorOnInputTouchEndSignature) -> None
unreal.Actor.on_input_touch_enter(value: ActorBeginTouchOverSignature) -> None
unreal.Actor.on_input_touch_leave(value: ActorEndTouchOverSignature) -> None
unreal.Actor.on_released(value: ActorOnReleasedSignature) -> None
unreal.Actor.on_reset() -> None
unreal.Actor.on_take_any_damage(value: TakeAnyDamageSignature) -> None
unreal.Actor.on_take_point_damage(value: TakePointDamageSignature) -> None
unreal.Actor.on_take_radial_damage(value: TakeRadialDamageSignature) -> None
unreal.Actor.only_relevant_to_owner() -> bool
unreal.Actor.pivot_offset() -> Vector
unreal.Actor.prestream_textures(seconds: float, enable_streaming: bool, cinematic_texture_groups: int = 0) -> None
unreal.Actor.receive_actor_begin_cursor_over() -> None
unreal.Actor.receive_actor_begin_overlap(other_actor: Actor) -> None
unreal.Actor.receive_actor_end_cursor_over() -> None
unreal.Actor.receive_actor_end_overlap(other_actor: Actor) -> None
unreal.Actor.receive_actor_on_clicked(button_pressed: Key) -> None
unreal.Actor.receive_actor_on_input_touch_begin(finger_index: TouchIndex) -> None
unreal.Actor.receive_actor_on_input_touch_end(finger_index: TouchIndex) -> None
unreal.Actor.receive_actor_on_input_touch_enter(finger_index: TouchIndex) -> None
unreal.Actor.receive_actor_on_input_touch_leave(finger_index: TouchIndex) -> None
unreal.Actor.receive_actor_on_released(button_released: Key) -> None
unreal.Actor.receive_actor_touch(other_actor: Actor) -> None
unreal.Actor.receive_actor_untouch(other_actor: Actor) -> None
unreal.Actor.receive_any_damage(damage: float, damage_type: DamageType, instigated_by: Controller, damage_causer: Actor) -> None
unreal.Actor.receive_async_physics_tick(delta_seconds: float, sim_seconds: float) -> None
unreal.Actor.receive_begin_play() -> None
unreal.Actor.receive_destroyed() -> None
unreal.Actor.receive_end_play(end_play_reason: EndPlayReason) -> None
unreal.Actor.receive_hit(my_comp: PrimitiveComponent, other: Actor, other_comp: PrimitiveComponent, self_moved: bool, hit_location: Vector, hit_normal: Vector, normal_impulse: Vector, hit: HitResult) -> None
unreal.Actor.receive_point_damage(damage: float, damage_type: DamageType, hit_location: Vector, hit_normal: Vector, hit_component: PrimitiveComponent, bone_name: Name, shot_from_direction: Vector, instigated_by: Controller, damage_causer: Actor, hit_info: HitResult) -> None
unreal.Actor.receive_radial_damage(damage_received: float, damage_type: DamageType, origin: Vector, hit_info: HitResult, instigated_by: Controller, damage_causer: Actor) -> None
unreal.Actor.receive_tick(delta_seconds: float) -> None
unreal.Actor.remove_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
unreal.Actor.remove_tick_prerequisite_component(prerequisite_component: ActorComponent) -> None
unreal.Actor.replicate_using_registered_sub_object_list() -> bool
unreal.Actor.replicates() -> bool
unreal.Actor.root_component() -> SceneComponent
unreal.Actor.set_actor_enable_collision(new_actor_enable_collision: bool) -> None
unreal.Actor.set_actor_hidden(new_hidden: bool) -> None
unreal.Actor.set_actor_hidden_in_game(new_hidden: bool) -> None
unreal.Actor.set_actor_label(new_actor_label: str, mark_dirty: bool = True) -> None
unreal.Actor.set_actor_location(new_location: Vector, sweep: bool, teleport: bool) -> Optional[HitResult]
unreal.Actor.set_actor_location_and_rotation(new_location: Vector, new_rotation: Rotator, sweep: bool, teleport: bool) -> Optional[HitResult]
unreal.Actor.set_actor_relative_location(new_relative_location: Vector, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.set_actor_relative_rotation(new_relative_rotation: Rotator, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.set_actor_relative_scale3d(new_relative_scale: Vector) -> None
unreal.Actor.set_actor_relative_transform(new_relative_transform: Transform, sweep: bool, teleport: bool) -> HitResult
unreal.Actor.set_actor_rotation(new_rotation: Rotator, teleport_physics: bool) -> bool
unreal.Actor.set_actor_scale3d(new_scale3d: Vector) -> None
unreal.Actor.set_actor_tick_enabled(enabled: bool) -> None
unreal.Actor.set_actor_tick_interval(tick_interval: float) -> None
unreal.Actor.set_actor_transform(new_transform: Transform, sweep: bool, teleport: bool) -> Optional[HitResult]
unreal.Actor.set_folder_path(new_folder_path: Name) -> None
unreal.Actor.set_is_temporarily_hidden_in_editor(is_hidden: bool) -> None
unreal.Actor.set_life_span(lifespan: float) -> None
unreal.Actor.set_net_dormancy(new_dormancy: NetDormancy) -> None
unreal.Actor.set_owner(new_owner: Actor) -> None
unreal.Actor.set_physics_replication_mode(replication_mode: PhysicsReplicationMode) -> None
unreal.Actor.set_ray_tracing_group_id(raytracing_group_id: int) -> None
unreal.Actor.set_replicate_movement(replicate_movement: bool) -> None
unreal.Actor.set_replicates(replicates: bool) -> None
unreal.Actor.set_tick_enabled(enabled: bool) -> None
unreal.Actor.set_tick_group(new_tick_group: TickingGroup) -> None
unreal.Actor.set_tick_prerequisite(prerequisite_actor: Actor) -> None
unreal.Actor.set_tickable_when_paused(tickable_when_paused: bool) -> None
unreal.Actor.spawn_collision_handling_method(value: SpawnActorCollisionHandlingMethod) -> None
unreal.Actor.sprite_scale(value: float) -> None
unreal.Actor.tags(value: Array[Name]) -> None
unreal.Actor.tear_off() -> None
unreal.Actor.teleport(dest_location: Vector, dest_rotation: Rotator) -> bool
unreal.Actor.was_recently_rendered(tolerance: float = 0.200000) -> bool
```

## `unreal.ActorActionUtility(EditorUtilityObject)`

```python
unreal.ActorActionUtility.get_supported_class() -> Class
unreal.ActorActionUtility.get_supported_classes() -> Array[Class]
```

## `unreal.ActorBeginCursorOverSignature(MulticastDelegateBase)`

```python
unreal.ActorBeginCursorOverSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorBeginOverlapSignature(MulticastDelegateBase)`

```python
unreal.ActorBeginOverlapSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorBeginTouchOverSignature(MulticastDelegateBase)`

```python
unreal.ActorBeginTouchOverSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorComponent(Object)`

```python
unreal.ActorComponent.acquire_editor_element_handle(allow_create: bool = True) -> ScriptTypedElementHandle
unreal.ActorComponent.activate(reset: bool = False) -> None
unreal.ActorComponent.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.ActorComponent.add_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
unreal.ActorComponent.add_tick_prerequisite_component(prerequisite_component: ActorComponent) -> None
unreal.ActorComponent.auto_activate() -> bool
unreal.ActorComponent.component_has_tag(tag: Name) -> bool
unreal.ActorComponent.component_tags(value: Array[Name]) -> None
unreal.ActorComponent.deactivate() -> None
unreal.ActorComponent.destroy_component(object: Object) -> None
unreal.ActorComponent.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.ActorComponent.get_component_tick_interval() -> float
unreal.ActorComponent.get_owner() -> Actor
unreal.ActorComponent.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.ActorComponent.is_active() -> bool
unreal.ActorComponent.is_being_destroyed() -> bool
unreal.ActorComponent.is_component_tick_enabled() -> bool
unreal.ActorComponent.is_editor_only() -> bool
unreal.ActorComponent.on_component_activated(value: ActorComponentActivatedSignature) -> None
unreal.ActorComponent.on_component_deactivated(value: ActorComponentDeactivateSignature) -> None
unreal.ActorComponent.receive_async_physics_tick(delta_seconds: float, sim_seconds: float) -> None
unreal.ActorComponent.receive_begin_play() -> None
unreal.ActorComponent.receive_end_play(end_play_reason: EndPlayReason) -> None
unreal.ActorComponent.receive_initialize_component() -> None
unreal.ActorComponent.receive_tick(delta_seconds: float) -> None
unreal.ActorComponent.receive_uninitialize_component(end_play_reason: EndPlayReason) -> None
unreal.ActorComponent.remove_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
unreal.ActorComponent.remove_tick_prerequisite_component(prerequisite_component: ActorComponent) -> None
unreal.ActorComponent.replicate_using_registered_sub_object_list() -> bool
unreal.ActorComponent.replicates() -> bool
unreal.ActorComponent.set_active(new_active: bool, reset: bool = False) -> None
unreal.ActorComponent.set_auto_activate(new_auto_activate: bool) -> None
unreal.ActorComponent.set_component_tick_enabled(enabled: bool) -> None
unreal.ActorComponent.set_component_tick_interval(tick_interval: float) -> None
unreal.ActorComponent.set_component_tick_interval_and_cooldown(tick_interval: float) -> None
unreal.ActorComponent.set_is_replicated(should_replicate: bool) -> None
unreal.ActorComponent.set_tick_group(new_tick_group: TickingGroup) -> None
unreal.ActorComponent.set_tickable_when_paused(tickable_when_paused: bool) -> None
unreal.ActorComponent.toggle_active() -> None
```

## `unreal.ActorComponentActivatedSignature(MulticastDelegateBase)`

```python
unreal.ActorComponentActivatedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorComponentDeactivateSignature(MulticastDelegateBase)`

```python
unreal.ActorComponentDeactivateSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorComponentTickFunction(TickFunction)`

```python
unreal.ActorComponentTickFunction.__init__() -> None
```

## `unreal.ActorDataLayer(StructBase)`

```python
unreal.ActorDataLayer.__init__(name: Name = "None") -> None
unreal.ActorDataLayer.name() -> Name
```

## `unreal.ActorDesc(StructBase)`

```python
unreal.ActorDesc.__init__(guid: Guid = [], native_class: Class = None, class_: SoftObjectPath = [""], name: Name = "None", label: Name = "None", bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], runtime_grid: Name = "None", is_spatially_loaded: bool = False, actor_is_editor_only: bool = False, actor_package: Name = "None", actor_path: Name = "None", data_layer_assets: Array[SoftObjectPath] = []) -> None
unreal.ActorDesc.actor_is_editor_only() -> bool
unreal.ActorDesc.actor_package() -> Name
unreal.ActorDesc.actor_path() -> Name
unreal.ActorDesc.bounds() -> Box
unreal.ActorDesc.class_() -> SoftObjectPath
unreal.ActorDesc.data_layer_assets() -> Array[SoftObjectPath]
unreal.ActorDesc.guid() -> Guid
unreal.ActorDesc.is_spatially_loaded() -> bool
unreal.ActorDesc.label() -> Name
unreal.ActorDesc.name() -> Name
unreal.ActorDesc.native_class() -> Class
unreal.ActorDesc.runtime_grid() -> Name
```

## `unreal.ActorDestroyedSignature(MulticastDelegateBase)`

```python
unreal.ActorDestroyedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorElementsCopy(Object)`

```python
unreal.ActorElementsCopy.actors_to_copy(value: Array[Actor]) -> None
```

## `unreal.ActorEndCursorOverSignature(MulticastDelegateBase)`

```python
unreal.ActorEndCursorOverSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorEndOverlapSignature(MulticastDelegateBase)`

```python
unreal.ActorEndOverlapSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorEndPlaySignature(MulticastDelegateBase)`

```python
unreal.ActorEndPlaySignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorEndTouchOverSignature(MulticastDelegateBase)`

```python
unreal.ActorEndTouchOverSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorForWorldTransforms(StructBase)`

```python
unreal.ActorForWorldTransforms.__init__(actor: Actor = None, component: SceneComponent = None, socket_name: Name = "None") -> None
unreal.ActorForWorldTransforms.actor(value: Actor) -> None
unreal.ActorForWorldTransforms.component(value: SceneComponent) -> None
unreal.ActorForWorldTransforms.socket_name(value: Name) -> None
```

## `unreal.ActorGroupingUtils(Object)`

```python
unreal.ActorGroupingUtils.add_selected_to_group() -> None
unreal.ActorGroupingUtils.can_group_actors(actors_to_group: Array[Actor]) -> bool
unreal.ActorGroupingUtils.can_group_selected_actors() -> bool
unreal.ActorGroupingUtils.get() -> ActorGroupingUtils
unreal.ActorGroupingUtils.group_actors(actors_to_group: Array[Actor]) -> GroupActor
unreal.ActorGroupingUtils.group_selected() -> GroupActor
unreal.ActorGroupingUtils.is_grouping_active() -> bool
unreal.ActorGroupingUtils.lock_selected_groups() -> None
unreal.ActorGroupingUtils.remove_selected_from_group() -> None
unreal.ActorGroupingUtils.set_grouping_active(grouping_active: bool) -> None
unreal.ActorGroupingUtils.ungroup_actors(actors_to_ungroup: Array[Actor]) -> None
unreal.ActorGroupingUtils.ungroup_selected() -> None
unreal.ActorGroupingUtils.unlock_selected_groups() -> None
```

## `unreal.ActorHitSignature(MulticastDelegateBase)`

```python
unreal.ActorHitSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorInitStateChangedBPDelegate(DelegateBase)`

```python
unreal.ActorInitStateChangedBPDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorInitStateChangedParams(StructBase)`

```python
unreal.ActorInitStateChangedParams.__init__(owning_actor: Actor = None, feature_name: Name = "None", implementer: Object = None, feature_state: GameplayTag = ["None"]) -> None
unreal.ActorInitStateChangedParams.feature_name(value: Name) -> None
unreal.ActorInitStateChangedParams.feature_state(value: GameplayTag) -> None
unreal.ActorInitStateChangedParams.implementer(value: Object) -> None
unreal.ActorInitStateChangedParams.owning_actor(value: Actor) -> None
```

## `unreal.ActorInstanceHandle(StructBase)`

```python
unreal.ActorInstanceHandle.__init__() -> None
```

## `unreal.ActorIterator(object)`

```python
unreal.ActorIterator.__init__(world: World, type: Union[Class, type] = ...) -> None
```

## `unreal.ActorLayer(StructBase)`

```python
unreal.ActorLayer.__init__(name: Name = "None") -> None
unreal.ActorLayer.name(value: Name) -> None
```

## `unreal.ActorOnClickedSignature(MulticastDelegateBase)`

```python
unreal.ActorOnClickedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorOnInputTouchBeginSignature(MulticastDelegateBase)`

```python
unreal.ActorOnInputTouchBeginSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorOnInputTouchEndSignature(MulticastDelegateBase)`

```python
unreal.ActorOnInputTouchEndSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorOnReleasedSignature(MulticastDelegateBase)`

```python
unreal.ActorOnReleasedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorPerceptionBlueprintInfo(StructBase)`

```python
unreal.ActorPerceptionBlueprintInfo.__init__(target: Actor = None, last_sensed_stimuli: Array[AIStimulus] = [], is_hostile: bool = False, is_friendly: bool = False) -> None
unreal.ActorPerceptionBlueprintInfo.is_friendly(value: bool) -> None
unreal.ActorPerceptionBlueprintInfo.is_hostile(value: bool) -> None
unreal.ActorPerceptionBlueprintInfo.last_sensed_stimuli(value: Array[AIStimulus]) -> None
unreal.ActorPerceptionBlueprintInfo.target(value: Actor) -> None
```

## `unreal.ActorPerceptionForgetUpdatedDelegate(MulticastDelegateBase)`

```python
unreal.ActorPerceptionForgetUpdatedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorPerceptionInfoUpdatedDelegate(MulticastDelegateBase)`

```python
unreal.ActorPerceptionInfoUpdatedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorPerceptionUpdateInfo(StructBase)`

```python
unreal.ActorPerceptionUpdateInfo.__init__(target_id: int = 0, target: Actor = None, stimulus: AIStimulus = [340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000, -1.000000, [340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000], [340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000], "None", False]) -> None
unreal.ActorPerceptionUpdateInfo.stimulus(value: AIStimulus) -> None
unreal.ActorPerceptionUpdateInfo.target(value: Actor) -> None
unreal.ActorPerceptionUpdateInfo.target_id(value: int) -> None
```

## `unreal.ActorPerceptionUpdatedDelegate(MulticastDelegateBase)`

```python
unreal.ActorPerceptionUpdatedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ActorRecordedProperty(StructBase)`

```python
unreal.ActorRecordedProperty.__init__(property_name: Name = "None", enabled: bool = False) -> None
unreal.ActorRecordedProperty.enabled(value: bool) -> None
unreal.ActorRecordedProperty.property_name(value: Name) -> None
```

## `unreal.ActorRecorderPropertyMap(Object)`

```python
unreal.ActorRecorderPropertyMap.children(value: Array[ActorRecorderPropertyMap]) -> None
unreal.ActorRecorderPropertyMap.properties(value: Array[ActorRecordedProperty]) -> None
```

## `unreal.ActorSequenceComponent(ActorComponent)`

```python
unreal.ActorSequenceComponent.pause_sequence() -> None
unreal.ActorSequenceComponent.play_sequence() -> None
unreal.ActorSequenceComponent.sequence_player() -> ActorSequencePlayer
unreal.ActorSequenceComponent.stop_sequence() -> None
```

## `unreal.ActorSoundParameterInterface(Interface)`

```python
unreal.ActorSoundParameterInterface.get_actor_sound_params() -> Array[AudioParameter]
```

## `unreal.ActorTickFunction(TickFunction)`

```python
unreal.ActorTickFunction.__init__() -> None
```

## `unreal.AesAssetActorBase(Actor)`

```python
unreal.AesAssetActorBase.all_child_assets(value: Array[AesAssetChildMetaData]) -> None
unreal.AesAssetActorBase.asset_library(value: DataTable) -> None
unreal.AesAssetActorBase.auto_correct_curve(value: bool) -> None
unreal.AesAssetActorBase.auto_preview(value: bool) -> None
unreal.AesAssetActorBase.build_asset() -> None
unreal.AesAssetActorBase.build_in_game_thread(value: bool) -> None
unreal.AesAssetActorBase.child_assets(value: Array[AesAssetChildMetaData]) -> None
unreal.AesAssetActorBase.child_index_color(value: Color) -> None
unreal.AesAssetActorBase.child_index_world_size(value: float) -> None
unreal.AesAssetActorBase.collision_data(value: AesAssetCollisionData) -> None
unreal.AesAssetActorBase.convert_dynamic_mesh_to_static_mesh(value: bool) -> None
unreal.AesAssetActorBase.create_asset() -> None
unreal.AesAssetActorBase.debug_asset() -> None
unreal.AesAssetActorBase.destroy_asset() -> None
unreal.AesAssetActorBase.get_spline_curves() -> AesSplineCurves
unreal.AesAssetActorBase.has_per_instance_hit_proxies(value: bool) -> None
unreal.AesAssetActorBase.load_from_library() -> None
unreal.AesAssetActorBase.meta_data(value: AesAssetMetaData) -> None
unreal.AesAssetActorBase.preview_index(value: int) -> None
unreal.AesAssetActorBase.preview_lod(value: int) -> None
unreal.AesAssetActorBase.preview_lod_max(value: int) -> None
unreal.AesAssetActorBase.preview_name() -> Name
unreal.AesAssetActorBase.primitive_components(value: Array[PrimitiveComponent]) -> None
unreal.AesAssetActorBase.random_seed(value: int) -> None
unreal.AesAssetActorBase.register_asset() -> None
unreal.AesAssetActorBase.save_child_assets(value: bool) -> None
unreal.AesAssetActorBase.save_to_library() -> None
unreal.AesAssetActorBase.set_spline_curves(spline_curves: AesSplineCurves) -> None
unreal.AesAssetActorBase.show_child_index(value: bool) -> None
unreal.AesAssetActorBase.show_registered_components(value: bool) -> None
unreal.AesAssetActorBase.size_data(value: AesAssetSizeData) -> None
unreal.AesAssetActorBase.spline_component(value: SplineComponent) -> None
unreal.AesAssetActorBase.sync_asset_data(reverse: bool = False) -> None
unreal.AesAssetActorBase.text_render_components(value: Array[TextRenderComponent]) -> None
```

## `unreal.AesEditorUISubsystem(WorldSubsystem)`

```python
unreal.AesEditorUISubsystem.aes_editor_main_ui() -> UserWidget
unreal.AesEditorUISubsystem.aes_editor_ui_hide_event(value: AesEditorUIHideEvent) -> None
unreal.AesEditorUISubsystem.aes_editor_ui_show_event(value: AesEditorUIShowEvent) -> None
unreal.AesEditorUISubsystem.aes_probe_ui() -> UserWidget
unreal.AesEditorUISubsystem.close_ui() -> None
unreal.AesEditorUISubsystem.enter_free_mode() -> None
unreal.AesEditorUISubsystem.get_asset_tooltip_texture(guid: str) -> Texture2D
unreal.AesEditorUISubsystem.is_aes_editor_main_ui_enabled() -> bool
unreal.AesEditorUISubsystem.open_probe_ui() -> None
unreal.AesEditorUISubsystem.open_ui() -> None
unreal.AesEditorUISubsystem.set_aes_editor_main_ui_enabled(enabled: bool) -> None
```

## `unreal.AesFacadeAssetActor(AesAssetActorBase)`

```python
unreal.AesFacadeAssetActor.tag_data(value: AesFacadeAssetTagData) -> None
```

## `unreal.AesFacadeLevelData(StructBase)`

```python
unreal.AesFacadeLevelData.__init__(module_grammar: str = "", height: float = 0.000000, weight: float = 0.000000, variations: Map[Name, float] = {}) -> None
unreal.AesFacadeLevelData.height(value: float) -> None
unreal.AesFacadeLevelData.module_grammar(value: str) -> None
unreal.AesFacadeLevelData.variations(value: Map[Name, float]) -> None
unreal.AesFacadeLevelData.weight(value: float) -> None
```

## `unreal.AesGridLayoutAssetActor(AesAssetActorBase)`

```python
unreal.AesGridLayoutAssetActor.tag_data(value: AesGridLayoutAssetTagData) -> None
```

## `unreal.AesInstanceSplineAssetActor(AesAssetActorBase)`

```python
unreal.AesInstanceSplineAssetActor.load_data_from_asset() -> None
unreal.AesInstanceSplineAssetActor.tag_data(value: AesInstanceSplineAssetTagData) -> None
```

## `unreal.AesLandmarkAssetActor(AesAssetActorBase)`

```python
unreal.AesLandmarkAssetActor.load_data_from_asset() -> None
unreal.AesLandmarkAssetActor.tag_data(value: AesLandmarkAssetTagData) -> None
```

## `unreal.AesMaterialLevelRange(StructBase)`

```python
unreal.AesMaterialLevelRange.__init__() -> None
```

## `unreal.AesModularBuildingAssetActor(AesAssetActorBase)`

```python
unreal.AesModularBuildingAssetActor.load_data_from_asset() -> None
unreal.AesModularBuildingAssetActor.save_outlines(value: bool) -> None
unreal.AesModularBuildingAssetActor.tag_data(value: AesModularBuildingAssetTagData) -> None
```

## `unreal.AesObjectAssetActor(AesAssetActorBase)`

```python
unreal.AesObjectAssetActor.load_data_from_asset() -> None
unreal.AesObjectAssetActor.tag_data(value: AesObjectAssetTagData) -> None
```

## `unreal.AesPOISubsystem(TickableWorldSubsystem)`

```python
unreal.AesPOISubsystem.aes_poi_main_ui() -> UserWidget
unreal.AesPOISubsystem.get_poi_enabled() -> bool
unreal.AesPOISubsystem.set_poi_enabled(enabled: bool) -> None
```

## `unreal.AesRenderResourceBatchCounterFactors(StructBase)`

```python
unreal.AesRenderResourceBatchCounterFactors.__init__() -> None
```

## `unreal.AesRoadActor(Actor)`

```python
unreal.AesRoadActor.debug_mode(value: bool) -> None
unreal.AesRoadActor.destroy_all_render_resource() -> None
unreal.AesRoadActor.entity_type(value: RoadEntityType) -> None
```

## `unreal.AesRoadLaneAssetActor(AesAssetActorBase)`

```python
unreal.AesRoadLaneAssetActor.load_mesh_from_asset() -> None
unreal.AesRoadLaneAssetActor.tag_data(value: AesRoadLaneAssetTagData) -> None
```

## `unreal.AesRoofAssetActor(AesAssetActorBase)`

```python
unreal.AesRoofAssetActor.tag_data(value: AesRoofAssetTagData) -> None
```

## `unreal.AesSlotAssetActor(AesAssetActorBase)`

```python
unreal.AesSlotAssetActor.tag_data_list(value: Array[AesSlotAssetTagData]) -> None
```

## `unreal.AesTilesSubsystem(WorldSubsystem)`

```python
unreal.AesTilesSubsystem.create_aes_tiles_entity(space_id: str, range_b_box: Array[Vector2D], version: str) -> Optional[int]
unreal.AesTilesSubsystem.create_aes_tiles_entity_with_out_grpc(uri: str) -> Optional[int]
```

## `unreal.AesWorldBuilderLayer(StructBase)`

```python
unreal.AesWorldBuilderLayer.__init__() -> None
```

## `unreal.AesWorldTerrainBuilderLayer(AesWorldBuilderLayer)`

```python
unreal.AesWorldTerrainBuilderLayer.__init__() -> None
```

## `unreal.AnimDetailControlsProxyTransform(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyTransform.location(value: AnimDetailProxyLocation) -> None
unreal.AnimDetailControlsProxyTransform.rotation(value: AnimDetailProxyRotation) -> None
unreal.AnimDetailControlsProxyTransform.scale(value: AnimDetailProxyScale) -> None
```

## `unreal.AnimSequenceLevelSequenceLink(AssetUserData)`

```python
unreal.AnimSequenceLevelSequenceLink.path_to_level_sequence(value: SoftObjectPath) -> None
unreal.AnimSequenceLevelSequenceLink.skel_track_guid(value: Guid) -> None
```

## `unreal.ApplyRootMotionMoveToActorForceDelegate(MulticastDelegateBase)`

```python
unreal.ApplyRootMotionMoveToActorForceDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AssetEditorSubsystem(EditorSubsystem)`

```python
unreal.AssetEditorSubsystem.close_all_editors_for_asset(asset: Object) -> int
unreal.AssetEditorSubsystem.open_editor_for_assets(assets: Array[Object], opened_method: AssetTypeActivationOpenedMethod = AssetTypeActivationOpenedMethod.EDIT) -> bool
```

## `unreal.AssetTagsSubsystem(EngineSubsystem)`

```python
unreal.AssetTagsSubsystem.add_asset_data_to_collection(name: Name, asset_data: AssetData) -> bool
unreal.AssetTagsSubsystem.add_asset_datas_to_collection(name: Name, asset_datas: Array[AssetData]) -> bool
unreal.AssetTagsSubsystem.add_asset_ptr_to_collection(name: Name, asset_ptr: Object) -> bool
unreal.AssetTagsSubsystem.add_asset_ptrs_to_collection(name: Name, asset_ptrs: Array[Object]) -> bool
unreal.AssetTagsSubsystem.add_asset_to_collection(name: Name, asset_path_name: Name) -> bool
unreal.AssetTagsSubsystem.add_assets_to_collection(name: Name, asset_path_names: Array[Name]) -> bool
unreal.AssetTagsSubsystem.collection_exists(name: Name) -> bool
unreal.AssetTagsSubsystem.create_collection(name: Name, share_type: CollectionShareType) -> bool
unreal.AssetTagsSubsystem.destroy_collection(name: Name) -> bool
unreal.AssetTagsSubsystem.empty_collection(name: Name) -> bool
unreal.AssetTagsSubsystem.get_assets_in_collection(name: Name) -> Array[AssetData]
unreal.AssetTagsSubsystem.get_collections() -> Array[Name]
unreal.AssetTagsSubsystem.get_collections_containing_asset(asset_path_name: Name) -> Array[Name]
unreal.AssetTagsSubsystem.get_collections_containing_asset_data(asset_data: AssetData) -> Array[Name]
unreal.AssetTagsSubsystem.get_collections_containing_asset_ptr(asset_ptr: Object) -> Array[Name]
unreal.AssetTagsSubsystem.k2_add_asset_to_collection(name: Name, asset_path: SoftObjectPath) -> bool
unreal.AssetTagsSubsystem.k2_add_assets_to_collection(name: Name, asset_paths: Array[SoftObjectPath]) -> bool
unreal.AssetTagsSubsystem.k2_get_collections_containing_asset(asset_path: SoftObjectPath) -> Array[Name]
unreal.AssetTagsSubsystem.k2_remove_asset_from_collection(name: Name, asset_path: SoftObjectPath) -> bool
unreal.AssetTagsSubsystem.k2_remove_assets_from_collection(name: Name, asset_paths: Array[SoftObjectPath]) -> bool
unreal.AssetTagsSubsystem.remove_asset_data_from_collection(name: Name, asset_data: AssetData) -> bool
unreal.AssetTagsSubsystem.remove_asset_datas_from_collection(name: Name, asset_datas: Array[AssetData]) -> bool
unreal.AssetTagsSubsystem.remove_asset_from_collection(name: Name, asset_path_name: Name) -> bool
unreal.AssetTagsSubsystem.remove_asset_ptr_from_collection(name: Name, asset_ptr: Object) -> bool
unreal.AssetTagsSubsystem.remove_asset_ptrs_from_collection(name: Name, asset_ptrs: Array[Object]) -> bool
unreal.AssetTagsSubsystem.remove_assets_from_collection(name: Name, asset_path_names: Array[Name]) -> bool
unreal.AssetTagsSubsystem.rename_collection(name: Name, new_name: Name) -> bool
unreal.AssetTagsSubsystem.reparent_collection(name: Name, new_parent_name: Name) -> bool
```

## `unreal.AsyncEditorOpenMapAndFocusActor(EditorUtilityBlueprintAsyncActionBase)`

```python
unreal.AsyncEditorOpenMapAndFocusActor.complete(value: AsyncDelayComplete) -> None
```

## `unreal.AsyncEditorWaitForGameWorld(EditorUtilityBlueprintAsyncActionBase)`

```python
unreal.AsyncEditorWaitForGameWorld.complete(value: AsyncEditorWaitForGameWorldEvent) -> None
```

## `unreal.AsyncEditorWaitForGameWorldEvent(MulticastDelegateBase)`

```python
unreal.AsyncEditorWaitForGameWorldEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioDeviceNotificationSubsystem(EngineSubsystem)`

```python
unreal.AudioDeviceNotificationSubsystem.default_capture_device_changed(value: OnAudioDefaultDeviceChanged) -> None
unreal.AudioDeviceNotificationSubsystem.default_render_device_changed(value: OnAudioDefaultDeviceChanged) -> None
unreal.AudioDeviceNotificationSubsystem.device_added(value: OnAudioDeviceChange) -> None
unreal.AudioDeviceNotificationSubsystem.device_removed(value: OnAudioDeviceChange) -> None
unreal.AudioDeviceNotificationSubsystem.device_state_changed(value: OnAudioDeviceStateChanged) -> None
unreal.AudioDeviceNotificationSubsystem.device_switched(value: OnAudioDeviceChange) -> None
```

## `unreal.AutomatedLevelSequenceCapture(MovieSceneCapture)`

```python
unreal.AutomatedLevelSequenceCapture.burn_in_options(value: LevelSequenceBurnInOptions) -> None
unreal.AutomatedLevelSequenceCapture.custom_end_frame(value: FrameNumber) -> None
unreal.AutomatedLevelSequenceCapture.custom_start_frame(value: FrameNumber) -> None
unreal.AutomatedLevelSequenceCapture.delay_before_shot_warm_up(value: float) -> None
unreal.AutomatedLevelSequenceCapture.delay_before_warm_up(value: float) -> None
unreal.AutomatedLevelSequenceCapture.delay_every_frame(value: float) -> None
unreal.AutomatedLevelSequenceCapture.level_sequence_asset(value: SoftObjectPath) -> None
unreal.AutomatedLevelSequenceCapture.shot_name(value: str) -> None
unreal.AutomatedLevelSequenceCapture.use_custom_end_frame(value: bool) -> None
unreal.AutomatedLevelSequenceCapture.use_custom_start_frame(value: bool) -> None
unreal.AutomatedLevelSequenceCapture.warm_up_frame_count(value: int) -> None
unreal.AutomatedLevelSequenceCapture.write_edit_decision_list(value: bool) -> None
unreal.AutomatedLevelSequenceCapture.write_final_cut_pro_xml(value: bool) -> None
```

## `unreal.BakedTerrainsActor(Actor)`

```python
unreal.BakedTerrainsActor.load() -> None
unreal.BakedTerrainsActor.terrain_path(value: DirectoryPath) -> None
unreal.BakedTerrainsActor.unload() -> None
```

## `unreal.BaseMaterialTranslationSubsystem(GameInstanceSubsystem)`

```python
unreal.BaseMaterialTranslationSubsystem.toggle_bmt_enable() -> None
```

## `unreal.CableActor(Actor)`

```python
unreal.CableActor.cable_component() -> CableComponent
```

## `unreal.CameraActor(Actor)`

```python
unreal.CameraActor.camera_component() -> CameraComponent
unreal.CameraActor.get_auto_activate_player_index() -> int
unreal.CameraActor.scene_component() -> SceneComponent
```

## `unreal.CameraShakeSourceActor(Actor)`

```python
unreal.CameraShakeSourceActor.camera_shake_source_component() -> CameraShakeSourceComponent
```

## `unreal.CausticsGeneratorActor(Actor)`

```python
unreal.CausticsGeneratorActor.default_scene_root(value: SceneComponent) -> None
unreal.CausticsGeneratorActor.editor_tick(delta_seconds: float) -> None
unreal.CausticsGeneratorActor.set_editor_tick_enabled(enabled: bool) -> None
unreal.CausticsGeneratorActor.spawn_caustic_particle_grid(hismc: HierarchicalInstancedStaticMeshComponent, grid_size: float, grid_tiles: int) -> None
unreal.CausticsGeneratorActor.spawn_water_preview_grid(hismc: HierarchicalInstancedStaticMeshComponent, grid_size: float, grid_tiles: int) -> None
```

## `unreal.CesiumGlobeAnchoredActorComponent(ActorComponent)`

```python
unreal.CesiumGlobeAnchoredActorComponent.globe_anchor() -> CesiumGlobeAnchorComponent
```

## `unreal.CesiumSubLevel(StructBase)`

```python
unreal.CesiumSubLevel.__init__() -> None
```

## `unreal.CesiumSubLevelComponent(ActorComponent)`

```python
unreal.CesiumSubLevelComponent.enabled(value: bool) -> None
unreal.CesiumSubLevelComponent.georeference(value: CesiumGeoreference) -> None
unreal.CesiumSubLevelComponent.load_radius(value: float) -> None
unreal.CesiumSubLevelComponent.origin_height(value: float) -> None
unreal.CesiumSubLevelComponent.origin_latitude(value: float) -> None
unreal.CesiumSubLevelComponent.origin_longitude(value: float) -> None
unreal.CesiumSubLevelComponent.resolve_georeference(force_reresolve: bool = False) -> CesiumGeoreference
unreal.CesiumSubLevelComponent.resolved_georeference() -> CesiumGeoreference
unreal.CesiumSubLevelComponent.set_origin_longitude_latitude_height(longitude_latitude_height: Vector) -> None
```

## `unreal.CesiumSubLevelSwitcherComponent(ActorComponent)`

```python
unreal.CesiumSubLevelSwitcherComponent.get_current_sub_level() -> LevelInstance
unreal.CesiumSubLevelSwitcherComponent.get_registered_sub_levels() -> Array[LevelInstance]
unreal.CesiumSubLevelSwitcherComponent.get_target_sub_level() -> LevelInstance
unreal.CesiumSubLevelSwitcherComponent.set_target_sub_level(level_instance: LevelInstance) -> None
```

## `unreal.ChaosClothingInteractor(ClothingInteractor)`

```python
unreal.ChaosClothingInteractor.reset_and_teleport(reset: bool = False, teleport: bool = False) -> None
unreal.ChaosClothingInteractor.set_aerodynamics(drag_coefficient: float = 0.070000, lift_coefficient: float = 0.035000, wind_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.ChaosClothingInteractor.set_anim_drive(anim_drive_stiffness: Vector2D = [0.000000, 1.000000], anim_drive_damping: Vector2D = [0.000000, 1.000000]) -> None
unreal.ChaosClothingInteractor.set_anim_drive_linear(anim_drive_stiffness: float = 0.000000) -> None
unreal.ChaosClothingInteractor.set_backstop(enabled: bool = True) -> None
unreal.ChaosClothingInteractor.set_collision(collision_thickness: float = 1.000000, friction_coefficient: float = 0.800000, use_ccd: bool = False, self_collision_thickness: float = 2.000000) -> None
unreal.ChaosClothingInteractor.set_damping(damping_coefficient: float = 0.010000, local_damping_coefficient: float = 0.000000) -> None
unreal.ChaosClothingInteractor.set_gravity(gravity_scale: float = 1.000000, is_gravity_overridden: bool = False, gravity_override: Vector = [0.000000, 0.000000, -981.000000]) -> None
unreal.ChaosClothingInteractor.set_long_range_attachment(tether_stiffness: Vector2D = [1.000000, 1.000000], tether_scale: Vector2D = [1.000000, 1.000000]) -> None
unreal.ChaosClothingInteractor.set_long_range_attachment_linear(tether_stiffness: float = 1.000000, tether_scale: float = 1.000000) -> None
unreal.ChaosClothingInteractor.set_material(edge_stiffness: Vector2D = [1.000000, 1.000000], bending_stiffness: Vector2D = [1.000000, 1.000000], area_stiffness: Vector2D = [1.000000, 1.000000]) -> None
unreal.ChaosClothingInteractor.set_material_buckling(buckling_ratio: Vector2D = [0.000000, 0.000000], buckling_stiffness: Vector2D = [1.000000, 1.000000]) -> None
unreal.ChaosClothingInteractor.set_material_linear(edge_stiffness: float = 1.000000, bending_stiffness: float = 1.000000, area_stiffness: float = 1.000000) -> None
unreal.ChaosClothingInteractor.set_pressure(pressure: Vector2D = [0.000000, 1.000000]) -> None
unreal.ChaosClothingInteractor.set_velocity_scale(linear_velocity_scale: Vector = [0.750000, 0.750000, 0.750000], angular_velocity_scale: float = 0.750000, fictitious_angular_scale: float = 1.000000) -> None
unreal.ChaosClothingInteractor.set_wind(drag: Vector2D = [0.070000, 0.500000], lift: Vector2D = [0.070000, 0.500000], air_density: float = 0.000001, wind_velocity: Vector = [0.000000, 0.000000, 0.000000], outer_drag: Vector2D = [0.070000, 0.500000], outer_lift: Vector2D = [0.070000, 0.500000]) -> None
```

## `unreal.ChaosSolverActor(Actor)`

```python
unreal.ChaosSolverActor.set_as_current_world_solver() -> None
unreal.ChaosSolverActor.set_solver_active(active: bool) -> None
```

## `unreal.ChildActorComponent(SceneComponent)`

```python
unreal.ChildActorComponent.child_actor() -> Actor
unreal.ChildActorComponent.child_actor_class() -> Class
unreal.ChildActorComponent.set_child_actor_class(class_: Class) -> None
```

## `unreal.CineCameraActor(CameraActor)`

```python
unreal.CineCameraActor.get_cine_camera_component() -> CineCameraComponent
unreal.CineCameraActor.lookat_tracking_settings(value: CameraLookatTrackingSettings) -> None
```

## `unreal.ClothingSimulationInteractor(Object)`

```python
unreal.ClothingSimulationInteractor.cloth_config_updated() -> None
unreal.ClothingSimulationInteractor.disable_gravity_override() -> None
unreal.ClothingSimulationInteractor.enable_gravity_override(vector: Vector) -> None
unreal.ClothingSimulationInteractor.get_clothing_interactor(clothing_asset_name: str) -> ClothingInteractor
unreal.ClothingSimulationInteractor.get_num_cloths() -> int
unreal.ClothingSimulationInteractor.get_num_dynamic_particles() -> int
unreal.ClothingSimulationInteractor.get_num_iterations() -> int
unreal.ClothingSimulationInteractor.get_num_kinematic_particles() -> int
unreal.ClothingSimulationInteractor.get_num_substeps() -> int
unreal.ClothingSimulationInteractor.get_simulation_time() -> float
unreal.ClothingSimulationInteractor.physics_asset_updated() -> None
unreal.ClothingSimulationInteractor.set_anim_drive_spring_stiffness(stiffness: float) -> None
unreal.ClothingSimulationInteractor.set_max_num_iterations(max_num_iterations: int = 10) -> None
unreal.ClothingSimulationInteractor.set_num_iterations(num_iterations: int = 1) -> None
unreal.ClothingSimulationInteractor.set_num_substeps(num_substeps: int = 1) -> None
```

## `unreal.ClothingSimulationInteractorNv(ClothingSimulationInteractor)`

```python
unreal.ClothingSimulationInteractorNv.set_anim_drive_damper_stiffness(stiffness: float) -> None
```

## `unreal.ClusterUnionActor(Actor)`

```python
unreal.ClusterUnionActor.cluster_union() -> ClusterUnionComponent
```

## `unreal.ConcertClientDesktopPresenceActor(ConcertClientPresenceActor)`

```python
unreal.ConcertClientDesktopPresenceActor.desktop_mesh_component() -> StaticMeshComponent
unreal.ConcertClientDesktopPresenceActor.laser_pointer() -> SplineMeshComponent
```

## `unreal.ConcertClientPresenceActor(Actor)`

```python
unreal.ConcertClientPresenceActor.presence_device_type() -> Name
unreal.ConcertClientPresenceActor.presence_mesh_component() -> StaticMeshComponent
unreal.ConcertClientPresenceActor.presence_text_component() -> TextRenderComponent
```

## `unreal.ConcertClientVRPresenceActor(ConcertClientPresenceActor)`

```python
unreal.ConcertClientVRPresenceActor.laser_thickness(value: float) -> None
```

## `unreal.ConstraintSubsystem(EngineSubsystem)`

```python
unreal.ConstraintSubsystem.on_constraint_added_to_system_bp(value: OnConstraintAddedToSystem) -> None
unreal.ConstraintSubsystem.on_constraint_removed_from_system_bp(value: OnConstraintRemovedFromSystem) -> None
```

## `unreal.ConstraintSubsystem_OnConstraintAddedToSystem(MulticastDelegateBase)`

```python
unreal.ConstraintSubsystem_OnConstraintAddedToSystem.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ConstraintSubsystem_OnConstraintRemovedFromSystem(MulticastDelegateBase)`

```python
unreal.ConstraintSubsystem_OnConstraintRemovedFromSystem.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ControlPointMeshActor(Actor)`

```python
unreal.ControlPointMeshActor.control_point_mesh_component() -> ControlPointMeshComponent
```

## `unreal.ControlRigControlActor(Actor)`

```python
unreal.ControlRigControlActor.actor_to_track(value: Actor) -> None
unreal.ControlRigControlActor.cast_shadows(value: bool) -> None
unreal.ControlRigControlActor.clear() -> None
unreal.ControlRigControlActor.color_parameter(value: str) -> None
unreal.ControlRigControlActor.control_rig_class(value: Class) -> None
unreal.ControlRigControlActor.is_selectable(value: bool) -> None
unreal.ControlRigControlActor.material_override(value: MaterialInterface) -> None
unreal.ControlRigControlActor.refresh() -> None
unreal.ControlRigControlActor.refresh_on_tick(value: bool) -> None
unreal.ControlRigControlActor.reset_control_actor() -> None
```

## `unreal.ControlRigForWorldTransforms(StructBase)`

```python
unreal.ControlRigForWorldTransforms.__init__(control_rig: ControlRig = None, control_names: Array[Name] = []) -> None
unreal.ControlRigForWorldTransforms.control_names(value: Array[Name]) -> None
unreal.ControlRigForWorldTransforms.control_rig(value: ControlRig) -> None
```

## `unreal.ControlRigShapeActor(Actor)`

```python
unreal.ControlRigShapeActor.get_global_transform() -> Transform
unreal.ControlRigShapeActor.hovered(value: bool) -> None
unreal.ControlRigShapeActor.on_enabled_changed(is_enabled: bool) -> None
unreal.ControlRigShapeActor.on_hovered_changed(is_selected: bool) -> None
unreal.ControlRigShapeActor.on_manipulating_changed(is_manipulating: bool) -> None
unreal.ControlRigShapeActor.on_selection_changed(is_selected: bool) -> None
unreal.ControlRigShapeActor.on_transform_changed(new_transform: Transform) -> None
unreal.ControlRigShapeActor.selected(value: bool) -> None
unreal.ControlRigShapeActor.set_global_transform(transform: Transform) -> None
unreal.ControlRigShapeActor.static_mesh_component() -> StaticMeshComponent
```

## `unreal.ControlRigTransformWorkflowOptions(ControlRigWorkflowOptions)`

```python
unreal.ControlRigTransformWorkflowOptions.transform_type(value: RigTransformType) -> None
```

## `unreal.ControlToTransformMappings(StructBase)`

```python
unreal.ControlToTransformMappings.__init__() -> None
```

## `unreal.CoveringSubsystem(GameInstanceSubsystem)`

```python
unreal.CoveringSubsystem.get() -> CoveringSubsystem
```

## `unreal.CreateActorParams(StructBase)`

```python
unreal.CreateActorParams.__init__() -> None
unreal.CreateActorParams.template_actor(value: Actor) -> None
```

## `unreal.CreateActorResult(StructBase)`

```python
unreal.CreateActorResult.__init__() -> None
```

## `unreal.CreateProxyMeshActorOptions(JoinStaticMeshActorsOptions)`

```python
unreal.CreateProxyMeshActorOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_proxy_settings: MeshProxySettings = [300, 3.000000, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], 0.000000, [0, 0, 0, 255], 20.000000, 130.000000, 256, ProxyNormalComputationMethod.ANGLE_WEIGHTED, LandscapeCullingPrecision.MEDIUM, False, False, False, False, False, True, False, True, False, True, False, True, False, False, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
unreal.CreateProxyMeshActorOptions.base_package_name(value: str) -> None
unreal.CreateProxyMeshActorOptions.mesh_proxy_settings(value: MeshProxySettings) -> None
unreal.CreateProxyMeshActorOptions.spawn_merged_actor(value: bool) -> None
```

## `unreal.CustomProgramSubsystem(WorldSubsystem)`

```python
unreal.CustomProgramSubsystem.player_controller(value: PlayerController) -> None
```

## `unreal.DCPNodeLevelParam(DCPNodeBaseParam)`

```python
unreal.DCPNodeLevelParam.__init__(node_id: int = 0, level: int = 0) -> None
unreal.DCPNodeLevelParam.level(value: int) -> None
```

## `unreal.DCPNodeTransformAtom(EntityAtomBase)`

```python
unreal.DCPNodeTransformAtom.create_transform_nodes(node_ids: Array[int]) -> bool
unreal.DCPNodeTransformAtom.create_transform_nodes_with_invisible(node_ids: Array[int], invisible_node_ids: Array[int]) -> bool
unreal.DCPNodeTransformAtom.custom_node_transform_find() -> Map[int, int]
unreal.DCPNodeTransformAtom.debug_anchor_transform() -> None
unreal.DCPNodeTransformAtom.flip_coordinate_system() -> bool
unreal.DCPNodeTransformAtom.node_id_to_anchor() -> Map[int, SceneComponent]
unreal.DCPNodeTransformAtom.node_id_to_mesh() -> Map[int, ProceduralMeshComponent]
unreal.DCPNodeTransformAtom.reset_transform_nodes() -> None
unreal.DCPNodeTransformAtom.set_custom_node_transform_find(node_ids_transform_find: Map[int, int]) -> None
unreal.DCPNodeTransformAtom.set_node_location(node_ids_location: Map[int, Vector]) -> None
unreal.DCPNodeTransformAtom.set_node_rotation(node_ids_rotation: Map[int, Rotator]) -> None
unreal.DCPNodeTransformAtom.set_node_scale(node_ids_scale: Map[int, Vector]) -> None
unreal.DCPNodeTransformAtom.set_node_transform(node_ids_transform: Map[int, Transform]) -> None
```

## `unreal.DCPNodeTransformResult(ResultBase)`

```python
unreal.DCPNodeTransformResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.DCPNodeTransformResult.location(value: Vector) -> None
unreal.DCPNodeTransformResult.rotation(value: Rotator) -> None
unreal.DCPNodeTransformResult.scale(value: Vector) -> None
```

## `unreal.DCPSectionTransformParams(StructBase)`

```python
unreal.DCPSectionTransformParams.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotator: Rotator = [0.000000, 0.000000, 0.000000], size: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.DCPSectionTransformParams.location() -> Vector
unreal.DCPSectionTransformParams.rotator() -> Rotator
unreal.DCPSectionTransformParams.size() -> Vector
```

## `unreal.DCPTransformAnchorData(AssetUserData)`

```python
unreal.DCPTransformAnchorData.node_id() -> int
unreal.DCPTransformAnchorData.relative_location() -> Vector
```

## `unreal.DCPTransformAnchorObject(AssetUserData)`

```python
unreal.DCPTransformAnchorObject.anchor_component() -> SceneComponent
```

## `unreal.DCPTransformAtomUtils(BlueprintFunctionLibrary)`

```python
unreal.DCPTransformAtomUtils.get_anchor_component(mesh: SceneComponent) -> Optional[SceneComponent]
```

## `unreal.DCPWorldSubsystem(WorldSubsystem)`

```python
unreal.DCPWorldSubsystem.get() -> DCPWorldSubsystem
```

## `unreal.DataDrivenCVarEngineSubsystem(EngineSubsystem)`

```python
unreal.DataDrivenCVarEngineSubsystem.on_data_driven_c_var_delegate(value: OnDataDrivenCVarChanged) -> None
```

## `unreal.DataDrivenCVarEngineSubsystem_OnDataDrivenCVarChanged(MulticastDelegateBase)`

```python
unreal.DataDrivenCVarEngineSubsystem_OnDataDrivenCVarChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.DataLayerEditorSubsystem(EditorSubsystem)`

```python
unreal.DataLayerEditorSubsystem.add_actor_to_data_layer(actor: Actor, data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.add_actor_to_data_layers(actor: Actor, data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.add_actors_to_data_layer(actors: Array[Actor], data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.add_actors_to_data_layers(actors: Array[Actor], data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.add_selected_actors_to_data_layer(data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.add_selected_actors_to_data_layers(data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.add_to_actor_editor_context(data_layer_instance: DataLayerInstance) -> None
unreal.DataLayerEditorSubsystem.append_actors_from_data_layer(data_layer: DataLayerInstance) -> Array[Actor]
unreal.DataLayerEditorSubsystem.append_actors_from_data_layers(data_layers: Array[DataLayerInstance]) -> Array[Actor]
unreal.DataLayerEditorSubsystem.create_data_layer(parent_data_layer: DataLayerInstance = None) -> DataLayerInstance
unreal.DataLayerEditorSubsystem.create_data_layer_instance(parameters: DataLayerCreationParameters) -> DataLayerInstance
unreal.DataLayerEditorSubsystem.delete_data_layer(data_layer_to_delete: DataLayerInstance) -> None
unreal.DataLayerEditorSubsystem.delete_data_layers(data_layers_to_delete: Array[DataLayerInstance]) -> None
unreal.DataLayerEditorSubsystem.get_actor_editor_context_current_external_data_layer() -> ExternalDataLayerAsset
unreal.DataLayerEditorSubsystem.get_actors_from_data_layer(data_layer: DataLayerInstance) -> Array[Actor]
unreal.DataLayerEditorSubsystem.get_actors_from_data_layers(data_layers: Array[DataLayerInstance]) -> Array[Actor]
unreal.DataLayerEditorSubsystem.get_all_data_layers() -> Array[DataLayerInstance]
unreal.DataLayerEditorSubsystem.get_data_layer(actor_data_layer: ActorDataLayer) -> DataLayerInstance
unreal.DataLayerEditorSubsystem.get_data_layer_from_label(data_layer_label: Name) -> DataLayerInstance
unreal.DataLayerEditorSubsystem.get_data_layer_instance(data_layer_asset: DataLayerAsset) -> DataLayerInstance
unreal.DataLayerEditorSubsystem.get_data_layer_instances(data_layer_assets: Array[DataLayerAsset]) -> Array[DataLayerInstance]
unreal.DataLayerEditorSubsystem.is_actor_valid_for_data_layer(actor: Actor) -> bool
unreal.DataLayerEditorSubsystem.is_actor_valid_for_data_layer_instances(actor: Actor, data_layer_instances: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.make_all_data_layers_visible() -> None
unreal.DataLayerEditorSubsystem.remove_actor_from_all_data_layers(actor: Actor) -> bool
unreal.DataLayerEditorSubsystem.remove_actor_from_data_layer(actor: Actor, data_layer_to_remove: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.remove_actor_from_data_layers(actor: Actor, data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.remove_actors_from_all_data_layers(actors: Array[Actor]) -> bool
unreal.DataLayerEditorSubsystem.remove_actors_from_data_layer(actors: Array[Actor], data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.remove_actors_from_data_layers(actors: Array[Actor], data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.remove_from_actor_editor_context(data_layer_instance: DataLayerInstance) -> None
unreal.DataLayerEditorSubsystem.remove_selected_actors_from_data_layer(data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.remove_selected_actors_from_data_layers(data_layers: Array[DataLayerInstance]) -> bool
unreal.DataLayerEditorSubsystem.rename_data_layer(data_layer: DataLayerInstance, new_data_layer_label: Name) -> bool
unreal.DataLayerEditorSubsystem.select_actors_in_data_layer(data_layer: DataLayerInstance, select: bool, notify: bool, select_even_if_hidden: bool = False) -> bool
unreal.DataLayerEditorSubsystem.select_actors_in_data_layers(data_layers: Array[DataLayerInstance], select: bool, notify: bool, select_even_if_hidden: bool = False) -> bool
unreal.DataLayerEditorSubsystem.set_actor_editor_context_current_external_data_layer(external_data_layer_asset: ExternalDataLayerAsset) -> bool
unreal.DataLayerEditorSubsystem.set_data_layer_is_dynamically_loaded_in_editor(data_layer: DataLayer, is_loaded_in_editor: bool, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.set_data_layer_is_loaded_in_editor(data_layer: DataLayerInstance, is_loaded_in_editor: bool, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.set_data_layer_visibility(data_layer: DataLayerInstance, is_visible: bool) -> None
unreal.DataLayerEditorSubsystem.set_data_layers_is_dynamically_loaded_in_editor(data_layers: Array[DataLayer], is_loaded_in_editor: bool, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.set_data_layers_is_loaded_in_editor(data_layers: Array[DataLayerInstance], is_loaded_in_editor: bool, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.set_data_layers_visibility(data_layers: Array[DataLayerInstance], is_visible: bool) -> None
unreal.DataLayerEditorSubsystem.set_parent_data_layer(data_layer: DataLayerInstance, parent_data_layer: DataLayerInstance) -> bool
unreal.DataLayerEditorSubsystem.set_parent_data_layer_for_data_layers(data_layers: Array[DataLayerInstance], parent_data_layer: DataLayerInstance) -> None
unreal.DataLayerEditorSubsystem.toggle_data_layer_is_dynamically_loaded_in_editor(data_layer: DataLayer, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.toggle_data_layer_is_loaded_in_editor(data_layer: DataLayerInstance, is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.toggle_data_layer_visibility(data_layer: DataLayerInstance) -> None
unreal.DataLayerEditorSubsystem.toggle_data_layers_is_dynamically_loaded_in_editor(data_layers: Array[DataLayer], is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.toggle_data_layers_is_loaded_in_editor(data_layers: Array[DataLayerInstance], is_from_user_change: bool) -> bool
unreal.DataLayerEditorSubsystem.toggle_data_layers_visibility(data_layers: Array[DataLayerInstance]) -> None
unreal.DataLayerEditorSubsystem.update_actor_all_views_visibility(actor: Actor) -> None
unreal.DataLayerEditorSubsystem.update_actor_visibility(actor: Actor, notify_selection_change: bool, redraw_viewports: bool) -> Optional[Tuple[bool, bool]]
unreal.DataLayerEditorSubsystem.update_all_actors_visibility(notify_selection_change: bool, redraw_viewports: bool) -> bool
unreal.DataLayerEditorSubsystem.update_all_view_visibility(data_layer_that_changed: DataLayer) -> None
```

## `unreal.DataLayerSubsystem(WorldSubsystem)`

```python
unreal.DataLayerSubsystem.get_active_data_layer_names() -> Set[Name]
unreal.DataLayerSubsystem.get_data_layer(data_layer: ActorDataLayer) -> DataLayerInstance
unreal.DataLayerSubsystem.get_data_layer_effective_runtime_state(data_layer: ActorDataLayer) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_effective_runtime_state_by_label(data_layer_label: Name) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_from_label(data_layer_label: Name) -> DataLayerInstance
unreal.DataLayerSubsystem.get_data_layer_from_name(data_layer_name: Name) -> DataLayerInstance
unreal.DataLayerSubsystem.get_data_layer_instance_effective_runtime_state(data_layer_asset: DataLayerAsset) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_instance_from_asset(data_layer_asset: DataLayerAsset) -> DataLayerInstance
unreal.DataLayerSubsystem.get_data_layer_instance_runtime_state(data_layer_asset: DataLayerAsset) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_runtime_state(data_layer: ActorDataLayer) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_runtime_state_by_label(data_layer_label: Name) -> DataLayerRuntimeState
unreal.DataLayerSubsystem.get_data_layer_state(data_layer: ActorDataLayer) -> DataLayerStateType
unreal.DataLayerSubsystem.get_data_layer_state_by_label(data_layer_label: Name) -> DataLayerStateType
unreal.DataLayerSubsystem.get_loaded_data_layer_names() -> Set[Name]
unreal.DataLayerSubsystem.on_data_layer_runtime_state_changed(value: OnDataLayerRuntimeStateChanged) -> None
unreal.DataLayerSubsystem.on_data_layer_state_changed(value: OnDataLayerRuntimeStateChanged) -> None
unreal.DataLayerSubsystem.set_data_layer_instance_runtime_state(data_layer_asset: DataLayerAsset, state: DataLayerRuntimeState, is_recursive: bool = False) -> None
unreal.DataLayerSubsystem.set_data_layer_runtime_state(data_layer: ActorDataLayer, state: DataLayerRuntimeState, is_recursive: bool = False) -> None
unreal.DataLayerSubsystem.set_data_layer_runtime_state_by_label(data_layer_label: Name, state: DataLayerRuntimeState, is_recursive: bool = False) -> None
unreal.DataLayerSubsystem.set_data_layer_state(data_layer: ActorDataLayer, state: DataLayerStateType) -> None
unreal.DataLayerSubsystem.set_data_layer_state_by_label(data_layer_label: Name, state: DataLayerStateType) -> None
```

## `unreal.DataRegistrySubsystem(EngineSubsystem)`

```python
unreal.DataRegistrySubsystem.acquire_item_bp(item_id: DataRegistryId, acquire_callback: DataRegistryItemAcquiredBPCallback) -> bool
unreal.DataRegistrySubsystem.conv_data_registry_id_to_string(data_registry_id: DataRegistryId) -> str
unreal.DataRegistrySubsystem.conv_data_registry_type_to_string(data_registry_type: DataRegistryType) -> str
unreal.DataRegistrySubsystem.equal_equal_data_registry_id(a: DataRegistryId, b: DataRegistryId) -> bool
unreal.DataRegistrySubsystem.equal_equal_data_registry_type(a: DataRegistryType, b: DataRegistryType) -> bool
unreal.DataRegistrySubsystem.evaluate_data_registry_curve(item_id: DataRegistryId, input_value: float, default_value: float) -> Tuple[DataRegistrySubsystemGetItemResult, float]
unreal.DataRegistrySubsystem.get_possible_data_registry_id_list(registry_type: DataRegistryType) -> Array[DataRegistryId]
unreal.DataRegistrySubsystem.is_valid_data_registry_id(data_registry_id: DataRegistryId) -> bool
unreal.DataRegistrySubsystem.is_valid_data_registry_type(data_registry_type: DataRegistryType) -> bool
unreal.DataRegistrySubsystem.not_equal_data_registry_id(a: DataRegistryId, b: DataRegistryId) -> bool
unreal.DataRegistrySubsystem.not_equal_data_registry_type(a: DataRegistryType, b: DataRegistryType) -> bool
```

## `unreal.DataflowActor(Actor)`

```python
unreal.DataflowActor.dataflow_component() -> DataflowComponent
```

## `unreal.DataflowSimulationActor(Interface)`

```python
unreal.DataflowSimulationActor.post_dataflow_simulation_tick(simulation_time: float, delta_time: float) -> None
unreal.DataflowSimulationActor.pre_dataflow_simulation_tick(simulation_time: float, delta_time: float) -> None
```

## `unreal.DatasmithAreaLightActor(Actor)`

```python
unreal.DatasmithAreaLightActor.attenuation_radius(value: float) -> None
unreal.DatasmithAreaLightActor.color(value: LinearColor) -> None
unreal.DatasmithAreaLightActor.dimensions(value: Vector2D) -> None
unreal.DatasmithAreaLightActor.ies_brightness_scale(value: float) -> None
unreal.DatasmithAreaLightActor.ies_texture(value: TextureLightProfile) -> None
unreal.DatasmithAreaLightActor.intensity(value: float) -> None
unreal.DatasmithAreaLightActor.intensity_units(value: LightUnits) -> None
unreal.DatasmithAreaLightActor.light_shape(value: DatasmithAreaLightActorShape) -> None
unreal.DatasmithAreaLightActor.light_type(value: DatasmithAreaLightActorType) -> None
unreal.DatasmithAreaLightActor.mobility() -> ComponentMobility
unreal.DatasmithAreaLightActor.rotation(value: Rotator) -> None
unreal.DatasmithAreaLightActor.source_length(value: float) -> None
unreal.DatasmithAreaLightActor.source_radius(value: float) -> None
unreal.DatasmithAreaLightActor.spotlight_inner_angle(value: float) -> None
unreal.DatasmithAreaLightActor.spotlight_outer_angle(value: float) -> None
unreal.DatasmithAreaLightActor.temperature(value: float) -> None
unreal.DatasmithAreaLightActor.use_ies_brightness(value: bool) -> None
```

## `unreal.DatasmithImportedSequencesActor(Actor)`

```python
unreal.DatasmithImportedSequencesActor.imported_sequences(value: Array[LevelSequence]) -> None
unreal.DatasmithImportedSequencesActor.play_level_sequence(sequence_to_play: LevelSequence) -> None
```

## `unreal.DecalActor(Actor)`

```python
unreal.DecalActor.create_dynamic_material_instance() -> MaterialInstanceDynamic
unreal.DecalActor.create_mid_for_decal() -> MaterialInstanceDynamic
unreal.DecalActor.decal() -> DecalComponent
unreal.DecalActor.get_decal_material() -> MaterialInterface
unreal.DecalActor.set_decal_material(new_decal_material: MaterialInterface) -> None
```

## `unreal.DefaultLevelSequenceInstanceData(Object)`

```python
unreal.DefaultLevelSequenceInstanceData.bp_get_transform_origin() -> Transform
unreal.DefaultLevelSequenceInstanceData.transform_origin(value: Transform) -> None
unreal.DefaultLevelSequenceInstanceData.transform_origin_actor(value: Actor) -> None
```

## `unreal.DocumentationActor(Actor)`

```python
unreal.DocumentationActor.billboard() -> MaterialBillboardComponent
unreal.DocumentationActor.document_link(value: str) -> None
```

## `unreal.DynamicMeshActor(Actor)`

```python
unreal.DynamicMeshActor.allocate_compute_mesh() -> DynamicMesh
unreal.DynamicMeshActor.dynamic_mesh_component() -> DynamicMeshComponent
unreal.DynamicMeshActor.enable_compute_mesh_pool(value: bool) -> None
unreal.DynamicMeshActor.free_all_compute_meshes() -> None
unreal.DynamicMeshActor.get_compute_mesh_pool() -> DynamicMeshPool
unreal.DynamicMeshActor.get_dynamic_mesh_component() -> DynamicMeshComponent
unreal.DynamicMeshActor.release_all_compute_meshes() -> None
unreal.DynamicMeshActor.release_compute_mesh(mesh: DynamicMesh) -> bool
```

## `unreal.EarthActorComponentArrayFragment(EarthOutputFragment)`

```python
unreal.EarthActorComponentArrayFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, component_fragments: Array[EarthActorComponentFragment] = []) -> None
unreal.EarthActorComponentArrayFragment.component_fragments(value: Array[EarthActorComponentFragment]) -> None
```

## `unreal.EarthActorComponentFragment(EarthOutputFragment)`

```python
unreal.EarthActorComponentFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, component: ActorComponent = None) -> None
unreal.EarthActorComponentFragment.component(value: ActorComponent) -> None
```

## `unreal.EarthActorEntity(Actor)`

```python
unreal.EarthActorEntity.create_graphics() -> bool
unreal.EarthActorEntity.destroy_graphics() -> bool
unreal.EarthActorEntity.entity_atoms() -> Array[EarthEntityAtomBase]
unreal.EarthActorEntity.entity_init(entity_init_params: EarthEntityInitParams) -> bool
unreal.EarthActorEntity.get_all_entity_atoms() -> Array[EarthEntityAtomBase]
unreal.EarthActorEntity.get_bounding_box() -> Box
unreal.EarthActorEntity.get_entity_atom_by_class(atom_class: Class) -> EarthEntityAtomBase
unreal.EarthActorEntity.get_entity_atoms_class() -> Set[Class]
unreal.EarthActorEntity.get_entity_category() -> EarthCategory
unreal.EarthActorEntity.get_entity_class() -> Class
unreal.EarthActorEntity.get_entity_define_flags() -> EarthEntityDefineFlags
unreal.EarthActorEntity.get_entity_id() -> int
unreal.EarthActorEntity.get_entity_instance_flags() -> EarthEntityInstanceFlags
unreal.EarthActorEntity.get_entity_type() -> Name
unreal.EarthActorEntity.handle_entity_operations(operations: EarthJsonObjectWrapper, operate_entity_time: EarthOperateEntityTime) -> bool
unreal.EarthActorEntity.notify2d_entity_mouse_event(mouse_pos: Vector2D, event_type: Earth2DEntityMouseEventType) -> None
unreal.EarthActorEntity.post_entity_created() -> None
unreal.EarthActorEntity.pre_delete_entity_operation() -> None
unreal.EarthActorEntity.pre_entity_removed() -> None
unreal.EarthActorEntity.should_redraw(atom_changed_data: Map[Class, EarthAtomChangedProperty]) -> bool
unreal.EarthActorEntity.update_graphics(atom_changed_data: Map[Class, EarthAtomChangedProperty]) -> bool
```

## `unreal.EarthActorFragment(EarthOutputFragment)`

```python
unreal.EarthActorFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, actor: Actor = None) -> None
unreal.EarthActorFragment.actor(value: Actor) -> None
```

## `unreal.EarthAssistantActor(Actor)`

```python
unreal.EarthAssistantActor.clear() -> None
unreal.EarthAssistantActor.convert_glb_to_assets() -> None
unreal.EarthAssistantActor.convert_glb_to_changeset() -> None
unreal.EarthAssistantActor.convert_landmark_to_json() -> None
unreal.EarthAssistantActor.export_changeset_geo_json() -> None
unreal.EarthAssistantActor.export_vector_data_to_geo_json() -> None
unreal.EarthAssistantActor.merge_changeset() -> None
unreal.EarthAssistantActor.merge_local_changeset() -> None
unreal.EarthAssistantActor.set_bin_changeset_to_text() -> None
unreal.EarthAssistantActor.set_text_changeset_to_bin() -> None
unreal.EarthAssistantActor.test() -> None
unreal.EarthAssistantActor.test_payload_process() -> None
unreal.EarthAssistantActor.update_chanagesets_to_lastest() -> None
unreal.EarthAssistantActor.update_changesets_to_latest() -> None
unreal.EarthAssistantActor.upgrade_changeset_water_feature_id() -> None
```

## `unreal.EarthControlActor(Actor)`

```python
unreal.EarthControlActor.camera_altitude(value: float) -> None
unreal.EarthControlActor.earth_camera_component() -> EarthCameraComponent
unreal.EarthControlActor.earth_input(value: EarthControlEnhancedInput) -> None
unreal.EarthControlActor.earth_radius(value: float) -> None
unreal.EarthControlActor.fly_to_position(position: EarthFlytoPos, fly_all_time: float = 5.000000) -> None
unreal.EarthControlActor.focus_to_point(world_location: Vector) -> None
unreal.EarthControlActor.get_camera_lon_lat() -> Vector2D
unreal.EarthControlActor.world_center(value: Vector) -> None
```

## `unreal.EarthDemExtractorFragment(EarthTextureExtractorFragment)`

```python
unreal.EarthDemExtractorFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, extract_level: int = 0, texture: TextureRenderTarget2D = None, producer_name: Name = "None", render_target_format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_R8, srgb: bool = False, need_swizzle_channel: bool = False, earth_actor: Actor = None, source_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], target_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], tiles: Array[str] = [], tile_size: IntPoint = [0, 0], dem_extractor_type: EarthDemExtractorType = EarthDemExtractorType.DEM, normalized: bool = False, height_range: Vector2f = [0.000000, 0.000000]) -> None
unreal.EarthDemExtractorFragment.dem_extractor_type(value: EarthDemExtractorType) -> None
unreal.EarthDemExtractorFragment.height_range(value: Vector2f) -> None
unreal.EarthDemExtractorFragment.normalized(value: bool) -> None
```

## `unreal.EarthDemExtractorPrefab(EarthPrefabBase)`

```python
unreal.EarthDemExtractorPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthDerivedPrefabActorFragment(EarthExternalFragment)`

```python
unreal.EarthDerivedPrefabActorFragment.__init__(validated: bool = False, valid: bool = False, derived_prefab_class: Array[ScriptStruct] = []) -> None
unreal.EarthDerivedPrefabActorFragment.derived_prefab_class(value: Array[ScriptStruct]) -> None
```

## `unreal.EarthDomExtractorFragment(EarthTextureExtractorFragment)`

```python
unreal.EarthDomExtractorFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, extract_level: int = 0, texture: TextureRenderTarget2D = None, producer_name: Name = "None", render_target_format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_R8, srgb: bool = False, need_swizzle_channel: bool = False, earth_actor: Actor = None, source_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], target_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], tiles: Array[str] = [], tile_size: IntPoint = [0, 0], dom_extractor_type: EarthDomExtractorType = EarthDomExtractorType.DOM) -> None
unreal.EarthDomExtractorFragment.dom_extractor_type(value: EarthDomExtractorType) -> None
```

## `unreal.EarthDomExtractorPrefab(EarthPrefabBase)`

```python
unreal.EarthDomExtractorPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthFacadeLevelInfo(StructBase)`

```python
unreal.EarthFacadeLevelInfo.__init__(symbol: Name = "None", grammar: str = "", height: float = 0.000000, scalable: bool = False, use_as_placeholder: bool = False, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.EarthFacadeLevelInfo.grammar(value: str) -> None
unreal.EarthFacadeLevelInfo.height(value: float) -> None
unreal.EarthFacadeLevelInfo.scalable(value: bool) -> None
unreal.EarthFacadeLevelInfo.symbol(value: Name) -> None
unreal.EarthFacadeLevelInfo.transform(value: Transform) -> None
unreal.EarthFacadeLevelInfo.use_as_placeholder(value: bool) -> None
```

## `unreal.EarthInstanceTransformsFragment(EarthPropertyFragment)`

```python
unreal.EarthInstanceTransformsFragment.__init__(validated: bool = False, valid: bool = False, transforms: Array[Transform] = []) -> None
unreal.EarthInstanceTransformsFragment.transforms(value: Array[Transform]) -> None
```

## `unreal.EarthPrefabActor(Actor)`

```python
unreal.EarthPrefabActor.algorithm(value: Class) -> None
unreal.EarthPrefabActor.asset_name(value: str) -> None
unreal.EarthPrefabActor.asset_path(value: DirectoryPath) -> None
unreal.EarthPrefabActor.auto_preview(value: bool) -> None
unreal.EarthPrefabActor.bake_asset(value: bool) -> None
unreal.EarthPrefabActor.batch_entity_size(value: int) -> None
unreal.EarthPrefabActor.build() -> None
unreal.EarthPrefabActor.build_delay(value: float) -> None
unreal.EarthPrefabActor.build_in_game_thread(value: bool) -> None
unreal.EarthPrefabActor.build_parallel(value: bool) -> None
unreal.EarthPrefabActor.capture_from_viewport(value: bool) -> None
unreal.EarthPrefabActor.cleanup() -> None
unreal.EarthPrefabActor.cleanup_spatial_data() -> None
unreal.EarthPrefabActor.clear_prefab_asset() -> None
unreal.EarthPrefabActor.convert_dynamic_mesh_to_static_mesh(value: bool) -> None
unreal.EarthPrefabActor.convert_instance_to_static_mesh(value: bool) -> None
unreal.EarthPrefabActor.convert_nanite_static_mesh(value: bool) -> None
unreal.EarthPrefabActor.debug_mode(value: bool) -> None
unreal.EarthPrefabActor.document_link(value: str) -> None
unreal.EarthPrefabActor.execute() -> None
unreal.EarthPrefabActor.force_build_on_begin_play(value: bool) -> None
unreal.EarthPrefabActor.get_prefab_asset() -> EarthPrefabAsset
unreal.EarthPrefabActor.input_collection(value: EarthInputCollection) -> None
unreal.EarthPrefabActor.input_provider(value: EarthInputProviderBase) -> None
unreal.EarthPrefabActor.load_data_from_fragment() -> None
unreal.EarthPrefabActor.load_prefab_asset() -> None
unreal.EarthPrefabActor.load_static_bounds() -> None
unreal.EarthPrefabActor.lod(value: int) -> None
unreal.EarthPrefabActor.lod_max(value: int) -> None
unreal.EarthPrefabActor.on_property_change() -> None
unreal.EarthPrefabActor.open_document_link() -> None
unreal.EarthPrefabActor.output_collection(value: EarthOutputCollection) -> None
unreal.EarthPrefabActor.prefab(value: InstancedStruct) -> None
unreal.EarthPrefabActor.prefab_asset(value: EarthPrefabAsset) -> None
unreal.EarthPrefabActor.prepare() -> None
unreal.EarthPrefabActor.recapture_thumbnail(value: bool) -> None
unreal.EarthPrefabActor.register() -> None
unreal.EarthPrefabActor.register_spatial_data() -> None
unreal.EarthPrefabActor.save_input_collection(value: bool) -> None
unreal.EarthPrefabActor.save_output_collection(value: bool) -> None
unreal.EarthPrefabActor.save_prefab_asset() -> None
unreal.EarthPrefabActor.seed(value: int) -> None
unreal.EarthPrefabActor.set_prefab_asset(prefab_asset: EarthPrefabAsset) -> None
unreal.EarthPrefabActor.thumbnail(value: Texture2D) -> None
```

## `unreal.EarthProbeActor(Actor)`

```python
unreal.EarthProbeActor.altitude() -> float
unreal.EarthProbeActor.data_srs(value: str) -> None
unreal.EarthProbeActor.geo_point(value: Vector) -> None
unreal.EarthProbeActor.lon_lat() -> Vector2D
unreal.EarthProbeActor.origin_point(value: Vector2D) -> None
unreal.EarthProbeActor.probe() -> None
unreal.EarthProbeActor.probe_with_param() -> float
unreal.EarthProbeActor.project_mode(value: ProjectMode) -> None
unreal.EarthProbeActor.quad_key() -> str
unreal.EarthProbeActor.scene_srs(value: str) -> None
```

## `unreal.EarthShapeGrammarLevelInfo(StructBase)`

```python
unreal.EarthShapeGrammarLevelInfo.__init__(symbol: Name = "None", module_grammar: str = "", left_corner_module: str = "", right_corner_module: str = "", height: float = 0.000000, weight: float = 0.000000, min_scale_factor: float = 0.000000, scalable: bool = False, position_offset: Vector = [0.000000, 0.000000, 0.000000], variations: Map[Name, float] = {}) -> None
unreal.EarthShapeGrammarLevelInfo.height(value: float) -> None
unreal.EarthShapeGrammarLevelInfo.left_corner_module(value: str) -> None
unreal.EarthShapeGrammarLevelInfo.min_scale_factor(value: float) -> None
unreal.EarthShapeGrammarLevelInfo.module_grammar(value: str) -> None
unreal.EarthShapeGrammarLevelInfo.position_offset(value: Vector) -> None
unreal.EarthShapeGrammarLevelInfo.right_corner_module(value: str) -> None
unreal.EarthShapeGrammarLevelInfo.scalable(value: bool) -> None
unreal.EarthShapeGrammarLevelInfo.symbol(value: Name) -> None
unreal.EarthShapeGrammarLevelInfo.variations(value: Map[Name, float]) -> None
unreal.EarthShapeGrammarLevelInfo.weight(value: float) -> None
```

## `unreal.EarthTextureExtractor(EarthPrefabActor)`

```python
unreal.EarthTextureExtractor.box_component(value: EarthBoxComponent) -> None
unreal.EarthTextureExtractor.create_overlayer() -> None
unreal.EarthTextureExtractor.create_static_texture() -> None
unreal.EarthTextureExtractor.related_overlayer(value: EarthTextureOverlayer) -> None
unreal.EarthTextureExtractor.save_texture_name(value: str) -> None
unreal.EarthTextureExtractor.texture_extractor(value: Texture) -> None
```

## `unreal.EarthTextureExtractorFragment(EarthOutputFragment)`

```python
unreal.EarthTextureExtractorFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, extract_level: int = 0, texture: TextureRenderTarget2D = None, producer_name: Name = "None", render_target_format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_R8, srgb: bool = False, need_swizzle_channel: bool = False, earth_actor: Actor = None, source_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], target_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False], tiles: Array[str] = [], tile_size: IntPoint = [0, 0]) -> None
unreal.EarthTextureExtractorFragment.earth_actor(value: Actor) -> None
unreal.EarthTextureExtractorFragment.extract_level(value: int) -> None
unreal.EarthTextureExtractorFragment.need_swizzle_channel() -> bool
unreal.EarthTextureExtractorFragment.producer_name() -> Name
unreal.EarthTextureExtractorFragment.render_target_format() -> TextureRenderTargetFormat
unreal.EarthTextureExtractorFragment.source_bounds(value: Box2D) -> None
unreal.EarthTextureExtractorFragment.srgb() -> bool
unreal.EarthTextureExtractorFragment.target_bounds(value: Box2D) -> None
unreal.EarthTextureExtractorFragment.texture(value: TextureRenderTarget2D) -> None
unreal.EarthTextureExtractorFragment.tile_size(value: IntPoint) -> None
unreal.EarthTextureExtractorFragment.tiles(value: Array[str]) -> None
```

## `unreal.EarthTextureExtractorPrefab(EarthPrefabBase)`

```python
unreal.EarthTextureExtractorPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthTransformFragment(EarthExternalFragment)`

```python
unreal.EarthTransformFragment.__init__(validated: bool = False, valid: bool = False, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], world_space: bool = False) -> None
unreal.EarthTransformFragment.transform(value: Transform) -> None
unreal.EarthTransformFragment.world_space(value: bool) -> None
```

## `unreal.EarthVegetationLevelConfig(StructBase)`

```python
unreal.EarthVegetationLevelConfig.__init__() -> None
```

## `unreal.EditorActorSubsystem(EditorSubsystem)`

```python
unreal.EditorActorSubsystem.clear_actor_selection_set() -> None
unreal.EditorActorSubsystem.convert_actors(actors: Array[Actor], actor_class: Class, static_mesh_package_path: str) -> Array[Actor]
unreal.EditorActorSubsystem.delete_selected_actors(world: World) -> None
unreal.EditorActorSubsystem.destroy_actor(actor_to_destroy: Actor) -> bool
unreal.EditorActorSubsystem.destroy_actors(actors_to_destroy: Array[Actor]) -> bool
unreal.EditorActorSubsystem.duplicate_actor(actor_to_duplicate: Actor, to_world: World = None, offset: Vector = [0.000000, 0.000000, 0.000000]) -> Actor
unreal.EditorActorSubsystem.duplicate_actors(actors_to_duplicate: Array[Actor], to_world: World = None, offset: Vector = [0.000000, 0.000000, 0.000000]) -> Array[Actor]
unreal.EditorActorSubsystem.duplicate_selected_actors(world: World) -> None
unreal.EditorActorSubsystem.get_actor_reference(path_to_actor: str) -> Actor
unreal.EditorActorSubsystem.get_all_level_actors() -> Array[Actor]
unreal.EditorActorSubsystem.get_all_level_actors_components() -> Array[ActorComponent]
unreal.EditorActorSubsystem.get_selected_level_actors() -> Array[Actor]
unreal.EditorActorSubsystem.invert_selection(world: World) -> None
unreal.EditorActorSubsystem.on_actor_label_changed(value: OnActorLabelChanged) -> None
unreal.EditorActorSubsystem.on_delete_actors_begin(value: OnDeleteActorsBegin) -> None
unreal.EditorActorSubsystem.on_delete_actors_end(value: OnDeleteActorsEnd) -> None
unreal.EditorActorSubsystem.on_duplicate_actors_begin(value: OnEditCutActorsBegin) -> None
unreal.EditorActorSubsystem.on_duplicate_actors_end(value: OnDuplicateActorsEnd) -> None
unreal.EditorActorSubsystem.on_edit_copy_actors_begin(value: OnEditCopyActorsBegin) -> None
unreal.EditorActorSubsystem.on_edit_copy_actors_end(value: OnEditCopyActorsEnd) -> None
unreal.EditorActorSubsystem.on_edit_cut_actors_begin(value: OnEditCutActorsBegin) -> None
unreal.EditorActorSubsystem.on_edit_cut_actors_end(value: OnEditCutActorsEnd) -> None
unreal.EditorActorSubsystem.on_edit_paste_actors_begin(value: OnEditPasteActorsBegin) -> None
unreal.EditorActorSubsystem.on_edit_paste_actors_end(value: OnEditPasteActorsEnd) -> None
unreal.EditorActorSubsystem.on_new_actors_dropped(value: OnEditNewActorsDropped) -> None
unreal.EditorActorSubsystem.on_new_actors_placed(value: OnEditNewActorsPlaced) -> None
unreal.EditorActorSubsystem.select_all(world: World) -> None
unreal.EditorActorSubsystem.select_all_children(recurse_children: bool) -> None
unreal.EditorActorSubsystem.select_nothing() -> None
unreal.EditorActorSubsystem.set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
unreal.EditorActorSubsystem.set_actor_transform(actor: Actor, world_transform: Transform) -> bool
unreal.EditorActorSubsystem.set_component_transform(scene_component: SceneComponent, world_transform: Transform) -> bool
unreal.EditorActorSubsystem.set_selected_level_actors(actors_to_select: Array[Actor]) -> None
unreal.EditorActorSubsystem.spawn_actor_from_class(actor_class: Class, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], transient: bool = False) -> Actor
unreal.EditorActorSubsystem.spawn_actor_from_object(object_to_use: Object, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], transient: bool = False) -> Actor
```

## `unreal.EditorAssetSubsystem(EditorSubsystem)`

```python
unreal.EditorAssetSubsystem.add_on_extract_asset_from_file(delegate: OnExtractAssetFromFileDynamic) -> None
unreal.EditorAssetSubsystem.checkout_asset(asset_to_checkout: str) -> bool
unreal.EditorAssetSubsystem.checkout_directory(directory_path: str, recursive: bool = True) -> bool
unreal.EditorAssetSubsystem.checkout_loaded_asset(asset_to_checkout: Object) -> bool
unreal.EditorAssetSubsystem.checkout_loaded_assets(assets_to_checkout: Array[Object]) -> bool
unreal.EditorAssetSubsystem.consolidate_assets(asset_to_consolidate_to: Object, assets_to_consolidate: Array[Object]) -> bool
unreal.EditorAssetSubsystem.delete_asset(asset_path_to_delete: str) -> bool
unreal.EditorAssetSubsystem.delete_directory(directory_path: str) -> bool
unreal.EditorAssetSubsystem.delete_loaded_asset(asset_to_delete: Object) -> bool
unreal.EditorAssetSubsystem.delete_loaded_assets(assets_to_delete: Array[Object]) -> bool
unreal.EditorAssetSubsystem.do_assets_exist(asset_paths: Array[str]) -> bool
unreal.EditorAssetSubsystem.does_asset_exist(asset_path: str) -> bool
unreal.EditorAssetSubsystem.does_directory_contain_assets(directory_path: str, recursive: bool = True) -> bool
unreal.EditorAssetSubsystem.does_directory_exist(directory_path: str) -> bool
unreal.EditorAssetSubsystem.duplicate_asset(source_asset_path: str, destination_asset_path: str) -> Object
unreal.EditorAssetSubsystem.duplicate_directory(source_directory_path: str, destination_directory_path: str) -> bool
unreal.EditorAssetSubsystem.duplicate_loaded_asset(source_asset: Object, destination_asset_path: str) -> Object
unreal.EditorAssetSubsystem.find_asset_data(asset_path: str) -> AssetData
unreal.EditorAssetSubsystem.find_package_referencers_for_asset(asset_path: str, load_assets_to_confirm: bool = False) -> Array[str]
unreal.EditorAssetSubsystem.get_all_assets_by_meta_data_tags(required_tags: Set[Name], allowed_classes: Set[Class]) -> Array[AssetData]
unreal.EditorAssetSubsystem.get_asset_filename_length_for_cooking(asset_path: str) -> int
unreal.EditorAssetSubsystem.get_loaded_asset_filename_length_for_cooking(asset: Object) -> int
unreal.EditorAssetSubsystem.get_metadata_tag(object: Object, tag: Name) -> str
unreal.EditorAssetSubsystem.get_metadata_tag_values(object: Object) -> Map[Name, str]
unreal.EditorAssetSubsystem.get_path_name_for_loaded_asset(loaded_asset: Object) -> str
unreal.EditorAssetSubsystem.get_tag_values(asset_path: str) -> Map[Name, str]
unreal.EditorAssetSubsystem.list_assets(directory_path: str, recursive: bool = True, include_folder: bool = False) -> Array[str]
unreal.EditorAssetSubsystem.list_assets_by_tag_value(tag_name: Name, tag_value: str) -> Array[str]
unreal.EditorAssetSubsystem.load_asset(asset_path: str) -> Object
unreal.EditorAssetSubsystem.load_blueprint_class(asset_path: str) -> Class
unreal.EditorAssetSubsystem.make_directory(directory_path: str) -> bool
unreal.EditorAssetSubsystem.remove_metadata_tag(object: Object, tag: Name) -> None
unreal.EditorAssetSubsystem.remove_on_extract_asset_from_file(delegate: OnExtractAssetFromFileDynamic) -> None
unreal.EditorAssetSubsystem.rename_asset(source_asset_path: str, destination_asset_path: str) -> bool
unreal.EditorAssetSubsystem.rename_directory(source_directory_path: str, destination_directory_path: str) -> bool
unreal.EditorAssetSubsystem.rename_loaded_asset(source_asset: Object, destination_asset_path: str) -> bool
unreal.EditorAssetSubsystem.save_asset(asset_to_save: str, only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetSubsystem.save_directory(directory_path: str, only_if_is_dirty: bool = True, recursive: bool = True) -> bool
unreal.EditorAssetSubsystem.save_loaded_asset(asset_to_save: Object, only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetSubsystem.save_loaded_assets(assets_to_save: Array[Object], only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetSubsystem.set_dirty_flag(object: Object, dirty_state: bool) -> bool
unreal.EditorAssetSubsystem.set_metadata_tag(object: Object, tag: Name, value: str) -> None
unreal.EditorAssetSubsystem.sort_by_meta_data(assets: Array[AssetData], meta_data_tag: Name, meta_data_type: EditorAssetMetaDataSortType, sort_order: EditorAssetSortOrder) -> Optional[Array[AssetData]]
```

## `unreal.EditorAssetSubsystem_OnExtractAssetFromFileDynamic(DelegateBase)`

```python
unreal.EditorAssetSubsystem_OnExtractAssetFromFileDynamic.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EditorLevelLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorLevelLibrary.clear_actor_selection_set() -> None
unreal.EditorLevelLibrary.convert_actors(actors: Array[Actor], actor_class: Class, static_mesh_package_path: str) -> Array[Actor]
unreal.EditorLevelLibrary.create_proxy_mesh_actor(actors_to_merge: Array[StaticMeshActor], merge_options: CreateProxyMeshActorOptions) -> Optional[StaticMeshActor]
unreal.EditorLevelLibrary.destroy_actor(actor_to_destroy: Actor) -> bool
unreal.EditorLevelLibrary.editor_end_play() -> None
unreal.EditorLevelLibrary.editor_invalidate_viewports() -> None
unreal.EditorLevelLibrary.editor_play_simulate() -> None
unreal.EditorLevelLibrary.editor_set_game_view(game_view: bool) -> None
unreal.EditorLevelLibrary.eject_pilot_level_actor() -> None
unreal.EditorLevelLibrary.get_actor_reference(path_to_actor: str) -> Actor
unreal.EditorLevelLibrary.get_all_level_actors() -> Array[Actor]
unreal.EditorLevelLibrary.get_all_level_actors_components() -> Array[ActorComponent]
unreal.EditorLevelLibrary.get_editor_world() -> World
unreal.EditorLevelLibrary.get_game_world() -> World
unreal.EditorLevelLibrary.get_level_viewport_camera_info() -> Optional[Tuple[Vector, Rotator]]
unreal.EditorLevelLibrary.get_pie_worlds(include_dedicated_server: bool) -> Array[World]
unreal.EditorLevelLibrary.get_selected_level_actors() -> Array[Actor]
unreal.EditorLevelLibrary.join_static_mesh_actors(actors_to_join: Array[StaticMeshActor], join_options: JoinStaticMeshActorsOptions) -> Actor
unreal.EditorLevelLibrary.load_level(asset_path: str) -> bool
unreal.EditorLevelLibrary.merge_static_mesh_actors(actors_to_merge: Array[StaticMeshActor], merge_options: MergeStaticMeshActorsOptions) -> Optional[StaticMeshActor]
unreal.EditorLevelLibrary.new_level(asset_path: str) -> bool
unreal.EditorLevelLibrary.new_level_from_template(asset_path: str, template_asset_path: str) -> bool
unreal.EditorLevelLibrary.pilot_level_actor(actor_to_pilot: Actor) -> None
unreal.EditorLevelLibrary.replace_mesh_components_materials(mesh_components: Array[MeshComponent], material_to_be_replaced: MaterialInterface, new_material: MaterialInterface) -> None
unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors(actors: Array[Actor], material_to_be_replaced: MaterialInterface, new_material: MaterialInterface) -> None
unreal.EditorLevelLibrary.replace_mesh_components_meshes(mesh_components: Array[StaticMeshComponent], mesh_to_be_replaced: StaticMesh, new_mesh: StaticMesh) -> None
unreal.EditorLevelLibrary.replace_mesh_components_meshes_on_actors(actors: Array[Actor], mesh_to_be_replaced: StaticMesh, new_mesh: StaticMesh) -> None
unreal.EditorLevelLibrary.replace_selected_actors(asset_path: str) -> None
unreal.EditorLevelLibrary.save_all_dirty_levels() -> bool
unreal.EditorLevelLibrary.save_current_level() -> bool
unreal.EditorLevelLibrary.select_nothing() -> None
unreal.EditorLevelLibrary.set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
unreal.EditorLevelLibrary.set_current_level_by_name(level_name: Name) -> bool
unreal.EditorLevelLibrary.set_level_viewport_camera_info(camera_location: Vector, camera_rotation: Rotator) -> None
unreal.EditorLevelLibrary.set_selected_level_actors(actors_to_select: Array[Actor]) -> None
unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class: Class, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], transient: bool = False) -> Actor
unreal.EditorLevelLibrary.spawn_actor_from_object(object_to_use: Object, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], transient: bool = False) -> Actor
```

## `unreal.EditorLevelUtils(Object)`

```python
unreal.EditorLevelUtils.add_level_to_world(world: World, level_package_name: str, level_streaming_class: Class) -> LevelStreaming
unreal.EditorLevelUtils.add_level_to_world_with_transform(world: World, level_package_name: str, level_streaming_class: Class, level_transform: Transform) -> LevelStreaming
unreal.EditorLevelUtils.create_new_streaming_level(level_streaming_class: Class, new_level_path: str = "", move_selected_actors_into_new_level: bool = False) -> LevelStreaming
unreal.EditorLevelUtils.get_levels(world: World) -> Array[Level]
unreal.EditorLevelUtils.make_level_current(streaming_level: LevelStreaming) -> None
unreal.EditorLevelUtils.move_actors_to_level(actors_to_move: Array[Actor], dest_streaming_level: LevelStreaming, warn_about_references: bool = True, warn_about_renaming: bool = True) -> int
unreal.EditorLevelUtils.move_selected_actors_to_level(dest_level: LevelStreaming, warn_about_references: bool = True) -> int
unreal.EditorLevelUtils.remove_level_from_world(level: Level, clear_selection: bool = True, reset_transaction_buffer: bool = True) -> bool
unreal.EditorLevelUtils.set_level_visibility(level: Level, should_be_visible: bool, force_layers_visible: bool, modify_mode: LevelVisibilityDirtyMode = LevelVisibilityDirtyMode.MODIFY_ON_CHANGE) -> None
unreal.EditorLevelUtils.set_levels_visibility(levels: Array[Level], should_be_visible: Array[bool], force_layers_visible: bool, modify_mode: LevelVisibilityDirtyMode = LevelVisibilityDirtyMode.MODIFY_ON_CHANGE) -> None
```

## `unreal.EditorScriptingCreateProxyMeshActorOptions(CreateProxyMeshActorOptions)`

```python
unreal.EditorScriptingCreateProxyMeshActorOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_proxy_settings: MeshProxySettings = [300, 3.000000, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], 0.000000, [0, 0, 0, 255], 20.000000, 130.000000, 256, ProxyNormalComputationMethod.ANGLE_WEIGHTED, LandscapeCullingPrecision.MEDIUM, False, False, False, False, False, True, False, True, False, True, False, True, False, False, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
```

## `unreal.EditorScriptingCreateProxyMeshActorOptions_Deprecated(EditorScriptingJoinStaticMeshActorsOptions_Deprecated)`

```python
unreal.EditorScriptingCreateProxyMeshActorOptions_Deprecated.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_proxy_settings: MeshProxySettings = [300, 3.000000, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], 0.000000, [0, 0, 0, 255], 20.000000, 130.000000, 256, ProxyNormalComputationMethod.ANGLE_WEIGHTED, LandscapeCullingPrecision.MEDIUM, False, False, False, False, False, True, False, True, False, True, False, True, False, False, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
unreal.EditorScriptingCreateProxyMeshActorOptions_Deprecated.base_package_name(value: str) -> None
unreal.EditorScriptingCreateProxyMeshActorOptions_Deprecated.mesh_proxy_settings(value: MeshProxySettings) -> None
unreal.EditorScriptingCreateProxyMeshActorOptions_Deprecated.spawn_merged_actor(value: bool) -> None
```

## `unreal.EditorScriptingJoinStaticMeshActorsOptions(JoinStaticMeshActorsOptions)`

```python
unreal.EditorScriptingJoinStaticMeshActorsOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False) -> None
```

## `unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated(StructBase)`

```python
unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False) -> None
unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.destroy_source_actors(value: bool) -> None
unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.new_actor_label(value: str) -> None
unreal.EditorScriptingJoinStaticMeshActorsOptions_Deprecated.rename_components_from_source(value: bool) -> None
```

## `unreal.EditorScriptingMergeStaticMeshActorsOptions(MergeStaticMeshActorsOptions)`

```python
unreal.EditorScriptingMergeStaticMeshActorsOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_merging_settings: MeshMergingSettings = [256, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], MeshLODSelectionType.CALCULATE_LOD, 0, True, False, False, False, False, False, False, True, False, False, True, True, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
```

## `unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated(EditorScriptingJoinStaticMeshActorsOptions_Deprecated)`

```python
unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_merging_settings: MeshMergingSettings = [256, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], MeshLODSelectionType.CALCULATE_LOD, 0, True, False, False, False, False, False, False, True, False, False, True, True, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated.base_package_name(value: str) -> None
unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated.mesh_merging_settings(value: MeshMergingSettings) -> None
unreal.EditorScriptingMergeStaticMeshActorsOptions_Deprecated.spawn_merged_actor(value: bool) -> None
```

## `unreal.EditorUtilityActor(Actor)`

```python
unreal.EditorUtilityActor.get_input_component() -> InputComponent
unreal.EditorUtilityActor.receives_editor_input(value: bool) -> None
unreal.EditorUtilityActor.run() -> None
```

## `unreal.EditorUtilitySubsystem(EditorSubsystem)`

```python
unreal.EditorUtilitySubsystem.can_run(asset: Object) -> bool
unreal.EditorUtilitySubsystem.close_tab_by_id(new_tab_id: Name) -> bool
unreal.EditorUtilitySubsystem.does_tab_exist(new_tab_id: Name) -> bool
unreal.EditorUtilitySubsystem.find_utility_widget_from_blueprint(blueprint: EditorUtilityWidgetBlueprint) -> EditorUtilityWidget
unreal.EditorUtilitySubsystem.on_begin_pie(value: OnEditorUtilityPIEEvent) -> None
unreal.EditorUtilitySubsystem.on_end_pie(value: OnEditorUtilityPIEEvent) -> None
unreal.EditorUtilitySubsystem.register_and_execute_task(new_task: EditorUtilityTask, optional_parent_task: EditorUtilityTask = None) -> None
unreal.EditorUtilitySubsystem.register_tab_and_get_id(blueprint: EditorUtilityWidgetBlueprint) -> Name
unreal.EditorUtilitySubsystem.register_tab_and_get_id_generated_class(generated_widget_blueprint: WidgetBlueprintGeneratedClass) -> Name
unreal.EditorUtilitySubsystem.release_instance_of_asset(asset: Object) -> None
unreal.EditorUtilitySubsystem.spawn_and_register_tab(blueprint: EditorUtilityWidgetBlueprint) -> EditorUtilityWidget
unreal.EditorUtilitySubsystem.spawn_and_register_tab_and_get_id(blueprint: EditorUtilityWidgetBlueprint) -> Tuple[EditorUtilityWidget, Name]
unreal.EditorUtilitySubsystem.spawn_and_register_tab_and_get_id_generated_class(generated_widget_blueprint: WidgetBlueprintGeneratedClass) -> Tuple[EditorUtilityWidget, Name]
unreal.EditorUtilitySubsystem.spawn_and_register_tab_generated_class(generated_widget_blueprint: WidgetBlueprintGeneratedClass) -> EditorUtilityWidget
unreal.EditorUtilitySubsystem.spawn_and_register_tab_with_id(blueprint: EditorUtilityWidgetBlueprint, tab_id: Name) -> EditorUtilityWidget
unreal.EditorUtilitySubsystem.spawn_and_register_tab_with_id_generated_class(generated_widget_blueprint: WidgetBlueprintGeneratedClass, tab_id: Name) -> EditorUtilityWidget
unreal.EditorUtilitySubsystem.spawn_registered_tab_by_id(new_tab_id: Name) -> bool
unreal.EditorUtilitySubsystem.try_run(asset: Object) -> bool
unreal.EditorUtilitySubsystem.try_run_class(object_class: Class) -> bool
unreal.EditorUtilitySubsystem.unregister_tab_by_id(tab_id: Name) -> bool
```

## `unreal.EditorValidatorSubsystem(EditorSubsystem)`

```python
unreal.EditorValidatorSubsystem.add_validator(validator: EditorValidatorBase) -> None
unreal.EditorValidatorSubsystem.is_asset_valid(asset_data: AssetData, validation_usecase: DataValidationUsecase) -> Tuple[DataValidationResult, Array[Text], Array[Text]]
unreal.EditorValidatorSubsystem.is_object_valid(object: Object, validation_usecase: DataValidationUsecase) -> Tuple[DataValidationResult, Array[Text], Array[Text]]
unreal.EditorValidatorSubsystem.remove_validator(validator: EditorValidatorBase) -> None
unreal.EditorValidatorSubsystem.validate_assets_with_settings(asset_data_list: Array[AssetData], settings: ValidateAssetsSettings) -> Tuple[int, ValidateAssetsResults]
unreal.EditorValidatorSubsystem.validate_changelist(changelist: DataValidationChangelist, settings: ValidateAssetsSettings) -> Tuple[DataValidationResult, ValidateAssetsResults]
unreal.EditorValidatorSubsystem.validate_changelists(changelists: Array[DataValidationChangelist], settings: ValidateAssetsSettings) -> Tuple[DataValidationResult, ValidateAssetsResults]
unreal.EditorValidatorSubsystem.validate_on_save(value: bool) -> None
```

## `unreal.EngineCamerasSubsystem(WorldSubsystem)`

```python
unreal.EngineCamerasSubsystem.is_camera_animation_active(player_controller: PlayerController, handle: CameraAnimationHandle) -> bool
unreal.EngineCamerasSubsystem.play_camera_animation(player_controller: PlayerController, sequence: CameraAnimationSequence, params: CameraAnimationParams) -> CameraAnimationHandle
unreal.EngineCamerasSubsystem.stop_all_camera_animations(player_controller: PlayerController, immediate: bool = False) -> None
unreal.EngineCamerasSubsystem.stop_all_camera_animations_of(player_controller: PlayerController, sequence: CameraAnimationSequence, immediate: bool = False) -> None
unreal.EngineCamerasSubsystem.stop_camera_animation(player_controller: PlayerController, handle: CameraAnimationHandle, immediate: bool = False) -> None
```

## `unreal.EnhancedInputEditorSubsystem(EditorSubsystem)`

```python
unreal.EnhancedInputEditorSubsystem.add_mapping_context(mapping_context: InputMappingContext, priority: int, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputEditorSubsystem.clear_all_mappings() -> None
unreal.EnhancedInputEditorSubsystem.get_all_player_mappable_action_key_mappings() -> Array[EnhancedActionKeyMapping]
unreal.EnhancedInputEditorSubsystem.get_user_settings() -> EnhancedInputUserSettings
unreal.EnhancedInputEditorSubsystem.has_mapping_context(mapping_context: InputMappingContext) -> Optional[int]
unreal.EnhancedInputEditorSubsystem.inject_input_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.inject_input_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.inject_input_vector_for_action(action: InputAction, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.inject_input_vector_for_player_mapping(mapping_name: Name, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.is_consuming_input() -> bool
unreal.EnhancedInputEditorSubsystem.pop_input_component(input_component: InputComponent) -> bool
unreal.EnhancedInputEditorSubsystem.push_input_component(input_component: InputComponent) -> None
unreal.EnhancedInputEditorSubsystem.query_keys_mapped_to_action(action: InputAction) -> Array[Key]
unreal.EnhancedInputEditorSubsystem.query_map_key_in_active_context_set(input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputEditorSubsystem.query_map_key_in_context_set(prioritized_active_contexts: Array[InputMappingContext], input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputEditorSubsystem.remove_mapping_context(mapping_context: InputMappingContext, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputEditorSubsystem.request_rebuild_control_mappings(options: ModifyContextOptions = [True, False, False], rebuild_type: InputMappingRebuildType = InputMappingRebuildType.REBUILD) -> None
unreal.EnhancedInputEditorSubsystem.start_consuming_input() -> None
unreal.EnhancedInputEditorSubsystem.start_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.start_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputEditorSubsystem.stop_consuming_input() -> None
unreal.EnhancedInputEditorSubsystem.stop_continuous_input_injection_for_action(action: InputAction) -> None
unreal.EnhancedInputEditorSubsystem.stop_continuous_input_injection_for_player_mapping(mapping_name: Name) -> None
unreal.EnhancedInputEditorSubsystem.update_value_of_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue) -> None
unreal.EnhancedInputEditorSubsystem.update_value_of_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue) -> None
```

## `unreal.EnhancedInputLocalPlayerSubsystem(LocalPlayerSubsystem)`

```python
unreal.EnhancedInputLocalPlayerSubsystem.add_mapping_context(mapping_context: InputMappingContext, priority: int, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.clear_all_mappings() -> None
unreal.EnhancedInputLocalPlayerSubsystem.control_mappings_rebuilt_delegate(value: OnControlMappingsRebuilt) -> None
unreal.EnhancedInputLocalPlayerSubsystem.get_all_player_mappable_action_key_mappings() -> Array[EnhancedActionKeyMapping]
unreal.EnhancedInputLocalPlayerSubsystem.get_user_settings() -> EnhancedInputUserSettings
unreal.EnhancedInputLocalPlayerSubsystem.has_mapping_context(mapping_context: InputMappingContext) -> Optional[int]
unreal.EnhancedInputLocalPlayerSubsystem.inject_input_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.inject_input_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.inject_input_vector_for_action(action: InputAction, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.inject_input_vector_for_player_mapping(mapping_name: Name, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.query_keys_mapped_to_action(action: InputAction) -> Array[Key]
unreal.EnhancedInputLocalPlayerSubsystem.query_map_key_in_active_context_set(input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputLocalPlayerSubsystem.query_map_key_in_context_set(prioritized_active_contexts: Array[InputMappingContext], input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputLocalPlayerSubsystem.remove_mapping_context(mapping_context: InputMappingContext, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.request_rebuild_control_mappings(options: ModifyContextOptions = [True, False, False], rebuild_type: InputMappingRebuildType = InputMappingRebuildType.REBUILD) -> None
unreal.EnhancedInputLocalPlayerSubsystem.start_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.start_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputLocalPlayerSubsystem.stop_continuous_input_injection_for_action(action: InputAction) -> None
unreal.EnhancedInputLocalPlayerSubsystem.stop_continuous_input_injection_for_player_mapping(mapping_name: Name) -> None
unreal.EnhancedInputLocalPlayerSubsystem.update_value_of_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue) -> None
unreal.EnhancedInputLocalPlayerSubsystem.update_value_of_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue) -> None
```

## `unreal.EnhancedInputLocalPlayerSubsystem_OnControlMappingsRebuilt(MulticastDelegateBase)`

```python
unreal.EnhancedInputLocalPlayerSubsystem_OnControlMappingsRebuilt.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EnhancedInputSubsystemInterface(Interface)`

```python
unreal.EnhancedInputSubsystemInterface.add_mapping_context(mapping_context: InputMappingContext, priority: int, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputSubsystemInterface.clear_all_mappings() -> None
unreal.EnhancedInputSubsystemInterface.get_all_player_mappable_action_key_mappings() -> Array[EnhancedActionKeyMapping]
unreal.EnhancedInputSubsystemInterface.get_user_settings() -> EnhancedInputUserSettings
unreal.EnhancedInputSubsystemInterface.has_mapping_context(mapping_context: InputMappingContext) -> Optional[int]
unreal.EnhancedInputSubsystemInterface.inject_input_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.inject_input_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.inject_input_vector_for_action(action: InputAction, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.inject_input_vector_for_player_mapping(mapping_name: Name, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.query_keys_mapped_to_action(action: InputAction) -> Array[Key]
unreal.EnhancedInputSubsystemInterface.query_map_key_in_active_context_set(input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputSubsystemInterface.query_map_key_in_context_set(prioritized_active_contexts: Array[InputMappingContext], input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputSubsystemInterface.remove_mapping_context(mapping_context: InputMappingContext, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputSubsystemInterface.request_rebuild_control_mappings(options: ModifyContextOptions = [True, False, False], rebuild_type: InputMappingRebuildType = InputMappingRebuildType.REBUILD) -> None
unreal.EnhancedInputSubsystemInterface.start_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.start_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputSubsystemInterface.stop_continuous_input_injection_for_action(action: InputAction) -> None
unreal.EnhancedInputSubsystemInterface.stop_continuous_input_injection_for_player_mapping(mapping_name: Name) -> None
unreal.EnhancedInputSubsystemInterface.update_value_of_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue) -> None
unreal.EnhancedInputSubsystemInterface.update_value_of_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue) -> None
```

## `unreal.EnhancedInputWorldSubsystem(WorldSubsystem)`

```python
unreal.EnhancedInputWorldSubsystem.add_actor_input_component(actor: Actor) -> None
unreal.EnhancedInputWorldSubsystem.add_mapping_context(mapping_context: InputMappingContext, priority: int, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputWorldSubsystem.clear_all_mappings() -> None
unreal.EnhancedInputWorldSubsystem.get_all_player_mappable_action_key_mappings() -> Array[EnhancedActionKeyMapping]
unreal.EnhancedInputWorldSubsystem.get_user_settings() -> EnhancedInputUserSettings
unreal.EnhancedInputWorldSubsystem.has_mapping_context(mapping_context: InputMappingContext) -> Optional[int]
unreal.EnhancedInputWorldSubsystem.inject_input_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.inject_input_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.inject_input_vector_for_action(action: InputAction, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.inject_input_vector_for_player_mapping(mapping_name: Name, value: Vector, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.query_keys_mapped_to_action(action: InputAction) -> Array[Key]
unreal.EnhancedInputWorldSubsystem.query_map_key_in_active_context_set(input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputWorldSubsystem.query_map_key_in_context_set(prioritized_active_contexts: Array[InputMappingContext], input_context: InputMappingContext, action: InputAction, key: Key, blocking_issues: MappingQueryIssueFlag) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
unreal.EnhancedInputWorldSubsystem.remove_actor_input_component(actor: Actor) -> bool
unreal.EnhancedInputWorldSubsystem.remove_mapping_context(mapping_context: InputMappingContext, options: ModifyContextOptions = [True, False, False]) -> None
unreal.EnhancedInputWorldSubsystem.request_rebuild_control_mappings(options: ModifyContextOptions = [True, False, False], rebuild_type: InputMappingRebuildType = InputMappingRebuildType.REBUILD) -> None
unreal.EnhancedInputWorldSubsystem.start_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.start_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue, modifiers: Array[InputModifier], triggers: Array[InputTrigger]) -> None
unreal.EnhancedInputWorldSubsystem.stop_continuous_input_injection_for_action(action: InputAction) -> None
unreal.EnhancedInputWorldSubsystem.stop_continuous_input_injection_for_player_mapping(mapping_name: Name) -> None
unreal.EnhancedInputWorldSubsystem.update_value_of_continuous_input_injection_for_action(action: InputAction, raw_value: InputActionValue) -> None
unreal.EnhancedInputWorldSubsystem.update_value_of_continuous_input_injection_for_player_mapping(mapping_name: Name, raw_value: InputActionValue) -> None
```

## `unreal.EntityBuildLevelLimits(StructBase)`

```python
unreal.EntityBuildLevelLimits.__init__(height: float = 0.000000, area: float = 0.000000) -> None
unreal.EntityBuildLevelLimits.area(value: float) -> None
unreal.EntityBuildLevelLimits.height(value: float) -> None
```

## `unreal.EulerTransform(StructBase)`

```python
unreal.EulerTransform.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.EulerTransform.location(value: Vector) -> None
unreal.EulerTransform.rotation(value: Rotator) -> None
unreal.EulerTransform.scale(value: Vector) -> None
```

## `unreal.FieldSystemActor(Actor)`

```python
unreal.FieldSystemActor.field_system_component() -> FieldSystemComponent
```

## `unreal.FollowActorInterface(Interface)`

```python
unreal.FollowActorInterface.bpi_get_follow_camera_settings() -> Optional[FollowCameraSettings]
unreal.FollowActorInterface.bpi_on_following_end() -> None
unreal.FollowActorInterface.bpi_on_following_start() -> None
```

## `unreal.ForEachActorIteratorSignature(MulticastDelegateBase)`

```python
unreal.ForEachActorIteratorSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GDALTransformLibrary(BlueprintFunctionLibrary)`

```python
unreal.GDALTransformLibrary.get_last_transform_params() -> Tuple[str, str]
unreal.GDALTransformLibrary.lon_lat_to_xyz(lon_lat: Vector) -> Optional[Vector]
unreal.GDALTransformLibrary.lon_lat_to_xyz_batch(lon_lat_array: Array[Vector], geo_srs_from: str = "", geo_srs_to: str = "") -> Optional[Array[Vector]]
unreal.GDALTransformLibrary.update_global_transform(geo_srs_from: str, geo_srs_to: str) -> None
unreal.GDALTransformLibrary.xyz_to_lon_lat(xyz: Vector) -> Optional[Vector]
unreal.GDALTransformLibrary.xyz_to_lon_lat_batch(xyz_array: Array[Vector], geo_srs_from: str = "", geo_srs_to: str = "") -> Optional[Array[Vector]]
```

## `unreal.GameViewportSubsystem(EngineSubsystem)`

```python
unreal.GameViewportSubsystem.add_widget(widget: Widget, slot: GameViewportWidgetSlot) -> bool
unreal.GameViewportSubsystem.add_widget_for_player(widget: Widget, player: LocalPlayer, slot: GameViewportWidgetSlot) -> bool
unreal.GameViewportSubsystem.get_widget_slot(widget: Widget) -> GameViewportWidgetSlot
unreal.GameViewportSubsystem.is_widget_added(widget: Widget) -> bool
unreal.GameViewportSubsystem.remove_widget(widget: Widget) -> None
unreal.GameViewportSubsystem.set_widget_slot(widget: Widget, slot: GameViewportWidgetSlot) -> None
unreal.GameViewportSubsystem.set_widget_slot_desired_size(slot: GameViewportWidgetSlot, size: Vector2D) -> GameViewportWidgetSlot
unreal.GameViewportSubsystem.set_widget_slot_position(slot: GameViewportWidgetSlot, widget: Widget, position: Vector2D, remove_dpi_scale: bool) -> GameViewportWidgetSlot
```

## `unreal.GameplayAbilityActorInfo(StructBase)`

```python
unreal.GameplayAbilityActorInfo.__init__(owner_actor: Actor = None, avatar_actor: Actor = None, player_controller: PlayerController = None, ability_system_component: AbilitySystemComponent = None, skeletal_mesh_component: SkeletalMeshComponent = None, anim_instance: AnimInstance = None, movement_component: MovementComponent = None, affected_anim_instance_tag: Name = "None") -> None
unreal.GameplayAbilityActorInfo.ability_system_component() -> AbilitySystemComponent
unreal.GameplayAbilityActorInfo.affected_anim_instance_tag() -> Name
unreal.GameplayAbilityActorInfo.anim_instance() -> AnimInstance
unreal.GameplayAbilityActorInfo.avatar_actor() -> Actor
unreal.GameplayAbilityActorInfo.movement_component() -> MovementComponent
unreal.GameplayAbilityActorInfo.owner_actor() -> Actor
unreal.GameplayAbilityActorInfo.player_controller() -> PlayerController
unreal.GameplayAbilityActorInfo.skeletal_mesh_component() -> SkeletalMeshComponent
```

## `unreal.GameplayAbilityTargetActor(Actor)`

```python
unreal.GameplayAbilityTargetActor.debug(value: bool) -> None
unreal.GameplayAbilityTargetActor.destroy_on_confirmation() -> bool
unreal.GameplayAbilityTargetActor.filter(value: GameplayTargetDataFilterHandle) -> None
unreal.GameplayAbilityTargetActor.primary_pc() -> PlayerController
unreal.GameplayAbilityTargetActor.reticle_class(value: Class) -> None
unreal.GameplayAbilityTargetActor.reticle_params(value: WorldReticleParameters) -> None
unreal.GameplayAbilityTargetActor.source_actor() -> Actor
unreal.GameplayAbilityTargetActor.start_location() -> GameplayAbilityTargetingLocationInfo
```

## `unreal.GameplayAbilityTargetActor_ActorPlacement(GameplayAbilityTargetActor_GroundTrace)`

```python
unreal.GameplayAbilityTargetActor_ActorPlacement.placed_actor_class(value: Class) -> None
unreal.GameplayAbilityTargetActor_ActorPlacement.placed_actor_material(value: MaterialInterface) -> None
```

## `unreal.GameplayAbilityTargetActor_GroundTrace(GameplayAbilityTargetActor_Trace)`

```python
unreal.GameplayAbilityTargetActor_GroundTrace.collision_height(value: float) -> None
unreal.GameplayAbilityTargetActor_GroundTrace.collision_radius(value: float) -> None
```

## `unreal.GameplayAbilityTargetActor_Radius(GameplayAbilityTargetActor)`

```python
unreal.GameplayAbilityTargetActor_Radius.radius(value: float) -> None
```

## `unreal.GameplayAbilityTargetActor_Trace(GameplayAbilityTargetActor)`

```python
unreal.GameplayAbilityTargetActor_Trace.max_range(value: float) -> None
unreal.GameplayAbilityTargetActor_Trace.trace_affects_aim_pitch(value: bool) -> None
unreal.GameplayAbilityTargetActor_Trace.trace_profile(value: CollisionProfileName) -> None
```

## `unreal.GameplayAbilityTargetData_ActorArray(GameplayAbilityTargetData)`

```python
unreal.GameplayAbilityTargetData_ActorArray.__init__(source_location: GameplayAbilityTargetingLocationInfo = [None, None, None, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "None", GameplayAbilityTargetingLocationType.LITERAL_TRANSFORM]) -> None
unreal.GameplayAbilityTargetData_ActorArray.source_location(value: GameplayAbilityTargetingLocationInfo) -> None
```

## `unreal.GameplayAbilityWorldReticle(Actor)`

```python
unreal.GameplayAbilityWorldReticle.face_owner_flat(value: bool) -> None
unreal.GameplayAbilityWorldReticle.face_toward_source(face_in2d: bool) -> None
unreal.GameplayAbilityWorldReticle.is_target_an_actor() -> bool
unreal.GameplayAbilityWorldReticle.is_target_valid() -> bool
unreal.GameplayAbilityWorldReticle.on_parameters_initialized() -> None
unreal.GameplayAbilityWorldReticle.on_targeting_an_actor(new_value: bool) -> None
unreal.GameplayAbilityWorldReticle.on_valid_target_changed(new_value: bool) -> None
unreal.GameplayAbilityWorldReticle.parameters(value: WorldReticleParameters) -> None
unreal.GameplayAbilityWorldReticle.primary_pc() -> PlayerController
unreal.GameplayAbilityWorldReticle.set_reticle_material_param_float(param_name: Name, value: float) -> None
unreal.GameplayAbilityWorldReticle.set_reticle_material_param_vector(param_name: Name, value: Vector) -> None
unreal.GameplayAbilityWorldReticle.snap_to_targeted_actor(value: bool) -> None
unreal.GameplayAbilityWorldReticle.targeting_actor() -> GameplayAbilityTargetActor
```

## `unreal.GameplayCameraActor(Actor)`

```python
unreal.GameplayCameraActor.camera_component() -> GameplayCameraComponent
```

## `unreal.GameplayCameraSystemActor(Actor)`

```python
unreal.GameplayCameraSystemActor.auto_manage_active_view_target(player_controller: PlayerController) -> None
unreal.GameplayCameraSystemActor.camera_system_component() -> GameplayCameraSystemComponent
unreal.GameplayCameraSystemActor.get_auto_spawned_camera_system_actor(player_controller: PlayerController, force_spawn: bool = False) -> GameplayCameraSystemActor
```

## `unreal.GameplayCueNotify_Actor(Actor)`

```python
unreal.GameplayCueNotify_Actor.end_gameplay_cue() -> None
unreal.GameplayCueNotify_Actor.handle_gameplay_cue(my_target: Actor, event_type: GameplayCueEvent, parameters: GameplayCueParameters) -> None
unreal.GameplayCueNotify_Actor.on_become_relevant(my_target: Actor, parameters: GameplayCueParameters) -> bool
unreal.GameplayCueNotify_Actor.on_burst(my_target: Actor, parameters: GameplayCueParameters) -> bool
unreal.GameplayCueNotify_Actor.on_cease_relevant(my_target: Actor, parameters: GameplayCueParameters) -> bool
unreal.GameplayCueNotify_Actor.on_execute(my_target: Actor, parameters: GameplayCueParameters) -> bool
```

## `unreal.GameplayStatics(BlueprintFunctionLibrary)`

```python
unreal.GameplayStatics.activate_reverb_effect(world_context_object: Object, reverb_effect: ReverbEffect, tag_name: Name, priority: float = 0.000000, volume: float = 0.500000, fade_time: float = 2.000000) -> None
unreal.GameplayStatics.announce_accessible_string(announcement_string: str) -> None
unreal.GameplayStatics.apply_damage(damaged_actor: Actor, base_damage: float, event_instigator: Controller, damage_causer: Actor, damage_type_class: Class) -> float
unreal.GameplayStatics.apply_point_damage(damaged_actor: Actor, base_damage: float, hit_from_direction: Vector, hit_info: HitResult, event_instigator: Controller, damage_causer: Actor, damage_type_class: Class) -> float
unreal.GameplayStatics.apply_radial_damage(world_context_object: Object, base_damage: float, origin: Vector, damage_radius: float, damage_type_class: Class, ignore_actors: Array[Actor], damage_causer: Actor = None, instigated_by_controller: Controller = None, do_full_damage: bool = False, damage_prevention_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY) -> bool
unreal.GameplayStatics.apply_radial_damage_with_falloff(world_context_object: Object, base_damage: float, minimum_damage: float, origin: Vector, damage_inner_radius: float, damage_outer_radius: float, damage_falloff: float, damage_type_class: Class, ignore_actors: Array[Actor], damage_causer: Actor = None, instigated_by_controller: Controller = None, damage_prevention_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY) -> bool
unreal.GameplayStatics.are_any_listeners_within_range(world_context_object: Object, location: Vector, maximum_range: float) -> bool
unreal.GameplayStatics.are_subtitles_enabled() -> bool
unreal.GameplayStatics.blueprint_predict_projectile_path_advanced(world_context_object: Object, predict_params: PredictProjectilePathParams) -> Optional[PredictProjectilePathResult]
unreal.GameplayStatics.blueprint_predict_projectile_path_by_object_type(world_context_object: Object, start_pos: Vector, launch_velocity: Vector, trace_path: bool = True, projectile_radius: float = ..., object_types: Array[ObjectTypeQuery] = ..., trace_complex: bool = ..., actors_to_ignore: Array[Actor] = ..., draw_debug_type: DrawDebugTrace = ..., draw_debug_time: float = ..., sim_frequency: float = 15.000000, max_sim_time: float = 2.000000, override_gravity_z: float = 0.000000) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
unreal.GameplayStatics.blueprint_predict_projectile_path_by_trace_channel(world_context_object: Object, start_pos: Vector, launch_velocity: Vector, trace_path: bool = True, projectile_radius: float = ..., trace_channel: CollisionChannel = CollisionChannel.ECC_WORLD_DYNAMIC, trace_complex: bool = ..., actors_to_ignore: Array[Actor] = ..., draw_debug_type: DrawDebugTrace = ..., draw_debug_time: float = ..., sim_frequency: float = 15.000000, max_sim_time: float = 2.000000, override_gravity_z: float = 0.000000) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
unreal.GameplayStatics.blueprint_suggest_projectile_velocity(world_context_object: Object, start_location: Vector, end_location: Vector, launch_speed: float, override_gravity_z: float, trace_option: SuggestProjVelocityTraceOption, collision_radius: float, favor_high_arc: bool, draw_debug: bool, accept_closest_on_no_solutions: bool = False) -> Optional[Vector]
unreal.GameplayStatics.cancel_async_loading() -> None
unreal.GameplayStatics.clear_sound_mix_class_override(world_context_object: Object, sound_mix_modifier: SoundMix, sound_class: SoundClass, fade_out_time: float = 1.000000) -> None
unreal.GameplayStatics.clear_sound_mix_modifiers(world_context_object: Object) -> None
unreal.GameplayStatics.clear_sound_mode(world_context_object: Object) -> None
unreal.GameplayStatics.create_player(world_context_object: Object, controller_id: int = -1, spawn_player_controller: bool = True) -> PlayerController
unreal.GameplayStatics.create_player_from_platform_user(world_context_object: Object, user_id: PlatformUserId, spawn_player_controller: bool = True) -> PlayerController
unreal.GameplayStatics.create_save_game_object(save_game_class: Class) -> SaveGame
unreal.GameplayStatics.create_sound2d(world_context_object: Object, sound: SoundBase, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, concurrency_settings: SoundConcurrency = None, persist_across_level_transition: bool = False, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.deactivate_reverb_effect(world_context_object: Object, tag_name: Name) -> None
unreal.GameplayStatics.delete_game_in_slot(slot_name: str, user_index: int) -> bool
unreal.GameplayStatics.deproject_scene_capture_component_to_world(scene_capture_component2d: SceneCaptureComponent2D, target_uv: Vector2D) -> Optional[Tuple[Vector, Vector]]
unreal.GameplayStatics.deproject_scene_capture_to_world(scene_capture2d: SceneCapture2D, target_uv: Vector2D) -> Optional[Tuple[Vector, Vector]]
unreal.GameplayStatics.deproject_screen_to_world(player: PlayerController, screen_position: Vector2D) -> Optional[Tuple[Vector, Vector]]
unreal.GameplayStatics.does_save_game_exist(slot_name: str, user_index: int) -> bool
unreal.GameplayStatics.enable_live_streaming(enable: bool = True) -> None
unreal.GameplayStatics.find_collision_uv(hit: HitResult, uv_channel: int) -> Optional[Vector2D]
unreal.GameplayStatics.find_nearest_actor(origin: Vector, actors_to_check: Array[Actor]) -> Tuple[Actor, float]
unreal.GameplayStatics.flush_level_streaming(world_context_object: Object) -> None
unreal.GameplayStatics.get_accurate_real_time() -> Tuple[int, float]
unreal.GameplayStatics.get_active_spatial_plugin_name(world_context_object: Object) -> Name
unreal.GameplayStatics.get_actor_array_average_location(actors: Array[Actor]) -> Vector
unreal.GameplayStatics.get_actor_array_bounds(actors: Array[Actor], only_colliding_components: bool) -> Tuple[Vector, Vector]
unreal.GameplayStatics.get_actor_of_class(world_context_object: Object, actor_class: Class) -> Actor
unreal.GameplayStatics.get_all_actors_of_class(world_context_object: Object, actor_class: Class) -> Array[Actor]
unreal.GameplayStatics.get_all_actors_of_class_with_tag(world_context_object: Object, actor_class: Class, tag: Name) -> Array[Actor]
unreal.GameplayStatics.get_all_actors_with_interface(world_context_object: Object, interface: Class) -> Array[Actor]
unreal.GameplayStatics.get_all_actors_with_tag(world_context_object: Object, tag: Name) -> Array[Actor]
unreal.GameplayStatics.get_audio_time_seconds(world_context_object: Object) -> float
unreal.GameplayStatics.get_available_spatial_plugin_names(world_context_object: Object) -> Array[Name]
unreal.GameplayStatics.get_closest_listener_location(world_context_object: Object, location: Vector, maximum_range: float, allow_attenuation_override: bool) -> Optional[Vector]
unreal.GameplayStatics.get_current_level_name(world_context_object: Object, remove_prefix_string: bool = True) -> str
unreal.GameplayStatics.get_current_reverb_effect(world_context_object: Object) -> ReverbEffect
unreal.GameplayStatics.get_enable_world_rendering(world_context_object: Object) -> bool
unreal.GameplayStatics.get_game_info(world_context_object: Object) -> GameModeBase
unreal.GameplayStatics.get_game_instance(world_context_object: Object) -> GameInstance
unreal.GameplayStatics.get_game_mode(world_context_object: Object) -> GameModeBase
unreal.GameplayStatics.get_game_replication_info(world_context_object: Object) -> GameStateBase
unreal.GameplayStatics.get_game_state(world_context_object: Object) -> GameStateBase
unreal.GameplayStatics.get_global_time_dilation(world_context_object: Object) -> float
unreal.GameplayStatics.get_int_option(options: str, key: str, default_value: int) -> int
unreal.GameplayStatics.get_key_value(pair: str) -> Tuple[str, str]
unreal.GameplayStatics.get_max_audio_channel_count(world_context_object: Object) -> int
unreal.GameplayStatics.get_num_local_player_controllers(world_context_object: Object) -> int
unreal.GameplayStatics.get_num_player_controllers(world_context_object: Object) -> int
unreal.GameplayStatics.get_num_player_states(world_context_object: Object) -> int
unreal.GameplayStatics.get_object_class(object: Object) -> Class
unreal.GameplayStatics.get_platform_name() -> str
unreal.GameplayStatics.get_player_camera(world_context_object: Object, player_index: int) -> PlayerCameraManager
unreal.GameplayStatics.get_player_camera_manager(world_context_object: Object, player_index: int) -> PlayerCameraManager
unreal.GameplayStatics.get_player_character(world_context_object: Object, player_index: int) -> Character
unreal.GameplayStatics.get_player_controller(world_context_object: Object, player_index: int) -> PlayerController
unreal.GameplayStatics.get_player_controller_from_id(world_context_object: Object, controller_id: int) -> PlayerController
unreal.GameplayStatics.get_player_controller_from_platform_user(world_context_object: Object, user_id: PlatformUserId) -> PlayerController
unreal.GameplayStatics.get_player_controller_id(player: PlayerController) -> int
unreal.GameplayStatics.get_player_pawn(world_context_object: Object, player_index: int) -> Pawn
unreal.GameplayStatics.get_player_state(world_context_object: Object, player_state_index: int) -> PlayerState
unreal.GameplayStatics.get_player_state_from_unique_net_id(world_context_object: Object, unique_id: UniqueNetIdRepl) -> PlayerState
unreal.GameplayStatics.get_real_time_seconds(world_context_object: Object) -> float
unreal.GameplayStatics.get_streaming_level(world_context_object: Object, package_name: Name) -> LevelStreaming
unreal.GameplayStatics.get_surface_type(hit: HitResult) -> PhysicalSurface
unreal.GameplayStatics.get_time_seconds(world_context_object: Object) -> float
unreal.GameplayStatics.get_unpaused_time_seconds(world_context_object: Object) -> float
unreal.GameplayStatics.get_view_projection_matrix(desired_view: MinimalViewInfo) -> Tuple[Matrix, Matrix, Matrix]
unreal.GameplayStatics.get_viewport_mouse_capture_mode(world_context_object: Object) -> MouseCaptureMode
unreal.GameplayStatics.get_world_delta_seconds(world_context_object: Object) -> float
unreal.GameplayStatics.get_world_origin_location(world_context_object: Object) -> IntVector
unreal.GameplayStatics.grass_overlapping_sphere_count(world_context_object: Object, static_mesh: StaticMesh, center_position: Vector, radius: float) -> int
unreal.GameplayStatics.has_launch_option(option_to_check: str) -> bool
unreal.GameplayStatics.has_option(options: str, key: str) -> bool
unreal.GameplayStatics.is_any_local_player_camera_within_range(world_context_object: Object, location: Vector, maximum_range: float) -> bool
unreal.GameplayStatics.is_game_paused(world_context_object: Object) -> bool
unreal.GameplayStatics.is_splitscreen_force_disabled(world_context_object: Object) -> bool
unreal.GameplayStatics.k2_set_sound_mode(world_context_object: Object, sound_mix: SoundMix) -> None
unreal.GameplayStatics.load_game_from_slot(slot_name: str, user_index: int) -> SaveGame
unreal.GameplayStatics.load_stream_level(world_context_object: Object, level_name: Name, make_visible_after_load: bool, should_block_on_load: bool, latent_info: LatentActionInfo) -> None
unreal.GameplayStatics.load_stream_level_by_soft_object_ptr(world_context_object: Object, level: World, make_visible_after_load: bool, should_block_on_load: bool, latent_info: LatentActionInfo) -> None
unreal.GameplayStatics.object_is_a(object: Object, object_class: Class) -> bool
unreal.GameplayStatics.open_level(world_context_object: Object, level_name: Name, absolute: bool = True, options: str = "") -> None
unreal.GameplayStatics.open_level_by_soft_object_ptr(world_context_object: Object, level: World, absolute: bool = True, options: str = "") -> None
unreal.GameplayStatics.parse_option(options: str, key: str) -> str
unreal.GameplayStatics.play_dialogue2d(world_context_object: Object, dialogue: DialogueWave, context: DialogueContext, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000) -> None
unreal.GameplayStatics.play_dialogue_at_location(world_context_object: Object, dialogue: DialogueWave, context: DialogueContext, location: Vector, rotation: Rotator, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None) -> None
unreal.GameplayStatics.play_dialogue_attached(dialogue: DialogueWave, context: DialogueContext, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed: bool = False, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.play_sound2d(world_context_object: Object, sound: SoundBase, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, concurrency_settings: SoundConcurrency = None, owning_actor: Actor = None, is_ui_sound: bool = True) -> None
unreal.GameplayStatics.play_sound_at_location(world_context_object: Object, sound: SoundBase, location: Vector, rotation: Rotator, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, concurrency_settings: SoundConcurrency = None, owning_actor: Actor = None, initial_params: InitialActiveSoundParams = None) -> None
unreal.GameplayStatics.play_sound_attached(sound: SoundBase, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed: bool = False, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, concurrency_settings: SoundConcurrency = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.play_world_camera_shake(world_context_object: Object, shake: Class, epicenter: Vector, inner_radius: float, outer_radius: float, falloff: float = 1.000000, orient_shake_towards_epicenter: bool = False) -> None
unreal.GameplayStatics.pop_sound_mix_modifier(world_context_object: Object, sound_mix_modifier: SoundMix) -> None
unreal.GameplayStatics.pop_sound_mode(world_context_object: Object, sound_mix_modifier: SoundMix) -> None
unreal.GameplayStatics.predict_projectile_path(world_context_object: Object, start_pos: Vector, launch_velocity: Vector, trace_path: bool = True, projectile_radius: float = ..., object_types: Array[ObjectTypeQuery] = ..., trace_complex: bool = ..., actors_to_ignore: Array[Actor] = ..., draw_debug_type: DrawDebugTrace = ..., draw_debug_time: float = ..., sim_frequency: float = 15.000000, max_sim_time: float = 2.000000, override_gravity_z: float = 0.000000) -> Optional[Tuple[HitResult, Array[Vector], Vector]]
unreal.GameplayStatics.prime_all_sounds_in_sound_class(sound_class: SoundClass) -> None
unreal.GameplayStatics.prime_sound(sound: SoundBase) -> None
unreal.GameplayStatics.project_world_to_screen(player: PlayerController, world_position: Vector, player_viewport_relative: bool = False) -> Optional[Vector2D]
unreal.GameplayStatics.push_sound_mix_modifier(world_context_object: Object, sound_mix_modifier: SoundMix) -> None
unreal.GameplayStatics.push_sound_mode(world_context_object: Object, sound_mix_modifier: SoundMix) -> None
unreal.GameplayStatics.rebase_local_origin_onto_zero(world_context_object: Object, world_location: Vector) -> Vector
unreal.GameplayStatics.rebase_zero_origin_onto_local(world_context_object: Object, world_location: Vector) -> Vector
unreal.GameplayStatics.remove_player(player: PlayerController, destroy_pawn: bool) -> None
unreal.GameplayStatics.save_game_to_slot(save_game_object: SaveGame, slot_name: str, user_index: int) -> bool
unreal.GameplayStatics.set_active_spatial_plugin_by_name(world_context_object: Object, plugin_name: Name) -> bool
unreal.GameplayStatics.set_base_sound_mix(world_context_object: Object, sound_mix: SoundMix) -> None
unreal.GameplayStatics.set_enable_world_rendering(world_context_object: Object, enable: bool) -> None
unreal.GameplayStatics.set_force_disable_splitscreen(world_context_object: Object, disable: bool) -> None
unreal.GameplayStatics.set_game_paused(world_context_object: Object, paused: bool) -> bool
unreal.GameplayStatics.set_global_listener_focus_parameters(world_context_object: Object, focus_azimuth_scale: float = 1.000000, non_focus_azimuth_scale: float = 1.000000, focus_distance_scale: float = 1.000000, non_focus_distance_scale: float = 1.000000, focus_volume_scale: float = 1.000000, non_focus_volume_scale: float = 1.000000, focus_priority_scale: float = 1.000000, non_focus_priority_scale: float = 1.000000) -> None
unreal.GameplayStatics.set_global_pitch_modulation(world_context_object: Object, pitch_modulation: float, time_sec: float) -> None
unreal.GameplayStatics.set_global_time_dilation(world_context_object: Object, time_dilation: float) -> None
unreal.GameplayStatics.set_max_audio_channels_scaled(world_context_object: Object, max_channel_count_scale: float) -> None
unreal.GameplayStatics.set_player_controller_id(player: PlayerController, controller_id: int) -> None
unreal.GameplayStatics.set_player_platform_user_id(player_controller: PlayerController, user_id: PlatformUserId) -> None
unreal.GameplayStatics.set_sound_class_distance_scale(world_context_object: Object, sound_class: SoundClass, distance_attenuation_scale: float, time_sec: float = 0.000000) -> None
unreal.GameplayStatics.set_sound_mix_class_override(world_context_object: Object, sound_mix_modifier: SoundMix, sound_class: SoundClass, volume: float = 1.000000, pitch: float = 1.000000, fade_in_time: float = 1.000000, apply_to_children: bool = True) -> None
unreal.GameplayStatics.set_subtitles_enabled(enabled: bool) -> None
unreal.GameplayStatics.set_time_dilation(world_context_object: Object, time_dilation: float) -> None
unreal.GameplayStatics.set_viewport_mouse_capture_mode(world_context_object: Object, mouse_capture_mode: MouseCaptureMode) -> None
unreal.GameplayStatics.set_world_origin_location(world_context_object: Object, new_location: IntVector) -> None
unreal.GameplayStatics.spawn_decal_at_location(world_context_object: Object, decal_material: MaterialInterface, decal_size: Vector, location: Vector, rotation: Rotator = [0.000000, -90.000000, 0.000000], life_span: float = 0.000000) -> DecalComponent
unreal.GameplayStatics.spawn_decal_attached(decal_material: MaterialInterface, decal_size: Vector, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, life_span: float = 0.000000) -> DecalComponent
unreal.GameplayStatics.spawn_dialogue2d(world_context_object: Object, dialogue: DialogueWave, context: DialogueContext, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.spawn_dialogue_at_location(world_context_object: Object, dialogue: DialogueWave, context: DialogueContext, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.spawn_dialogue_attached(dialogue: DialogueWave, context: DialogueContext, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed: bool = False, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.spawn_emitter_at_location(world_context_object: Object, emitter_template: ParticleSystem, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [1.000000, 1.000000, 1.000000], auto_destroy: bool = True, pooling_method: PSCPoolMethod = PSCPoolMethod.NONE, auto_activate_system: bool = True) -> ParticleSystemComponent
unreal.GameplayStatics.spawn_emitter_attached(emitter_template: ParticleSystem, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [1.000000, 1.000000, 1.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, auto_destroy: bool = True, pooling_method: PSCPoolMethod = PSCPoolMethod.NONE, auto_activate: bool = True) -> ParticleSystemComponent
unreal.GameplayStatics.spawn_force_feedback_at_location(world_context_object: Object, force_feedback_effect: ForceFeedbackEffect, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], looping: bool = False, intensity_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: ForceFeedbackAttenuation = None, auto_destroy: bool = True) -> ForceFeedbackComponent
unreal.GameplayStatics.spawn_force_feedback_attached(force_feedback_effect: ForceFeedbackEffect, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed: bool = False, looping: bool = False, intensity_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: ForceFeedbackAttenuation = None, auto_destroy: bool = True) -> ForceFeedbackComponent
unreal.GameplayStatics.spawn_sound2d(world_context_object: Object, sound: SoundBase, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, concurrency_settings: SoundConcurrency = None, persist_across_level_transition: bool = False, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.spawn_sound_at_location(world_context_object: Object, sound: SoundBase, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, concurrency_settings: SoundConcurrency = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.spawn_sound_attached(sound: SoundBase, attach_to_component: SceneComponent, attach_point_name: Name = "None", location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, stop_when_attached_to_destroyed: bool = False, volume_multiplier: float = 1.000000, pitch_multiplier: float = 1.000000, start_time: float = 0.000000, attenuation_settings: SoundAttenuation = None, concurrency_settings: SoundConcurrency = None, auto_destroy: bool = True) -> AudioComponent
unreal.GameplayStatics.suggest_projectile_velocity_custom_arc(world_context_object: Object, start_pos: Vector, end_pos: Vector, override_gravity_z: float = 0.000000, arc_param: float = 0.500000) -> Optional[Vector]
unreal.GameplayStatics.suggest_projectile_velocity_moving_target(world_context_object: Object, projectile_start_location: Vector, target_actor: Actor, target_location_offset: Vector = [0.000000, 0.000000, 0.000000], gravity_z_override: float = 0.000000, time_to_target: float = 1.000000, draw_debug_type: DrawDebugTrace = DrawDebugTrace.NONE, draw_debug_time: float = 3.000000, draw_debug_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000]) -> Optional[Vector]
unreal.GameplayStatics.transform_world_to_first_person(view_info: MinimalViewInfo, world_position: Vector, ignore_first_person_scale: bool) -> Vector
unreal.GameplayStatics.un_retain_all_sounds_in_sound_class(sound_class: SoundClass) -> None
unreal.GameplayStatics.unload_stream_level(world_context_object: Object, level_name: Name, latent_info: LatentActionInfo, should_block_on_unload: bool) -> None
unreal.GameplayStatics.unload_stream_level_by_soft_object_ptr(world_context_object: Object, level: World, latent_info: LatentActionInfo, should_block_on_unload: bool) -> None
```

## `unreal.GameplayTaskSpawnActorDelegate(MulticastDelegateBase)`

```python
unreal.GameplayTaskSpawnActorDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GameplayTask_SpawnActor(GameplayTask)`

```python
unreal.GameplayTask_SpawnActor.did_not_spawn(value: GameplayTaskSpawnActorDelegate) -> None
unreal.GameplayTask_SpawnActor.success(value: GameplayTaskSpawnActorDelegate) -> None
```

## `unreal.GeneratedDynamicMeshActor(DynamicMeshActor)`

```python
unreal.GeneratedDynamicMeshActor.copy_properties_from_static_mesh(static_mesh_actor: StaticMeshActor, copy_component_materials: bool = False) -> None
unreal.GeneratedDynamicMeshActor.copy_properties_to_static_mesh(static_mesh_actor: StaticMeshActor, copy_component_materials: bool = False) -> None
unreal.GeneratedDynamicMeshActor.dialog_delay(value: float) -> None
unreal.GeneratedDynamicMeshActor.enable_rebuild_progress(value: bool) -> None
unreal.GeneratedDynamicMeshActor.frozen(value: bool) -> None
unreal.GeneratedDynamicMeshActor.increment_progress(num_steps: int, message: str) -> None
unreal.GeneratedDynamicMeshActor.mark_for_mesh_rebuild(immediate: bool = False, immediate_even_if_frozen: bool = False) -> None
unreal.GeneratedDynamicMeshActor.num_progress_steps(value: int) -> None
unreal.GeneratedDynamicMeshActor.on_rebuild_generated_mesh(target_mesh: DynamicMesh) -> None
unreal.GeneratedDynamicMeshActor.progress_message(value: str) -> None
unreal.GeneratedDynamicMeshActor.reset_on_rebuild(value: bool) -> None
```

## `unreal.GeometryCacheActor(Actor)`

```python
unreal.GeometryCacheActor.geometry_cache_component() -> GeometryCacheComponent
unreal.GeometryCacheActor.get_geometry_cache_component() -> GeometryCacheComponent
```

## `unreal.GeometryCollectionActor(Actor)`

```python
unreal.GeometryCollectionActor.geometry_collection_component() -> GeometryCollectionComponent
unreal.GeometryCollectionActor.raycast_single(start: Vector, end: Vector) -> Optional[HitResult]
```

## `unreal.GeometryCollectionISMPoolActor(Actor)`

```python
unreal.GeometryCollectionISMPoolActor.ism_pool_comp() -> GeometryCollectionISMPoolComponent
unreal.GeometryCollectionISMPoolActor.ism_pool_debug_draw_comp() -> GeometryCollectionISMPoolDebugDrawComponent
```

## `unreal.GeometryCollectionLevelSetData(StructBase)`

```python
unreal.GeometryCollectionLevelSetData.__init__() -> None
```

## `unreal.GeometryCollectionRenderLevelSetActor(Actor)`

```python
unreal.GeometryCollectionRenderLevelSetActor.enabled(value: bool) -> None
unreal.GeometryCollectionRenderLevelSetActor.isovalue(value: float) -> None
unreal.GeometryCollectionRenderLevelSetActor.ray_march_material(value: Material) -> None
unreal.GeometryCollectionRenderLevelSetActor.render_volume_bounding_box(value: bool) -> None
unreal.GeometryCollectionRenderLevelSetActor.surface_tolerance(value: float) -> None
unreal.GeometryCollectionRenderLevelSetActor.target_volume_texture(value: VolumeTexture) -> None
```

## `unreal.GeometryScriptTransformCollisionOptions(StructBase)`

```python
unreal.GeometryScriptTransformCollisionOptions.__init__(warn_on_invalid_transforms: bool = False, center_transform_pivot_per_shape: bool = False) -> None
unreal.GeometryScriptTransformCollisionOptions.center_transform_pivot_per_shape(value: bool) -> None
unreal.GeometryScriptTransformCollisionOptions.warn_on_invalid_transforms(value: bool) -> None
```

## `unreal.GeometryScript_MeshTransforms(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshTransforms.rotate_mesh(target_mesh: DynamicMesh, rotation: Rotator, rotation_origin: Vector = [0.000000, 0.000000, 0.000000], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.rotate_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, rotation: Rotator, rotation_origin: Vector = [0.000000, 0.000000, 0.000000], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.scale_mesh(target_mesh: DynamicMesh, scale: Vector = [1.000000, 1.000000, 1.000000], scale_origin: Vector = [0.000000, 0.000000, 0.000000], fix_orientation_for_negative_scale: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.scale_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, scale: Vector = [1.000000, 1.000000, 1.000000], scale_origin: Vector = [0.000000, 0.000000, 0.000000], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.transform_mesh(target_mesh: DynamicMesh, transform: Transform, fix_orientation_for_negative_scale: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.transform_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, transform: Transform, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.translate_mesh(target_mesh: DynamicMesh, translation: Vector, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.translate_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, translation: Vector, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshTransforms.translate_pivot_to_location(target_mesh: DynamicMesh, pivot_location: Vector, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_Transform(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Transform.get_transform_axis_plane(transform: Transform, axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Plane
unreal.GeometryScript_Transform.get_transform_axis_ray(transform: Transform, axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Ray
unreal.GeometryScript_Transform.get_transform_axis_vector(transform: Transform, axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Vector
unreal.GeometryScript_Transform.make_transform_from_axes(location: Vector, z_axis: Vector, tangent_axis: Vector, tangent_is_x: bool = True) -> Transform
unreal.GeometryScript_Transform.make_transform_from_z_axis(location: Vector, z_axis: Vector) -> Transform
```

## `unreal.GetDCPNodeTransformParam(ParamsBase)`

```python
unreal.GetDCPNodeTransformParam.__init__(node_id: int = 0, coord_type: GetDCPNodeTransformType = GetDCPNodeTransformType.TOP) -> None
unreal.GetDCPNodeTransformParam.coord_type(value: GetDCPNodeTransformType) -> None
unreal.GetDCPNodeTransformParam.node_id(value: int) -> None
```

## `unreal.GroomActor(Actor)`

```python
unreal.GroomActor.groom_component() -> GroomComponent
```

## `unreal.HoldoutCompositeSubsystem(WorldSubsystem)`

```python
unreal.HoldoutCompositeSubsystem.register_primitive(primitive_component: PrimitiveComponent, holdout_state: bool = True) -> None
unreal.HoldoutCompositeSubsystem.unregister_primitive(primitive_component: PrimitiveComponent, holdout_state: bool = False) -> None
```

## `unreal.HttpImageStateSubsystem(GameInstanceSubsystem)`

```python
unreal.HttpImageStateSubsystem.get() -> HttpImageStateSubsystem
unreal.HttpImageStateSubsystem.get_http_image_state(url: str) -> Optional[HttpImageStateData]
unreal.HttpImageStateSubsystem.remove_http_image_state(url: str) -> bool
unreal.HttpImageStateSubsystem.set_http_image_state(url: str, http_image_state: HttpImageState, texture: Texture2DDynamic) -> None
```

## `unreal.IKRig_SetTransformEffector(Object)`

```python
unreal.IKRig_SetTransformEffector.alpha(value: float) -> None
unreal.IKRig_SetTransformEffector.enable_position(value: bool) -> None
unreal.IKRig_SetTransformEffector.enable_rotation(value: bool) -> None
```

## `unreal.ImportSubsystem(EditorSubsystem)`

```python
unreal.ImportSubsystem.on_asset_post_import(value: OnAssetPostImport_Dyn) -> None
unreal.ImportSubsystem.on_asset_post_lod_import(value: OnAssetPostLODImport_Dyn) -> None
unreal.ImportSubsystem.on_asset_pre_import(value: OnAssetPreImport_Dyn) -> None
unreal.ImportSubsystem.on_asset_reimport(value: OnAssetReimport_Dyn) -> None
```

## `unreal.ImportSubsystem_OnAssetPostImport_Dyn(MulticastDelegateBase)`

```python
unreal.ImportSubsystem_OnAssetPostImport_Dyn.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ImportSubsystem_OnAssetPostLODImport_Dyn(MulticastDelegateBase)`

```python
unreal.ImportSubsystem_OnAssetPostLODImport_Dyn.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ImportSubsystem_OnAssetPreImport_Dyn(MulticastDelegateBase)`

```python
unreal.ImportSubsystem_OnAssetPreImport_Dyn.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ImportSubsystem_OnAssetReimport_Dyn(MulticastDelegateBase)`

```python
unreal.ImportSubsystem_OnAssetReimport_Dyn.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputDeviceSubsystem(EngineSubsystem)`

```python
unreal.InputDeviceSubsystem.activate_device_property_of_class(property_class: Class, params: ActivateDevicePropertyParams) -> InputDevicePropertyHandle
unreal.InputDeviceSubsystem.get_active_device_property(handle: InputDevicePropertyHandle) -> InputDeviceProperty
unreal.InputDeviceSubsystem.get_input_device_hardware_identifier(input_device: InputDeviceId) -> HardwareDeviceIdentifier
unreal.InputDeviceSubsystem.get_most_recently_used_hardware_device(user_id: PlatformUserId) -> HardwareDeviceIdentifier
unreal.InputDeviceSubsystem.get_most_recently_used_input_device_id(user_id: PlatformUserId) -> InputDeviceId
unreal.InputDeviceSubsystem.is_property_active(handle: InputDevicePropertyHandle) -> bool
unreal.InputDeviceSubsystem.on_input_hardware_device_changed(value: HardwareInputDeviceChanged) -> None
unreal.InputDeviceSubsystem.remove_all_device_properties() -> None
unreal.InputDeviceSubsystem.remove_device_property_by_handle(handle_to_remove: InputDevicePropertyHandle) -> None
unreal.InputDeviceSubsystem.remove_device_property_handles(handles_to_remove: Set[InputDevicePropertyHandle]) -> None
```

## `unreal.InstancedFoliageActor(ISMPartitionActor)`

```python
unreal.InstancedFoliageActor.add_instances(world_context_object: Object, foliage_type: FoliageType, transforms: Array[Transform]) -> None
unreal.InstancedFoliageActor.remove_all_instances(world_context_object: Object, foliage_type: FoliageType) -> None
```

## `unreal.InteractiveFoliageActor(StaticMeshActor)`

```python
unreal.InteractiveFoliageActor.foliage_damage_impulse_scale(value: float) -> None
unreal.InteractiveFoliageActor.foliage_damping(value: float) -> None
unreal.InteractiveFoliageActor.foliage_stiffness(value: float) -> None
unreal.InteractiveFoliageActor.foliage_stiffness_quadratic(value: float) -> None
unreal.InteractiveFoliageActor.foliage_touch_impulse_scale(value: float) -> None
unreal.InteractiveFoliageActor.max_damage_impulse(value: float) -> None
unreal.InteractiveFoliageActor.max_force(value: float) -> None
unreal.InteractiveFoliageActor.max_touch_impulse(value: float) -> None
```

## `unreal.InterchangeGenericLevelPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericLevelPipeline.delete_missing_actors(value: bool) -> None
unreal.InterchangeGenericLevelPipeline.delete_missing_assets(value: bool) -> None
unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_actors(value: bool) -> None
unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_assets(value: bool) -> None
unreal.InterchangeGenericLevelPipeline.pipeline_display_name(value: str) -> None
unreal.InterchangeGenericLevelPipeline.reimport_property_strategy(value: ReimportStrategyFlags) -> None
unreal.InterchangeGenericLevelPipeline.scene_hierarchy_type(value: InterchangeSceneHierarchyType) -> None
unreal.InterchangeGenericLevelPipeline.use_physical_instead_of_standard_perspective_camera(value: bool) -> None
```

## `unreal.InterchangeTransformAnimationTrackNode(InterchangeAnimationTrackNode)`

```python
unreal.InterchangeTransformAnimationTrackNode.get_custom_used_channels() -> Optional[int]
unreal.InterchangeTransformAnimationTrackNode.set_custom_used_channels(attribute_value: int) -> bool
```

## `unreal.JoinStaticMeshActorsOptions(StructBase)`

```python
unreal.JoinStaticMeshActorsOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False) -> None
unreal.JoinStaticMeshActorsOptions.destroy_source_actors(value: bool) -> None
unreal.JoinStaticMeshActorsOptions.new_actor_label(value: str) -> None
unreal.JoinStaticMeshActorsOptions.rename_components_from_source(value: bool) -> None
```

## `unreal.KLevelSetElem(KShapeElem)`

```python
unreal.KLevelSetElem.__init__() -> None
```

## `unreal.KSkinnedLevelSetElem(KShapeElem)`

```python
unreal.KSkinnedLevelSetElem.__init__() -> None
```

## `unreal.LandmassActor(Actor)`

```python
unreal.LandmassActor.actor_selection_changed(selected: bool) -> None
unreal.LandmassActor.affects_heightmap(value: bool) -> None
unreal.LandmassActor.affects_visibility(value: bool) -> None
unreal.LandmassActor.affects_weightmaps(value: bool) -> None
unreal.LandmassActor.brush_extents() -> Vector4
unreal.LandmassActor.brush_manager(value: LandmassManagerBase) -> None
unreal.LandmassActor.brush_render_parameters(value: LandscapeBrushParameters) -> None
unreal.LandmassActor.brush_size(value: float) -> None
unreal.LandmassActor.custom_tick(delta_seconds: float) -> None
unreal.LandmassActor.draw_brush_material(material: MaterialInterface) -> None
unreal.LandmassActor.draw_to_entire_landscape(value: bool) -> None
unreal.LandmassActor.extents_preview_mid(value: MaterialInstanceDynamic) -> None
unreal.LandmassActor.fast_preview_mode() -> None
unreal.LandmassActor.height_blend_mode(value: BrushBlendMode) -> None
unreal.LandmassActor.height_material(value: MaterialInterface) -> None
unreal.LandmassActor.heightmap_render_mid(value: MaterialInstanceDynamic) -> None
unreal.LandmassActor.move_brush_down() -> None
unreal.LandmassActor.move_brush_up() -> None
unreal.LandmassActor.move_to_bottom() -> None
unreal.LandmassActor.move_to_top() -> None
unreal.LandmassActor.on_brush_updated(value: OnBrushUpdatedDelegate) -> None
unreal.LandmassActor.render_layer(parameters: LandscapeBrushParameters) -> None
unreal.LandmassActor.render_layer_native(parameters: LandscapeBrushParameters) -> None
unreal.LandmassActor.restore_landscape_editing() -> None
unreal.LandmassActor.set_editor_tick_enabled(enabled: bool) -> None
unreal.LandmassActor.set_mesh_exents_material(material: MaterialInterface) -> None
unreal.LandmassActor.update_brush_extents() -> None
unreal.LandmassActor.weight_map_blend_mode(value: BrushBlendMode) -> None
unreal.LandmassActor.weightmap_layers(value: Array[Name]) -> None
unreal.LandmassActor.weightmap_material(value: MaterialInterface) -> None
unreal.LandmassActor.weightmap_render_mid(value: MaterialInstanceDynamic) -> None
```

## `unreal.LandscapeMeshProxyActor(Actor)`

```python
unreal.LandscapeMeshProxyActor.landscape_mesh_proxy_component() -> LandscapeMeshProxyComponent
```

## `unreal.LandscapeSplineMeshesActor(PartitionActor)`

```python
unreal.LandscapeSplineMeshesActor.static_mesh_components() -> Array[StaticMeshComponent]
```

## `unreal.LayersSubsystem(EditorSubsystem)`

```python
unreal.LayersSubsystem.add_actor_to_layer(actor: Actor, layer_name: Name) -> bool
unreal.LayersSubsystem.add_actor_to_layers(actor: Actor, layer_names: Array[Name]) -> bool
unreal.LayersSubsystem.add_actors_to_layer(actors: Array[Actor], layer_name: Name) -> bool
unreal.LayersSubsystem.add_actors_to_layers(actors: Array[Actor], layer_names: Array[Name]) -> bool
unreal.LayersSubsystem.add_all_layer_names_to() -> Array[Name]
unreal.LayersSubsystem.add_all_layers_to() -> Array[Layer]
unreal.LayersSubsystem.add_level_layer_information(level: Level) -> None
unreal.LayersSubsystem.add_selected_actors_to_layer(layer_name: Name) -> bool
unreal.LayersSubsystem.add_selected_actors_to_layers(layer_names: Array[Name]) -> bool
unreal.LayersSubsystem.append_actors_from_layer(layer_name: Name) -> Array[Actor]
unreal.LayersSubsystem.append_actors_from_layers(layer_names: Array[Name]) -> Array[Actor]
unreal.LayersSubsystem.create_layer(layer_name: Name) -> Layer
unreal.LayersSubsystem.delete_layer(layer_to_delete: Name) -> None
unreal.LayersSubsystem.delete_layers(layers_to_delete: Array[Name]) -> None
unreal.LayersSubsystem.disassociate_actor_from_layers(actor: Actor) -> bool
unreal.LayersSubsystem.disassociate_actors_from_layers(actors: Array[Actor]) -> bool
unreal.LayersSubsystem.editor_map_change() -> None
unreal.LayersSubsystem.editor_refresh_layer_browser() -> None
unreal.LayersSubsystem.get_actors_from_layer(layer_name: Name) -> Array[Actor]
unreal.LayersSubsystem.get_actors_from_layers(layer_names: Array[Name]) -> Array[Actor]
unreal.LayersSubsystem.get_layer(layer_name: Name) -> Layer
unreal.LayersSubsystem.get_selected_actors() -> Array[Actor]
unreal.LayersSubsystem.get_world() -> World
unreal.LayersSubsystem.initialize_new_actor_layers(actor: Actor) -> bool
unreal.LayersSubsystem.is_actor_valid_for_layer(actor: Actor) -> bool
unreal.LayersSubsystem.is_layer(layer_name: Name) -> bool
unreal.LayersSubsystem.make_all_layers_visible() -> None
unreal.LayersSubsystem.remove_actor_from_layer(actor: Actor, layer_to_remove: Name, update_stats: bool = True) -> bool
unreal.LayersSubsystem.remove_actor_from_layers(actor: Actor, layer_names: Array[Name], update_stats: bool = True) -> bool
unreal.LayersSubsystem.remove_actors_from_layer(actors: Array[Actor], layer_name: Name, update_stats: bool = True) -> bool
unreal.LayersSubsystem.remove_actors_from_layers(actors: Array[Actor], layer_names: Array[Name], update_stats: bool = True) -> bool
unreal.LayersSubsystem.remove_level_layer_information(level: Level) -> None
unreal.LayersSubsystem.remove_selected_actors_from_layer(layer_name: Name) -> bool
unreal.LayersSubsystem.remove_selected_actors_from_layers(layer_names: Array[Name]) -> bool
unreal.LayersSubsystem.rename_layer(original_layer_name: Name, new_layer_name: Name) -> bool
unreal.LayersSubsystem.select_actors_in_layer(layer_name: Name, select: bool, notify: bool, select_even_if_hidden: bool = False) -> bool
unreal.LayersSubsystem.select_actors_in_layers(layer_names: Array[Name], select: bool, notify: bool, select_even_if_hidden: bool = False) -> bool
unreal.LayersSubsystem.set_layer_visibility(layer_name: Name, is_visible: bool) -> None
unreal.LayersSubsystem.set_layers_visibility(layer_names: Array[Name], is_visible: bool) -> None
unreal.LayersSubsystem.toggle_layer_visibility(layer_name: Name) -> None
unreal.LayersSubsystem.toggle_layers_visibility(layer_names: Array[Name]) -> None
unreal.LayersSubsystem.try_get_layer(layer_name: Name) -> Optional[Layer]
unreal.LayersSubsystem.update_actor_all_views_visibility(actor: Actor) -> None
unreal.LayersSubsystem.update_actor_visibility(actor: Actor, notify_selection_change: bool, redraw_viewports: bool) -> Optional[Tuple[bool, bool]]
unreal.LayersSubsystem.update_all_actors_visibility(notify_selection_change: bool, redraw_viewports: bool) -> bool
unreal.LayersSubsystem.update_all_view_visibility(layer_that_changed: Name) -> None
```

## `unreal.Level(Object)`

```python
unreal.Level.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.Level.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.Level.has_asset_user_data_of_class(user_data_class: Class) -> bool
```

## `unreal.LevelEditorContextMenuContext(Object)`

```python
unreal.LevelEditorContextMenuContext.context_type() -> LevelEditorMenuContext
unreal.LevelEditorContextMenuContext.current_selection() -> TypedElementSelectionSet
unreal.LevelEditorContextMenuContext.cursor_world_location() -> Vector
unreal.LevelEditorContextMenuContext.get_hit_proxy_element() -> ScriptTypedElementHandle
unreal.LevelEditorContextMenuContext.hit_proxy_actor() -> Actor
unreal.LevelEditorContextMenuContext.selected_components() -> Array[ActorComponent]
```

## `unreal.LevelEditorSubsystem(EditorSubsystem)`

```python
unreal.LevelEditorSubsystem.build_light_maps(quality: LightingBuildQuality = LightingBuildQuality.QUALITY_PRODUCTION, with_reflection_captures: bool = False) -> bool
unreal.LevelEditorSubsystem.editor_get_game_view(viewport_config_key: Name = "None") -> bool
unreal.LevelEditorSubsystem.editor_invalidate_viewports() -> None
unreal.LevelEditorSubsystem.editor_play_simulate() -> None
unreal.LevelEditorSubsystem.editor_request_begin_play() -> None
unreal.LevelEditorSubsystem.editor_request_end_play() -> None
unreal.LevelEditorSubsystem.editor_set_game_view(game_view: bool, viewport_config_key: Name = "None") -> None
unreal.LevelEditorSubsystem.editor_set_viewport_realtime(realtime: bool, viewport_config_key: Name = "None") -> None
unreal.LevelEditorSubsystem.eject_pilot_level_actor(viewport_config_key: Name = "None") -> None
unreal.LevelEditorSubsystem.get_active_viewport_config_key() -> Name
unreal.LevelEditorSubsystem.get_allows_cinematic_control(viewport_config_key: Name = "None") -> bool
unreal.LevelEditorSubsystem.get_current_level() -> Level
unreal.LevelEditorSubsystem.get_pilot_level_actor(viewport_config_key: Name = "None") -> Actor
unreal.LevelEditorSubsystem.get_selection_set() -> TypedElementSelectionSet
unreal.LevelEditorSubsystem.get_viewport_config_keys() -> Array[Name]
unreal.LevelEditorSubsystem.is_in_play_in_editor() -> bool
unreal.LevelEditorSubsystem.load_level(asset_path: str) -> bool
unreal.LevelEditorSubsystem.new_level(asset_path: str, is_partitioned_world: bool = False) -> bool
unreal.LevelEditorSubsystem.new_level_from_template(asset_path: str, template_asset_path: str) -> bool
unreal.LevelEditorSubsystem.on_editor_camera_moved(value: OnLevelEditorEditorCameraMoved) -> None
unreal.LevelEditorSubsystem.on_map_changed(value: OnLevelEditorMapChanged) -> None
unreal.LevelEditorSubsystem.on_map_opened(value: OnLevelEditorMapOpened) -> None
unreal.LevelEditorSubsystem.on_post_save_world(value: OnLevelEditorPostSaveWorld) -> None
unreal.LevelEditorSubsystem.on_pre_save_world(value: OnLevelEditorPreSaveWorld) -> None
unreal.LevelEditorSubsystem.pilot_level_actor(actor_to_pilot: Actor, viewport_config_key: Name = "None") -> None
unreal.LevelEditorSubsystem.save_all_dirty_levels() -> bool
unreal.LevelEditorSubsystem.save_current_level() -> bool
unreal.LevelEditorSubsystem.set_allows_cinematic_control(allow: bool, viewport_config_key: Name = "None") -> None
unreal.LevelEditorSubsystem.set_current_level_by_name(level_name: Name) -> bool
```

## `unreal.LevelInstance(Actor)`

```python
unreal.LevelInstance.get_loaded_level() -> Level
unreal.LevelInstance.get_world_asset() -> World
unreal.LevelInstance.is_loaded() -> bool
unreal.LevelInstance.load_level_instance() -> None
unreal.LevelInstance.set_world_asset(world_asset: World) -> bool
unreal.LevelInstance.unload_level_instance() -> None
```

## `unreal.LevelInstanceInterface(Interface)`

```python
unreal.LevelInstanceInterface.get_loaded_level() -> Level
unreal.LevelInstanceInterface.get_world_asset() -> World
unreal.LevelInstanceInterface.is_loaded() -> bool
unreal.LevelInstanceInterface.load_level_instance() -> None
unreal.LevelInstanceInterface.set_world_asset(world_asset: World) -> bool
unreal.LevelInstanceInterface.unload_level_instance() -> None
```

## `unreal.LevelScriptActor(Actor)`

```python
unreal.LevelScriptActor.level_reset() -> None
unreal.LevelScriptActor.remote_event(event_name: Name) -> bool
unreal.LevelScriptActor.set_cinematic_mode(cinematic_mode: bool, hide_player: bool = True, affects_hud: bool = True, affects_movement: bool = False, affects_turning: bool = False) -> None
unreal.LevelScriptActor.world_origin_location_changed(old_origin_location: IntVector, new_origin_location: IntVector) -> None
```

## `unreal.LevelSequence(MovieSceneSequence)`

```python
unreal.LevelSequence.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.LevelSequence.copy_meta_data(meta_data: Object) -> Object
unreal.LevelSequence.find_meta_data_by_class(class_: Class) -> Object
unreal.LevelSequence.find_or_add_meta_data_by_class(class_: Class) -> Object
unreal.LevelSequence.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.LevelSequence.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.LevelSequence.remove_meta_data_by_class(class_: Class) -> None
```

## `unreal.LevelSequenceActor(Actor)`

```python
unreal.LevelSequenceActor.add_binding(binding: MovieSceneObjectBindingID, actor: Actor, allow_bindings_from_asset: bool = False) -> None
unreal.LevelSequenceActor.add_binding_by_tag(binding_tag: Name, actor: Actor, allow_bindings_from_asset: bool = False) -> None
unreal.LevelSequenceActor.binding_overrides() -> MovieSceneBindingOverrides
unreal.LevelSequenceActor.burn_in_options() -> LevelSequenceBurnInOptions
unreal.LevelSequenceActor.camera_settings(value: LevelSequenceCameraSettings) -> None
unreal.LevelSequenceActor.default_instance_data(value: Object) -> None
unreal.LevelSequenceActor.find_named_binding(tag: Name) -> MovieSceneObjectBindingID
unreal.LevelSequenceActor.find_named_bindings(tag: Name) -> Array[MovieSceneObjectBindingID]
unreal.LevelSequenceActor.get_sequence() -> LevelSequence
unreal.LevelSequenceActor.hide_burnin() -> None
unreal.LevelSequenceActor.level_sequence_asset() -> LevelSequence
unreal.LevelSequenceActor.override_instance_data(value: bool) -> None
unreal.LevelSequenceActor.playback_settings() -> MovieSceneSequencePlaybackSettings
unreal.LevelSequenceActor.remove_binding(binding: MovieSceneObjectBindingID, actor: Actor) -> None
unreal.LevelSequenceActor.remove_binding_by_tag(tag: Name, actor: Actor) -> None
unreal.LevelSequenceActor.replicate_playback(value: bool) -> None
unreal.LevelSequenceActor.reset_binding(binding: MovieSceneObjectBindingID) -> None
unreal.LevelSequenceActor.reset_bindings() -> None
unreal.LevelSequenceActor.sequence_player() -> LevelSequencePlayer
unreal.LevelSequenceActor.set_binding(binding: MovieSceneObjectBindingID, actors: Array[Actor], allow_bindings_from_asset: bool = False) -> None
unreal.LevelSequenceActor.set_binding_by_tag(binding_tag: Name, actors: Array[Actor], allow_bindings_from_asset: bool = False) -> None
unreal.LevelSequenceActor.set_sequence(sequence: LevelSequence) -> None
unreal.LevelSequenceActor.show_burnin() -> None
```

## `unreal.LevelSequenceActor_OnLevelSequenceLoaded(DelegateBase)`

```python
unreal.LevelSequenceActor_OnLevelSequenceLoaded.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.LevelSequenceAnimSequenceLink(AssetUserData)`

```python
unreal.LevelSequenceAnimSequenceLink.anim_sequence_links(value: Array[LevelSequenceAnimSequenceLinkItem]) -> None
```

## `unreal.LevelSequenceAnimSequenceLinkItem(StructBase)`

```python
unreal.LevelSequenceAnimSequenceLinkItem.__init__(skel_track_guid: Guid = [], path_to_anim_sequence: SoftObjectPath = [""], export_transforms: bool = False, export_morph_targets: bool = False, export_attribute_curves: bool = False, export_material_curves: bool = False, interpolation: AnimInterpolationType = AnimInterpolationType.LINEAR, curve_interpolation: RichCurveInterpMode = RichCurveInterpMode.RCIM_LINEAR, record_in_world_space: bool = False, evaluate_all_skeletal_mesh_components: bool = False, include_animation_names: Array[str] = [], exclude_animation_names: Array[str] = [], warm_up_frames: FrameNumber = [0], delay_before_start: FrameNumber = [0], use_custom_time_range: bool = False, custom_start_frame: FrameNumber = [0], custom_end_frame: FrameNumber = [0], custom_display_rate: FrameRate = [60000, 1]) -> None
unreal.LevelSequenceAnimSequenceLinkItem.curve_interpolation(value: RichCurveInterpMode) -> None
unreal.LevelSequenceAnimSequenceLinkItem.custom_display_rate(value: FrameRate) -> None
unreal.LevelSequenceAnimSequenceLinkItem.custom_end_frame(value: FrameNumber) -> None
unreal.LevelSequenceAnimSequenceLinkItem.custom_start_frame(value: FrameNumber) -> None
unreal.LevelSequenceAnimSequenceLinkItem.delay_before_start(value: FrameNumber) -> None
unreal.LevelSequenceAnimSequenceLinkItem.evaluate_all_skeletal_mesh_components(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.exclude_animation_names(value: Array[str]) -> None
unreal.LevelSequenceAnimSequenceLinkItem.export_attribute_curves(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.export_material_curves(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.export_morph_targets(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.export_transforms(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.include_animation_names(value: Array[str]) -> None
unreal.LevelSequenceAnimSequenceLinkItem.interpolation(value: AnimInterpolationType) -> None
unreal.LevelSequenceAnimSequenceLinkItem.path_to_anim_sequence(value: SoftObjectPath) -> None
unreal.LevelSequenceAnimSequenceLinkItem.record_in_world_space(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.skel_track_guid(value: Guid) -> None
unreal.LevelSequenceAnimSequenceLinkItem.use_custom_time_range(value: bool) -> None
unreal.LevelSequenceAnimSequenceLinkItem.warm_up_frames(value: FrameNumber) -> None
```

## `unreal.LevelSequenceBurnIn(UserWidget)`

```python
unreal.LevelSequenceBurnIn.frame_information() -> LevelSequencePlayerSnapshot
unreal.LevelSequenceBurnIn.get_settings_class() -> Class
unreal.LevelSequenceBurnIn.level_sequence_actor() -> LevelSequenceActor
unreal.LevelSequenceBurnIn.set_settings(settings: Object) -> None
```

## `unreal.LevelSequenceBurnInOptions(Object)`

```python
unreal.LevelSequenceBurnInOptions.burn_in_class(value: SoftClassPath) -> None
unreal.LevelSequenceBurnInOptions.set_burn_in(burn_in_class: SoftClassPath) -> None
unreal.LevelSequenceBurnInOptions.settings(value: LevelSequenceBurnInInitSettings) -> None
unreal.LevelSequenceBurnInOptions.use_burn_in(value: bool) -> None
```

## `unreal.LevelSequenceCameraSettings(StructBase)`

```python
unreal.LevelSequenceCameraSettings.__init__(override_aspect_ratio_axis_constraint: bool = False, aspect_ratio_axis_constraint: AspectRatioAxisConstraint = AspectRatioAxisConstraint.ASPECT_RATIO_MAINTAIN_YFOV) -> None
unreal.LevelSequenceCameraSettings.aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
unreal.LevelSequenceCameraSettings.override_aspect_ratio_axis_constraint(value: bool) -> None
```

## `unreal.LevelSequenceDirector(Object)`

```python
unreal.LevelSequenceDirector.get_bound_actor(object_binding: MovieSceneObjectBindingID) -> Actor
unreal.LevelSequenceDirector.get_bound_actors(object_binding: MovieSceneObjectBindingID) -> Array[Actor]
unreal.LevelSequenceDirector.get_bound_object(object_binding: MovieSceneObjectBindingID) -> Object
unreal.LevelSequenceDirector.get_bound_objects(object_binding: MovieSceneObjectBindingID) -> Array[Object]
unreal.LevelSequenceDirector.get_current_time() -> QualifiedTime
unreal.LevelSequenceDirector.get_root_sequence_time() -> QualifiedTime
unreal.LevelSequenceDirector.get_sequence() -> MovieSceneSequence
unreal.LevelSequenceDirector.on_created() -> None
unreal.LevelSequenceDirector.player() -> LevelSequencePlayer
```

## `unreal.LevelSequenceEditorBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.LevelSequenceEditorBlueprintLibrary.close_level_sequence() -> None
unreal.LevelSequenceEditorBlueprintLibrary.delete_color_for_channels(class_: Class) -> str
unreal.LevelSequenceEditorBlueprintLibrary.empty_selection() -> None
unreal.LevelSequenceEditorBlueprintLibrary.focus_level_sequence(sub_section: MovieSceneSubSection) -> None
unreal.LevelSequenceEditorBlueprintLibrary.focus_parent_sequence() -> None
unreal.LevelSequenceEditorBlueprintLibrary.force_update() -> None
unreal.LevelSequenceEditorBlueprintLibrary.get_bound_objects(object_binding: MovieSceneObjectBindingID) -> Array[Object]
unreal.LevelSequenceEditorBlueprintLibrary.get_channels_with_selected_keys() -> Array[SequencerChannelProxy]
unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence() -> LevelSequence
unreal.LevelSequenceEditorBlueprintLibrary.get_current_local_time() -> int
unreal.LevelSequenceEditorBlueprintLibrary.get_current_time() -> int
unreal.LevelSequenceEditorBlueprintLibrary.get_custom_color_for_channel(class_: Class, identifier: str) -> LinearColor
unreal.LevelSequenceEditorBlueprintLibrary.get_focused_level_sequence() -> LevelSequence
unreal.LevelSequenceEditorBlueprintLibrary.get_global_position(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneSequencePlaybackParams
unreal.LevelSequenceEditorBlueprintLibrary.get_local_position(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneSequencePlaybackParams
unreal.LevelSequenceEditorBlueprintLibrary.get_loop_mode() -> SequencerLoopMode
unreal.LevelSequenceEditorBlueprintLibrary.get_playback_speed() -> float
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_bindings() -> Array[MovieSceneBindingProxy]
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_channels() -> Array[SequencerChannelProxy]
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_folders() -> Array[MovieSceneFolder]
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_keys(channel_proxy: SequencerChannelProxy) -> Array[int]
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_sections() -> Array[MovieSceneSection]
unreal.LevelSequenceEditorBlueprintLibrary.get_selected_tracks() -> Array[MovieSceneTrack]
unreal.LevelSequenceEditorBlueprintLibrary.get_selection_range_end() -> int
unreal.LevelSequenceEditorBlueprintLibrary.get_selection_range_start() -> int
unreal.LevelSequenceEditorBlueprintLibrary.get_sub_sequence_hierarchy() -> Array[MovieSceneSubSection]
unreal.LevelSequenceEditorBlueprintLibrary.get_track_filter_names() -> Array[Text]
unreal.LevelSequenceEditorBlueprintLibrary.has_custom_color_for_channel(class_: Class, identifier: str) -> bool
unreal.LevelSequenceEditorBlueprintLibrary.is_camera_cut_locked_to_viewport() -> bool
unreal.LevelSequenceEditorBlueprintLibrary.is_level_sequence_locked() -> bool
unreal.LevelSequenceEditorBlueprintLibrary.is_playing() -> bool
unreal.LevelSequenceEditorBlueprintLibrary.is_track_filter_active(track_filter_name: Text) -> bool
unreal.LevelSequenceEditorBlueprintLibrary.is_track_filter_enabled(track_filter_name: Text) -> bool
unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(level_sequence: LevelSequence) -> bool
unreal.LevelSequenceEditorBlueprintLibrary.pause() -> None
unreal.LevelSequenceEditorBlueprintLibrary.play() -> None
unreal.LevelSequenceEditorBlueprintLibrary.play_to(playback_params: MovieSceneSequencePlaybackParams, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence() -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_bindings(object_bindings: Array[MovieSceneBindingProxy]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_channels(channels: Array[SequencerChannelProxy]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_folders(folders: Array[MovieSceneFolder]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_keys(channel: SequencerChannelProxy, indices: Array[int]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_sections(sections: Array[MovieSceneSection]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.select_tracks(tracks: Array[MovieSceneTrack]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_current_local_time(new_frame: int) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_current_time(new_frame: int) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_custom_color_for_channel(class_: Class, identifier: str, new_color: LinearColor) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_custom_color_for_channels(class_: Class, identifiers: Array[str], new_colors: Array[LinearColor]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_global_position(playback_params: MovieSceneSequencePlaybackParams, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_local_position(playback_params: MovieSceneSequencePlaybackParams, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_lock_camera_cut_to_viewport(lock: bool) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_lock_level_sequence(lock: bool) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_loop_mode(new_loop_mode: SequencerLoopMode) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_playback_speed(new_playback_speed: float) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_random_color_for_channels(class_: Class, identifiers: Array[str]) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_selection_range_end(new_frame: int) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_selection_range_start(new_frame: int) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_track_filter_active(track_filter_name: Text, active: bool) -> None
unreal.LevelSequenceEditorBlueprintLibrary.set_track_filter_enabled(track_filter_name: Text, enabled: bool) -> None
```

## `unreal.LevelSequenceEditorSubsystem(EditorSubsystem)`

```python
unreal.LevelSequenceEditorSubsystem.add_actors(actors: Array[Actor]) -> Array[MovieSceneBindingProxy]
unreal.LevelSequenceEditorSubsystem.add_actors_to_binding(actors: Array[Actor], object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.bake_transform(object_bindings: Array[MovieSceneBindingProxy], bake_in_time: FrameTime, bake_out_time: FrameTime, bake_interval: FrameTime, params: MovieSceneScriptingParams = [MovieSceneTimeUnit.DISPLAY_RATE]) -> None
unreal.LevelSequenceEditorSubsystem.bake_transform_with_settings(object_bindings: Array[MovieSceneBindingProxy], settings: BakingAnimationKeySettings, params: MovieSceneScriptingParams = [MovieSceneTimeUnit.DISPLAY_RATE]) -> bool
unreal.LevelSequenceEditorSubsystem.change_actor_template_class(object_binding: MovieSceneBindingProxy, actor_class: Class) -> bool
unreal.LevelSequenceEditorSubsystem.convert_to_custom_binding(object_binding: MovieSceneBindingProxy, binding_type: Class) -> MovieSceneBindingProxy
unreal.LevelSequenceEditorSubsystem.convert_to_possessable(object_binding: MovieSceneBindingProxy) -> MovieSceneBindingProxy
unreal.LevelSequenceEditorSubsystem.convert_to_spawnable(object_binding: MovieSceneBindingProxy) -> Array[MovieSceneBindingProxy]
unreal.LevelSequenceEditorSubsystem.copy_bindings(bindings: Array[MovieSceneBindingProxy]) -> str
unreal.LevelSequenceEditorSubsystem.copy_folders(folders: Array[MovieSceneFolder]) -> str
unreal.LevelSequenceEditorSubsystem.copy_sections(sections: Array[MovieSceneSection]) -> str
unreal.LevelSequenceEditorSubsystem.copy_tracks(tracks: Array[MovieSceneTrack]) -> str
unreal.LevelSequenceEditorSubsystem.create_camera(spawnable: bool) -> Tuple[MovieSceneBindingProxy, CineCameraActor]
unreal.LevelSequenceEditorSubsystem.fix_actor_references() -> None
unreal.LevelSequenceEditorSubsystem.get_curve_editor() -> SequencerCurveEditorObject
unreal.LevelSequenceEditorSubsystem.get_custom_binding_objects(object_binding: MovieSceneBindingProxy) -> Array[MovieSceneCustomBinding]
unreal.LevelSequenceEditorSubsystem.get_custom_binding_type(object_binding: MovieSceneBindingProxy) -> Class
unreal.LevelSequenceEditorSubsystem.get_custom_bindings_of_type(custom_binding_type: Class) -> Array[MovieSceneBindingProxy]
unreal.LevelSequenceEditorSubsystem.get_scripting_layer() -> SequencerModuleScriptingLayer
unreal.LevelSequenceEditorSubsystem.paste_bindings(text_to_import: str, paste_bindings_params: MovieScenePasteBindingsParams) -> Optional[Array[MovieSceneBindingProxy]]
unreal.LevelSequenceEditorSubsystem.paste_folders(text_to_import: str, paste_folders_params: MovieScenePasteFoldersParams) -> Optional[Array[MovieSceneFolder]]
unreal.LevelSequenceEditorSubsystem.paste_sections(text_to_import: str, paste_sections_params: MovieScenePasteSectionsParams) -> Optional[Array[MovieSceneSection]]
unreal.LevelSequenceEditorSubsystem.paste_tracks(text_to_import: str, paste_tracks_params: MovieScenePasteTracksParams) -> Optional[Array[MovieSceneTrack]]
unreal.LevelSequenceEditorSubsystem.rebind_component(component_bindings: Array[MovieSceneBindingProxy], component_name: Name) -> None
unreal.LevelSequenceEditorSubsystem.remove_actors_from_binding(actors: Array[Actor], object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.remove_all_bindings(object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.remove_invalid_bindings(object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.replace_binding_with_actors(actors: Array[Actor], object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.save_default_spawnable_state(object_binding: MovieSceneBindingProxy) -> None
unreal.LevelSequenceEditorSubsystem.snap_sections_to_timeline_using_source_timecode(sections: Array[MovieSceneSection]) -> None
unreal.LevelSequenceEditorSubsystem.sync_sections_using_source_timecode(sections: Array[MovieSceneSection]) -> None
```

## `unreal.LevelSequenceMediaController(Actor)`

```python
unreal.LevelSequenceMediaController.get_media_component() -> MediaComponent
unreal.LevelSequenceMediaController.get_sequence() -> LevelSequenceActor
unreal.LevelSequenceMediaController.media_component() -> MediaComponent
unreal.LevelSequenceMediaController.play() -> None
unreal.LevelSequenceMediaController.sequence() -> LevelSequenceActor
unreal.LevelSequenceMediaController.server_start_time_seconds() -> float
unreal.LevelSequenceMediaController.synchronize_to_server(desync_threshold_seconds: float = 2.000000) -> None
```

## `unreal.LevelSequencePlaybackSettings(MovieSceneSequencePlaybackSettings)`

```python
unreal.LevelSequencePlaybackSettings.__init__(auto_play: bool = False, loop_count: MovieSceneSequenceLoopCount = [0], tick_interval: MovieSceneSequenceTickInterval = [0.000000, 0.000000, False, True], play_rate: float = 0.000000, start_time: float = 0.000000, random_start_time: bool = False, disable_movement_input: bool = False, disable_look_at_input: bool = False, hide_player: bool = False, hide_hud: bool = False, disable_camera_cuts: bool = False, finish_completion_state_override: MovieSceneCompletionModeOverride = MovieSceneCompletionModeOverride.NONE, pause_at_end: bool = False) -> None
```

## `unreal.LevelSequencePlayer(MovieSceneSequencePlayer)`

```python
unreal.LevelSequencePlayer.create_level_sequence_player(world_context_object: Object, level_sequence: LevelSequence, settings: MovieSceneSequencePlaybackSettings) -> Tuple[LevelSequencePlayer, LevelSequenceActor]
unreal.LevelSequencePlayer.get_active_camera_component() -> CameraComponent
unreal.LevelSequencePlayer.on_camera_cut(value: OnLevelSequencePlayerCameraCutEvent) -> None
```

## `unreal.LevelSequencePlayerSnapshot(StructBase)`

```python
unreal.LevelSequencePlayerSnapshot.__init__(root_name: str = "", root_time: QualifiedTime = [[0], [24, 1], 0.000000], source_time: QualifiedTime = [[0], [24, 1], 0.000000], current_shot_name: str = "", current_shot_local_time: QualifiedTime = [[0], [24, 1], 0.000000], current_shot_source_time: QualifiedTime = [[0], [24, 1], 0.000000], source_timecode: str = "", camera_component: CameraComponent = None, active_shot: LevelSequence = None) -> None
unreal.LevelSequencePlayerSnapshot.active_shot() -> LevelSequence
unreal.LevelSequencePlayerSnapshot.camera_component() -> CameraComponent
unreal.LevelSequencePlayerSnapshot.current_shot_local_time() -> QualifiedTime
unreal.LevelSequencePlayerSnapshot.current_shot_name() -> str
unreal.LevelSequencePlayerSnapshot.current_shot_source_time() -> QualifiedTime
unreal.LevelSequencePlayerSnapshot.root_name() -> str
unreal.LevelSequencePlayerSnapshot.root_time() -> QualifiedTime
unreal.LevelSequencePlayerSnapshot.source_time() -> QualifiedTime
unreal.LevelSequencePlayerSnapshot.source_timecode() -> str
```

## `unreal.LevelSequenceWithShotsSettings(Object)`

```python
unreal.LevelSequenceWithShotsSettings.sub_sequence_names(value: Array[Name]) -> None
```

## `unreal.LevelStreaming(Object)`

```python
unreal.LevelStreaming.create_instance(unique_instance_name: str) -> LevelStreaming
unreal.LevelStreaming.disable_distance_streaming(value: bool) -> None
unreal.LevelStreaming.get_is_requesting_unload_and_removal() -> bool
unreal.LevelStreaming.get_loaded_level() -> Level
unreal.LevelStreaming.get_world_asset_package_f_name() -> Name
unreal.LevelStreaming.is_level_loaded() -> bool
unreal.LevelStreaming.is_level_visible() -> bool
unreal.LevelStreaming.is_streaming_state_pending() -> bool
unreal.LevelStreaming.level_lod_index(value: int) -> None
unreal.LevelStreaming.level_transform(value: Transform) -> None
unreal.LevelStreaming.on_level_hidden(value: LevelStreamingVisibilityStatus) -> None
unreal.LevelStreaming.on_level_loaded(value: LevelStreamingLoadedStatus) -> None
unreal.LevelStreaming.on_level_shown(value: LevelStreamingVisibilityStatus) -> None
unreal.LevelStreaming.on_level_unloaded(value: LevelStreamingLoadedStatus) -> None
unreal.LevelStreaming.set_is_requesting_unload_and_removal(is_requesting_unload_and_removal: bool) -> None
unreal.LevelStreaming.should_be_loaded(value: bool) -> None
unreal.LevelStreaming.should_be_visible(value: bool) -> None
unreal.LevelStreaming.should_block_on_load(value: bool) -> None
unreal.LevelStreaming.should_block_on_unload(value: bool) -> None
unreal.LevelStreaming.streaming_priority(value: int) -> None
unreal.LevelStreaming.world_asset() -> World
```

## `unreal.LevelStreamingDynamic(LevelStreaming)`

```python
unreal.LevelStreamingDynamic.load_level_instance(world_context_object: Object, level_name: str, location: Vector, rotation: Rotator, optional_level_name_override: str = "", optional_level_streaming_class: Class = None, load_as_temp_package: bool = False) -> Tuple[LevelStreamingDynamic, bool]
unreal.LevelStreamingDynamic.load_level_instance_by_soft_object_ptr(world_context_object: Object, level: World, location: Vector, rotation: Rotator, optional_level_name_override: str = "", optional_level_streaming_class: Class = None, load_as_temp_package: bool = False) -> Tuple[LevelStreamingDynamic, bool]
```

## `unreal.LevelStreamingLoadedStatus(MulticastDelegateBase)`

```python
unreal.LevelStreamingLoadedStatus.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.LevelStreamingVisibilityStatus(MulticastDelegateBase)`

```python
unreal.LevelStreamingVisibilityStatus.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.LevelStreamingVolume(Volume)`

```python
unreal.LevelStreamingVolume.disabled(value: bool) -> None
unreal.LevelStreamingVolume.editor_pre_vis_only(value: bool) -> None
unreal.LevelStreamingVolume.streaming_level_names() -> Array[Name]
unreal.LevelStreamingVolume.streaming_usage(value: StreamingVolumeUsage) -> None
```

## `unreal.LevelVariantSets(Object)`

```python
unreal.LevelVariantSets.add_variant_set(variant_set: VariantSet) -> None
unreal.LevelVariantSets.get_num_variant_sets() -> int
unreal.LevelVariantSets.get_variant_set(variant_set_index: int) -> VariantSet
unreal.LevelVariantSets.get_variant_set_by_name(variant_set_name: str) -> VariantSet
unreal.LevelVariantSets.remove_variant_set(variant_set: VariantSet) -> None
unreal.LevelVariantSets.remove_variant_set_by_name(variant_set_name: str) -> None
```

## `unreal.LevelVariantSetsActor(Actor)`

```python
unreal.LevelVariantSetsActor.get_level_variant_sets(load: bool = False) -> LevelVariantSets
unreal.LevelVariantSetsActor.level_variant_sets() -> SoftObjectPath
unreal.LevelVariantSetsActor.set_level_variant_sets(variant_sets: LevelVariantSets) -> None
unreal.LevelVariantSetsActor.switch_on_variant_by_index(variant_set_index: int, variant_index: int) -> bool
unreal.LevelVariantSetsActor.switch_on_variant_by_name(variant_set_name: str, variant_name: str) -> bool
```

## `unreal.LidarPointCloudActor(Actor)`

```python
unreal.LidarPointCloudActor.get_point_cloud() -> LidarPointCloud
unreal.LidarPointCloudActor.point_cloud_component() -> LidarPointCloudComponent
unreal.LidarPointCloudActor.set_point_cloud(point_cloud: LidarPointCloud) -> None
```

## `unreal.LightmassWorldInfoSettings(StructBase)`

```python
unreal.LightmassWorldInfoSettings.__init__(static_lighting_level_scale: float = 0.000000, num_indirect_lighting_bounces: int = 0, num_sky_lighting_bounces: int = 0, indirect_lighting_quality: float = 0.000000, indirect_lighting_smoothness: float = 0.000000, environment_color: Color = [0, 0, 0, 0], environment_intensity: float = 0.000000, diffuse_boost: float = 0.000000, volume_lighting_method: VolumeLightingMethod = VolumeLightingMethod.VLM_VOLUMETRIC_LIGHTMAP, use_ambient_occlusion: bool = False, generate_ambient_occlusion_material_mask: bool = False, visualize_material_diffuse: bool = False, visualize_ambient_occlusion: bool = False, compress_lightmaps: bool = False, volumetric_lightmap_detail_cell_size: float = 0.000000, volumetric_lightmap_maximum_brick_memory_mb: float = 0.000000, volumetric_lightmap_loading_cell_size: float = 0.000000, volumetric_lightmap_spherical_harmonic_smoothing: float = 0.000000, volume_light_sample_placement_scale: float = 0.000000, direct_illumination_occlusion_fraction: float = 0.000000, indirect_illumination_occlusion_fraction: float = 0.000000, occlusion_exponent: float = 0.000000, fully_occluded_samples_fraction: float = 0.000000, max_occlusion_distance: float = 0.000000) -> None
unreal.LightmassWorldInfoSettings.compress_lightmaps(value: bool) -> None
unreal.LightmassWorldInfoSettings.diffuse_boost(value: float) -> None
unreal.LightmassWorldInfoSettings.direct_illumination_occlusion_fraction(value: float) -> None
unreal.LightmassWorldInfoSettings.environment_color(value: Color) -> None
unreal.LightmassWorldInfoSettings.environment_intensity(value: float) -> None
unreal.LightmassWorldInfoSettings.fully_occluded_samples_fraction(value: float) -> None
unreal.LightmassWorldInfoSettings.generate_ambient_occlusion_material_mask(value: bool) -> None
unreal.LightmassWorldInfoSettings.indirect_illumination_occlusion_fraction(value: float) -> None
unreal.LightmassWorldInfoSettings.indirect_lighting_quality(value: float) -> None
unreal.LightmassWorldInfoSettings.indirect_lighting_smoothness(value: float) -> None
unreal.LightmassWorldInfoSettings.max_occlusion_distance(value: float) -> None
unreal.LightmassWorldInfoSettings.num_indirect_lighting_bounces(value: int) -> None
unreal.LightmassWorldInfoSettings.num_sky_lighting_bounces(value: int) -> None
unreal.LightmassWorldInfoSettings.occlusion_exponent(value: float) -> None
unreal.LightmassWorldInfoSettings.static_lighting_level_scale(value: float) -> None
unreal.LightmassWorldInfoSettings.use_ambient_occlusion(value: bool) -> None
unreal.LightmassWorldInfoSettings.visualize_ambient_occlusion(value: bool) -> None
unreal.LightmassWorldInfoSettings.visualize_material_diffuse(value: bool) -> None
unreal.LightmassWorldInfoSettings.volume_light_sample_placement_scale(value: float) -> None
unreal.LightmassWorldInfoSettings.volume_lighting_method(value: VolumeLightingMethod) -> None
unreal.LightmassWorldInfoSettings.volumetric_lightmap_detail_cell_size(value: float) -> None
unreal.LightmassWorldInfoSettings.volumetric_lightmap_loading_cell_size(value: float) -> None
unreal.LightmassWorldInfoSettings.volumetric_lightmap_maximum_brick_memory_mb(value: float) -> None
unreal.LightmassWorldInfoSettings.volumetric_lightmap_spherical_harmonic_smoothing(value: float) -> None
```

## `unreal.LiveLinkTransform(StructBase)`

```python
unreal.LiveLinkTransform.__init__() -> None
```

## `unreal.LiveLinkTransformAxisSwitchPreProcessor(LiveLinkFramePreProcessor)`

```python
unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_x(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_y(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_z(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_x(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_y(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_z(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_x(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_y(value: LiveLinkAxis) -> None
unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_z(value: LiveLinkAxis) -> None
```

## `unreal.LiveLinkTransformBlueprintData(LiveLinkBaseBlueprintData)`

```python
unreal.LiveLinkTransformBlueprintData.__init__(static_data: LiveLinkTransformStaticData = [True, True, False, []], frame_data: LiveLinkTransformFrameData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [{}, [[0], [24, 1], 0.000000]], []]) -> None
unreal.LiveLinkTransformBlueprintData.frame_data(value: LiveLinkTransformFrameData) -> None
unreal.LiveLinkTransformBlueprintData.static_data(value: LiveLinkTransformStaticData) -> None
```

## `unreal.LiveLinkTransformController(LiveLinkControllerBase)`

```python
unreal.LiveLinkTransformController.offset_transform(value: Transform) -> None
unreal.LiveLinkTransformController.transform_data(value: LiveLinkTransformControllerData) -> None
```

## `unreal.LiveLinkTransformControllerData(StructBase)`

```python
unreal.LiveLinkTransformControllerData.__init__(world_transform: bool = False, use_location: bool = False, use_rotation: bool = False, use_scale: bool = False, sweep: bool = False, teleport: bool = False) -> None
unreal.LiveLinkTransformControllerData.sweep(value: bool) -> None
unreal.LiveLinkTransformControllerData.teleport(value: bool) -> None
unreal.LiveLinkTransformControllerData.use_location(value: bool) -> None
unreal.LiveLinkTransformControllerData.use_rotation(value: bool) -> None
unreal.LiveLinkTransformControllerData.use_scale(value: bool) -> None
unreal.LiveLinkTransformControllerData.world_transform(value: bool) -> None
```

## `unreal.LiveLinkTransformFrameData(LiveLinkBaseFrameData)`

```python
unreal.LiveLinkTransformFrameData.__init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]], property_values: Array[float] = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.LiveLinkTransformFrameData.transform(value: Transform) -> None
```

## `unreal.LiveLinkTransformStaticData(LiveLinkBaseStaticData)`

```python
unreal.LiveLinkTransformStaticData.__init__(property_names: Array[Name] = [], is_location_supported: bool = False, is_rotation_supported: bool = False, is_scale_supported: bool = False) -> None
unreal.LiveLinkTransformStaticData.is_location_supported(value: bool) -> None
unreal.LiveLinkTransformStaticData.is_rotation_supported(value: bool) -> None
unreal.LiveLinkTransformStaticData.is_scale_supported(value: bool) -> None
```

## `unreal.LiveLinkWorldTime(StructBase)`

```python
unreal.LiveLinkWorldTime.__init__() -> None
```

## `unreal.MagicGISAppSubsystem(WorldSubsystem)`

```python
unreal.MagicGISAppSubsystem.geo_feature_clicked_notify_event(value: GeoFeatureClickedEvent) -> None
unreal.MagicGISAppSubsystem.get_gis_reference_lon_lat() -> Vector2D
unreal.MagicGISAppSubsystem.set_local_lon_lat(lon_lat: Vector2D) -> None
```

## `unreal.MagicGISLayerViewActor(MagicGISViewActor)`

```python
unreal.MagicGISLayerViewActor.update_gis_layer_view_params(json_string: str) -> None
```

## `unreal.MagicGISLayerViewActorFinishedEvent(DelegateBase)`

```python
unreal.MagicGISLayerViewActorFinishedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MassActorPoolableInterface(Interface)`

```python
unreal.MassActorPoolableInterface.can_be_pooled() -> bool
unreal.MassActorPoolableInterface.prepare_for_game() -> None
unreal.MassActorPoolableInterface.prepare_for_pooling() -> None
```

## `unreal.MaterialInstanceActor(Actor)`

```python
unreal.MaterialInstanceActor.target_actors(value: Array[Actor]) -> None
```

## `unreal.MergeStaticMeshActorsOptions(JoinStaticMeshActorsOptions)`

```python
unreal.MergeStaticMeshActorsOptions.__init__(destroy_source_actors: bool = False, new_actor_label: str = "", rename_components_from_source: bool = False, spawn_merged_actor: bool = False, base_package_name: str = "", mesh_merging_settings: MeshMergingSettings = [256, [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], MeshLODSelectionType.CALCULATE_LOD, 0, True, False, False, False, False, False, False, True, False, False, True, True, [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]]) -> None
unreal.MergeStaticMeshActorsOptions.base_package_name(value: str) -> None
unreal.MergeStaticMeshActorsOptions.mesh_merging_settings(value: MeshMergingSettings) -> None
unreal.MergeStaticMeshActorsOptions.spawn_merged_actor(value: bool) -> None
```

## `unreal.MetaSoundAssetSubsystem(EngineSubsystem)`

```python
unreal.MetaSoundAssetSubsystem.reassign_class_name(doc_interface: MetaSoundDocumentInterface) -> bool
unreal.MetaSoundAssetSubsystem.register_asset_classes_in_directories(directories: Array[MetaSoundAssetDirectory]) -> None
unreal.MetaSoundAssetSubsystem.replace_references_in_directory(directories: Array[MetaSoundAssetDirectory], old_class_name: MetasoundFrontendClassName, new_class_name: MetasoundFrontendClassName, old_version: MetasoundFrontendVersionNumber = [1, 0], new_version: MetasoundFrontendVersionNumber = [1, 0]) -> bool
unreal.MetaSoundAssetSubsystem.unregister_asset_classes_in_directories(directories: Array[MetaSoundAssetDirectory]) -> None
```

## `unreal.MetaSoundBuilderSubsystem(EngineSubsystem)`

```python
unreal.MetaSoundBuilderSubsystem.create_bool_array_meta_sound_literal(value: Array[bool]) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_bool_meta_sound_literal(value: bool) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_float_array_meta_sound_literal(value: Array[float]) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_float_meta_sound_literal(value: float) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_int_array_meta_sound_literal(value: Array[int]) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_int_meta_sound_literal(value: int) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_meta_sound_literal_from_param(param: AudioParameter) -> MetasoundFrontendLiteral
unreal.MetaSoundBuilderSubsystem.create_object_array_meta_sound_literal(value: Array[Object]) -> MetasoundFrontendLiteral
unreal.MetaSoundBuilderSubsystem.create_object_meta_sound_literal(value: Object) -> MetasoundFrontendLiteral
unreal.MetaSoundBuilderSubsystem.create_patch_builder(builder_name: Name) -> Tuple[MetaSoundPatchBuilder, MetaSoundBuilderResult]
unreal.MetaSoundBuilderSubsystem.create_patch_preset_builder(builder_name: Name, referenced_patch_class: MetaSoundDocumentInterface) -> Tuple[MetaSoundPatchBuilder, MetaSoundBuilderResult]
unreal.MetaSoundBuilderSubsystem.create_source_builder(builder_name: Name, output_format: MetaSoundOutputAudioFormat = MetaSoundOutputAudioFormat.MONO, is_one_shot: bool = True) -> Tuple[MetaSoundSourceBuilder, MetaSoundBuilderNodeOutputHandle, MetaSoundBuilderNodeInputHandle, Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderSubsystem.create_source_preset_builder(builder_name: Name, referenced_source_class: MetaSoundDocumentInterface) -> Tuple[MetaSoundSourceBuilder, MetaSoundBuilderResult]
unreal.MetaSoundBuilderSubsystem.create_string_array_meta_sound_literal(value: Array[str]) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.create_string_meta_sound_literal(value: str) -> Tuple[MetasoundFrontendLiteral, Name]
unreal.MetaSoundBuilderSubsystem.find_builder(builder_name: Name) -> MetaSoundBuilderBase
unreal.MetaSoundBuilderSubsystem.find_builder_of_document(meta_sound: MetaSoundDocumentInterface) -> MetaSoundBuilderBase
unreal.MetaSoundBuilderSubsystem.find_patch_builder(builder_name: Name) -> MetaSoundPatchBuilder
unreal.MetaSoundBuilderSubsystem.find_source_builder(builder_name: Name) -> MetaSoundSourceBuilder
unreal.MetaSoundBuilderSubsystem.is_interface_registered(interface_name: Name) -> bool
unreal.MetaSoundBuilderSubsystem.register_builder(builder_name: Name, builder: MetaSoundBuilderBase) -> None
unreal.MetaSoundBuilderSubsystem.register_patch_builder(builder_name: Name, builder: MetaSoundPatchBuilder) -> None
unreal.MetaSoundBuilderSubsystem.register_source_builder(builder_name: Name, builder: MetaSoundSourceBuilder) -> None
unreal.MetaSoundBuilderSubsystem.set_target_page(page_name: Name) -> bool
unreal.MetaSoundBuilderSubsystem.unregister_builder(builder_name: Name) -> bool
unreal.MetaSoundBuilderSubsystem.unregister_patch_builder(builder_name: Name) -> bool
unreal.MetaSoundBuilderSubsystem.unregister_source_builder(builder_name: Name) -> bool
```

## `unreal.MetaSoundCacheSubsystem(AudioEngineSubsystem)`

```python
unreal.MetaSoundCacheSubsystem.precache_meta_sound(meta_sound: MetaSoundSource, num_instances: int = 1) -> None
unreal.MetaSoundCacheSubsystem.remove_cached_operators_for_meta_sound(meta_sound: MetaSoundSource) -> None
unreal.MetaSoundCacheSubsystem.touch_or_precache_meta_sound(meta_sound: MetaSoundSource, num_instances: int = 1) -> None
```

## `unreal.MetaSoundEditorSubsystem(EditorSubsystem)`

```python
unreal.MetaSoundEditorSubsystem.build_to_asset(builder: MetaSoundBuilderBase, author: str, asset_name: str, package_path: str, template_sound_wave: SoundWave = None) -> Tuple[MetaSoundDocumentInterface, MetaSoundBuilderResult]
unreal.MetaSoundEditorSubsystem.find_or_begin_building(meta_sound: MetaSoundDocumentInterface) -> Tuple[MetaSoundBuilderBase, MetaSoundBuilderResult]
unreal.MetaSoundEditorSubsystem.find_or_create_graph_input_metadata(builder: MetaSoundBuilderBase, input_name: Name) -> Tuple[MetaSoundFrontendMemberMetadata, MetaSoundBuilderResult]
unreal.MetaSoundEditorSubsystem.set_focused_page(builder: MetaSoundBuilderBase, page_name: Name, open_editor: bool) -> MetaSoundBuilderResult
unreal.MetaSoundEditorSubsystem.set_node_location(builder: MetaSoundBuilderBase, node: MetaSoundNodeHandle, location: Vector2D) -> MetaSoundBuilderResult
```

## `unreal.MetaSoundOutputSubsystem(WorldSubsystem)`

```python
unreal.MetaSoundOutputSubsystem.watch_output(audio_component: AudioComponent, output_name: Name, on_output_value_changed: OnMetasoundOutputValueChanged, analyzer_name: Name = "None", analyzer_output_name: Name = "None") -> bool
```

## `unreal.ModelerEmbankActor(Actor)`

```python
unreal.ModelerEmbankActor.generate_mesh() -> None
unreal.ModelerEmbankActor.mesh_info(value: EmbankEntityInfo) -> None
```

## `unreal.ModelerFenceActor(Actor)`

```python
unreal.ModelerFenceActor.generate_mesh() -> None
unreal.ModelerFenceActor.mesh_info(value: FenceEntityInfo) -> None
```

## `unreal.ModelerFloorMeshActor(Actor)`

```python
unreal.ModelerFloorMeshActor.destroy_component() -> None
unreal.ModelerFloorMeshActor.generate_mesh() -> None
unreal.ModelerFloorMeshActor.mesh_info(value: FloorMeshInfo) -> None
```

## `unreal.ModelerRiverMeshActor(Actor)`

```python
unreal.ModelerRiverMeshActor.destroy_component() -> None
unreal.ModelerRiverMeshActor.generate_mesh() -> None
unreal.ModelerRiverMeshActor.mesh_info(value: RiverMeshInfo) -> None
```

## `unreal.ModelerTreeSamplerActor(Actor)`

```python
unreal.ModelerTreeSamplerActor.destroy_component() -> None
unreal.ModelerTreeSamplerActor.generate_mesh() -> None
unreal.ModelerTreeSamplerActor.mesh_info(value: TreeSamplerEntityInfo) -> None
unreal.ModelerTreeSamplerActor.random_seed() -> None
unreal.ModelerTreeSamplerActor.update_actor_transform() -> None
```

## `unreal.ModelerWaterMeshActor(Actor)`

```python
unreal.ModelerWaterMeshActor.destroy_component() -> None
unreal.ModelerWaterMeshActor.generate_mesh() -> None
unreal.ModelerWaterMeshActor.mesh_info(value: WaterMeshInfo) -> None
```

## `unreal.MotionExtractorModifier(AnimationModifier)`

```python
unreal.MotionExtractorModifier.absolute_value(value: bool) -> None
unreal.MotionExtractorModifier.axis(value: MotionExtractor_Axis) -> None
unreal.MotionExtractorModifier.bone_name(value: Name) -> None
unreal.MotionExtractorModifier.custom_curve_name(value: Name) -> None
unreal.MotionExtractorModifier.math_operation(value: MotionExtractor_MathOperation) -> None
unreal.MotionExtractorModifier.modifier(value: float) -> None
unreal.MotionExtractorModifier.motion_type(value: MotionExtractor_MotionType) -> None
unreal.MotionExtractorModifier.normalize(value: bool) -> None
unreal.MotionExtractorModifier.relative_to_bone_name(value: Name) -> None
unreal.MotionExtractorModifier.relative_to_first_frame(value: bool) -> None
unreal.MotionExtractorModifier.remove_curve_on_revert(value: bool) -> None
unreal.MotionExtractorModifier.space(value: MotionExtractor_Space) -> None
unreal.MotionExtractorModifier.use_custom_curve_name(value: bool) -> None
```

## `unreal.MotionExtractorUtilityLibrary(BlueprintFunctionLibrary)`

```python
unreal.MotionExtractorUtilityLibrary.generate_curve_name(bone_name: Name, motion_type: MotionExtractor_MotionType, axis: MotionExtractor_Axis) -> Name
unreal.MotionExtractorUtilityLibrary.get_desired_value(bone_transform: Transform, last_bone_transform: Transform, delta_time: float, motion_type: MotionExtractor_MotionType, axis: MotionExtractor_Axis) -> float
unreal.MotionExtractorUtilityLibrary.get_moving_ranges_from_root_motion(anim_sequence: AnimSequence, stop_speed_threshold: float = 10.000000, sample_rate: float = 120.000000) -> Array[Vector2D]
unreal.MotionExtractorUtilityLibrary.get_stopped_ranges_from_root_motion(anim_sequence: AnimSequence, stop_speed_threshold: float = 10.000000, sample_rate: float = 120.000000) -> Array[Vector2D]
```

## `unreal.MovieSceneActorPredictionFailure(MulticastDelegateBase)`

```python
unreal.MovieSceneActorPredictionFailure.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MovieSceneActorPredictionResult(MulticastDelegateBase)`

```python
unreal.MovieSceneActorPredictionResult.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MovieSceneLevelVisibilitySection(MovieSceneSection)`

```python
unreal.MovieSceneLevelVisibilitySection.get_level_names() -> Array[Name]
unreal.MovieSceneLevelVisibilitySection.get_visibility() -> LevelVisibility
unreal.MovieSceneLevelVisibilitySection.set_level_names(level_names: Array[Name]) -> None
unreal.MovieSceneLevelVisibilitySection.set_visibility(visibility: LevelVisibility) -> None
```

## `unreal.MovieSceneReplaceableActorBinding_BPBase(MovieSceneReplaceableBindingBase)`

```python
unreal.MovieSceneReplaceableActorBinding_BPBase.binding_type_pretty_name() -> Text
unreal.MovieSceneReplaceableActorBinding_BPBase.binding_type_tooltip() -> Text
unreal.MovieSceneReplaceableActorBinding_BPBase.bp_init_replaceable_binding(source_object: Object, owner_movie_scene: MovieScene) -> None
unreal.MovieSceneReplaceableActorBinding_BPBase.bp_resolve_runtime_binding(resolve_context: MovieSceneBindingResolveContext) -> MovieSceneBindingResolveResult
unreal.MovieSceneReplaceableActorBinding_BPBase.bp_supports_binding_creation_from_object(source_object: Object) -> bool
unreal.MovieSceneReplaceableActorBinding_BPBase.custom_binding_priority() -> int
unreal.MovieSceneReplaceableActorBinding_BPBase.preview_spawnable_type() -> Class
```

## `unreal.MovieSceneScriptingActorReferenceChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingActorReferenceChannel.add_key(time: FrameNumber, new_value: MovieSceneObjectBindingID, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingActorReferenceKey
unreal.MovieSceneScriptingActorReferenceChannel.get_default() -> MovieSceneObjectBindingID
unreal.MovieSceneScriptingActorReferenceChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingActorReferenceChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingActorReferenceChannel.has_default() -> bool
unreal.MovieSceneScriptingActorReferenceChannel.remove_default() -> None
unreal.MovieSceneScriptingActorReferenceChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingActorReferenceChannel.set_default(default_value: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneScriptingActorReferenceKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingActorReferenceKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingActorReferenceKey.get_value() -> MovieSceneObjectBindingID
unreal.MovieSceneScriptingActorReferenceKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingActorReferenceKey.set_value(new_value: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneSpawnableActorBindingBase(MovieSceneSpawnableBindingBase)`

```python
unreal.MovieSceneSpawnableActorBindingBase.level_name(value: Name) -> None
unreal.MovieSceneSpawnableActorBindingBase.net_addressable_name(value: bool) -> None
```

## `unreal.MovieSceneTransformOrigin(Interface)`

```python
unreal.MovieSceneTransformOrigin.bp_get_transform_origin() -> Transform
```

## `unreal.NamedTransform(StructBase)`

```python
unreal.NamedTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], name: Name = "None") -> None
unreal.NamedTransform.name(value: Name) -> None
unreal.NamedTransform.value(value: Transform) -> None
```

## `unreal.NavigationTestingActor(Actor)`

```python
unreal.NavigationTestingActor.path_cost() -> float
unreal.NavigationTestingActor.path_exist() -> bool
unreal.NavigationTestingActor.path_is_partial() -> bool
unreal.NavigationTestingActor.path_search_out_of_nodes() -> bool
unreal.NavigationTestingActor.pathfinding_steps() -> int
unreal.NavigationTestingActor.pathfinding_time() -> float
unreal.NavigationTestingActor.projected_location() -> Vector
unreal.NavigationTestingActor.projected_location_valid() -> bool
```

## `unreal.NiagaraActor(Actor)`

```python
unreal.NiagaraActor.get_destroy_on_system_finish() -> bool
unreal.NiagaraActor.niagara_component() -> NiagaraComponent
unreal.NiagaraActor.set_destroy_on_system_finish(should_destroy_on_system_finish: bool) -> None
```

## `unreal.NonBlendableTransformAnimationAttribute(TransformAnimationAttribute)`

```python
unreal.NonBlendableTransformAnimationAttribute.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.OnActorLabelChanged(MulticastDelegateBase)`

```python
unreal.OnActorLabelChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnActorReady(DelegateBase)`

```python
unreal.OnActorReady.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnBoneTransformsFinalized(MulticastDelegateBase)`

```python
unreal.OnBoneTransformsFinalized.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnDeleteActorsBegin(MulticastDelegateBase)`

```python
unreal.OnDeleteActorsBegin.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnDeleteActorsEnd(MulticastDelegateBase)`

```python
unreal.OnDeleteActorsEnd.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnDuplicateActorsBegin(MulticastDelegateBase)`

```python
unreal.OnDuplicateActorsBegin.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnDuplicateActorsEnd(MulticastDelegateBase)`

```python
unreal.OnDuplicateActorsEnd.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditCopyActorsBegin(MulticastDelegateBase)`

```python
unreal.OnEditCopyActorsBegin.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditCopyActorsEnd(MulticastDelegateBase)`

```python
unreal.OnEditCopyActorsEnd.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditCutActorsBegin(MulticastDelegateBase)`

```python
unreal.OnEditCutActorsBegin.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditCutActorsEnd(MulticastDelegateBase)`

```python
unreal.OnEditCutActorsEnd.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditNewActorsDropped(MulticastDelegateBase)`

```python
unreal.OnEditNewActorsDropped.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditNewActorsPlaced(MulticastDelegateBase)`

```python
unreal.OnEditNewActorsPlaced.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditPasteActorsBegin(MulticastDelegateBase)`

```python
unreal.OnEditPasteActorsBegin.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditPasteActorsEnd(MulticastDelegateBase)`

```python
unreal.OnEditPasteActorsEnd.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelEditorEditorCameraMoved(MulticastDelegateBase)`

```python
unreal.OnLevelEditorEditorCameraMoved.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelEditorMapChanged(MulticastDelegateBase)`

```python
unreal.OnLevelEditorMapChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelEditorMapOpened(MulticastDelegateBase)`

```python
unreal.OnLevelEditorMapOpened.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelEditorPostSaveWorld(MulticastDelegateBase)`

```python
unreal.OnLevelEditorPostSaveWorld.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelEditorPreSaveWorld(MulticastDelegateBase)`

```python
unreal.OnLevelEditorPreSaveWorld.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLevelSequencePlayerCameraCutEvent(MulticastDelegateBase)`

```python
unreal.OnLevelSequencePlayerCameraCutEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OptimusMultiLevelDataDomain(OptimusDataDomain)`

```python
unreal.OptimusMultiLevelDataDomain.__init__() -> None
```

## `unreal.PCGActorPropertyOverride(StructBase)`

```python
unreal.PCGActorPropertyOverride.__init__() -> None
```

## `unreal.PCGActorPropertyOverrideDescription(PCGObjectPropertyOverrideDescription)`

```python
unreal.PCGActorPropertyOverrideDescription.__init__() -> None
```

## `unreal.PCGActorSelectorSettings(StructBase)`

```python
unreal.PCGActorSelectorSettings.__init__(actor_filter: PCGActorFilter = PCGActorFilter.SELF, must_overlap_self: bool = False, include_children: bool = False, disable_filter: bool = False, actor_selection: PCGActorSelection = PCGActorSelection.BY_TAG, actor_selection_tag: Name = "None", actor_selection_class: Class = None, actor_reference_selector: PCGAttributePropertyInputSelector = [], select_multiple: bool = False, ignore_self_and_children: bool = False) -> None
unreal.PCGActorSelectorSettings.actor_filter(value: PCGActorFilter) -> None
unreal.PCGActorSelectorSettings.actor_reference_selector(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGActorSelectorSettings.actor_selection(value: PCGActorSelection) -> None
unreal.PCGActorSelectorSettings.actor_selection_class(value: Class) -> None
unreal.PCGActorSelectorSettings.actor_selection_tag(value: Name) -> None
unreal.PCGActorSelectorSettings.disable_filter(value: bool) -> None
unreal.PCGActorSelectorSettings.ignore_self_and_children(value: bool) -> None
unreal.PCGActorSelectorSettings.include_children(value: bool) -> None
unreal.PCGActorSelectorSettings.must_overlap_self(value: bool) -> None
unreal.PCGActorSelectorSettings.select_multiple(value: bool) -> None
```

## `unreal.PCGApplyOnActorSettings(PCGSettings)`

```python
unreal.PCGApplyOnActorSettings.object_reference_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGApplyOnActorSettings.post_process_function_names(value: Array[Name]) -> None
unreal.PCGApplyOnActorSettings.property_override_descriptions(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGApplyOnActorSettings.silence_error_on_empty_object_path(value: bool) -> None
unreal.PCGApplyOnActorSettings.synchronous_load(value: bool) -> None
unreal.PCGApplyOnActorSettings.target_actor(value: Actor) -> None
```

## `unreal.PCGCreateTargetActor(PCGSettings)`

```python
unreal.PCGCreateTargetActor.allow_template_actor_editing(value: bool) -> None
unreal.PCGCreateTargetActor.attach_options(value: PCGAttachOptions) -> None
unreal.PCGCreateTargetActor.post_process_function_names(value: Array[Name]) -> None
unreal.PCGCreateTargetActor.property_override_descriptions(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGCreateTargetActor.template_actor(value: Actor) -> None
unreal.PCGCreateTargetActor.template_actor_class() -> Class
```

## `unreal.PCGCullPointsOutsideActorBoundsSettings(PCGSettings)`

```python
unreal.PCGCullPointsOutsideActorBoundsSettings.bounds_expansion(value: float) -> None
unreal.PCGCullPointsOutsideActorBoundsSettings.mode(value: PCGCullPointsMode) -> None
```

## `unreal.PCGDataFromActorSettings(PCGSettings)`

```python
unreal.PCGDataFromActorSettings.actor_selector(value: PCGActorSelectorSettings) -> None
unreal.PCGDataFromActorSettings.allowed_grids(value: int) -> None
unreal.PCGDataFromActorSettings.also_output_single_point_data(value: bool) -> None
unreal.PCGDataFromActorSettings.component_selector(value: PCGComponentSelectorSettings) -> None
unreal.PCGDataFromActorSettings.components_must_overlap_self(value: bool) -> None
unreal.PCGDataFromActorSettings.expected_pins(value: Array[Name]) -> None
unreal.PCGDataFromActorSettings.get_data_on_all_grids(value: bool) -> None
unreal.PCGDataFromActorSettings.ignore_pcg_generated_components(value: bool) -> None
unreal.PCGDataFromActorSettings.merge_single_point_data(value: bool) -> None
unreal.PCGDataFromActorSettings.mode(value: PCGGetDataFromActorMode) -> None
unreal.PCGDataFromActorSettings.property_name(value: Name) -> None
unreal.PCGDataFromActorSettings.silence_sanitized_attribute_name_warnings(value: bool) -> None
unreal.PCGDataFromActorSettings.track_actors_only_within_bounds() -> bool
```

## `unreal.PCGDummyGetPropertyLevel2Struct(StructBase)`

```python
unreal.PCGDummyGetPropertyLevel2Struct.__init__(double_array_property: Array[float] = []) -> None
unreal.PCGDummyGetPropertyLevel2Struct.double_array_property() -> Array[float]
```

## `unreal.PCGDynamicMeshTransformSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGDynamicMeshTransformSettings.transform(value: Transform) -> None
```

## `unreal.PCGGetActorPropertySettings(PCGSettings)`

```python
unreal.PCGGetActorPropertySettings.actor_selector(value: PCGActorSelectorSettings) -> None
unreal.PCGGetActorPropertySettings.always_requery_actors(value: bool) -> None
unreal.PCGGetActorPropertySettings.component_class(value: Class) -> None
unreal.PCGGetActorPropertySettings.force_object_and_struct_extraction(value: bool) -> None
unreal.PCGGetActorPropertySettings.output_actor_reference(value: bool) -> None
unreal.PCGGetActorPropertySettings.output_attribute_name(value: Name) -> None
unreal.PCGGetActorPropertySettings.output_component_reference(value: bool) -> None
unreal.PCGGetActorPropertySettings.process_all_components(value: bool) -> None
unreal.PCGGetActorPropertySettings.property_name(value: Name) -> None
unreal.PCGGetActorPropertySettings.select_component(value: bool) -> None
unreal.PCGGetActorPropertySettings.track_actors_only_within_bounds() -> bool
```

## `unreal.PCGLevelToAsset(PCGAssetExporter)`

```python
unreal.PCGLevelToAsset.bp_export_world(world: World, package_name: str, asset: PCGDataAsset) -> bool
unreal.PCGLevelToAsset.get_world() -> World
unreal.PCGLevelToAsset.set_world(world: World) -> None
```

## `unreal.PCGManagedActors(PCGManagedResource)`

```python
unreal.PCGManagedActors.generated_actors(value: Set[Actor]) -> None
```

## `unreal.PCGMetadataBreakTransformSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataBreakTransformSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGMetadataMakeTransformSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataMakeTransformSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeTransformSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeTransformSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGMetadataTransformSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataTransformSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataTransformSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataTransformSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataTransformSettings.operation(value: PCGMetadataTransformOperation) -> None
unreal.PCGMetadataTransformSettings.transform_lerp_mode(value: PCGTransformLerpMode) -> None
```

## `unreal.PCGPartitionActor(PartitionActor)`

```python
unreal.PCGPartitionActor.get_local_component(original_component: PCGComponent) -> PCGComponent
unreal.PCGPartitionActor.get_original_component(local_component: PCGComponent) -> PCGComponent
```

## `unreal.PCGSpawnActorSettings(PCGBaseSubgraphSettings)`

```python
unreal.PCGSpawnActorSettings.allow_template_actor_editing(value: bool) -> None
unreal.PCGSpawnActorSettings.attach_options(value: PCGAttachOptions) -> None
unreal.PCGSpawnActorSettings.force_disable_actor_parsing(value: bool) -> None
unreal.PCGSpawnActorSettings.generation_trigger(value: PCGSpawnActorGenerationTrigger) -> None
unreal.PCGSpawnActorSettings.inherit_actor_tags(value: bool) -> None
unreal.PCGSpawnActorSettings.option(value: PCGSpawnActorOption) -> None
unreal.PCGSpawnActorSettings.post_spawn_function_names(value: Array[Name]) -> None
unreal.PCGSpawnActorSettings.spawn_attribute(value: Name) -> None
unreal.PCGSpawnActorSettings.spawn_by_attribute(value: bool) -> None
unreal.PCGSpawnActorSettings.spawned_actor_property_override_descriptions(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGSpawnActorSettings.tags_to_add_on_actors(value: Array[Name]) -> None
unreal.PCGSpawnActorSettings.template_actor(value: Actor) -> None
unreal.PCGSpawnActorSettings.template_actor_class() -> Class
unreal.PCGSpawnActorSettings.warn_on_identical_spawn(value: bool) -> None
```

## `unreal.PCGTransformPointsSettings(PCGSettings)`

```python
unreal.PCGTransformPointsSettings.absolute_offset(value: bool) -> None
unreal.PCGTransformPointsSettings.absolute_rotation(value: bool) -> None
unreal.PCGTransformPointsSettings.absolute_scale(value: bool) -> None
unreal.PCGTransformPointsSettings.apply_to_attribute(value: bool) -> None
unreal.PCGTransformPointsSettings.attribute_name(value: Name) -> None
unreal.PCGTransformPointsSettings.offset_max(value: Vector) -> None
unreal.PCGTransformPointsSettings.offset_min(value: Vector) -> None
unreal.PCGTransformPointsSettings.recompute_seed(value: bool) -> None
unreal.PCGTransformPointsSettings.rotation_max(value: Rotator) -> None
unreal.PCGTransformPointsSettings.rotation_min(value: Rotator) -> None
unreal.PCGTransformPointsSettings.scale_max(value: Vector) -> None
unreal.PCGTransformPointsSettings.scale_min(value: Vector) -> None
unreal.PCGTransformPointsSettings.uniform_scale(value: bool) -> None
```

## `unreal.PCGUnitTestDummyActor(Actor)`

```python
unreal.PCGUnitTestDummyActor.array_of_ints_property() -> Array[int]
unreal.PCGUnitTestDummyActor.array_of_objects_property() -> Array[PCGDummyGetPropertyTest]
unreal.PCGUnitTestDummyActor.array_of_structs_property() -> Array[PCGTestMyColorStruct]
unreal.PCGUnitTestDummyActor.array_of_vectors_property() -> Array[Vector]
unreal.PCGUnitTestDummyActor.bool_property() -> bool
unreal.PCGUnitTestDummyActor.class_property() -> Class
unreal.PCGUnitTestDummyActor.color_property() -> Color
unreal.PCGUnitTestDummyActor.double_property() -> float
unreal.PCGUnitTestDummyActor.dummy_struct() -> PCGDummyGetPropertyStruct
unreal.PCGUnitTestDummyActor.enum_property() -> PCGUnitTestDummyEnum
unreal.PCGUnitTestDummyActor.float_property() -> float
unreal.PCGUnitTestDummyActor.int64_property() -> int
unreal.PCGUnitTestDummyActor.int_property() -> int
unreal.PCGUnitTestDummyActor.linear_color_property() -> LinearColor
unreal.PCGUnitTestDummyActor.name_property() -> Name
unreal.PCGUnitTestDummyActor.object_property() -> PCGDummyGetPropertyTest
unreal.PCGUnitTestDummyActor.pcg_color_property() -> PCGTestMyColorStruct
unreal.PCGUnitTestDummyActor.quat_property() -> Quat
unreal.PCGUnitTestDummyActor.rotator_property() -> Rotator
unreal.PCGUnitTestDummyActor.set_of_ints_property() -> Array[int]
unreal.PCGUnitTestDummyActor.soft_class_path_property() -> SoftClassPath
unreal.PCGUnitTestDummyActor.soft_object_path_property() -> SoftObjectPath
unreal.PCGUnitTestDummyActor.string_property() -> str
unreal.PCGUnitTestDummyActor.transform_property() -> Transform
unreal.PCGUnitTestDummyActor.vector2_property() -> Vector2D
unreal.PCGUnitTestDummyActor.vector4_property() -> Vector4
unreal.PCGUnitTestDummyActor.vector_property() -> Vector
```

## `unreal.PCGWorldActor(Actor)`

```python
unreal.PCGWorldActor.landscape_cache_object() -> PCGLandscapeCache
unreal.PCGWorldActor.treat_editor_viewport_as_generation_source(value: bool) -> None
```

## `unreal.PCGWorldCommonQueryParams(StructBase)`

```python
unreal.PCGWorldCommonQueryParams.__init__(ignore_pcg_hits: bool = False, ignore_self_hits: bool = False, collision_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, trace_complex: bool = False, actor_tag_filter: PCGWorldQueryFilterByTag = PCGWorldQueryFilterByTag.NO_TAG_FILTER, actor_tags_list: str = "", select_landscape_hits: PCGWorldQuerySelectLandscapeHits = PCGWorldQuerySelectLandscapeHits.EXCLUDE, get_reference_to_actor_hit: bool = False, get_reference_to_physical_material: bool = False) -> None
unreal.PCGWorldCommonQueryParams.actor_tag_filter(value: PCGWorldQueryFilterByTag) -> None
unreal.PCGWorldCommonQueryParams.actor_tags_list(value: str) -> None
unreal.PCGWorldCommonQueryParams.collision_channel(value: CollisionChannel) -> None
unreal.PCGWorldCommonQueryParams.get_reference_to_actor_hit(value: bool) -> None
unreal.PCGWorldCommonQueryParams.get_reference_to_physical_material(value: bool) -> None
unreal.PCGWorldCommonQueryParams.ignore_landscape_hits(value: bool) -> None
unreal.PCGWorldCommonQueryParams.ignore_pcg_hits(value: bool) -> None
unreal.PCGWorldCommonQueryParams.ignore_self_hits(value: bool) -> None
unreal.PCGWorldCommonQueryParams.select_landscape_hits(value: PCGWorldQuerySelectLandscapeHits) -> None
unreal.PCGWorldCommonQueryParams.trace_complex(value: bool) -> None
```

## `unreal.PCGWorldQuerySettings(PCGSettings)`

```python
unreal.PCGWorldQuerySettings.query_params(value: PCGWorldVolumetricQueryParams) -> None
```

## `unreal.PCGWorldRayHitData(PCGSurfaceData)`

```python
unreal.PCGWorldRayHitData.query_params(value: PCGWorldRayHitQueryParams) -> None
```

## `unreal.PCGWorldRayHitQueryParams(PCGWorldRaycastQueryParams)`

```python
unreal.PCGWorldRayHitQueryParams.__init__(ignore_pcg_hits: bool = False, ignore_self_hits: bool = False, collision_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, trace_complex: bool = False, actor_tag_filter: PCGWorldQueryFilterByTag = PCGWorldQueryFilterByTag.NO_TAG_FILTER, actor_tags_list: str = "", select_landscape_hits: PCGWorldQuerySelectLandscapeHits = PCGWorldQuerySelectLandscapeHits.EXCLUDE, get_reference_to_actor_hit: bool = False, get_reference_to_physical_material: bool = False, ignore_backface_hits: bool = False, get_impact: bool = False, get_impact_point: bool = False, get_impact_normal: bool = False, get_reflection: bool = False, get_distance: bool = False, get_local_impact_point: bool = False, get_reference_to_render_material: bool = False, get_reference_to_static_mesh: bool = False, get_face_index: bool = False, get_uv_coords: bool = False, get_element_index: bool = False, apply_metadata_from_landscape: bool = False, render_material_index: int = 0, uv_channel: int = 0, override_default_params: bool = False, ray_origin: Vector = [0.000000, 0.000000, 0.000000], ray_direction: Vector = [0.000000, 0.000000, 0.000000], ray_length: float = 0.000000) -> None
unreal.PCGWorldRayHitQueryParams.override_default_params(value: bool) -> None
unreal.PCGWorldRayHitQueryParams.ray_direction(value: Vector) -> None
unreal.PCGWorldRayHitQueryParams.ray_length(value: float) -> None
unreal.PCGWorldRayHitQueryParams.ray_origin(value: Vector) -> None
```

## `unreal.PCGWorldRayHitSettings(PCGSettings)`

```python
unreal.PCGWorldRayHitSettings.query_params(value: PCGWorldRayHitQueryParams) -> None
```

## `unreal.PCGWorldRaycastElementSettings(PCGSettings)`

```python
unreal.PCGWorldRaycastElementSettings.end_point_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGWorldRaycastElementSettings.keep_original_point_on_miss(value: bool) -> None
unreal.PCGWorldRaycastElementSettings.origin_input_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGWorldRaycastElementSettings.override_ray_directions(value: bool) -> None
unreal.PCGWorldRaycastElementSettings.override_ray_lengths(value: bool) -> None
unreal.PCGWorldRaycastElementSettings.ray_direction(value: Vector) -> None
unreal.PCGWorldRaycastElementSettings.ray_direction_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGWorldRaycastElementSettings.ray_length(value: float) -> None
unreal.PCGWorldRaycastElementSettings.ray_length_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGWorldRaycastElementSettings.raycast_mode(value: PCGWorldRaycastMode) -> None
unreal.PCGWorldRaycastElementSettings.unbounded(value: bool) -> None
unreal.PCGWorldRaycastElementSettings.world_query_params(value: PCGWorldRaycastQueryParams) -> None
```

## `unreal.PCGWorldRaycastQueryParams(PCGWorldCommonQueryParams)`

```python
unreal.PCGWorldRaycastQueryParams.__init__(ignore_pcg_hits: bool = False, ignore_self_hits: bool = False, collision_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, trace_complex: bool = False, actor_tag_filter: PCGWorldQueryFilterByTag = PCGWorldQueryFilterByTag.NO_TAG_FILTER, actor_tags_list: str = "", select_landscape_hits: PCGWorldQuerySelectLandscapeHits = PCGWorldQuerySelectLandscapeHits.EXCLUDE, get_reference_to_actor_hit: bool = False, get_reference_to_physical_material: bool = False, ignore_backface_hits: bool = False, get_impact: bool = False, get_impact_point: bool = False, get_impact_normal: bool = False, get_reflection: bool = False, get_distance: bool = False, get_local_impact_point: bool = False, get_reference_to_render_material: bool = False, get_reference_to_static_mesh: bool = False, get_face_index: bool = False, get_uv_coords: bool = False, get_element_index: bool = False, apply_metadata_from_landscape: bool = False, render_material_index: int = 0, uv_channel: int = 0) -> None
unreal.PCGWorldRaycastQueryParams.apply_metadata_from_landscape(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_distance(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_element_index(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_face_index(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_impact(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_impact_normal(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_impact_point(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_local_impact_point(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_reference_to_render_material(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_reference_to_static_mesh(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_reflection(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.get_uv_coords(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.ignore_backface_hits(value: bool) -> None
unreal.PCGWorldRaycastQueryParams.render_material_index(value: int) -> None
unreal.PCGWorldRaycastQueryParams.uv_channel(value: int) -> None
```

## `unreal.PCGWorldVolumetricData(PCGVolumeData)`

```python
unreal.PCGWorldVolumetricData.query_params(value: PCGWorldVolumetricQueryParams) -> None
```

## `unreal.PCGWorldVolumetricQueryParams(PCGWorldCommonQueryParams)`

```python
unreal.PCGWorldVolumetricQueryParams.__init__(ignore_pcg_hits: bool = False, ignore_self_hits: bool = False, collision_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, trace_complex: bool = False, actor_tag_filter: PCGWorldQueryFilterByTag = PCGWorldQueryFilterByTag.NO_TAG_FILTER, actor_tags_list: str = "", select_landscape_hits: PCGWorldQuerySelectLandscapeHits = PCGWorldQuerySelectLandscapeHits.EXCLUDE, get_reference_to_actor_hit: bool = False, get_reference_to_physical_material: bool = False, search_for_overlap: bool = False) -> None
unreal.PCGWorldVolumetricQueryParams.search_for_overlap(value: bool) -> None
```

## `unreal.PaperFlipbookActor(Actor)`

```python
unreal.PaperFlipbookActor.render_component() -> PaperFlipbookComponent
```

## `unreal.PaperGroupedSpriteActor(Actor)`

```python
unreal.PaperGroupedSpriteActor.render_component() -> PaperGroupedSpriteComponent
```

## `unreal.PaperSpriteActor(Actor)`

```python
unreal.PaperSpriteActor.render_component() -> PaperSpriteComponent
```

## `unreal.PaperTerrainActor(Actor)`

```python
unreal.PaperTerrainActor.render_component() -> PaperTerrainComponent
```

## `unreal.PaperTileMapActor(Actor)`

```python
unreal.PaperTileMapActor.render_component() -> PaperTileMapComponent
```

## `unreal.PerQualityLevelFloat(StructBase)`

```python
unreal.PerQualityLevelFloat.__init__(default: float = 0.000000) -> None
unreal.PerQualityLevelFloat.default() -> float
```

## `unreal.PerQualityLevelInt(StructBase)`

```python
unreal.PerQualityLevelInt.__init__(default: int = 0) -> None
unreal.PerQualityLevelInt.default() -> int
```

## `unreal.PhasedAutomationActorBase(Actor)`

```python
unreal.PhasedAutomationActorBase.on_functional_testing_begin() -> None
unreal.PhasedAutomationActorBase.on_functional_testing_complete() -> None
```

## `unreal.PhysicsConstraintActor(RigidBodyBase)`

```python
unreal.PhysicsConstraintActor.constraint_comp() -> PhysicsConstraintComponent
```

## `unreal.PoiSubsystem(GameInstanceSubsystem)`

```python
unreal.PoiSubsystem.get() -> PoiSubsystem
unreal.PoiSubsystem.register_screen_layer(layer_name: Name, z_order: int) -> bool
```

## `unreal.PointCloudBpActor(LidarPointCloudActor)`

```python
unreal.PointCloudBpActor.back_ground_color(value: Color) -> None
unreal.PointCloudBpActor.colors(value: Array[LinearColor]) -> None
unreal.PointCloudBpActor.datas(value: Array[PointCloudData]) -> None
unreal.PointCloudBpActor.is_sphere(value: bool) -> None
unreal.PointCloudBpActor.on_construction() -> None
unreal.PointCloudBpActor.refresh_data() -> None
unreal.PointCloudBpActor.set_point_cloud_back_ground_color(color: Color) -> None
unreal.PointCloudBpActor.set_point_cloud_data_colors(m_colors: Array[LinearColor]) -> None
unreal.PointCloudBpActor.set_point_cloud_datas(point_cloud_datas: Array[PointCloudData], point_cloudis_sphere: bool = True) -> None
unreal.PointCloudBpActor.set_point_cloud_material(custom_material: MaterialInterface) -> None
unreal.PointCloudBpActor.set_point_cloud_size(size: float) -> None
```

## `unreal.PolylinesGraphicsActor(WdpStandardActorEntity)`

```python
unreal.PolylinesGraphicsActor.add_entities(eids: Array[int], coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.ALTITUDE) -> None
unreal.PolylinesGraphicsActor.clear() -> None
unreal.PolylinesGraphicsActor.get_polyline(guid: Guid) -> Optional[PolylineGraphicsData]
unreal.PolylinesGraphicsActor.remove_entities(eids: Array[int]) -> None
unreal.PolylinesGraphicsActor.remove_polylines(guids: Array[Guid]) -> None
unreal.PolylinesGraphicsActor.set_polylines(polylines: Array[PolylineGraphicsData]) -> None
```

## `unreal.PoseDriverTransform(StructBase)`

```python
unreal.PoseDriverTransform.__init__() -> None
```

## `unreal.ProjectObjectTransform(StructBase)`

```python
unreal.ProjectObjectTransform.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotator: Rotator = [0.000000, 0.000000, 0.000000], scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.ProjectObjectTransform.location() -> Vector
unreal.ProjectObjectTransform.rotator() -> Rotator
unreal.ProjectObjectTransform.scale3d() -> Vector
```

## `unreal.ProjectObjectTransformParams(ParamsBase)`

```python
unreal.ProjectObjectTransformParams.__init__(eid: int = 0, location: Vector = [0.000000, 0.000000, 0.000000], rotator: Rotator = [0.000000, 0.000000, 0.000000], scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.ProjectObjectTransformParams.eid(value: int) -> None
unreal.ProjectObjectTransformParams.location() -> Vector
unreal.ProjectObjectTransformParams.rotator() -> Rotator
unreal.ProjectObjectTransformParams.scale3d() -> Vector
```

## `unreal.ProjectObjectTransformResult(ResultBase)`

```python
unreal.ProjectObjectTransformResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, transforms: Array[ProjectObjectTransform] = []) -> None
unreal.ProjectObjectTransformResult.transforms() -> Array[ProjectObjectTransform]
```

## `unreal.PythonLevelLib(BlueprintFunctionLibrary)`

```python
unreal.PythonLevelLib.apply_world_offset(level: Level, position: IntVector) -> None
unreal.PythonLevelLib.delete_umap(level: Object) -> None
unreal.PythonLevelLib.get_levels(world_in: World) -> Array[Level]
unreal.PythonLevelLib.remove_level_from_world(level_short_name: str) -> bool
```

## `unreal.QuartzSubsystem(TickableWorldSubsystem)`

```python
unreal.QuartzSubsystem.create_new_clock(world_context_object: Object, clock_name: Name, settings: QuartzClockSettings, override_settings_if_clock_exists: bool = False, use_audio_engine_clock_manager: bool = True) -> QuartzClockHandle
unreal.QuartzSubsystem.delete_clock_by_handle(world_context_object: Object, clock_handle: QuartzClockHandle) -> QuartzClockHandle
unreal.QuartzSubsystem.delete_clock_by_name(world_context_object: Object, clock_name: Name) -> None
unreal.QuartzSubsystem.does_clock_exist(world_context_object: Object, clock_name: Name) -> bool
unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_average_latency() -> float
unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_max_latency() -> float
unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_min_latency() -> float
unreal.QuartzSubsystem.get_current_clock_timestamp(world_context_object: Object, clock_name: Name) -> QuartzTransportTimeStamp
unreal.QuartzSubsystem.get_duration_of_quantization_type_in_seconds(world_context_object: Object, clock_name: Name, quantization_type: QuartzCommandQuantization, multiplier: float = 1.000000) -> float
unreal.QuartzSubsystem.get_estimated_clock_run_time(world_context_object: Object, clock_name: Name) -> float
unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_average_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_max_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_min_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.get_handle_for_clock(world_context_object: Object, clock_name: Name) -> QuartzClockHandle
unreal.QuartzSubsystem.get_round_trip_average_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.get_round_trip_max_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.get_round_trip_min_latency(world_context_object: Object) -> float
unreal.QuartzSubsystem.is_clock_running(world_context_object: Object, clock_name: Name) -> bool
unreal.QuartzSubsystem.is_quartz_enabled() -> bool
unreal.QuartzSubsystem.set_quartz_subsystem_tickable_when_paused(tickable_when_paused: bool) -> None
```

## `unreal.RadialForceActor(RigidBodyBase)`

```python
unreal.RadialForceActor.disable_force() -> None
unreal.RadialForceActor.enable_force() -> None
unreal.RadialForceActor.fire_impulse() -> None
unreal.RadialForceActor.force_component() -> RadialForceComponent
unreal.RadialForceActor.toggle_force() -> None
```

## `unreal.RegionScaleFactors(StructBase)`

```python
unreal.RegionScaleFactors.__init__(positive_width: float = 0.000000, negative_width: float = 0.000000, positive_height: float = 0.000000, negative_height: float = 0.000000) -> None
unreal.RegionScaleFactors.negative_height(value: float) -> None
unreal.RegionScaleFactors.negative_width(value: float) -> None
unreal.RegionScaleFactors.positive_height(value: float) -> None
unreal.RegionScaleFactors.positive_width(value: float) -> None
```

## `unreal.ReplaySubsystem(GameInstanceSubsystem)`

```python
unreal.ReplaySubsystem.get_active_replay_name() -> str
unreal.ReplaySubsystem.get_replay_current_time() -> float
unreal.ReplaySubsystem.is_playing() -> bool
unreal.ReplaySubsystem.is_recording() -> bool
unreal.ReplaySubsystem.request_checkpoint() -> None
```

## `unreal.RigComputedTransform(StructBase)`

```python
unreal.RigComputedTransform.__init__() -> None
```

## `unreal.RigCurrentAndInitialTransform(StructBase)`

```python
unreal.RigCurrentAndInitialTransform.__init__(current: RigLocalAndGlobalTransform = [[], []], initial: RigLocalAndGlobalTransform = [[], []]) -> None
unreal.RigCurrentAndInitialTransform.current() -> RigLocalAndGlobalTransform
unreal.RigCurrentAndInitialTransform.initial() -> RigLocalAndGlobalTransform
```

## `unreal.RigLocalAndGlobalTransform(StructBase)`

```python
unreal.RigLocalAndGlobalTransform.__init__(local: RigComputedTransform = [], global_: RigComputedTransform = []) -> None
unreal.RigLocalAndGlobalTransform.global_() -> RigComputedTransform
unreal.RigLocalAndGlobalTransform.local() -> RigComputedTransform
```

## `unreal.RigTransformDirtyState(StructBase)`

```python
unreal.RigTransformDirtyState.__init__() -> None
```

## `unreal.RigTransformElement(RigBaseElement)`

```python
unreal.RigTransformElement.__init__(key: RigElementKey = [RigElementType.NONE, "None"], index: int = 0, sub_index: int = 0, created_at_instruction_index: int = 0, selected: bool = False) -> None
```

## `unreal.RigUnit_AccumulateTransformLerp(RigVMFunction_AccumulateTransformLerp)`

```python
unreal.RigUnit_AccumulateTransformLerp.__init__(target_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], initial_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], blend: float = 0.000000, integrate_delta_time: bool = False, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_AccumulateTransformMul(RigVMFunction_AccumulateTransformMul)`

```python
unreal.RigUnit_AccumulateTransformMul.__init__(multiplier: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], initial_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], flip_order: bool = False, integrate_delta_time: bool = False, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_AddBoneTransform(RigUnitMutable)`

```python
unreal.RigUnit_AddBoneTransform.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, post_multiply: bool = False, propagate_to_children: bool = False) -> None
unreal.RigUnit_AddBoneTransform.bone(value: Name) -> None
unreal.RigUnit_AddBoneTransform.post_multiply(value: bool) -> None
unreal.RigUnit_AddBoneTransform.propagate_to_children() -> bool
unreal.RigUnit_AddBoneTransform.transform(value: Transform) -> None
unreal.RigUnit_AddBoneTransform.weight(value: float) -> None
```

## `unreal.RigUnit_AimConstraint_WorldUp(StructBase)`

```python
unreal.RigUnit_AimConstraint_WorldUp.__init__(target: Vector = [0.000000, 0.000000, 0.000000], kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION, space: RigElementKey = [RigElementType.NONE, "None"]) -> None
unreal.RigUnit_AimConstraint_WorldUp.kind(value: ControlRigVectorKind) -> None
unreal.RigUnit_AimConstraint_WorldUp.space(value: RigElementKey) -> None
unreal.RigUnit_AimConstraint_WorldUp.target(value: Vector) -> None
```

## `unreal.RigUnit_BinaryTransformOp(RigUnit)`

```python
unreal.RigUnit_BinaryTransformOp.__init__(argument0: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], argument1: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_BinaryTransformOp.argument0(value: Transform) -> None
unreal.RigUnit_BinaryTransformOp.argument1(value: Transform) -> None
unreal.RigUnit_BinaryTransformOp.result() -> Transform
```

## `unreal.RigUnit_BlendTransform(RigUnit)`

```python
unreal.RigUnit_BlendTransform.__init__(source: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], targets: Array[BlendTarget] = [], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_BlendTransform.result() -> Transform
unreal.RigUnit_BlendTransform.source(value: Transform) -> None
unreal.RigUnit_BlendTransform.targets(value: Array[BlendTarget]) -> None
```

## `unreal.RigUnit_ControlRigSplineFromTransforms(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_ControlRigSplineFromTransforms.__init__(transforms: Array[Transform] = [], spline_mode: SplineType = SplineType.B_SPLINE, closed: bool = False, samples_per_segment: int = 0, compression: float = 0.000000, stretch: float = 0.000000, spline: ControlRigSpline = []) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.closed(value: bool) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.compression(value: float) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.samples_per_segment(value: int) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.spline() -> ControlRigSpline
unreal.RigUnit_ControlRigSplineFromTransforms.spline_mode(value: SplineType) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.stretch(value: float) -> None
unreal.RigUnit_ControlRigSplineFromTransforms.transforms(value: Array[Transform]) -> None
```

## `unreal.RigUnit_ConvertEulerTransform(RigUnit)`

```python
unreal.RigUnit_ConvertEulerTransform.__init__(input: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ConvertEulerTransform.input(value: EulerTransform) -> None
unreal.RigUnit_ConvertEulerTransform.result() -> Transform
```

## `unreal.RigUnit_ConvertTransform(RigUnit)`

```python
unreal.RigUnit_ConvertTransform.__init__(input: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ConvertTransform.input(value: Transform) -> None
unreal.RigUnit_ConvertTransform.result() -> EulerTransform
```

## `unreal.RigUnit_DebugTransform(RigUnit_DebugBase)`

```python
unreal.RigUnit_DebugTransform.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, space: Name = "None", world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugTransform.color(value: LinearColor) -> None
unreal.RigUnit_DebugTransform.enabled() -> bool
unreal.RigUnit_DebugTransform.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigUnit_DebugTransform.scale(value: float) -> None
unreal.RigUnit_DebugTransform.space(value: Name) -> None
unreal.RigUnit_DebugTransform.thickness(value: float) -> None
unreal.RigUnit_DebugTransform.transform(value: Transform) -> None
unreal.RigUnit_DebugTransform.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DebugTransformArrayMutable(RigUnit_DebugBaseMutable)`

```python
unreal.RigUnit_DebugTransformArrayMutable.__init__(execute_context: ControlRigExecuteContext = [], transforms: Array[Transform] = [], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, space: Name = "None", world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugTransformArrayMutable.color(value: LinearColor) -> None
unreal.RigUnit_DebugTransformArrayMutable.enabled() -> bool
unreal.RigUnit_DebugTransformArrayMutable.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigUnit_DebugTransformArrayMutable.scale(value: float) -> None
unreal.RigUnit_DebugTransformArrayMutable.space(value: Name) -> None
unreal.RigUnit_DebugTransformArrayMutable.thickness(value: float) -> None
unreal.RigUnit_DebugTransformArrayMutable.transforms(value: Array[Transform]) -> None
unreal.RigUnit_DebugTransformArrayMutable.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DebugTransformArrayMutableItemSpace(RigUnit_DebugBaseMutable)`

```python
unreal.RigUnit_DebugTransformArrayMutableItemSpace.__init__(execute_context: ControlRigExecuteContext = [], transforms: Array[Transform] = [], parent_indices: Array[int] = [], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, space: RigElementKey = [RigElementType.NONE, "None"], world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.color(value: LinearColor) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.enabled(value: bool) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.parent_indices(value: Array[int]) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.scale(value: float) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.space(value: RigElementKey) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.thickness(value: float) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.transforms(value: Array[Transform]) -> None
unreal.RigUnit_DebugTransformArrayMutableItemSpace.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DebugTransformMutable(RigUnit_DebugBaseMutable)`

```python
unreal.RigUnit_DebugTransformMutable.__init__(execute_context: ControlRigExecuteContext = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, space: Name = "None", world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugTransformMutable.color(value: LinearColor) -> None
unreal.RigUnit_DebugTransformMutable.enabled() -> bool
unreal.RigUnit_DebugTransformMutable.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigUnit_DebugTransformMutable.scale(value: float) -> None
unreal.RigUnit_DebugTransformMutable.space(value: Name) -> None
unreal.RigUnit_DebugTransformMutable.thickness(value: float) -> None
unreal.RigUnit_DebugTransformMutable.transform(value: Transform) -> None
unreal.RigUnit_DebugTransformMutable.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DebugTransformMutableItemSpace(RigUnit_DebugBaseMutable)`

```python
unreal.RigUnit_DebugTransformMutableItemSpace.__init__(execute_context: ControlRigExecuteContext = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, space: RigElementKey = [RigElementType.NONE, "None"], world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.color(value: LinearColor) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.enabled(value: bool) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.scale(value: float) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.space(value: RigElementKey) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.thickness(value: float) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.transform(value: Transform) -> None
unreal.RigUnit_DebugTransformMutableItemSpace.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DeltaFromPreviousTransform(RigVMFunction_DeltaFromPreviousTransform)`

```python
unreal.RigUnit_DeltaFromPreviousTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], delta: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], previous_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_DrawContainerSetTransform(RigUnitMutable)`

```python
unreal.RigUnit_DrawContainerSetTransform.__init__(execute_context: ControlRigExecuteContext = [], instruction_name: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_DrawContainerSetTransform.instruction_name() -> Name
unreal.RigUnit_DrawContainerSetTransform.transform(value: Transform) -> None
```

## `unreal.RigUnit_GetBoneTransform(RigUnit)`

```python
unreal.RigUnit_GetBoneTransform.__init__(bone: Name = "None", space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetBoneTransform.bone(value: Name) -> None
unreal.RigUnit_GetBoneTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetBoneTransform.transform() -> Transform
```

## `unreal.RigUnit_GetControlInitialTransform(RigUnit)`

```python
unreal.RigUnit_GetControlInitialTransform.__init__(control: Name = "None", space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetControlInitialTransform.control(value: Name) -> None
unreal.RigUnit_GetControlInitialTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetControlInitialTransform.transform() -> Transform
```

## `unreal.RigUnit_GetControlTransform(RigUnit)`

```python
unreal.RigUnit_GetControlTransform.__init__(control: Name = "None", space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], minimum: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], maximum: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetControlTransform.control(value: Name) -> None
unreal.RigUnit_GetControlTransform.maximum() -> Transform
unreal.RigUnit_GetControlTransform.minimum() -> Transform
unreal.RigUnit_GetControlTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetControlTransform.transform() -> Transform
```

## `unreal.RigUnit_GetInitialBoneTransform(RigUnit)`

```python
unreal.RigUnit_GetInitialBoneTransform.__init__(bone: Name = "None", space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetInitialBoneTransform.bone(value: Name) -> None
unreal.RigUnit_GetInitialBoneTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetInitialBoneTransform.transform() -> Transform
```

## `unreal.RigUnit_GetJointTransform(RigUnitMutable)`

```python
unreal.RigUnit_GetJointTransform.__init__(execute_context: ControlRigExecuteContext = [], joint: Name = "None", type: TransformGetterType = TransformGetterType.INITIAL, transform_space: TransformSpaceMode = TransformSpaceMode.LOCAL_SPACE, base_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], base_joint: Name = "None", output: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetJointTransform.base_joint(value: Name) -> None
unreal.RigUnit_GetJointTransform.base_transform(value: Transform) -> None
unreal.RigUnit_GetJointTransform.joint(value: Name) -> None
unreal.RigUnit_GetJointTransform.output() -> Transform
unreal.RigUnit_GetJointTransform.transform_space(value: TransformSpaceMode) -> None
unreal.RigUnit_GetJointTransform.type(value: TransformGetterType) -> None
```

## `unreal.RigUnit_GetRelativeBoneTransform(RigUnit)`

```python
unreal.RigUnit_GetRelativeBoneTransform.__init__(bone: Name = "None", space: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetRelativeBoneTransform.bone(value: Name) -> None
unreal.RigUnit_GetRelativeBoneTransform.space(value: Name) -> None
unreal.RigUnit_GetRelativeBoneTransform.transform() -> Transform
```

## `unreal.RigUnit_GetRelativeTransform(RigUnit_BinaryTransformOp)`

```python
unreal.RigUnit_GetRelativeTransform.__init__(argument0: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], argument1: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_GetRelativeTransformForItem(RigUnit)`

```python
unreal.RigUnit_GetRelativeTransformForItem.__init__(child: RigElementKey = [RigElementType.NONE, "None"], child_initial: bool = False, parent: RigElementKey = [RigElementType.NONE, "None"], parent_initial: bool = False, relative_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetRelativeTransformForItem.child(value: RigElementKey) -> None
unreal.RigUnit_GetRelativeTransformForItem.child_initial(value: bool) -> None
unreal.RigUnit_GetRelativeTransformForItem.parent(value: RigElementKey) -> None
unreal.RigUnit_GetRelativeTransformForItem.parent_initial(value: bool) -> None
unreal.RigUnit_GetRelativeTransformForItem.relative_transform() -> Transform
```

## `unreal.RigUnit_GetShapeTransform(RigUnit)`

```python
unreal.RigUnit_GetShapeTransform.__init__(control: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetShapeTransform.control(value: Name) -> None
unreal.RigUnit_GetShapeTransform.transform() -> Transform
```

## `unreal.RigUnit_GetSpaceTransform(RigUnit)`

```python
unreal.RigUnit_GetSpaceTransform.__init__(space: Name = "None", space_type: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetSpaceTransform.space(value: Name) -> None
unreal.RigUnit_GetSpaceTransform.space_type(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetSpaceTransform.transform() -> Transform
```

## `unreal.RigUnit_GetTransform(RigUnit)`

```python
unreal.RigUnit_GetTransform.__init__(item: RigElementKey = [RigElementType.NONE, "None"], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetTransform.initial(value: bool) -> None
unreal.RigUnit_GetTransform.item(value: RigElementKey) -> None
unreal.RigUnit_GetTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetTransform.transform() -> Transform
```

## `unreal.RigUnit_GetTransformAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetTransformAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetTransformAnimationChannel.value() -> Transform
```

## `unreal.RigUnit_GetTransformAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetTransformAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_GetTransformAnimationChannelFromItem.value() -> Transform
```

## `unreal.RigUnit_GetTransformArray(RigUnit)`

```python
unreal.RigUnit_GetTransformArray.__init__(items: RigElementKeyCollection = [[]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, transforms: Array[Transform] = []) -> None
unreal.RigUnit_GetTransformArray.initial(value: bool) -> None
unreal.RigUnit_GetTransformArray.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_GetTransformArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetTransformArray.transforms() -> Array[Transform]
```

## `unreal.RigUnit_GetTransformItemArray(RigUnit)`

```python
unreal.RigUnit_GetTransformItemArray.__init__(items: Array[RigElementKey] = [], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, transforms: Array[Transform] = []) -> None
unreal.RigUnit_GetTransformItemArray.initial(value: bool) -> None
unreal.RigUnit_GetTransformItemArray.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_GetTransformItemArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_GetTransformItemArray.transforms() -> Array[Transform]
```

## `unreal.RigUnit_GetWorldTime(RigVMFunction_GetWorldTime)`

```python
unreal.RigUnit_GetWorldTime.__init__(year: float = 0.000000, month: float = 0.000000, day: float = 0.000000, week_day: float = 0.000000, hours: float = 0.000000, minutes: float = 0.000000, seconds: float = 0.000000, overall_seconds: float = 0.000000) -> None
```

## `unreal.RigUnit_HierarchyAddControlTransform(RigUnit_HierarchyAddControlElement)`

```python
unreal.RigUnit_HierarchyAddControlTransform.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], offset_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], offset_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], settings: RigUnit_HierarchyAddControlTransform_Settings = [RigVMTransformSpace.LOCAL_SPACE, False, EulerRotationOrder.YZX, [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [[-100.000000, -100.000000, -100.000000], [-180.000000, -180.000000, -180.000000], [0.000000, 0.000000, 0.000000]], [[100.000000, 100.000000, 100.000000], [180.000000, 180.000000, 180.000000], [10.000000, 10.000000, 10.000000]], True], [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], [False, [], RigControlVisibility.BASED_ON_SELECTION], [], "None"]) -> None
unreal.RigUnit_HierarchyAddControlTransform.initial_value(value: Transform) -> None
unreal.RigUnit_HierarchyAddControlTransform.settings(value: RigUnit_HierarchyAddControlTransform_Settings) -> None
```

## `unreal.RigUnit_HierarchyAddControlTransform_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.__init__(limit_translation_x: RigControlLimitEnabled = [False, False], limit_translation_y: RigControlLimitEnabled = [False, False], limit_translation_z: RigControlLimitEnabled = [False, False], limit_pitch: RigControlLimitEnabled = [False, False], limit_yaw: RigControlLimitEnabled = [False, False], limit_roll: RigControlLimitEnabled = [False, False], limit_scale_x: RigControlLimitEnabled = [False, False], limit_scale_y: RigControlLimitEnabled = [False, False], limit_scale_z: RigControlLimitEnabled = [False, False], min_value: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], max_value: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_pitch(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_roll(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_y(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_scale_z(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_y(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_translation_z(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.limit_yaw(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.max_value(value: EulerTransform) -> None
unreal.RigUnit_HierarchyAddControlTransform_LimitSettings.min_value(value: EulerTransform) -> None
```

## `unreal.RigUnit_HierarchyAddControlTransform_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlTransform_Settings.__init__(display_name: Name = "None", initial_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, use_preferred_rotation_order: bool = False, preferred_rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ, limits: RigUnit_HierarchyAddControlTransform_LimitSettings = [[False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [False, False], [[-100.000000, -100.000000, -100.000000], [-180.000000, -180.000000, -180.000000], [0.000000, 0.000000, 0.000000]], [[100.000000, 100.000000, 100.000000], [180.000000, 180.000000, 180.000000], [10.000000, 10.000000, 10.000000]], True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION], filtered_channels: Array[RigControlTransformChannel] = []) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.filtered_channels(value: Array[RigControlTransformChannel]) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.initial_space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.limits(value: RigUnit_HierarchyAddControlTransform_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.preferred_rotation_order(value: EulerRotationOrder) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
unreal.RigUnit_HierarchyAddControlTransform_Settings.use_preferred_rotation_order(value: bool) -> None
```

## `unreal.RigUnit_HighlevelBase(RigUnit)`

```python
unreal.RigUnit_HighlevelBase.__init__() -> None
```

## `unreal.RigUnit_HighlevelBaseMutable(RigUnitMutable)`

```python
unreal.RigUnit_HighlevelBaseMutable.__init__(execute_context: ControlRigExecuteContext = []) -> None
```

## `unreal.RigUnit_KalmanTransform(RigVMFunction_KalmanTransform)`

```python
unreal.RigUnit_KalmanTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], buffer_size: int = 0, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathMatrixFromTransform(RigVMFunction_MathMatrixFromTransform)`

```python
unreal.RigUnit_MathMatrixFromTransform.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]]) -> None
```

## `unreal.RigUnit_MathMatrixFromTransformV2(RigVMFunction_MathMatrixFromTransformV2)`

```python
unreal.RigUnit_MathMatrixFromTransformV2.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]]) -> None
```

## `unreal.RigUnit_MathMatrixToTransform(RigVMFunction_MathMatrixToTransform)`

```python
unreal.RigUnit_MathMatrixToTransform.__init__(value: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathQuaternionMirrorTransform(RigVMFunction_MathQuaternionMirrorTransform)`

```python
unreal.RigUnit_MathQuaternionMirrorTransform.__init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

## `unreal.RigUnit_MathTransformAccumulateArray(RigVMFunction_MathTransformAccumulateArray)`

```python
unreal.RigUnit_MathTransformAccumulateArray.__init__(execute_context: RigVMExecuteContext = [], transforms: Array[Transform] = [], target_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, root: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent_indices: Array[int] = []) -> None
```

## `unreal.RigUnit_MathTransformArrayToSRT(RigVMFunction_MathTransformArrayToSRT)`

```python
unreal.RigUnit_MathTransformArrayToSRT.__init__(transforms: Array[Transform] = [], translations: Array[Vector] = [], rotations: Array[Quat] = [], scales: Array[Vector] = []) -> None
```

## `unreal.RigUnit_MathTransformBase(RigVMFunction_MathTransformBase)`

```python
unreal.RigUnit_MathTransformBase.__init__() -> None
```

## `unreal.RigUnit_MathTransformBinaryAggregateOp(RigVMFunction_MathTransformBinaryAggregateOp)`

```python
unreal.RigUnit_MathTransformBinaryAggregateOp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformBinaryOp(RigVMFunction_MathTransformBinaryOp)`

```python
unreal.RigUnit_MathTransformBinaryOp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformClampSpatially(RigVMFunction_MathTransformClampSpatially)`

```python
unreal.RigUnit_MathTransformClampSpatially.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], axis: AxisType = AxisType.NONE, type: RigVMClampSpatialMode = RigVMClampSpatialMode.PLANE, minimum: float = 0.000000, maximum: float = 0.000000, space: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], draw_debug: bool = False, debug_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], debug_thickness: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformFromEulerTransform(RigVMFunction_MathTransformFromEulerTransform)`

```python
unreal.RigUnit_MathTransformFromEulerTransform.__init__(euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformFromEulerTransformV2(RigVMFunction_MathTransformFromEulerTransformV2)`

```python
unreal.RigUnit_MathTransformFromEulerTransformV2.__init__(value: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformFromSRT(RigVMFunction_MathTransformFromSRT)`

```python
unreal.RigUnit_MathTransformFromSRT.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Vector = [0.000000, 0.000000, 0.000000], rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ, scale: Vector = [0.000000, 0.000000, 0.000000], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformInverse(RigVMFunction_MathTransformInverse)`

```python
unreal.RigUnit_MathTransformInverse.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformLerp(RigVMFunction_MathTransformLerp)`

```python
unreal.RigUnit_MathTransformLerp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], t: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMake(RigVMFunction_MathTransformMake)`

```python
unreal.RigUnit_MathTransformMake.__init__(translation: Vector = [0.000000, 0.000000, 0.000000], rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], scale: Vector = [0.000000, 0.000000, 0.000000], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMakeAbsolute(RigVMFunction_MathTransformMakeAbsolute)`

```python
unreal.RigUnit_MathTransformMakeAbsolute.__init__(local: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], global_: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMakeRelative(RigVMFunction_MathTransformMakeRelative)`

```python
unreal.RigUnit_MathTransformMakeRelative.__init__(global_: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], local: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMirrorTransform(RigVMFunction_MathTransformMirrorTransform)`

```python
unreal.RigUnit_MathTransformMirrorTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMul(RigVMFunction_MathTransformMul)`

```python
unreal.RigUnit_MathTransformMul.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformMutableBase(RigVMFunction_MathTransformMutableBase)`

```python
unreal.RigUnit_MathTransformMutableBase.__init__(execute_context: RigVMExecuteContext = []) -> None
```

## `unreal.RigUnit_MathTransformRotateVector(RigVMFunction_MathTransformRotateVector)`

```python
unreal.RigUnit_MathTransformRotateVector.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], vector: Vector = [0.000000, 0.000000, 0.000000], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

## `unreal.RigUnit_MathTransformSelectBool(RigVMFunction_MathTransformSelectBool)`

```python
unreal.RigUnit_MathTransformSelectBool.__init__(condition: bool = False, if_true: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], if_false: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformToEulerTransform(RigVMFunction_MathTransformToEulerTransform)`

```python
unreal.RigUnit_MathTransformToEulerTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathTransformTransformVector(RigVMFunction_MathTransformTransformVector)`

```python
unreal.RigUnit_MathTransformTransformVector.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], location: Vector = [0.000000, 0.000000, 0.000000], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

## `unreal.RigUnit_MathTransformUnaryOp(RigVMFunction_MathTransformUnaryOp)`

```python
unreal.RigUnit_MathTransformUnaryOp.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_MathVectorMirrorTransform(RigVMFunction_MathVectorMirrorTransform)`

```python
unreal.RigUnit_MathVectorMirrorTransform.__init__(value: Vector = [0.000000, 0.000000, 0.000000], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

## `unreal.RigUnit_ModifyBoneTransforms(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_ModifyBoneTransforms.__init__(execute_context: ControlRigExecuteContext = [], bone_to_modify: Array[RigUnit_ModifyBoneTransforms_PerBone] = [], weight: float = 0.000000, weight_minimum: float = 0.000000, weight_maximum: float = 0.000000, mode: ControlRigModifyBoneMode = ControlRigModifyBoneMode.OVERRIDE_LOCAL) -> None
unreal.RigUnit_ModifyBoneTransforms.bone_to_modify(value: Array[RigUnit_ModifyBoneTransforms_PerBone]) -> None
unreal.RigUnit_ModifyBoneTransforms.mode() -> ControlRigModifyBoneMode
unreal.RigUnit_ModifyBoneTransforms.weight(value: float) -> None
unreal.RigUnit_ModifyBoneTransforms.weight_maximum() -> float
unreal.RigUnit_ModifyBoneTransforms.weight_minimum() -> float
```

## `unreal.RigUnit_ModifyBoneTransforms_PerBone(StructBase)`

```python
unreal.RigUnit_ModifyBoneTransforms_PerBone.__init__(bone: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ModifyBoneTransforms_PerBone.bone(value: Name) -> None
unreal.RigUnit_ModifyBoneTransforms_PerBone.transform(value: Transform) -> None
```

## `unreal.RigUnit_ModifyTransforms(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_ModifyTransforms.__init__(execute_context: ControlRigExecuteContext = [], item_to_modify: Array[RigUnit_ModifyTransforms_PerItem] = [], weight: float = 0.000000, weight_minimum: float = 0.000000, weight_maximum: float = 0.000000, mode: ControlRigModifyBoneMode = ControlRigModifyBoneMode.OVERRIDE_LOCAL) -> None
unreal.RigUnit_ModifyTransforms.item_to_modify(value: Array[RigUnit_ModifyTransforms_PerItem]) -> None
unreal.RigUnit_ModifyTransforms.mode() -> ControlRigModifyBoneMode
unreal.RigUnit_ModifyTransforms.weight(value: float) -> None
unreal.RigUnit_ModifyTransforms.weight_maximum() -> float
unreal.RigUnit_ModifyTransforms.weight_minimum() -> float
```

## `unreal.RigUnit_ModifyTransforms_PerItem(StructBase)`

```python
unreal.RigUnit_ModifyTransforms_PerItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ModifyTransforms_PerItem.item(value: RigElementKey) -> None
unreal.RigUnit_ModifyTransforms_PerItem.transform(value: Transform) -> None
```

## `unreal.RigUnit_MultiplyTransform(RigUnit_BinaryTransformOp)`

```python
unreal.RigUnit_MultiplyTransform.__init__(argument0: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], argument1: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_OffsetTransformForItem(RigUnitMutable)`

```python
unreal.RigUnit_OffsetTransformForItem.__init__(execute_context: ControlRigExecuteContext = [], item: RigElementKey = [RigElementType.NONE, "None"], offset_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_OffsetTransformForItem.item(value: RigElementKey) -> None
unreal.RigUnit_OffsetTransformForItem.offset_transform(value: Transform) -> None
unreal.RigUnit_OffsetTransformForItem.propagate_to_children(value: bool) -> None
unreal.RigUnit_OffsetTransformForItem.weight(value: float) -> None
```

## `unreal.RigUnit_PoseGetTransform(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetTransform.__init__(pose: RigPose = [], item: RigElementKey = [RigElementType.NONE, "None"], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, valid: bool = False, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], curve_value: float = 0.000000) -> None
unreal.RigUnit_PoseGetTransform.curve_value() -> float
unreal.RigUnit_PoseGetTransform.item(value: RigElementKey) -> None
unreal.RigUnit_PoseGetTransform.pose(value: RigPose) -> None
unreal.RigUnit_PoseGetTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_PoseGetTransform.transform() -> Transform
unreal.RigUnit_PoseGetTransform.valid() -> bool
```

## `unreal.RigUnit_PoseGetTransformArray(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetTransformArray.__init__(pose: RigPose = [], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, valid: bool = False, transforms: Array[Transform] = []) -> None
unreal.RigUnit_PoseGetTransformArray.pose(value: RigPose) -> None
unreal.RigUnit_PoseGetTransformArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_PoseGetTransformArray.transforms() -> Array[Transform]
unreal.RigUnit_PoseGetTransformArray.valid() -> bool
```

## `unreal.RigUnit_ProjectTransformToNewParent(RigUnit)`

```python
unreal.RigUnit_ProjectTransformToNewParent.__init__(child: RigElementKey = [RigElementType.NONE, "None"], child_initial: bool = False, old_parent: RigElementKey = [RigElementType.NONE, "None"], old_parent_initial: bool = False, new_parent: RigElementKey = [RigElementType.NONE, "None"], new_parent_initial: bool = False, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ProjectTransformToNewParent.child(value: RigElementKey) -> None
unreal.RigUnit_ProjectTransformToNewParent.child_initial(value: bool) -> None
unreal.RigUnit_ProjectTransformToNewParent.new_parent(value: RigElementKey) -> None
unreal.RigUnit_ProjectTransformToNewParent.new_parent_initial(value: bool) -> None
unreal.RigUnit_ProjectTransformToNewParent.old_parent(value: RigElementKey) -> None
unreal.RigUnit_ProjectTransformToNewParent.old_parent_initial(value: bool) -> None
unreal.RigUnit_ProjectTransformToNewParent.transform() -> Transform
```

## `unreal.RigUnit_PropagateTransform(RigUnitMutable)`

```python
unreal.RigUnit_PropagateTransform.__init__(execute_context: ControlRigExecuteContext = [], item: RigElementKey = [RigElementType.NONE, "None"], recompute_global: bool = False, apply_to_children: bool = False, recursive: bool = False) -> None
unreal.RigUnit_PropagateTransform.apply_to_children(value: bool) -> None
unreal.RigUnit_PropagateTransform.item(value: RigElementKey) -> None
unreal.RigUnit_PropagateTransform.recompute_global(value: bool) -> None
unreal.RigUnit_PropagateTransform.recursive(value: bool) -> None
```

## `unreal.RigUnit_SetBoneInitialTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetBoneInitialTransform.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetBoneInitialTransform.bone(value: Name) -> None
unreal.RigUnit_SetBoneInitialTransform.propagate_to_children() -> bool
unreal.RigUnit_SetBoneInitialTransform.result() -> Transform
unreal.RigUnit_SetBoneInitialTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetBoneInitialTransform.transform(value: Transform) -> None
```

## `unreal.RigUnit_SetBoneTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetBoneTransform.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetBoneTransform.bone(value: Name) -> None
unreal.RigUnit_SetBoneTransform.propagate_to_children() -> bool
unreal.RigUnit_SetBoneTransform.result() -> Transform
unreal.RigUnit_SetBoneTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetBoneTransform.transform(value: Transform) -> None
unreal.RigUnit_SetBoneTransform.weight(value: float) -> None
```

## `unreal.RigUnit_SetControlTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetControlTransform.__init__(execute_context: ControlRigExecuteContext = [], control: Name = "None", weight: float = 0.000000, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
unreal.RigUnit_SetControlTransform.control(value: Name) -> None
unreal.RigUnit_SetControlTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetControlTransform.transform(value: Transform) -> None
unreal.RigUnit_SetControlTransform.weight(value: float) -> None
```

## `unreal.RigUnit_SetRelativeBoneTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetRelativeBoneTransform.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", space: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetRelativeBoneTransform.bone(value: Name) -> None
unreal.RigUnit_SetRelativeBoneTransform.propagate_to_children() -> bool
unreal.RigUnit_SetRelativeBoneTransform.space(value: Name) -> None
unreal.RigUnit_SetRelativeBoneTransform.transform(value: Transform) -> None
unreal.RigUnit_SetRelativeBoneTransform.weight(value: float) -> None
```

## `unreal.RigUnit_SetRelativeTransformForItem(RigUnitMutable)`

```python
unreal.RigUnit_SetRelativeTransformForItem.__init__(execute_context: ControlRigExecuteContext = [], child: RigElementKey = [RigElementType.NONE, "None"], parent: RigElementKey = [RigElementType.NONE, "None"], parent_initial: bool = False, value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetRelativeTransformForItem.child(value: RigElementKey) -> None
unreal.RigUnit_SetRelativeTransformForItem.parent(value: RigElementKey) -> None
unreal.RigUnit_SetRelativeTransformForItem.parent_initial(value: bool) -> None
unreal.RigUnit_SetRelativeTransformForItem.propagate_to_children(value: bool) -> None
unreal.RigUnit_SetRelativeTransformForItem.relative_transform(value: Transform) -> None
unreal.RigUnit_SetRelativeTransformForItem.value(value: Transform) -> None
unreal.RigUnit_SetRelativeTransformForItem.weight(value: float) -> None
```

## `unreal.RigUnit_SetShapeTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetShapeTransform.__init__(execute_context: ControlRigExecuteContext = [], control: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_SetShapeTransform.control(value: Name) -> None
unreal.RigUnit_SetShapeTransform.transform(value: Transform) -> None
```

## `unreal.RigUnit_SetSpaceInitialTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetSpaceInitialTransform.__init__(execute_context: ControlRigExecuteContext = [], space_name: Name = "None", transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
unreal.RigUnit_SetSpaceInitialTransform.result() -> Transform
unreal.RigUnit_SetSpaceInitialTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetSpaceInitialTransform.space_name(value: Name) -> None
unreal.RigUnit_SetSpaceInitialTransform.transform(value: Transform) -> None
```

## `unreal.RigUnit_SetSpaceTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetSpaceTransform.__init__(execute_context: ControlRigExecuteContext = [], space: Name = "None", weight: float = 0.000000, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space_type: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
unreal.RigUnit_SetSpaceTransform.space(value: Name) -> None
unreal.RigUnit_SetSpaceTransform.space_type(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetSpaceTransform.transform(value: Transform) -> None
unreal.RigUnit_SetSpaceTransform.weight(value: float) -> None
```

## `unreal.RigUnit_SetSplineTransforms(RigUnitMutable)`

```python
unreal.RigUnit_SetSplineTransforms.__init__(execute_context: ControlRigExecuteContext = [], transforms: Array[Transform] = [], spline: ControlRigSpline = []) -> None
unreal.RigUnit_SetSplineTransforms.spline(value: ControlRigSpline) -> None
unreal.RigUnit_SetSplineTransforms.transforms(value: Array[Transform]) -> None
```

## `unreal.RigUnit_SetTransform(RigUnitMutable)`

```python
unreal.RigUnit_SetTransform.__init__(execute_context: ControlRigExecuteContext = [], item: RigElementKey = [RigElementType.NONE, "None"], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetTransform.initial(value: bool) -> None
unreal.RigUnit_SetTransform.item(value: RigElementKey) -> None
unreal.RigUnit_SetTransform.propagate_to_children(value: bool) -> None
unreal.RigUnit_SetTransform.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetTransform.transform(value: Transform) -> None
unreal.RigUnit_SetTransform.value(value: Transform) -> None
unreal.RigUnit_SetTransform.weight(value: float) -> None
```

## `unreal.RigUnit_SetTransformAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetTransformAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_SetTransformAnimationChannel.value(value: Transform) -> None
```

## `unreal.RigUnit_SetTransformAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetTransformAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_SetTransformAnimationChannelFromItem.value(value: Transform) -> None
```

## `unreal.RigUnit_SetTransformArray(RigUnitMutable)`

```python
unreal.RigUnit_SetTransformArray.__init__(execute_context: ControlRigExecuteContext = [], items: RigElementKeyCollection = [[]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, transforms: Array[Transform] = [], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetTransformArray.initial(value: bool) -> None
unreal.RigUnit_SetTransformArray.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_SetTransformArray.propagate_to_children(value: bool) -> None
unreal.RigUnit_SetTransformArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetTransformArray.transforms(value: Array[Transform]) -> None
unreal.RigUnit_SetTransformArray.weight(value: float) -> None
```

## `unreal.RigUnit_SetTransformItemArray(RigUnitMutable)`

```python
unreal.RigUnit_SetTransformItemArray.__init__(execute_context: ControlRigExecuteContext = [], items: Array[RigElementKey] = [], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, initial: bool = False, transforms: Array[Transform] = [], weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetTransformItemArray.initial(value: bool) -> None
unreal.RigUnit_SetTransformItemArray.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_SetTransformItemArray.propagate_to_children(value: bool) -> None
unreal.RigUnit_SetTransformItemArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetTransformItemArray.transforms(value: Array[Transform]) -> None
unreal.RigUnit_SetTransformItemArray.weight(value: float) -> None
```

## `unreal.RigUnit_SphereTraceWorld(RigUnit)`

```python
unreal.RigUnit_SphereTraceWorld.__init__(start: Vector = [0.000000, 0.000000, 0.000000], end: Vector = [0.000000, 0.000000, 0.000000], channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, radius: float = 0.000000, hit: bool = False, hit_location: Vector = [0.000000, 0.000000, 0.000000], hit_normal: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_SphereTraceWorld.channel(value: CollisionChannel) -> None
unreal.RigUnit_SphereTraceWorld.end(value: Vector) -> None
unreal.RigUnit_SphereTraceWorld.hit() -> bool
unreal.RigUnit_SphereTraceWorld.hit_location() -> Vector
unreal.RigUnit_SphereTraceWorld.hit_normal() -> Vector
unreal.RigUnit_SphereTraceWorld.radius(value: float) -> None
unreal.RigUnit_SphereTraceWorld.start(value: Vector) -> None
```

## `unreal.RigUnit_TimeOffsetTransform(RigVMFunction_TimeOffsetTransform)`

```python
unreal.RigUnit_TimeOffsetTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], seconds_ago: float = 0.000000, buffer_size: int = 0, time_range: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigUnit_ToRigSpace_Transform(RigUnit)`

```python
unreal.RigUnit_ToRigSpace_Transform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], global_: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ToRigSpace_Transform.global_() -> Transform
unreal.RigUnit_ToRigSpace_Transform.transform(value: Transform) -> None
unreal.RigUnit_ToRigSpace_Transform.value(value: Transform) -> None
```

## `unreal.RigUnit_ToWorldSpace_Location(RigUnit)`

```python
unreal.RigUnit_ToWorldSpace_Location.__init__(value: Vector = [0.000000, 0.000000, 0.000000], world: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_ToWorldSpace_Location.location(value: Vector) -> None
unreal.RigUnit_ToWorldSpace_Location.value(value: Vector) -> None
unreal.RigUnit_ToWorldSpace_Location.world() -> Vector
```

## `unreal.RigUnit_ToWorldSpace_Rotation(RigUnit)`

```python
unreal.RigUnit_ToWorldSpace_Rotation.__init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000], world: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.RigUnit_ToWorldSpace_Rotation.rotation(value: Quat) -> None
unreal.RigUnit_ToWorldSpace_Rotation.value(value: Quat) -> None
unreal.RigUnit_ToWorldSpace_Rotation.world() -> Quat
```

## `unreal.RigUnit_ToWorldSpace_Transform(RigUnit)`

```python
unreal.RigUnit_ToWorldSpace_Transform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], world: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_ToWorldSpace_Transform.transform(value: Transform) -> None
unreal.RigUnit_ToWorldSpace_Transform.value(value: Transform) -> None
unreal.RigUnit_ToWorldSpace_Transform.world() -> Transform
```

## `unreal.RigUnit_TransformConstraint(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TransformConstraint.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", base_transform_space: TransformSpaceMode = TransformSpaceMode.LOCAL_SPACE, base_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], base_bone: Name = "None", targets: Array[ConstraintTarget] = [], use_initial_transforms: bool = False) -> None
unreal.RigUnit_TransformConstraint.base_bone(value: Name) -> None
unreal.RigUnit_TransformConstraint.base_transform(value: Transform) -> None
unreal.RigUnit_TransformConstraint.base_transform_space(value: TransformSpaceMode) -> None
unreal.RigUnit_TransformConstraint.bone(value: Name) -> None
unreal.RigUnit_TransformConstraint.targets(value: Array[ConstraintTarget]) -> None
unreal.RigUnit_TransformConstraint.use_initial_transforms() -> bool
```

## `unreal.RigUnit_TransformConstraintPerItem(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TransformConstraintPerItem.__init__(execute_context: ControlRigExecuteContext = [], item: RigElementKey = [RigElementType.NONE, "None"], base_transform_space: TransformSpaceMode = TransformSpaceMode.LOCAL_SPACE, base_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], base_item: RigElementKey = [RigElementType.NONE, "None"], targets: Array[ConstraintTarget] = [], use_initial_transforms: bool = False) -> None
unreal.RigUnit_TransformConstraintPerItem.base_item(value: RigElementKey) -> None
unreal.RigUnit_TransformConstraintPerItem.base_transform(value: Transform) -> None
unreal.RigUnit_TransformConstraintPerItem.base_transform_space(value: TransformSpaceMode) -> None
unreal.RigUnit_TransformConstraintPerItem.item(value: RigElementKey) -> None
unreal.RigUnit_TransformConstraintPerItem.targets(value: Array[ConstraintTarget]) -> None
unreal.RigUnit_TransformConstraintPerItem.use_initial_transforms() -> bool
```

## `unreal.RigUnit_TransformFromControlRigSpline(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_TransformFromControlRigSpline.__init__(spline: ControlRigSpline = [], up_vector: Vector = [0.000000, 0.000000, 0.000000], roll: float = 0.000000, u: float = 0.000000, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_TransformFromControlRigSpline.roll(value: float) -> None
unreal.RigUnit_TransformFromControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_TransformFromControlRigSpline.transform() -> Transform
unreal.RigUnit_TransformFromControlRigSpline.u(value: float) -> None
unreal.RigUnit_TransformFromControlRigSpline.up_vector(value: Vector) -> None
```

## `unreal.RigUnit_TransformFromControlRigSpline2(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_TransformFromControlRigSpline2.__init__(spline: ControlRigSpline = [], u: float = 0.000000, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_TransformFromControlRigSpline2.primary_axis(value: Vector) -> None
unreal.RigUnit_TransformFromControlRigSpline2.secondary_axis(value: Vector) -> None
unreal.RigUnit_TransformFromControlRigSpline2.spline(value: ControlRigSpline) -> None
unreal.RigUnit_TransformFromControlRigSpline2.transform() -> Transform
unreal.RigUnit_TransformFromControlRigSpline2.u(value: float) -> None
```

## `unreal.RigUnit_TwoBoneIKSimpleTransforms(RigUnit_HighlevelBase)`

```python
unreal.RigUnit_TwoBoneIKSimpleTransforms.__init__(root: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], pole_vector: Vector = [0.000000, 0.000000, 0.000000], effector: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis_weight: float = 0.000000, enable_stretch: bool = False, stretch_start_ratio: float = 0.000000, stretch_maximum_ratio: float = 0.000000, bone_a_length: float = 0.000000, bone_b_length: float = 0.000000, elbow: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_a_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.bone_b_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.effector(value: Transform) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.elbow(value: Transform) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.enable_stretch(value: bool) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.pole_vector(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.primary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.root(value: Transform) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.secondary_axis_weight(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_maximum_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleTransforms.stretch_start_ratio(value: float) -> None
```

## `unreal.RigUnit_VisualDebugTransform(RigUnit_DebugBase)`

```python
unreal.RigUnit_VisualDebugTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False, thickness: float = 0.000000, scale: float = 0.000000, bone_space: Name = "None") -> None
unreal.RigUnit_VisualDebugTransform.bone_space(value: Name) -> None
unreal.RigUnit_VisualDebugTransform.enabled(value: bool) -> None
unreal.RigUnit_VisualDebugTransform.scale(value: float) -> None
unreal.RigUnit_VisualDebugTransform.thickness(value: float) -> None
unreal.RigUnit_VisualDebugTransform.value(value: Transform) -> None
```

## `unreal.RigUnit_VisualDebugTransformItemSpace(RigUnit_DebugBase)`

```python
unreal.RigUnit_VisualDebugTransformItemSpace.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False, thickness: float = 0.000000, scale: float = 0.000000, space: RigElementKey = [RigElementType.NONE, "None"]) -> None
unreal.RigUnit_VisualDebugTransformItemSpace.enabled(value: bool) -> None
unreal.RigUnit_VisualDebugTransformItemSpace.scale(value: float) -> None
unreal.RigUnit_VisualDebugTransformItemSpace.space(value: RigElementKey) -> None
unreal.RigUnit_VisualDebugTransformItemSpace.thickness(value: float) -> None
unreal.RigUnit_VisualDebugTransformItemSpace.value(value: Transform) -> None
```

## `unreal.RigVMFunction_AccumulateTransformLerp(RigVMFunction_AccumulateBase)`

```python
unreal.RigVMFunction_AccumulateTransformLerp.__init__(target_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], initial_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], blend: float = 0.000000, integrate_delta_time: bool = False, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_AccumulateTransformLerp.blend(value: float) -> None
unreal.RigVMFunction_AccumulateTransformLerp.initial_value(value: Transform) -> None
unreal.RigVMFunction_AccumulateTransformLerp.integrate_delta_time(value: bool) -> None
unreal.RigVMFunction_AccumulateTransformLerp.result() -> Transform
unreal.RigVMFunction_AccumulateTransformLerp.target_value(value: Transform) -> None
```

## `unreal.RigVMFunction_AccumulateTransformMul(RigVMFunction_AccumulateBase)`

```python
unreal.RigVMFunction_AccumulateTransformMul.__init__(multiplier: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], initial_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], flip_order: bool = False, integrate_delta_time: bool = False, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_AccumulateTransformMul.flip_order(value: bool) -> None
unreal.RigVMFunction_AccumulateTransformMul.initial_value(value: Transform) -> None
unreal.RigVMFunction_AccumulateTransformMul.integrate_delta_time(value: bool) -> None
unreal.RigVMFunction_AccumulateTransformMul.multiplier(value: Transform) -> None
unreal.RigVMFunction_AccumulateTransformMul.result() -> Transform
```

## `unreal.RigVMFunction_DebugTransformArrayMutableNoSpace(RigVMFunction_DebugBaseMutable)`

```python
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.__init__(execute_context: RigVMExecuteContext = [], transforms: Array[Transform] = [], parent_indices: Array[int] = [], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.color(value: LinearColor) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.enabled(value: bool) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.parent_indices(value: Array[int]) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.scale(value: float) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.thickness(value: float) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.transforms(value: Array[Transform]) -> None
unreal.RigVMFunction_DebugTransformArrayMutableNoSpace.world_offset(value: Transform) -> None
```

## `unreal.RigVMFunction_DebugTransformMutableNoSpace(RigVMFunction_DebugBaseMutable)`

```python
unreal.RigVMFunction_DebugTransformMutableNoSpace.__init__(execute_context: RigVMExecuteContext = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mode: RigUnitDebugTransformMode = RigUnitDebugTransformMode.POINT, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, scale: float = 0.000000, world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.color(value: LinearColor) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.enabled(value: bool) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.mode(value: RigUnitDebugTransformMode) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.scale(value: float) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.thickness(value: float) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.transform(value: Transform) -> None
unreal.RigVMFunction_DebugTransformMutableNoSpace.world_offset(value: Transform) -> None
```

## `unreal.RigVMFunction_DeltaFromPreviousTransform(RigVMFunction_SimBase)`

```python
unreal.RigVMFunction_DeltaFromPreviousTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], delta: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], previous_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_DeltaFromPreviousTransform.delta() -> Transform
unreal.RigVMFunction_DeltaFromPreviousTransform.previous_value() -> Transform
unreal.RigVMFunction_DeltaFromPreviousTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_GetWorldTime(RigVMFunction_AnimBase)`

```python
unreal.RigVMFunction_GetWorldTime.__init__(year: float = 0.000000, month: float = 0.000000, day: float = 0.000000, week_day: float = 0.000000, hours: float = 0.000000, minutes: float = 0.000000, seconds: float = 0.000000, overall_seconds: float = 0.000000) -> None
unreal.RigVMFunction_GetWorldTime.day() -> float
unreal.RigVMFunction_GetWorldTime.hours() -> float
unreal.RigVMFunction_GetWorldTime.minutes() -> float
unreal.RigVMFunction_GetWorldTime.month() -> float
unreal.RigVMFunction_GetWorldTime.overall_seconds() -> float
unreal.RigVMFunction_GetWorldTime.seconds() -> float
unreal.RigVMFunction_GetWorldTime.week_day() -> float
unreal.RigVMFunction_GetWorldTime.year() -> float
```

## `unreal.RigVMFunction_KalmanTransform(RigVMFunction_SimBase)`

```python
unreal.RigVMFunction_KalmanTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], buffer_size: int = 0, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_KalmanTransform.buffer_size() -> int
unreal.RigVMFunction_KalmanTransform.result() -> Transform
unreal.RigVMFunction_KalmanTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathBoxTransform(RigVMFunction_MathBoxBase)`

```python
unreal.RigVMFunction_MathBoxTransform.__init__(box: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False]) -> None
unreal.RigVMFunction_MathBoxTransform.box(value: Box) -> None
unreal.RigVMFunction_MathBoxTransform.result() -> Box
unreal.RigVMFunction_MathBoxTransform.transform(value: Transform) -> None
```

## `unreal.RigVMFunction_MathMatrixFromTransform(RigVMFunction_MathMatrixBase)`

```python
unreal.RigVMFunction_MathMatrixFromTransform.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]]) -> None
unreal.RigVMFunction_MathMatrixFromTransform.result() -> Matrix
unreal.RigVMFunction_MathMatrixFromTransform.transform(value: Transform) -> None
```

## `unreal.RigVMFunction_MathMatrixFromTransformV2(RigVMFunction_MathMatrixBase)`

```python
unreal.RigVMFunction_MathMatrixFromTransformV2.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]]) -> None
unreal.RigVMFunction_MathMatrixFromTransformV2.result() -> Matrix
unreal.RigVMFunction_MathMatrixFromTransformV2.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathMatrixToTransform(RigVMFunction_MathMatrixBase)`

```python
unreal.RigVMFunction_MathMatrixToTransform.__init__(value: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathMatrixToTransform.result() -> Transform
unreal.RigVMFunction_MathMatrixToTransform.value(value: Matrix) -> None
```

## `unreal.RigVMFunction_MathQuaternionMirrorTransform(RigVMFunction_MathQuaternionBase)`

```python
unreal.RigVMFunction_MathQuaternionMirrorTransform.__init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.RigVMFunction_MathQuaternionMirrorTransform.axis_to_flip(value: AxisType) -> None
unreal.RigVMFunction_MathQuaternionMirrorTransform.central_transform(value: Transform) -> None
unreal.RigVMFunction_MathQuaternionMirrorTransform.mirror_axis(value: AxisType) -> None
unreal.RigVMFunction_MathQuaternionMirrorTransform.result() -> Quat
unreal.RigVMFunction_MathQuaternionMirrorTransform.value(value: Quat) -> None
```

## `unreal.RigVMFunction_MathRayTransform(RigVMFunction_MathRayBase)`

```python
unreal.RigVMFunction_MathRayTransform.__init__(ray: Ray = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Ray = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]]) -> None
unreal.RigVMFunction_MathRayTransform.ray(value: Ray) -> None
unreal.RigVMFunction_MathRayTransform.result() -> Ray
unreal.RigVMFunction_MathRayTransform.transform(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformAccumulateArray(RigVMFunction_MathTransformMutableBase)`

```python
unreal.RigVMFunction_MathTransformAccumulateArray.__init__(execute_context: RigVMExecuteContext = [], transforms: Array[Transform] = [], target_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, root: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent_indices: Array[int] = []) -> None
unreal.RigVMFunction_MathTransformAccumulateArray.parent_indices(value: Array[int]) -> None
unreal.RigVMFunction_MathTransformAccumulateArray.root(value: Transform) -> None
unreal.RigVMFunction_MathTransformAccumulateArray.target_space(value: RigVMTransformSpace) -> None
unreal.RigVMFunction_MathTransformAccumulateArray.transforms(value: Array[Transform]) -> None
```

## `unreal.RigVMFunction_MathTransformArrayToSRT(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformArrayToSRT.__init__(transforms: Array[Transform] = [], translations: Array[Vector] = [], rotations: Array[Quat] = [], scales: Array[Vector] = []) -> None
unreal.RigVMFunction_MathTransformArrayToSRT.rotations() -> Array[Quat]
unreal.RigVMFunction_MathTransformArrayToSRT.scales() -> Array[Vector]
unreal.RigVMFunction_MathTransformArrayToSRT.transforms(value: Array[Transform]) -> None
unreal.RigVMFunction_MathTransformArrayToSRT.translations() -> Array[Vector]
```

## `unreal.RigVMFunction_MathTransformBase(RigVMFunction_MathBase)`

```python
unreal.RigVMFunction_MathTransformBase.__init__() -> None
```

## `unreal.RigVMFunction_MathTransformBinaryAggregateOp(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformBinaryAggregateOp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformBinaryAggregateOp.a(value: Transform) -> None
unreal.RigVMFunction_MathTransformBinaryAggregateOp.b(value: Transform) -> None
unreal.RigVMFunction_MathTransformBinaryAggregateOp.result() -> Transform
```

## `unreal.RigVMFunction_MathTransformBinaryOp(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformBinaryOp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformBinaryOp.a(value: Transform) -> None
unreal.RigVMFunction_MathTransformBinaryOp.b(value: Transform) -> None
unreal.RigVMFunction_MathTransformBinaryOp.result() -> Transform
```

## `unreal.RigVMFunction_MathTransformClampSpatially(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformClampSpatially.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], axis: AxisType = AxisType.NONE, type: RigVMClampSpatialMode = RigVMClampSpatialMode.PLANE, minimum: float = 0.000000, maximum: float = 0.000000, space: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], draw_debug: bool = False, debug_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], debug_thickness: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformClampSpatially.axis(value: AxisType) -> None
unreal.RigVMFunction_MathTransformClampSpatially.debug_color(value: LinearColor) -> None
unreal.RigVMFunction_MathTransformClampSpatially.debug_thickness(value: float) -> None
unreal.RigVMFunction_MathTransformClampSpatially.draw_debug(value: bool) -> None
unreal.RigVMFunction_MathTransformClampSpatially.maximum(value: float) -> None
unreal.RigVMFunction_MathTransformClampSpatially.minimum(value: float) -> None
unreal.RigVMFunction_MathTransformClampSpatially.result() -> Transform
unreal.RigVMFunction_MathTransformClampSpatially.space(value: Transform) -> None
unreal.RigVMFunction_MathTransformClampSpatially.type(value: RigVMClampSpatialMode) -> None
unreal.RigVMFunction_MathTransformClampSpatially.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformFromEulerTransform(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformFromEulerTransform.__init__(euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformFromEulerTransform.euler_transform(value: EulerTransform) -> None
unreal.RigVMFunction_MathTransformFromEulerTransform.result() -> Transform
```

## `unreal.RigVMFunction_MathTransformFromEulerTransformV2(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformFromEulerTransformV2.__init__(value: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformFromEulerTransformV2.result() -> Transform
unreal.RigVMFunction_MathTransformFromEulerTransformV2.value(value: EulerTransform) -> None
```

## `unreal.RigVMFunction_MathTransformFromSRT(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformFromSRT.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Vector = [0.000000, 0.000000, 0.000000], rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ, scale: Vector = [0.000000, 0.000000, 0.000000], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], euler_transform: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformFromSRT.euler_transform() -> EulerTransform
unreal.RigVMFunction_MathTransformFromSRT.location(value: Vector) -> None
unreal.RigVMFunction_MathTransformFromSRT.rotation(value: Vector) -> None
unreal.RigVMFunction_MathTransformFromSRT.rotation_order(value: EulerRotationOrder) -> None
unreal.RigVMFunction_MathTransformFromSRT.scale(value: Vector) -> None
unreal.RigVMFunction_MathTransformFromSRT.transform() -> Transform
```

## `unreal.RigVMFunction_MathTransformInverse(RigVMFunction_MathTransformUnaryOp)`

```python
unreal.RigVMFunction_MathTransformInverse.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigVMFunction_MathTransformLerp(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformLerp.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], t: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformLerp.a(value: Transform) -> None
unreal.RigVMFunction_MathTransformLerp.b(value: Transform) -> None
unreal.RigVMFunction_MathTransformLerp.result() -> Transform
unreal.RigVMFunction_MathTransformLerp.t(value: float) -> None
```

## `unreal.RigVMFunction_MathTransformMake(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformMake.__init__(translation: Vector = [0.000000, 0.000000, 0.000000], rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], scale: Vector = [0.000000, 0.000000, 0.000000], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformMake.result() -> Transform
unreal.RigVMFunction_MathTransformMake.rotation(value: Quat) -> None
unreal.RigVMFunction_MathTransformMake.scale(value: Vector) -> None
unreal.RigVMFunction_MathTransformMake.translation(value: Vector) -> None
```

## `unreal.RigVMFunction_MathTransformMakeAbsolute(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformMakeAbsolute.__init__(local: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], global_: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformMakeAbsolute.global_() -> Transform
unreal.RigVMFunction_MathTransformMakeAbsolute.local(value: Transform) -> None
unreal.RigVMFunction_MathTransformMakeAbsolute.parent(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformMakeRelative(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformMakeRelative.__init__(global_: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], parent: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], local: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformMakeRelative.global_(value: Transform) -> None
unreal.RigVMFunction_MathTransformMakeRelative.local() -> Transform
unreal.RigVMFunction_MathTransformMakeRelative.parent(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformMirrorTransform(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformMirrorTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformMirrorTransform.axis_to_flip(value: AxisType) -> None
unreal.RigVMFunction_MathTransformMirrorTransform.central_transform(value: Transform) -> None
unreal.RigVMFunction_MathTransformMirrorTransform.mirror_axis(value: AxisType) -> None
unreal.RigVMFunction_MathTransformMirrorTransform.result() -> Transform
unreal.RigVMFunction_MathTransformMirrorTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformMul(RigVMFunction_MathTransformBinaryAggregateOp)`

```python
unreal.RigVMFunction_MathTransformMul.__init__(a: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], b: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.RigVMFunction_MathTransformMutableBase(RigVMFunction_MathMutableBase)`

```python
unreal.RigVMFunction_MathTransformMutableBase.__init__(execute_context: RigVMExecuteContext = []) -> None
```

## `unreal.RigVMFunction_MathTransformRotateVector(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformRotateVector.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], vector: Vector = [0.000000, 0.000000, 0.000000], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigVMFunction_MathTransformRotateVector.direction(value: Vector) -> None
unreal.RigVMFunction_MathTransformRotateVector.result() -> Vector
unreal.RigVMFunction_MathTransformRotateVector.transform(value: Transform) -> None
unreal.RigVMFunction_MathTransformRotateVector.vector(value: Vector) -> None
```

## `unreal.RigVMFunction_MathTransformSelectBool(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformSelectBool.__init__(condition: bool = False, if_true: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], if_false: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformSelectBool.condition(value: bool) -> None
unreal.RigVMFunction_MathTransformSelectBool.if_false(value: Transform) -> None
unreal.RigVMFunction_MathTransformSelectBool.if_true(value: Transform) -> None
unreal.RigVMFunction_MathTransformSelectBool.result() -> Transform
```

## `unreal.RigVMFunction_MathTransformToEulerTransform(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformToEulerTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformToEulerTransform.result() -> EulerTransform
unreal.RigVMFunction_MathTransformToEulerTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformToVectors(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformToVectors.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], forward: Vector = [0.000000, 0.000000, 0.000000], right: Vector = [0.000000, 0.000000, 0.000000], up: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigVMFunction_MathTransformToVectors.forward() -> Vector
unreal.RigVMFunction_MathTransformToVectors.right() -> Vector
unreal.RigVMFunction_MathTransformToVectors.up() -> Vector
unreal.RigVMFunction_MathTransformToVectors.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformTransformVector(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformTransformVector.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], location: Vector = [0.000000, 0.000000, 0.000000], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigVMFunction_MathTransformTransformVector.location(value: Vector) -> None
unreal.RigVMFunction_MathTransformTransformVector.result() -> Vector
unreal.RigVMFunction_MathTransformTransformVector.transform(value: Transform) -> None
```

## `unreal.RigVMFunction_MathTransformUnaryOp(RigVMFunction_MathTransformBase)`

```python
unreal.RigVMFunction_MathTransformUnaryOp.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_MathTransformUnaryOp.result() -> Transform
unreal.RigVMFunction_MathTransformUnaryOp.value(value: Transform) -> None
```

## `unreal.RigVMFunction_MathVectorMirrorTransform(RigVMFunction_MathVectorBase)`

```python
unreal.RigVMFunction_MathVectorMirrorTransform.__init__(value: Vector = [0.000000, 0.000000, 0.000000], mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, central_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigVMFunction_MathVectorMirrorTransform.axis_to_flip(value: AxisType) -> None
unreal.RigVMFunction_MathVectorMirrorTransform.central_transform(value: Transform) -> None
unreal.RigVMFunction_MathVectorMirrorTransform.mirror_axis(value: AxisType) -> None
unreal.RigVMFunction_MathVectorMirrorTransform.result() -> Vector
unreal.RigVMFunction_MathVectorMirrorTransform.value(value: Vector) -> None
```

## `unreal.RigVMFunction_TimeOffsetTransform(RigVMFunction_SimBase)`

```python
unreal.RigVMFunction_TimeOffsetTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], seconds_ago: float = 0.000000, buffer_size: int = 0, time_range: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigVMFunction_TimeOffsetTransform.buffer_size() -> int
unreal.RigVMFunction_TimeOffsetTransform.result() -> Transform
unreal.RigVMFunction_TimeOffsetTransform.seconds_ago(value: float) -> None
unreal.RigVMFunction_TimeOffsetTransform.time_range() -> float
unreal.RigVMFunction_TimeOffsetTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_VisualDebugTransform(RigVMFunction_DebugBase)`

```python
unreal.RigVMFunction_VisualDebugTransform.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False, thickness: float = 0.000000, scale: float = 0.000000, bone_space: Name = "None") -> None
unreal.RigVMFunction_VisualDebugTransform.bone_space(value: Name) -> None
unreal.RigVMFunction_VisualDebugTransform.enabled(value: bool) -> None
unreal.RigVMFunction_VisualDebugTransform.scale(value: float) -> None
unreal.RigVMFunction_VisualDebugTransform.thickness(value: float) -> None
unreal.RigVMFunction_VisualDebugTransform.value(value: Transform) -> None
```

## `unreal.RigVMFunction_VisualDebugTransformNoSpace(RigVMFunction_DebugBase)`

```python
unreal.RigVMFunction_VisualDebugTransformNoSpace.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False, thickness: float = 0.000000, scale: float = 0.000000) -> None
unreal.RigVMFunction_VisualDebugTransformNoSpace.enabled(value: bool) -> None
unreal.RigVMFunction_VisualDebugTransformNoSpace.scale(value: float) -> None
unreal.RigVMFunction_VisualDebugTransformNoSpace.thickness(value: float) -> None
unreal.RigVMFunction_VisualDebugTransformNoSpace.value(value: Transform) -> None
```

## `unreal.RigVMTrait_SetDeformerTransformArrayVariable(RigVMTrait_OptimusVariableBase)`

```python
unreal.RigVMTrait_SetDeformerTransformArrayVariable.__init__() -> None
```

## `unreal.RigVMTrait_SetDeformerTransformVariable(RigVMTrait_OptimusVariableBase)`

```python
unreal.RigVMTrait_SetDeformerTransformVariable.__init__() -> None
```

## `unreal.RunTestCaseActor(Actor)`

```python
unreal.RunTestCaseActor.test_case_folder_absolute_path(value: str) -> None
```

## `unreal.RuntimeCellTransformerInstance(StructBase)`

```python
unreal.RuntimeCellTransformerInstance.__init__() -> None
```

## `unreal.SectionTransformParams(StructBase)`

```python
unreal.SectionTransformParams.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotator: Rotator = [0.000000, 0.000000, 0.000000], scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.SectionTransformParams.location() -> Vector
unreal.SectionTransformParams.rotator() -> Rotator
unreal.SectionTransformParams.scale3d() -> Vector
```

## `unreal.SelectedActorIterator(object)`

```python
unreal.SelectedActorIterator.__init__(world: World, type: Union[Class, type] = ...) -> None
```

## `unreal.SkelMeshMergeMeshUVTransforms(StructBase)`

```python
unreal.SkelMeshMergeMeshUVTransforms.__init__(uv_transforms: Array[Transform] = []) -> None
unreal.SkelMeshMergeMeshUVTransforms.uv_transforms(value: Array[Transform]) -> None
```

## `unreal.SkelMeshMergeUVTransformMapping(StructBase)`

```python
unreal.SkelMeshMergeUVTransformMapping.__init__(uv_transforms_per_mesh: Array[SkelMeshMergeMeshUVTransforms] = []) -> None
unreal.SkelMeshMergeUVTransformMapping.uv_transforms_per_mesh(value: Array[SkelMeshMergeMeshUVTransforms]) -> None
```

## `unreal.SkeletalMeshActor(Actor)`

```python
unreal.SkeletalMeshActor.should_do_anim_notifies(value: bool) -> None
unreal.SkeletalMeshActor.skeletal_mesh_component() -> SkeletalMeshComponent
```

## `unreal.SkeletalMeshEditorSubsystem(EditorSubsystem)`

```python
unreal.SkeletalMeshEditorSubsystem.assign_physics_asset(target_mesh: SkeletalMesh, physics_asset: PhysicsAsset) -> bool
unreal.SkeletalMeshEditorSubsystem.create_physics_asset(skeletal_mesh: SkeletalMesh) -> PhysicsAsset
unreal.SkeletalMeshEditorSubsystem.get_lod_build_settings(skeletal_mesh: SkeletalMesh, lod_index: int) -> SkeletalMeshBuildSettings
unreal.SkeletalMeshEditorSubsystem.get_lod_count(skeletal_mesh: SkeletalMesh) -> int
unreal.SkeletalMeshEditorSubsystem.get_lod_material_slot(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int) -> int
unreal.SkeletalMeshEditorSubsystem.get_num_sections(skeletal_mesh: SkeletalMesh, lod_index: int) -> int
unreal.SkeletalMeshEditorSubsystem.get_num_verts(skeletal_mesh: SkeletalMesh, lod_index: int) -> int
unreal.SkeletalMeshEditorSubsystem.get_section_cast_shadow(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int) -> Optional[bool]
unreal.SkeletalMeshEditorSubsystem.get_section_recompute_tangent(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int) -> Optional[bool]
unreal.SkeletalMeshEditorSubsystem.get_section_recompute_tangents_vertex_mask_channel(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int) -> Optional[int]
unreal.SkeletalMeshEditorSubsystem.get_section_visible_in_ray_tracing(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int) -> Optional[bool]
unreal.SkeletalMeshEditorSubsystem.import_lod(base_mesh: SkeletalMesh, lod_index: int, source_filename: str) -> int
unreal.SkeletalMeshEditorSubsystem.is_physics_asset_compatible(target_mesh: SkeletalMesh, physics_asset: PhysicsAsset) -> bool
unreal.SkeletalMeshEditorSubsystem.regenerate_lod(skeletal_mesh: SkeletalMesh, new_lod_count: int = 0, regenerate_even_if_imported: bool = False, generate_base_lod: bool = False) -> bool
unreal.SkeletalMeshEditorSubsystem.reimport_all_custom_lo_ds(skeletal_mesh: SkeletalMesh) -> bool
unreal.SkeletalMeshEditorSubsystem.rename_socket(skeletal_mesh: SkeletalMesh, old_name: Name, new_name: Name) -> bool
unreal.SkeletalMeshEditorSubsystem.set_lod_build_settings(skeletal_mesh: SkeletalMesh, lod_index: int, build_options: SkeletalMeshBuildSettings) -> None
unreal.SkeletalMeshEditorSubsystem.set_section_cast_shadow(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int, cast_shadow: bool) -> bool
unreal.SkeletalMeshEditorSubsystem.set_section_recompute_tangent(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int, recompute_tangent: bool) -> bool
unreal.SkeletalMeshEditorSubsystem.set_section_recompute_tangents_vertex_mask_channel(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int, recompute_tangents_vertex_mask_channel: int) -> bool
unreal.SkeletalMeshEditorSubsystem.set_section_visible_in_ray_tracing(skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int, visible_in_ray_tracing: bool) -> bool
```

## `unreal.SlateFXSubsystem(EngineSubsystem)`

```python
unreal.SlateFXSubsystem.get_slate_post_processor(post_buffer_bit: SlatePostRT) -> SlateRHIPostBufferProcessor
```

## `unreal.SmartObjectSubsystem(WorldSubsystem)`

```python
unreal.SmartObjectSubsystem.add_tag_to_instance(handle: SmartObjectHandle, tag: GameplayTag) -> None
unreal.SmartObjectSubsystem.add_tag_to_slot(slot_handle: SmartObjectSlotHandle, tag: GameplayTag) -> None
unreal.SmartObjectSubsystem.find_smart_object(request: SmartObjectRequest, user_actor: Actor = None) -> SmartObjectRequestResult
unreal.SmartObjectSubsystem.find_smart_objects(request: SmartObjectRequest, user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectSubsystem.find_smart_objects_bp(request: SmartObjectRequest, user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectSubsystem.get_all_slots(handle: SmartObjectHandle) -> Array[SmartObjectSlotHandle]
unreal.SmartObjectSubsystem.get_behavior_definition(claim_handle: SmartObjectClaimHandle, definition_class: Class) -> SmartObjectBehaviorDefinition
unreal.SmartObjectSubsystem.get_behavior_definition_by_request_result(request_result: SmartObjectRequestResult, definition_class: Class) -> SmartObjectBehaviorDefinition
unreal.SmartObjectSubsystem.get_instance_tags(handle: SmartObjectHandle) -> GameplayTagContainer
unreal.SmartObjectSubsystem.get_slot_location(claim_handle: SmartObjectClaimHandle) -> Optional[Vector]
unreal.SmartObjectSubsystem.get_slot_state(slot_handle: SmartObjectSlotHandle) -> SmartObjectSlotState
unreal.SmartObjectSubsystem.get_slot_tags(slot_handle: SmartObjectSlotHandle) -> GameplayTagContainer
unreal.SmartObjectSubsystem.get_slot_transform(claim_handle: SmartObjectClaimHandle) -> Optional[Transform]
unreal.SmartObjectSubsystem.get_slot_transform_from_request_result(request_result: SmartObjectRequestResult) -> Optional[Transform]
unreal.SmartObjectSubsystem.get_smart_object_component(claim_handle: SmartObjectClaimHandle, try_spawn_actor_if_dehydrated: TrySpawnActorIfDehydrated = TrySpawnActorIfDehydrated.NO) -> SmartObjectComponent
unreal.SmartObjectSubsystem.get_smart_object_component_by_request_result(result: SmartObjectRequestResult, try_spawn_actor_if_dehydrated: TrySpawnActorIfDehydrated = TrySpawnActorIfDehydrated.NO) -> SmartObjectComponent
unreal.SmartObjectSubsystem.is_enabled(handle: SmartObjectHandle) -> bool
unreal.SmartObjectSubsystem.is_enabled_for_reason(handle: SmartObjectHandle, reason_tag: GameplayTag) -> bool
unreal.SmartObjectSubsystem.release(claim_handle: SmartObjectClaimHandle) -> bool
unreal.SmartObjectSubsystem.remove_tag_from_instance(handle: SmartObjectHandle, tag: GameplayTag) -> None
unreal.SmartObjectSubsystem.remove_tag_from_slot(slot_handle: SmartObjectSlotHandle, tag: GameplayTag) -> bool
unreal.SmartObjectSubsystem.set_enabled(handle: SmartObjectHandle, enabled: bool) -> bool
unreal.SmartObjectSubsystem.set_enabled_for_reason(handle: SmartObjectHandle, reason_tag: GameplayTag, enabled: bool) -> bool
unreal.SmartObjectSubsystem.set_slot_enabled(slot_handle: SmartObjectSlotHandle, enabled: bool) -> bool
```

## `unreal.SmartObjectTestingActor(Actor)`

```python
unreal.SmartObjectTestingActor.reset_tests() -> None
unreal.SmartObjectTestingActor.run_tests() -> None
```

## `unreal.SoftWorldReference(StructBase)`

```python
unreal.SoftWorldReference.__init__(world_asset: World = None) -> None
unreal.SoftWorldReference.world_asset(value: World) -> None
```

## `unreal.SpawnActorDelegate(MulticastDelegateBase)`

```python
unreal.SpawnActorDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.SplineMeshActor(Actor)`

```python
unreal.SplineMeshActor.spline_mesh_component() -> SplineMeshComponent
```

## `unreal.StaticMeshActor(Actor)`

```python
unreal.StaticMeshActor.set_mobility(mobility: ComponentMobility) -> None
unreal.StaticMeshActor.static_mesh_component() -> StaticMeshComponent
```

## `unreal.StaticMeshEditorSubsystem(EditorSubsystem)`

```python
unreal.StaticMeshEditorSubsystem.add_simple_collisions(static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType) -> int
unreal.StaticMeshEditorSubsystem.add_simple_collisions_with_notification(static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType, apply_changes: bool) -> int
unreal.StaticMeshEditorSubsystem.add_uv_channel(static_mesh: StaticMesh, lod_index: int) -> bool
unreal.StaticMeshEditorSubsystem.bulk_set_convex_decomposition_collisions(static_meshes: Array[StaticMesh], hull_count: int, max_hull_verts: int, hull_precision: int) -> bool
unreal.StaticMeshEditorSubsystem.bulk_set_convex_decomposition_collisions_with_notification(static_meshes: Array[StaticMesh], hull_count: int, max_hull_verts: int, hull_precision: int, apply_changes: bool) -> bool
unreal.StaticMeshEditorSubsystem.create_proxy_mesh_actor(actors_to_merge: Array[StaticMeshActor], merge_options: CreateProxyMeshActorOptions) -> Optional[StaticMeshActor]
unreal.StaticMeshEditorSubsystem.enable_section_cast_shadow(static_mesh: StaticMesh, cast_shadow: bool, lod_index: int, section_index: int) -> None
unreal.StaticMeshEditorSubsystem.enable_section_collision(static_mesh: StaticMesh, collision_enabled: bool, lod_index: int, section_index: int) -> None
unreal.StaticMeshEditorSubsystem.generate_box_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, size: Vector) -> bool
unreal.StaticMeshEditorSubsystem.generate_cylindrical_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, tiling: Vector2D) -> bool
unreal.StaticMeshEditorSubsystem.generate_planar_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, tiling: Vector2D) -> bool
unreal.StaticMeshEditorSubsystem.get_collision_complexity(static_mesh: StaticMesh) -> CollisionTraceFlag
unreal.StaticMeshEditorSubsystem.get_convex_collision_count(static_mesh: StaticMesh) -> int
unreal.StaticMeshEditorSubsystem.get_lod_build_settings(static_mesh: StaticMesh, lod_index: int) -> MeshBuildSettings
unreal.StaticMeshEditorSubsystem.get_lod_count(static_mesh: StaticMesh) -> int
unreal.StaticMeshEditorSubsystem.get_lod_group(static_mesh: StaticMesh) -> Name
unreal.StaticMeshEditorSubsystem.get_lod_material_slot(static_mesh: StaticMesh, lod_index: int, section_index: int) -> int
unreal.StaticMeshEditorSubsystem.get_lod_reduction_settings(static_mesh: StaticMesh, lod_index: int) -> MeshReductionSettings
unreal.StaticMeshEditorSubsystem.get_lod_screen_sizes(static_mesh: StaticMesh) -> Array[float]
unreal.StaticMeshEditorSubsystem.get_nanite_settings(static_mesh: StaticMesh) -> MeshNaniteSettings
unreal.StaticMeshEditorSubsystem.get_num_uv_channels(static_mesh: StaticMesh, lod_index: int) -> int
unreal.StaticMeshEditorSubsystem.get_number_materials(static_mesh: StaticMesh) -> int
unreal.StaticMeshEditorSubsystem.get_number_verts(static_mesh: StaticMesh, lod_index: int) -> int
unreal.StaticMeshEditorSubsystem.get_simple_collision_count(static_mesh: StaticMesh) -> int
unreal.StaticMeshEditorSubsystem.has_instance_vertex_colors(static_mesh_component: StaticMeshComponent) -> bool
unreal.StaticMeshEditorSubsystem.has_vertex_colors(static_mesh: StaticMesh) -> bool
unreal.StaticMeshEditorSubsystem.import_lod(base_static_mesh: StaticMesh, lod_index: int, source_filename: str) -> int
unreal.StaticMeshEditorSubsystem.insert_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int) -> bool
unreal.StaticMeshEditorSubsystem.is_section_collision_enabled(static_mesh: StaticMesh, lod_index: int, section_index: int) -> bool
unreal.StaticMeshEditorSubsystem.join_static_mesh_actors(actors_to_join: Array[StaticMeshActor], join_options: JoinStaticMeshActorsOptions) -> Actor
unreal.StaticMeshEditorSubsystem.merge_static_mesh_actors(actors_to_merge: Array[StaticMeshActor], merge_options: MergeStaticMeshActorsOptions) -> Optional[StaticMeshActor]
unreal.StaticMeshEditorSubsystem.reimport_all_custom_lo_ds(static_mesh: StaticMesh) -> bool
unreal.StaticMeshEditorSubsystem.remove_collisions(static_mesh: StaticMesh) -> bool
unreal.StaticMeshEditorSubsystem.remove_collisions_with_notification(static_mesh: StaticMesh, apply_changes: bool) -> bool
unreal.StaticMeshEditorSubsystem.remove_lods(static_mesh: StaticMesh) -> bool
unreal.StaticMeshEditorSubsystem.remove_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int) -> bool
unreal.StaticMeshEditorSubsystem.replace_mesh_components_materials(mesh_components: Array[MeshComponent], material_to_be_replaced: MaterialInterface, new_material: MaterialInterface) -> None
unreal.StaticMeshEditorSubsystem.replace_mesh_components_materials_on_actors(actors: Array[Actor], material_to_be_replaced: MaterialInterface, new_material: MaterialInterface) -> None
unreal.StaticMeshEditorSubsystem.replace_mesh_components_meshes(mesh_components: Array[StaticMeshComponent], mesh_to_be_replaced: StaticMesh, new_mesh: StaticMesh) -> None
unreal.StaticMeshEditorSubsystem.replace_mesh_components_meshes_on_actors(actors: Array[Actor], mesh_to_be_replaced: StaticMesh, new_mesh: StaticMesh) -> None
unreal.StaticMeshEditorSubsystem.set_allow_cpu_access(static_mesh: StaticMesh, allow_cpu_access: bool) -> None
unreal.StaticMeshEditorSubsystem.set_convex_decomposition_collisions(static_mesh: StaticMesh, hull_count: int, max_hull_verts: int, hull_precision: int) -> bool
unreal.StaticMeshEditorSubsystem.set_convex_decomposition_collisions_with_notification(static_mesh: StaticMesh, hull_count: int, max_hull_verts: int, hull_precision: int, apply_changes: bool) -> bool
unreal.StaticMeshEditorSubsystem.set_generate_lightmap_uv(static_mesh: StaticMesh, generate_lightmap_u_vs: bool) -> bool
unreal.StaticMeshEditorSubsystem.set_lod_build_settings(static_mesh: StaticMesh, lod_index: int, build_options: MeshBuildSettings) -> None
unreal.StaticMeshEditorSubsystem.set_lod_from_static_mesh(destination_static_mesh: StaticMesh, destination_lod_index: int, source_static_mesh: StaticMesh, source_lod_index: int, reuse_existing_material_slots: bool) -> int
unreal.StaticMeshEditorSubsystem.set_lod_group(static_mesh: StaticMesh, lod_group: Name, rebuild_immediately: bool = True) -> bool
unreal.StaticMeshEditorSubsystem.set_lod_material_slot(static_mesh: StaticMesh, material_slot_index: int, lod_index: int, section_index: int) -> None
unreal.StaticMeshEditorSubsystem.set_lod_reduction_settings(static_mesh: StaticMesh, lod_index: int, reduction_options: MeshReductionSettings) -> None
unreal.StaticMeshEditorSubsystem.set_lod_screen_sizes(static_mesh: StaticMesh, screen_sizes: Array[float]) -> bool
unreal.StaticMeshEditorSubsystem.set_lods(static_mesh: StaticMesh, reduction_options: StaticMeshReductionOptions) -> int
unreal.StaticMeshEditorSubsystem.set_lods_with_notification(static_mesh: StaticMesh, reduction_options: StaticMeshReductionOptions, apply_changes: bool) -> int
unreal.StaticMeshEditorSubsystem.set_nanite_settings(static_mesh: StaticMesh, nanite_settings: MeshNaniteSettings, apply_changes: bool = True) -> None
```

## `unreal.SubobjectDataSubsystem(EngineSubsystem)`

```python
unreal.SubobjectDataSubsystem.add_new_subobject(params: AddNewSubobjectParams) -> Tuple[SubobjectDataHandle, Text]
unreal.SubobjectDataSubsystem.attach_subobject(owner_handle: SubobjectDataHandle, child_to_add_handle: SubobjectDataHandle) -> bool
unreal.SubobjectDataSubsystem.can_copy_subobjects(handles: Array[SubobjectDataHandle]) -> bool
unreal.SubobjectDataSubsystem.can_paste_subobjects(root_handle: SubobjectDataHandle, bp_context: Blueprint = None) -> bool
unreal.SubobjectDataSubsystem.change_subobject_class(handle: SubobjectDataHandle, new_class: Class) -> bool
unreal.SubobjectDataSubsystem.copy_subobjects(handles: Array[SubobjectDataHandle], bp_context: Blueprint) -> None
unreal.SubobjectDataSubsystem.create_new_bp_component(component_class: Class, new_class_path: str, new_class_name: str) -> Class
unreal.SubobjectDataSubsystem.create_new_cpp_component(component_class: Class, new_class_path: str, new_class_name: str) -> Class
unreal.SubobjectDataSubsystem.delete_subobject(context_handle: SubobjectDataHandle, subobject_to_delete: SubobjectDataHandle, bp_context: Blueprint = None) -> int
unreal.SubobjectDataSubsystem.delete_subobjects(context_handle: SubobjectDataHandle, subobjects_to_delete: Array[SubobjectDataHandle], bp_context: Blueprint = None) -> int
unreal.SubobjectDataSubsystem.detach_subobject(owner_handle: SubobjectDataHandle, child_to_remove: SubobjectDataHandle) -> bool
unreal.SubobjectDataSubsystem.duplicate_subobjects(context: SubobjectDataHandle, subobjects_to_dup: Array[SubobjectDataHandle], bp_context: Blueprint) -> Array[SubobjectDataHandle]
unreal.SubobjectDataSubsystem.find_handle_for_object(context: SubobjectDataHandle, object_to_find: Object, bp_context: Blueprint = None) -> SubobjectDataHandle
unreal.SubobjectDataSubsystem.is_valid_rename(handle: SubobjectDataHandle, new_text: Text) -> Optional[Text]
unreal.SubobjectDataSubsystem.k2_delete_subobject_from_instance(context_handle: SubobjectDataHandle, subobject_to_delete: SubobjectDataHandle) -> int
unreal.SubobjectDataSubsystem.k2_delete_subobjects_from_instance(context_handle: SubobjectDataHandle, subobjects_to_delete: Array[SubobjectDataHandle]) -> int
unreal.SubobjectDataSubsystem.k2_find_subobject_data_from_handle(handle: SubobjectDataHandle) -> Optional[SubobjectData]
unreal.SubobjectDataSubsystem.k2_gather_subobject_data_for_blueprint(context: Blueprint) -> Array[SubobjectDataHandle]
unreal.SubobjectDataSubsystem.k2_gather_subobject_data_for_instance(context: Actor) -> Array[SubobjectDataHandle]
unreal.SubobjectDataSubsystem.make_new_scene_root(context: SubobjectDataHandle, new_scene_root: SubobjectDataHandle, bp_context: Blueprint) -> bool
unreal.SubobjectDataSubsystem.paste_subobjects(paste_to_context: SubobjectDataHandle, new_parent_handles: Array[SubobjectDataHandle], bp_context: Blueprint) -> Array[SubobjectDataHandle]
unreal.SubobjectDataSubsystem.rename_subobject(handle: SubobjectDataHandle, new_name: Text) -> bool
unreal.SubobjectDataSubsystem.rename_subobject_member_variable(bp_context: Blueprint, handle: SubobjectDataHandle, new_name: Name) -> None
unreal.SubobjectDataSubsystem.reparent_subobject(params: ReparentSubobjectParams, to_reparent_handle: SubobjectDataHandle) -> bool
unreal.SubobjectDataSubsystem.reparent_subobjects(params: ReparentSubobjectParams, handles_to_move: Array[SubobjectDataHandle]) -> bool
```

## `unreal.SwitchActor(Actor)`

```python
unreal.SwitchActor.get_options() -> Array[Actor]
unreal.SwitchActor.get_selected_option() -> int
unreal.SwitchActor.select_option(option_index: int) -> None
```

## `unreal.SynTransformActor(Actor)`

```python
unreal.SynTransformActor.activate() -> bool
unreal.SynTransformActor.player_index() -> int
unreal.SynTransformActor.set_pawn_collision() -> None
unreal.SynTransformActor.syn_camera_distance() -> bool
unreal.SynTransformActor.syn_location() -> bool
unreal.SynTransformActor.syn_rotator() -> bool
```

## `unreal.TakeRecorderActorSource(TakeRecorderSource)`

```python
unreal.TakeRecorderActorSource.add_source_for_actor(actor: Actor, sources: TakeRecorderSources) -> TakeRecorderSource
unreal.TakeRecorderActorSource.exclude_animation_names(value: Array[str]) -> None
unreal.TakeRecorderActorSource.get_source_actor() -> Actor
unreal.TakeRecorderActorSource.include_animation_names(value: Array[str]) -> None
unreal.TakeRecorderActorSource.record_parent_hierarchy(value: bool) -> None
unreal.TakeRecorderActorSource.record_type(value: TakeRecorderActorRecordType) -> None
unreal.TakeRecorderActorSource.recorded_properties(value: ActorRecorderPropertyMap) -> None
unreal.TakeRecorderActorSource.reduce_keys(value: bool) -> None
unreal.TakeRecorderActorSource.remove_actor_from_sources(actor: Actor, sources: TakeRecorderSources) -> None
unreal.TakeRecorderActorSource.set_source_actor(target: Actor) -> None
unreal.TakeRecorderActorSource.target(value: Actor) -> None
```

## `unreal.TakeRecorderLevelSequenceSource(TakeRecorderSource)`

```python
unreal.TakeRecorderLevelSequenceSource.level_sequences_to_trigger(value: Array[LevelSequence]) -> None
```

## `unreal.TakeRecorderLevelVisibilitySourceSettings(TakeRecorderSource)`

```python
unreal.TakeRecorderLevelVisibilitySourceSettings.level_visibility_track_name(value: Text) -> None
```

## `unreal.TakeRecorderNearbySpawnedActorSource(TakeRecorderSource)`

```python
unreal.TakeRecorderNearbySpawnedActorSource.filter_spawned_actors(value: bool) -> None
unreal.TakeRecorderNearbySpawnedActorSource.filter_types(value: Array[Class]) -> None
unreal.TakeRecorderNearbySpawnedActorSource.proximity(value: float) -> None
```

## `unreal.TakeRecorderSubsystem(EngineSubsystem)`

```python
unreal.TakeRecorderSubsystem.take_recorder_cancelled(value: TakeRecorderCancelled) -> None
unreal.TakeRecorderSubsystem.take_recorder_finished(value: TakeRecorderFinished) -> None
unreal.TakeRecorderSubsystem.take_recorder_marked_frame_added(value: TakeRecorderMarkedFrameAdded) -> None
unreal.TakeRecorderSubsystem.take_recorder_pre_initialize(value: TakeRecorderPreInitialize) -> None
unreal.TakeRecorderSubsystem.take_recorder_started(value: TakeRecorderStarted) -> None
unreal.TakeRecorderSubsystem.take_recorder_stopped(value: TakeRecorderStopped) -> None
```

## `unreal.TakeRecorderWorldSourceSettings(TakeRecorderSource)`

```python
unreal.TakeRecorderWorldSourceSettings.autotrack_actors(value: bool) -> None
unreal.TakeRecorderWorldSourceSettings.record_world_settings(value: bool) -> None
```

## `unreal.TargetingSubsystem(GameInstanceSubsystem)`

```python
unreal.TargetingSubsystem.execute_targeting_request(targeting_preset: TargetingPreset, source_context: TargetingSourceContext, completion_dynamic_delegate: TargetingRequestDynamicDelegate) -> None
unreal.TargetingSubsystem.get_targeting_results(targeting_handle: TargetingRequestHandle) -> Array[HitResult]
unreal.TargetingSubsystem.get_targeting_results_actors(targeting_handle: TargetingRequestHandle) -> Array[Actor]
unreal.TargetingSubsystem.get_targeting_source_context(targeting_handle: TargetingRequestHandle) -> TargetingSourceContext
unreal.TargetingSubsystem.override_collision_query_task_data(targeting_handle: TargetingRequestHandle, collision_query_data_override: CollisionQueryTaskData) -> None
unreal.TargetingSubsystem.remove_async_targeting_request_with_handle(targeting_handle: TargetingRequestHandle) -> TargetingRequestHandle
unreal.TargetingSubsystem.start_async_targeting_request(targeting_preset: TargetingPreset, source_context: TargetingSourceContext, completion_dynamic_delegate: TargetingRequestDynamicDelegate) -> TargetingRequestHandle
```

## `unreal.TemplateSequenceActor(Actor)`

```python
unreal.TemplateSequenceActor.binding_override() -> TemplateSequenceBindingOverrideData
unreal.TemplateSequenceActor.get_sequence() -> TemplateSequence
unreal.TemplateSequenceActor.load_sequence() -> TemplateSequence
unreal.TemplateSequenceActor.playback_settings() -> MovieSceneSequencePlaybackSettings
unreal.TemplateSequenceActor.sequence_player() -> TemplateSequencePlayer
unreal.TemplateSequenceActor.set_binding(actor: Actor, overrides_default: bool = True) -> None
unreal.TemplateSequenceActor.set_sequence(sequence: TemplateSequence) -> None
unreal.TemplateSequenceActor.template_sequence() -> SoftObjectPath
```

## `unreal.Text3DActor(Actor)`

```python
unreal.Text3DActor.text3d_component() -> Text3DComponent
```

## `unreal.Text3DCharacterTransform(SceneComponent)`

```python
unreal.Text3DCharacterTransform.location_distance(value: Vector) -> None
unreal.Text3DCharacterTransform.location_enabled(value: bool) -> None
unreal.Text3DCharacterTransform.location_order(value: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.location_progress(value: float) -> None
unreal.Text3DCharacterTransform.location_range(value: float) -> None
unreal.Text3DCharacterTransform.rotate_begin(value: Rotator) -> None
unreal.Text3DCharacterTransform.rotate_enabled(value: bool) -> None
unreal.Text3DCharacterTransform.rotate_end(value: Rotator) -> None
unreal.Text3DCharacterTransform.rotate_order(value: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.rotate_progress(value: float) -> None
unreal.Text3DCharacterTransform.rotate_range(value: float) -> None
unreal.Text3DCharacterTransform.scale_begin(value: Vector) -> None
unreal.Text3DCharacterTransform.scale_enabled(value: bool) -> None
unreal.Text3DCharacterTransform.scale_end(value: Vector) -> None
unreal.Text3DCharacterTransform.scale_order(value: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.scale_progress(value: float) -> None
unreal.Text3DCharacterTransform.scale_range(value: float) -> None
unreal.Text3DCharacterTransform.set_location_distance(distance: Vector) -> None
unreal.Text3DCharacterTransform.set_location_enabled(enabled: bool) -> None
unreal.Text3DCharacterTransform.set_location_order(order: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.set_location_progress(progress: float) -> None
unreal.Text3DCharacterTransform.set_location_range(range: float) -> None
unreal.Text3DCharacterTransform.set_rotate_begin(value: Rotator) -> None
unreal.Text3DCharacterTransform.set_rotate_enabled(enabled: bool) -> None
unreal.Text3DCharacterTransform.set_rotate_end(value: Rotator) -> None
unreal.Text3DCharacterTransform.set_rotate_order(order: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.set_rotate_progress(progress: float) -> None
unreal.Text3DCharacterTransform.set_rotate_range(range: float) -> None
unreal.Text3DCharacterTransform.set_scale_begin(value: Vector) -> None
unreal.Text3DCharacterTransform.set_scale_enabled(enabled: bool) -> None
unreal.Text3DCharacterTransform.set_scale_end(value: Vector) -> None
unreal.Text3DCharacterTransform.set_scale_order(order: Text3DCharacterEffectOrder) -> None
unreal.Text3DCharacterTransform.set_scale_progress(progress: float) -> None
unreal.Text3DCharacterTransform.set_scale_range(range: float) -> None
```

## `unreal.TextRenderActor(Actor)`

```python
unreal.TextRenderActor.text_render() -> TextRenderComponent
```

## `unreal.TickableTransformConstraint(TickableConstraint)`

```python
unreal.TickableTransformConstraint.child_trs_handle(value: TransformableHandle) -> None
unreal.TickableTransformConstraint.dynamic_offset(value: bool) -> None
unreal.TickableTransformConstraint.maintain_offset(value: bool) -> None
unreal.TickableTransformConstraint.parent_trs_handle(value: TransformableHandle) -> None
```

## `unreal.TopLevelAssetPath(StructBase)`

```python
unreal.TopLevelAssetPath.__init__(package_name: str = "", asset_name: str = "") -> None
unreal.TopLevelAssetPath.asset_name(value: Name) -> None
unreal.TopLevelAssetPath.package_name(value: Name) -> None
```

## `unreal.TrafficSpawnActor(Actor)`

```python
unreal.TrafficSpawnActor.build_zone_graph() -> None
unreal.TrafficSpawnActor.spawn_missing_zone_graph_data() -> None
unreal.TrafficSpawnActor.zone_graph_data(value: ZoneGraphData) -> None
```

## `unreal.Transform(StructBase)`

```python
unreal.Transform.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [1.000000, 1.000000, 1.000000]) -> None
unreal.Transform.determinant() -> float
unreal.Transform.equals(b: Transform) -> bool
unreal.Transform.interp_to(target: Transform, delta_time: float, interp_speed: float) -> Transform
unreal.Transform.inverse() -> Transform
unreal.Transform.inverse_transform_direction(direction: Vector) -> Vector
unreal.Transform.inverse_transform_location(location: Vector) -> Vector
unreal.Transform.inverse_transform_rotation(rotation: Rotator) -> Rotator
unreal.Transform.is_near_equal(b: Transform, location_tolerance: float = 0.000100, rotation_tolerance: float = 0.000100, scale3d_tolerance: float = 0.000100) -> bool
unreal.Transform.lerp(b: Transform, alpha: float, interp_mode: LerpInterpolationMode = LerpInterpolationMode.QUAT_INTERP) -> Transform
unreal.Transform.make_relative(relative_to: Transform) -> Transform
unreal.Transform.multiply(b: Transform) -> Transform
unreal.Transform.rotation(value: Quat) -> None
unreal.Transform.scale3d(value: Vector) -> None
unreal.Transform.to_matrix() -> Matrix
unreal.Transform.transform_direction(direction: Vector) -> Vector
unreal.Transform.transform_location(location: Vector) -> Vector
unreal.Transform.transform_rotation(rotation: Rotator) -> Rotator
unreal.Transform.translation(value: Vector) -> None
```

## `unreal.Transform3d(StructBase)`

```python
unreal.Transform3d.__init__() -> None
```

## `unreal.Transform3f(StructBase)`

```python
unreal.Transform3f.__init__() -> None
```

## `unreal.TransformAnimationAttribute(StructBase)`

```python
unreal.TransformAnimationAttribute.__init__(value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.TransformAnimationAttribute.value(value: Transform) -> None
```

## `unreal.TransformAnimationSettings(StructBase)`

```python
unreal.TransformAnimationSettings.__init__(target_relative_location: Vector = [0.000000, 0.000000, 0.000000], target_relative_rotation: Rotator = [0.000000, 0.000000, 0.000000], ease_out: bool = False, ease_in: bool = False, over_time: float = 0.000000, force_shortest_rotation_path: bool = False) -> None
unreal.TransformAnimationSettings.ease_in(value: bool) -> None
unreal.TransformAnimationSettings.ease_out(value: bool) -> None
unreal.TransformAnimationSettings.force_shortest_rotation_path(value: bool) -> None
unreal.TransformAnimationSettings.over_time(value: float) -> None
unreal.TransformAnimationSettings.target_relative_location(value: Vector) -> None
unreal.TransformAnimationSettings.target_relative_rotation(value: Rotator) -> None
```

## `unreal.TransformAtom(TransformAtomBase)`

```python
unreal.TransformAtom.location() -> Vector
unreal.TransformAtom.pivot_offset() -> Vector
unreal.TransformAtom.rotator() -> Rotator
unreal.TransformAtom.scale3d() -> Vector
```

## `unreal.TransformAtomBase(EntityAtomBase)`

```python
unreal.TransformAtomBase.can_move() -> bool
unreal.TransformAtomBase.can_rotate() -> bool
unreal.TransformAtomBase.can_scale() -> bool
unreal.TransformAtomBase.get_data_transform() -> Transform
unreal.TransformAtomBase.get_location_data() -> Vector
unreal.TransformAtomBase.get_pivot() -> Vector
unreal.TransformAtomBase.get_pivot_offset_data() -> Vector
unreal.TransformAtomBase.get_pivot_transform() -> Transform
unreal.TransformAtomBase.get_rotator_data() -> Rotator
unreal.TransformAtomBase.get_scale3d() -> Vector
unreal.TransformAtomBase.get_view_transform() -> Transform
unreal.TransformAtomBase.set_location(new_location: Vector) -> bool
unreal.TransformAtomBase.set_pivot_offset(offset: Vector) -> bool
unreal.TransformAtomBase.set_rotator(new_rotator: Rotator) -> bool
unreal.TransformAtomBase.set_scale3d(new_scale: Vector) -> bool
unreal.TransformAtomBase.set_view_transform(new_transform: Transform) -> bool
```

## `unreal.TransformConstraint(StructBase)`

```python
unreal.TransformConstraint.__init__(operator: ConstraintDescription = [True, True, False, False, [True, True, True], [True, True, True], [True, True, True]], source_node: Name = "None", target_node: Name = "None", weight: float = 0.000000, maintain_offset: bool = False) -> None
unreal.TransformConstraint.maintain_offset(value: bool) -> None
unreal.TransformConstraint.operator(value: ConstraintDescription) -> None
unreal.TransformConstraint.source_node(value: Name) -> None
unreal.TransformConstraint.target_node(value: Name) -> None
unreal.TransformConstraint.weight(value: float) -> None
```

## `unreal.TransformCurve(AnimCurveBase)`

```python
unreal.TransformCurve.__init__() -> None
```

## `unreal.TransformFilter(StructBase)`

```python
unreal.TransformFilter.__init__(translation_filter: FilterOptionPerAxis = [True, True, True], rotation_filter: FilterOptionPerAxis = [True, True, True], scale_filter: FilterOptionPerAxis = [True, True, True]) -> None
unreal.TransformFilter.rotation_filter(value: FilterOptionPerAxis) -> None
unreal.TransformFilter.scale_filter(value: FilterOptionPerAxis) -> None
unreal.TransformFilter.translation_filter(value: FilterOptionPerAxis) -> None
```

## `unreal.TransformNoScale(StructBase)`

```python
unreal.TransformNoScale.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.TransformNoScale.location(value: Vector) -> None
unreal.TransformNoScale.rotation(value: Quat) -> None
```

## `unreal.TransformableComponentHandle(TransformableHandle)`

```python
unreal.TransformableComponentHandle.component() -> SceneComponent
unreal.TransformableComponentHandle.socket_name() -> Name
```

## `unreal.TransformableControlHandle(TransformableHandle)`

```python
unreal.TransformableControlHandle.control_name() -> Name
unreal.TransformableControlHandle.control_rig() -> ControlRig
```

## `unreal.TransformableHandle(Object)`

```python
unreal.TransformableHandle.constraint_binding_id() -> MovieSceneObjectBindingID
```

## `unreal.TypedElementWorldInterface(Interface)`

```python
unreal.TypedElementWorldInterface.can_delete_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.can_duplicate_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.can_edit_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.can_move_element(element_handle: ScriptTypedElementHandle, world_type: TypedElementWorldType) -> bool
unreal.TypedElementWorldInterface.can_promote_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.can_scale_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.delete_element(element_handle: ScriptTypedElementHandle, world: World, selection_set: TypedElementSelectionSet, deletion_options: TypedElementDeletionOptions) -> bool
unreal.TypedElementWorldInterface.duplicate_element(element_handle: ScriptTypedElementHandle, world: World, location_offset: Vector) -> ScriptTypedElementHandle
unreal.TypedElementWorldInterface.get_bounds(element_handle: ScriptTypedElementHandle) -> Optional[BoxSphereBounds]
unreal.TypedElementWorldInterface.get_owner_level(element_handle: ScriptTypedElementHandle) -> Level
unreal.TypedElementWorldInterface.get_owner_world(element_handle: ScriptTypedElementHandle) -> World
unreal.TypedElementWorldInterface.get_pivot_offset(element_handle: ScriptTypedElementHandle) -> Optional[Vector]
unreal.TypedElementWorldInterface.get_relative_transform(element_handle: ScriptTypedElementHandle) -> Optional[Transform]
unreal.TypedElementWorldInterface.get_world_transform(element_handle: ScriptTypedElementHandle) -> Optional[Transform]
unreal.TypedElementWorldInterface.is_template_element(element_handle: ScriptTypedElementHandle) -> bool
unreal.TypedElementWorldInterface.notify_movement_ended(element_handle: ScriptTypedElementHandle) -> None
unreal.TypedElementWorldInterface.notify_movement_ongoing(element_handle: ScriptTypedElementHandle) -> None
unreal.TypedElementWorldInterface.notify_movement_started(element_handle: ScriptTypedElementHandle) -> None
unreal.TypedElementWorldInterface.promote_element(element_handle: ScriptTypedElementHandle, override_world: World = None) -> ScriptTypedElementHandle
unreal.TypedElementWorldInterface.set_pivot_offset(element_handle: ScriptTypedElementHandle, pivot_offset: Vector) -> bool
unreal.TypedElementWorldInterface.set_relative_transform(element_handle: ScriptTypedElementHandle, transform: Transform) -> bool
unreal.TypedElementWorldInterface.set_world_transform(element_handle: ScriptTypedElementHandle, transform: Transform) -> bool
```

## `unreal.UnrealEditorSubsystem(EditorSubsystem)`

```python
unreal.UnrealEditorSubsystem.get_editor_world() -> World
unreal.UnrealEditorSubsystem.get_game_world() -> World
unreal.UnrealEditorSubsystem.get_level_viewport_camera_info() -> Optional[Tuple[Vector, Rotator]]
unreal.UnrealEditorSubsystem.set_level_viewport_camera_info(camera_location: Vector, camera_rotation: Rotator) -> None
```

## `unreal.UrbanEntityModelerActor(Actor)`

```python
unreal.UrbanEntityModelerActor.build_all_children_modeler_actor() -> None
unreal.UrbanEntityModelerActor.build_modeler_actor() -> None
unreal.UrbanEntityModelerActor.build_reason(value: UrbanEntityModelerDirtyReason) -> None
unreal.UrbanEntityModelerActor.editing_entity(reason: UrbanEntityModelerDirtyReason) -> None
unreal.UrbanEntityModelerActor.entity_infos(value: Array[ModelerEntityInfo]) -> None
unreal.UrbanEntityModelerActor.get_modeler_current_level_name() -> str
unreal.UrbanEntityModelerActor.get_urban_entity() -> UrbanEntity
unreal.UrbanEntityModelerActor.get_urban_entity_asset() -> UrbanEntityAsset
unreal.UrbanEntityModelerActor.get_urban_entity_from_asset() -> UrbanEntity
unreal.UrbanEntityModelerActor.init_property_string() -> None
unreal.UrbanEntityModelerActor.load_property_string() -> None
unreal.UrbanEntityModelerActor.on_build_all_children_modeler_actor() -> None
unreal.UrbanEntityModelerActor.on_build_modeler_actor() -> None
unreal.UrbanEntityModelerActor.on_editing_entity(reason: UrbanEntityModelerDirtyReason) -> None
unreal.UrbanEntityModelerActor.on_reload_urban_scene_node() -> None
unreal.UrbanEntityModelerActor.on_update_variabilization() -> None
unreal.UrbanEntityModelerActor.prefab_asset(value: UrbanEntityPrefab_New) -> None
unreal.UrbanEntityModelerActor.property_string(value: str) -> None
unreal.UrbanEntityModelerActor.receive_entity_info(entity_info: ModelerEntityInfo) -> ModelerEntityInfo
unreal.UrbanEntityModelerActor.reload_urban_scene_node() -> None
unreal.UrbanEntityModelerActor.save_as_prefab() -> None
unreal.UrbanEntityModelerActor.set_property_from_data_table(table: DataTable, index: int, array_name: Name) -> None
unreal.UrbanEntityModelerActor.set_property_string(string: str) -> None
unreal.UrbanEntityModelerActor.set_property_value_by_name(array_name: Name, name: Name, value: str) -> None
unreal.UrbanEntityModelerActor.set_urban_entity(entity: UrbanEntity) -> None
unreal.UrbanEntityModelerActor.spawning(value: bool) -> None
unreal.UrbanEntityModelerActor.sync_actor_transform_to_entity(transform: Transform) -> None
unreal.UrbanEntityModelerActor.update_variabilization() -> None
unreal.UrbanEntityModelerActor.update_variabilization_by_asset(replace_data: bool) -> None
```

## `unreal.UrbanWorld(Actor)`

```python
unreal.UrbanWorld.get_camera_altitude_and_location() -> Tuple[float, Vector, Vector]
unreal.UrbanWorld.get_target_srs() -> str
unreal.UrbanWorld.get_world_location_bp() -> Vector
unreal.UrbanWorld.get_world_rotation_bp() -> Rotator
unreal.UrbanWorld.orbit_camera_component() -> OrbitCameraComponent
```

## `unreal.UrbanWorldBuildLevelConfig(StructBase)`

```python
unreal.UrbanWorldBuildLevelConfig.__init__() -> None
```

## `unreal.UrbanWorldBuildManager(Object)`

```python
unreal.UrbanWorldBuildManager.get_build_system(target_level: int, layer_name: str) -> UrbanBuildSystem
```

## `unreal.UrbanWorldLayerSettings(StructBase)`

```python
unreal.UrbanWorldLayerSettings.__init__() -> None
```

## `unreal.UrbanWorldLocation(StructBase)`

```python
unreal.UrbanWorldLocation.__init__() -> None
```

## `unreal.UrbanWorldProjectionSetting(StructBase)`

```python
unreal.UrbanWorldProjectionSetting.__init__() -> None
```

## `unreal.UrbanWorldResource(StructBase)`

```python
unreal.UrbanWorldResource.__init__() -> None
```

## `unreal.UsdLevelSequenceAssetUserData(AssetUserData)`

```python
unreal.UsdLevelSequenceAssetUserData.handled_binding_guids(value: Set[Guid]) -> None
unreal.UsdLevelSequenceAssetUserData.last_checked_signature(value: Guid) -> None
```

## `unreal.VFPlayerActor(Actor)`

```python
unreal.VFPlayerActor.get_texture() -> Texture2D
unreal.VFPlayerActor.on_load_video_callback(success: bool) -> None
unreal.VFPlayerActor.pause() -> None
unreal.VFPlayerActor.play() -> None
unreal.VFPlayerActor.stop() -> None
unreal.VFPlayerActor.test() -> None
```

## `unreal.VREditorInteractor(ViewportInteractor)`

```python
unreal.VREditorInteractor.get_controller_hand_side() -> Name
unreal.VREditorInteractor.get_controller_side() -> ControllerHand
unreal.VREditorInteractor.get_controller_type() -> ControllerType
unreal.VREditorInteractor.get_hmd_device_type() -> Name
unreal.VREditorInteractor.get_laser_end() -> Vector
unreal.VREditorInteractor.get_laser_start() -> Vector
unreal.VREditorInteractor.get_last_trackpad_position() -> Vector2D
unreal.VREditorInteractor.get_motion_controller_component() -> MotionControllerComponent
unreal.VREditorInteractor.get_select_and_move_trigger_value() -> float
unreal.VREditorInteractor.get_slide_delta() -> float
unreal.VREditorInteractor.get_teleport_actor() -> VREditorTeleporter
unreal.VREditorInteractor.get_trackpad_position() -> Vector2D
unreal.VREditorInteractor.hand_mesh_component(value: StaticMeshComponent) -> None
unreal.VREditorInteractor.init(vr_mode: VREditorMode) -> None
unreal.VREditorInteractor.is_clicking_on_ui() -> bool
unreal.VREditorInteractor.is_hovering_over_ui() -> bool
unreal.VREditorInteractor.is_touching_trackpad() -> bool
unreal.VREditorInteractor.replace_hand_mesh_component(new_mesh: StaticMesh, mesh_scale: Vector = [1.000000, 1.000000, 1.000000]) -> None
unreal.VREditorInteractor.set_controller_hand_side(controller_hand_side: Name) -> None
unreal.VREditorInteractor.set_controller_type(controller_type: ControllerType) -> None
unreal.VREditorInteractor.set_force_laser_color(color: LinearColor) -> None
unreal.VREditorInteractor.set_force_show_laser(force_show: bool) -> None
unreal.VREditorInteractor.setup_component(owning_actor: Actor) -> None
unreal.VREditorInteractor.try_override_controller_type(controller_type: ControllerType) -> bool
unreal.VREditorInteractor.update_hand_mesh_relative_transform() -> None
```

## `unreal.VRScoutingInteractor(VREditorInteractor)`

```python
unreal.VRScoutingInteractor.flying_indicator_component() -> StaticMeshComponent
unreal.VRScoutingInteractor.get_gizmo_mode() -> GizmoHandleTypes
unreal.VRScoutingInteractor.get_input_component() -> InputComponent
unreal.VRScoutingInteractor.get_selected_actors() -> Array[Actor]
unreal.VRScoutingInteractor.receives_editor_input(value: bool) -> None
unreal.VRScoutingInteractor.set_gizmo_mode(gizmo_mode: GizmoHandleTypes) -> None
```

## `unreal.VariantManagerTestActor(Actor)`

```python
unreal.VariantManagerTestActor.captured_bool_property(value: bool) -> None
unreal.VariantManagerTestActor.captured_byte_property(value: int) -> None
unreal.VariantManagerTestActor.captured_color_property(value: Color) -> None
unreal.VariantManagerTestActor.captured_float_property(value: float) -> None
unreal.VariantManagerTestActor.captured_int_point_property(value: IntPoint) -> None
unreal.VariantManagerTestActor.captured_int_property(value: int) -> None
unreal.VariantManagerTestActor.captured_interface_property(value: Interface) -> None
unreal.VariantManagerTestActor.captured_linear_color_property(value: LinearColor) -> None
unreal.VariantManagerTestActor.captured_name_property(value: Name) -> None
unreal.VariantManagerTestActor.captured_object_property(value: Object) -> None
unreal.VariantManagerTestActor.captured_quat_property(value: Quat) -> None
unreal.VariantManagerTestActor.captured_rotator_property(value: Rotator) -> None
unreal.VariantManagerTestActor.captured_str_property(value: str) -> None
unreal.VariantManagerTestActor.captured_text_property(value: Text) -> None
unreal.VariantManagerTestActor.captured_u_object_array_property(value: Array[Object]) -> None
unreal.VariantManagerTestActor.captured_vector2d_property(value: Vector2D) -> None
unreal.VariantManagerTestActor.captured_vector4_property(value: Vector4) -> None
unreal.VariantManagerTestActor.captured_vector_array_property(value: Array[Vector]) -> None
unreal.VariantManagerTestActor.captured_vector_property(value: Vector) -> None
unreal.VariantManagerTestActor.enum_with_no_default(value: VariantManagerTestEnum) -> None
unreal.VariantManagerTestActor.enum_with_second_default(value: VariantManagerTestEnum) -> None
```

## `unreal.ViewportInteractor(Object)`

```python
unreal.ViewportInteractor.can_carry() -> bool
unreal.ViewportInteractor.get_dragging_mode() -> ViewportInteractionDraggingMode
unreal.ViewportInteractor.get_hit_result_gizmo_filter_mode() -> HitResultGizmoFilterMode
unreal.ViewportInteractor.get_hover_location() -> Vector
unreal.ViewportInteractor.get_laser_pointer(even_if_blocked: bool = False, laser_length_override: float = 0.000000) -> Optional[Tuple[Vector, Vector]]
unreal.ViewportInteractor.get_last_room_space_transform() -> Transform
unreal.ViewportInteractor.get_last_transform() -> Transform
unreal.ViewportInteractor.get_other_interactor() -> ViewportInteractor
unreal.ViewportInteractor.get_room_space_transform() -> Transform
unreal.ViewportInteractor.get_transform() -> Transform
unreal.ViewportInteractor.get_transform_and_forward_vector() -> Optional[Tuple[Transform, Vector]]
unreal.ViewportInteractor.get_world_interaction() -> ViewportWorldInteraction
unreal.ViewportInteractor.handle_input_axis_bp(action: ViewportActionKeyInput, key: Key, delta: float, delta_time: float) -> bool
unreal.ViewportInteractor.handle_input_key_bp(action: ViewportActionKeyInput, key: Key, event: InputEventType) -> bool
unreal.ViewportInteractor.is_hovering_over_gizmo() -> bool
unreal.ViewportInteractor.set_can_carry(can_carry: bool) -> None
unreal.ViewportInteractor.set_dragging_mode(new_dragging_mode: ViewportInteractionDraggingMode) -> None
unreal.ViewportInteractor.set_hit_result_gizmo_filter_mode(new_filter: HitResultGizmoFilterMode) -> None
unreal.ViewportInteractor.shutdown() -> None
unreal.ViewportInteractor.tick(delta_time: float) -> None
```

## `unreal.ViewportStatsSubsystem(WorldSubsystem)`

```python
unreal.ViewportStatsSubsystem.add_display_delegate(delegate: ViewportDisplayCallback) -> int
unreal.ViewportStatsSubsystem.add_timed_display(text: Text, color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], duration: float = 0.000000, display_offset: Vector2D = [0.000000, 0.000000]) -> None
unreal.ViewportStatsSubsystem.remove_display_delegate(index_to_remove: int) -> None
```

## `unreal.ViewportWorldInteraction(EditorWorldExtension)`

```python
unreal.ViewportWorldInteraction.add_actor_to_exclude_from_hit_tests(actor_to_exclude_from_hit_tests: Actor) -> None
unreal.ViewportWorldInteraction.add_interactor(interactor: ViewportInteractor) -> None
unreal.ViewportWorldInteraction.get_head_transform() -> Transform
unreal.ViewportWorldInteraction.get_interactors() -> Array[ViewportInteractor]
unreal.ViewportWorldInteraction.get_room_space_head_transform() -> Transform
unreal.ViewportWorldInteraction.get_room_transform() -> Transform
unreal.ViewportWorldInteraction.get_transform_gizmo_actor() -> BaseTransformGizmo
unreal.ViewportWorldInteraction.get_world_scale_factor() -> float
unreal.ViewportWorldInteraction.remove_interactor(interactor: ViewportInteractor) -> None
unreal.ViewportWorldInteraction.set_head_transform(new_head_transform: Transform) -> None
unreal.ViewportWorldInteraction.set_room_transform_for_next_frame(new_room_transform: Transform) -> None
unreal.ViewportWorldInteraction.set_world_to_meters_scale(new_world_to_meters_scale: float, compensate_room_world_scale: bool = False) -> None
```

## `unreal.WDPCameraBaseTransformParams(ParamsBase)`

```python
unreal.WDPCameraBaseTransformParams.__init__(direction: str = "", velocity: float = 0.000000) -> None
unreal.WDPCameraBaseTransformParams.direction(value: str) -> None
unreal.WDPCameraBaseTransformParams.velocity(value: float) -> None
```

## `unreal.WDPCameraMoveTransformParams(WDPCameraBaseTransformParams)`

```python
unreal.WDPCameraMoveTransformParams.__init__(direction: str = "", velocity: float = 0.000000, distance: float = 0.000000) -> None
unreal.WDPCameraMoveTransformParams.distance(value: float) -> None
```

## `unreal.WDPCameraRotateTransformParams(WDPCameraBaseTransformParams)`

```python
unreal.WDPCameraRotateTransformParams.__init__(direction: str = "", velocity: float = 0.000000, angle: float = 0.000000) -> None
unreal.WDPCameraRotateTransformParams.angle(value: float) -> None
```

## `unreal.WaterSubsystem(TickableWorldSubsystem)`

```python
unreal.WaterSubsystem.get_camera_underwater_depth() -> float
unreal.WaterSubsystem.get_ocean_base_height() -> float
unreal.WaterSubsystem.get_ocean_flood_height() -> float
unreal.WaterSubsystem.get_ocean_total_height() -> float
unreal.WaterSubsystem.get_shallow_water_max_dynamic_forces() -> int
unreal.WaterSubsystem.get_shallow_water_max_impulse_forces() -> int
unreal.WaterSubsystem.get_shallow_water_simulation_render_target_size() -> int
unreal.WaterSubsystem.get_smoothed_world_time_seconds() -> float
unreal.WaterSubsystem.get_water_time_seconds() -> float
unreal.WaterSubsystem.is_shallow_water_simulation_enabled() -> bool
unreal.WaterSubsystem.is_underwater_post_process_enabled() -> bool
unreal.WaterSubsystem.is_water_rendering_enabled() -> bool
unreal.WaterSubsystem.on_camera_underwater_state_changed(value: OnCameraUnderwaterStateChanged) -> None
unreal.WaterSubsystem.on_water_scalability_changed(value: OnWaterScalabilityChanged) -> None
unreal.WaterSubsystem.print_to_water_log(message: str, warning: bool) -> None
unreal.WaterSubsystem.set_ocean_flood_height(flood_height: float) -> None
```

## `unreal.WaveTableTransform(StructBase)`

```python
unreal.WaveTableTransform.__init__(curve: WaveTableCurve = WaveTableCurve.LINEAR, scalar: float = 0.000000, curve_shared: CurveFloat = None) -> None
unreal.WaveTableTransform.curve(value: WaveTableCurve) -> None
unreal.WaveTableTransform.curve_shared(value: CurveFloat) -> None
unreal.WaveTableTransform.scalar(value: float) -> None
```

## `unreal.WdpActorEntity(Actor)`

```python
unreal.WdpActorEntity.create_graphics() -> bool
unreal.WdpActorEntity.destroy_graphics() -> bool
unreal.WdpActorEntity.entity_atoms() -> Array[EntityAtomBase]
unreal.WdpActorEntity.entity_init(entity_init_params: EntityInitParams) -> bool
unreal.WdpActorEntity.get_all_entity_atoms() -> Array[EntityAtomBase]
unreal.WdpActorEntity.get_bounding_box() -> Box
unreal.WdpActorEntity.get_entity_atom_by_class(atom_class: Class) -> EntityAtomBase
unreal.WdpActorEntity.get_entity_atoms_class() -> Set[Class]
unreal.WdpActorEntity.get_entity_category() -> WdpCategory
unreal.WdpActorEntity.get_entity_class() -> Class
unreal.WdpActorEntity.get_entity_define_flags() -> EntityDefineFlags
unreal.WdpActorEntity.get_entity_id() -> int
unreal.WdpActorEntity.get_entity_instance_flags() -> EntityInstanceFlags
unreal.WdpActorEntity.get_entity_type() -> Name
unreal.WdpActorEntity.handle_entity_operations(operations: WdpJsonObjectWrapper, operate_entity_time: OperateEntityTime) -> bool
unreal.WdpActorEntity.notify2d_entity_mouse_event(mouse_pos: Vector2D, event_type: E2DEntityMouseEventType, button_type: E2DEntityMouseButtonType = E2DEntityMouseButtonType.LEFT_MOUSE_BUTTON) -> None
unreal.WdpActorEntity.post_entity_created() -> None
unreal.WdpActorEntity.pre_delete_entity_operation() -> None
unreal.WdpActorEntity.pre_entity_removed() -> None
unreal.WdpActorEntity.should_redraw(atom_changed_data: Map[Class, AtomChangedProperty]) -> bool
unreal.WdpActorEntity.update_graphics(atom_changed_data: Map[Class, AtomChangedProperty]) -> bool
```

## `unreal.WdpCameraPresetActor(Actor)`

```python
unreal.WdpCameraPresetActor.all_camera_data_preview(value: AllCameraData) -> None
unreal.WdpCameraPresetActor.camera_fov(value: float) -> None
unreal.WdpCameraPresetActor.camera_index(value: int) -> None
unreal.WdpCameraPresetActor.camera_location(value: Vector) -> None
unreal.WdpCameraPresetActor.camera_pivot(value: Vector) -> None
unreal.WdpCameraPresetActor.camera_rotation(value: Rotator) -> None
unreal.WdpCameraPresetActor.camera_tag(value: GameplayTagContainer) -> None
unreal.WdpCameraPresetActor.change_camera(settings: TravelAnimationSettings, duration: float) -> bool
unreal.WdpCameraPresetActor.collision_mode(value: CameraCollisionMode) -> None
unreal.WdpCameraPresetActor.custom_points(value: Array[Vector]) -> None
unreal.WdpCameraPresetActor.does_match_camera(tag: GameplayTag, index: int) -> bool
unreal.WdpCameraPresetActor.enabled_features(value: int) -> None
unreal.WdpCameraPresetActor.forward_direction(value: MoveForwardDirection) -> None
unreal.WdpCameraPresetActor.ground_position_mode(value: GroundPositionMode) -> None
unreal.WdpCameraPresetActor.max_zoom_distance(value: float) -> None
unreal.WdpCameraPresetActor.max_zoom_fov(value: float) -> None
unreal.WdpCameraPresetActor.min_zoom_distance(value: float) -> None
unreal.WdpCameraPresetActor.min_zoom_fov(value: float) -> None
unreal.WdpCameraPresetActor.note(value: str) -> None
unreal.WdpCameraPresetActor.override_collision(value: bool) -> None
unreal.WdpCameraPresetActor.override_core_data(value: bool) -> None
unreal.WdpCameraPresetActor.override_features(value: bool) -> None
unreal.WdpCameraPresetActor.override_forward_direction(value: bool) -> None
unreal.WdpCameraPresetActor.override_rotate_limit(value: bool) -> None
unreal.WdpCameraPresetActor.override_rotate_mode(value: bool) -> None
unreal.WdpCameraPresetActor.override_zoom_limit(value: bool) -> None
unreal.WdpCameraPresetActor.override_zoom_mode(value: bool) -> None
unreal.WdpCameraPresetActor.pitch_limit(value: Vector2D) -> None
unreal.WdpCameraPresetActor.possess_pawn_ref(value: Pawn) -> None
unreal.WdpCameraPresetActor.possess_use_auto_spawn(value: bool) -> None
unreal.WdpCameraPresetActor.profile_name(value: CollisionProfileName) -> None
unreal.WdpCameraPresetActor.roll_limit(value: Vector2D) -> None
unreal.WdpCameraPresetActor.rotate_mode(value: CameraRotateMode) -> None
unreal.WdpCameraPresetActor.set_preset_with_camera_data(all_camera_data: AllCameraData) -> None
unreal.WdpCameraPresetActor.spawn_pawn_class(value: Class) -> None
unreal.WdpCameraPresetActor.use_as_default_camera(value: bool) -> None
unreal.WdpCameraPresetActor.use_pivot_location_as_spawn_location(value: bool) -> None
unreal.WdpCameraPresetActor.use_possess_mode(value: bool) -> None
unreal.WdpCameraPresetActor.use_wdp_pawn_as_default(value: bool) -> None
unreal.WdpCameraPresetActor.yaw_limit(value: Vector2D) -> None
unreal.WdpCameraPresetActor.zoom_mode(value: ZoomActionType) -> None
```

## `unreal.WdpCoordinateTransformParams(ParamsBase)`

```python
unreal.WdpCoordinateTransformParams.__init__(from_: Array[Vector] = []) -> None
unreal.WdpCoordinateTransformParams.from_(value: Array[Vector]) -> None
```

## `unreal.WdpCoordinateTransformResults(ResultBase)`

```python
unreal.WdpCoordinateTransformResults.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, to: Array[Vector] = []) -> None
unreal.WdpCoordinateTransformResults.to(value: Array[Vector]) -> None
```

## `unreal.WdpEnvironmentSubsystem(WorldSubsystem)`

```python
unreal.WdpEnvironmentSubsystem.get() -> WdpEnvironmentSubsystem
unreal.WdpEnvironmentSubsystem.get_realtime_weather_manager() -> RealtimeWeatherManager
unreal.WdpEnvironmentSubsystem.get_weather_control_manager() -> WeatherControlManager
```

## `unreal.WdpEnvironmentUtilSubsystem(WorldSubsystem)`

```python
unreal.WdpEnvironmentUtilSubsystem.get() -> WdpEnvironmentUtilSubsystem
unreal.WdpEnvironmentUtilSubsystem.get_environment_util_manager() -> EnvironmentUtilManager
```

## `unreal.WdpVisualSubsystem(TickableWorldSubsystem)`

```python
unreal.WdpVisualSubsystem.get_outline_thickness() -> float
unreal.WdpVisualSubsystem.get_visual_style() -> Array[VisualStyleValue]
unreal.WdpVisualSubsystem.hidden_by_f_id(hidden_f_ids: Set[int]) -> bool
unreal.WdpVisualSubsystem.highlight_actor(actor: Actor, enabled: bool = True, custom_style_index: int = 0) -> bool
unreal.WdpVisualSubsystem.highlight_by_f_id(outline_params: Array[VisualParam]) -> bool
unreal.WdpVisualSubsystem.highlight_by_layer(outline_params: Array[VisualParam]) -> bool
unreal.WdpVisualSubsystem.highlight_component(pc: PrimitiveComponent, enabled: bool = True, custom_style_index: int = 0) -> bool
unreal.WdpVisualSubsystem.outline_actor(actor: Actor, enabled: bool = True, custom_style_index: int = 0) -> bool
unreal.WdpVisualSubsystem.outline_by_f_id(outline_params: Array[VisualParam]) -> bool
unreal.WdpVisualSubsystem.outline_by_layer(outline_params: Array[VisualParam]) -> bool
unreal.WdpVisualSubsystem.outline_component(pc: PrimitiveComponent, enabled: bool = True, custom_style_index: int = 0) -> bool
unreal.WdpVisualSubsystem.set_outline_thickness(thickness: float) -> bool
unreal.WdpVisualSubsystem.set_visual_style(custom_style_index: int, color: str) -> bool
```

## `unreal.WdpWorldPosParams(ParamsBase)`

```python
unreal.WdpWorldPosParams.__init__(world_pos: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.WdpWorldPosParams.world_pos(value: Vector) -> None
```

## `unreal.WidgetTransform(StructBase)`

```python
unreal.WidgetTransform.__init__(translation: Vector2D = [0.000000, 0.000000], scale: Vector2D = [0.000000, 0.000000], shear: Vector2D = [0.000000, 0.000000], angle: float = 0.000000) -> None
unreal.WidgetTransform.angle(value: float) -> None
unreal.WidgetTransform.scale(value: Vector2D) -> None
unreal.WidgetTransform.shear(value: Vector2D) -> None
unreal.WidgetTransform.translation(value: Vector2D) -> None
```

## `unreal.WindowSubsystem(GameInstanceSubsystem)`

```python
unreal.WindowSubsystem.get() -> WindowSubsystem
unreal.WindowSubsystem.register_screen_layer(layer_name: Name, z_order: int) -> bool
```

## `unreal.World(Object)`

```python
unreal.World.get_data_layer_manager() -> DataLayerManager
unreal.World.get_world_settings() -> WorldSettings
```

## `unreal.WorldConditionEditable(StructBase)`

```python
unreal.WorldConditionEditable.__init__() -> None
```

## `unreal.WorldConditionQueryDefinition(StructBase)`

```python
unreal.WorldConditionQueryDefinition.__init__() -> None
```

## `unreal.WorldDataLayers(Info)`

```python
unreal.WorldDataLayers.world_data_layers(value: Set[DataLayer]) -> None
```

## `unreal.WorldOriginAnchor(Actor)`

```python
unreal.WorldOriginAnchor.anchor_type(value: AnchorType) -> None
unreal.WorldOriginAnchor.calc_move_along_surface(start: Vector, surface_dir: Vector) -> Tuple[Vector, Rotator]
unreal.WorldOriginAnchor.calc_move_on_sphere_surface(current: Transform, world_dir: Vector, distance: float) -> Transform
unreal.WorldOriginAnchor.calc_origin_from_sphere_center_transform(transform: Transform) -> Vector
unreal.WorldOriginAnchor.calc_world_center_transform(lon: float, lat: float, alt: float) -> Transform
unreal.WorldOriginAnchor.convert_focus_to_lon_lat_alt_to_camera_data(target_longtude: float, target_latitude: float, target_altitude: float, distance: float = 1000.000000, surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]) -> Optional[CoreCameraData]
unreal.WorldOriginAnchor.convert_lon_lat_alt_to_camera_data(longtude: float, latitude: float, altitude: float, surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]) -> Optional[CoreCameraData]
unreal.WorldOriginAnchor.convert_rotation_to_surface_space(location: Vector, rotation: Rotator) -> Rotator
unreal.WorldOriginAnchor.convert_surface_rotation_to_world(location: Vector, rotation: Rotator) -> Rotator
unreal.WorldOriginAnchor.earth_radius(value: float) -> None
unreal.WorldOriginAnchor.get_altitude_at_location(location: Vector) -> float
unreal.WorldOriginAnchor.get_earth_center_transform() -> Transform
unreal.WorldOriginAnchor.get_earth_center_transform_aes6() -> Transform
unreal.WorldOriginAnchor.get_earth_center_transform_cesium() -> Transform
unreal.WorldOriginAnchor.get_earth_center_transform_geo_ref() -> Transform
unreal.WorldOriginAnchor.get_east_south_up_rotation(location: Vector) -> Rotator
unreal.WorldOriginAnchor.get_east_south_up_rotation_aes6(location: Vector) -> Rotator
unreal.WorldOriginAnchor.get_east_south_up_rotation_cesium(location: Vector) -> Rotator
unreal.WorldOriginAnchor.get_east_south_up_rotation_geo_ref(location: Vector) -> Rotator
unreal.WorldOriginAnchor.get_east_south_up_rotation_sphere(location: Vector) -> Rotator
unreal.WorldOriginAnchor.get_gravity_direction(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_is_planet_world() -> bool
unreal.WorldOriginAnchor.get_lon_lat_to_world_location(lon: float, lat: float, alt: float) -> Vector
unreal.WorldOriginAnchor.get_lon_lat_to_world_location_aes6(lon: float, lat: float, alt: float) -> Vector
unreal.WorldOriginAnchor.get_lon_lat_to_world_location_cesium(lon: float, lat: float, alt: float) -> Vector
unreal.WorldOriginAnchor.get_lon_lat_to_world_location_geo_ref(lon: float, lat: float, alt: float) -> Vector
unreal.WorldOriginAnchor.get_lon_lat_to_world_location_sphere(lon: float, lat: float, alt: float, radius: float) -> Vector
unreal.WorldOriginAnchor.get_surface_direction(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_surface_direction_sphere(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_world_center() -> Vector
unreal.WorldOriginAnchor.get_world_location_to_lon_lat(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_world_location_to_lon_lat_aes6(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_world_location_to_lon_lat_cesium(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_world_location_to_lon_lat_geo_ref(location: Vector) -> Vector
unreal.WorldOriginAnchor.get_world_location_to_lon_lat_sphere(location: Vector, radius: float) -> Vector
unreal.WorldOriginAnchor.get_world_origin_anchor(world_context_object: Object) -> WorldOriginAnchor
unreal.WorldOriginAnchor.init_sphere_mode_transform() -> None
unreal.WorldOriginAnchor.initialize() -> None
unreal.WorldOriginAnchor.origin_altitude(value: float) -> None
unreal.WorldOriginAnchor.origin_at_planet_center(value: bool) -> None
unreal.WorldOriginAnchor.origin_latitude(value: float) -> None
unreal.WorldOriginAnchor.origin_longitude(value: float) -> None
unreal.WorldOriginAnchor.update_sphere_mode_data(new_origin_at_center: bool, origin_lon: float, origin_lat: float, origin_alt: float) -> None
unreal.WorldOriginAnchor.use_actor_transform_as_origin(value: bool) -> None
unreal.WorldOriginAnchor.world_center_transform(value: Transform) -> None
```

## `unreal.WorldPartitionActorFilter(StructBase)`

```python
unreal.WorldPartitionActorFilter.__init__() -> None
```

## `unreal.WorldPartitionBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.WorldPartitionBlueprintLibrary.get_actor_descs() -> Optional[Array[ActorDesc]]
unreal.WorldPartitionBlueprintLibrary.get_actor_descs_for_actors(actors: Array[Actor]) -> Optional[Array[ActorDesc]]
unreal.WorldPartitionBlueprintLibrary.get_data_layer_manager(world_context_object: Object) -> DataLayerManager
unreal.WorldPartitionBlueprintLibrary.get_editor_world_bounds() -> Box
unreal.WorldPartitionBlueprintLibrary.get_intersecting_actor_descs(box: Box) -> Optional[Array[ActorDesc]]
unreal.WorldPartitionBlueprintLibrary.get_runtime_world_bounds() -> Box
unreal.WorldPartitionBlueprintLibrary.load_actors(actors_to_load: Array[Guid]) -> None
unreal.WorldPartitionBlueprintLibrary.pin_actors(actors_to_pin: Array[Guid]) -> None
unreal.WorldPartitionBlueprintLibrary.unload_actors(actors_to_unload: Array[Guid]) -> None
unreal.WorldPartitionBlueprintLibrary.unpin_actors(actors_to_unpin: Array[Guid]) -> None
```

## `unreal.WorldPartitionDestructibleInHLODSupportLibrary(BlueprintFunctionLibrary)`

```python
unreal.WorldPartitionDestructibleInHLODSupportLibrary.damage_in_hlod(destructible_in_hlod: WorldPartitionDestructibleInHLODInterface, damage_percent: float) -> None
unreal.WorldPartitionDestructibleInHLODSupportLibrary.destroy_in_hlod(destructible_in_hlod: WorldPartitionDestructibleInHLODInterface) -> None
```

## `unreal.WorldPartitionHLODDestructionTag(StructBase)`

```python
unreal.WorldPartitionHLODDestructionTag.__init__() -> None
```

## `unreal.WorldPartitionStreamingQuerySource(StructBase)`

```python
unreal.WorldPartitionStreamingQuerySource.__init__(location: Vector = [0.000000, 0.000000, 0.000000], radius: float = 0.000000, use_grid_loading_range: bool = False, data_layers: Array[Name] = [], data_layers_only: bool = False, spatial_query: bool = False) -> None
unreal.WorldPartitionStreamingQuerySource.data_layers(value: Array[Name]) -> None
unreal.WorldPartitionStreamingQuerySource.data_layers_only(value: bool) -> None
unreal.WorldPartitionStreamingQuerySource.location(value: Vector) -> None
unreal.WorldPartitionStreamingQuerySource.radius(value: float) -> None
unreal.WorldPartitionStreamingQuerySource.spatial_query(value: bool) -> None
unreal.WorldPartitionStreamingQuerySource.use_grid_loading_range(value: bool) -> None
```

## `unreal.WorldPartitionStreamingSourceComponent(ActorComponent)`

```python
unreal.WorldPartitionStreamingSourceComponent.disable_streaming_source() -> None
unreal.WorldPartitionStreamingSourceComponent.enable_streaming_source() -> None
unreal.WorldPartitionStreamingSourceComponent.is_streaming_completed() -> bool
unreal.WorldPartitionStreamingSourceComponent.is_streaming_source_enabled() -> bool
unreal.WorldPartitionStreamingSourceComponent.priority(value: StreamingSourcePriority) -> None
unreal.WorldPartitionStreamingSourceComponent.shapes(value: Array[StreamingSourceShape]) -> None
unreal.WorldPartitionStreamingSourceComponent.streaming_source_enabled(value: bool) -> None
unreal.WorldPartitionStreamingSourceComponent.target_behavior(value: StreamingSourceTargetBehavior) -> None
unreal.WorldPartitionStreamingSourceComponent.target_grid(value: Name) -> None
unreal.WorldPartitionStreamingSourceComponent.target_grids(value: Array[Name]) -> None
unreal.WorldPartitionStreamingSourceComponent.target_hlod_layer(value: HLODLayer) -> None
unreal.WorldPartitionStreamingSourceComponent.target_hlod_layers(value: Array[HLODLayer]) -> None
```

## `unreal.WorldPartitionSubsystem(TickableWorldSubsystem)`

```python
unreal.WorldPartitionSubsystem.is_all_streaming_completed() -> bool
unreal.WorldPartitionSubsystem.is_streaming_completed(query_state: WorldPartitionRuntimeCellState, query_sources: Array[WorldPartitionStreamingQuerySource], exact_state: bool) -> bool
```

## `unreal.WorldReticleParameters(StructBase)`

```python
unreal.WorldReticleParameters.__init__(aoe_scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.WorldReticleParameters.aoe_scale(value: Vector) -> None
```

## `unreal.WorldSettings(Info)`

```python
unreal.WorldSettings.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.WorldSettings.ai_system_class() -> Class
unreal.WorldSettings.default_color_scale() -> Vector
unreal.WorldSettings.default_game_mode() -> Class
unreal.WorldSettings.default_game_type() -> Class
unreal.WorldSettings.default_physics_volume_class() -> Class
unreal.WorldSettings.enable_ai_system() -> bool
unreal.WorldSettings.enable_large_worlds(value: bool) -> None
unreal.WorldSettings.enable_navigation_system() -> bool
unreal.WorldSettings.enable_world_bounds_checks() -> bool
unreal.WorldSettings.enable_world_composition() -> bool
unreal.WorldSettings.enable_world_origin_rebasing() -> bool
unreal.WorldSettings.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.WorldSettings.global_gravity_set() -> bool
unreal.WorldSettings.global_gravity_z() -> float
unreal.WorldSettings.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.WorldSettings.kill_z() -> float
unreal.WorldSettings.kill_z_damage_type() -> Class
unreal.WorldSettings.lightmass_settings(value: LightmassWorldInfoSettings) -> None
unreal.WorldSettings.navigation_system_config() -> NavigationSystemConfig
unreal.WorldSettings.physics_collision_handler_class() -> Class
unreal.WorldSettings.use_client_side_level_streaming_volumes() -> bool
unreal.WorldSettings.volumetric_lightmap_loading_range(value: float) -> None
unreal.WorldSettings.world_to_meters() -> float
```

## `unreal.ZoneGraphAnnotationTestingActor(Actor)`

```python
unreal.ZoneGraphAnnotationTestingActor.trigger() -> None
```

## `unreal.ZoneGraphTestingActor(Actor)`

```python
unreal.ZoneGraphTestingActor.disable_custom_tests() -> None
unreal.ZoneGraphTestingActor.enable_custom_tests() -> None
```

## `unreal.glTFRuntimeAssetActor(Actor)`

```python
unreal.glTFRuntimeAssetActor.allow_cameras(value: bool) -> None
unreal.glTFRuntimeAssetActor.allow_lights(value: bool) -> None
unreal.glTFRuntimeAssetActor.allow_node_animations(value: bool) -> None
unreal.glTFRuntimeAssetActor.allow_pose_animations(value: bool) -> None
unreal.glTFRuntimeAssetActor.allow_skeletal_animations(value: bool) -> None
unreal.glTFRuntimeAssetActor.asset(value: glTFRuntimeAsset) -> None
unreal.glTFRuntimeAssetActor.asset_root() -> SceneComponent
unreal.glTFRuntimeAssetActor.auto_play_animations(value: bool) -> None
unreal.glTFRuntimeAssetActor.curve_based_animations(value: Map[SceneComponent, glTFRuntimeAnimationCurve]) -> None
unreal.glTFRuntimeAssetActor.discovered_curve_animations_names() -> Set[str]
unreal.glTFRuntimeAssetActor.force_skinned_mesh_to_root(value: bool) -> None
unreal.glTFRuntimeAssetActor.get_skeletal_animation_by_name(skeletal_mesh_component: SkeletalMeshComponent, animation_name: str) -> AnimSequence
unreal.glTFRuntimeAssetActor.light_config(value: glTFRuntimeLightConfig) -> None
unreal.glTFRuntimeAssetActor.load_all_skeletal_animations(value: bool) -> None
unreal.glTFRuntimeAssetActor.receive_on_skeletal_mesh_component_created(skeletal_mesh_component: SkeletalMeshComponent, node: glTFRuntimeNode) -> None
unreal.glTFRuntimeAssetActor.receive_on_static_mesh_component_created(static_mesh_component: StaticMeshComponent, node: glTFRuntimeNode) -> None
unreal.glTFRuntimeAssetActor.root_node_index(value: int) -> None
unreal.glTFRuntimeAssetActor.set_curve_animation_by_name(curve_animation_name: str) -> None
unreal.glTFRuntimeAssetActor.skeletal_animation_config(value: glTFRuntimeSkeletalAnimationConfig) -> None
unreal.glTFRuntimeAssetActor.skeletal_mesh_config(value: glTFRuntimeSkeletalMeshConfig) -> None
unreal.glTFRuntimeAssetActor.static_mesh_config(value: glTFRuntimeStaticMeshConfig) -> None
unreal.glTFRuntimeAssetActor.static_meshes_as_skeletal(value: bool) -> None
unreal.glTFRuntimeAssetActor.static_meshes_as_skeletal_on_morph_targets(value: bool) -> None
```

## `unreal.glTFRuntimeAssetActorAsync(Actor)`

```python
unreal.glTFRuntimeAssetActorAsync.asset(value: glTFRuntimeAsset) -> None
unreal.glTFRuntimeAssetActorAsync.asset_root() -> SceneComponent
unreal.glTFRuntimeAssetActorAsync.receive_on_scenes_loaded() -> None
unreal.glTFRuntimeAssetActorAsync.show_while_loading(value: bool) -> None
unreal.glTFRuntimeAssetActorAsync.skeletal_mesh_config(value: glTFRuntimeSkeletalMeshConfig) -> None
unreal.glTFRuntimeAssetActorAsync.static_mesh_config(value: glTFRuntimeStaticMeshConfig) -> None
unreal.glTFRuntimeAssetActorAsync.static_meshes_as_skeletal(value: bool) -> None
```

