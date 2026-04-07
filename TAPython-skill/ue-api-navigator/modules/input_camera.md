# Unreal Python API — Input Camera

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AITestSpawnInfo(AITestSpawnInfoBase)`

```python
unreal.AITestSpawnInfo.__init__(spawn_location: Actor = None, number_to_spawn: int = 0, spawn_delay: float = 0.000000, pre_spawn_delay: float = 0.000000, pawn_class: Class = None, controller_class: Class = None, team_id: GenericTeamId = [255], behavior_tree: BehaviorTree = None) -> None
unreal.AITestSpawnInfo.behavior_tree(value: BehaviorTree) -> None
unreal.AITestSpawnInfo.controller_class(value: Class) -> None
unreal.AITestSpawnInfo.pawn_class(value: Class) -> None
unreal.AITestSpawnInfo.team_id(value: GenericTeamId) -> None
```

## `unreal.AITestSpawnInfoBase(StructBase)`

```python
unreal.AITestSpawnInfoBase.__init__(spawn_location: Actor = None, number_to_spawn: int = 0, spawn_delay: float = 0.000000, pre_spawn_delay: float = 0.000000) -> None
unreal.AITestSpawnInfoBase.number_to_spawn(value: int) -> None
unreal.AITestSpawnInfoBase.pre_spawn_delay(value: float) -> None
unreal.AITestSpawnInfoBase.spawn_delay(value: float) -> None
unreal.AITestSpawnInfoBase.spawn_location(value: Actor) -> None
```

## `unreal.AITestSpawnSet(AITestSpawnSetBase)`

```python
unreal.AITestSpawnSet.__init__(name: Name = "None", enabled: bool = False, fallback_spawn_location: Actor = None, spawn_info_container: Array[AITestSpawnInfo] = []) -> None
unreal.AITestSpawnSet.spawn_info_container(value: Array[AITestSpawnInfo]) -> None
```

## `unreal.AITestSpawnSetBase(StructBase)`

```python
unreal.AITestSpawnSetBase.__init__(name: Name = "None", enabled: bool = False, fallback_spawn_location: Actor = None) -> None
unreal.AITestSpawnSetBase.enabled(value: bool) -> None
unreal.AITestSpawnSetBase.fallback_spawn_location(value: Actor) -> None
unreal.AITestSpawnSetBase.name(value: Name) -> None
```

## `unreal.AbilitySystemTestPawn(DefaultPawn)`

```python
unreal.AbilitySystemTestPawn.ability_system_component() -> AbilitySystemComponent
unreal.AbilitySystemTestPawn.forward_gameplay_cue_to_parent() -> None
```

## `unreal.AbilityTask_WaitInputPress(AbilityTask)`

```python
unreal.AbilityTask_WaitInputPress.on_press(value: InputPressDelegate) -> None
```

## `unreal.AbilityTask_WaitInputRelease(AbilityTask)`

```python
unreal.AbilityTask_WaitInputRelease.on_release(value: InputReleaseDelegate) -> None
```

## `unreal.ActivateCameraRigFunctions(BlueprintFunctionLibrary)`

```python
unreal.ActivateCameraRigFunctions.activate_base_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
unreal.ActivateCameraRigFunctions.activate_global_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
unreal.ActivateCameraRigFunctions.activate_persistent_base_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
unreal.ActivateCameraRigFunctions.activate_persistent_global_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
unreal.ActivateCameraRigFunctions.activate_persistent_visual_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
unreal.ActivateCameraRigFunctions.activate_visual_camera_rig(world_context_object: Object, player_controller: PlayerController, camera_rig: CameraRigAsset) -> None
```

## `unreal.AesEditorPawnInterface(Interface)`

```python
unreal.AesEditorPawnInterface.focus_to(point: Vector) -> None
```

## `unreal.AllCameraData(TableRowBase)`

```python
unreal.AllCameraData.__init__(core_camera_data: CoreCameraData = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 90.000000, [0.000000, 0.000000, 0.000000]], rotate_limit_data: CameraRotationLimitationData = [-89.000000, 0.000000, -179.999985, 179.999985, False], zoom_limit_data: CameraZoomLimitationData = [0.000000, 1000000.000000, 50.000000, 110.000000], collision_data: CameraCollisionData = [CameraCollisionMode.CCM_NO_COLLISION, "NoCollision", [], GroundPositionMode.GPM_AVOID_ONLY]) -> None
unreal.AllCameraData.collision_data(value: CameraCollisionData) -> None
unreal.AllCameraData.core_camera_data(value: CoreCameraData) -> None
unreal.AllCameraData.rotate_limit_data(value: CameraRotationLimitationData) -> None
unreal.AllCameraData.zoom_limit_data(value: CameraZoomLimitationData) -> None
```

## `unreal.AnalogInputEvent(KeyEvent)`

```python
unreal.AnalogInputEvent.__init__() -> None
```

## `unreal.ArchVisCharacter(Character)`

```python
unreal.ArchVisCharacter.look_up_at_rate_axis_name() -> str
unreal.ArchVisCharacter.look_up_axis_name() -> str
unreal.ArchVisCharacter.mouse_sensitivity_scale_pitch() -> float
unreal.ArchVisCharacter.mouse_sensitivity_scale_yaw() -> float
unreal.ArchVisCharacter.move_forward_axis_name() -> str
unreal.ArchVisCharacter.move_right_axis_name() -> str
unreal.ArchVisCharacter.turn_at_rate_axis_name() -> str
unreal.ArchVisCharacter.turn_axis_name() -> str
```

## `unreal.BindToController(StructBase)`

```python
unreal.BindToController.__init__() -> None
```

## `unreal.BlendSpacePlayerLibrary(BlueprintFunctionLibrary)`

```python
unreal.BlendSpacePlayerLibrary.convert_to_blend_space_player(node: AnimNodeReference) -> Tuple[BlendSpacePlayerReference, AnimNodeReferenceConversionResult]
unreal.BlendSpacePlayerLibrary.convert_to_blend_space_player_pure(node: AnimNodeReference) -> Tuple[BlendSpacePlayerReference, bool]
unreal.BlendSpacePlayerLibrary.get_blend_space(blend_space_player: BlendSpacePlayerReference) -> BlendSpace
unreal.BlendSpacePlayerLibrary.get_loop(blend_space_player: BlendSpacePlayerReference) -> bool
unreal.BlendSpacePlayerLibrary.get_play_rate(blend_space_player: BlendSpacePlayerReference) -> float
unreal.BlendSpacePlayerLibrary.get_position(blend_space_player: BlendSpacePlayerReference) -> Vector
unreal.BlendSpacePlayerLibrary.get_start_position(blend_space_player: BlendSpacePlayerReference) -> float
unreal.BlendSpacePlayerLibrary.set_blend_space(blend_space_player: BlendSpacePlayerReference, blend_space: BlendSpace) -> BlendSpacePlayerReference
unreal.BlendSpacePlayerLibrary.set_blend_space_with_inertial_blending(update_context: AnimUpdateContext, blend_space_player: BlendSpacePlayerReference, blend_space: BlendSpace, blend_time: float = 0.200000) -> BlendSpacePlayerReference
unreal.BlendSpacePlayerLibrary.set_loop(blend_space_player: BlendSpacePlayerReference, loop: bool) -> BlendSpacePlayerReference
unreal.BlendSpacePlayerLibrary.set_play_rate(blend_space_player: BlendSpacePlayerReference, play_rate: float) -> BlendSpacePlayerReference
unreal.BlendSpacePlayerLibrary.set_reset_play_time_when_blend_space_changes(blend_space_player: BlendSpacePlayerReference, reset: bool) -> BlendSpacePlayerReference
unreal.BlendSpacePlayerLibrary.should_reset_play_time_when_blend_space_changes(blend_space_player: BlendSpacePlayerReference) -> bool
unreal.BlendSpacePlayerLibrary.snap_to_position(blend_space_player: BlendSpacePlayerReference, new_position: Vector) -> None
```

## `unreal.BlendSpacePlayerReference(AnimNodeReference)`

```python
unreal.BlendSpacePlayerReference.__init__() -> None
```

## `unreal.CacheSpawnableTemplate(StructBase)`

```python
unreal.CacheSpawnableTemplate.__init__() -> None
```

## `unreal.CameraComponent(SceneComponent)`

```python
unreal.CameraComponent.add_or_update_blendable(blendable_object: BlendableInterface, weight: float = 1.000000) -> None
unreal.CameraComponent.aspect_ratio(value: float) -> None
unreal.CameraComponent.aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
unreal.CameraComponent.auto_calculate_ortho_planes(value: bool) -> None
unreal.CameraComponent.auto_plane_shift(value: float) -> None
unreal.CameraComponent.b_use_controller_view_rotation(value: bool) -> None
unreal.CameraComponent.b_use_pawn_view_rotation(value: bool) -> None
unreal.CameraComponent.camera_mesh(value: StaticMesh) -> None
unreal.CameraComponent.camera_mesh_hidden_in_game(value: bool) -> None
unreal.CameraComponent.constrain_aspect_ratio(value: bool) -> None
unreal.CameraComponent.crop_overscan(value: bool) -> None
unreal.CameraComponent.draw_frustum_allowed(value: bool) -> None
unreal.CameraComponent.enable_first_person_field_of_view(value: bool) -> None
unreal.CameraComponent.enable_first_person_scale(value: bool) -> None
unreal.CameraComponent.field_of_view(value: float) -> None
unreal.CameraComponent.first_person_field_of_view(value: float) -> None
unreal.CameraComponent.first_person_scale(value: float) -> None
unreal.CameraComponent.get_camera_view(delta_time: float) -> MinimalViewInfo
unreal.CameraComponent.lock_to_hmd(value: bool) -> None
unreal.CameraComponent.ortho_far_clip_plane(value: float) -> None
unreal.CameraComponent.ortho_near_clip_plane(value: float) -> None
unreal.CameraComponent.ortho_width(value: float) -> None
unreal.CameraComponent.override_aspect_ratio_axis_constraint(value: bool) -> None
unreal.CameraComponent.overscan(value: float) -> None
unreal.CameraComponent.post_process_blend_weight(value: float) -> None
unreal.CameraComponent.post_process_settings(value: PostProcessSettings) -> None
unreal.CameraComponent.projection_mode(value: CameraProjectionMode) -> None
unreal.CameraComponent.remove_blendable(blendable_object: BlendableInterface) -> None
unreal.CameraComponent.scale_resolution_with_overscan(value: bool) -> None
unreal.CameraComponent.set_aspect_ratio(aspect_ratio: float) -> None
unreal.CameraComponent.set_aspect_ratio_axis_constraint(aspect_ratio_axis_constraint: AspectRatioAxisConstraint) -> None
unreal.CameraComponent.set_auto_calculate_ortho_planes(auto_calculate: bool) -> None
unreal.CameraComponent.set_auto_plane_shift(auto_plane_shift: float) -> None
unreal.CameraComponent.set_constraint_aspect_ratio(constrain_aspect_ratio: bool) -> None
unreal.CameraComponent.set_crop_overscan(crop_overscan: bool) -> None
unreal.CameraComponent.set_enable_first_person_field_of_view(enable_first_person_field_of_view: bool) -> None
unreal.CameraComponent.set_enable_first_person_scale(enable_first_person_scale: bool) -> None
unreal.CameraComponent.set_field_of_view(field_of_view: float) -> None
unreal.CameraComponent.set_first_person_field_of_view(first_person_field_of_view: float) -> None
unreal.CameraComponent.set_first_person_scale(first_person_scale: float) -> None
unreal.CameraComponent.set_ortho_far_clip_plane(ortho_far_clip_plane: float) -> None
unreal.CameraComponent.set_ortho_near_clip_plane(ortho_near_clip_plane: float) -> None
unreal.CameraComponent.set_ortho_width(ortho_width: float) -> None
unreal.CameraComponent.set_overscan(overscan: float) -> None
unreal.CameraComponent.set_post_process_blend_weight(post_process_blend_weight: float) -> None
unreal.CameraComponent.set_projection_mode(projection_mode: CameraProjectionMode) -> None
unreal.CameraComponent.set_scale_resolution_with_overscan(scale_resolution_with_overscan: bool) -> None
unreal.CameraComponent.set_update_ortho_planes(update_ortho_planes: bool) -> None
unreal.CameraComponent.set_use_camera_height_as_view_target(use_camera_height_as_view_target: bool) -> None
unreal.CameraComponent.set_use_field_of_view_for_lod(use_field_of_view_for_lod: bool) -> None
unreal.CameraComponent.update_ortho_planes(value: bool) -> None
unreal.CameraComponent.use_camera_height_as_view_target(value: bool) -> None
unreal.CameraComponent.use_field_of_view_for_lod(value: bool) -> None
unreal.CameraComponent.use_pawn_control_rotation(value: bool) -> None
```

## `unreal.CameraControlManager(WorldSubsystem)`

```python
unreal.CameraControlManager.camera_control_pitch_limit() -> Vector2D
unreal.CameraControlManager.camera_control_yaw_limit() -> Vector2D
unreal.CameraControlManager.disable_camera_control_features(features: int) -> None
unreal.CameraControlManager.enable_camera_control_features(features: int) -> None
unreal.CameraControlManager.focus_to_point(target_location: Vector, distance: float = 5000.000000, default_duration: float = 0.500000) -> bool
unreal.CameraControlManager.focus_to_position(target_location: Vector, target_rotation: Rotator, distance: float = 5000.000000, duration: float = 0.500000) -> bool
unreal.CameraControlManager.get_camera_animation() -> Optional[WDPCameraAnimationData]
unreal.CameraControlManager.get_camera_info() -> Optional[WDPCameraInfo]
unreal.CameraControlManager.get_camera_limit() -> Optional[WDPCameraLimitData]
unreal.CameraControlManager.get_camera_speed() -> Optional[WDPCameraSpeedData]
unreal.CameraControlManager.get_control_mode() -> str
unreal.CameraControlManager.notify_camera_motion_end() -> None
unreal.CameraControlManager.notify_camera_motion_start(e_reason: CameraMotionReason, eids: Array[str]) -> None
unreal.CameraControlManager.remote_camera_move(move_direction: WDPDirection, step: float) -> bool
unreal.CameraControlManager.remote_toggle_camera_rotate(start: bool = False) -> bool
unreal.CameraControlManager.remote_toggle_camera_self_rotate(pressed: bool = False) -> bool
unreal.CameraControlManager.remote_toggle_camera_zoom(start: bool = True) -> bool
unreal.CameraControlManager.remote_update_camera_rotate(rotate_direction: WdpCameraRotateDir, step: float) -> bool
unreal.CameraControlManager.remote_update_camera_zoom(step: float) -> bool
unreal.CameraControlManager.screen_to_world_position(screen_position: Vector2D) -> Optional[Tuple[Vector, Vector]]
unreal.CameraControlManager.set_camera_animation(animation_data: WDPCameraAnimationData) -> bool
unreal.CameraControlManager.set_camera_control_enabled(enabled: bool) -> None
unreal.CameraControlManager.set_camera_limit(limit_data: WDPCameraLimitData) -> bool
unreal.CameraControlManager.set_camera_preset_data(camera_location: Vector, rotation: Rotator = [0.000000, -30.000000, 0.000000], pitch_limit: Vector2D = [-89.000000, 0.000000], yaw_limit: Vector2D = [-179.999000, 179.999000], distance_limit: Vector2D = [0.000000, 10000000.000000], fov: float = 90.000000, control_mode: Name = "RTS", duration: float = 0.500000) -> bool
unreal.CameraControlManager.set_camera_speed(speed_data: WDPCameraSpeedData) -> bool
unreal.CameraControlManager.set_control_mode(control_mode: str, possess_duration: float = 2.000000) -> bool
unreal.CameraControlManager.start_camera_auto_movement_distance(direction: Vector, distance: float, duration: float) -> bool
unreal.CameraControlManager.stop_all_camera_movement() -> bool
unreal.CameraControlManager.toggle_camera_auto_movement(active: bool, direction: Vector, speed: float) -> bool
unreal.CameraControlManager.toggle_camera_auto_rotate(active: bool, rotate_axis: Vector, speed: float, angle: float = 0.000000) -> bool
unreal.CameraControlManager.toggle_camera_rotate_around(active: bool, clock_wise: bool, speed: float) -> bool
unreal.CameraControlManager.update_camera(camera_info: CoreCameraData, duration: float = 1.200000) -> bool
unreal.CameraControlManager.world_to_screen_position(world_position: Vector) -> Optional[Vector2D]
```

## `unreal.CameraData(StructBase)`

```python
unreal.CameraData.__init__(hide_distance: float = 0.000000, hide_type: str = "", url: str = "", size: Vector2D = [0.000000, 0.000000], scale_mode: str = "") -> None
unreal.CameraData.hide_distance() -> float
unreal.CameraData.hide_type() -> str
unreal.CameraData.scale_mode() -> str
unreal.CameraData.size() -> Vector2D
unreal.CameraData.url() -> str
```

## `unreal.CameraExposureSettings(StructBase)`

```python
unreal.CameraExposureSettings.__init__(method: AutoExposureMethod = AutoExposureMethod.AEM_HISTOGRAM, low_percent: float = 0.000000, high_percent: float = 0.000000, min_brightness: float = 0.000000, max_brightness: float = 0.000000, speed_up: float = 0.000000, speed_down: float = 0.000000, bias: float = 0.000000, bias_curve: CurveFloat = None, meter_mask: Texture = None, histogram_log_min: float = 0.000000, histogram_log_max: float = 0.000000, calibration_constant: float = 0.000000, apply_physical_camera_exposure: bool = False) -> None
unreal.CameraExposureSettings.apply_physical_camera_exposure(value: bool) -> None
unreal.CameraExposureSettings.bias(value: float) -> None
unreal.CameraExposureSettings.bias_curve(value: CurveFloat) -> None
unreal.CameraExposureSettings.calibration_constant(value: float) -> None
unreal.CameraExposureSettings.high_percent(value: float) -> None
unreal.CameraExposureSettings.histogram_log_max(value: float) -> None
unreal.CameraExposureSettings.histogram_log_min(value: float) -> None
unreal.CameraExposureSettings.low_percent(value: float) -> None
unreal.CameraExposureSettings.max_brightness(value: float) -> None
unreal.CameraExposureSettings.meter_mask(value: Texture) -> None
unreal.CameraExposureSettings.method(value: AutoExposureMethod) -> None
unreal.CameraExposureSettings.min_brightness(value: float) -> None
unreal.CameraExposureSettings.speed_down(value: float) -> None
unreal.CameraExposureSettings.speed_up(value: float) -> None
```

## `unreal.CameraFilmbackSettings(StructBase)`

```python
unreal.CameraFilmbackSettings.__init__(sensor_width: float = 0.000000, sensor_height: float = 0.000000, sensor_horizontal_offset: float = 0.000000, sensor_vertical_offset: float = 0.000000, sensor_aspect_ratio: float = 0.000000) -> None
unreal.CameraFilmbackSettings.sensor_aspect_ratio() -> float
unreal.CameraFilmbackSettings.sensor_height(value: float) -> None
unreal.CameraFilmbackSettings.sensor_horizontal_offset(value: float) -> None
unreal.CameraFilmbackSettings.sensor_vertical_offset(value: float) -> None
unreal.CameraFilmbackSettings.sensor_width(value: float) -> None
```

## `unreal.CameraFocusSettings(StructBase)`

```python
unreal.CameraFocusSettings.__init__(focus_method: CameraFocusMethod = CameraFocusMethod.DO_NOT_OVERRIDE, manual_focus_distance: float = 0.000000, tracking_focus_settings: CameraTrackingFocusSettings = [None, [0.000000, 0.000000, 0.000000], False], smooth_focus_changes: bool = False, focus_smoothing_interp_speed: float = 0.000000, focus_offset: float = 0.000000) -> None
unreal.CameraFocusSettings.focus_method(value: CameraFocusMethod) -> None
unreal.CameraFocusSettings.focus_offset(value: float) -> None
unreal.CameraFocusSettings.focus_smoothing_interp_speed(value: float) -> None
unreal.CameraFocusSettings.manual_focus_distance(value: float) -> None
unreal.CameraFocusSettings.smooth_focus_changes(value: bool) -> None
unreal.CameraFocusSettings.tracking_focus_settings(value: CameraTrackingFocusSettings) -> None
```

## `unreal.CameraLensEffectInterface(Interface)`

```python
unreal.CameraLensEffectInterface.get_particle_components() -> Array[FXSystemComponent]
unreal.CameraLensEffectInterface.get_primary_particle_component() -> FXSystemComponent
```

## `unreal.CameraLensEffectInterfaceClassSupportLibrary(BlueprintFunctionLibrary)`

```python
unreal.CameraLensEffectInterfaceClassSupportLibrary.get_interface_class(camera_lens: CameraLensInterfaceClassSupport) -> Class
unreal.CameraLensEffectInterfaceClassSupportLibrary.is_interface_class_valid(camera_lens: CameraLensInterfaceClassSupport) -> InterfaceValidResult
unreal.CameraLensEffectInterfaceClassSupportLibrary.is_interface_valid(camera_lens: CameraLensEffectInterface) -> InterfaceValidResult
unreal.CameraLensEffectInterfaceClassSupportLibrary.set_interface_class(class_: Class, var: CameraLensInterfaceClassSupport) -> Tuple[CameraLensInterfaceClassSupport, InterfaceValidResult]
```

## `unreal.CameraLensInterfaceClassSupport(StructBase)`

```python
unreal.CameraLensInterfaceClassSupport.__init__() -> None
```

## `unreal.CameraLensSettings(StructBase)`

```python
unreal.CameraLensSettings.__init__(min_focal_length: float = 0.000000, max_focal_length: float = 0.000000, min_f_stop: float = 0.000000, max_f_stop: float = 0.000000, minimum_focus_distance: float = 0.000000, squeeze_factor: float = 0.000000, diaphragm_blade_count: int = 0) -> None
unreal.CameraLensSettings.diaphragm_blade_count(value: int) -> None
unreal.CameraLensSettings.max_f_stop(value: float) -> None
unreal.CameraLensSettings.max_focal_length(value: float) -> None
unreal.CameraLensSettings.min_f_stop(value: float) -> None
unreal.CameraLensSettings.min_focal_length(value: float) -> None
unreal.CameraLensSettings.minimum_focus_distance(value: float) -> None
unreal.CameraLensSettings.squeeze_factor(value: float) -> None
```

## `unreal.CameraLookatTrackingSettings(StructBase)`

```python
unreal.CameraLookatTrackingSettings.__init__(enable_look_at_tracking: bool = False, draw_debug_look_at_tracking_position: bool = False, look_at_tracking_interp_speed: float = 0.000000, actor_to_track: Actor = None, relative_offset: Vector = [0.000000, 0.000000, 0.000000], allow_roll: bool = False) -> None
unreal.CameraLookatTrackingSettings.actor_to_track(value: Actor) -> None
unreal.CameraLookatTrackingSettings.allow_roll(value: bool) -> None
unreal.CameraLookatTrackingSettings.draw_debug_look_at_tracking_position(value: bool) -> None
unreal.CameraLookatTrackingSettings.enable_look_at_tracking(value: bool) -> None
unreal.CameraLookatTrackingSettings.look_at_tracking_interp_speed(value: float) -> None
unreal.CameraLookatTrackingSettings.relative_offset(value: Vector) -> None
```

## `unreal.CameraModifier(Object)`

```python
unreal.CameraModifier.alpha() -> float
unreal.CameraModifier.alpha_in_time() -> float
unreal.CameraModifier.alpha_out_time() -> float
unreal.CameraModifier.blueprint_modify_camera(delta_time: float, view_location: Vector, view_rotation: Rotator, fov: float) -> Tuple[Vector, Rotator, float]
unreal.CameraModifier.blueprint_modify_post_process(delta_time: float) -> Tuple[float, PostProcessSettings]
unreal.CameraModifier.camera_owner() -> PlayerCameraManager
unreal.CameraModifier.disable_modifier(immediate: bool = False) -> None
unreal.CameraModifier.enable_modifier() -> None
unreal.CameraModifier.exclusive() -> bool
unreal.CameraModifier.get_view_target() -> Actor
unreal.CameraModifier.is_disabled() -> bool
unreal.CameraModifier.is_pending_disable() -> bool
unreal.CameraModifier.priority() -> int
```

## `unreal.CameraMotionReasonData(StructBase)`

```python
unreal.CameraMotionReasonData.__init__() -> None
```

## `unreal.CameraPresetApplyParams(EidParams)`

```python
unreal.CameraPresetApplyParams.__init__(fly_time: float = 0.000000) -> None
unreal.CameraPresetApplyParams.fly_time() -> float
```

## `unreal.CameraPresetEntityAtom(EntityAtomBase)`

```python
unreal.CameraPresetEntityAtom.control_mode(value: str) -> None
unreal.CameraPresetEntityAtom.default_camera(value: bool) -> None
unreal.CameraPresetEntityAtom.field_of_view(value: float) -> None
unreal.CameraPresetEntityAtom.location(value: Vector) -> None
unreal.CameraPresetEntityAtom.pitch_limit(value: Vector2D) -> None
unreal.CameraPresetEntityAtom.rotation(value: CameraPresetRotator) -> None
unreal.CameraPresetEntityAtom.view_distance_limit(value: Vector2D) -> None
unreal.CameraPresetEntityAtom.yaw_limit(value: Vector2D) -> None
```

## `unreal.CameraPresetRotator(StructBase)`

```python
unreal.CameraPresetRotator.__init__(pitch: float = 0.000000, yaw: float = 0.000000) -> None
unreal.CameraPresetRotator.pitch(value: float) -> None
unreal.CameraPresetRotator.yaw(value: float) -> None
```

## `unreal.CameraRigAsset(Object)`

```python
unreal.CameraRigAsset.has_all_matching_gameplay_tags(tag_container: GameplayTagContainer) -> bool
unreal.CameraRigAsset.has_any_matching_gameplay_tags(tag_container: GameplayTagContainer) -> bool
unreal.CameraRigAsset.has_matching_gameplay_tag(tag_to_check: GameplayTag) -> bool
```

## `unreal.CameraRigAssetReference(StructBase)`

```python
unreal.CameraRigAssetReference.__init__() -> None
```

## `unreal.CameraRigParameterOverrides(StructBase)`

```python
unreal.CameraRigParameterOverrides.__init__() -> None
```

## `unreal.CameraRig_Crane(Actor)`

```python
unreal.CameraRig_Crane.crane_arm_length(value: float) -> None
unreal.CameraRig_Crane.crane_pitch(value: float) -> None
unreal.CameraRig_Crane.crane_yaw(value: float) -> None
unreal.CameraRig_Crane.lock_mount_pitch(value: bool) -> None
unreal.CameraRig_Crane.lock_mount_yaw(value: bool) -> None
```

## `unreal.CameraRig_Rail(Actor)`

```python
unreal.CameraRig_Rail.current_position_on_rail(value: float) -> None
unreal.CameraRig_Rail.get_rail_spline_component() -> SplineComponent
unreal.CameraRig_Rail.lock_orientation_to_rail(value: bool) -> None
```

## `unreal.CameraRoamAtom(EntityAtomBase)`

```python
unreal.CameraRoamAtom.auto_rotation() -> bool
unreal.CameraRoamAtom.frames() -> Array[WdpCameraRoamFrame]
unreal.CameraRoamAtom.reset_after_finished() -> bool
```

## `unreal.CameraRoamEntity(WdpStandardEntity)`

```python
unreal.CameraRoamEntity.current_frame_index() -> int
unreal.CameraRoamEntity.current_frame_time() -> float
unreal.CameraRoamEntity.is_playing() -> bool
```

## `unreal.CameraRoamPath(StructBase)`

```python
unreal.CameraRoamPath.__init__(location: RuntimeVectorCurve = [], rotation: RuntimeVectorCurve = [], duration: float = 0.000000, length: float = 0.000000) -> None
unreal.CameraRoamPath.duration(value: float) -> None
unreal.CameraRoamPath.length(value: float) -> None
unreal.CameraRoamPath.location(value: RuntimeVectorCurve) -> None
unreal.CameraRoamPath.rotation(value: RuntimeVectorCurve) -> None
```

## `unreal.CameraRoamingFrameEventArgs(EventArgsBase)`

```python
unreal.CameraRoamingFrameEventArgs.__init__(camera_roam_eid: int = 0, frame_index: int = 0, location: Vector = [0.000000, 0.000000, 0.000000], progress_ratio: float = 0.000000) -> None
unreal.CameraRoamingFrameEventArgs.camera_roam_eid(value: int) -> None
unreal.CameraRoamingFrameEventArgs.frame_index(value: int) -> None
unreal.CameraRoamingFrameEventArgs.location(value: Vector) -> None
unreal.CameraRoamingFrameEventArgs.progress_ratio(value: float) -> None
```

## `unreal.CameraRotationLimitationData(StructBase)`

```python
unreal.CameraRotationLimitationData.__init__(min_pitch: float = 0.000000, max_pitch: float = 0.000000, min_yaw: float = 0.000000, max_yaw: float = 0.000000, use_local_space: bool = False) -> None
unreal.CameraRotationLimitationData.max_pitch(value: float) -> None
unreal.CameraRotationLimitationData.max_yaw(value: float) -> None
unreal.CameraRotationLimitationData.min_pitch(value: float) -> None
unreal.CameraRotationLimitationData.min_yaw(value: float) -> None
unreal.CameraRotationLimitationData.use_local_space(value: bool) -> None
```

## `unreal.CameraShakeBase(Object)`

```python
unreal.CameraShakeBase.get_root_shake_pattern() -> CameraShakePattern
unreal.CameraShakeBase.set_root_shake_pattern(pattern: CameraShakePattern) -> None
unreal.CameraShakeBase.shake_scale(value: float) -> None
```

## `unreal.CameraShakeDuration(StructBase)`

```python
unreal.CameraShakeDuration.__init__() -> None
```

## `unreal.CameraShakeInfo(StructBase)`

```python
unreal.CameraShakeInfo.__init__() -> None
```

## `unreal.CameraShakePatternScrubParams(StructBase)`

```python
unreal.CameraShakePatternScrubParams.__init__(absolute_time: float = 0.000000, shake_scale: float = 0.000000, dynamic_scale: float = 0.000000, pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 90.000000, 90.000000, 1.000000, 512.000000, True, 0.000000, False, False, 0.000000, 2097152.000000, -1.000000, 1.333333, False, False, True, CameraProjectionMode.PERSPECTIVE, 0.000000, [], [0.000000, 0.000000], 1.000000, 1.000000]) -> None
unreal.CameraShakePatternScrubParams.absolute_time(value: float) -> None
unreal.CameraShakePatternScrubParams.dynamic_scale(value: float) -> None
unreal.CameraShakePatternScrubParams.pov(value: MinimalViewInfo) -> None
unreal.CameraShakePatternScrubParams.shake_scale(value: float) -> None
```

## `unreal.CameraShakePatternStartParams(StructBase)`

```python
unreal.CameraShakePatternStartParams.__init__(is_restarting: bool = False, override_duration: bool = False, duration_override: float = 0.000000) -> None
unreal.CameraShakePatternStartParams.duration_override(value: float) -> None
unreal.CameraShakePatternStartParams.is_restarting(value: bool) -> None
unreal.CameraShakePatternStartParams.override_duration(value: bool) -> None
```

## `unreal.CameraShakePatternStopParams(StructBase)`

```python
unreal.CameraShakePatternStopParams.__init__(immediately: bool = False) -> None
unreal.CameraShakePatternStopParams.immediately(value: bool) -> None
```

## `unreal.CameraShakePatternUpdateParams(StructBase)`

```python
unreal.CameraShakePatternUpdateParams.__init__(delta_time: float = 0.000000, shake_scale: float = 0.000000, dynamic_scale: float = 0.000000, pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 90.000000, 90.000000, 1.000000, 512.000000, True, 0.000000, False, False, 0.000000, 2097152.000000, -1.000000, 1.333333, False, False, True, CameraProjectionMode.PERSPECTIVE, 0.000000, [], [0.000000, 0.000000], 1.000000, 1.000000]) -> None
unreal.CameraShakePatternUpdateParams.delta_time(value: float) -> None
unreal.CameraShakePatternUpdateParams.dynamic_scale(value: float) -> None
unreal.CameraShakePatternUpdateParams.pov(value: MinimalViewInfo) -> None
unreal.CameraShakePatternUpdateParams.shake_scale(value: float) -> None
```

## `unreal.CameraShakePatternUpdateResult(StructBase)`

```python
unreal.CameraShakePatternUpdateResult.__init__() -> None
```

## `unreal.CameraShakeScrubParams(CameraShakePatternScrubParams)`

```python
unreal.CameraShakeScrubParams.__init__(absolute_time: float = 0.000000, shake_scale: float = 0.000000, dynamic_scale: float = 0.000000, pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 90.000000, 90.000000, 1.000000, 512.000000, True, 0.000000, False, False, 0.000000, 2097152.000000, -1.000000, 1.333333, False, False, True, CameraProjectionMode.PERSPECTIVE, 0.000000, [], [0.000000, 0.000000], 1.000000, 1.000000]) -> None
```

## `unreal.CameraShakeSourceComponent(SceneComponent)`

```python
unreal.CameraShakeSourceComponent.attenuation(value: CameraShakeAttenuation) -> None
unreal.CameraShakeSourceComponent.auto_start(value: bool) -> None
unreal.CameraShakeSourceComponent.b_auto_play(value: bool) -> None
unreal.CameraShakeSourceComponent.camera_shake(value: Class) -> None
unreal.CameraShakeSourceComponent.get_attenuation_factor(location: Vector) -> float
unreal.CameraShakeSourceComponent.inner_attenuation_radius(value: float) -> None
unreal.CameraShakeSourceComponent.outer_attenuation_radius(value: float) -> None
unreal.CameraShakeSourceComponent.play() -> None
unreal.CameraShakeSourceComponent.play_camera_shake(camera_shake: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.CameraShakeSourceComponent.start() -> None
unreal.CameraShakeSourceComponent.start_camera_shake(camera_shake: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.CameraShakeSourceComponent.stop_all_camera_shakes(immediately: bool = True) -> None
unreal.CameraShakeSourceComponent.stop_all_camera_shakes_of_type(camera_shake: Class, immediately: bool = True) -> None
```

## `unreal.CameraShakeStartParams(CameraShakePatternStartParams)`

```python
unreal.CameraShakeStartParams.__init__(is_restarting: bool = False, override_duration: bool = False, duration_override: float = 0.000000) -> None
```

## `unreal.CameraShakeStopParams(CameraShakePatternStopParams)`

```python
unreal.CameraShakeStopParams.__init__(immediately: bool = False) -> None
```

## `unreal.CameraShakeUpdateParams(CameraShakePatternUpdateParams)`

```python
unreal.CameraShakeUpdateParams.__init__(delta_time: float = 0.000000, shake_scale: float = 0.000000, dynamic_scale: float = 0.000000, pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 90.000000, 90.000000, 1.000000, 512.000000, True, 0.000000, False, False, 0.000000, 2097152.000000, -1.000000, 1.333333, False, False, True, CameraProjectionMode.PERSPECTIVE, 0.000000, [], [0.000000, 0.000000], 1.000000, 1.000000]) -> None
```

## `unreal.CameraShakeUpdateResult(CameraShakePatternUpdateResult)`

```python
unreal.CameraShakeUpdateResult.__init__() -> None
```

## `unreal.CameraStartAtom(EntityAtomBase)`

```python
unreal.CameraStartAtom.control_mode(value: str) -> None
unreal.CameraStartAtom.field_of_view(value: float) -> None
unreal.CameraStartAtom.location(value: Vector) -> None
unreal.CameraStartAtom.location_limit(value: Array[Vector2D]) -> None
unreal.CameraStartAtom.pitch_limit(value: Vector2D) -> None
unreal.CameraStartAtom.rotation(value: CameraPresetRotator) -> None
unreal.CameraStartAtom.view_distance_limit(value: Vector2D) -> None
unreal.CameraStartAtom.yaw_limit(value: Vector2D) -> None
```

## `unreal.CameraStepMoveParams(ParamsBase)`

```python
unreal.CameraStepMoveParams.__init__(move_direction: WDPDirection = WDPDirection.E_FORWARD, step: float = 0.000000, continuous: bool = False) -> None
unreal.CameraStepMoveParams.continuous() -> bool
unreal.CameraStepMoveParams.move_direction() -> WDPDirection
unreal.CameraStepMoveParams.step() -> float
```

## `unreal.CameraStepRotateParams(ParamsBase)`

```python
unreal.CameraStepRotateParams.__init__(rotate_direction: WdpCameraRotateDir = WdpCameraRotateDir.E_PITCH, step: float = 0.000000, continuous: bool = False) -> None
unreal.CameraStepRotateParams.continuous() -> bool
unreal.CameraStepRotateParams.rotate_direction() -> WdpCameraRotateDir
unreal.CameraStepRotateParams.step() -> float
```

## `unreal.CameraStepZoomParams(ParamsBase)`

```python
unreal.CameraStepZoomParams.__init__(step: float = 0.000000, continuous: bool = False) -> None
unreal.CameraStepZoomParams.continuous() -> bool
unreal.CameraStepZoomParams.step() -> float
```

## `unreal.CameraTrackingFocusSettings(StructBase)`

```python
unreal.CameraTrackingFocusSettings.__init__(actor_to_track: Actor = None, relative_offset: Vector = [0.000000, 0.000000, 0.000000], draw_debug_tracking_focus_point: bool = False) -> None
unreal.CameraTrackingFocusSettings.actor_to_track(value: Actor) -> None
unreal.CameraTrackingFocusSettings.draw_debug_tracking_focus_point(value: bool) -> None
unreal.CameraTrackingFocusSettings.relative_offset(value: Vector) -> None
```

## `unreal.CameraZoomLimitationData(StructBase)`

```python
unreal.CameraZoomLimitationData.__init__(min_zoom_distance: float = 0.000000, max_zoom_distance: float = 0.000000, min_fov: float = 0.000000, max_fov: float = 0.000000) -> None
unreal.CameraZoomLimitationData.max_fov(value: float) -> None
unreal.CameraZoomLimitationData.max_zoom_distance(value: float) -> None
unreal.CameraZoomLimitationData.min_fov(value: float) -> None
unreal.CameraZoomLimitationData.min_zoom_distance(value: float) -> None
```

## `unreal.CesiumCamera(StructBase)`

```python
unreal.CesiumCamera.__init__(viewport_size: Vector2D = [0.000000, 0.000000], location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], field_of_view_degrees: float = 0.000000, override_aspect_ratio: float = 0.000000) -> None
unreal.CesiumCamera.field_of_view_degrees(value: float) -> None
unreal.CesiumCamera.location(value: Vector) -> None
unreal.CesiumCamera.override_aspect_ratio(value: float) -> None
unreal.CesiumCamera.rotation(value: Rotator) -> None
unreal.CesiumCamera.viewport_size(value: Vector2D) -> None
```

## `unreal.CesiumCameraManager(Actor)`

```python
unreal.CesiumCameraManager.add_camera(camera: CesiumCamera) -> int
unreal.CesiumCameraManager.get_cameras() -> Map[int, CesiumCamera]
unreal.CesiumCameraManager.get_default_camera_manager(world_context_object: Object) -> CesiumCameraManager
unreal.CesiumCameraManager.remove_camera(camera_id: int) -> bool
unreal.CesiumCameraManager.update_camera(camera_id: int, camera: CesiumCamera) -> bool
```

## `unreal.Character(Pawn)`

```python
unreal.Character.cache_initial_mesh_offset(mesh_relative_location: Vector, mesh_relative_rotation: Rotator) -> None
unreal.Character.can_crouch() -> bool
unreal.Character.can_jump() -> bool
unreal.Character.can_jump_internal() -> bool
unreal.Character.capsule_component() -> CapsuleComponent
unreal.Character.character_movement() -> CharacterMovementComponent
unreal.Character.crouch(client_simulation: bool = False) -> None
unreal.Character.crouched_eye_height(value: float) -> None
unreal.Character.get_anim_root_motion_translation_scale() -> float
unreal.Character.get_base_rotation_offset() -> Rotator
unreal.Character.get_base_translation_offset() -> Vector
unreal.Character.get_current_montage() -> AnimMontage
unreal.Character.has_any_root_motion() -> bool
unreal.Character.is_crouched() -> bool
unreal.Character.is_jump_providing_force() -> bool
unreal.Character.is_jumping() -> bool
unreal.Character.is_playing_networked_root_motion_montage() -> bool
unreal.Character.is_playing_root_motion() -> bool
unreal.Character.jump() -> None
unreal.Character.jump_current_count() -> int
unreal.Character.jump_current_count_pre_jump() -> int
unreal.Character.jump_force_time_remaining() -> float
unreal.Character.jump_key_hold_time() -> float
unreal.Character.jump_max_count(value: int) -> None
unreal.Character.jump_max_hold_time(value: float) -> None
unreal.Character.landed_delegate(value: LandedSignature) -> None
unreal.Character.launch(launch_velocity: Vector, xy_override: bool, z_override: bool) -> None
unreal.Character.launch_character(launch_velocity: Vector, xy_override: bool, z_override: bool) -> None
unreal.Character.mesh() -> SkeletalMeshComponent
unreal.Character.movement_mode_changed_delegate(value: MovementModeChangedSignature) -> None
unreal.Character.on_character_movement_updated(value: CharacterMovementUpdatedSignature) -> None
unreal.Character.on_end_crouch(half_height_adjust: float, scaled_half_height_adjust: float) -> None
unreal.Character.on_jumped() -> None
unreal.Character.on_landed(hit: HitResult) -> None
unreal.Character.on_launched(launch_velocity: Vector, xy_override: bool, z_override: bool) -> None
unreal.Character.on_movement_mode_changed(prev_movement_mode: MovementMode, new_movement_mode: MovementMode, prev_custom_mode: int, new_custom_mode: int) -> None
unreal.Character.on_reached_jump_apex(value: CharacterReachedApexSignature) -> None
unreal.Character.on_start_crouch(half_height_adjust: float, scaled_half_height_adjust: float) -> None
unreal.Character.on_walking_off_ledge(previous_floor_impact_normal: Vector, previous_floor_contact_normal: Vector, previous_location: Vector, time_delta: float) -> None
unreal.Character.play_anim_montage(anim_montage: AnimMontage, play_rate: float = 1.000000, start_section_name: Name = "None") -> float
unreal.Character.pressed_jump() -> bool
unreal.Character.proxy_jump_force_started_time() -> float
unreal.Character.stop_anim_montage(anim_montage: AnimMontage = None) -> None
unreal.Character.stop_jumping() -> None
unreal.Character.un_crouch(client_simulation: bool = False) -> None
unreal.Character.update_custom_movement(delta_time: float) -> None
unreal.Character.was_jumping() -> bool
```

## `unreal.CharacterEvent(InputEvent)`

```python
unreal.CharacterEvent.__init__() -> None
```

## `unreal.CharacterMovementComponent(PawnMovementComponent)`

```python
unreal.CharacterMovementComponent.accel_rate(value: float) -> None
unreal.CharacterMovementComponent.add_force(force: Vector) -> None
unreal.CharacterMovementComponent.add_impulse(impulse: Vector, velocity_change: bool = False) -> None
unreal.CharacterMovementComponent.add_momentum(impulse: Vector, velocity_change: bool = False) -> None
unreal.CharacterMovementComponent.air_control(value: float) -> None
unreal.CharacterMovementComponent.air_control_boost_multiplier(value: float) -> None
unreal.CharacterMovementComponent.air_control_boost_velocity_threshold(value: float) -> None
unreal.CharacterMovementComponent.air_speed(value: float) -> None
unreal.CharacterMovementComponent.allow_physics_rotation_during_anim_root_motion(value: bool) -> None
unreal.CharacterMovementComponent.always_check_floor(value: bool) -> None
unreal.CharacterMovementComponent.apply_gravity_while_jumping(value: bool) -> None
unreal.CharacterMovementComponent.avoidance_consideration_radius() -> float
unreal.CharacterMovementComponent.avoidance_group() -> NavAvoidanceMask
unreal.CharacterMovementComponent.avoidance_uid() -> int
unreal.CharacterMovementComponent.avoidance_weight() -> float
unreal.CharacterMovementComponent.b_crouch_moves_character_down() -> bool
unreal.CharacterMovementComponent.b_orient_to_movement(value: bool) -> None
unreal.CharacterMovementComponent.base_on_attachment_root(value: bool) -> None
unreal.CharacterMovementComponent.based_movement_ignore_physics_base(value: bool) -> None
unreal.CharacterMovementComponent.braking_deceleration(value: float) -> None
unreal.CharacterMovementComponent.braking_deceleration_falling(value: float) -> None
unreal.CharacterMovementComponent.braking_deceleration_flying(value: float) -> None
unreal.CharacterMovementComponent.braking_deceleration_swimming(value: float) -> None
unreal.CharacterMovementComponent.braking_deceleration_walking(value: float) -> None
unreal.CharacterMovementComponent.braking_friction(value: float) -> None
unreal.CharacterMovementComponent.braking_friction_factor(value: float) -> None
unreal.CharacterMovementComponent.braking_sub_step_time(value: float) -> None
unreal.CharacterMovementComponent.buoyancy(value: float) -> None
unreal.CharacterMovementComponent.calc_velocity(delta_time: float, friction: float, fluid: bool, braking_deceleration: float) -> None
unreal.CharacterMovementComponent.can_walk_off_ledges(value: bool) -> None
unreal.CharacterMovementComponent.can_walk_off_ledges_when_crouching(value: bool) -> None
unreal.CharacterMovementComponent.clear_accumulated_forces() -> None
unreal.CharacterMovementComponent.compute_floor_distance(capsule_location: Vector, line_distance: float, sweep_distance: float, sweep_radius: float) -> FindFloorResult
unreal.CharacterMovementComponent.crouch_height(value: float) -> None
unreal.CharacterMovementComponent.crouch_maintains_base_location() -> bool
unreal.CharacterMovementComponent.crouched_half_height(value: float) -> None
unreal.CharacterMovementComponent.current_floor() -> FindFloorResult
unreal.CharacterMovementComponent.custom_movement_mode() -> int
unreal.CharacterMovementComponent.default_land_movement_mode(value: MovementMode) -> None
unreal.CharacterMovementComponent.default_water_movement_mode(value: MovementMode) -> None
unreal.CharacterMovementComponent.disable_movement() -> None
unreal.CharacterMovementComponent.dont_fall_below_jump_z_velocity_during_jump(value: bool) -> None
unreal.CharacterMovementComponent.enable_physics_interaction(value: bool) -> None
unreal.CharacterMovementComponent.falling_lateral_friction(value: float) -> None
unreal.CharacterMovementComponent.find_floor(capsule_location: Vector) -> FindFloorResult
unreal.CharacterMovementComponent.force_next_floor_check() -> bool
unreal.CharacterMovementComponent.former_base_velocity_decay_half_life(value: float) -> None
unreal.CharacterMovementComponent.get_analog_input_modifier() -> float
unreal.CharacterMovementComponent.get_character_owner() -> Character
unreal.CharacterMovementComponent.get_current_acceleration() -> Vector
unreal.CharacterMovementComponent.get_gravity_direction() -> Vector
unreal.CharacterMovementComponent.get_imparted_movement_base_velocity() -> Vector
unreal.CharacterMovementComponent.get_last_update_location() -> Vector
unreal.CharacterMovementComponent.get_last_update_requested_velocity() -> Vector
unreal.CharacterMovementComponent.get_last_update_rotation() -> Rotator
unreal.CharacterMovementComponent.get_last_update_velocity() -> Vector
unreal.CharacterMovementComponent.get_max_acceleration() -> float
unreal.CharacterMovementComponent.get_max_braking_deceleration() -> float
unreal.CharacterMovementComponent.get_max_jump_height() -> float
unreal.CharacterMovementComponent.get_max_jump_height_with_jump_time() -> float
unreal.CharacterMovementComponent.get_min_analog_speed() -> float
unreal.CharacterMovementComponent.get_movement_base() -> PrimitiveComponent
unreal.CharacterMovementComponent.get_perch_radius_threshold() -> float
unreal.CharacterMovementComponent.get_valid_perch_radius() -> float
unreal.CharacterMovementComponent.get_walkable_floor_angle() -> float
unreal.CharacterMovementComponent.get_walkable_floor_z() -> float
unreal.CharacterMovementComponent.gravity_direction() -> Vector
unreal.CharacterMovementComponent.gravity_scale(value: float) -> None
unreal.CharacterMovementComponent.gravity_to_world_transform() -> Quat
unreal.CharacterMovementComponent.ground_friction(value: float) -> None
unreal.CharacterMovementComponent.ground_speed(value: float) -> None
unreal.CharacterMovementComponent.groups_to_avoid() -> NavAvoidanceMask
unreal.CharacterMovementComponent.groups_to_ignore() -> NavAvoidanceMask
unreal.CharacterMovementComponent.has_custom_gravity() -> bool
unreal.CharacterMovementComponent.ignore_base_rotation(value: bool) -> None
unreal.CharacterMovementComponent.ignore_client_movement_error_checks_and_correction(value: bool) -> None
unreal.CharacterMovementComponent.impart_base_angular_velocity(value: bool) -> None
unreal.CharacterMovementComponent.impart_base_velocity_x(value: bool) -> None
unreal.CharacterMovementComponent.impart_base_velocity_y(value: bool) -> None
unreal.CharacterMovementComponent.impart_base_velocity_z(value: bool) -> None
unreal.CharacterMovementComponent.initial_push_force_factor(value: float) -> None
unreal.CharacterMovementComponent.is_walkable(hit: HitResult) -> bool
unreal.CharacterMovementComponent.is_walking() -> bool
unreal.CharacterMovementComponent.jump_off_jump_z_factor(value: float) -> None
unreal.CharacterMovementComponent.jump_out_of_water_pitch(value: float) -> None
unreal.CharacterMovementComponent.jump_z(value: float) -> None
unreal.CharacterMovementComponent.jump_z_velocity(value: float) -> None
unreal.CharacterMovementComponent.just_teleported() -> bool
unreal.CharacterMovementComponent.ledge_check_threshold(value: float) -> None
unreal.CharacterMovementComponent.maintain_horizontal_ground_velocity(value: bool) -> None
unreal.CharacterMovementComponent.mass(value: float) -> None
unreal.CharacterMovementComponent.max_acceleration(value: float) -> None
unreal.CharacterMovementComponent.max_custom_movement_speed(value: float) -> None
unreal.CharacterMovementComponent.max_depenetration_with_geometry(value: float) -> None
unreal.CharacterMovementComponent.max_depenetration_with_geometry_as_proxy(value: float) -> None
unreal.CharacterMovementComponent.max_depenetration_with_pawn(value: float) -> None
unreal.CharacterMovementComponent.max_depenetration_with_pawn_as_proxy(value: float) -> None
unreal.CharacterMovementComponent.max_fly_speed(value: float) -> None
unreal.CharacterMovementComponent.max_jump_apex_attempts_per_simulation(value: int) -> None
unreal.CharacterMovementComponent.max_out_of_water_step_height(value: float) -> None
unreal.CharacterMovementComponent.max_simulation_iterations(value: int) -> None
unreal.CharacterMovementComponent.max_simulation_time_step(value: float) -> None
unreal.CharacterMovementComponent.max_step_height(value: float) -> None
unreal.CharacterMovementComponent.max_swim_speed(value: float) -> None
unreal.CharacterMovementComponent.max_touch_force(value: float) -> None
unreal.CharacterMovementComponent.max_walk_speed(value: float) -> None
unreal.CharacterMovementComponent.max_walk_speed_crouched(value: float) -> None
unreal.CharacterMovementComponent.min_analog_walk_speed(value: float) -> None
unreal.CharacterMovementComponent.min_touch_force(value: float) -> None
unreal.CharacterMovementComponent.movement_mode() -> MovementMode
unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_down(value: float) -> None
unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_up(value: float) -> None
unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_down(value: float) -> None
unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_up(value: float) -> None
unreal.CharacterMovementComponent.nav_mesh_projection_interp_speed(value: float) -> None
unreal.CharacterMovementComponent.nav_mesh_projection_interval(value: float) -> None
unreal.CharacterMovementComponent.nav_walking_floor_dist_tolerance(value: float) -> None
unreal.CharacterMovementComponent.network_smoothing_mode() -> NetworkSmoothingMode
unreal.CharacterMovementComponent.notify_apex() -> bool
unreal.CharacterMovementComponent.orient_rotation_to_movement(value: bool) -> None
unreal.CharacterMovementComponent.outof_water_z(value: float) -> None
unreal.CharacterMovementComponent.perch_additional_height(value: float) -> None
unreal.CharacterMovementComponent.perch_radius_threshold(value: float) -> None
unreal.CharacterMovementComponent.project_nav_mesh_on_both_world_channels() -> bool
unreal.CharacterMovementComponent.project_nav_mesh_walking() -> bool
unreal.CharacterMovementComponent.push_force_factor(value: float) -> None
unreal.CharacterMovementComponent.push_force_point_z_offset_factor(value: float) -> None
unreal.CharacterMovementComponent.push_force_scaled_to_mass(value: bool) -> None
unreal.CharacterMovementComponent.push_force_using_z_offset(value: bool) -> None
unreal.CharacterMovementComponent.repulsion_force(value: float) -> None
unreal.CharacterMovementComponent.requested_move_use_acceleration(value: bool) -> None
unreal.CharacterMovementComponent.rotation_rate(value: Rotator) -> None
unreal.CharacterMovementComponent.run_physics_with_no_controller(value: bool) -> None
unreal.CharacterMovementComponent.scale_push_force_to_velocity(value: bool) -> None
unreal.CharacterMovementComponent.server_accept_client_authoritative_position(value: bool) -> None
unreal.CharacterMovementComponent.set_avoidance_enabled(enable: bool) -> None
unreal.CharacterMovementComponent.set_avoidance_group(group_flags: int) -> None
unreal.CharacterMovementComponent.set_avoidance_group_mask(group_mask: NavAvoidanceMask) -> None
unreal.CharacterMovementComponent.set_gravity_direction(gravity_dir: Vector) -> None
unreal.CharacterMovementComponent.set_groups_to_avoid(group_flags: int) -> None
unreal.CharacterMovementComponent.set_groups_to_avoid_mask(group_mask: NavAvoidanceMask) -> None
unreal.CharacterMovementComponent.set_groups_to_ignore(group_flags: int) -> None
unreal.CharacterMovementComponent.set_groups_to_ignore_mask(group_mask: NavAvoidanceMask) -> None
unreal.CharacterMovementComponent.set_movement_mode(new_movement_mode: MovementMode, new_custom_mode: int = 0) -> None
unreal.CharacterMovementComponent.set_walkable_floor_angle(walkable_floor_angle: float) -> None
unreal.CharacterMovementComponent.set_walkable_floor_z(walkable_floor_z: float) -> None
unreal.CharacterMovementComponent.standing_downward_force_scale(value: float) -> None
unreal.CharacterMovementComponent.stay_based_in_air(value: bool) -> None
unreal.CharacterMovementComponent.stay_based_in_air_height(value: float) -> None
unreal.CharacterMovementComponent.sweep_while_nav_walking(value: bool) -> None
unreal.CharacterMovementComponent.touch_force_factor(value: float) -> None
unreal.CharacterMovementComponent.touch_force_scaled_to_mass(value: bool) -> None
unreal.CharacterMovementComponent.use_controller_desired_rotation(value: bool) -> None
unreal.CharacterMovementComponent.use_flat_base_for_floor_checks(value: bool) -> None
unreal.CharacterMovementComponent.use_rvo_avoidance() -> bool
unreal.CharacterMovementComponent.use_separate_braking_friction(value: bool) -> None
unreal.CharacterMovementComponent.wants_to_crouch() -> bool
unreal.CharacterMovementComponent.water_speed(value: float) -> None
unreal.CharacterMovementComponent.world_to_gravity_transform() -> Quat
```

## `unreal.CharacterMovementUpdatedSignature(MulticastDelegateBase)`

```python
unreal.CharacterMovementUpdatedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CharacterReachedApexSignature(MulticastDelegateBase)`

```python
unreal.CharacterReachedApexSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CineCameraComponent(CameraComponent)`

```python
unreal.CineCameraComponent.crop_settings(value: PlateCropSettings) -> None
unreal.CineCameraComponent.current_aperture(value: float) -> None
unreal.CineCameraComponent.current_focal_length(value: float) -> None
unreal.CineCameraComponent.current_focus_distance() -> float
unreal.CineCameraComponent.custom_near_clipping_plane(value: float) -> None
unreal.CineCameraComponent.filmback(value: CameraFilmbackSettings) -> None
unreal.CineCameraComponent.focus_settings(value: CameraFocusSettings) -> None
unreal.CineCameraComponent.get_crop_preset_name() -> str
unreal.CineCameraComponent.get_default_filmback_preset_name() -> str
unreal.CineCameraComponent.get_filmback_preset_name() -> str
unreal.CineCameraComponent.get_filmback_presets_copy() -> Array[NamedFilmbackPreset]
unreal.CineCameraComponent.get_horizontal_field_of_view() -> float
unreal.CineCameraComponent.get_horizontal_projection_offset() -> float
unreal.CineCameraComponent.get_lens_preset_name() -> str
unreal.CineCameraComponent.get_lens_presets_copy() -> Array[NamedLensPreset]
unreal.CineCameraComponent.get_vertical_field_of_view() -> float
unreal.CineCameraComponent.get_vertical_projection_offset() -> float
unreal.CineCameraComponent.lens_settings(value: CameraLensSettings) -> None
unreal.CineCameraComponent.override_custom_near_clipping_plane(value: bool) -> None
unreal.CineCameraComponent.set_crop_preset_by_name(preset_name: str) -> None
unreal.CineCameraComponent.set_filmback_preset_by_name(preset_name: str) -> None
unreal.CineCameraComponent.set_lens_preset_by_name(preset_name: str) -> None
```

## `unreal.CineCameraSettings(DeveloperSettings)`

```python
unreal.CineCameraSettings.crop_presets(value: Array[NamedPlateCropPreset]) -> None
unreal.CineCameraSettings.default_crop_preset_name(value: str) -> None
unreal.CineCameraSettings.default_filmback_preset(value: str) -> None
unreal.CineCameraSettings.default_lens_f_stop(value: float) -> None
unreal.CineCameraSettings.default_lens_focal_length(value: float) -> None
unreal.CineCameraSettings.default_lens_preset_name(value: str) -> None
unreal.CineCameraSettings.filmback_presets(value: Array[NamedFilmbackPreset]) -> None
unreal.CineCameraSettings.get_cine_camera_settings() -> CineCameraSettings
unreal.CineCameraSettings.get_crop_preset_by_name(preset_name: str) -> Optional[PlateCropSettings]
unreal.CineCameraSettings.get_filmback_preset_by_name(preset_name: str) -> Optional[CameraFilmbackSettings]
unreal.CineCameraSettings.get_lens_preset_by_name(preset_name: str) -> Optional[CameraLensSettings]
unreal.CineCameraSettings.lens_presets(value: Array[NamedLensPreset]) -> None
```

## `unreal.ColorInputDeviceProperty(InputDeviceProperty)`

```python
unreal.ColorInputDeviceProperty.color_data(value: DeviceColorData) -> None
unreal.ColorInputDeviceProperty.device_override_data(value: Map[Name, DeviceColorData]) -> None
```

## `unreal.ComponentOnInputTouchBeginSignature(MulticastDelegateBase)`

```python
unreal.ComponentOnInputTouchBeginSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ComponentOnInputTouchEndSignature(MulticastDelegateBase)`

```python
unreal.ComponentOnInputTouchEndSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Controller(Actor)`

```python
unreal.Controller.get_control_rotation() -> Rotator
unreal.Controller.get_controlled_pawn() -> Pawn
unreal.Controller.get_desired_rotation() -> Rotator
unreal.Controller.get_player_view_point() -> Tuple[Vector, Rotator]
unreal.Controller.get_view_target() -> Actor
unreal.Controller.is_local_controller() -> bool
unreal.Controller.is_local_player_controller() -> bool
unreal.Controller.is_look_input_ignored() -> bool
unreal.Controller.is_move_input_ignored() -> bool
unreal.Controller.is_player_controller() -> bool
unreal.Controller.line_of_sight_to(other: Actor, view_point: Vector = [0.000000, 0.000000, 0.000000], alternate_checks: bool = False) -> bool
unreal.Controller.on_instigated_any_damage(value: InstigatedAnyDamageSignature) -> None
unreal.Controller.on_possess(possessed_pawn: Pawn) -> None
unreal.Controller.on_possessed_pawn_changed(value: OnPossessedPawnChanged) -> None
unreal.Controller.on_un_possess(unpossessed_pawn: Pawn) -> None
unreal.Controller.player_replication_info() -> PlayerState
unreal.Controller.player_state() -> PlayerState
unreal.Controller.possess(pawn: Pawn) -> None
unreal.Controller.receive_instigated_any_damage(damage: float, damage_type: DamageType, damaged_actor: Actor, damage_causer: Actor) -> None
unreal.Controller.receive_possess(possessed_pawn: Pawn) -> None
unreal.Controller.receive_un_possess(unpossessed_pawn: Pawn) -> None
unreal.Controller.reset_ignore_input_flags() -> None
unreal.Controller.reset_ignore_look_input() -> None
unreal.Controller.reset_ignore_move_input() -> None
unreal.Controller.set_control_rotation(new_rotation: Rotator) -> None
unreal.Controller.set_ignore_look_input(new_look_input: bool) -> None
unreal.Controller.set_ignore_move_input(new_move_input: bool) -> None
unreal.Controller.set_initial_location_and_rotation(new_location: Vector, new_rotation: Rotator) -> None
unreal.Controller.stop_movement() -> None
unreal.Controller.un_possess() -> None
```

## `unreal.CoreCameraData(StructBase)`

```python
unreal.CoreCameraData.__init__(camera_location: Vector = [0.000000, 0.000000, 0.000000], camera_rotation: Rotator = [0.000000, 0.000000, 0.000000], fov: float = 0.000000, pivot: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.CoreCameraData.camera_location(value: Vector) -> None
unreal.CoreCameraData.camera_rotation(value: Rotator) -> None
unreal.CoreCameraData.fov(value: float) -> None
unreal.CoreCameraData.pivot(value: Vector) -> None
```

## `unreal.CustomInput(StructBase)`

```python
unreal.CustomInput.__init__() -> None
```

## `unreal.CustomLocalPlayer(LocalPlayer)`

```python
unreal.CustomLocalPlayer.enable_multi_views(value: bool) -> None
unreal.CustomLocalPlayer.get_max_num_of_views() -> int
unreal.CustomLocalPlayer.views_manager(value: ViewportsManager) -> None
```

## `unreal.DCPFocusCameraParams(StructBase)`

```python
unreal.DCPFocusCameraParams.__init__(rotation: CameraPresetRotator = [0.000000, 0.000000], distance_factor: float = 0.000000, fly_time: float = 0.000000) -> None
unreal.DCPFocusCameraParams.distance_factor(value: float) -> None
unreal.DCPFocusCameraParams.fly_time(value: float) -> None
unreal.DCPFocusCameraParams.rotation(value: CameraPresetRotator) -> None
```

## `unreal.DebugCameraController(PlayerController)`

```python
unreal.DebugCameraController.get_selected_actor() -> Actor
unreal.DebugCameraController.initial_accel() -> float
unreal.DebugCameraController.initial_decel() -> float
unreal.DebugCameraController.initial_max_speed() -> float
unreal.DebugCameraController.receive_on_activate(original_pc: PlayerController) -> None
unreal.DebugCameraController.receive_on_actor_selected(new_selected_actor: Actor, select_hit_location: Vector, select_hit_normal: Vector, hit: HitResult) -> None
unreal.DebugCameraController.receive_on_deactivate(restored_pc: PlayerController) -> None
unreal.DebugCameraController.set_pawn_movement_speed_scale(new_speed_scale: float) -> None
unreal.DebugCameraController.speed_scale() -> float
unreal.DebugCameraController.toggle_display() -> None
```

## `unreal.DefaultPawn(Pawn)`

```python
unreal.DefaultPawn.add_default_movement_bindings() -> bool
unreal.DefaultPawn.base_look_up_rate() -> float
unreal.DefaultPawn.base_turn_rate() -> float
unreal.DefaultPawn.collision_component() -> SphereComponent
unreal.DefaultPawn.default_pawn_movement() -> PawnMovementComponent
unreal.DefaultPawn.look_up_at_rate(rate: float) -> None
unreal.DefaultPawn.mesh_component() -> StaticMeshComponent
unreal.DefaultPawn.move_forward(val: float) -> None
unreal.DefaultPawn.move_right(val: float) -> None
unreal.DefaultPawn.move_up_world(val: float) -> None
unreal.DefaultPawn.movement_component() -> PawnMovementComponent
unreal.DefaultPawn.turn_at_rate(rate: float) -> None
```

## `unreal.EarthCameraComponent(CameraComponent)`

```python
unreal.EarthCameraComponent.flying(value: bool) -> None
unreal.EarthCameraComponent.reset_state() -> None
unreal.EarthCameraComponent.stop_fly() -> None
unreal.EarthCameraComponent.turn_rate(axis_value: float) -> None
```

## `unreal.EarthControlEnhancedInput(Object)`

```python
unreal.EarthControlEnhancedInput.look_up_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.mapping_context(value: InputMappingContext) -> None
unreal.EarthControlEnhancedInput.move_forward_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.move_right_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.move_up_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.pan_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.rotate_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.turn_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.zoom_in_action(value: InputAction) -> None
unreal.EarthControlEnhancedInput.zoom_out_action(value: InputAction) -> None
```

## `unreal.EarthInputCollection(StructBase)`

```python
unreal.EarthInputCollection.__init__(instanced_entities: Array[InstancedStruct] = [], owned_component: ActorComponent = None) -> None
unreal.EarthInputCollection.instanced_entities(value: Array[InstancedStruct]) -> None
unreal.EarthInputCollection.owned_component(value: ActorComponent) -> None
```

## `unreal.EarthInputProviderBase(Object)`

```python
unreal.EarthInputProviderBase.execute_generate_input_collection(world_context_object: Object) -> EarthInputCollection
unreal.EarthInputProviderBase.generate_input_collection(world_context_object: Object) -> EarthInputCollection
unreal.EarthInputProviderBase.global_prefab(value: EarthPrefabBase) -> None
unreal.EarthInputProviderBase.pre_generate_input_collection(world_context_object: Object) -> EarthInputCollection
```

## `unreal.EarthInputProvider_TWE(EarthInputProviderBase)`

```python
unreal.EarthInputProvider_TWE.base_level(value: int) -> None
unreal.EarthInputProvider_TWE.data_source_path(value: FilePath) -> None
unreal.EarthInputProvider_TWE.geo_referencing_system(value: EarthGeoReferencingSystem) -> None
unreal.EarthInputProvider_TWE.layer_type(value: LayerType) -> None
unreal.EarthInputProvider_TWE.quad_key(value: str) -> None
```

## `unreal.EmitterCameraLensEffectBase(Emitter)`

```python
unreal.EmitterCameraLensEffectBase.get_particle_components() -> Array[FXSystemComponent]
unreal.EmitterCameraLensEffectBase.get_primary_particle_component() -> FXSystemComponent
```

## `unreal.EnhancedInputActionHandlerDynamicSignature(DelegateBase)`

```python
unreal.EnhancedInputActionHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EnhancedInputLibrary(BlueprintFunctionLibrary)`

```python
unreal.EnhancedInputLibrary.conv_input_action_value_to_string(action_value: InputActionValue) -> str
unreal.EnhancedInputLibrary.conv_trigger_event_value_to_string(trigger_event: TriggerEvent) -> str
unreal.EnhancedInputLibrary.flush_player_input(player_controller: PlayerController) -> None
unreal.EnhancedInputLibrary.get_first_player_mappable_key_slot() -> PlayerMappableKeySlotData
unreal.EnhancedInputLibrary.get_fourth_player_mappable_key_slot() -> PlayerMappableKeySlotData
unreal.EnhancedInputLibrary.get_mapping_name(action_key_mapping: EnhancedActionKeyMapping) -> Name
unreal.EnhancedInputLibrary.get_player_mappable_key_settings(action_key_mapping: EnhancedActionKeyMapping) -> PlayerMappableKeySettings
unreal.EnhancedInputLibrary.get_second_player_mappable_key_slot() -> PlayerMappableKeySlotData
unreal.EnhancedInputLibrary.get_third_player_mappable_key_slot() -> PlayerMappableKeySlotData
unreal.EnhancedInputLibrary.is_action_key_mapping_player_mappable(action_key_mapping: EnhancedActionKeyMapping) -> bool
unreal.EnhancedInputLibrary.request_rebuild_control_mappings_using_context(context: InputMappingContext, force_immediately: bool = False) -> None
```

## `unreal.EnhancedInputPlatformData(Object)`

```python
unreal.EnhancedInputPlatformData.get_context_redirect(context: InputMappingContext) -> InputMappingContext
unreal.EnhancedInputPlatformData.mapping_context_redirects() -> Map[InputMappingContext, InputMappingContext]
```

## `unreal.EnhancedInputUserSettings(SaveGame)`

```python
unreal.EnhancedInputUserSettings.apply_settings() -> None
unreal.EnhancedInputUserSettings.async_save_settings() -> None
unreal.EnhancedInputUserSettings.create_new_key_profile(args: PlayerMappableKeyProfileCreationArgs) -> EnhancedPlayerMappableKeyProfile
unreal.EnhancedInputUserSettings.find_mappings_in_row(mapping_name: Name) -> Set[PlayerKeyMapping]
unreal.EnhancedInputUserSettings.get_current_key_profile() -> EnhancedPlayerMappableKeyProfile
unreal.EnhancedInputUserSettings.get_current_key_profile_identifier() -> GameplayTag
unreal.EnhancedInputUserSettings.get_key_profile_with_identifier(profile_id: GameplayTag) -> EnhancedPlayerMappableKeyProfile
unreal.EnhancedInputUserSettings.is_mapping_context_registered(imc: InputMappingContext) -> bool
unreal.EnhancedInputUserSettings.map_player_key(args: MapPlayerKeyArgs) -> GameplayTagContainer
unreal.EnhancedInputUserSettings.on_settings_applied(value: EnhancedInputUserSettingsApplied) -> None
unreal.EnhancedInputUserSettings.on_settings_changed(value: EnhancedInputUserSettingsChanged) -> None
unreal.EnhancedInputUserSettings.register_input_mapping_context(imc: InputMappingContext) -> bool
unreal.EnhancedInputUserSettings.register_input_mapping_contexts(mapping_contexts: Set[InputMappingContext]) -> bool
unreal.EnhancedInputUserSettings.reset_all_player_keys_in_row(args: MapPlayerKeyArgs) -> GameplayTagContainer
unreal.EnhancedInputUserSettings.reset_key_profile_to_default(profile_id: GameplayTag) -> GameplayTagContainer
unreal.EnhancedInputUserSettings.save_settings() -> None
unreal.EnhancedInputUserSettings.set_key_profile(profile_id: GameplayTag) -> bool
unreal.EnhancedInputUserSettings.un_map_player_key(args: MapPlayerKeyArgs) -> GameplayTagContainer
unreal.EnhancedInputUserSettings.unregister_input_mapping_context(imc: InputMappingContext) -> bool
unreal.EnhancedInputUserSettings.unregister_input_mapping_contexts(mapping_contexts: Set[InputMappingContext]) -> bool
```

## `unreal.EnhancedInputUserSettings_EnhancedInputUserSettingsApplied(MulticastDelegateBase)`

```python
unreal.EnhancedInputUserSettings_EnhancedInputUserSettingsApplied.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EnhancedInputUserSettings_EnhancedInputUserSettingsChanged(MulticastDelegateBase)`

```python
unreal.EnhancedInputUserSettings_EnhancedInputUserSettingsChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EnhancedInputUserSettings_MappableKeyProfileChanged(MulticastDelegateBase)`

```python
unreal.EnhancedInputUserSettings_MappableKeyProfileChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.EnhancedPlayerMappableKeyProfile(Object)`

```python
unreal.EnhancedPlayerMappableKeyProfile.display_name(value: Text) -> None
unreal.EnhancedPlayerMappableKeyProfile.does_mapping_pass_query_options(player_mapping: PlayerKeyMapping, options: PlayerMappableKeyQueryOptions) -> bool
unreal.EnhancedPlayerMappableKeyProfile.dump_profile_to_log() -> None
unreal.EnhancedPlayerMappableKeyProfile.get_mapped_keys_in_row(mapping_name: Name) -> Tuple[int, Array[Key]]
unreal.EnhancedPlayerMappableKeyProfile.get_mapping_names_for_key(key: Key) -> Tuple[int, Array[Name]]
unreal.EnhancedPlayerMappableKeyProfile.get_player_mapping_rows() -> Map[Name, KeyMappingRow]
unreal.EnhancedPlayerMappableKeyProfile.get_profile_display_name() -> Text
unreal.EnhancedPlayerMappableKeyProfile.get_profile_identifer() -> GameplayTag
unreal.EnhancedPlayerMappableKeyProfile.k2_find_key_mapping(args: MapPlayerKeyArgs) -> PlayerKeyMapping
unreal.EnhancedPlayerMappableKeyProfile.owning_user_id() -> PlatformUserId
unreal.EnhancedPlayerMappableKeyProfile.player_mapped_keys() -> Map[Name, KeyMappingRow]
unreal.EnhancedPlayerMappableKeyProfile.profile_identifier() -> GameplayTag
unreal.EnhancedPlayerMappableKeyProfile.query_player_mapped_keys(options: PlayerMappableKeyQueryOptions) -> Tuple[int, Array[Key]]
unreal.EnhancedPlayerMappableKeyProfile.reset_mapping_to_default(mapping_name: Name) -> None
unreal.EnhancedPlayerMappableKeyProfile.reset_to_default() -> None
unreal.EnhancedPlayerMappableKeyProfile.set_display_name(new_display_name: Text) -> None
unreal.EnhancedPlayerMappableKeyProfile.to_string() -> str
```

## `unreal.FXSystemSpawnParameters(StructBase)`

```python
unreal.FXSystemSpawnParameters.__init__(world_context_object: Object = None, system_template: FXSystemAsset = None, location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000], attach_to_component: SceneComponent = None, attach_point_name: Name = "None", location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET, auto_destroy: bool = False, auto_activate: bool = False, pooling_method: PSCPoolMethod = PSCPoolMethod.NONE, pre_cull_check: bool = False, is_player_effect: bool = False) -> None
unreal.FXSystemSpawnParameters.attach_point_name(value: Name) -> None
unreal.FXSystemSpawnParameters.attach_to_component(value: SceneComponent) -> None
unreal.FXSystemSpawnParameters.auto_activate(value: bool) -> None
unreal.FXSystemSpawnParameters.auto_destroy(value: bool) -> None
unreal.FXSystemSpawnParameters.is_player_effect(value: bool) -> None
unreal.FXSystemSpawnParameters.location(value: Vector) -> None
unreal.FXSystemSpawnParameters.location_type(value: AttachLocation) -> None
unreal.FXSystemSpawnParameters.pooling_method(value: PSCPoolMethod) -> None
unreal.FXSystemSpawnParameters.pre_cull_check(value: bool) -> None
unreal.FXSystemSpawnParameters.rotation(value: Rotator) -> None
unreal.FXSystemSpawnParameters.scale(value: Vector) -> None
unreal.FXSystemSpawnParameters.system_template(value: FXSystemAsset) -> None
unreal.FXSystemSpawnParameters.world_context_object(value: Object) -> None
```

## `unreal.FloatingPawnMovement(PawnMovementComponent)`

```python
unreal.FloatingPawnMovement.accel_rate(value: float) -> None
unreal.FloatingPawnMovement.acceleration(value: float) -> None
unreal.FloatingPawnMovement.decel_rate(value: float) -> None
unreal.FloatingPawnMovement.deceleration(value: float) -> None
unreal.FloatingPawnMovement.max_speed(value: float) -> None
unreal.FloatingPawnMovement.turning_boost(value: float) -> None
```

## `unreal.FollowCameraSettings(StructBase)`

```python
unreal.FollowCameraSettings.__init__(pivot_location: Vector = [0.000000, 0.000000, 0.000000], default_rotation: Rotator = [0.000000, 0.000000, 0.000000], use_relative_rotation: bool = False, rotation_lag_speed: float = 0.000000, default_distance: float = 0.000000, distance_limit: Vector2D = [0.000000, 0.000000], default_fov: float = 0.000000, auto_resore_time: float = 0.000000) -> None
unreal.FollowCameraSettings.auto_resore_time(value: float) -> None
unreal.FollowCameraSettings.default_distance(value: float) -> None
unreal.FollowCameraSettings.default_fov(value: float) -> None
unreal.FollowCameraSettings.default_rotation(value: Rotator) -> None
unreal.FollowCameraSettings.distance_limit(value: Vector2D) -> None
unreal.FollowCameraSettings.pivot_location(value: Vector) -> None
unreal.FollowCameraSettings.rotation_lag_speed(value: float) -> None
unreal.FollowCameraSettings.use_relative_rotation(value: bool) -> None
```

## `unreal.FontCharacter(StructBase)`

```python
unreal.FontCharacter.__init__() -> None
```

## `unreal.FunctionalTestAISpawned(MulticastDelegateBase)`

```python
unreal.FunctionalTestAISpawned.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GameplayCameraComponent(SceneComponent)`

```python
unreal.GameplayCameraComponent.activate_camera_for_player_controller(player_controller: PlayerController) -> None
unreal.GameplayCameraComponent.activate_camera_for_player_index(player_index: int) -> None
unreal.GameplayCameraComponent.auto_activate_for_player(value: AutoReceiveInput) -> None
unreal.GameplayCameraComponent.camera(value: CameraAsset) -> None
unreal.GameplayCameraComponent.deactivate_camera() -> None
unreal.GameplayCameraComponent.get_initial_pose() -> BlueprintCameraPose
unreal.GameplayCameraComponent.get_initial_variable_table() -> BlueprintCameraVariableTable
unreal.GameplayCameraComponent.set_initial_pose(camera_pose: BlueprintCameraPose) -> None
```

## `unreal.GameplayCameraSystemComponent(SceneComponent)`

```python
unreal.GameplayCameraSystemComponent.activate_camera_system_for_player_controller(player_controller: PlayerController) -> None
unreal.GameplayCameraSystemComponent.activate_camera_system_for_player_index(player_index: int) -> None
unreal.GameplayCameraSystemComponent.auto_activate_for_player(value: AutoReceiveInput) -> None
unreal.GameplayCameraSystemComponent.deactivate_camera_system(next_view_target: Actor = None) -> None
unreal.GameplayCameraSystemComponent.is_camera_system_active_for_play_controller(player_controller: PlayerController) -> bool
unreal.GameplayCameraSystemComponent.set_player_controller_rotation(value: bool) -> None
```

## `unreal.GameplayCueNotify_CameraLensEffectInfo(StructBase)`

```python
unreal.GameplayCueNotify_CameraLensEffectInfo.__init__(spawn_condition_override: GameplayCueNotify_SpawnCondition = [GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR, GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []], placement_info_override: GameplayCueNotify_PlacementInfo = ["None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH, AttachmentRule.KEEP_WORLD, False, True, [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], camera_lens_effect: Class = None, override_spawn_condition: bool = False, override_placement_info: bool = False, play_in_world: bool = False, world_inner_radius: float = 0.000000, world_outer_radius: float = 0.000000) -> None
unreal.GameplayCueNotify_CameraLensEffectInfo.camera_lens_effect() -> Class
unreal.GameplayCueNotify_CameraLensEffectInfo.override_placement_info() -> bool
unreal.GameplayCueNotify_CameraLensEffectInfo.override_spawn_condition() -> bool
unreal.GameplayCueNotify_CameraLensEffectInfo.placement_info_override() -> GameplayCueNotify_PlacementInfo
unreal.GameplayCueNotify_CameraLensEffectInfo.play_in_world() -> bool
unreal.GameplayCueNotify_CameraLensEffectInfo.spawn_condition_override() -> GameplayCueNotify_SpawnCondition
unreal.GameplayCueNotify_CameraLensEffectInfo.world_inner_radius() -> float
unreal.GameplayCueNotify_CameraLensEffectInfo.world_outer_radius() -> float
```

## `unreal.GameplayCueNotify_CameraShakeInfo(StructBase)`

```python
unreal.GameplayCueNotify_CameraShakeInfo.__init__(spawn_condition_override: GameplayCueNotify_SpawnCondition = [GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR, GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []], placement_info_override: GameplayCueNotify_PlacementInfo = ["None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH, AttachmentRule.KEEP_WORLD, False, True, [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], camera_shake: Class = None, shake_scale: float = 0.000000, play_space: GameplayCueNotify_EffectPlaySpace = GameplayCueNotify_EffectPlaySpace.WORLD_SPACE, override_spawn_condition: bool = False, override_placement_info: bool = False, play_in_world: bool = False, world_inner_radius: float = 0.000000, world_outer_radius: float = 0.000000, world_falloff_exponent: float = 0.000000) -> None
unreal.GameplayCueNotify_CameraShakeInfo.camera_shake() -> Class
unreal.GameplayCueNotify_CameraShakeInfo.override_placement_info() -> bool
unreal.GameplayCueNotify_CameraShakeInfo.override_spawn_condition() -> bool
unreal.GameplayCueNotify_CameraShakeInfo.placement_info_override() -> GameplayCueNotify_PlacementInfo
unreal.GameplayCueNotify_CameraShakeInfo.play_in_world() -> bool
unreal.GameplayCueNotify_CameraShakeInfo.play_space() -> GameplayCueNotify_EffectPlaySpace
unreal.GameplayCueNotify_CameraShakeInfo.shake_scale() -> float
unreal.GameplayCueNotify_CameraShakeInfo.spawn_condition_override() -> GameplayCueNotify_SpawnCondition
unreal.GameplayCueNotify_CameraShakeInfo.world_falloff_exponent() -> float
unreal.GameplayCueNotify_CameraShakeInfo.world_inner_radius() -> float
unreal.GameplayCueNotify_CameraShakeInfo.world_outer_radius() -> float
```

## `unreal.GameplayCueNotify_InputDevicePropertyInfo(StructBase)`

```python
unreal.GameplayCueNotify_InputDevicePropertyInfo.__init__(device_properties: Array[Class] = []) -> None
unreal.GameplayCueNotify_InputDevicePropertyInfo.device_properties() -> Array[Class]
```

## `unreal.GameplayCueNotify_SpawnCondition(StructBase)`

```python
unreal.GameplayCueNotify_SpawnCondition.__init__(locally_controlled_source: GameplayCueNotify_LocallyControlledSource = GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR, locally_controlled_policy: GameplayCueNotify_LocallyControlledPolicy = GameplayCueNotify_LocallyControlledPolicy.ALWAYS, chance_to_play: float = 0.000000, allowed_surface_types: Array[PhysicalSurface] = [], rejected_surface_types: Array[PhysicalSurface] = []) -> None
unreal.GameplayCueNotify_SpawnCondition.allowed_surface_types() -> Array[PhysicalSurface]
unreal.GameplayCueNotify_SpawnCondition.chance_to_play() -> float
unreal.GameplayCueNotify_SpawnCondition.locally_controlled_policy() -> GameplayCueNotify_LocallyControlledPolicy
unreal.GameplayCueNotify_SpawnCondition.locally_controlled_source() -> GameplayCueNotify_LocallyControlledSource
unreal.GameplayCueNotify_SpawnCondition.rejected_surface_types() -> Array[PhysicalSurface]
```

## `unreal.GameplayCueNotify_SpawnResult(StructBase)`

```python
unreal.GameplayCueNotify_SpawnResult.__init__(fx_system_components: Array[FXSystemComponent] = [], audio_components: Array[AudioComponent] = [], camera_shakes: Array[CameraShakeBase] = [], camera_lens_effects: Array[CameraLensEffectInterface] = [], force_feedback_component: ForceFeedbackComponent = None, decal_component: DecalComponent = None) -> None
unreal.GameplayCueNotify_SpawnResult.audio_components() -> Array[AudioComponent]
unreal.GameplayCueNotify_SpawnResult.camera_lens_effects() -> Array[CameraLensEffectInterface]
unreal.GameplayCueNotify_SpawnResult.camera_shakes() -> Array[CameraShakeBase]
unreal.GameplayCueNotify_SpawnResult.decal_component() -> DecalComponent
unreal.GameplayCueNotify_SpawnResult.force_feedback_component() -> ForceFeedbackComponent
unreal.GameplayCueNotify_SpawnResult.fx_system_components() -> Array[FXSystemComponent]
```

## `unreal.GetCameraRoamingInfoParams(ParamsBase)`

```python
unreal.GetCameraRoamingInfoParams.__init__(camera_roam_eid: int = 0) -> None
unreal.GetCameraRoamingInfoParams.camera_roam_eid(value: int) -> None
```

## `unreal.GetCameraRoamingInfoResult(ResultBase)`

```python
unreal.GetCameraRoamingInfoResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, progress_ratio: float = 0.000000) -> None
unreal.GetCameraRoamingInfoResult.progress_ratio(value: float) -> None
```

## `unreal.GlobeAwareDefaultPawn(DefaultPawn)`

```python
unreal.GlobeAwareDefaultPawn.fly_to_altitude_profile_curve(value: CurveFloat) -> None
unreal.GlobeAwareDefaultPawn.fly_to_duration(value: float) -> None
unreal.GlobeAwareDefaultPawn.fly_to_granularity_degrees(value: float) -> None
unreal.GlobeAwareDefaultPawn.fly_to_location_ecef(ecef_destination: Vector, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.GlobeAwareDefaultPawn.fly_to_location_longitude_latitude_height(longitude_latitude_height_destination: Vector, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.GlobeAwareDefaultPawn.fly_to_maximum_altitude_curve(value: CurveFloat) -> None
unreal.GlobeAwareDefaultPawn.fly_to_progress_curve(value: CurveFloat) -> None
unreal.GlobeAwareDefaultPawn.georeference() -> CesiumGeoreference
unreal.GlobeAwareDefaultPawn.get_globe_to_unreal_world_transform() -> Transform
unreal.GlobeAwareDefaultPawn.globe_anchor() -> CesiumGlobeAnchorComponent
unreal.GlobeAwareDefaultPawn.inaccurate_fly_to_location_ecef(ecef_destination: Vector, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.GlobeAwareDefaultPawn.inaccurate_fly_to_location_longitude_latitude_height(longitude_latitude_height_destination: Vector, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.GlobeAwareDefaultPawn.on_flight_complete(value: CompletedFlight) -> None
unreal.GlobeAwareDefaultPawn.on_flight_interrupt(value: InterruptedFlight) -> None
```

## `unreal.GrassInput(StructBase)`

```python
unreal.GrassInput.__init__() -> None
```

## `unreal.HardwareInputDeviceChanged(MulticastDelegateBase)`

```python
unreal.HardwareInputDeviceChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.IKRetargeterController(Object)`

```python
unreal.IKRetargeterController.add_retarget_op(op_class: Class) -> int
unreal.IKRetargeterController.auto_align_all_bones(source_or_target: RetargetSourceOrTarget) -> None
unreal.IKRetargeterController.auto_align_bones(bones_to_align: Array[Name], method: RetargetAutoAlignMethod, source_or_target: RetargetSourceOrTarget) -> None
unreal.IKRetargeterController.auto_map_chains(auto_map_type: AutoMapChainType, force_remap: bool) -> None
unreal.IKRetargeterController.create_retarget_pose(new_pose_name: Name, source_or_target: RetargetSourceOrTarget) -> Name
unreal.IKRetargeterController.duplicate_retarget_pose(pose_to_duplicate: Name, new_name: Name, source_or_target: RetargetSourceOrTarget) -> Name
unreal.IKRetargeterController.get_all_chain_settings() -> Array[RetargetChainSettings]
unreal.IKRetargeterController.get_controller(retargeter_asset: IKRetargeter) -> IKRetargeterController
unreal.IKRetargeterController.get_current_retarget_pose(source_or_target: RetargetSourceOrTarget) -> IKRetargetPose
unreal.IKRetargeterController.get_current_retarget_pose_name(source_or_target: RetargetSourceOrTarget) -> Name
unreal.IKRetargeterController.get_global_settings() -> RetargetGlobalSettings
unreal.IKRetargeterController.get_ik_rig(source_or_target: RetargetSourceOrTarget) -> IKRigDefinition
unreal.IKRetargeterController.get_index_of_retarget_op(retarget_op: RetargetOpBase) -> int
unreal.IKRetargeterController.get_num_retarget_ops() -> int
unreal.IKRetargeterController.get_preview_mesh(source_or_target: RetargetSourceOrTarget) -> SkeletalMesh
unreal.IKRetargeterController.get_retarget_chain_settings(target_chain_name: Name) -> TargetChainSettings
unreal.IKRetargeterController.get_retarget_op_at_index(index: int) -> RetargetOpBase
unreal.IKRetargeterController.get_retarget_op_enabled(retarget_op_index: int) -> bool
unreal.IKRetargeterController.get_retarget_poses(source_or_target: RetargetSourceOrTarget) -> Map[Name, IKRetargetPose]
unreal.IKRetargeterController.get_root_offset_in_retarget_pose(source_or_target: RetargetSourceOrTarget) -> Vector
unreal.IKRetargeterController.get_root_settings() -> TargetRootSettings
unreal.IKRetargeterController.get_rotation_offset_for_retarget_pose_bone(bone_name: Name, source_or_target: RetargetSourceOrTarget) -> Quat
unreal.IKRetargeterController.get_source_chain(target_chain_name: Name) -> Name
unreal.IKRetargeterController.move_retarget_op_in_stack(op_to_move_index: int, target_index: int) -> bool
unreal.IKRetargeterController.remove_all_ops() -> bool
unreal.IKRetargeterController.remove_retarget_op(op_index: int) -> bool
unreal.IKRetargeterController.remove_retarget_pose(pose_to_remove: Name, source_or_target: RetargetSourceOrTarget) -> bool
unreal.IKRetargeterController.rename_retarget_pose(old_pose_name: Name, new_pose_name: Name, source_or_target: RetargetSourceOrTarget) -> bool
unreal.IKRetargeterController.reset_retarget_pose(pose_to_reset: Name, bones_to_reset: Array[Name], source_or_target: RetargetSourceOrTarget) -> None
unreal.IKRetargeterController.set_current_retarget_pose(current_pose: Name, source_or_target: RetargetSourceOrTarget) -> bool
unreal.IKRetargeterController.set_global_settings(global_settings: RetargetGlobalSettings) -> None
unreal.IKRetargeterController.set_ik_rig(source_or_target: RetargetSourceOrTarget, ik_rig: IKRigDefinition) -> None
unreal.IKRetargeterController.set_preview_mesh(source_or_target: RetargetSourceOrTarget, preview_mesh: SkeletalMesh) -> None
unreal.IKRetargeterController.set_retarget_chain_settings(target_chain_name: Name, settings: TargetChainSettings) -> bool
unreal.IKRetargeterController.set_retarget_op_enabled(retarget_op_index: int, is_enabled: bool) -> bool
unreal.IKRetargeterController.set_root_offset_in_retarget_pose(translation_offset: Vector, source_or_target: RetargetSourceOrTarget) -> None
unreal.IKRetargeterController.set_root_settings(root_settings: TargetRootSettings) -> None
unreal.IKRetargeterController.set_rotation_offset_for_retarget_pose_bone(bone_name: Name, rotation_offset: Quat, skeleton_mode: RetargetSourceOrTarget) -> None
unreal.IKRetargeterController.set_source_chain(source_chain_name: Name, target_chain_name: Name) -> bool
unreal.IKRetargeterController.snap_bone_to_ground(reference_bone: Name, source_or_target: RetargetSourceOrTarget) -> None
```

## `unreal.InputAction(DataAsset)`

```python
unreal.InputAction.accumulation_behavior() -> InputActionAccumulationBehavior
unreal.InputAction.action_description() -> Text
unreal.InputAction.consume_input(value: bool) -> None
unreal.InputAction.consumes_action_and_axis_mappings(value: bool) -> None
unreal.InputAction.modifiers(value: Array[InputModifier]) -> None
unreal.InputAction.player_mappable_key_settings(value: PlayerMappableKeySettings) -> None
unreal.InputAction.reserve_all_mappings() -> bool
unreal.InputAction.trigger_events_that_consume_legacy_keys(value: int) -> None
unreal.InputAction.trigger_when_paused() -> bool
unreal.InputAction.triggers(value: Array[InputTrigger]) -> None
unreal.InputAction.value_type() -> InputActionValueType
```

## `unreal.InputActionHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputActionHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputActionInstance(StructBase)`

```python
unreal.InputActionInstance.__init__(source_action: InputAction = None, trigger_event: TriggerEvent = 0, last_triggered_world_time: float = 0.000000, triggers: Array[InputTrigger] = [], modifiers: Array[InputModifier] = [], elapsed_processed_time: float = 0.000000, elapsed_triggered_time: float = 0.000000) -> None
unreal.InputActionInstance.elapsed_processed_time() -> float
unreal.InputActionInstance.elapsed_triggered_time() -> float
unreal.InputActionInstance.last_triggered_world_time() -> float
unreal.InputActionInstance.modifiers() -> Array[InputModifier]
unreal.InputActionInstance.source_action() -> InputAction
unreal.InputActionInstance.trigger_event() -> TriggerEvent
unreal.InputActionInstance.triggers() -> Array[InputTrigger]
```

## `unreal.InputActionValue(StructBase)`

```python
unreal.InputActionValue.__init__(x: float = 0.000000, y: float = 0.000000, z: float = 0.000000, value_type: InputActionValueType = InputActionValueType.BOOLEAN) -> None
```

## `unreal.InputAlphaBoolBlend(StructBase)`

```python
unreal.InputAlphaBoolBlend.__init__(blend_in_time: float = 0.000000, blend_out_time: float = 0.000000, blend_option: AlphaBlendOption = AlphaBlendOption.LINEAR, custom_curve: CurveFloat = None) -> None
unreal.InputAlphaBoolBlend.blend_in_time(value: float) -> None
unreal.InputAlphaBoolBlend.blend_option(value: AlphaBlendOption) -> None
unreal.InputAlphaBoolBlend.blend_out_time(value: float) -> None
unreal.InputAlphaBoolBlend.custom_curve(value: CurveFloat) -> None
```

## `unreal.InputAxisConfigEntry(StructBase)`

```python
unreal.InputAxisConfigEntry.__init__() -> None
```

## `unreal.InputAxisHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputAxisHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputAxisProperties(StructBase)`

```python
unreal.InputAxisProperties.__init__() -> None
```

## `unreal.InputCancelAction(StructBase)`

```python
unreal.InputCancelAction.__init__(cancel_action: InputAction = None, cancellation_states: int = 0) -> None
unreal.InputCancelAction.cancel_action(value: InputAction) -> None
unreal.InputCancelAction.cancellation_states(value: int) -> None
```

## `unreal.InputChord(StructBase)`

```python
unreal.InputChord.__init__(key: Key = [], shift: bool = False, ctrl: bool = False, alt: bool = False, cmd: bool = False) -> None
unreal.InputChord.alt(value: bool) -> None
unreal.InputChord.cmd(value: bool) -> None
unreal.InputChord.ctrl(value: bool) -> None
unreal.InputChord.key(value: Key) -> None
unreal.InputChord.shift(value: bool) -> None
```

## `unreal.InputClampConstants(StructBase)`

```python
unreal.InputClampConstants.__init__(clamp_result: bool = False, interp_result: bool = False, clamp_min: float = 0.000000, clamp_max: float = 0.000000, interp_speed_increasing: float = 0.000000, interp_speed_decreasing: float = 0.000000) -> None
unreal.InputClampConstants.clamp_max(value: float) -> None
unreal.InputClampConstants.clamp_min(value: float) -> None
unreal.InputClampConstants.clamp_result(value: bool) -> None
unreal.InputClampConstants.interp_result(value: bool) -> None
unreal.InputClampConstants.interp_speed_decreasing(value: float) -> None
unreal.InputClampConstants.interp_speed_increasing(value: float) -> None
```

## `unreal.InputClampState(StructBase)`

```python
unreal.InputClampState.__init__() -> None
```

## `unreal.InputComboStepData(StructBase)`

```python
unreal.InputComboStepData.__init__(combo_step_action: InputAction = None, combo_step_completion_states: int = 0, time_to_press_key: float = 0.000000) -> None
unreal.InputComboStepData.combo_step_action(value: InputAction) -> None
unreal.InputComboStepData.combo_step_completion_states(value: int) -> None
unreal.InputComboStepData.time_to_press_key(value: float) -> None
```

## `unreal.InputComponent(ActorComponent)`

```python
unreal.InputComponent.get_controller_analog_key_state(key: Key) -> float
unreal.InputComponent.get_controller_analog_stick_state(which_stick: ControllerAnalogStick) -> Tuple[float, float]
unreal.InputComponent.get_controller_key_time_down(key: Key) -> float
unreal.InputComponent.get_controller_mouse_delta() -> Tuple[float, float]
unreal.InputComponent.get_controller_vector_key_state(key: Key) -> Vector
unreal.InputComponent.get_touch_state(finger_index: int) -> Tuple[float, float, bool]
unreal.InputComponent.is_controller_key_down(key: Key) -> bool
unreal.InputComponent.was_controller_key_just_pressed(key: Key) -> bool
unreal.InputComponent.was_controller_key_just_released(key: Key) -> bool
```

## `unreal.InputDebugKeyHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputDebugKeyHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputDeviceId(StructBase)`

```python
unreal.InputDeviceId.__init__() -> None
unreal.InputDeviceId.equals(b: InputDeviceId) -> bool
unreal.InputDeviceId.not_equal(b: InputDeviceId) -> bool
```

## `unreal.InputDeviceLibrary(BlueprintFunctionLibrary)`

```python
unreal.InputDeviceLibrary.equal_equal_input_device_id(a: InputDeviceId, b: InputDeviceId) -> bool
unreal.InputDeviceLibrary.equal_equal_platform_user_id(a: PlatformUserId, b: PlatformUserId) -> bool
unreal.InputDeviceLibrary.get_all_active_users() -> Tuple[int, Array[PlatformUserId]]
unreal.InputDeviceLibrary.get_all_connected_input_devices() -> Tuple[int, Array[InputDeviceId]]
unreal.InputDeviceLibrary.get_all_input_devices() -> Tuple[int, Array[InputDeviceId]]
unreal.InputDeviceLibrary.get_all_input_devices_for_user(user_id: PlatformUserId) -> Tuple[int, Array[InputDeviceId]]
unreal.InputDeviceLibrary.get_default_input_device() -> InputDeviceId
unreal.InputDeviceLibrary.get_input_device_connection_state(device_id: InputDeviceId) -> InputDeviceConnectionState
unreal.InputDeviceLibrary.get_player_controller_from_input_device(device_id: InputDeviceId) -> PlayerController
unreal.InputDeviceLibrary.get_player_controller_from_platform_user(user_id: PlatformUserId) -> PlayerController
unreal.InputDeviceLibrary.get_primary_input_device_for_user(user_id: PlatformUserId) -> InputDeviceId
unreal.InputDeviceLibrary.get_primary_platform_user() -> PlatformUserId
unreal.InputDeviceLibrary.get_user_for_input_device(device_id: InputDeviceId) -> PlatformUserId
unreal.InputDeviceLibrary.get_user_for_unpaired_input_devices() -> PlatformUserId
unreal.InputDeviceLibrary.is_device_property_handle_valid(handle: InputDevicePropertyHandle) -> bool
unreal.InputDeviceLibrary.is_input_device_mapped_to_unpaired_user(input_device: InputDeviceId) -> bool
unreal.InputDeviceLibrary.is_unpaired_user_id(platform_id: PlatformUserId) -> bool
unreal.InputDeviceLibrary.is_valid_input_device(device_id: InputDeviceId) -> bool
unreal.InputDeviceLibrary.is_valid_platform_id(user_id: PlatformUserId) -> bool
unreal.InputDeviceLibrary.not_equal_input_device_id(a: InputDeviceId, b: InputDeviceId) -> bool
unreal.InputDeviceLibrary.not_equal_platform_user_id(a: PlatformUserId, b: PlatformUserId) -> bool
```

## `unreal.InputDeviceProperty(Object)`

```python
unreal.InputDeviceProperty.evaluate_device_property(platform_user: PlatformUserId, device_id: InputDeviceId, delta_time: float, duration: float) -> None
unreal.InputDeviceProperty.property_duration() -> float
unreal.InputDeviceProperty.reset_device_property(platform_user: PlatformUserId, device_id: InputDeviceId, force_reset: bool) -> None
```

## `unreal.InputDevicePropertyHandle(StructBase)`

```python
unreal.InputDevicePropertyHandle.__init__() -> None
```

## `unreal.InputDeviceRay(StructBase)`

```python
unreal.InputDeviceRay.__init__(world_ray: Ray = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], has2d: bool = False, screen_position: Vector2D = [0.000000, 0.000000]) -> None
unreal.InputDeviceRay.has2d(value: bool) -> None
unreal.InputDeviceRay.screen_position(value: Vector2D) -> None
unreal.InputDeviceRay.world_ray(value: Ray) -> None
```

## `unreal.InputDeviceState(StructBase)`

```python
unreal.InputDeviceState.__init__(input_device: InputDevices = InputDevices.NONE, shift_key_down: bool = False, alt_key_down: bool = False, ctrl_key_down: bool = False, cmd_key_down: bool = False, keyboard: KeyboardInputDeviceState = [[[], False, False, False, False]], mouse: MouseInputDeviceState = [[[], False, False, False, False], [[], False, False, False, False], [[], False, False, False, False], 0.000000, [0.000000, 0.000000], [0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 1.000000]]]) -> None
unreal.InputDeviceState.alt_key_down(value: bool) -> None
unreal.InputDeviceState.cmd_key_down(value: bool) -> None
unreal.InputDeviceState.ctrl_key_down(value: bool) -> None
unreal.InputDeviceState.input_device(value: InputDevices) -> None
unreal.InputDeviceState.keyboard(value: KeyboardInputDeviceState) -> None
unreal.InputDeviceState.mouse(value: MouseInputDeviceState) -> None
unreal.InputDeviceState.shift_key_down(value: bool) -> None
```

## `unreal.InputDeviceTriggerEffect(InputDeviceProperty)`

```python
unreal.InputDeviceTriggerEffect.base_trigger_data(value: DeviceTriggerBaseData) -> None
```

## `unreal.InputDeviceTriggerFeedbackProperty(InputDeviceTriggerEffect)`

```python
unreal.InputDeviceTriggerFeedbackProperty.device_override_data(value: Map[Name, DeviceTriggerFeedbackData]) -> None
unreal.InputDeviceTriggerFeedbackProperty.trigger_data(value: DeviceTriggerFeedbackData) -> None
```

## `unreal.InputDeviceTriggerResistanceProperty(InputDeviceTriggerEffect)`

```python
unreal.InputDeviceTriggerResistanceProperty.device_override_data(value: Map[Name, DeviceTriggerTriggerResistanceData]) -> None
unreal.InputDeviceTriggerResistanceProperty.trigger_data(value: DeviceTriggerTriggerResistanceData) -> None
```

## `unreal.InputDeviceTriggerVibrationProperty(InputDeviceTriggerEffect)`

```python
unreal.InputDeviceTriggerVibrationProperty.device_override_data(value: Map[Name, DeviceTriggerTriggerVibrationData]) -> None
unreal.InputDeviceTriggerVibrationProperty.trigger_data(value: DeviceTriggerTriggerVibrationData) -> None
```

## `unreal.InputEvent(StructBase)`

```python
unreal.InputEvent.__init__() -> None
```

## `unreal.InputGestureHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputGestureHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputKeySelector(Widget)`

```python
unreal.InputKeySelector.allow_gamepad_keys(value: bool) -> None
unreal.InputKeySelector.allow_modifier_keys(value: bool) -> None
unreal.InputKeySelector.escape_keys() -> Array[Key]
unreal.InputKeySelector.get_is_selecting_key() -> bool
unreal.InputKeySelector.key_selection_text(value: Text) -> None
unreal.InputKeySelector.margin(value: Margin) -> None
unreal.InputKeySelector.no_key_specified_text(value: Text) -> None
unreal.InputKeySelector.on_is_selecting_key_changed(value: OnIsSelectingKeyChanged) -> None
unreal.InputKeySelector.on_key_selected(value: OnKeySelected) -> None
unreal.InputKeySelector.selected_key(value: InputChord) -> None
unreal.InputKeySelector.set_allow_gamepad_keys(allow_gamepad_keys: bool) -> None
unreal.InputKeySelector.set_allow_modifier_keys(allow_modifier_keys: bool) -> None
unreal.InputKeySelector.set_escape_keys(keys: Array[Key]) -> None
unreal.InputKeySelector.set_key_selection_text(key_selection_text: Text) -> None
unreal.InputKeySelector.set_no_key_specified_text(no_key_specified_text: Text) -> None
unreal.InputKeySelector.set_selected_key(selected_key: InputChord) -> None
unreal.InputKeySelector.set_text_block_visibility(visibility: SlateVisibility) -> None
unreal.InputKeySelector.text_style(value: TextBlockStyle) -> None
unreal.InputKeySelector.widget_style(value: ButtonStyle) -> None
```

## `unreal.InputKeySelector_OnIsSelectingKeyChanged(MulticastDelegateBase)`

```python
unreal.InputKeySelector_OnIsSelectingKeyChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputKeySelector_OnKeySelected(MulticastDelegateBase)`

```python
unreal.InputKeySelector_OnKeySelected.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputLibrary(BlueprintFunctionLibrary)`

```python
unreal.InputLibrary.calibrate_tilt() -> None
unreal.InputLibrary.equal_equal_input_chord_input_chord(a: InputChord, b: InputChord) -> bool
unreal.InputLibrary.equal_equal_key_key(a: Key, b: Key) -> bool
unreal.InputLibrary.get_analog_value(input: AnalogInputEvent) -> float
unreal.InputLibrary.get_key(input: KeyEvent) -> Key
unreal.InputLibrary.get_modifier_keys_state() -> SlateModifierKeysState
unreal.InputLibrary.get_user_index(input: KeyEvent) -> int
unreal.InputLibrary.input_chord_get_display_name(key: InputChord) -> Text
unreal.InputLibrary.input_event_is_alt_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_command_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_control_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_left_alt_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_left_command_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_left_control_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_left_shift_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_repeat(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_right_alt_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_right_command_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_right_control_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_right_shift_down(input: InputEvent) -> bool
unreal.InputLibrary.input_event_is_shift_down(input: InputEvent) -> bool
unreal.InputLibrary.key_get_display_name(key: Key, long_display_name: bool = True) -> Text
unreal.InputLibrary.key_get_navigation_action(key: Key) -> UINavigationAction
unreal.InputLibrary.key_get_navigation_action_from_key(key_event: KeyEvent) -> UINavigationAction
unreal.InputLibrary.key_get_navigation_direction_from_analog(analog_event: AnalogInputEvent) -> UINavigation
unreal.InputLibrary.key_get_navigation_direction_from_key(key_event: KeyEvent) -> UINavigation
unreal.InputLibrary.key_is_analog(key: Key) -> bool
unreal.InputLibrary.key_is_axis1d(key: Key) -> bool
unreal.InputLibrary.key_is_axis2d(key: Key) -> bool
unreal.InputLibrary.key_is_axis3d(key: Key) -> bool
unreal.InputLibrary.key_is_button_axis(key: Key) -> bool
unreal.InputLibrary.key_is_digital(key: Key) -> bool
unreal.InputLibrary.key_is_float_axis(key: Key) -> bool
unreal.InputLibrary.key_is_gamepad_key(key: Key) -> bool
unreal.InputLibrary.key_is_keyboard_key(key: Key) -> bool
unreal.InputLibrary.key_is_modifier_key(key: Key) -> bool
unreal.InputLibrary.key_is_mouse_button(key: Key) -> bool
unreal.InputLibrary.key_is_valid(key: Key) -> bool
unreal.InputLibrary.key_is_vector_axis(key: Key) -> bool
unreal.InputLibrary.modifier_keys_state_is_alt_down(keys_state: SlateModifierKeysState) -> bool
unreal.InputLibrary.modifier_keys_state_is_command_down(keys_state: SlateModifierKeysState) -> bool
unreal.InputLibrary.modifier_keys_state_is_control_down(keys_state: SlateModifierKeysState) -> bool
unreal.InputLibrary.modifier_keys_state_is_shift_down(keys_state: SlateModifierKeysState) -> bool
unreal.InputLibrary.pointer_event_get_cursor_delta(input: PointerEvent) -> Vector2D
unreal.InputLibrary.pointer_event_get_effecting_button(input: PointerEvent) -> Key
unreal.InputLibrary.pointer_event_get_gesture_delta(input: PointerEvent) -> Vector2D
unreal.InputLibrary.pointer_event_get_gesture_type(input: PointerEvent) -> SlateGesture
unreal.InputLibrary.pointer_event_get_last_screen_space_position(input: PointerEvent) -> Vector2D
unreal.InputLibrary.pointer_event_get_pointer_index(input: PointerEvent) -> int
unreal.InputLibrary.pointer_event_get_screen_space_position(input: PointerEvent) -> Vector2D
unreal.InputLibrary.pointer_event_get_touchpad_index(input: PointerEvent) -> int
unreal.InputLibrary.pointer_event_get_user_index(input: PointerEvent) -> int
unreal.InputLibrary.pointer_event_get_wheel_delta(input: PointerEvent) -> float
unreal.InputLibrary.pointer_event_is_mouse_button_down(input: PointerEvent, mouse_button: Key) -> bool
unreal.InputLibrary.pointer_event_is_touch_event(input: PointerEvent) -> bool
```

## `unreal.InputModifier(Object)`

```python
unreal.InputModifier.get_visualization_color(sample_value: InputActionValue, final_value: InputActionValue) -> LinearColor
unreal.InputModifier.modify_raw(player_input: EnhancedPlayerInput, current_value: InputActionValue, delta_time: float) -> InputActionValue
```

## `unreal.InputModifierDeadZone(InputModifier)`

```python
unreal.InputModifierDeadZone.lower_threshold(value: float) -> None
unreal.InputModifierDeadZone.type(value: DeadZoneType) -> None
unreal.InputModifierDeadZone.upper_threshold(value: float) -> None
```

## `unreal.InputModifierFOVScaling(InputModifier)`

```python
unreal.InputModifierFOVScaling.fov_scale(value: float) -> None
unreal.InputModifierFOVScaling.fov_scaling_type(value: FOVScalingType) -> None
```

## `unreal.InputModifierNegate(InputModifier)`

```python
unreal.InputModifierNegate.x(value: bool) -> None
unreal.InputModifierNegate.y(value: bool) -> None
unreal.InputModifierNegate.z(value: bool) -> None
```

## `unreal.InputModifierScalar(InputModifier)`

```python
unreal.InputModifierScalar.scalar(value: Vector) -> None
```

## `unreal.InputModifierSmoothDelta(InputModifier)`

```python
unreal.InputModifierSmoothDelta.easing_exponent(value: float) -> None
unreal.InputModifierSmoothDelta.smoothing_method(value: NormalizeInputSmoothingType) -> None
unreal.InputModifierSmoothDelta.speed(value: float) -> None
```

## `unreal.InputModifierSwizzleAxis(InputModifier)`

```python
unreal.InputModifierSwizzleAxis.order(value: InputAxisSwizzle) -> None
```

## `unreal.InputPressDelegate(MulticastDelegateBase)`

```python
unreal.InputPressDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputRange(StructBase)`

```python
unreal.InputRange.__init__(min: float = 0.000000, max: float = 0.000000) -> None
unreal.InputRange.max(value: float) -> None
unreal.InputRange.min(value: float) -> None
```

## `unreal.InputRayHit(StructBase)`

```python
unreal.InputRayHit.__init__(hit: bool = False, hit_depth: float = 0.000000, hit_normal: Vector = [0.000000, 0.000000, 0.000000], has_hit_normal: bool = False, hit_identifier: int = 0, hit_object: Object = None) -> None
unreal.InputRayHit.has_hit_normal(value: bool) -> None
unreal.InputRayHit.hit(value: bool) -> None
unreal.InputRayHit.hit_depth(value: float) -> None
unreal.InputRayHit.hit_identifier(value: int) -> None
unreal.InputRayHit.hit_normal(value: Vector) -> None
unreal.InputRayHit.hit_object(value: Object) -> None
```

## `unreal.InputReleaseDelegate(MulticastDelegateBase)`

```python
unreal.InputReleaseDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputScaleBias(StructBase)`

```python
unreal.InputScaleBias.__init__(scale: float = 0.000000, bias: float = 0.000000) -> None
unreal.InputScaleBias.bias(value: float) -> None
unreal.InputScaleBias.scale(value: float) -> None
```

## `unreal.InputScaleBiasClamp(StructBase)`

```python
unreal.InputScaleBiasClamp.__init__(map_range: bool = False, clamp_result: bool = False, interp_result: bool = False, range: InputRange = [0.000000, 1.000000], out_range: InputRange = [0.000000, 1.000000], scale: float = 0.000000, bias: float = 0.000000, clamp_min: float = 0.000000, clamp_max: float = 0.000000, interp_speed_increasing: float = 0.000000, interp_speed_decreasing: float = 0.000000) -> None
unreal.InputScaleBiasClamp.bias(value: float) -> None
unreal.InputScaleBiasClamp.clamp_max(value: float) -> None
unreal.InputScaleBiasClamp.clamp_min(value: float) -> None
unreal.InputScaleBiasClamp.clamp_result(value: bool) -> None
unreal.InputScaleBiasClamp.interp_result(value: bool) -> None
unreal.InputScaleBiasClamp.interp_speed_decreasing(value: float) -> None
unreal.InputScaleBiasClamp.interp_speed_increasing(value: float) -> None
unreal.InputScaleBiasClamp.map_range(value: bool) -> None
unreal.InputScaleBiasClamp.out_range(value: InputRange) -> None
unreal.InputScaleBiasClamp.range(value: InputRange) -> None
unreal.InputScaleBiasClamp.scale(value: float) -> None
```

## `unreal.InputScaleBiasClampConstants(StructBase)`

```python
unreal.InputScaleBiasClampConstants.__init__(map_range: bool = False, clamp_result: bool = False, interp_result: bool = False, range: InputRange = [0.000000, 1.000000], out_range: InputRange = [0.000000, 1.000000], scale: float = 0.000000, bias: float = 0.000000, clamp_min: float = 0.000000, clamp_max: float = 0.000000, interp_speed_increasing: float = 0.000000, interp_speed_decreasing: float = 0.000000) -> None
unreal.InputScaleBiasClampConstants.bias(value: float) -> None
unreal.InputScaleBiasClampConstants.clamp_max(value: float) -> None
unreal.InputScaleBiasClampConstants.clamp_min(value: float) -> None
unreal.InputScaleBiasClampConstants.clamp_result(value: bool) -> None
unreal.InputScaleBiasClampConstants.interp_result(value: bool) -> None
unreal.InputScaleBiasClampConstants.interp_speed_decreasing(value: float) -> None
unreal.InputScaleBiasClampConstants.interp_speed_increasing(value: float) -> None
unreal.InputScaleBiasClampConstants.map_range(value: bool) -> None
unreal.InputScaleBiasClampConstants.out_range(value: InputRange) -> None
unreal.InputScaleBiasClampConstants.range(value: InputRange) -> None
unreal.InputScaleBiasClampConstants.scale(value: float) -> None
```

## `unreal.InputScaleBiasClampState(StructBase)`

```python
unreal.InputScaleBiasClampState.__init__() -> None
```

## `unreal.InputSettings(Object)`

```python
unreal.InputSettings.add_action_mapping(key_mapping: InputActionKeyMapping, force_rebuild_keymaps: bool = True) -> None
unreal.InputSettings.add_axis_mapping(key_mapping: InputAxisKeyMapping, force_rebuild_keymaps: bool = True) -> None
unreal.InputSettings.enable_input_device_subsystem(value: bool) -> None
unreal.InputSettings.force_rebuild_keymaps() -> None
unreal.InputSettings.get_action_mapping_by_name(action_name: Name) -> Array[InputActionKeyMapping]
unreal.InputSettings.get_action_names() -> Array[Name]
unreal.InputSettings.get_axis_mapping_by_name(axis_name: Name) -> Array[InputAxisKeyMapping]
unreal.InputSettings.get_axis_names() -> Array[Name]
unreal.InputSettings.get_input_settings() -> InputSettings
unreal.InputSettings.remove_action_mapping(key_mapping: InputActionKeyMapping, force_rebuild_keymaps: bool = True) -> None
unreal.InputSettings.remove_axis_mapping(key_mapping: InputAxisKeyMapping, force_rebuild_keymaps: bool = True) -> None
unreal.InputSettings.save_key_mappings() -> None
```

## `unreal.InputTouchHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputTouchHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.InputTrigger(Object)`

```python
unreal.InputTrigger.actuation_threshold(value: float) -> None
unreal.InputTrigger.get_trigger_type() -> TriggerType
unreal.InputTrigger.is_actuated(for_value: InputActionValue) -> bool
unreal.InputTrigger.last_value() -> InputActionValue
unreal.InputTrigger.should_always_tick() -> bool
unreal.InputTrigger.update_state(player_input: EnhancedPlayerInput, modified_value: InputActionValue, delta_time: float) -> TriggerState
```

## `unreal.InputTriggerChordAction(InputTrigger)`

```python
unreal.InputTriggerChordAction.chord_action(value: InputAction) -> None
```

## `unreal.InputTriggerCombo(InputTrigger)`

```python
unreal.InputTriggerCombo.combo_actions(value: Array[InputComboStepData]) -> None
unreal.InputTriggerCombo.current_combo_step_index() -> int
unreal.InputTriggerCombo.current_time_between_combo_steps() -> float
unreal.InputTriggerCombo.input_cancel_actions(value: Array[InputCancelAction]) -> None
```

## `unreal.InputTriggerHold(InputTriggerTimedBase)`

```python
unreal.InputTriggerHold.hold_time_threshold(value: float) -> None
unreal.InputTriggerHold.is_one_shot(value: bool) -> None
```

## `unreal.InputTriggerHoldAndRelease(InputTriggerTimedBase)`

```python
unreal.InputTriggerHoldAndRelease.hold_time_threshold(value: float) -> None
```

## `unreal.InputTriggerPulse(InputTriggerTimedBase)`

```python
unreal.InputTriggerPulse.interval(value: float) -> None
unreal.InputTriggerPulse.trigger_limit(value: int) -> None
unreal.InputTriggerPulse.trigger_on_start(value: bool) -> None
```

## `unreal.InputTriggerTap(InputTriggerTimedBase)`

```python
unreal.InputTriggerTap.tap_release_time_threshold(value: float) -> None
```

## `unreal.InputTriggerTimedBase(InputTrigger)`

```python
unreal.InputTriggerTimedBase.affected_by_time_dilation(value: bool) -> None
unreal.InputTriggerTimedBase.held_duration(value: float) -> None
```

## `unreal.InputVectorAxisHandlerDynamicSignature(DelegateBase)`

```python
unreal.InputVectorAxisHandlerDynamicSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.KeyboardInputDeviceState(StructBase)`

```python
unreal.KeyboardInputDeviceState.__init__(active_key: DeviceButtonState = [[], False, False, False, False]) -> None
unreal.KeyboardInputDeviceState.active_key(value: DeviceButtonState) -> None
```

## `unreal.LayerBlendInput(StructBase)`

```python
unreal.LayerBlendInput.__init__() -> None
```

## `unreal.LegacyCameraShake(CameraShakeBase)`

```python
unreal.LegacyCameraShake.blueprint_update_camera_shake(delta_time: float, alpha: float, pov: MinimalViewInfo) -> MinimalViewInfo
unreal.LegacyCameraShake.fov_oscillation(value: FOscillator) -> None
unreal.LegacyCameraShake.loc_oscillation(value: VOscillator) -> None
unreal.LegacyCameraShake.oscillator_time_remaining() -> float
unreal.LegacyCameraShake.receive_is_finished() -> bool
unreal.LegacyCameraShake.receive_play_shake(scale: float) -> None
unreal.LegacyCameraShake.receive_stop_shake(immediately: bool) -> None
unreal.LegacyCameraShake.rot_oscillation(value: ROscillator) -> None
unreal.LegacyCameraShake.start_legacy_camera_shake(player_camera_manager: PlayerCameraManager, shake_class: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
unreal.LegacyCameraShake.start_legacy_camera_shake_from_source(player_camera_manager: PlayerCameraManager, shake_class: Class, source_component: CameraShakeSourceComponent, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
unreal.LegacyCameraShake.start_matinee_camera_shake(player_camera_manager: PlayerCameraManager, shake_class: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
unreal.LegacyCameraShake.start_matinee_camera_shake_from_source(player_camera_manager: PlayerCameraManager, shake_class: Class, source_component: CameraShakeSourceComponent, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> LegacyCameraShake
```

## `unreal.LegacyCameraShakeFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.LegacyCameraShakeFunctionLibrary.conv_legacy_camera_shake(camera_shake: CameraShakeBase) -> LegacyCameraShake
unreal.LegacyCameraShakeFunctionLibrary.conv_matinee_camera_shake(camera_shake: CameraShakeBase) -> LegacyCameraShake
```

## `unreal.LiveLinkCameraFrameData(LiveLinkTransformFrameData)`

```python
unreal.LiveLinkCameraFrameData.__init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]], property_values: Array[float] = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], field_of_view: float = 0.000000, aspect_ratio: float = 0.000000, focal_length: float = 0.000000, aperture: float = 0.000000, focus_distance: float = 0.000000, projection_mode: LiveLinkCameraProjectionMode = LiveLinkCameraProjectionMode.PERSPECTIVE) -> None
unreal.LiveLinkCameraFrameData.aperture(value: float) -> None
unreal.LiveLinkCameraFrameData.aspect_ratio(value: float) -> None
unreal.LiveLinkCameraFrameData.field_of_view(value: float) -> None
unreal.LiveLinkCameraFrameData.focal_length(value: float) -> None
unreal.LiveLinkCameraFrameData.focus_distance(value: float) -> None
unreal.LiveLinkCameraFrameData.projection_mode(value: LiveLinkCameraProjectionMode) -> None
```

## `unreal.LiveLinkCameraStaticData(LiveLinkTransformStaticData)`

```python
unreal.LiveLinkCameraStaticData.__init__(property_names: Array[Name] = [], is_location_supported: bool = False, is_rotation_supported: bool = False, is_scale_supported: bool = False, is_field_of_view_supported: bool = False, is_aspect_ratio_supported: bool = False, is_focal_length_supported: bool = False, is_projection_mode_supported: bool = False, film_back_width: float = 0.000000, film_back_height: float = 0.000000, is_aperture_supported: bool = False, is_focus_distance_supported: bool = False, is_depth_of_field_supported: bool = False) -> None
unreal.LiveLinkCameraStaticData.film_back_height(value: float) -> None
unreal.LiveLinkCameraStaticData.film_back_width(value: float) -> None
unreal.LiveLinkCameraStaticData.is_aperture_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_aspect_ratio_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_depth_of_field_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_field_of_view_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_focal_length_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_focus_distance_supported(value: bool) -> None
unreal.LiveLinkCameraStaticData.is_projection_mode_supported(value: bool) -> None
```

## `unreal.LiveLinkComponentController(ActorComponent)`

```python
unreal.LiveLinkComponentController.controller_map() -> Map[Class, LiveLinkControllerBase]
unreal.LiveLinkComponentController.disable_evaluate_live_link_when_spawnable(value: bool) -> None
unreal.LiveLinkComponentController.evaluate_live_link(value: bool) -> None
unreal.LiveLinkComponentController.get_controlled_component(role_class: Class) -> ActorComponent
unreal.LiveLinkComponentController.on_controller_map_updated_delegate(value: OnControllerMapUpdatedDelegate) -> None
unreal.LiveLinkComponentController.on_live_link_updated(value: LiveLinkTickDelegate) -> None
unreal.LiveLinkComponentController.set_controlled_component(role_class: Class, component: ActorComponent) -> None
unreal.LiveLinkComponentController.subject_representation(value: LiveLinkSubjectRepresentation) -> None
```

## `unreal.LiveLinkGamepadInputDeviceFrameData(LiveLinkBaseFrameData)`

```python
unreal.LiveLinkGamepadInputDeviceFrameData.__init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]], property_values: Array[float] = [], left_analog_x: float = 0.000000, left_analog_y: float = 0.000000, right_analog_x: float = 0.000000, right_analog_y: float = 0.000000, left_trigger_analog: float = 0.000000, right_trigger_analog: float = 0.000000, left_thumb: float = 0.000000, right_thumb: float = 0.000000, special_left: float = 0.000000, special_left_x: float = 0.000000, special_left_y: float = 0.000000, special_right: float = 0.000000, face_button_bottom: float = 0.000000, face_button_right: float = 0.000000, face_button_left: float = 0.000000, face_button_top: float = 0.000000, left_shoulder: float = 0.000000, right_shoulder: float = 0.000000, left_trigger_threshold: float = 0.000000, right_trigger_threshold: float = 0.000000, d_pad_up: float = 0.000000, d_pad_down: float = 0.000000, d_pad_right: float = 0.000000, d_pad_left: float = 0.000000, left_stick_up: float = 0.000000, left_stick_down: float = 0.000000, left_stick_right: float = 0.000000, left_stick_left: float = 0.000000, right_stick_up: float = 0.000000, right_stick_down: float = 0.000000, right_stick_right: float = 0.000000, right_stick_left: float = 0.000000) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_down(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_left(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_right(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_up(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.face_button_bottom(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.face_button_left(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.face_button_right(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.face_button_top(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_x(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_y(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_shoulder(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_down(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_left(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_right(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_up(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_thumb(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_analog(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_threshold(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_x(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_y(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_shoulder(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_down(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_left(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_right(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_up(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_thumb(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_analog(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_threshold(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.special_left(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.special_left_x(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.special_left_y(value: float) -> None
unreal.LiveLinkGamepadInputDeviceFrameData.special_right(value: float) -> None
```

## `unreal.LiveLinkGamepadInputDeviceStaticData(LiveLinkBaseStaticData)`

```python
unreal.LiveLinkGamepadInputDeviceStaticData.__init__(property_names: Array[Name] = []) -> None
```

## `unreal.LocalPlayerSaveGame(SaveGame)`

```python
unreal.LocalPlayerSaveGame.async_load_or_create_save_game_for_local_player(save_game_class: Class, local_player_controller: PlayerController, slot_name: str, delegate: OnLocalPlayerSaveGameLoaded) -> bool
unreal.LocalPlayerSaveGame.async_save_game_to_slot_for_local_player() -> bool
unreal.LocalPlayerSaveGame.get_invalid_data_version() -> int
unreal.LocalPlayerSaveGame.get_latest_data_version() -> int
unreal.LocalPlayerSaveGame.get_local_player_controller() -> PlayerController
unreal.LocalPlayerSaveGame.get_platform_user_id() -> PlatformUserId
unreal.LocalPlayerSaveGame.get_platform_user_index() -> int
unreal.LocalPlayerSaveGame.get_save_slot_name() -> str
unreal.LocalPlayerSaveGame.get_saved_data_version() -> int
unreal.LocalPlayerSaveGame.is_save_in_progress() -> bool
unreal.LocalPlayerSaveGame.load_or_create_save_game_for_local_player(save_game_class: Class, local_player_controller: PlayerController, slot_name: str) -> LocalPlayerSaveGame
unreal.LocalPlayerSaveGame.on_post_load() -> None
unreal.LocalPlayerSaveGame.on_post_save(success: bool) -> None
unreal.LocalPlayerSaveGame.on_pre_save() -> None
unreal.LocalPlayerSaveGame.on_reset_to_default() -> None
unreal.LocalPlayerSaveGame.reset_to_default() -> None
unreal.LocalPlayerSaveGame.save_game_to_slot_for_local_player() -> bool
unreal.LocalPlayerSaveGame.was_last_save_successful() -> bool
unreal.LocalPlayerSaveGame.was_loaded() -> bool
unreal.LocalPlayerSaveGame.was_save_requested() -> bool
```

## `unreal.MapPlayerKeyArgs(StructBase)`

```python
unreal.MapPlayerKeyArgs.__init__(mapping_name: Name = "None", slot: PlayerMappableKeySlot = PlayerMappableKeySlot.FIRST, new_key: Key = [], hardware_device_id: Name = "None", profile_id: GameplayTag = ["None"], create_matching_slot_if_needed: bool = False, defer_on_settings_changed_broadcast: bool = False) -> None
unreal.MapPlayerKeyArgs.create_matching_slot_if_needed(value: bool) -> None
unreal.MapPlayerKeyArgs.defer_on_settings_changed_broadcast(value: bool) -> None
unreal.MapPlayerKeyArgs.hardware_device_id(value: Name) -> None
unreal.MapPlayerKeyArgs.mapping_name(value: Name) -> None
unreal.MapPlayerKeyArgs.new_key(value: Key) -> None
unreal.MapPlayerKeyArgs.profile_id(value: GameplayTag) -> None
unreal.MapPlayerKeyArgs.slot(value: PlayerMappableKeySlot) -> None
```

## `unreal.MediaPlayer(Object)`

```python
unreal.MediaPlayer.affected_by_pie_handling(value: bool) -> None
unreal.MediaPlayer.cache_ahead(value: Timespan) -> None
unreal.MediaPlayer.cache_behind(value: Timespan) -> None
unreal.MediaPlayer.cache_behind_game(value: Timespan) -> None
unreal.MediaPlayer.can_pause() -> bool
unreal.MediaPlayer.can_play_source(media_source: MediaSource) -> bool
unreal.MediaPlayer.can_play_url(url: str) -> bool
unreal.MediaPlayer.close() -> None
unreal.MediaPlayer.get_audio_track_channels(track_index: int, format_index: int) -> int
unreal.MediaPlayer.get_audio_track_sample_rate(track_index: int, format_index: int) -> int
unreal.MediaPlayer.get_audio_track_type(track_index: int, format_index: int) -> str
unreal.MediaPlayer.get_desired_player_name() -> Name
unreal.MediaPlayer.get_display_time() -> Timespan
unreal.MediaPlayer.get_display_time_stamp() -> MediaTimeStampInfo
unreal.MediaPlayer.get_duration() -> Timespan
unreal.MediaPlayer.get_horizontal_field_of_view() -> float
unreal.MediaPlayer.get_media_metadata_items() -> Map[str, MediaMetadataItemsBPT]
unreal.MediaPlayer.get_media_name() -> Text
unreal.MediaPlayer.get_num_track_formats(track_type: MediaPlayerTrack, track_index: int) -> int
unreal.MediaPlayer.get_num_tracks(track_type: MediaPlayerTrack) -> int
unreal.MediaPlayer.get_playback_time_range(range_to_get: MediaTimeRangeBPType) -> FloatInterval
unreal.MediaPlayer.get_player_name() -> Name
unreal.MediaPlayer.get_playlist() -> MediaPlaylist
unreal.MediaPlayer.get_playlist_index() -> int
unreal.MediaPlayer.get_rate() -> float
unreal.MediaPlayer.get_selected_track(track_type: MediaPlayerTrack) -> int
unreal.MediaPlayer.get_supported_rates(unthinned: bool) -> Array[FloatRange]
unreal.MediaPlayer.get_time() -> Timespan
unreal.MediaPlayer.get_time_delay() -> Timespan
unreal.MediaPlayer.get_time_stamp() -> MediaTimeStampInfo
unreal.MediaPlayer.get_track_display_name(track_type: MediaPlayerTrack, track_index: int) -> Text
unreal.MediaPlayer.get_track_format(track_type: MediaPlayerTrack, track_index: int) -> int
unreal.MediaPlayer.get_track_language(track_type: MediaPlayerTrack, track_index: int) -> str
unreal.MediaPlayer.get_url() -> str
unreal.MediaPlayer.get_vertical_field_of_view() -> float
unreal.MediaPlayer.get_video_track_aspect_ratio(track_index: int, format_index: int) -> float
unreal.MediaPlayer.get_video_track_dimensions(track_index: int, format_index: int) -> IntPoint
unreal.MediaPlayer.get_video_track_frame_rate(track_index: int, format_index: int) -> float
unreal.MediaPlayer.get_video_track_frame_rates(track_index: int, format_index: int) -> FloatRange
unreal.MediaPlayer.get_video_track_type(track_index: int, format_index: int) -> str
unreal.MediaPlayer.get_view_rotation() -> Rotator
unreal.MediaPlayer.has_error() -> bool
unreal.MediaPlayer.is_buffering() -> bool
unreal.MediaPlayer.is_closed() -> bool
unreal.MediaPlayer.is_connecting() -> bool
unreal.MediaPlayer.is_looping() -> bool
unreal.MediaPlayer.is_paused() -> bool
unreal.MediaPlayer.is_playing() -> bool
unreal.MediaPlayer.is_preparing() -> bool
unreal.MediaPlayer.is_ready() -> bool
unreal.MediaPlayer.loop() -> bool
unreal.MediaPlayer.native_audio_out(value: bool) -> None
unreal.MediaPlayer.next() -> bool
unreal.MediaPlayer.on_end_reached(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_media_closed(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_media_open_failed(value: OnMediaPlayerMediaOpenFailed) -> None
unreal.MediaPlayer.on_media_opened(value: OnMediaPlayerMediaOpened) -> None
unreal.MediaPlayer.on_metadata_changed(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_playback_resumed(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_playback_suspended(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_seek_completed(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.on_tracks_changed(value: OnMediaPlayerMediaEvent) -> None
unreal.MediaPlayer.open_file(file_path: str) -> bool
unreal.MediaPlayer.open_playlist(playlist: MediaPlaylist) -> bool
unreal.MediaPlayer.open_playlist_index(playlist: MediaPlaylist, index: int) -> bool
unreal.MediaPlayer.open_source(media_source: MediaSource) -> bool
unreal.MediaPlayer.open_source_latent(world_context_object: Object, latent_info: LatentActionInfo, media_source: MediaSource, options: MediaPlayerOptions) -> bool
unreal.MediaPlayer.open_source_with_options(media_source: MediaSource, options: MediaPlayerOptions) -> bool
unreal.MediaPlayer.open_url(url: str) -> bool
unreal.MediaPlayer.pause() -> bool
unreal.MediaPlayer.play() -> bool
unreal.MediaPlayer.play_and_seek() -> None
unreal.MediaPlayer.play_on_open(value: bool) -> None
unreal.MediaPlayer.playlist() -> MediaPlaylist
unreal.MediaPlayer.playlist_index() -> int
unreal.MediaPlayer.previous() -> bool
unreal.MediaPlayer.reopen() -> bool
unreal.MediaPlayer.rewind() -> bool
unreal.MediaPlayer.seek(time: Timespan) -> bool
unreal.MediaPlayer.select_track(track_type: MediaPlayerTrack, track_index: int) -> bool
unreal.MediaPlayer.set_block_on_time(time: Timespan) -> None
unreal.MediaPlayer.set_desired_player_name(player_name: Name) -> None
unreal.MediaPlayer.set_looping(looping: bool) -> bool
unreal.MediaPlayer.set_media_options(options: MediaSource) -> None
unreal.MediaPlayer.set_native_volume(volume: float) -> bool
unreal.MediaPlayer.set_playback_time_range(time_range: FloatInterval) -> bool
unreal.MediaPlayer.set_rate(rate: float) -> bool
unreal.MediaPlayer.set_time_delay(time_delay: Timespan) -> None
unreal.MediaPlayer.set_track_format(track_type: MediaPlayerTrack, track_index: int, format_index: int) -> bool
unreal.MediaPlayer.set_video_track_frame_rate(track_index: int, format_index: int, frame_rate: float) -> bool
unreal.MediaPlayer.set_view_field(horizontal: float, vertical: float, absolute: bool) -> bool
unreal.MediaPlayer.set_view_rotation(rotation: Rotator, absolute: bool) -> bool
unreal.MediaPlayer.shuffle(value: bool) -> None
unreal.MediaPlayer.supports_playback_time_range() -> bool
unreal.MediaPlayer.supports_rate(rate: float, unthinned: bool) -> bool
unreal.MediaPlayer.supports_scrubbing() -> bool
unreal.MediaPlayer.supports_seeking() -> bool
unreal.MediaPlayer.time_delay() -> Timespan
```

## `unreal.MediaPlayerEditorMediaContext(ToolMenuContextBase)`

```python
unreal.MediaPlayerEditorMediaContext.selected_asset(value: Object) -> None
unreal.MediaPlayerEditorMediaContext.style_set_name(value: Name) -> None
```

## `unreal.MediaPlayerOptions(StructBase)`

```python
unreal.MediaPlayerOptions.__init__(tracks: MediaPlayerTrackOptions = [0, -1, -1, -1, -1, -1, 0], track_selection: MediaPlayerOptionTrackSelectMode = MediaPlayerOptionTrackSelectMode.USE_MEDIA_PLAYER_DEFAULTS, seek_time: Timespan = [0, 0, 0, 0, 0], seek_time_type: MediaPlayerOptionSeekTimeType = MediaPlayerOptionSeekTimeType.IGNORED, play_on_open: MediaPlayerOptionBooleanOverride = MediaPlayerOptionBooleanOverride.USE_MEDIA_PLAYER_SETTING, loop: MediaPlayerOptionBooleanOverride = MediaPlayerOptionBooleanOverride.USE_MEDIA_PLAYER_SETTING) -> None
unreal.MediaPlayerOptions.loop(value: MediaPlayerOptionBooleanOverride) -> None
unreal.MediaPlayerOptions.play_on_open(value: MediaPlayerOptionBooleanOverride) -> None
unreal.MediaPlayerOptions.seek_time(value: Timespan) -> None
unreal.MediaPlayerOptions.seek_time_type(value: MediaPlayerOptionSeekTimeType) -> None
unreal.MediaPlayerOptions.track_selection(value: MediaPlayerOptionTrackSelectMode) -> None
unreal.MediaPlayerOptions.tracks(value: MediaPlayerTrackOptions) -> None
```

## `unreal.MediaPlayerTrackOptions(StructBase)`

```python
unreal.MediaPlayerTrackOptions.__init__(audio: int = 0, caption: int = 0, metadata: int = 0, script: int = 0, subtitle: int = 0, text: int = 0, video: int = 0) -> None
unreal.MediaPlayerTrackOptions.audio(value: int) -> None
unreal.MediaPlayerTrackOptions.caption(value: int) -> None
unreal.MediaPlayerTrackOptions.metadata(value: int) -> None
unreal.MediaPlayerTrackOptions.script(value: int) -> None
unreal.MediaPlayerTrackOptions.subtitle(value: int) -> None
unreal.MediaPlayerTrackOptions.text(value: int) -> None
unreal.MediaPlayerTrackOptions.video(value: int) -> None
```

## `unreal.MotionControllerComponent(PrimitiveComponent)`

```python
unreal.MotionControllerComponent.current_tracking_status() -> TrackingStatus
unreal.MotionControllerComponent.disable_low_latency_update(value: bool) -> None
unreal.MotionControllerComponent.get_angular_velocity() -> Optional[Rotator]
unreal.MotionControllerComponent.get_hand_joint_position(joint_index: int) -> Tuple[Vector, bool]
unreal.MotionControllerComponent.get_linear_acceleration() -> Optional[Vector]
unreal.MotionControllerComponent.get_linear_velocity() -> Optional[Vector]
unreal.MotionControllerComponent.get_parameter_value(name: Name) -> Tuple[float, bool]
unreal.MotionControllerComponent.is_tracked() -> bool
unreal.MotionControllerComponent.motion_source(value: Name) -> None
unreal.MotionControllerComponent.on_motion_controller_updated() -> None
unreal.MotionControllerComponent.player_index(value: int) -> None
```

## `unreal.MotionProcessInput(StructBase)`

```python
unreal.MotionProcessInput.__init__() -> None
```

## `unreal.MouseInputDeviceState(StructBase)`

```python
unreal.MouseInputDeviceState.__init__(left: DeviceButtonState = [[], False, False, False, False], middle: DeviceButtonState = [[], False, False, False, False], right: DeviceButtonState = [[], False, False, False, False], wheel_delta: float = 0.000000, position2d: Vector2D = [0.000000, 0.000000], delta2d: Vector2D = [0.000000, 0.000000], world_ray: Ray = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]]) -> None
unreal.MouseInputDeviceState.delta2d(value: Vector2D) -> None
unreal.MouseInputDeviceState.left(value: DeviceButtonState) -> None
unreal.MouseInputDeviceState.middle(value: DeviceButtonState) -> None
unreal.MouseInputDeviceState.position2d(value: Vector2D) -> None
unreal.MouseInputDeviceState.right(value: DeviceButtonState) -> None
unreal.MouseInputDeviceState.wheel_delta(value: float) -> None
unreal.MouseInputDeviceState.world_ray(value: Ray) -> None
```

## `unreal.OnCameraMotionEndEvent(EventArgsBase)`

```python
unreal.OnCameraMotionEndEvent.__init__(camera_motion_reason: str = "", eids: Array[str] = []) -> None
unreal.OnCameraMotionEndEvent.camera_motion_reason(value: str) -> None
unreal.OnCameraMotionEndEvent.eids(value: Array[str]) -> None
```

## `unreal.OnCameraMotionStartEvent(EventArgsBase)`

```python
unreal.OnCameraMotionStartEvent.__init__(camera_motion_reason: str = "") -> None
unreal.OnCameraMotionStartEvent.camera_motion_reason(value: str) -> None
```

## `unreal.OnControllerCaptureBeginEvent(MulticastDelegateBase)`

```python
unreal.OnControllerCaptureBeginEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnControllerCaptureEndEvent(MulticastDelegateBase)`

```python
unreal.OnControllerCaptureEndEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnControllerMapUpdatedDelegate(MulticastDelegateBase)`

```python
unreal.OnControllerMapUpdatedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnInputAction(DelegateBase)`

```python
unreal.OnInputAction.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLocalPlayerSaveGameLoaded(DelegateBase)`

```python
unreal.OnLocalPlayerSaveGameLoaded.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMediaPlayerMediaEvent(MulticastDelegateBase)`

```python
unreal.OnMediaPlayerMediaEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMediaPlayerMediaOpenFailed(MulticastDelegateBase)`

```python
unreal.OnMediaPlayerMediaOpenFailed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMediaPlayerMediaOpened(MulticastDelegateBase)`

```python
unreal.OnMediaPlayerMediaOpened.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnPawnControllerChanged(MulticastDelegateBase)`

```python
unreal.OnPawnControllerChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnPlayerStatePawnSet(MulticastDelegateBase)`

```python
unreal.OnPlayerStatePawnSet.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnPossessedPawnChanged(MulticastDelegateBase)`

```python
unreal.OnPossessedPawnChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnUserInputDeviceConnectionChange(MulticastDelegateBase)`

```python
unreal.OnUserInputDeviceConnectionChange.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnUserInputDevicePairingChange(MulticastDelegateBase)`

```python
unreal.OnUserInputDevicePairingChange.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OptimusSecondaryInputBindingsGroup(StructBase)`

```python
unreal.OptimusSecondaryInputBindingsGroup.__init__() -> None
```

## `unreal.PaperCharacter(Character)`

```python
unreal.PaperCharacter.sprite() -> PaperFlipbookComponent
```

## `unreal.ParticleSpawnSignature(MulticastDelegateBase)`

```python
unreal.ParticleSpawnSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Pawn(Actor)`

```python
unreal.Pawn.add_controller_pitch_input(val: float) -> None
unreal.Pawn.add_controller_roll_input(val: float) -> None
unreal.Pawn.add_controller_yaw_input(val: float) -> None
unreal.Pawn.add_look_up_input(val: float) -> None
unreal.Pawn.add_movement_input(world_direction: Vector, scale_value: float = 1.000000, force: bool = False) -> None
unreal.Pawn.add_pitch_input(val: float) -> None
unreal.Pawn.add_roll_input(val: float) -> None
unreal.Pawn.add_turn_input(val: float) -> None
unreal.Pawn.add_yaw_input(val: float) -> None
unreal.Pawn.ai_controller_class(value: Class) -> None
unreal.Pawn.base_eye_height(value: float) -> None
unreal.Pawn.can_affect_navigation_generation() -> bool
unreal.Pawn.consume_movement_input_vector() -> Vector
unreal.Pawn.controller_class(value: Class) -> None
unreal.Pawn.detach_from_controller_pending_destroy() -> None
unreal.Pawn.get_base_aim_rotation() -> Rotator
unreal.Pawn.get_control_rotation() -> Rotator
unreal.Pawn.get_controller() -> Controller
unreal.Pawn.get_last_movement_input_vector() -> Vector
unreal.Pawn.get_local_viewing_player_controller() -> PlayerController
unreal.Pawn.get_movement_base_actor(pawn: Pawn) -> Actor
unreal.Pawn.get_movement_component() -> PawnMovementComponent
unreal.Pawn.get_nav_agent_location() -> Vector
unreal.Pawn.get_override_input_component_class() -> Class
unreal.Pawn.get_pending_movement_input_vector() -> Vector
unreal.Pawn.get_platform_user_id() -> PlatformUserId
unreal.Pawn.is_bot_controlled() -> bool
unreal.Pawn.is_controlled() -> bool
unreal.Pawn.is_locally_controlled() -> bool
unreal.Pawn.is_locally_viewed() -> bool
unreal.Pawn.is_move_input_ignored() -> bool
unreal.Pawn.is_pawn_controlled() -> bool
unreal.Pawn.is_player_controlled() -> bool
unreal.Pawn.last_hit_by() -> Controller
unreal.Pawn.pawn_make_noise(loudness: float, noise_location: Vector, use_noise_maker_location: bool = True, noise_maker: Actor = None) -> None
unreal.Pawn.player_replication_info() -> PlayerState
unreal.Pawn.player_state() -> PlayerState
unreal.Pawn.receive_controller_changed(old_controller: Controller, new_controller: Controller) -> None
unreal.Pawn.receive_controller_changed_delegate(value: PawnControllerChangedSignature) -> None
unreal.Pawn.receive_possessed(new_controller: Controller) -> None
unreal.Pawn.receive_restarted() -> None
unreal.Pawn.receive_restarted_delegate(value: PawnRestartedSignature) -> None
unreal.Pawn.receive_unpossessed(old_controller: Controller) -> None
unreal.Pawn.set_can_affect_navigation_generation(new_value: bool, force_update: bool = False) -> None
unreal.Pawn.spawn_default_controller() -> None
unreal.Pawn.use_controller_rotation_pitch(value: bool) -> None
unreal.Pawn.use_controller_rotation_roll(value: bool) -> None
unreal.Pawn.use_controller_rotation_yaw(value: bool) -> None
```

## `unreal.PawnAction(Object)`

```python
unreal.PawnAction.allow_new_same_class_instance() -> bool
unreal.PawnAction.always_notify_on_finished(value: bool) -> None
unreal.PawnAction.create_action_instance(world_context_object: Object, action_class: Class) -> PawnAction
unreal.PawnAction.finish(with_result: PawnActionResult) -> None
unreal.PawnAction.get_action_priority() -> AIRequestPriority
unreal.PawnAction.replace_active_same_class_instance(value: bool) -> None
unreal.PawnAction.should_pause_movement(value: bool) -> None
```

## `unreal.PawnAction_Move(PawnAction)`

```python
unreal.PawnAction_Move.acceptable_radius(value: float) -> None
unreal.PawnAction_Move.allow_strafe(value: bool) -> None
unreal.PawnAction_Move.filter_class(value: Class) -> None
unreal.PawnAction_Move.goal_actor(value: Actor) -> None
unreal.PawnAction_Move.goal_location(value: Vector) -> None
```

## `unreal.PawnAction_Repeat(PawnAction)`

```python
unreal.PawnAction_Repeat.child_failure_handling_mode() -> PawnActionFailHandling
```

## `unreal.PawnAction_Sequence(PawnAction)`

```python
unreal.PawnAction_Sequence.child_failure_handling_mode() -> PawnActionFailHandling
```

## `unreal.PawnActionsComponent(ActorComponent)`

```python
unreal.PawnActionsComponent.abort_action(action_to_abort: PawnAction) -> PawnActionAbortState
unreal.PawnActionsComponent.controlled_pawn() -> Pawn
unreal.PawnActionsComponent.force_abort_action(action_to_abort: PawnAction) -> PawnActionAbortState
unreal.PawnActionsComponent.perform_action(pawn: Pawn, action: PawnAction, priority: AIRequestPriority = AIRequestPriority.HARD_SCRIPT) -> bool
unreal.PawnActionsComponent.push_action(new_action: PawnAction, priority: AIRequestPriority, instigator: Object = None) -> bool
```

## `unreal.PawnControllerChangedSignature(MulticastDelegateBase)`

```python
unreal.PawnControllerChangedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PawnInnerDelegate(MulticastDelegateBase)`

```python
unreal.PawnInnerDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PawnMovementComponent(NavMovementComponent)`

```python
unreal.PawnMovementComponent.add_input_vector(world_vector: Vector, force: bool = False) -> None
unreal.PawnMovementComponent.consume_input_vector() -> Vector
unreal.PawnMovementComponent.get_input_vector() -> Vector
unreal.PawnMovementComponent.get_last_input_vector() -> Vector
unreal.PawnMovementComponent.get_pawn_owner() -> Pawn
unreal.PawnMovementComponent.get_pending_input_vector() -> Vector
unreal.PawnMovementComponent.is_move_input_ignored() -> bool
```

## `unreal.PawnNoiseEmitterComponent(ActorComponent)`

```python
unreal.PawnNoiseEmitterComponent.make_noise(noise_maker: Actor, loudness: float, noise_location: Vector) -> None
unreal.PawnNoiseEmitterComponent.noise_lifetime(value: float) -> None
```

## `unreal.PawnRestartedSignature(MulticastDelegateBase)`

```python
unreal.PawnRestartedSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PawnSensingComponent(ActorComponent)`

```python
unreal.PawnSensingComponent.b_wants_see_player_notify(value: bool) -> None
unreal.PawnSensingComponent.enable_sensing_updates() -> bool
unreal.PawnSensingComponent.get_peripheral_vision_angle() -> float
unreal.PawnSensingComponent.get_peripheral_vision_cosine() -> float
unreal.PawnSensingComponent.hear_noises(value: bool) -> None
unreal.PawnSensingComponent.hearing_max_sound_age(value: float) -> None
unreal.PawnSensingComponent.hearing_threshold(value: float) -> None
unreal.PawnSensingComponent.los_hearing_threshold(value: float) -> None
unreal.PawnSensingComponent.on_hear_noise(value: HearNoiseDelegate) -> None
unreal.PawnSensingComponent.on_see_pawn(value: SeePawnDelegate) -> None
unreal.PawnSensingComponent.only_sense_players(value: bool) -> None
unreal.PawnSensingComponent.peripheral_vision_angle() -> float
unreal.PawnSensingComponent.see_pawns(value: bool) -> None
unreal.PawnSensingComponent.sensing_interval() -> float
unreal.PawnSensingComponent.set_peripheral_vision_angle(new_peripheral_vision_angle: float) -> None
unreal.PawnSensingComponent.set_sensing_interval(new_sensing_interval: float) -> None
unreal.PawnSensingComponent.set_sensing_updates_enabled(enabled: bool) -> None
unreal.PawnSensingComponent.sight_counter_interval() -> float
unreal.PawnSensingComponent.sight_radius(value: float) -> None
```

## `unreal.PawnSensingComponent_HearNoiseDelegate(MulticastDelegateBase)`

```python
unreal.PawnSensingComponent_HearNoiseDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PawnSensingComponent_SeePawnDelegate(MulticastDelegateBase)`

```python
unreal.PawnSensingComponent_SeePawnDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PendingDelayedSpawn(StructBase)`

```python
unreal.PendingDelayedSpawn.__init__() -> None
```

## `unreal.PerlinNoiseCameraShakePattern(SimpleCameraShakePattern)`

```python
unreal.PerlinNoiseCameraShakePattern.fov(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.location_amplitude_multiplier(value: float) -> None
unreal.PerlinNoiseCameraShakePattern.location_frequency_multiplier(value: float) -> None
unreal.PerlinNoiseCameraShakePattern.pitch(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.roll(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.rotation_amplitude_multiplier(value: float) -> None
unreal.PerlinNoiseCameraShakePattern.rotation_frequency_multiplier(value: float) -> None
unreal.PerlinNoiseCameraShakePattern.x(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.y(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.yaw(value: PerlinNoiseShaker) -> None
unreal.PerlinNoiseCameraShakePattern.z(value: PerlinNoiseShaker) -> None
```

## `unreal.PixelStreamer51CloudInputComponent(ActorComponent)`

```python
unreal.PixelStreamer51CloudInputComponent.add_json_string_value(descriptor: str, field_name: str, string_value: str) -> Tuple[str, bool]
unreal.PixelStreamer51CloudInputComponent.get_json_string_value(descriptor: str, field_name: str) -> Tuple[str, bool]
unreal.PixelStreamer51CloudInputComponent.on_input_event(value: OnInput) -> None
unreal.PixelStreamer51CloudInputComponent.on_large_data_bp(value: OnLargeData_BP) -> None
unreal.PixelStreamer51CloudInputComponent.on_large_string_bp(value: OnLargeString_BP) -> None
unreal.PixelStreamer51CloudInputComponent.query_max_fps() -> float
unreal.PixelStreamer51CloudInputComponent.query_max_res_x() -> int
unreal.PixelStreamer51CloudInputComponent.query_max_res_y() -> int
unreal.PixelStreamer51CloudInputComponent.query_min_fps() -> float
unreal.PixelStreamer51CloudInputComponent.query_min_res_x() -> int
unreal.PixelStreamer51CloudInputComponent.query_min_res_y() -> int
unreal.PixelStreamer51CloudInputComponent.send_command_to_agent(descriptor: str) -> None
unreal.PixelStreamer51CloudInputComponent.send_message_to_agent(msg: AgentMessage) -> None
unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_large_data(large_data: Array[int]) -> None
unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_large_string(large_string: str) -> None
unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_notification(type: NotificationType, msg: str) -> None
unreal.PixelStreamer51CloudInputComponent.send_pixel_streaming_response(descriptor: str, rtc_channel_type: RtcChannelType = RtcChannelType.AUTO) -> None
```

## `unreal.PixelStreamer51CloudInputComponent_OnInput(MulticastDelegateBase)`

```python
unreal.PixelStreamer51CloudInputComponent_OnInput.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PixelStreamer51CloudInputComponent_OnLargeData_BP(MulticastDelegateBase)`

```python
unreal.PixelStreamer51CloudInputComponent_OnLargeData_BP.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PixelStreamer51CloudInputComponent_OnLargeString_BP(MulticastDelegateBase)`

```python
unreal.PixelStreamer51CloudInputComponent_OnLargeString_BP.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PlatformInputDeviceState(StructBase)`

```python
unreal.PlatformInputDeviceState.__init__(owning_platform_user: PlatformUserId = [], connection_state: InputDeviceConnectionState = InputDeviceConnectionState.INVALID) -> None
unreal.PlatformInputDeviceState.connection_state() -> InputDeviceConnectionState
unreal.PlatformInputDeviceState.owning_platform_user() -> PlatformUserId
```

## `unreal.PlayerCameraManager(Actor)`

```python
unreal.PlayerCameraManager.add_generic_camera_lens_effect(lens_effect_emitter_class: Class) -> CameraLensEffectInterface
unreal.PlayerCameraManager.add_new_camera_modifier(modifier_class: Class) -> CameraModifier
unreal.PlayerCameraManager.auto_calculate_ortho_planes(value: bool) -> None
unreal.PlayerCameraManager.auto_plane_shift(value: float) -> None
unreal.PlayerCameraManager.blueprint_update_camera(camera_target: Actor) -> Optional[Tuple[Vector, Rotator, float]]
unreal.PlayerCameraManager.clear_camera_lens_effects() -> None
unreal.PlayerCameraManager.client_simulating_view_target(value: bool) -> None
unreal.PlayerCameraManager.default_aspect_ratio(value: float) -> None
unreal.PlayerCameraManager.default_constrain_aspect_ratio(value: bool) -> None
unreal.PlayerCameraManager.default_fov(value: float) -> None
unreal.PlayerCameraManager.default_modifiers() -> Array[Class]
unreal.PlayerCameraManager.default_ortho_width(value: float) -> None
unreal.PlayerCameraManager.find_camera_modifier_by_class(modifier_class: Class) -> CameraModifier
unreal.PlayerCameraManager.free_cam_distance(value: float) -> None
unreal.PlayerCameraManager.free_cam_offset(value: Vector) -> None
unreal.PlayerCameraManager.game_camera_cut_this_frame() -> bool
unreal.PlayerCameraManager.get_camera_location() -> Vector
unreal.PlayerCameraManager.get_camera_rotation() -> Rotator
unreal.PlayerCameraManager.get_fov_angle() -> float
unreal.PlayerCameraManager.get_owning_player_controller() -> PlayerController
unreal.PlayerCameraManager.is_orthographic(value: bool) -> None
unreal.PlayerCameraManager.kismet_update_camera(camera_target: Actor) -> Optional[Tuple[Vector, Rotator, float]]
unreal.PlayerCameraManager.on_audio_fade_change_event(value: OnAudioFadeChangeSignature) -> None
unreal.PlayerCameraManager.on_photography_multi_part_capture_end() -> None
unreal.PlayerCameraManager.on_photography_multi_part_capture_start() -> None
unreal.PlayerCameraManager.on_photography_session_end() -> None
unreal.PlayerCameraManager.on_photography_session_start() -> None
unreal.PlayerCameraManager.photography_camera_modify(new_camera_location: Vector, previous_camera_location: Vector, original_camera_location: Vector) -> Vector
unreal.PlayerCameraManager.play_camera_shake(shake_class: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.play_camera_shake_from_source(shake_class: Class, source_component: CameraShakeSourceComponent, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.remove_camera_modifier(modifier_to_remove: CameraModifier) -> bool
unreal.PlayerCameraManager.remove_generic_camera_lens_effect(emitter: CameraLensEffectInterface) -> None
unreal.PlayerCameraManager.set_game_camera_cut_this_frame() -> None
unreal.PlayerCameraManager.set_manual_camera_fade(fade_amount: float, color: LinearColor, fade_audio: bool) -> None
unreal.PlayerCameraManager.start_camera_fade(from_alpha: float, to_alpha: float, duration: float, color: LinearColor, should_fade_audio: bool = False, hold_when_finished: bool = False) -> None
unreal.PlayerCameraManager.start_camera_shake(shake_class: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.start_camera_shake_from_source(shake_class: Class, source_component: CameraShakeSourceComponent, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.start_matinee_camera_shake(shake_class: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.start_matinee_camera_shake_from_source(shake_class: Class, source_component: CameraShakeSourceComponent, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> CameraShakeBase
unreal.PlayerCameraManager.stop_all_camera_shakes(immediately: bool = True) -> None
unreal.PlayerCameraManager.stop_all_camera_shakes_from_source(source_component: CameraShakeSourceComponent, immediately: bool = True) -> None
unreal.PlayerCameraManager.stop_all_instances_of_camera_shake(shake: Class, immediately: bool = True) -> None
unreal.PlayerCameraManager.stop_all_instances_of_camera_shake_from_source(shake: Class, source_component: CameraShakeSourceComponent, immediately: bool = True) -> None
unreal.PlayerCameraManager.stop_camera_fade() -> None
unreal.PlayerCameraManager.stop_camera_shake(shake_instance: CameraShakeBase, immediately: bool = True) -> None
unreal.PlayerCameraManager.transform_component() -> SceneComponent
unreal.PlayerCameraManager.update_ortho_planes(value: bool) -> None
unreal.PlayerCameraManager.use_camera_height_as_view_target(value: bool) -> None
unreal.PlayerCameraManager.use_client_side_camera_updates() -> bool
unreal.PlayerCameraManager.view_pitch_max(value: float) -> None
unreal.PlayerCameraManager.view_pitch_min(value: float) -> None
unreal.PlayerCameraManager.view_roll_max(value: float) -> None
unreal.PlayerCameraManager.view_roll_min(value: float) -> None
unreal.PlayerCameraManager.view_target_offset(value: Vector) -> None
unreal.PlayerCameraManager.view_yaw_max(value: float) -> None
unreal.PlayerCameraManager.view_yaw_min(value: float) -> None
```

## `unreal.PlayerController(Controller)`

```python
unreal.PlayerController.activate_touch_interface(new_touch_interface: TouchInterface) -> None
unreal.PlayerController.add_look_up_input(val: float) -> None
unreal.PlayerController.add_pitch_input(val: float) -> None
unreal.PlayerController.add_roll_input(val: float) -> None
unreal.PlayerController.add_turn_input(val: float) -> None
unreal.PlayerController.add_yaw_input(val: float) -> None
unreal.PlayerController.can_restart_player() -> bool
unreal.PlayerController.cheat_class() -> Class
unreal.PlayerController.cheat_manager() -> CheatManager
unreal.PlayerController.clear_audio_listener_attenuation_override() -> None
unreal.PlayerController.clear_audio_listener_override() -> None
unreal.PlayerController.click_event_keys(value: Array[Key]) -> None
unreal.PlayerController.client_clear_camera_lens_effects() -> None
unreal.PlayerController.client_play_camera_shake(shake: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.PlayerController.client_play_camera_shake_from_source(shake: Class, source_component: CameraShakeSourceComponent) -> None
unreal.PlayerController.client_play_force_feedback(force_feedback_effect: ForceFeedbackEffect, tag: Name, looping: bool, ignore_time_dilation: bool, play_while_paused: bool) -> None
unreal.PlayerController.client_set_hud(new_hud_class: Class) -> None
unreal.PlayerController.client_spawn_generic_camera_lens_effect(lens_effect_emitter_class: Class) -> None
unreal.PlayerController.client_start_camera_shake(shake: Class, scale: float = 1.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.PlayerController.client_start_camera_shake_from_source(shake: Class, source_component: CameraShakeSourceComponent) -> None
unreal.PlayerController.client_stop_camera_shake(shake: Class, immediately: bool = True) -> None
unreal.PlayerController.client_stop_camera_shakes_from_source(source_component: CameraShakeSourceComponent, immediately: bool = True) -> None
unreal.PlayerController.client_stop_force_feedback(force_feedback_effect: ForceFeedbackEffect, tag: Name) -> None
unreal.PlayerController.current_click_trace_channel(value: CollisionChannel) -> None
unreal.PlayerController.current_mouse_cursor(value: MouseCursor) -> None
unreal.PlayerController.default_click_trace_channel() -> CollisionChannel
unreal.PlayerController.default_mouse_cursor() -> MouseCursor
unreal.PlayerController.deproject_mouse_position_to_world() -> Optional[Tuple[Vector, Vector]]
unreal.PlayerController.deproject_screen_position_to_world(screen_x: float, screen_y: float) -> Optional[Tuple[Vector, Vector]]
unreal.PlayerController.enable_click_events(value: bool) -> None
unreal.PlayerController.enable_motion_controls(value: bool) -> None
unreal.PlayerController.enable_mouse_over_events(value: bool) -> None
unreal.PlayerController.enable_streaming_source(value: bool) -> None
unreal.PlayerController.enable_touch_events(value: bool) -> None
unreal.PlayerController.enable_touch_over_events(value: bool) -> None
unreal.PlayerController.force_feedback_enabled(value: bool) -> None
unreal.PlayerController.get_deprecated_input_pitch_scale() -> float
unreal.PlayerController.get_deprecated_input_roll_scale() -> float
unreal.PlayerController.get_deprecated_input_yaw_scale() -> float
unreal.PlayerController.get_focal_location() -> Vector
unreal.PlayerController.get_hit_result_under_cursor(trace_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY, trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hit_result_under_cursor_by_channel(trace_channel: TraceTypeQuery, trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hit_result_under_cursor_for_objects(object_types: Array[ObjectTypeQuery], trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hit_result_under_finger(finger_index: TouchIndex, trace_channel: CollisionChannel = CollisionChannel.ECC_VISIBILITY, trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hit_result_under_finger_by_channel(finger_index: TouchIndex, trace_channel: TraceTypeQuery, trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hit_result_under_finger_for_objects(finger_index: TouchIndex, object_types: Array[ObjectTypeQuery], trace_complex: bool = True) -> Optional[HitResult]
unreal.PlayerController.get_hud() -> HUD
unreal.PlayerController.get_input_analog_key_state(key: Key) -> float
unreal.PlayerController.get_input_analog_stick_state(which_stick: ControllerAnalogStick) -> Tuple[float, float]
unreal.PlayerController.get_input_key_time_down(key: Key) -> float
unreal.PlayerController.get_input_motion_state() -> Tuple[Vector, Vector, Vector, Vector]
unreal.PlayerController.get_input_mouse_delta() -> Tuple[float, float]
unreal.PlayerController.get_input_touch_state(finger_index: TouchIndex) -> Tuple[float, float, bool]
unreal.PlayerController.get_input_vector_key_state(key: Key) -> Vector
unreal.PlayerController.get_mouse_position() -> Optional[Tuple[float, float]]
unreal.PlayerController.get_override_player_input_class() -> Class
unreal.PlayerController.get_platform_user_id() -> PlatformUserId
unreal.PlayerController.get_spectator_pawn() -> SpectatorPawn
unreal.PlayerController.get_streaming_source_location_and_rotation() -> Tuple[Vector, Rotator]
unreal.PlayerController.get_streaming_source_priority() -> StreamingSourcePriority
unreal.PlayerController.get_streaming_source_shapes() -> Array[StreamingSourceShape]
unreal.PlayerController.get_viewport_size() -> Tuple[int, int]
unreal.PlayerController.hit_result_trace_distance(value: float) -> None
unreal.PlayerController.input_pitch_scale(value: float) -> None
unreal.PlayerController.input_roll_scale(value: float) -> None
unreal.PlayerController.input_yaw_scale(value: float) -> None
unreal.PlayerController.is_input_key_down(key: Key) -> bool
unreal.PlayerController.is_streaming_source_enabled() -> bool
unreal.PlayerController.k2_client_play_force_feedback(force_feedback_effect: ForceFeedbackEffect, tag: Name, looping: bool, ignore_time_dilation: bool, play_while_paused: bool) -> None
unreal.PlayerController.look_right_scale(value: float) -> None
unreal.PlayerController.look_up_scale(value: float) -> None
unreal.PlayerController.play_dynamic_force_feedback(intensity: float, duration: float = -1.000000, affects_left_large: bool = True, affects_left_small: bool = True, affects_right_large: bool = True, affects_right_small: bool = True, action: DynamicForceFeedbackAction = ..., latent_info: LatentActionInfo = ...) -> None
unreal.PlayerController.play_haptic_effect(haptic_effect: HapticFeedbackEffect_Base, hand: ControllerHand, scale: float = 1.000000, loop: bool = False) -> None
unreal.PlayerController.player_camera() -> PlayerCameraManager
unreal.PlayerController.player_camera_class() -> Class
unreal.PlayerController.player_camera_manager() -> PlayerCameraManager
unreal.PlayerController.player_camera_manager_class() -> Class
unreal.PlayerController.player_is_waiting() -> bool
unreal.PlayerController.project_world_location_to_screen(world_location: Vector, player_viewport_relative: bool = False) -> Optional[Vector2D]
unreal.PlayerController.reset_controller_dead_zones() -> None
unreal.PlayerController.reset_controller_light_color() -> None
unreal.PlayerController.set_audio_listener_attenuation_override(attach_to_component: SceneComponent, attenuation_location_o_verride: Vector) -> None
unreal.PlayerController.set_audio_listener_override(attach_to_component: SceneComponent, location: Vector, rotation: Rotator) -> None
unreal.PlayerController.set_cinematic_mode(cinematic_mode: bool, hide_player: bool = True, affects_hud: bool = True, affects_movement: bool = ..., affects_turning: bool = ...) -> None
unreal.PlayerController.set_controller_dead_zones(left_dead_zone: float, right_dead_zone: float) -> None
unreal.PlayerController.set_controller_light_color(color: Color) -> None
unreal.PlayerController.set_deprecated_input_pitch_scale(new_value: float) -> None
unreal.PlayerController.set_deprecated_input_roll_scale(new_value: float) -> None
unreal.PlayerController.set_deprecated_input_yaw_scale(new_value: float) -> None
unreal.PlayerController.set_disable_haptics(new_disabled: bool) -> None
unreal.PlayerController.set_haptics_by_value(frequency: float, amplitude: float, hand: ControllerHand) -> None
unreal.PlayerController.set_mouse_cursor_widget(cursor: MouseCursor, cursor_widget: UserWidget) -> None
unreal.PlayerController.set_mouse_location(x: int, y: int) -> None
unreal.PlayerController.set_view_target_with_blend(new_view_target: Actor, blend_time: float = 0.000000, blend_func: ViewTargetBlendFunction = ViewTargetBlendFunction.VT_BLEND_LINEAR, blend_exp: float = 0.000000, lock_outgoing: bool = False) -> None
unreal.PlayerController.set_virtual_joystick_visibility(visible: bool) -> None
unreal.PlayerController.should_perform_full_tick_when_paused(value: bool) -> None
unreal.PlayerController.show_mouse_cursor(value: bool) -> None
unreal.PlayerController.smooth_target_view_rotation_speed(value: float) -> None
unreal.PlayerController.stop_haptic_effect(hand: ControllerHand) -> None
unreal.PlayerController.streaming_source_debug_color(value: Color) -> None
unreal.PlayerController.streaming_source_priority(value: StreamingSourcePriority) -> None
unreal.PlayerController.streaming_source_shapes(value: Array[StreamingSourceShape]) -> None
unreal.PlayerController.streaming_source_should_activate() -> bool
unreal.PlayerController.streaming_source_should_block_on_slow_streaming() -> bool
unreal.PlayerController.was_input_key_just_pressed(key: Key) -> bool
unreal.PlayerController.was_input_key_just_released(key: Key) -> bool
```

## `unreal.PlayerInput(Object)`

```python
unreal.PlayerInput.get_outer_a_player_controller() -> PlayerController
```

## `unreal.PlayerMappableInputConfig(PrimaryDataAsset)`

```python
unreal.PlayerMappableInputConfig.config_display_name() -> Text
unreal.PlayerMappableInputConfig.config_name() -> Name
unreal.PlayerMappableInputConfig.contexts() -> Map[InputMappingContext, int]
unreal.PlayerMappableInputConfig.get_config_name() -> Name
unreal.PlayerMappableInputConfig.get_display_name() -> Text
unreal.PlayerMappableInputConfig.get_keys_bound_to_action(action: InputAction) -> Array[EnhancedActionKeyMapping]
unreal.PlayerMappableInputConfig.get_mapping_by_name(mapping_name: Name) -> EnhancedActionKeyMapping
unreal.PlayerMappableInputConfig.get_mapping_contexts() -> Map[InputMappingContext, int]
unreal.PlayerMappableInputConfig.get_metadata() -> Object
unreal.PlayerMappableInputConfig.get_player_mappable_keys() -> Array[EnhancedActionKeyMapping]
unreal.PlayerMappableInputConfig.is_deprecated() -> bool
unreal.PlayerMappableInputConfig.metadata() -> Object
unreal.PlayerMappableInputConfig.reset_to_default() -> None
```

## `unreal.PlayerMappableKeyOptions(StructBase)`

```python
unreal.PlayerMappableKeyOptions.__init__(metadata: Object = None, name: Name = "None", display_name: Text = "", display_category: Text = "") -> None
unreal.PlayerMappableKeyOptions.display_category(value: Text) -> None
unreal.PlayerMappableKeyOptions.display_name(value: Text) -> None
unreal.PlayerMappableKeyOptions.metadata(value: Object) -> None
unreal.PlayerMappableKeyOptions.name(value: Name) -> None
```

## `unreal.PlayerMappableKeyProfileCreationArgs(StructBase)`

```python
unreal.PlayerMappableKeyProfileCreationArgs.__init__(profile_type: Class = None, profile_identifier: GameplayTag = ["None"], user_id: PlatformUserId = [], display_name: Text = "", set_as_current_profile: bool = False) -> None
unreal.PlayerMappableKeyProfileCreationArgs.display_name(value: Text) -> None
unreal.PlayerMappableKeyProfileCreationArgs.profile_identifier(value: GameplayTag) -> None
unreal.PlayerMappableKeyProfileCreationArgs.profile_type(value: Class) -> None
unreal.PlayerMappableKeyProfileCreationArgs.set_as_current_profile(value: bool) -> None
unreal.PlayerMappableKeyProfileCreationArgs.user_id(value: PlatformUserId) -> None
```

## `unreal.PlayerMappableKeyQueryOptions(StructBase)`

```python
unreal.PlayerMappableKeyQueryOptions.__init__(mapping_name: Name = "None", key_to_match: Key = [], slot_to_match: PlayerMappableKeySlot = PlayerMappableKeySlot.FIRST, match_basic_key_types: bool = False, match_key_axis_type: bool = False, required_device_type: HardwareDevicePrimaryType = HardwareDevicePrimaryType.UNSPECIFIED, required_device_flags: int = 0) -> None
unreal.PlayerMappableKeyQueryOptions.key_to_match(value: Key) -> None
unreal.PlayerMappableKeyQueryOptions.mapping_name(value: Name) -> None
unreal.PlayerMappableKeyQueryOptions.match_basic_key_types(value: bool) -> None
unreal.PlayerMappableKeyQueryOptions.match_key_axis_type(value: bool) -> None
unreal.PlayerMappableKeyQueryOptions.required_device_flags(value: int) -> None
unreal.PlayerMappableKeyQueryOptions.required_device_type(value: HardwareDevicePrimaryType) -> None
unreal.PlayerMappableKeyQueryOptions.slot_to_match(value: PlayerMappableKeySlot) -> None
```

## `unreal.PlayerMappableKeySettings(Object)`

```python
unreal.PlayerMappableKeySettings.display_category() -> Text
unreal.PlayerMappableKeySettings.display_name() -> Text
unreal.PlayerMappableKeySettings.metadata() -> Object
unreal.PlayerMappableKeySettings.name() -> Name
unreal.PlayerMappableKeySettings.supported_key_profiles() -> GameplayTagContainer
```

## `unreal.PlayerMappableKeySlotData(StructBase)`

```python
unreal.PlayerMappableKeySlotData.__init__(slot_number: int = 0) -> None
unreal.PlayerMappableKeySlotData.slot_number(value: int) -> None
```

## `unreal.PlayerStart(NavigationObjectBase)`

```python
unreal.PlayerStart.player_start_tag(value: Name) -> None
```

## `unreal.PlayerState(Info)`

```python
unreal.PlayerState.bp_get_unique_id() -> UniqueNetIdRepl
unreal.PlayerState.compressed_ping() -> int
unreal.PlayerState.get_pawn() -> Pawn
unreal.PlayerState.get_ping_in_milliseconds() -> float
unreal.PlayerState.get_player_controller() -> PlayerController
unreal.PlayerState.get_player_name() -> str
unreal.PlayerState.is_a_bot() -> bool
unreal.PlayerState.is_only_a_spectator() -> bool
unreal.PlayerState.is_spectator() -> bool
unreal.PlayerState.on_pawn_set(value: OnPlayerStatePawnSet) -> None
unreal.PlayerState.pawn_private() -> Pawn
unreal.PlayerState.ping() -> int
unreal.PlayerState.player_id() -> int
unreal.PlayerState.receive_copy_properties(new_player_state: PlayerState) -> None
unreal.PlayerState.receive_override_with(old_player_state: PlayerState) -> None
unreal.PlayerState.score() -> float
```

## `unreal.PossessPawnSettings(StructBase)`

```python
unreal.PossessPawnSettings.__init__(auto_follow: bool = False, return_to_default_pawn_when_destroyed: bool = False) -> None
unreal.PossessPawnSettings.auto_follow(value: bool) -> None
unreal.PossessPawnSettings.return_to_default_pawn_when_destroyed(value: bool) -> None
```

## `unreal.RandomPlayerSequenceEntry(StructBase)`

```python
unreal.RandomPlayerSequenceEntry.__init__(sequence: AnimSequenceBase = None, chance_to_play: float = 0.000000, min_loop_count: int = 0, max_loop_count: int = 0, min_play_rate: float = 0.000000, max_play_rate: float = 0.000000) -> None
unreal.RandomPlayerSequenceEntry.chance_to_play(value: float) -> None
unreal.RandomPlayerSequenceEntry.max_loop_count(value: int) -> None
unreal.RandomPlayerSequenceEntry.max_play_rate(value: float) -> None
unreal.RandomPlayerSequenceEntry.min_loop_count(value: int) -> None
unreal.RandomPlayerSequenceEntry.min_play_rate(value: float) -> None
unreal.RandomPlayerSequenceEntry.sequence(value: AnimSequenceBase) -> None
```

## `unreal.RigHierarchyController(Object)`

```python
unreal.RigHierarchyController.add_animation_channel(name: Name, parent_control: RigElementKey, settings: RigControlSettings, setup_undo: bool = True, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_available_space(control: RigElementKey, space: RigElementKey, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.add_bone(name: Name, parent: RigElementKey, transform: Transform, transform_in_global: bool = True, bone_type: RigBoneType = RigBoneType.USER, setup_undo: bool = False, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_channel_host(channel: RigElementKey, host: RigElementKey, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.add_connector(name: Name, settings: RigConnectorSettings = ["", ConnectorType.PRIMARY, False, []], setup_undo: bool = False, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_control(name: Name, parent: RigElementKey, settings: RigControlSettings, value: RigControlValue, setup_undo: bool = True, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_curve(name: Name, value: float = 0.000000, setup_undo: bool = True, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_null(name: Name, parent: RigElementKey, transform: Transform, transform_in_global: bool = True, setup_undo: bool = False, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_parent(child: RigElementKey, parent: RigElementKey, weight: float = 0.000000, maintain_global_transform: bool = True, setup_undo: bool = False) -> bool
unreal.RigHierarchyController.add_physics_element(name: Name, parent: RigElementKey, solver: RigPhysicsSolverID, settings: RigPhysicsSettings, local_transform: Transform, setup_undo: bool = False, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.add_socket(name: Name, parent: RigElementKey, transform: Transform, transform_in_global: bool = True, color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], description: str = "", setup_undo: bool = False, print_python_command: bool = False) -> RigElementKey
unreal.RigHierarchyController.clear_selection() -> bool
unreal.RigHierarchyController.deselect_element(key: RigElementKey) -> bool
unreal.RigHierarchyController.duplicate_elements(keys: Array[RigElementKey], select_new_elements: bool = True, setup_undo: bool = False, print_python_commands: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.export_selection_to_text() -> str
unreal.RigHierarchyController.export_to_text(keys: Array[RigElementKey]) -> str
unreal.RigHierarchyController.generate_python_commands() -> Array[str]
unreal.RigHierarchyController.get_control_settings(key: RigElementKey) -> RigControlSettings
unreal.RigHierarchyController.get_hierarchy() -> RigHierarchy
unreal.RigHierarchyController.import_bones(skeleton: Skeleton, name_space: Name = "None", replace_existing_bones: bool = True, remove_obsolete_bones: bool = True, select_bones: bool = False, setup_undo: bool = False, print_python_command: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.import_bones_from_asset(asset_path: str, name_space: Name = "None", replace_existing_bones: bool = True, remove_obsolete_bones: bool = True, select_bones: bool = False, setup_undo: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.import_curves(skeleton: Skeleton, name_space: Name = "None", select_curves: bool = False, setup_undo: bool = False, print_python_command: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.import_curves_from_asset(asset_path: str, name_space: Name = "None", select_curves: bool = False, setup_undo: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.import_curves_from_skeletal_mesh(skeletal_mesh: SkeletalMesh, name_space: Name = "None", select_curves: bool = False, setup_undo: bool = False, print_python_command: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.import_from_text(content: str, replace_existing_elements: bool = False, select_new_elements: bool = True, setup_undo: bool = False, print_python_commands: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.mirror_elements(keys: Array[RigElementKey], settings: RigVMMirrorSettings, select_new_elements: bool = True, setup_undo: bool = False, print_python_commands: bool = False) -> Array[RigElementKey]
unreal.RigHierarchyController.remove_all_parents(child: RigElementKey, maintain_global_transform: bool = True, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.remove_available_space(control: RigElementKey, space: RigElementKey, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.remove_channel_host(channel: RigElementKey, host: RigElementKey, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.remove_element(element: RigElementKey, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.remove_parent(child: RigElementKey, parent: RigElementKey, maintain_global_transform: bool = True, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.rename_element(element: RigElementKey, name: Name, setup_undo: bool = False, print_python_command: bool = False, clear_selection: bool = True) -> RigElementKey
unreal.RigHierarchyController.reorder_element(element: RigElementKey, index: int, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.select_element(key: RigElementKey, select: bool = True, clear_selection: bool = False) -> bool
unreal.RigHierarchyController.set_available_space_index(control: RigElementKey, space: RigElementKey, index: int, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.set_control_settings(key: RigElementKey, settings: RigControlSettings, setup_undo: bool = False) -> bool
unreal.RigHierarchyController.set_display_name(control: RigElementKey, display_name: Name, rename_element: bool = False, setup_undo: bool = False, print_python_command: bool = False) -> Name
unreal.RigHierarchyController.set_hierarchy(hierarchy: RigHierarchy) -> None
unreal.RigHierarchyController.set_parent(child: RigElementKey, parent: RigElementKey, maintain_global_transform: bool = True, setup_undo: bool = False, print_python_command: bool = False) -> bool
unreal.RigHierarchyController.set_selection(keys: Array[RigElementKey], print_python_command: bool = False) -> bool
```

## `unreal.RigVMController(Object)`

```python
unreal.RigVMController.add_aggregate_pin(node_name: str, pin_name: str, default_value: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> str
unreal.RigVMController.add_array_node(op_code: RigVMOpCode, cpp_type: str, cpp_type_object: Object, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False, is_patching: bool = False) -> RigVMNode
unreal.RigVMController.add_array_node_from_object_path(op_code: RigVMOpCode, cpp_type: str, cpp_type_object_path: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False, is_patching: bool = False) -> RigVMNode
unreal.RigVMController.add_array_pin(array_pin_path: str, default_value: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> str
unreal.RigVMController.add_branch_node(position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMNode
unreal.RigVMController.add_comment_node(comment_text: str, position: Vector2D = [0.000000, 0.000000], size: Vector2D = [400.000000, 300.000000], color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMCommentNode
unreal.RigVMController.add_default_tag_to_function_variant(function_name: Name, tag_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.add_empty_pin_category(node_name: Name, category: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.add_enum_node(cpp_type_object_path: Name, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMEnumNode
unreal.RigVMController.add_exposed_pin(pin_name: Name, direction: RigVMPinDirection, cpp_type: str, cpp_type_object_path: Name, default_value: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> Name
unreal.RigVMController.add_external_function_reference_node(host_path: str, function_name: Name, node_position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMFunctionReferenceNode
unreal.RigVMController.add_free_reroute_node(cpp_type: str, cpp_type_object_path: Name, is_constant: bool, custom_widget_name: Name, default_value: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True) -> RigVMRerouteNode
unreal.RigVMController.add_function_reference_node(function_definition: RigVMLibraryNode, node_position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMFunctionReferenceNode
unreal.RigVMController.add_function_reference_node_from_description(function_definition: RigVMGraphFunctionHeader, node_position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMFunctionReferenceNode
unreal.RigVMController.add_function_to_library(function_name: Name, mutable: bool, node_position: Vector2D = [0.000000, 0.000000], setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMLibraryNode
unreal.RigVMController.add_if_node(cpp_type: str, cpp_type_object_path: Name, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMNode
unreal.RigVMController.add_if_node_from_struct(script_struct: ScriptStruct, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True) -> RigVMNode
unreal.RigVMController.add_injected_node(pin_path: str, as_input: bool, script_struct: ScriptStruct, method_name: Name, input_pin_name: Name, output_pin_name: Name, node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMInjectionInfo
unreal.RigVMController.add_injected_node_from_struct_path(pin_path: str, as_input: bool, script_struct_path: str, method_name: Name, input_pin_name: Name, output_pin_name: Name, node_name: str = "", setup_undo_redo: bool = True) -> RigVMInjectionInfo
unreal.RigVMController.add_invoke_entry_node(entry_name: Name, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMInvokeEntryNode
unreal.RigVMController.add_link(output_pin_path: str, input_pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False, user_direction: RigVMPinDirection = RigVMPinDirection.OUTPUT, create_cast_node: bool = False) -> bool
unreal.RigVMController.add_local_variable(variable_name: Name, cpp_type: str, cpp_type_object: Object, default_value: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMGraphVariableDescription
unreal.RigVMController.add_local_variable_from_object_path(variable_name: Name, cpp_type: str, cpp_type_object_path: str, default_value: str, setup_undo_redo: bool = True) -> RigVMGraphVariableDescription
unreal.RigVMController.add_parameter_node(parameter_name: Name, cpp_type: str, cpp_type_object: Object, is_input: bool, default_value: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMParameterNode
unreal.RigVMController.add_parameter_node_from_object_path(parameter_name: Name, cpp_type: str, cpp_type_object_path: str, is_input: bool, default_value: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMParameterNode
unreal.RigVMController.add_reroute_node_on_link(link: RigVMLink, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMRerouteNode
unreal.RigVMController.add_reroute_node_on_link_path(link_pin_path_representation: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMRerouteNode
unreal.RigVMController.add_reroute_node_on_pin(pin_path: str, as_input: bool, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMRerouteNode
unreal.RigVMController.add_select_node(cpp_type: str, cpp_type_object_path: Name, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMNode
unreal.RigVMController.add_select_node_from_struct(script_struct: ScriptStruct, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True) -> RigVMNode
unreal.RigVMController.add_tag_to_function_variant(function_name: Name, tag: RigVMTag, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.add_template_node(notation: Name, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMTemplateNode
unreal.RigVMController.add_trait(node_name: Name, trait_type_object_path: Name, trait_name: Name = "None", default_value: str = "", pin_index: int = -1, setup_undo_redo: bool = True, print_python_command: bool = False) -> Name
unreal.RigVMController.add_unit_node(script_struct: ScriptStruct, method_name: Name = "Execute", position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMUnitNode
unreal.RigVMController.add_unit_node_from_struct_path(script_struct_path: str, method_name: Name = "Execute", position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMUnitNode
unreal.RigVMController.add_unit_node_with_defaults(script_struct: ScriptStruct, defaults: str, method_name: Name = "Execute", position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMUnitNode
unreal.RigVMController.add_variable_node(variable_name: Name, cpp_type: str, cpp_type_object: Object, is_getter: bool, default_value: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMVariableNode
unreal.RigVMController.add_variable_node_from_object_path(variable_name: Name, cpp_type: str, cpp_type_object_path: str, is_getter: bool, default_value: str, position: Vector2D = [0.000000, 0.000000], node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMVariableNode
unreal.RigVMController.bind_pin_to_variable(pin_path: str, new_bound_variable_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.break_all_links(pin_path: str, as_input: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.break_link(output_pin_path: str, input_pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.can_import_nodes_from_text(text: str) -> bool
unreal.RigVMController.cancel_undo_bracket() -> bool
unreal.RigVMController.change_exposed_pin_type(pin_name: Name, cpp_type: str, cpp_type_object_path: Name, setup_undo_redo: bool, setup_orphan_pins: bool = True, print_python_command: bool = False) -> Optional[bool]
unreal.RigVMController.clear_array_pin(array_pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.clear_node_layout(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.clear_node_selection(setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.clear_pin_category(pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.close_undo_bracket() -> bool
unreal.RigVMController.collapse_nodes(node_names: Array[Name], collapse_node_name: str = "", setup_undo_redo: bool = True, print_python_command: bool = False, is_aggregate: bool = False) -> RigVMCollapseNode
unreal.RigVMController.create_function_variant(function_name: Name, variant_name: Name = "None", setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMLibraryNode
unreal.RigVMController.duplicate_array_pin(array_element_pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> str
unreal.RigVMController.eject_node_from_pin(pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMNode
unreal.RigVMController.enable_reporting(enabled: bool = True) -> None
unreal.RigVMController.expand_library_node(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> Array[RigVMNode]
unreal.RigVMController.export_nodes_to_text(node_names: Array[Name], include_exterior_links: bool = False) -> str
unreal.RigVMController.export_selected_nodes_to_text(include_exterior_links: bool = False) -> str
unreal.RigVMController.find_graph_function_header(function_identifier: RigVMGraphFunctionIdentifier) -> RigVMGraphFunctionHeader
unreal.RigVMController.find_graph_function_header_by_name(host_path: str, function_name: Name) -> RigVMGraphFunctionHeader
unreal.RigVMController.find_graph_function_identifier(host_path: str, function_name: Name) -> RigVMGraphFunctionIdentifier
unreal.RigVMController.find_variants_of_function(function_name: Name) -> Array[RigVMVariantRef]
unreal.RigVMController.generate_python_commands() -> Array[str]
unreal.RigVMController.get_action_stack() -> RigVMActionStack
unreal.RigVMController.get_controller_for_graph(graph: RigVMGraph) -> RigVMController
unreal.RigVMController.get_graph() -> RigVMGraph
unreal.RigVMController.get_pin_default_value(pin_path: str) -> str
unreal.RigVMController.get_registered_templates() -> Array[str]
unreal.RigVMController.get_registered_unit_structs() -> Array[ScriptStruct]
unreal.RigVMController.get_schema() -> RigVMSchema
unreal.RigVMController.get_template_for_unit_struct(function: ScriptStruct, method_name: str = "Execute") -> str
unreal.RigVMController.get_top_level_graph() -> RigVMGraph
unreal.RigVMController.get_unit_structs_for_template(notation: Name) -> Array[ScriptStruct]
unreal.RigVMController.import_nodes_from_text(text: str, setup_undo_redo: bool = True, print_python_commands: bool = False) -> Array[Name]
unreal.RigVMController.insert_array_pin(array_pin_path: str, index: int = -1, default_value: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> str
unreal.RigVMController.is_function_public(function_name: Name) -> bool
unreal.RigVMController.is_reporting_enabled() -> bool
unreal.RigVMController.is_transacting() -> bool
unreal.RigVMController.join_function_variant(function_name: Name, guid: Guid, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.localize_function(function_definition: RigVMGraphFunctionIdentifier, localize_dependent_private_functions: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMLibraryNode
unreal.RigVMController.localize_function_from_path(host_path: str, function_name: Name, localize_dependent_private_functions: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> RigVMLibraryNode
unreal.RigVMController.localize_functions(function_definitions: Array[RigVMGraphFunctionIdentifier], localize_dependent_private_functions: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> Map[RigVMGraphFunctionIdentifier, RigVMLibraryNode]
unreal.RigVMController.make_bindings_from_variable_node(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.make_options_for_workflow(subject: Object, workflow: RigVMUserWorkflow) -> RigVMUserWorkflowOptions
unreal.RigVMController.make_variable_node_from_binding(pin_path: str, node_position: Vector2D = [0.000000, 0.000000], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.mark_function_as_public(function_name: Name, is_public: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.modified_event() -> RigVMGraphModifiedDynamicEvent
unreal.RigVMController.open_undo_bracket(title: str) -> bool
unreal.RigVMController.perform_user_workflow(workflow: RigVMUserWorkflow, options: RigVMUserWorkflowOptions, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.pop_graph(setup_undo_redo: bool = True) -> RigVMGraph
unreal.RigVMController.promote_collapse_node_to_function_reference_node(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False, existing_function_definition_path: str = "") -> Name
unreal.RigVMController.promote_function_reference_node_to_collapse_node(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False, remove_function_definition: bool = False) -> Name
unreal.RigVMController.promote_pin_to_variable(pin_path: str, create_variable_node: bool, node_position: Vector2D = [0.000000, 0.000000], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.push_graph(graph: RigVMGraph, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.redo() -> bool
unreal.RigVMController.refresh_variable_node(node_name: Name, variable_name: Name, cpp_type: str, cpp_type_object: Object, setup_undo_redo: bool, setup_orphan_pins: bool = True) -> None
unreal.RigVMController.remove_aggregate_pin(pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_array_pin(array_element_pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_exposed_pin(pin_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_function_from_library(function_name: Name, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.remove_injected_node(pin_path: str, as_input: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_local_variable(variable_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_node(node: RigVMNode, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_node_by_name(node_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_nodes(nodes: Array[RigVMNode], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_nodes_by_name(node_names: Array[Name], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_pin_category(node_name: Name, pin_category: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_tag_from_function_variant(function_name: Name, tag_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.remove_trait(node_name: Name, trait_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.rename_exposed_pin(old_pin_name: Name, new_pin_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.rename_function(old_function_name: Name, new_function_name: Name, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.rename_local_variable(variable_name: Name, new_variable_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.rename_node(node: RigVMNode, new_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.rename_parameter(old_name: Name, new_name: Name, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.rename_pin_category(node_name: Name, old_pin_category: str, new_pin_category: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.rename_variable(old_name: Name, new_name: Name, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.replace_parameter_node_with_variable(node_name: Name, variable_name: Name, cpp_type: str, cpp_type_object: Object, setup_undo_redo: bool) -> RigVMVariableNode
unreal.RigVMController.reset_pin_default_value(pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.resolve_wild_card_pin(pin_path: str, cpp_type: str, cpp_type_object_path: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.select_node(node: RigVMNode, select: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.select_node_by_name(node_name: Name, select: bool = True, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.set_action_stack(action_stack: RigVMActionStack) -> None
unreal.RigVMController.set_array_pin_size(array_pin_path: str, size: int, default_value: str = "", setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_comment_text(node: RigVMNode, comment_text: str, comment_font_size: int, comment_bubble_visible: bool, comment_color_bubble: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_comment_text_by_name(node_name: Name, comment_text: str, comment_font_size: int, comment_bubble_visible: bool, comment_color_bubble: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_exposed_pin_index(pin_name: Name, new_index: int, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_graph(graph: RigVMGraph) -> None
unreal.RigVMController.set_is_running_unit_test(is_running: bool) -> None
unreal.RigVMController.set_local_variable_default_value(variable_name: Name, default_value: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_local_variable_type(variable_name: Name, cpp_type: str, cpp_type_object: Object, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_local_variable_type_from_object_path(variable_name: Name, cpp_type: str, cpp_type_object_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_category(node: RigVMCollapseNode, category: str, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_category_by_name(node_name: Name, category: str, setup_undo_redo: bool = True, merge_undo_action: bool = False) -> bool
unreal.RigVMController.set_node_color(node: RigVMNode, color: LinearColor, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_color_by_name(node_name: Name, color: LinearColor, setup_undo_redo: bool = True, merge_undo_action: bool = False) -> bool
unreal.RigVMController.set_node_description(node: RigVMCollapseNode, description: str, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_description_by_name(node_name: Name, description: str, setup_undo_redo: bool = True, merge_undo_action: bool = False) -> bool
unreal.RigVMController.set_node_keywords(node: RigVMCollapseNode, keywords: str, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_keywords_by_name(node_name: Name, keywords: str, setup_undo_redo: bool = True, merge_undo_action: bool = False) -> bool
unreal.RigVMController.set_node_layout(node_name: Name, layout: RigVMNodeLayout, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_position(node: RigVMNode, position: Vector2D, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_position_by_name(node_name: Name, position: Vector2D, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_selection(node_names: Array[Name], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_size(node: RigVMNode, size: Vector2D, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_node_size_by_name(node_name: Name, size: Vector2D, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_category(pin_path: str, category: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_category_expansion(node_name: Name, pin_category: str, is_expanded: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_category_index(node_name: Name, pin_category: str, new_index: int, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_default_value(pin_path: str, default_value: str, resize_arrays: bool = True, setup_undo_redo: bool = True, merge_undo_action: bool = False, print_python_command: bool = False, set_value_on_linked_pins: bool = True) -> bool
unreal.RigVMController.set_pin_display_name(pin_path: str, display_name: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_expansion(pin_path: str, is_expanded: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_index_in_category(pin_path: str, index_in_category: int, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.set_pin_is_watched(pin_path: str, is_watched: bool, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.set_remapped_variable(function_ref_node: RigVMFunctionReferenceNode, inner_variable_name: Name, outer_variable_name: Name, setup_undo_redo: bool = True) -> bool
unreal.RigVMController.set_schema(schema: RigVMSchema) -> None
unreal.RigVMController.set_schema_class(schema_class: Class) -> None
unreal.RigVMController.set_unit_node_defaults(node: RigVMUnitNode, defaults: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.split_function_variant(function_name: Name, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.swap_all_function_references(old_function_identifier: RigVMGraphFunctionIdentifier, new_function_identifier: RigVMGraphFunctionIdentifier, setup_orphan_pins: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.swap_function_reference(function_reference_node: RigVMFunctionReferenceNode, new_function_identifier: RigVMGraphFunctionIdentifier, setup_orphan_pins: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.swap_function_reference_by_name(function_reference_node_name: Name, new_function_identifier: RigVMGraphFunctionIdentifier, setup_orphan_pins: bool, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.unbind_pin_from_variable(pin_path: str, setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.undo() -> bool
unreal.RigVMController.unresolve_template_nodes(node_names: Array[Name], setup_undo_redo: bool = True, print_python_command: bool = False) -> bool
unreal.RigVMController.upgrade_nodes(node_names: Array[Name], recursive: bool = True, setup_undo_redo: bool = True, print_python_command: bool = False) -> Array[RigVMNode]
```

## `unreal.RoundPlanetPawn(DefaultPawn)`

```python
unreal.RoundPlanetPawn.altitude() -> float
unreal.RoundPlanetPawn.base_speed_kmh(value: float) -> None
unreal.RoundPlanetPawn.decrease_speed_scalar() -> None
unreal.RoundPlanetPawn.fly_to_location_ecef(ecef_destination: Vector, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.RoundPlanetPawn.fly_to_location_geographic(geographic_destination: GeographicCoordinates, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.RoundPlanetPawn.fly_to_location_latitude_longitude_altitude(latitude: float, longitude: float, altitude: float, yaw_at_destination: float, pitch_at_destination: float, can_interrupt_by_moving: bool) -> None
unreal.RoundPlanetPawn.hat() -> float
unreal.RoundPlanetPawn.increase_speed_scalar() -> None
unreal.RoundPlanetPawn.interrupt_fly_to_location() -> None
unreal.RoundPlanetPawn.orbital_motion(value: bool) -> None
unreal.RoundPlanetPawn.reset_speed_scalar() -> None
unreal.RoundPlanetPawn.speed_scalar(value: float) -> None
unreal.RoundPlanetPawn.speed_scalar_increment(value: float) -> None
```

## `unreal.RuntimeCameraData(StructBase)`

```python
unreal.RuntimeCameraData.__init__(height_to_ground: float = 0.000000, screen_center_ground_location: Vector = [0.000000, 0.000000, 0.000000], screen_center_location: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RuntimeCameraData.height_to_ground(value: float) -> None
unreal.RuntimeCameraData.screen_center_ground_location(value: Vector) -> None
unreal.RuntimeCameraData.screen_center_location(value: Vector) -> None
```

## `unreal.SequenceCameraShakeTestUtil(BlueprintFunctionLibrary)`

```python
unreal.SequenceCameraShakeTestUtil.get_camera_cache_pov(player_controller: PlayerController) -> MinimalViewInfo
unreal.SequenceCameraShakeTestUtil.get_last_frame_camera_cache_pov(player_controller: PlayerController) -> MinimalViewInfo
unreal.SequenceCameraShakeTestUtil.get_post_process_blend_cache(player_controller: PlayerController, pp_index: int) -> Optional[Tuple[PostProcessSettings, float]]
```

## `unreal.SequencePlayerLibrary(BlueprintFunctionLibrary)`

```python
unreal.SequencePlayerLibrary.compute_play_rate_from_duration(sequence_player: SequencePlayerReference, duration: float = 1.000000) -> float
unreal.SequencePlayerLibrary.convert_to_sequence_player(node: AnimNodeReference) -> Tuple[SequencePlayerReference, AnimNodeReferenceConversionResult]
unreal.SequencePlayerLibrary.convert_to_sequence_player_pure(node: AnimNodeReference) -> Tuple[SequencePlayerReference, bool]
unreal.SequencePlayerLibrary.get_accumulated_time(sequence_player: SequencePlayerReference) -> float
unreal.SequencePlayerLibrary.get_loop_animation(sequence_player: SequencePlayerReference) -> bool
unreal.SequencePlayerLibrary.get_play_rate(sequence_player: SequencePlayerReference) -> float
unreal.SequencePlayerLibrary.get_sequence(sequence_player: SequencePlayerReference, sequence_base: AnimSequenceBase) -> Tuple[SequencePlayerReference, AnimSequenceBase]
unreal.SequencePlayerLibrary.get_sequence_pure(sequence_player: SequencePlayerReference) -> AnimSequenceBase
unreal.SequencePlayerLibrary.get_start_position(sequence_player: SequencePlayerReference) -> float
unreal.SequencePlayerLibrary.set_accumulated_time(sequence_player: SequencePlayerReference, time: float) -> SequencePlayerReference
unreal.SequencePlayerLibrary.set_play_rate(sequence_player: SequencePlayerReference, play_rate: float) -> SequencePlayerReference
unreal.SequencePlayerLibrary.set_sequence(sequence_player: SequencePlayerReference, sequence: AnimSequenceBase) -> SequencePlayerReference
unreal.SequencePlayerLibrary.set_sequence_with_inertial_blending(update_context: AnimUpdateContext, sequence_player: SequencePlayerReference, sequence: AnimSequenceBase, blend_time: float = 0.200000) -> SequencePlayerReference
unreal.SequencePlayerLibrary.set_start_position(sequence_player: SequencePlayerReference, start_position: float) -> SequencePlayerReference
```

## `unreal.SequencePlayerReference(AnimNodeReference)`

```python
unreal.SequencePlayerReference.__init__() -> None
```

## `unreal.SolverInput(StructBase)`

```python
unreal.SolverInput.__init__() -> None
```

## `unreal.SwitchCustomInput(StructBase)`

```python
unreal.SwitchCustomInput.__init__() -> None
```

## `unreal.TemplateSequencePlayer(MovieSceneSequencePlayer)`

```python
unreal.TemplateSequencePlayer.create_template_sequence_player(world_context_object: Object, template_sequence: TemplateSequence, settings: MovieSceneSequencePlaybackSettings) -> Tuple[TemplateSequencePlayer, TemplateSequenceActor]
```

## `unreal.TimedDataInputEvaluationData(StructBase)`

```python
unreal.TimedDataInputEvaluationData.__init__(distance_to_newest_sample_seconds: float = 0.000000, distance_to_oldest_sample_seconds: float = 0.000000) -> None
unreal.TimedDataInputEvaluationData.distance_to_newest_sample_seconds(value: float) -> None
unreal.TimedDataInputEvaluationData.distance_to_oldest_sample_seconds(value: float) -> None
```

## `unreal.ToggleCameraSelfRotateParams(EidParams)`

```python
unreal.ToggleCameraSelfRotateParams.__init__(self_rotate: bool = False) -> None
unreal.ToggleCameraSelfRotateParams.self_rotate() -> bool
```

## `unreal.TouchInputComponent(ActorComponent)`

```python
unreal.TouchInputComponent.current_angle() -> float
unreal.TouchInputComponent.current_finger_count() -> ExistFingerCount
unreal.TouchInputComponent.current_length() -> float
unreal.TouchInputComponent.current_pan_location() -> Vector
unreal.TouchInputComponent.fingers() -> Array[TouchIndex]
unreal.TouchInputComponent.get_finger_and_location_by_index(index: int) -> Optional[Tuple[TouchIndex, Vector]]
unreal.TouchInputComponent.get_fingers_length() -> int
unreal.TouchInputComponent.get_length_and_angle() -> Tuple[Vector, float, float]
unreal.TouchInputComponent.get_screen_right_vector() -> Vector
unreal.TouchInputComponent.get_screen_up_vector() -> Vector
unreal.TouchInputComponent.initial_angle() -> float
unreal.TouchInputComponent.initial_length() -> float
unreal.TouchInputComponent.initial_pan_location() -> Vector
unreal.TouchInputComponent.is_finger_location_exists(finger_index: TouchIndex) -> bool
unreal.TouchInputComponent.locations() -> Array[Vector]
unreal.TouchInputComponent.on_event_touch_moved(finger_index: TouchIndex, location: Vector) -> None
unreal.TouchInputComponent.on_event_touch_pressed(finger_index: TouchIndex, location: Vector) -> None
unreal.TouchInputComponent.on_event_touch_released(finger_index: TouchIndex, location: Vector) -> None
unreal.TouchInputComponent.on_one_finger_event(value: OnOneFingerPressed) -> None
unreal.TouchInputComponent.on_two_finger_event(value: OnTwoFingersMove) -> None
```

## `unreal.TouchInputComponent_OnOneFingerPressed(MulticastDelegateBase)`

```python
unreal.TouchInputComponent_OnOneFingerPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.TouchInputComponent_OnTwoFingersMove(MulticastDelegateBase)`

```python
unreal.TouchInputComponent_OnTwoFingersMove.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.TouchInputControl(StructBase)`

```python
unreal.TouchInputControl.__init__() -> None
```

## `unreal.UMGSequencePlayer(Object)`

```python
unreal.UMGSequencePlayer.get_user_tag() -> Name
unreal.UMGSequencePlayer.set_user_tag(user_tag: Name) -> None
```

## `unreal.UserCameraSettings(StructBase)`

```python
unreal.UserCameraSettings.__init__(rotation_yaw_speed_scale: float = 0.000000, rotation_pitch_speed_scale: float = 0.000000, zoom_speed_scale: float = 0.000000, enable_dynamic_speed: bool = False, key_movement_base_speed: float = 0.000000, invert_x: bool = False, invert_y: bool = False, boost_scale: float = 0.000000, decrease_scale: float = 0.000000, show_touch_effect: bool = False, show_rotate_icon: bool = False) -> None
unreal.UserCameraSettings.boost_scale(value: float) -> None
unreal.UserCameraSettings.decrease_scale(value: float) -> None
unreal.UserCameraSettings.enable_dynamic_speed(value: bool) -> None
unreal.UserCameraSettings.invert_x(value: bool) -> None
unreal.UserCameraSettings.invert_y(value: bool) -> None
unreal.UserCameraSettings.key_movement_base_speed(value: float) -> None
unreal.UserCameraSettings.rotation_pitch_speed_scale(value: float) -> None
unreal.UserCameraSettings.rotation_yaw_speed_scale(value: float) -> None
unreal.UserCameraSettings.show_rotate_icon(value: bool) -> None
unreal.UserCameraSettings.show_touch_effect(value: bool) -> None
unreal.UserCameraSettings.zoom_speed_scale(value: float) -> None
```

## `unreal.VFPlayerObject(Object)`

```python
unreal.VFPlayerObject.get_length() -> float
unreal.VFPlayerObject.get_texture() -> Texture2D
unreal.VFPlayerObject.initialize(url: str, on_video_loaded_callback: OnVideoLoadedDelegate) -> bool
unreal.VFPlayerObject.initialize_without_delegate(url: str) -> bool
unreal.VFPlayerObject.pause() -> None
unreal.VFPlayerObject.play() -> None
unreal.VFPlayerObject.scrub(time_sec: float) -> None
unreal.VFPlayerObject.stop() -> None
```

## `unreal.VFPlayerObject_OnVideoLoadedDelegate(DelegateBase)`

```python
unreal.VFPlayerObject_OnVideoLoadedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ViewportActionKeyInput(StructBase)`

```python
unreal.ViewportActionKeyInput.__init__(action_type: Name = "None", event: InputEventType = InputEventType.IE_PRESSED) -> None
unreal.ViewportActionKeyInput.action_type() -> Name
unreal.ViewportActionKeyInput.event() -> InputEventType
```

## `unreal.Visible2DCamera(StructBase)`

```python
unreal.Visible2DCamera.__init__(hide_distance: float = 0.000000, hide_type: str = "", scale_mode: str = "") -> None
unreal.Visible2DCamera.hide_distance(value: float) -> None
unreal.Visible2DCamera.hide_type(value: str) -> None
unreal.Visible2DCamera.scale_mode(value: str) -> None
```

## `unreal.WDPCameraAroundParams(ParamsBase)`

```python
unreal.WDPCameraAroundParams.__init__(direction: str = "", velocity: float = 0.000000) -> None
unreal.WDPCameraAroundParams.direction(value: str) -> None
unreal.WDPCameraAroundParams.velocity(value: float) -> None
```

## `unreal.WDPCameraInfo(StructBase)`

```python
unreal.WDPCameraInfo.__init__() -> None
```

## `unreal.WDPCameraLimitData(StructBase)`

```python
unreal.WDPCameraLimitData.__init__() -> None
```

## `unreal.WDPCameraRoamParams(ParamsBase)`

```python
unreal.WDPCameraRoamParams.__init__(camera_roam_eid: int = 0, state: WdpCameraRoamState = WdpCameraRoamState.PLAY, progress_ratio: float = 0.000000, speed_ratio: float = 0.000000, reverse: bool = False, enable_rotating_on_pause: bool = False, enable_zooming_on_pause: bool = False) -> None
unreal.WDPCameraRoamParams.camera_roam_eid(value: int) -> None
unreal.WDPCameraRoamParams.enable_rotating_on_pause(value: bool) -> None
unreal.WDPCameraRoamParams.enable_zooming_on_pause(value: bool) -> None
unreal.WDPCameraRoamParams.progress_ratio(value: float) -> None
unreal.WDPCameraRoamParams.reverse(value: bool) -> None
unreal.WDPCameraRoamParams.speed_ratio(value: float) -> None
unreal.WDPCameraRoamParams.state(value: WdpCameraRoamState) -> None
```

## `unreal.WDPCameraSpeedData(StructBase)`

```python
unreal.WDPCameraSpeedData.__init__() -> None
```

## `unreal.WDPGetCameraInfoResult(ResultBase)`

```python
unreal.WDPGetCameraInfoResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, location: Vector = [0.000000, 0.000000, 0.000000], rotation: CameraPresetRotator = [0.000000, 0.000000], location_limit: Array[Vector2D] = [], pitch_limit: Vector2D = [0.000000, 0.000000], yaw_limit: Vector2D = [0.000000, 0.000000], view_distance_limit: Vector2D = [0.000000, 0.000000], control_mode: str = "", field_of_view: float = 0.000000) -> None
unreal.WDPGetCameraInfoResult.control_mode(value: str) -> None
unreal.WDPGetCameraInfoResult.field_of_view(value: float) -> None
unreal.WDPGetCameraInfoResult.location(value: Vector) -> None
unreal.WDPGetCameraInfoResult.location_limit(value: Array[Vector2D]) -> None
unreal.WDPGetCameraInfoResult.pitch_limit(value: Vector2D) -> None
unreal.WDPGetCameraInfoResult.rotation(value: CameraPresetRotator) -> None
unreal.WDPGetCameraInfoResult.view_distance_limit(value: Vector2D) -> None
unreal.WDPGetCameraInfoResult.yaw_limit(value: Vector2D) -> None
```

## `unreal.WDPGetCameraLimitResult(ResultBase)`

```python
unreal.WDPGetCameraLimitResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, location_limit: Array[Vector2D] = [], pitch_limit: Vector2D = [0.000000, 0.000000], yaw_limit: Vector2D = [0.000000, 0.000000], view_distance_limit: Vector2D = [0.000000, 0.000000]) -> None
unreal.WDPGetCameraLimitResult.location_limit(value: Array[Vector2D]) -> None
unreal.WDPGetCameraLimitResult.pitch_limit(value: Vector2D) -> None
unreal.WDPGetCameraLimitResult.view_distance_limit(value: Vector2D) -> None
unreal.WDPGetCameraLimitResult.yaw_limit(value: Vector2D) -> None
```

## `unreal.WDPGetCameraSpeedResult(ResultBase)`

```python
unreal.WDPGetCameraSpeedResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, rotation_yaw_speed_scale: float = 0.000000, rotation_pitch_speed_scale: float = 0.000000, zoom_speed_scale: float = 0.000000, key_movement_base_speed: float = 0.000000, enable_dynamic_speed: bool = False) -> None
unreal.WDPGetCameraSpeedResult.enable_dynamic_speed(value: bool) -> None
unreal.WDPGetCameraSpeedResult.key_movement_base_speed(value: float) -> None
unreal.WDPGetCameraSpeedResult.rotation_pitch_speed_scale(value: float) -> None
unreal.WDPGetCameraSpeedResult.rotation_yaw_speed_scale(value: float) -> None
unreal.WDPGetCameraSpeedResult.zoom_speed_scale(value: float) -> None
```

## `unreal.WDPResetCameraLimitParams(ParamsBase)`

```python
unreal.WDPResetCameraLimitParams.__init__(state: WdpResetCameraLimitState = WdpResetCameraLimitState.DEFAULT) -> None
unreal.WDPResetCameraLimitParams.state(value: WdpResetCameraLimitState) -> None
```

## `unreal.WDPSetCameraLimitParams(ParamsBase)`

```python
unreal.WDPSetCameraLimitParams.__init__(location_limit: Array[Vector2D] = [], pitch_limit: Vector2D = [0.000000, 0.000000], yaw_limit: Vector2D = [0.000000, 0.000000], view_distance_limit: Vector2D = [0.000000, 0.000000]) -> None
unreal.WDPSetCameraLimitParams.location_limit(value: Array[Vector2D]) -> None
unreal.WDPSetCameraLimitParams.pitch_limit(value: Vector2D) -> None
unreal.WDPSetCameraLimitParams.view_distance_limit(value: Vector2D) -> None
unreal.WDPSetCameraLimitParams.yaw_limit(value: Vector2D) -> None
```

## `unreal.WDPSetCameraLockLimitParams(ParamsBase)`

```python
unreal.WDPSetCameraLockLimitParams.__init__(location_limit: float = 0.000000, pitch_limit: float = 0.000000, yaw_limit: float = 0.000000, view_distance_limit: float = 0.000000) -> None
unreal.WDPSetCameraLockLimitParams.location_limit(value: float) -> None
unreal.WDPSetCameraLockLimitParams.pitch_limit(value: float) -> None
unreal.WDPSetCameraLockLimitParams.view_distance_limit(value: float) -> None
unreal.WDPSetCameraLockLimitParams.yaw_limit(value: float) -> None
```

## `unreal.WDPSetCameraModeParams(ParamsBase)`

```python
unreal.WDPSetCameraModeParams.__init__(control_mode: WdpCameraControlMode = WdpCameraControlMode.RTS) -> None
unreal.WDPSetCameraModeParams.control_mode(value: WdpCameraControlMode) -> None
```

## `unreal.WDPSetCameraSpeedParams(ParamsBase)`

```python
unreal.WDPSetCameraSpeedParams.__init__(rotation_yaw_speed_scale: float = 0.000000, rotation_pitch_speed_scale: float = 0.000000, zoom_speed_scale: float = 0.000000, key_movement_base_speed: float = 0.000000, enable_dynamic_speed: bool = False) -> None
unreal.WDPSetCameraSpeedParams.enable_dynamic_speed(value: bool) -> None
unreal.WDPSetCameraSpeedParams.key_movement_base_speed(value: float) -> None
unreal.WDPSetCameraSpeedParams.rotation_pitch_speed_scale(value: float) -> None
unreal.WDPSetCameraSpeedParams.rotation_yaw_speed_scale(value: float) -> None
unreal.WDPSetCameraSpeedParams.zoom_speed_scale(value: float) -> None
```

## `unreal.WDPUpdateCameraInfoParams(ParamsBase)`

```python
unreal.WDPUpdateCameraInfoParams.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: CameraPresetRotator = [0.000000, 0.000000], location_limit: Array[Vector2D] = [], pitch_limit: Vector2D = [0.000000, 0.000000], yaw_limit: Vector2D = [0.000000, 0.000000], view_distance_limit: Vector2D = [0.000000, 0.000000], control_mode: WdpCameraControlMode = WdpCameraControlMode.RTS, field_of_view: float = 0.000000, fly_time: float = 0.000000) -> None
unreal.WDPUpdateCameraInfoParams.control_mode(value: WdpCameraControlMode) -> None
unreal.WDPUpdateCameraInfoParams.field_of_view(value: float) -> None
unreal.WDPUpdateCameraInfoParams.fly_time(value: float) -> None
unreal.WDPUpdateCameraInfoParams.location(value: Vector) -> None
unreal.WDPUpdateCameraInfoParams.location_limit(value: Array[Vector2D]) -> None
unreal.WDPUpdateCameraInfoParams.pitch_limit(value: Vector2D) -> None
unreal.WDPUpdateCameraInfoParams.rotation(value: CameraPresetRotator) -> None
unreal.WDPUpdateCameraInfoParams.view_distance_limit(value: Vector2D) -> None
unreal.WDPUpdateCameraInfoParams.yaw_limit(value: Vector2D) -> None
```

## `unreal.WaveOscillatorCameraShakePattern(SimpleCameraShakePattern)`

```python
unreal.WaveOscillatorCameraShakePattern.fov(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.location_amplitude_multiplier(value: float) -> None
unreal.WaveOscillatorCameraShakePattern.location_frequency_multiplier(value: float) -> None
unreal.WaveOscillatorCameraShakePattern.pitch(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.roll(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.rotation_amplitude_multiplier(value: float) -> None
unreal.WaveOscillatorCameraShakePattern.rotation_frequency_multiplier(value: float) -> None
unreal.WaveOscillatorCameraShakePattern.x(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.y(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.yaw(value: WaveOscillator) -> None
unreal.WaveOscillatorCameraShakePattern.z(value: WaveOscillator) -> None
```

## `unreal.WdpBasePawn(Pawn)`

```python
unreal.WdpBasePawn.add_camera_around_pivot_rotation(delta_rotation: Rotator) -> None
unreal.WdpBasePawn.add_camera_distance_zoom_input(value: float) -> None
unreal.WdpBasePawn.add_camera_distance_zoom_value(delta_zoom: float) -> None
unreal.WdpBasePawn.add_camera_follow_actor_movement_value(delta_movement: Vector) -> None
unreal.WdpBasePawn.add_camera_fov_zoom_input(value: float) -> None
unreal.WdpBasePawn.add_camera_free_movement_value(delta_movement: Vector) -> None
unreal.WdpBasePawn.add_camera_height_movement_value(height: float) -> None
unreal.WdpBasePawn.add_camera_movement_input(axis_value: Vector2D) -> None
unreal.WdpBasePawn.add_camera_movement_input_up_down(value: float) -> None
unreal.WdpBasePawn.add_camera_rotate_around_input(value: Vector2D) -> None
unreal.WdpBasePawn.add_camera_rotate_self_input(value: Vector2D) -> None
unreal.WdpBasePawn.add_camera_self_rotation(delta_rotation: Rotator) -> None
unreal.WdpBasePawn.add_camera_surface_movement_value(delta_movement: Vector) -> None
unreal.WdpBasePawn.add_camera_zoom_input(value: float) -> None
unreal.WdpBasePawn.add_collision_ignore_actor(actor: Actor) -> None
unreal.WdpBasePawn.anim_start_camera_data(value: CoreCameraData) -> None
unreal.WdpBasePawn.anim_target_camera_data(value: CoreCameraData) -> None
unreal.WdpBasePawn.apply_camera_collision_data(collision_data: CameraCollisionData) -> bool
unreal.WdpBasePawn.apply_camera_data(new_camera_data: AllCameraData) -> None
unreal.WdpBasePawn.apply_pitch_limit(min_pitch: float = -89.000000, max_pitch: float = 89.000000) -> None
unreal.WdpBasePawn.apply_rotate_limit(new_rotate_limit: CameraRotationLimitationData) -> None
unreal.WdpBasePawn.apply_yaw_limit(min_yaw: float = -179.998993, max_yaw: float = 179.998993) -> None
unreal.WdpBasePawn.apply_zoom_limit(new_zoom_limit: CameraZoomLimitationData) -> None
unreal.WdpBasePawn.are_anim_blend_feature_enabled(features_to_test: int) -> bool
unreal.WdpBasePawn.are_features_enabled(features_to_test: int) -> bool
unreal.WdpBasePawn.auto_camera_self_rotation_settings(value: AutoSelfRotationSettings) -> None
unreal.WdpBasePawn.auto_follow_when_not_being_view_target(value: bool) -> None
unreal.WdpBasePawn.auto_follow_when_un_possessed(value: bool) -> None
unreal.WdpBasePawn.auto_movement_settings(value: AutoMovementSettings) -> None
unreal.WdpBasePawn.auto_rotate_direction() -> int
unreal.WdpBasePawn.auto_rotation_duration_range(value: Vector2D) -> None
unreal.WdpBasePawn.auto_rotation_settings(value: AutoRotationSettings) -> None
unreal.WdpBasePawn.auto_rotation_start_min_threshold(value: float) -> None
unreal.WdpBasePawn.auto_travel_duration_range(value: Vector2D) -> None
unreal.WdpBasePawn.boost_movement_scale(value: float) -> None
unreal.WdpBasePawn.calc_anim_cam_rotation(start_rotation: Rotator, target_rotation: Rotator, alpha: float) -> Rotator
unreal.WdpBasePawn.calc_auto_travel_duration(duration: float, target_location: Vector) -> float
unreal.WdpBasePawn.calc_camera_collision_result(start_location: Vector, target_location: Vector, collision_data: CameraCollisionData, limit_direction: bool) -> Optional[Tuple[Vector, Vector]]
unreal.WdpBasePawn.calc_camera_self_rotate_data(start_rotation: Rotator, start_location: Vector, remain_rotation: Rotator, pitch_limit: Vector2D, yaw_limit: Vector2D, roll: float) -> Tuple[Rotator, Rotator]
unreal.WdpBasePawn.calc_camera_surface_height_movement_data(start_location: Vector, surface_remain: Vector, height_remain: float) -> Tuple[Vector, Vector, float, Vector, Vector]
unreal.WdpBasePawn.calc_delta_camera_rotation_data(current_location: Vector, rotate_pivot: Vector, delta_rotation_in: Rotator) -> Tuple[Vector, Rotator]
unreal.WdpBasePawn.calc_double_click_core_data(current_data: AllCameraData, target: Vector, scale: float) -> CoreCameraData
unreal.WdpBasePawn.calc_fix_rotate_around_pitch_delta(pitch_delta: float, camera_loc: Vector, camera_rot: Rotator, pivot: Vector, pitch_limit: Vector2D) -> float
unreal.WdpBasePawn.calc_fixed_collision_profile(start: Vector, target: Vector, collision_profile: Name) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_fixed_ground_position(start: Vector, target: Vector, ground_position_mode: GroundPositionMode = GroundPositionMode.GPM_AVOID_ONLY) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_follow_actor_movement_delta_value(current_location: Vector, follow_move_remain: Vector) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_free_movement_delta_value(current_location: Vector, free_move_remain: Vector) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_height_movement_delta_value(current_location: Vector, up_direction: Vector, remain_height: float) -> Tuple[Vector, Vector, float]
unreal.WdpBasePawn.calc_move_value_along_surface(start: Vector, surface_dir: Vector) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_pitch_from_pivot_camera_dir_local(camera_loc: Vector, camera_rot: Rotator, pivot: Vector) -> float
unreal.WdpBasePawn.calc_pitch_from_rotate_pivot_local(camera_loc: Vector, pivot: Vector) -> float
unreal.WdpBasePawn.calc_rotate_around_camera_data(start_rotation: Rotator, start_location: Vector, remain_rotation: Rotator, pivot: Vector, pitch_limit: Vector2D, yaw_limit: Vector2D) -> Tuple[Vector, Rotator, Rotator, Vector]
unreal.WdpBasePawn.calc_rotate_around_collision_value(pivot: Vector, start_location: Vector, target_location: Vector, collision_data: CameraCollisionData) -> Optional[Tuple[Vector, float]]
unreal.WdpBasePawn.calc_rotate_around_pivot_value(start_loc: Vector, start_rot: Rotator, pivot: Vector, pitch: float, yaw: float) -> Tuple[Vector, Rotator]
unreal.WdpBasePawn.calc_rotate_pivot_surface_move(start_camera_location: Vector, pivot: Vector, camera_surface_delta: Vector, camera_height_delta: Vector) -> Vector
unreal.WdpBasePawn.calc_split_movement_to_surface_and_height(move_direction: Vector, move_distance: float) -> Tuple[Vector, float]
unreal.WdpBasePawn.calc_surface_movement_delta_value(current: Vector) -> Tuple[Vector, Vector]
unreal.WdpBasePawn.calc_zoom_collision_block_value(start: Vector, target: Vector, collision_data: CameraCollisionData) -> Optional[Tuple[Vector, float]]
unreal.WdpBasePawn.calc_zoom_tick_delta_value(current: Vector, zoom_target: Vector, remain_distance: float) -> Tuple[Vector, Vector, float, float]
unreal.WdpBasePawn.camera_additional_rotate_scale(value: float) -> None
unreal.WdpBasePawn.camera_around_pivot_remain_rotation(value: Rotator) -> None
unreal.WdpBasePawn.camera_follow_actor_remain_location(value: Vector) -> None
unreal.WdpBasePawn.camera_free_movement_remain_location(value: Vector) -> None
unreal.WdpBasePawn.camera_height_movement_remain_distance(value: float) -> None
unreal.WdpBasePawn.camera_height_to_virtual_plane(value: float) -> None
unreal.WdpBasePawn.camera_roll(value: float) -> None
unreal.WdpBasePawn.camera_root() -> SceneComponent
unreal.WdpBasePawn.camera_rotate_mode(value: CameraRotateMode) -> None
unreal.WdpBasePawn.camera_self_remain_rotation(value: Rotator) -> None
unreal.WdpBasePawn.camera_surface_movement_remain_location(value: Vector) -> None
unreal.WdpBasePawn.camera_touch_input_sensitivity(value: float) -> None
unreal.WdpBasePawn.camera_travel_base_curve(value: CurveFloat) -> None
unreal.WdpBasePawn.camera_travel_curve_sample_count(value: int) -> None
unreal.WdpBasePawn.camera_travel_max_height_difference_scale(value: float) -> None
unreal.WdpBasePawn.camera_zoom_remain_distance(value: float) -> None
unreal.WdpBasePawn.can_keep_zooming_input(target: Vector, action_value: float) -> bool
unreal.WdpBasePawn.check_auto_break_movement(input_type: UserInputActionType) -> None
unreal.WdpBasePawn.check_should_break_following(auto_break: bool) -> bool
unreal.WdpBasePawn.clamp_fixed_collision_custom_points(start: Vector, target: Vector, custom_points: Array[Vector], limit_direction: bool = False) -> Vector
unreal.WdpBasePawn.clamp_target_point_in_zoom_distance_limit(target_point: Vector) -> Vector
unreal.WdpBasePawn.clear_all_remain_movement() -> None
unreal.WdpBasePawn.clear_collision_ignore_actors() -> None
unreal.WdpBasePawn.click_begin_camera_location(value: Vector) -> None
unreal.WdpBasePawn.click_begin_pointer_location(value: Vector) -> None
unreal.WdpBasePawn.click_begin_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.click_pointer_current_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.click_pointer_last_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.click_pointer_screen_delta_position(value: Vector2D) -> None
unreal.WdpBasePawn.collision_ignore_actors(value: Array[Actor]) -> None
unreal.WdpBasePawn.conver_transform_to_surface_space(origin: Vector, transform: Transform) -> Transform
unreal.WdpBasePawn.convert_rotation_to_surface_space(location: Vector, rotation: Rotator) -> Rotator
unreal.WdpBasePawn.convert_surface_rotation_to_world(location: Vector, rotation: Rotator) -> Rotator
unreal.WdpBasePawn.current_camera_data(value: AllCameraData) -> None
unreal.WdpBasePawn.current_camera_fov(value: float) -> None
unreal.WdpBasePawn.default_mapping_context() -> InputMappingContext
unreal.WdpBasePawn.default_trace_channel(value: TraceTypeQuery) -> None
unreal.WdpBasePawn.default_world_plane_height(value: float) -> None
unreal.WdpBasePawn.desired_camera_fov(value: float) -> None
unreal.WdpBasePawn.desired_camera_rotation(value: Rotator) -> None
unreal.WdpBasePawn.disable_features(features_to_disable: int) -> None
unreal.WdpBasePawn.distance_to_move_angle_curve(value: CurveFloat) -> None
unreal.WdpBasePawn.distance_zoom_speed(value: float) -> None
unreal.WdpBasePawn.double_click_zoom_scale(value: float) -> None
unreal.WdpBasePawn.drag_last_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.drag_start_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.drag_threshold_pitch_angle(value: float) -> None
unreal.WdpBasePawn.draw_debug_shapes(value: bool) -> None
unreal.WdpBasePawn.e_animation_blend_features(value: int) -> None
unreal.WdpBasePawn.enable_auto_rotation_after_travel(value: bool) -> None
unreal.WdpBasePawn.enable_camera_lag(value: bool) -> None
unreal.WdpBasePawn.enable_features(features_to_enable: int) -> None
unreal.WdpBasePawn.enable_input_when_not_being_view_target(value: bool) -> None
unreal.WdpBasePawn.enable_rotation_lag(value: bool) -> None
unreal.WdpBasePawn.enable_user_input(value: bool) -> None
unreal.WdpBasePawn.enabled_features() -> int
unreal.WdpBasePawn.final_camera_data(value: AllCameraData) -> None
unreal.WdpBasePawn.fix_core_camera_data(core_camera_data_in: CoreCameraData) -> CoreCameraData
unreal.WdpBasePawn.fix_pawn_movement_by_collision(start: Vector, target: Vector, profile_name: Name, ground_only: bool = False) -> Vector
unreal.WdpBasePawn.fix_rotate_around_collision_angle(pivot: Vector, start_location: Vector, target_location: Vector, collide_location: Vector, start_rotation: Rotator, delta_rotation: Rotator) -> Rotator
unreal.WdpBasePawn.follow_actor_lag_speed(value: float) -> None
unreal.WdpBasePawn.follow_traget_tick() -> None
unreal.WdpBasePawn.following_actor(value: Actor) -> None
unreal.WdpBasePawn.following_actor_last_location(value: Vector) -> None
unreal.WdpBasePawn.following_mode(value: FollowingMode) -> None
unreal.WdpBasePawn.following_time(value: float) -> None
unreal.WdpBasePawn.fov_lag_speed(value: float) -> None
unreal.WdpBasePawn.fov_zoom_speed(value: float) -> None
unreal.WdpBasePawn.get_alternative_forward_vector(rotation: Rotator, pivot: Vector) -> Vector
unreal.WdpBasePawn.get_alternative_right_vector(rotation: Rotator, pivot: Vector) -> Vector
unreal.WdpBasePawn.get_alternative_up_vector(rotation: Rotator, pivot: Vector) -> Vector
unreal.WdpBasePawn.get_camera_collision_data() -> CameraCollisionData
unreal.WdpBasePawn.get_camera_height_to_ground() -> float
unreal.WdpBasePawn.get_camera_height_to_ground_at_location(location: Vector) -> float
unreal.WdpBasePawn.get_camera_pitch_from_rotate_pivot() -> float
unreal.WdpBasePawn.get_click_hit_result(trace_channel: TraceTypeQuery) -> Optional[HitResult]
unreal.WdpBasePawn.get_click_object_hit_result(object_types: Array[ObjectTypeQuery]) -> Optional[HitResult]
unreal.WdpBasePawn.get_click_screen_position() -> Optional[Tuple[Vector2D, Vector2D]]
unreal.WdpBasePawn.get_collision_ignore_actors() -> Array[Actor]
unreal.WdpBasePawn.get_control_mode() -> ControlMode
unreal.WdpBasePawn.get_core_camera_data() -> CoreCameraData
unreal.WdpBasePawn.get_current_camera_data() -> AllCameraData
unreal.WdpBasePawn.get_current_zoom_distance() -> float
unreal.WdpBasePawn.get_default_touch_index() -> TouchIndex
unreal.WdpBasePawn.get_desired_rotate_pivot() -> Vector
unreal.WdpBasePawn.get_desired_zoom_distance() -> float
unreal.WdpBasePawn.get_desired_zoom_location() -> Vector
unreal.WdpBasePawn.get_desired_zoom_target_location() -> Optional[Tuple[Vector, Vector]]
unreal.WdpBasePawn.get_direction_hit_result(start: Vector, direction: Vector, trace_channel: TraceTypeQuery) -> Optional[HitResult]
unreal.WdpBasePawn.get_direction_object_hit_result(start: Vector, direction: Vector, trace_channel: CollisionChannel) -> Optional[HitResult]
unreal.WdpBasePawn.get_enable_camera_collision() -> bool
unreal.WdpBasePawn.get_enable_target_effect() -> bool
unreal.WdpBasePawn.get_enable_touch_effect() -> bool
unreal.WdpBasePawn.get_enable_user_input() -> bool
unreal.WdpBasePawn.get_enabled_features() -> int
unreal.WdpBasePawn.get_following_target_location() -> Vector
unreal.WdpBasePawn.get_following_zoom_limit() -> Vector2D
unreal.WdpBasePawn.get_fov_limit() -> Vector2D
unreal.WdpBasePawn.get_is_active_dargging() -> bool
unreal.WdpBasePawn.get_is_earth_mode() -> bool
unreal.WdpBasePawn.get_is_pointer_on_valid_dragging_position() -> bool
unreal.WdpBasePawn.get_is_view_target() -> bool
unreal.WdpBasePawn.get_last_conformed_zoom_location() -> Vector
unreal.WdpBasePawn.get_main_camera_forward_vector() -> Vector
unreal.WdpBasePawn.get_main_camera_fov() -> float
unreal.WdpBasePawn.get_main_camera_location() -> Vector
unreal.WdpBasePawn.get_main_camera_rotation() -> Rotator
unreal.WdpBasePawn.get_mouse_target_direction(force_center: bool) -> Vector
unreal.WdpBasePawn.get_movement_scale_factor() -> float
unreal.WdpBasePawn.get_pitch_limit() -> Vector2D
unreal.WdpBasePawn.get_rotate_pivot() -> Vector
unreal.WdpBasePawn.get_safe_click_location_on_plane(fallback_height: float) -> Vector
unreal.WdpBasePawn.get_screen_center_hit_result(trace_channel: TraceTypeQuery) -> Optional[HitResult]
unreal.WdpBasePawn.get_screen_center_object_hit_result(object_types: Array[ObjectTypeQuery]) -> Optional[HitResult]
unreal.WdpBasePawn.get_screen_center_position() -> Vector2D
unreal.WdpBasePawn.get_screen_position_hit_result(screen_position: Vector2D, trace_channel: TraceTypeQuery) -> Optional[HitResult]
unreal.WdpBasePawn.get_speed() -> float
unreal.WdpBasePawn.get_start_rotate_pivot(rotate_mode: CameraRotateMode) -> Optional[Vector]
unreal.WdpBasePawn.get_true_desired_location() -> Vector
unreal.WdpBasePawn.get_world_plane_normal() -> Vector
unreal.WdpBasePawn.get_world_plane_normal_at_location(location: Vector) -> Vector
unreal.WdpBasePawn.get_world_rotation_on_surface(origin: Vector) -> Rotator
unreal.WdpBasePawn.get_yaw_limit() -> Vector2D
unreal.WdpBasePawn.get_zoom_direction() -> Vector
unreal.WdpBasePawn.get_zoom_limit() -> Vector2D
unreal.WdpBasePawn.ground_component_tag(value: Name) -> None
unreal.WdpBasePawn.ground_trace_channel(value: CollisionChannel) -> None
unreal.WdpBasePawn.ground_trace_object_types(value: Array[ObjectTypeQuery]) -> None
unreal.WdpBasePawn.height_to_move_speed_curve(value: CurveFloat) -> None
unreal.WdpBasePawn.idle_time() -> float
unreal.WdpBasePawn.init_input_mapping() -> None
unreal.WdpBasePawn.init_pawn_settings() -> None
unreal.WdpBasePawn.init_starting_position() -> None
unreal.WdpBasePawn.init_travel_animation() -> None
unreal.WdpBasePawn.init_virtual_pivot_location() -> None
unreal.WdpBasePawn.init_world_origin_anchor() -> None
unreal.WdpBasePawn.inner_input_event_delegate(value: PawnInnerDelegate) -> None
unreal.WdpBasePawn.input_event_delegate(value: PawnInnerDelegate) -> None
unreal.WdpBasePawn.is_auto_camera_self_rotation_active(value: bool) -> None
unreal.WdpBasePawn.is_auto_movement_active(value: bool) -> None
unreal.WdpBasePawn.is_auto_rotation_active(value: bool) -> None
unreal.WdpBasePawn.is_camera_traveling(value: bool) -> None
unreal.WdpBasePawn.is_dragging_active(value: bool) -> None
unreal.WdpBasePawn.is_following_actor(value: bool) -> None
unreal.WdpBasePawn.is_following_any_actor() -> bool
unreal.WdpBasePawn.is_point_in_custom_points_range(point: Vector, custom_points: Array[Vector]) -> bool
unreal.WdpBasePawn.is_pointer_in_valid_dragging_position(direction: Vector) -> bool
unreal.WdpBasePawn.is_rotate_active(value: bool) -> None
unreal.WdpBasePawn.is_self_rotate_key_pressed() -> bool
unreal.WdpBasePawn.key_move_forward_direction(value: MoveForwardDirection) -> None
unreal.WdpBasePawn.key_movement_mode(value: KeyMovementMode) -> None
unreal.WdpBasePawn.last_click_hit_result(value: HitResult) -> None
unreal.WdpBasePawn.last_click_world_height(value: float) -> None
unreal.WdpBasePawn.last_conformed_zoom_location(value: Vector) -> None
unreal.WdpBasePawn.last_delta_time() -> float
unreal.WdpBasePawn.last_location() -> Vector
unreal.WdpBasePawn.last_rotate_world_height(value: float) -> None
unreal.WdpBasePawn.limit_camera_pitch(view_rotation: Rotator, view_pitch_min: float = -89.000000, view_pitch_max: float = 89.000000) -> Rotator
unreal.WdpBasePawn.limit_camera_yaw(view_rotation: Rotator, view_yaw_min: float = -179.998993, view_yaw_max: float = 179.998993) -> Rotator
unreal.WdpBasePawn.limit_zoom_direction(value: bool) -> None
unreal.WdpBasePawn.main_camera() -> CameraComponent
unreal.WdpBasePawn.min_fallback_zoom_distance(value: float) -> None
unreal.WdpBasePawn.min_movement_speed(value: float) -> None
unreal.WdpBasePawn.min_up_down_movement_speed(value: float) -> None
unreal.WdpBasePawn.min_zoom_step(value: float) -> None
unreal.WdpBasePawn.move_key_pressed(value: bool) -> None
unreal.WdpBasePawn.movement_lag_speed(value: float) -> None
unreal.WdpBasePawn.on_double_click_triggered(screen_position: Vector2D) -> None
unreal.WdpBasePawn.on_pointer_key_move(screen_position: Vector2D) -> None
unreal.WdpBasePawn.on_pointer_key_pressed(screen_position: Vector2D) -> None
unreal.WdpBasePawn.on_pointer_key_released() -> None
unreal.WdpBasePawn.on_rotate_key_pressed(screen_position: Vector2D) -> None
unreal.WdpBasePawn.on_rotate_key_released() -> None
unreal.WdpBasePawn.on_travel_animation_finished(value: OnTravelAnimationFinished) -> None
unreal.WdpBasePawn.on_zoom_key_pressed(screen_position: Vector2D) -> None
unreal.WdpBasePawn.on_zoom_key_released() -> None
unreal.WdpBasePawn.override_starting_location(value: bool) -> None
unreal.WdpBasePawn.override_starting_pitch(value: bool) -> None
unreal.WdpBasePawn.override_starting_yaw(value: bool) -> None
unreal.WdpBasePawn.pointer_key_pressed(value: bool) -> None
unreal.WdpBasePawn.print_debug_string(string: str = "Debug", duration: float = 2.000000, text_color: LinearColor = [0.000000, 0.660000, 1.000000, 1.000000]) -> None
unreal.WdpBasePawn.remove_collision_ignore_actor(actor: Actor) -> None
unreal.WdpBasePawn.remove_input_mapping() -> None
unreal.WdpBasePawn.reset_idle_time() -> None
unreal.WdpBasePawn.rotate_current_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.rotate_delta_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.rotate_key_pressed(value: bool) -> None
unreal.WdpBasePawn.rotate_last_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.rotate_pivot_use_real_world_collision(value: bool) -> None
unreal.WdpBasePawn.rotate_start_pivot_location(value: Vector) -> None
unreal.WdpBasePawn.rotate_start_screen_position(value: Vector2D) -> None
unreal.WdpBasePawn.rotate_start_zoom_distance(value: float) -> None
unreal.WdpBasePawn.rotate_threshold_pitch_angle(value: float) -> None
unreal.WdpBasePawn.rotation_lag_speed(value: float) -> None
unreal.WdpBasePawn.runtime_camera_data(value: RuntimeCameraData) -> None
unreal.WdpBasePawn.safe_move_pawn_by_collision(start: Vector, delta: Vector, profile_name: Name, sweep: bool, ground_only: bool = False) -> Tuple[Vector, HitResult]
unreal.WdpBasePawn.scaling_distance_reference(value: float) -> None
unreal.WdpBasePawn.self_rotate_key_pressed(value: bool) -> None
unreal.WdpBasePawn.set_camera_desired_self_rotation(desired_rotation: Rotator) -> None
unreal.WdpBasePawn.set_camera_desired_self_rotation_surface_space(desired_location: Vector, desired_surface_rotation: Rotator) -> None
unreal.WdpBasePawn.set_camera_free_movement_desired_location(desired_location: Vector) -> None
unreal.WdpBasePawn.set_camera_rotate_mode(new_mode: CameraRotateMode) -> None
unreal.WdpBasePawn.set_desired_fov(new_fov: float = 90.000000, ignore_lag: bool = False) -> None
unreal.WdpBasePawn.set_enabled_features(features_to_enable: int) -> None
unreal.WdpBasePawn.set_rotate_pivot(new_pivot: Vector) -> None
unreal.WdpBasePawn.set_virtual_pivot_location(new_pivot: Vector) -> None
unreal.WdpBasePawn.set_world_plane_height(new_height: float) -> None
unreal.WdpBasePawn.should_auto_update_pivot() -> bool
unreal.WdpBasePawn.should_enable_move_collision() -> bool
unreal.WdpBasePawn.should_update_arm_collision() -> bool
unreal.WdpBasePawn.show_debug_log(value: bool) -> None
unreal.WdpBasePawn.show_debug_status(value: bool) -> None
unreal.WdpBasePawn.single_sphere_trace_ground(start: Vector, end: Vector) -> Optional[HitResult]
unreal.WdpBasePawn.sphere_component() -> SphereComponent
unreal.WdpBasePawn.sphere_trace_move_by_profile(start: Vector, end: Vector, profile_name: Name) -> Optional[HitResult]
unreal.WdpBasePawn.start_following_actor(target_actor: Actor, follow_mode: FollowingMode = FollowingMode.FM_TRACKING_LIGHT, duration: float = 1.200000) -> None
unreal.WdpBasePawn.start_mouse_drag(screen_position: Vector2D) -> None
unreal.WdpBasePawn.start_travel_animation(target_data: AllCameraData, settings: TravelAnimationSettings, duration: float = 1.200000) -> None
unreal.WdpBasePawn.starting_location(value: Vector) -> None
unreal.WdpBasePawn.starting_pitch(value: float) -> None
unreal.WdpBasePawn.starting_yaw(value: float) -> None
unreal.WdpBasePawn.stop_all_camera_movement() -> None
unreal.WdpBasePawn.stop_auto_camera_self_rotation() -> None
unreal.WdpBasePawn.stop_camera_auto_movement() -> None
unreal.WdpBasePawn.stop_camera_auto_rotation() -> None
unreal.WdpBasePawn.stop_following_actor() -> None
unreal.WdpBasePawn.stop_mouse_drag() -> None
unreal.WdpBasePawn.tick_camera() -> None
unreal.WdpBasePawn.tick_delta() -> float
unreal.WdpBasePawn.toggle_auto_camera_self_rotation(active: bool, settings: AutoSelfRotationSettings) -> None
unreal.WdpBasePawn.toggle_auto_movement(active: bool, settings: AutoMovementSettings) -> bool
unreal.WdpBasePawn.toggle_auto_rotation(active: bool, settings: AutoRotationSettings) -> bool
unreal.WdpBasePawn.toggle_following_actor(target_actor: Actor, follow: bool) -> None
unreal.WdpBasePawn.toggle_mouse_drag(activate: bool) -> None
unreal.WdpBasePawn.toggle_rotating_active(activate: bool) -> None
unreal.WdpBasePawn.toggle_self_rotate_key_pressed(pressed: bool) -> None
unreal.WdpBasePawn.toggle_show_debug(show_log: bool, show_status: bool, show_shapes: bool) -> None
unreal.WdpBasePawn.toggle_speed_up(boost: float) -> None
unreal.WdpBasePawn.total_auto_rotate_angle() -> float
unreal.WdpBasePawn.travel_anim_duration(value: float) -> None
unreal.WdpBasePawn.travel_animtion_settings(value: TravelAnimationSettings) -> None
unreal.WdpBasePawn.travel_pivot_spline_component(value: SplineComponent) -> None
unreal.WdpBasePawn.travel_spline_component(value: SplineComponent) -> None
unreal.WdpBasePawn.up_down_movement_speed(value: float) -> None
unreal.WdpBasePawn.update_auto_camera_self_rotation() -> None
unreal.WdpBasePawn.update_auto_movement() -> None
unreal.WdpBasePawn.update_auto_rotation() -> None
unreal.WdpBasePawn.update_camera_fov(desired_fov: float = 90.000000, ignore_lag: bool = False) -> None
unreal.WdpBasePawn.update_camera_instant(camera_data: CoreCameraData) -> bool
unreal.WdpBasePawn.update_camera_location(new_location: Vector) -> None
unreal.WdpBasePawn.update_camera_rotation(new_rotation: Rotator) -> None
unreal.WdpBasePawn.update_debug_shapes() -> None
unreal.WdpBasePawn.update_debug_status() -> None
unreal.WdpBasePawn.update_idle_time() -> None
unreal.WdpBasePawn.update_mouse_drag(screen_position: Vector2D) -> None
unreal.WdpBasePawn.update_rotate_pivot_by_movement(start_camera_location: Vector, camera_surface_delta: Vector, camera_height_delta: Vector) -> None
unreal.WdpBasePawn.update_runtime_camera_data() -> None
unreal.WdpBasePawn.update_start_auto_rotation_after_travel(target_rotation: Rotator, duration: float) -> None
unreal.WdpBasePawn.update_travel_animation(alpha: float) -> None
unreal.WdpBasePawn.update_virtual_pivot() -> None
unreal.WdpBasePawn.use_clamped_target_when_dragging(value: bool) -> None
unreal.WdpBasePawn.use_pivot_as_zoom_target_when_input(value: bool) -> None
unreal.WdpBasePawn.use_rotate_value_from_input(value: bool) -> None
unreal.WdpBasePawn.use_screen_center_as_zoom_direction(value: bool) -> None
unreal.WdpBasePawn.use_tag_find_ground(value: bool) -> None
unreal.WdpBasePawn.use_vertical_fov(value: bool) -> None
unreal.WdpBasePawn.user_camera_settings(value: UserCameraSettings) -> None
unreal.WdpBasePawn.velocity() -> Vector
unreal.WdpBasePawn.virtual_camera_diatance(value: float) -> None
unreal.WdpBasePawn.virtual_pivot_location(value: Vector) -> None
unreal.WdpBasePawn.wdp_common_input() -> WdpCommonInput
unreal.WdpBasePawn.world_origin_anchor() -> WorldOriginAnchor
unreal.WdpBasePawn.zoom_action_type(value: ZoomActionType) -> None
unreal.WdpBasePawn.zoom_key_pressed(value: bool) -> None
unreal.WdpBasePawn.zoom_lag_speed(value: float) -> None
unreal.WdpBasePawn.zoom_start_screen_position() -> Vector2D
unreal.WdpBasePawn.zoom_target_location(value: Vector) -> None
```

## `unreal.WdpCameraBPLibrary(BlueprintFunctionLibrary)`

```python
unreal.WdpCameraBPLibrary.calc_focus_info_to_camera_data(target: Vector, distance: float, rotation: Rotator) -> Vector
unreal.WdpCameraBPLibrary.calc_focus_to_lon_lat_alt_to_camera_data(world_context_object: Object, lon: float, lat: float, alt: float, keep_rotation: bool, distance: float = 1000.000000, surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]) -> Optional[CoreCameraData]
unreal.WdpCameraBPLibrary.calc_lon_lat_alt_to_core_camera_data(world_context_object: Object, lon: float, lat: float, alt: float, keep_rotation: bool, surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]) -> Optional[CoreCameraData]
unreal.WdpCameraBPLibrary.calc_lon_lat_alt_to_world_location_rotation(world_context_object: Object, lon: float, lat: float, alt: float, local_rotation: Rotator) -> Optional[Tuple[Vector, Rotator]]
unreal.WdpCameraBPLibrary.calc_look_at_info_to_camera_data(target: Vector, current_location: Vector, use_distance: bool, distance: float, rotate_limit: CameraRotationLimitationData, override_pitch: bool, pitch: float) -> Tuple[Vector, Rotator]
unreal.WdpCameraBPLibrary.change_camera_auto_rotate_around_pivot(world_context_object: Object, target: Vector, settings: AutoRotationSettings, change_distance: bool = False, distance: float = 1000.000000, override_pitch: bool = False, pitch: float = -45.000000, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.change_camera_core_data(world_context_object: Object, target_core_camera_data: CoreCameraData, settings: TravelAnimationSettings, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.change_camera_focus_to_point(world_context_object: Object, target_location: Vector, settings: TravelAnimationSettings, distance: float = 5000.000000, duration: float = 0.500000) -> bool
unreal.WdpCameraBPLibrary.change_camera_focus_to_point_with_rotation(world_context_object: Object, target_location: Vector, target_rotation: Rotator, settings: TravelAnimationSettings, distance: float = 5000.000000, duration: float = 0.500000) -> bool
unreal.WdpCameraBPLibrary.change_camera_focus_to_points(world_context_object: Object, target_locations: Array[Vector], settings: TravelAnimationSettings, scale: float = 1.000000, min_distance: float = 5000.000000, duration: float = 0.500000) -> bool
unreal.WdpCameraBPLibrary.change_camera_index(world_context_object: Object, tag: GameplayTag, index: int, settings: TravelAnimationSettings, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.change_camera_look_at(world_context_object: Object, target: Vector, settings: TravelAnimationSettings, change_distance: bool = False, distance: float = 1000.000000, override_pitch: bool = False, pitch: float = -45.000000, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.change_camera_preset_data_api(world_context_object: Object, camera_location: Vector, camera_rotation: Rotator, pitch_limit: Vector2D = [-89.000000, 0.000000], yaw_limit: Vector2D = [-179.999000, 179.999000], distance_limit: Vector2D = [0.000000, 10000000.000000], fov: float = 90.000000, control_mode: Name = "RTS", duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.change_camera_standard(world_context_object: Object, target_camera_data: AllCameraData, settings: TravelAnimationSettings, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.convert_core_camera_data_to_surface_space(world_context_object: Object, core_camera_data_world_space: CoreCameraData) -> CoreCameraData
unreal.WdpCameraBPLibrary.convert_core_camera_data_to_world_space(world_context_object: Object, core_camera_data_surface_space: CoreCameraData) -> CoreCameraData
unreal.WdpCameraBPLibrary.find_camera_preset_by_index(world_context_object: Object, tag: GameplayTag, index: int) -> Optional[WdpCameraPresetActor]
unreal.WdpCameraBPLibrary.get_camera_collision_data(world_context_object: Object) -> Optional[CameraCollisionData]
unreal.WdpCameraBPLibrary.get_camera_core_data(world_context_object: Object) -> Optional[CoreCameraData]
unreal.WdpCameraBPLibrary.get_camera_limit_data(world_context_object: Object) -> Optional[Tuple[CameraRotationLimitationData, CameraZoomLimitationData]]
unreal.WdpCameraBPLibrary.get_current_camera_data(world_context_object: Object) -> Optional[AllCameraData]
unreal.WdpCameraBPLibrary.get_user_camera_settings(world_context_object: Object) -> Optional[UserCameraSettings]
unreal.WdpCameraBPLibrary.get_wdp_player_controller(world_context_object: Object, index: int = 0) -> WdpPlayerController
unreal.WdpCameraBPLibrary.get_wdp_player_pawn(world_context_object: Object, index: int = 0) -> WdpBasePawn
unreal.WdpCameraBPLibrary.possess_to_new_pawn(world_context_object: Object, new_pawn: Pawn, duration: float = 0.000000, index: int = 0) -> None
unreal.WdpCameraBPLibrary.remote_input_movement_value_update(world_context_object: Object, value: Vector) -> bool
unreal.WdpCameraBPLibrary.remote_input_rotate_key_value_update(world_context_object: Object, value: Vector2D) -> bool
unreal.WdpCameraBPLibrary.remote_input_toggle_rotate_key_pressed_released(world_context_object: Object, is_pressed: bool = False) -> bool
unreal.WdpCameraBPLibrary.remote_input_toggle_zoom_key_pressed_released(world_context_object: Object, is_pressed: bool = False) -> bool
unreal.WdpCameraBPLibrary.remote_input_zoom_key_value_update(world_context_object: Object, value: float) -> bool
unreal.WdpCameraBPLibrary.set_camera_collision_data(world_context_object: Object, collision_data: CameraCollisionData) -> bool
unreal.WdpCameraBPLibrary.set_camera_limit_data(world_context_object: Object, rotation_limit: CameraRotationLimitationData, zoom_limit: CameraZoomLimitationData) -> bool
unreal.WdpCameraBPLibrary.set_user_camera_settings(world_context_object: Object, user_camera_settings: UserCameraSettings) -> bool
unreal.WdpCameraBPLibrary.start_following_actor(world_context_object: Object, target_actor: Actor, follow_mode: FollowingMode = FollowingMode.FM_TRACKING_LIGHT, duration: float = 1.200000) -> bool
unreal.WdpCameraBPLibrary.stop_all_camera_movement(world_context_object: Object) -> bool
unreal.WdpCameraBPLibrary.stop_following_actor(world_context_object: Object) -> bool
unreal.WdpCameraBPLibrary.toggle_auto_movement(world_context_object: Object, active: bool, auto_movement_settings: AutoMovementSettings) -> bool
unreal.WdpCameraBPLibrary.toggle_auto_rotation(world_context_object: Object, active: bool, auto_rotation_settings: AutoRotationSettings) -> bool
unreal.WdpCameraBPLibrary.toggle_camera_self_auto_rotation(world_context_object: Object, active: bool, settings: AutoSelfRotationSettings) -> bool
unreal.WdpCameraBPLibrary.toggle_following_actor(world_context_object: Object, target_actor: Actor, follow: bool = False) -> bool
unreal.WdpCameraBPLibrary.un_possess_and_return(world_context_object: Object, duration: float = 0.000000, index: int = 0) -> None
```

## `unreal.WdpCameraControlAPI(StandardApiClassBase)`

```python
unreal.WdpCameraControlAPI.apply_camera_preset(params: CameraPresetApplyParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_around(params: WDPCameraAroundParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_move(params: WDPCameraMoveTransformParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_rotate(params: WDPCameraRotateTransformParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_step_move(params: CameraStepMoveParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_step_rotate(params: CameraStepRotateParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_step_zoom(params: CameraStepZoomParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.camera_stop(params: ParamsBase) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.focus_to_all_entities(params: WdpFocusToAllEntitiesParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.focus_to_box(params: WDPFocusBoxParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.focus_to_entities(params: WDPFocusEntitiesParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.focus_to_nodes(params: WDPFocusNodesParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.focus_to_position(params: WDPFocusPositionParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.follow_entity(params: WDPFollowEntityParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.get_camera_animation(params: ParamsBase) -> Optional[WDPGetCameraAnimationResult]
unreal.WdpCameraControlAPI.get_camera_info(params: ParamsBase) -> Optional[WDPGetCameraInfoResult]
unreal.WdpCameraControlAPI.get_camera_limit(params: ParamsBase) -> Optional[WDPGetCameraLimitResult]
unreal.WdpCameraControlAPI.get_camera_pose(params: ParamsBase) -> Optional[WDPGetCameraPoseResult]
unreal.WdpCameraControlAPI.get_camera_roaming_info(params: GetCameraRoamingInfoParams) -> Optional[GetCameraRoamingInfoResult]
unreal.WdpCameraControlAPI.get_camera_speed(params: ParamsBase) -> Optional[WDPGetCameraSpeedResult]
unreal.WdpCameraControlAPI.play_camera_roam(params: WDPCameraRoamParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.reset_camera_limit(params: WDPResetCameraLimitParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.reset_camera_pose(params: WDPResetCameraPoseParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_animation(params: WDPSetCameraAnimationParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_limit(params: WDPSetCameraLimitParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_lock_limit(params: WDPSetCameraLockLimitParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_mode(params: WDPSetCameraModeParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_pose(params: WDPSetCameraPoseParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.set_camera_speed(params: WDPSetCameraSpeedParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.stop_camera_step_update(params: ParamsBase) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.toggle_camera_self_rotate(params: ToggleCameraSelfRotateParams) -> Optional[ResultBase]
unreal.WdpCameraControlAPI.update_camera(params: WDPUpdateCameraInfoParams) -> Optional[ResultBase]
```

## `unreal.WdpCameraControlInterface(Interface)`

```python
unreal.WdpCameraControlInterface.bpi_change_camera_standard(camera_data: AllCameraData, settings: TravelAnimationSettings, duration: float = 1.200000) -> None
unreal.WdpCameraControlInterface.bpi_get_current_camera_data() -> Optional[AllCameraData]
unreal.WdpCameraControlInterface.bpi_get_user_camera_settings() -> Optional[UserCameraSettings]
unreal.WdpCameraControlInterface.bpi_play_camera_core_data(core_camera_data: CoreCameraData, settings: TravelAnimationSettings, duration: float = 1.200000) -> None
unreal.WdpCameraControlInterface.bpi_set_camera_collision_info(collision_data: CameraCollisionData) -> bool
unreal.WdpCameraControlInterface.bpi_set_camera_limit_info(rotation_limit: CameraRotationLimitationData, zoom_limit: CameraZoomLimitationData) -> bool
unreal.WdpCameraControlInterface.bpi_set_user_camera_settings(user_camera_settings: UserCameraSettings) -> bool
unreal.WdpCameraControlInterface.bpi_stop_all_camera_animation() -> None
unreal.WdpCameraControlInterface.bpi_toggle_camera_auto_movement(active: bool, settings: AutoMovementSettings) -> bool
unreal.WdpCameraControlInterface.bpi_toggle_camera_auto_rotation(active: bool, settings: AutoRotationSettings) -> bool
unreal.WdpCameraControlInterface.bpi_toggle_camera_self_auto_rotation(active: bool, settings: AutoSelfRotationSettings) -> bool
```

## `unreal.WdpCameraRoamFrame(StructBase)`

```python
unreal.WdpCameraRoamFrame.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: CameraPresetRotator = [0.000000, 0.000000], time: float = 0.000000) -> None
unreal.WdpCameraRoamFrame.location() -> Vector
unreal.WdpCameraRoamFrame.rotation() -> CameraPresetRotator
unreal.WdpCameraRoamFrame.time() -> float
```

## `unreal.WdpCameraSettingsAtom(EntityAtomBase)`

```python
unreal.WdpCameraSettingsAtom.enable_dynamic_speed(value: bool) -> None
unreal.WdpCameraSettingsAtom.key_movement_base_speed(value: float) -> None
unreal.WdpCameraSettingsAtom.rotation_pitch_speed_scale(value: float) -> None
unreal.WdpCameraSettingsAtom.rotation_yaw_speed_scale(value: float) -> None
unreal.WdpCameraSettingsAtom.view_distance_limit(value: Vector2D) -> None
unreal.WdpCameraSettingsAtom.zoom_speed_scale(value: float) -> None
```

## `unreal.WdpCameraUtilityLibrary(BlueprintFunctionLibrary)`

```python
unreal.WdpCameraUtilityLibrary.clear_on_screen_debug_messages() -> None
unreal.WdpCameraUtilityLibrary.color_to_hex(color: Color) -> str
unreal.WdpCameraUtilityLibrary.convert_vector_array_to_vector2d(array: Array[Vector]) -> Array[Vector2D]
unreal.WdpCameraUtilityLibrary.date_time_to_string(date_time: DateTime, format: str = "%Y-%m-%d %H:%M:%S") -> str
unreal.WdpCameraUtilityLibrary.distance_sort_map(map: Map[Vector, int], origin: Vector) -> Array[int]
unreal.WdpCameraUtilityLibrary.find_interp_value_from_date_time_key_map(data: Map[DateTime, float], input_time: DateTime, interp_mode: RichCurveInterpMode) -> Optional[float]
unreal.WdpCameraUtilityLibrary.find_interp_value_from_float_key_map(data: Map[float, float], input_time: float, interp_mode: RichCurveInterpMode) -> Optional[float]
unreal.WdpCameraUtilityLibrary.flush_inputs(player_controller: PlayerController) -> None
unreal.WdpCameraUtilityLibrary.get_hit_result_at_screen_position(player_controller: PlayerController, screen_position: Vector2D, trace_channel: TraceTypeQuery, trace_complex: bool) -> Optional[HitResult]
unreal.WdpCameraUtilityLibrary.hex_to_color(hex: str) -> Color
unreal.WdpCameraUtilityLibrary.sort_actors_by_distance(relative_to: Actor, array: Array[Actor]) -> Array[Actor]
unreal.WdpCameraUtilityLibrary.sort_actors_by_distance2d(relative_to: Actor, array: Array[Actor]) -> Array[Actor]
unreal.WdpCameraUtilityLibrary.sort_actors_by_location(relative_to: Vector, array: Array[Actor]) -> Array[Actor]
unreal.WdpCameraUtilityLibrary.sort_vectors_by_distance(relative_to: Vector, array: Array[Vector]) -> Array[Vector]
```

## `unreal.WdpCommonInput(ActorComponent)`

```python
unreal.WdpCommonInput.active_common_input(value: bool) -> None
unreal.WdpCommonInput.auto_bind_when_possessed(value: bool) -> None
unreal.WdpCommonInput.auto_unbind_when_un_possessed(value: bool) -> None
unreal.WdpCommonInput.bind_common_input_event(wdp_controller: WdpPlayerController) -> bool
unreal.WdpCommonInput.broadcast_when_not_possessed(value: bool) -> None
unreal.WdpCommonInput.clean_common_input_comp() -> None
unreal.WdpCommonInput.get_current_control_mode() -> ControlMode
unreal.WdpCommonInput.get_owning_wdp_player_controller() -> WdpPlayerController
unreal.WdpCommonInput.ia_on_any_key_rotate_value_updated(value: OnAnyKeyRotateValueUpdated) -> None
unreal.WdpCommonInput.ia_on_pointer_key_double_clicked(value: OnPointerKeyDoubleClicked) -> None
unreal.WdpCommonInput.ia_on_pointer_key_pressed(value: OnPointerKeyPressed) -> None
unreal.WdpCommonInput.ia_on_pointer_key_released(value: OnPointerKeyReleased) -> None
unreal.WdpCommonInput.ia_on_pointer_key_rotate_value_updated(value: OnPointerKeyRotateValueUpdated) -> None
unreal.WdpCommonInput.ia_on_pointer_key_triggered(value: OnPointerKeyTriggered) -> None
unreal.WdpCommonInput.ia_on_remote_move_key_updated(value: RemoteMoveKeyTriggered) -> None
unreal.WdpCommonInput.ia_on_rotate_key_pressed(value: OnRotateKeyPressed) -> None
unreal.WdpCommonInput.ia_on_rotate_key_released(value: OnRotateKeyReleased) -> None
unreal.WdpCommonInput.ia_on_rotate_key_triggered(value: OnRotateKeyTriggered) -> None
unreal.WdpCommonInput.ia_on_rotate_key_value_updated(value: OnRotateKeyValueUpdated) -> None
unreal.WdpCommonInput.ia_on_zoom_key_pressed(value: OnZoomKeyPressed) -> None
unreal.WdpCommonInput.ia_on_zoom_key_released(value: OnZoomKeyReleased) -> None
unreal.WdpCommonInput.ia_on_zoom_key_triggered(value: OnZoomKeyTriggered) -> None
unreal.WdpCommonInput.init_common_input_comp() -> None
unreal.WdpCommonInput.on_control_mode_changed(value: OnControlModeChanged) -> None
unreal.WdpCommonInput.should_broadcast_input_event() -> bool
unreal.WdpCommonInput.toggle_common_input_active(active: bool) -> None
unreal.WdpCommonInput.un_bind_common_input_event(wdp_controller: WdpPlayerController) -> bool
```

## `unreal.WdpCommonInput_OnAnyKeyRotateValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnAnyKeyRotateValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnControlModeChanged(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnControlModeChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnPointerKeyDoubleClicked(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnPointerKeyDoubleClicked.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnPointerKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnPointerKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnPointerKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnPointerKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnPointerKeyRotateValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnPointerKeyRotateValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnPointerKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnPointerKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnRotateKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnRotateKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnRotateKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnRotateKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnRotateKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnRotateKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnRotateKeyValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnRotateKeyValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnZoomKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnZoomKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnZoomKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnZoomKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_OnZoomKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_OnZoomKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpCommonInput_RemoteMoveKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpCommonInput_RemoteMoveKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController(PlayerController)`

```python
unreal.WdpPlayerController.auto_fix_capture_mode() -> None
unreal.WdpPlayerController.calc_rotate_value_by_screen_pos(current_pos: Vector2D, last_pos: Vector2D) -> Vector2D
unreal.WdpPlayerController.camera_touch_input_sensitivity(value: float) -> None
unreal.WdpPlayerController.control_mode(value: ControlMode) -> None
unreal.WdpPlayerController.cursor_style(value: MouseCursorStyle) -> None
unreal.WdpPlayerController.default_capture_mode(value: MouseCaptureMode) -> None
unreal.WdpPlayerController.get_default_touch_index() -> TouchIndex
unreal.WdpPlayerController.get_pointer_screen_position() -> Optional[Vector2D]
unreal.WdpPlayerController.get_pointer_screen_position_dpi() -> Optional[Vector2D]
unreal.WdpPlayerController.get_screen_center_position() -> Vector2D
unreal.WdpPlayerController.get_wdp_base_pawn() -> WdpBasePawn
unreal.WdpPlayerController.init_input_mapping() -> None
unreal.WdpPlayerController.init_input_mode() -> None
unreal.WdpPlayerController.init_world_origin_anchor() -> None
unreal.WdpPlayerController.is_pointer_key_down(value: bool) -> None
unreal.WdpPlayerController.is_possess_blending_camera(value: bool) -> None
unreal.WdpPlayerController.is_rotate_key_down(value: bool) -> None
unreal.WdpPlayerController.is_zoom_key_down(value: bool) -> None
unreal.WdpPlayerController.is_zoom_touch_down(value: bool) -> None
unreal.WdpPlayerController.on_any_key_rotate_value_updated(value: OnAnyKeyRotateValueUpdated) -> None
unreal.WdpPlayerController.on_control_mode_changed(value: InputChangedNotifyEvent) -> None
unreal.WdpPlayerController.on_move_key_triggered(value: OnMoveKeyTriggered) -> None
unreal.WdpPlayerController.on_pointer_key_double_clicked(value: OnPointerKeyDoubleClicked) -> None
unreal.WdpPlayerController.on_pointer_key_pressed(value: OnPointerKeyPressed) -> None
unreal.WdpPlayerController.on_pointer_key_released(value: OnPointerKeyReleased) -> None
unreal.WdpPlayerController.on_pointer_key_rotate_value_updated(value: OnPointerKeyRotateValueUpdated) -> None
unreal.WdpPlayerController.on_pointer_key_triggered(value: OnPointerKeyTriggered) -> None
unreal.WdpPlayerController.on_rotate_key_pressed(value: OnRotateKeyPressed) -> None
unreal.WdpPlayerController.on_rotate_key_released(value: OnRotateKeyReleased) -> None
unreal.WdpPlayerController.on_rotate_key_triggered(value: OnRotateKeyTriggered) -> None
unreal.WdpPlayerController.on_rotate_key_value_updated(value: OnRotateKeyValueUpdated) -> None
unreal.WdpPlayerController.on_zoom_key_pressed(value: OnZoomKeyPressed) -> None
unreal.WdpPlayerController.on_zoom_key_released(value: OnZoomKeyReleased) -> None
unreal.WdpPlayerController.on_zoom_key_triggered(value: OnZoomKeyTriggered) -> None
unreal.WdpPlayerController.pointer_action() -> InputAction
unreal.WdpPlayerController.pointer_key_screen_position(value: Vector2D) -> None
unreal.WdpPlayerController.possess_pawn_settings(value: PossessPawnSettings) -> None
unreal.WdpPlayerController.possess_to_new_pawn(new_pawn: Pawn, duration: float = 0.000000) -> None
unreal.WdpPlayerController.remote_move_key_triggered(value: Vector) -> None
unreal.WdpPlayerController.remote_rotate_key_pressed() -> None
unreal.WdpPlayerController.remote_rotate_key_released() -> None
unreal.WdpPlayerController.remote_rotate_key_value_update(value: Vector2D) -> None
unreal.WdpPlayerController.remote_zoom_key_pressed() -> None
unreal.WdpPlayerController.remote_zoom_key_released() -> None
unreal.WdpPlayerController.remote_zoom_value_update(value: float) -> None
unreal.WdpPlayerController.rotate_action() -> InputAction
unreal.WdpPlayerController.rotate_key_screen_position(value: Vector2D) -> None
unreal.WdpPlayerController.screen_mapping_context() -> InputMappingContext
unreal.WdpPlayerController.switch_control_mode(new_control_mode: ControlMode) -> None
unreal.WdpPlayerController.switch_control_mode_by_key(key: Key) -> ControlMode
unreal.WdpPlayerController.un_possess_and_return(duration: float = 0.000000) -> None
unreal.WdpPlayerController.update_possess_pawn_settings(settings: PossessPawnSettings) -> None
unreal.WdpPlayerController.wdp_base_pawn(value: WdpBasePawn) -> None
unreal.WdpPlayerController.world_origin_anchor() -> WorldOriginAnchor
unreal.WdpPlayerController.zoom_action() -> InputAction
unreal.WdpPlayerController.zoom_key_screen_position(value: Vector2D) -> None
```

## `unreal.WdpPlayerController_InputChangedNotifyEvent(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_InputChangedNotifyEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnAnyKeyRotateValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnAnyKeyRotateValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnMoveKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnMoveKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnPointerKeyDoubleClicked(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnPointerKeyDoubleClicked.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnPointerKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnPointerKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnPointerKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnPointerKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnPointerKeyRotateValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnPointerKeyRotateValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnPointerKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnPointerKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnRotateKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnRotateKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnRotateKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnRotateKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnRotateKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnRotateKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnRotateKeyValueUpdated(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnRotateKeyValueUpdated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnZoomKeyPressed(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnZoomKeyPressed.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnZoomKeyReleased(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnZoomKeyReleased.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WdpPlayerController_OnZoomKeyTriggered(MulticastDelegateBase)`

```python
unreal.WdpPlayerController_OnZoomKeyTriggered.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.XRMotionControllerData(StructBase)`

```python
unreal.XRMotionControllerData.__init__(valid: bool = False, device_name: Name = "None", application_instance_id: Guid = [], device_visual_type: XRVisualType = XRVisualType.CONTROLLER, hand_index: ControllerHand = ControllerHand.LEFT, tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED, grip_position: Vector = [0.000000, 0.000000, 0.000000], grip_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], aim_position: Vector = [0.000000, 0.000000, 0.000000], aim_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], palm_position: Vector = [0.000000, 0.000000, 0.000000], palm_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], hand_key_positions: Array[Vector] = [], hand_key_rotations: Array[Quat] = [], hand_key_radii: Array[float] = [], is_grasped: bool = False) -> None
unreal.XRMotionControllerData.aim_position() -> Vector
unreal.XRMotionControllerData.aim_rotation() -> Quat
unreal.XRMotionControllerData.application_instance_id() -> Guid
unreal.XRMotionControllerData.device_name() -> Name
unreal.XRMotionControllerData.device_visual_type() -> XRVisualType
unreal.XRMotionControllerData.grip_position() -> Vector
unreal.XRMotionControllerData.grip_rotation() -> Quat
unreal.XRMotionControllerData.hand_index() -> ControllerHand
unreal.XRMotionControllerData.hand_key_positions() -> Array[Vector]
unreal.XRMotionControllerData.hand_key_radii() -> Array[float]
unreal.XRMotionControllerData.hand_key_rotations() -> Array[Quat]
unreal.XRMotionControllerData.is_grasped() -> bool
unreal.XRMotionControllerData.palm_position() -> Vector
unreal.XRMotionControllerData.palm_rotation() -> Quat
unreal.XRMotionControllerData.tracking_status() -> TrackingStatus
unreal.XRMotionControllerData.valid() -> bool
```

## `unreal.XRMotionControllerState(StructBase)`

```python
unreal.XRMotionControllerState.__init__(valid: bool = False, device_name: Name = "None", application_instance_id: Guid = [], xr_space_type: XRSpaceType = XRSpaceType.UNREAL_WORLD_SPACE, hand: ControllerHand = ControllerHand.LEFT, tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED, xr_controller_pose_type: XRControllerPoseType = XRControllerPoseType.AIM, controller_location: Vector = [0.000000, 0.000000, 0.000000], controller_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.XRMotionControllerState.application_instance_id() -> Guid
unreal.XRMotionControllerState.controller_location() -> Vector
unreal.XRMotionControllerState.controller_rotation() -> Quat
unreal.XRMotionControllerState.device_name() -> Name
unreal.XRMotionControllerState.hand() -> ControllerHand
unreal.XRMotionControllerState.tracking_status() -> TrackingStatus
unreal.XRMotionControllerState.valid() -> bool
unreal.XRMotionControllerState.xr_controller_pose_type() -> XRControllerPoseType
unreal.XRMotionControllerState.xr_space_type() -> XRSpaceType
```

