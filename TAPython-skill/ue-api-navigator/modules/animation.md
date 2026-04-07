# Unreal Python API — Animation

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AbilityTask_PlayAnimAndWait(AbilityTask)`

```python
unreal.AbilityTask_PlayAnimAndWait.on_blend_in(value: PlayAnimWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayAnimAndWait.on_blend_out(value: PlayAnimWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayAnimAndWait.on_cancelled(value: PlayAnimWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayAnimAndWait.on_completed(value: PlayAnimWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayAnimAndWait.on_interrupted(value: PlayAnimWaitSimpleDelegate) -> None
```

## `unreal.AbilityTask_PlayMontageAndWait(AbilityTask)`

```python
unreal.AbilityTask_PlayMontageAndWait.on_blend_out(value: MontageWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayMontageAndWait.on_blended_in(value: MontageWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayMontageAndWait.on_cancelled(value: MontageWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayMontageAndWait.on_completed(value: MontageWaitSimpleDelegate) -> None
unreal.AbilityTask_PlayMontageAndWait.on_interrupted(value: MontageWaitSimpleDelegate) -> None
```

## `unreal.AnimBlueprint(Blueprint)`

```python
unreal.AnimBlueprint.add_node_asset_override(target: AnimationAsset, override: AnimationAsset, print_applied_overrides: bool = False) -> None
unreal.AnimBlueprint.get_animation_graphs() -> Array[AnimationGraph]
unreal.AnimBlueprint.get_nodes_of_class(node_class: Class, include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
```

## `unreal.AnimBlueprintFunctionPinInfo(StructBase)`

```python
unreal.AnimBlueprintFunctionPinInfo.__init__() -> None
```

## `unreal.AnimComponentSpacePoseContext(AnimExecutionContext)`

```python
unreal.AnimComponentSpacePoseContext.__init__() -> None
```

## `unreal.AnimCurveBase(StructBase)`

```python
unreal.AnimCurveBase.__init__() -> None
```

## `unreal.AnimDataController(Object)`

```python
unreal.AnimDataController.add_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.add_bone_curve(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimDataController.add_bone_track(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimDataController.add_curve(curve_id: AnimationCurveIdentifier, curve_flags: int = 4, should_transact: bool = True) -> bool
unreal.AnimDataController.close_bracket(should_transact: bool = True) -> None
unreal.AnimDataController.duplicate_attribute(attribute_identifier: AnimationAttributeIdentifier, new_attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.duplicate_curve(copy_curve_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.find_or_add_curve_names_on_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimDataController.get_model_interface() -> AnimationDataModel
unreal.AnimDataController.insert_bone_track(bone_name: Name, desired_index: int, should_transact: bool = True) -> int
unreal.AnimDataController.open_bracket(title: Text, should_transact: bool = True) -> None
unreal.AnimDataController.remove_all_attributes(should_transact: bool = True) -> int
unreal.AnimDataController.remove_all_attributes_for_bone(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimDataController.remove_all_bone_tracks(should_transact: bool = True) -> None
unreal.AnimDataController.remove_all_curves_of_type(supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimDataController.remove_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.remove_attribute_key(attribute_identifier: AnimationAttributeIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimDataController.remove_bone_track(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimDataController.remove_curve(curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.remove_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimDataController.remove_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimDataController.rename_curve(curve_to_rename_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimDataController.resize(length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimDataController.resize_in_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimDataController.resize_number_of_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimDataController.resize_play_length(new_length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimDataController.scale_curve(curve_id: AnimationCurveIdentifier, origin: float, factor: float, should_transact: bool = True) -> bool
unreal.AnimDataController.set_bone_track_keys(bone_name: Name, positional_keys: Array[Vector], rotational_keys: Array[Quat], scaling_keys: Array[Vector], should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_color(curve_id: AnimationCurveIdentifier, color: LinearColor, should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_comment(curve_id: AnimationCurveIdentifier, comment: str = "/**\n\t* Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.\n\t* Currently changing curve comments is only supported for float curves.\n\t*\n\t* @param\tCurveId\t\t\t\tIdentifier of the curve to change the comment for\n\t* @param\tComment\t\t\t\tComment to which the curve is to be set\n\t* @param\tbShouldTransact\t\tWhether or not any undo-redo changes should be generated\n\t*\n\t* @return\tWhether or not the curve comment was successfully changed\n\t*/", should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_flag(curve_id: AnimationCurveIdentifier, flag: AnimAssetCurveFlags, state: bool = True, should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_flags(curve_id: AnimationCurveIdentifier, flags: int, should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_key(curve_id: AnimationCurveIdentifier, key: RichCurveKey, should_transact: bool = True) -> bool
unreal.AnimDataController.set_curve_keys(curve_id: AnimationCurveIdentifier, curve_keys: Array[RichCurveKey], should_transact: bool = True) -> bool
unreal.AnimDataController.set_frame_rate(frame_rate: FrameRate, should_transact: bool = True) -> None
unreal.AnimDataController.set_model(model: AnimationDataModel) -> None
unreal.AnimDataController.set_number_of_frames(new_length_in_frames: FrameNumber, should_transact: bool = True) -> None
unreal.AnimDataController.set_play_length(length: float, should_transact: bool = True) -> None
unreal.AnimDataController.set_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, value: Transform, should_transact: bool = True) -> bool
unreal.AnimDataController.set_transform_curve_keys(curve_id: AnimationCurveIdentifier, transform_values: Array[Transform], time_keys: Array[float], should_transact: bool = True) -> bool
unreal.AnimDataController.update_curve_names_from_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
```

## `unreal.AnimDataModel(Object)`

```python
unreal.AnimDataModel.animated_bone_attributes() -> Array[AnimatedBoneAttribute]
unreal.AnimDataModel.bone_animation_tracks() -> Array[BoneAnimationTrack]
unreal.AnimDataModel.curve_data() -> AnimationCurveData
unreal.AnimDataModel.frame_rate() -> FrameRate
unreal.AnimDataModel.get_animation_sequence() -> AnimSequence
unreal.AnimDataModel.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
unreal.AnimDataModel.get_bone_track_by_index(track_index: int) -> BoneAnimationTrack
unreal.AnimDataModel.get_bone_track_by_name(track_name: Name) -> BoneAnimationTrack
unreal.AnimDataModel.get_bone_track_index(track: BoneAnimationTrack) -> int
unreal.AnimDataModel.get_bone_track_index_by_name(track_name: Name) -> int
unreal.AnimDataModel.get_bone_track_names() -> Array[Name]
unreal.AnimDataModel.get_frame_rate() -> FrameRate
unreal.AnimDataModel.get_num_bone_tracks() -> int
unreal.AnimDataModel.get_number_of_float_curves() -> int
unreal.AnimDataModel.get_number_of_frames() -> int
unreal.AnimDataModel.get_number_of_keys() -> int
unreal.AnimDataModel.get_number_of_transform_curves() -> int
unreal.AnimDataModel.get_play_length() -> float
unreal.AnimDataModel.is_valid_bone_track_index(track_index: int) -> bool
unreal.AnimDataModel.is_valid_bone_track_name(track_name: Name) -> bool
unreal.AnimDataModel.modified_event(value: AnimDataModelModifiedDynamicEvent) -> None
unreal.AnimDataModel.number_of_frames() -> int
unreal.AnimDataModel.number_of_keys() -> int
unreal.AnimDataModel.play_length() -> float
```

## `unreal.AnimDataModelModifiedDynamicEvent(MulticastDelegateBase)`

```python
unreal.AnimDataModelModifiedDynamicEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AnimDataModelNotifPayload(StructBase)`

```python
unreal.AnimDataModelNotifPayload.__init__() -> None
unreal.AnimDataModelNotifPayload.copy_payload(expected_struct: ScriptStruct, out_payload: EmptyPayload) -> EmptyPayload
unreal.AnimDataModelNotifPayload.get_payload() -> EmptyPayload
```

## `unreal.AnimDetailControlsProxyBool(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyBool.bool(value: AnimDetailProxyBool) -> None
```

## `unreal.AnimDetailControlsProxyEnum(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyEnum.enum(value: ControlRigEnumControlProxyValue) -> None
```

## `unreal.AnimDetailControlsProxyFloat(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyFloat.float(value: AnimDetailProxyFloat) -> None
```

## `unreal.AnimDetailControlsProxyInteger(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyInteger.integer(value: AnimDetailProxyInteger) -> None
```

## `unreal.AnimDetailControlsProxyLocation(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyLocation.location(value: AnimDetailProxyLocation) -> None
```

## `unreal.AnimDetailControlsProxyRotation(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyRotation.rotation(value: AnimDetailProxyRotation) -> None
```

## `unreal.AnimDetailControlsProxyScale(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyScale.scale(value: AnimDetailProxyScale) -> None
```

## `unreal.AnimDetailControlsProxyVector2D(AnimDetailControlsKeyedProxy)`

```python
unreal.AnimDetailControlsProxyVector2D.vector2d(value: AnimDetailProxyVector2D) -> None
```

## `unreal.AnimDetailProxyBool(StructBase)`

```python
unreal.AnimDetailProxyBool.__init__(bool: bool = False) -> None
unreal.AnimDetailProxyBool.bool(value: bool) -> None
```

## `unreal.AnimDetailProxyFloat(StructBase)`

```python
unreal.AnimDetailProxyFloat.__init__(float: float = 0.000000) -> None
unreal.AnimDetailProxyFloat.float(value: float) -> None
```

## `unreal.AnimDetailProxyInteger(StructBase)`

```python
unreal.AnimDetailProxyInteger.__init__(integer: int = 0) -> None
unreal.AnimDetailProxyInteger.integer(value: int) -> None
```

## `unreal.AnimDetailProxyLocation(StructBase)`

```python
unreal.AnimDetailProxyLocation.__init__(lx: float = 0.000000, ly: float = 0.000000, lz: float = 0.000000) -> None
unreal.AnimDetailProxyLocation.lx(value: float) -> None
unreal.AnimDetailProxyLocation.ly(value: float) -> None
unreal.AnimDetailProxyLocation.lz(value: float) -> None
```

## `unreal.AnimDetailProxyRotation(StructBase)`

```python
unreal.AnimDetailProxyRotation.__init__(rx: float = 0.000000, ry: float = 0.000000, rz: float = 0.000000) -> None
unreal.AnimDetailProxyRotation.rx(value: float) -> None
unreal.AnimDetailProxyRotation.ry(value: float) -> None
unreal.AnimDetailProxyRotation.rz(value: float) -> None
```

## `unreal.AnimDetailProxyScale(StructBase)`

```python
unreal.AnimDetailProxyScale.__init__(sx: float = 0.000000, sy: float = 0.000000, sz: float = 0.000000) -> None
unreal.AnimDetailProxyScale.sx(value: float) -> None
unreal.AnimDetailProxyScale.sy(value: float) -> None
unreal.AnimDetailProxyScale.sz(value: float) -> None
```

## `unreal.AnimDetailProxyVector2D(StructBase)`

```python
unreal.AnimDetailProxyVector2D.__init__(x: float = 0.000000, y: float = 0.000000) -> None
unreal.AnimDetailProxyVector2D.x(value: float) -> None
unreal.AnimDetailProxyVector2D.y(value: float) -> None
```

## `unreal.AnimDetailProxyVector3(StructBase)`

```python
unreal.AnimDetailProxyVector3.__init__(x: float = 0.000000, y: float = 0.000000, z: float = 0.000000) -> None
unreal.AnimDetailProxyVector3.x(value: float) -> None
unreal.AnimDetailProxyVector3.y(value: float) -> None
unreal.AnimDetailProxyVector3.z(value: float) -> None
```

## `unreal.AnimExecutionContext(StructBase)`

```python
unreal.AnimExecutionContext.__init__() -> None
```

## `unreal.AnimExecutionContextLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimExecutionContextLibrary.convert_to_component_space_pose_context(context: AnimExecutionContext) -> Tuple[AnimComponentSpacePoseContext, AnimExecutionContextConversionResult]
unreal.AnimExecutionContextLibrary.convert_to_initialization_context(context: AnimExecutionContext) -> Tuple[AnimInitializationContext, AnimExecutionContextConversionResult]
unreal.AnimExecutionContextLibrary.convert_to_pose_context(context: AnimExecutionContext) -> Tuple[AnimPoseContext, AnimExecutionContextConversionResult]
unreal.AnimExecutionContextLibrary.convert_to_update_context(context: AnimExecutionContext) -> Tuple[AnimUpdateContext, AnimExecutionContextConversionResult]
unreal.AnimExecutionContextLibrary.get_anim_instance(context: AnimExecutionContext) -> AnimInstance
unreal.AnimExecutionContextLibrary.get_current_weight(context: AnimUpdateContext) -> float
unreal.AnimExecutionContextLibrary.get_delta_time(context: AnimUpdateContext) -> float
unreal.AnimExecutionContextLibrary.is_active(context: AnimExecutionContext) -> bool
```

## `unreal.AnimGraphBlendOptions(StructBase)`

```python
unreal.AnimGraphBlendOptions.__init__() -> None
```

## `unreal.AnimGraphLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimGraphLibrary.calculate_direction(velocity: Vector, base_rotation: Rotator) -> float
unreal.AnimGraphLibrary.calculate_velocity_from_position_history(delta_seconds: float, position: Vector, history: PositionHistory, number_of_samples: int = 16, velocity_min: float = 0.000000, velocity_max: float = 128.000000) -> Tuple[float, PositionHistory]
unreal.AnimGraphLibrary.calculate_velocity_from_sockets(delta_seconds: float, component: SkeletalMeshComponent, socket_or_bone_name: Name, reference_socket_or_bone: Name, socket_space: RelativeTransformSpace, offset_in_bone_space: Vector, history: PositionHistory, number_of_samples: int = 16, velocity_min: float = 0.000000, velocity_max: float = 128.000000, easing_type: EasingFuncType = ..., custom_curve: RuntimeFloatCurve = ...) -> Tuple[float, PositionHistory]
unreal.AnimGraphLibrary.direction_between_sockets(component: SkeletalMeshComponent, socket_or_bone_name_from: Name, socket_or_bone_name_to: Name) -> Vector
unreal.AnimGraphLibrary.distance_between_sockets(component: SkeletalMeshComponent, socket_or_bone_name_a: Name, socket_space_a: RelativeTransformSpace, socket_or_bone_name_b: Name, socket_space_b: RelativeTransformSpace, remap_range: bool = False, range_min: float = ..., range_max: float = ..., out_range_min: float = ..., out_range_max: float = ...) -> float
unreal.AnimGraphLibrary.k2_end_profiling_timer(log: bool = True, log_prefix: str = "") -> float
unreal.AnimGraphLibrary.k2_start_profiling_timer() -> None
unreal.AnimGraphLibrary.look_at(current_transform: Transform, target_position: Vector, look_at_vector: Vector, use_up_vector: bool = False, up_vector: Vector = ..., clamp_cone_in_degree: float = ...) -> Transform
unreal.AnimGraphLibrary.make_float_from_perlin_noise(value: float, range_out_min: float, range_out_max: float) -> float
unreal.AnimGraphLibrary.make_vector_from_perlin_noise(x: float, y: float, z: float, range_out_min_x: float = -1.000000, range_out_max_x: float = 1.000000, range_out_min_y: float = -1.000000, range_out_max_y: float = 1.000000, range_out_min_z: float = -1.000000, range_out_max_z: float = 1.000000) -> Vector
unreal.AnimGraphLibrary.two_bone_ik(root_pos: Vector, joint_pos: Vector, end_pos: Vector, joint_target: Vector, effector: Vector, allow_stretching: bool = False, start_stretch_ratio: float = 1.000000, max_stretch_scale: float = 1.200000) -> Tuple[Vector, Vector]
```

## `unreal.AnimGraphNodeCustomizationInterface(Interface)`

```python
unreal.AnimGraphNodeCustomizationInterface.get_title_color() -> LinearColor
```

## `unreal.AnimGraphNode_PoseDriver(AnimGraphNode_PoseHandler)`

```python
unreal.AnimGraphNode_PoseDriver.copy_targets_from_pose_asset() -> None
unreal.AnimGraphNode_PoseDriver.get_driving_bone_names() -> Array[Name]
unreal.AnimGraphNode_PoseDriver.get_pose_driver_output() -> PoseDriverOutput
unreal.AnimGraphNode_PoseDriver.get_pose_driver_source() -> PoseDriverSource
unreal.AnimGraphNode_PoseDriver.get_rbf_parameters() -> RBFParams
unreal.AnimGraphNode_PoseDriver.get_source_bone_names() -> Array[Name]
unreal.AnimGraphNode_PoseDriver.node(value: AnimNode_PoseDriver) -> None
unreal.AnimGraphNode_PoseDriver.set_driving_bones(bone_names: Array[Name]) -> None
unreal.AnimGraphNode_PoseDriver.set_pose_driver_output(driver_output: PoseDriverOutput) -> None
unreal.AnimGraphNode_PoseDriver.set_pose_driver_source(driver_source: PoseDriverSource) -> None
unreal.AnimGraphNode_PoseDriver.set_rbf_parameters(parameters: RBFParams) -> None
unreal.AnimGraphNode_PoseDriver.set_source_bones(bone_names: Array[Name]) -> None
```

## `unreal.AnimGraphNode_TransitionPoseEvaluator(AnimGraphNode_Base)`

```python
unreal.AnimGraphNode_TransitionPoseEvaluator.node(value: AnimNode_TransitionPoseEvaluator) -> None
```

## `unreal.AnimInitializationContext(AnimExecutionContext)`

```python
unreal.AnimInitializationContext.__init__() -> None
```

## `unreal.AnimInstance(Object)`

```python
unreal.AnimInstance.blueprint_begin_play() -> None
unreal.AnimInstance.blueprint_get_main_anim_instance() -> AnimInstance
unreal.AnimInstance.blueprint_get_slot_montage_local_weight(slot_node_name: Name) -> float
unreal.AnimInstance.blueprint_initialize_animation() -> None
unreal.AnimInstance.blueprint_linked_animation_layers_initialized() -> None
unreal.AnimInstance.blueprint_post_evaluate_animation() -> None
unreal.AnimInstance.blueprint_thread_safe_update_animation(delta_time: float) -> None
unreal.AnimInstance.blueprint_update_animation(delta_time_x: float) -> None
unreal.AnimInstance.calculate_direction(velocity: Vector, base_rotation: Rotator) -> float
unreal.AnimInstance.clear_all_transition_events() -> None
unreal.AnimInstance.clear_layer_overlay(class_: Class) -> None
unreal.AnimInstance.clear_morph_targets() -> None
unreal.AnimInstance.clear_transition_events(event_name: Name) -> None
unreal.AnimInstance.dynamic_montage_is_playing_from(animation: AnimSequenceBase) -> bool
unreal.AnimInstance.get_active_curve_names(curve_type: AnimCurveType) -> Array[Name]
unreal.AnimInstance.get_all_curve_names() -> Array[Name]
unreal.AnimInstance.get_blend_profile_by_name(blend_profile_name: Name) -> BlendProfile
unreal.AnimInstance.get_current_active_montage() -> AnimMontage
unreal.AnimInstance.get_curve_value(curve_name: Name) -> float
unreal.AnimInstance.get_curve_value_with_default(curve_name: Name, default_value: float) -> Optional[float]
unreal.AnimInstance.get_delta_seconds() -> float
unreal.AnimInstance.get_layer_sub_instance_by_class(class_: Class, check_for_child_class: bool = False) -> AnimInstance
unreal.AnimInstance.get_layer_sub_instance_by_group(group: Name) -> AnimInstance
unreal.AnimInstance.get_linked_anim_graph_instance_by_tag(tag: Name) -> AnimInstance
unreal.AnimInstance.get_linked_anim_graph_instances_by_tag(tag: Name) -> Array[AnimInstance]
unreal.AnimInstance.get_linked_anim_layer_instance_by_class(class_: Class, check_for_child_class: bool = False) -> AnimInstance
unreal.AnimInstance.get_linked_anim_layer_instance_by_group(group: Name) -> AnimInstance
unreal.AnimInstance.get_linked_anim_layer_instance_by_group_and_class(group: Name, class_: Class) -> AnimInstance
unreal.AnimInstance.get_linked_anim_layer_instances_by_group(group: Name) -> Array[AnimInstance]
unreal.AnimInstance.get_owning_actor() -> Actor
unreal.AnimInstance.get_owning_component() -> SkeletalMeshComponent
unreal.AnimInstance.get_propagate_notifies_to_linked_instances() -> bool
unreal.AnimInstance.get_receive_notifies_from_linked_instances() -> bool
unreal.AnimInstance.get_sub_instance_by_tag(tag: Name) -> AnimInstance
unreal.AnimInstance.get_sub_instances_by_tag(tag: Name) -> Array[AnimInstance]
unreal.AnimInstance.get_sync_group_position(sync_group_name: Name) -> MarkerSyncAnimPosition
unreal.AnimInstance.get_time_to_closest_marker(sync_group: Name, marker_name: Name) -> Optional[float]
unreal.AnimInstance.has_marker_been_hit_this_frame(sync_group: Name, marker_name: Name) -> bool
unreal.AnimInstance.is_any_montage_playing() -> bool
unreal.AnimInstance.is_playing_slot_animation(asset: AnimSequenceBase, slot_node_name: Name) -> bool
unreal.AnimInstance.is_slot_active(slot_node_name: Name) -> bool
unreal.AnimInstance.is_sync_group_between_markers(sync_group_name: Name, previous_marker: Name, next_marker: Name, respect_marker_order: bool = True) -> bool
unreal.AnimInstance.is_using_main_instance_montage_evaluation_data() -> bool
unreal.AnimInstance.kismet_initialize_animation() -> None
unreal.AnimInstance.kismet_update_animation(delta_time_x: float) -> None
unreal.AnimInstance.link_anim_class_layers(class_: Class) -> None
unreal.AnimInstance.link_anim_graph_by_tag(tag: Name, class_: Class) -> None
unreal.AnimInstance.lock_ai_resources(lock_movement: bool, lock_ai_logic: bool) -> None
unreal.AnimInstance.montage_get_blend_time(montage: AnimMontage) -> float
unreal.AnimInstance.montage_get_current_section(montage: AnimMontage = None) -> Name
unreal.AnimInstance.montage_get_effective_play_rate(montage: AnimMontage) -> float
unreal.AnimInstance.montage_get_is_stopped(montage: AnimMontage) -> bool
unreal.AnimInstance.montage_get_play_rate(montage: AnimMontage) -> float
unreal.AnimInstance.montage_get_position(montage: AnimMontage) -> float
unreal.AnimInstance.montage_is_active(montage: AnimMontage) -> bool
unreal.AnimInstance.montage_is_playing(montage: AnimMontage) -> bool
unreal.AnimInstance.montage_jump_to_section(section_name: Name, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_jump_to_sections_end(section_name: Name, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_pause(montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_play(montage_to_play: AnimMontage, play_rate: float = 1.000000, return_value_type: MontagePlayReturnType = MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at: float = 0.000000, stop_all_montages: bool = True) -> float
unreal.AnimInstance.montage_play_with_blend_in(montage_to_play: AnimMontage, blend_in: AlphaBlendArgs, play_rate: float = 1.000000, return_value_type: MontagePlayReturnType = MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at: float = 0.000000, stop_all_montages: bool = True) -> float
unreal.AnimInstance.montage_play_with_blend_settings(montage_to_play: AnimMontage, blend_in_settings: MontageBlendSettings, play_rate: float = 1.000000, return_value_type: MontagePlayReturnType = MontagePlayReturnType.MONTAGE_LENGTH, time_to_start_montage_at: float = 0.000000, stop_all_montages: bool = True) -> float
unreal.AnimInstance.montage_resume(montage: AnimMontage) -> None
unreal.AnimInstance.montage_set_next_section(section_name_to_change: Name, next_section: Name, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_set_play_rate(montage: AnimMontage, new_play_rate: float = 1.000000) -> None
unreal.AnimInstance.montage_set_position(montage: AnimMontage, new_position: float) -> None
unreal.AnimInstance.montage_stop(blend_out_time: float, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_stop_group_by_name(blend_out_time: float, group_name: Name) -> None
unreal.AnimInstance.montage_stop_with_blend_out(blend_out: AlphaBlendArgs, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_stop_with_blend_settings(blend_out_settings: MontageBlendSettings, montage: AnimMontage = None) -> None
unreal.AnimInstance.montage_sync_follow(montage_follower: AnimMontage, other_anim_instance: AnimInstance, montage_leader: AnimMontage) -> None
unreal.AnimInstance.montage_sync_stop_following(montage_follower: AnimMontage) -> None
unreal.AnimInstance.on_all_montage_instances_ended(value: OnAllMontageInstancesEndedMCDelegate) -> None
unreal.AnimInstance.on_montage_blended_in(value: OnMontageBlendedInEndedMCDelegate) -> None
unreal.AnimInstance.on_montage_blending_out(value: OnMontageBlendingOutStartedMCDelegate) -> None
unreal.AnimInstance.on_montage_ended(value: OnMontageEndedMCDelegate) -> None
unreal.AnimInstance.on_montage_started(value: OnMontageStartedMCDelegate) -> None
unreal.AnimInstance.play_slot_animation_as_dynamic_montage(asset: AnimSequenceBase, slot_node_name: Name, blend_in_time: float = 0.250000, blend_out_time: float = 0.250000, play_rate: float = 1.000000, loop_count: int = 1, blend_out_trigger_time: float = -1.000000, time_to_start_montage_at: float = 0.000000) -> AnimMontage
unreal.AnimInstance.play_slot_animation_as_dynamic_montage_with_blend_args(asset: AnimSequenceBase, slot_node_name: Name, blend_in: AlphaBlendArgs, blend_out: AlphaBlendArgs, play_rate: float = 1.000000, loop_count: int = 1, blend_out_trigger_time: float = -1.000000, time_to_start_montage_at: float = 0.000000) -> AnimMontage
unreal.AnimInstance.play_slot_animation_as_dynamic_montage_with_blend_settings(asset: AnimSequenceBase, slot_node_name: Name, blend_in_settings: MontageBlendSettings, blend_out_settings: MontageBlendSettings, play_rate: float = 1.000000, loop_count: int = 1, blend_out_trigger_time: float = -1.000000, time_to_start_montage_at: float = 0.000000) -> AnimMontage
unreal.AnimInstance.remove_pose_snapshot(snapshot_name: Name) -> None
unreal.AnimInstance.request_slot_group_inertialization(slot_group_name: Name, duration: float, blend_profile: BlendProfile = None) -> None
unreal.AnimInstance.request_transition_event(event_name: Name, request_timeout: float, queue_mode: TransitionRequestQueueMode, overwrite_mode: TransitionRequestOverwriteMode) -> bool
unreal.AnimInstance.reset_dynamics(teleport_type: TeleportType) -> None
unreal.AnimInstance.save_pose_snapshot(snapshot_name: Name) -> None
unreal.AnimInstance.set_layer_overlay(class_: Class) -> None
unreal.AnimInstance.set_morph_target(morph_target_name: Name, value: float) -> None
unreal.AnimInstance.set_propagate_notifies_to_linked_instances(set: bool) -> None
unreal.AnimInstance.set_receive_notifies_from_linked_instances(set: bool) -> None
unreal.AnimInstance.set_root_motion_mode(value: RootMotionMode) -> None
unreal.AnimInstance.set_sub_instance_class_by_tag(tag: Name, class_: Class) -> None
unreal.AnimInstance.set_use_main_instance_montage_evaluation_data(set: bool) -> None
unreal.AnimInstance.snapshot_pose(snapshot: PoseSnapshot) -> PoseSnapshot
unreal.AnimInstance.stop_slot_animation(blend_out_time: float = 0.250000, slot_node_name: Name = "None") -> None
unreal.AnimInstance.try_get_pawn_owner() -> Pawn
unreal.AnimInstance.unlink_anim_class_layers(class_: Class) -> None
unreal.AnimInstance.unlock_ai_resources(unlock_movement: bool, unlock_ai_logic: bool) -> None
unreal.AnimInstance.was_anim_notify_state_active_in_any_state(anim_notify_state_type: Class) -> bool
```

## `unreal.AnimLayer(Object)`

```python
unreal.AnimLayer.add_selected_in_sequencer() -> bool
unreal.AnimLayer.get_active() -> bool
unreal.AnimLayer.get_keyed() -> CheckBoxState
unreal.AnimLayer.get_lock() -> bool
unreal.AnimLayer.get_name() -> Text
unreal.AnimLayer.get_selected() -> CheckBoxState
unreal.AnimLayer.get_type() -> AnimLayerType
unreal.AnimLayer.get_weight() -> float
unreal.AnimLayer.remove_selected_in_sequencer() -> bool
unreal.AnimLayer.set_active(active: bool) -> None
unreal.AnimLayer.set_keyed() -> None
unreal.AnimLayer.set_lock(lock: bool) -> None
unreal.AnimLayer.set_name(name: Text) -> None
unreal.AnimLayer.set_selected(selected: bool, clear_selection: bool) -> None
unreal.AnimLayer.set_type(layer_type: AnimLayerType) -> None
unreal.AnimLayer.set_weight(weight: float) -> None
```

## `unreal.AnimLayerControlRigObject(StructBase)`

```python
unreal.AnimLayerControlRigObject.__init__(control_rig: ControlRig = None, control_names: Array[Name] = []) -> None
unreal.AnimLayerControlRigObject.control_names(value: Array[Name]) -> None
unreal.AnimLayerControlRigObject.control_rig(value: ControlRig) -> None
```

## `unreal.AnimLayerItem(StructBase)`

```python
unreal.AnimLayerItem.__init__(section_items: Array[AnimLayerSectionItem] = []) -> None
unreal.AnimLayerItem.section_items(value: Array[AnimLayerSectionItem]) -> None
```

## `unreal.AnimLayerObjects(StructBase)`

```python
unreal.AnimLayerObjects.__init__(control_rig_objects: Array[AnimLayerControlRigObject] = [], scene_objects: Array[AnimLayerSceneObject] = []) -> None
unreal.AnimLayerObjects.control_rig_objects(value: Array[AnimLayerControlRigObject]) -> None
unreal.AnimLayerObjects.scene_objects(value: Array[AnimLayerSceneObject]) -> None
```

## `unreal.AnimLayerPropertyAndChannels(StructBase)`

```python
unreal.AnimLayerPropertyAndChannels.__init__(name: Name = "None") -> None
unreal.AnimLayerPropertyAndChannels.name(value: Name) -> None
```

## `unreal.AnimLayerSceneObject(StructBase)`

```python
unreal.AnimLayerSceneObject.__init__(scene_object_or_component: Object = None) -> None
unreal.AnimLayerSceneObject.scene_object_or_component(value: Object) -> None
```

## `unreal.AnimLayerSectionItem(StructBase)`

```python
unreal.AnimLayerSectionItem.__init__(anim_layer_set: AnimLayerSelectionSet = [None, {}], section: MovieSceneSection = None) -> None
unreal.AnimLayerSectionItem.anim_layer_set(value: AnimLayerSelectionSet) -> None
unreal.AnimLayerSectionItem.section(value: MovieSceneSection) -> None
```

## `unreal.AnimLayerSelectionSet(StructBase)`

```python
unreal.AnimLayerSelectionSet.__init__(bound_object: Object = None, names: Map[Name, AnimLayerPropertyAndChannels] = {}) -> None
unreal.AnimLayerSelectionSet.bound_object(value: Object) -> None
unreal.AnimLayerSelectionSet.names(value: Map[Name, AnimLayerPropertyAndChannels]) -> None
```

## `unreal.AnimLayerState(StructBase)`

```python
unreal.AnimLayerState.__init__(keyed: CheckBoxState = CheckBoxState.UNCHECKED, selected: CheckBoxState = CheckBoxState.UNCHECKED, active: bool = False, lock: bool = False, name: Text = "", weight: float = 0.000000, type: int = 0) -> None
unreal.AnimLayerState.active(value: bool) -> None
unreal.AnimLayerState.keyed(value: CheckBoxState) -> None
unreal.AnimLayerState.lock(value: bool) -> None
unreal.AnimLayerState.name(value: Text) -> None
unreal.AnimLayerState.selected(value: CheckBoxState) -> None
unreal.AnimLayerState.type(value: int) -> None
unreal.AnimLayerState.weight(value: float) -> None
```

## `unreal.AnimLayerWeightProxy(Object)`

```python
unreal.AnimLayerWeightProxy.weight(value: float) -> None
```

## `unreal.AnimLayers(AssetUserData)`

```python
unreal.AnimLayers.anim_layers(value: Array[AnimLayer]) -> None
```

## `unreal.AnimLegIKDefinition(StructBase)`

```python
unreal.AnimLegIKDefinition.__init__() -> None
```

## `unreal.AnimLinkableElement(StructBase)`

```python
unreal.AnimLinkableElement.__init__() -> None
```

## `unreal.AnimMontage(AnimCompositeBase)`

```python
unreal.AnimMontage.blend_mode_in() -> MontageBlendMode
unreal.AnimMontage.blend_mode_out() -> MontageBlendMode
unreal.AnimMontage.blend_profile_in() -> BlendProfile
unreal.AnimMontage.blend_profile_out() -> BlendProfile
unreal.AnimMontage.create_slot_animation_as_dynamic_montage_with_blend_settings(asset: AnimSequenceBase, slot_node_name: Name, blend_in_settings: MontageBlendSettings, blend_out_settings: MontageBlendSettings, play_rate: float = 1.000000, loop_count: int = 1, blend_out_trigger_time: float = -1.000000) -> AnimMontage
unreal.AnimMontage.get_blend_in_args() -> AlphaBlendArgs
unreal.AnimMontage.get_blend_out_args() -> AlphaBlendArgs
unreal.AnimMontage.get_default_blend_in_time() -> float
unreal.AnimMontage.get_default_blend_out_time() -> float
unreal.AnimMontage.get_first_anim_reference() -> AnimSequenceBase
unreal.AnimMontage.get_group_name() -> Name
unreal.AnimMontage.get_num_sections() -> int
unreal.AnimMontage.get_section_index(section_name: Name) -> int
unreal.AnimMontage.get_section_name(section_index: int) -> Name
unreal.AnimMontage.is_dynamic_montage() -> bool
unreal.AnimMontage.is_valid_additive_slot(slot_node_name: Name) -> bool
unreal.AnimMontage.is_valid_section_name(section_name: Name) -> bool
```

## `unreal.AnimNodeConstantData(StructBase)`

```python
unreal.AnimNodeConstantData.__init__() -> None
```

## `unreal.AnimNodeControlRigLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimNodeControlRigLibrary.convert_to_control_rig(node: AnimNodeReference) -> Tuple[ControlRigReference, AnimNodeReferenceConversionResult]
unreal.AnimNodeControlRigLibrary.convert_to_control_rig_pure(node: AnimNodeReference) -> Tuple[ControlRigReference, bool]
unreal.AnimNodeControlRigLibrary.set_control_rig_class(node: ControlRigReference, control_rig_class: Class) -> ControlRigReference
```

## `unreal.AnimNodeData(StructBase)`

```python
unreal.AnimNodeData.__init__() -> None
```

## `unreal.AnimNodeReference(StructBase)`

```python
unreal.AnimNodeReference.__init__() -> None
```

## `unreal.AnimNodeRigidBodyLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimNodeRigidBodyLibrary.convert_to_rigid_body_anim_node(node: AnimNodeReference) -> Tuple[RigidBodyAnimNodeReference, AnimNodeReferenceConversionResult]
unreal.AnimNodeRigidBodyLibrary.convert_to_rigid_body_anim_node_pure(node: AnimNodeReference) -> Tuple[RigidBodyAnimNodeReference, bool]
unreal.AnimNodeRigidBodyLibrary.set_override_physics_asset(node: RigidBodyAnimNodeReference, physics_asset: PhysicsAsset) -> RigidBodyAnimNodeReference
```

## `unreal.AnimNode_AimOffsetLookAt(AnimNode_BlendSpacePlayer)`

```python
unreal.AnimNode_AimOffsetLookAt.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, base_pose: PoseLink = [], lod_threshold: int = 0, source_socket_name: Name = "None", pivot_socket_name: Name = "None", look_at_location: Vector = [0.000000, 0.000000, 0.000000], socket_axis: Vector = [0.000000, 0.000000, 0.000000], alpha: float = 0.000000) -> None
unreal.AnimNode_AimOffsetLookAt.alpha(value: float) -> None
unreal.AnimNode_AimOffsetLookAt.base_pose(value: PoseLink) -> None
unreal.AnimNode_AimOffsetLookAt.lod_threshold(value: int) -> None
unreal.AnimNode_AimOffsetLookAt.look_at_location(value: Vector) -> None
unreal.AnimNode_AimOffsetLookAt.pivot_socket_name(value: Name) -> None
unreal.AnimNode_AimOffsetLookAt.socket_axis(value: Vector) -> None
unreal.AnimNode_AimOffsetLookAt.source_socket_name(value: Name) -> None
```

## `unreal.AnimNode_AnimDynamics(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_AnimDynamics.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], linear_damping_override: float = 0.000000, angular_damping_override: float = 0.000000, gravity_scale: float = 0.000000, gravity_override: Vector = [0.000000, 0.000000, 0.000000], linear_spring_constant: float = 0.000000, angular_spring_constant: float = 0.000000, angular_bias_override: float = 0.000000, simulation_space: AnimPhysSimSpaceType = AnimPhysSimSpaceType.COMPONENT, use_gravity_override: bool = False) -> None
unreal.AnimNode_AnimDynamics.angular_bias_override(value: float) -> None
unreal.AnimNode_AnimDynamics.angular_damping_override(value: float) -> None
unreal.AnimNode_AnimDynamics.angular_spring_constant(value: float) -> None
unreal.AnimNode_AnimDynamics.gravity_override(value: Vector) -> None
unreal.AnimNode_AnimDynamics.gravity_scale(value: float) -> None
unreal.AnimNode_AnimDynamics.linear_damping_override(value: float) -> None
unreal.AnimNode_AnimDynamics.linear_spring_constant(value: float) -> None
unreal.AnimNode_AnimDynamics.simulation_space(value: AnimPhysSimSpaceType) -> None
unreal.AnimNode_AnimDynamics.use_gravity_override(value: bool) -> None
```

## `unreal.AnimNode_ApplyAdditive(AnimNode_Base)`

```python
unreal.AnimNode_ApplyAdditive.__init__(base: PoseLink = [], additive: PoseLink = [], alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], lod_threshold: int = 0, alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False) -> None
unreal.AnimNode_ApplyAdditive.additive(value: PoseLink) -> None
unreal.AnimNode_ApplyAdditive.alpha(value: float) -> None
unreal.AnimNode_ApplyAdditive.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_ApplyAdditive.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_ApplyAdditive.alpha_curve_name(value: Name) -> None
unreal.AnimNode_ApplyAdditive.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_ApplyAdditive.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_ApplyAdditive.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_ApplyAdditive.base(value: PoseLink) -> None
unreal.AnimNode_ApplyAdditive.lod_threshold(value: int) -> None
```

## `unreal.AnimNode_ApplyLimits(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_ApplyLimits.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], angular_offsets: Array[Vector] = []) -> None
unreal.AnimNode_ApplyLimits.angular_offsets(value: Array[Vector]) -> None
```

## `unreal.AnimNode_ApplyMeshSpaceAdditive(AnimNode_Base)`

```python
unreal.AnimNode_ApplyMeshSpaceAdditive.__init__(base: PoseLink = [], additive: PoseLink = [], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha: float = 0.000000, alpha_bool_enabled: bool = False, alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], lod_threshold: int = 0) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.additive(value: PoseLink) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha(value: float) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_curve_name(value: Name) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.base(value: PoseLink) -> None
unreal.AnimNode_ApplyMeshSpaceAdditive.lod_threshold(value: int) -> None
```

## `unreal.AnimNode_AssetPlayerBase(AnimNode_AssetPlayerRelevancyBase)`

```python
unreal.AnimNode_AssetPlayerBase.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
unreal.AnimNode_AssetPlayerBase.blend_weight(value: float) -> None
unreal.AnimNode_AssetPlayerBase.internal_time_accumulator(value: float) -> None
```

## `unreal.AnimNode_AssetPlayerRelevancyBase(AnimNode_Base)`

```python
unreal.AnimNode_AssetPlayerRelevancyBase.__init__() -> None
```

## `unreal.AnimNode_Base(StructBase)`

```python
unreal.AnimNode_Base.__init__() -> None
```

## `unreal.AnimNode_BlendBoneByChannel(AnimNode_Base)`

```python
unreal.AnimNode_BlendBoneByChannel.__init__(a: PoseLink = [], b: PoseLink = [], alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000]) -> None
unreal.AnimNode_BlendBoneByChannel.a(value: PoseLink) -> None
unreal.AnimNode_BlendBoneByChannel.alpha(value: float) -> None
unreal.AnimNode_BlendBoneByChannel.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_BlendBoneByChannel.b(value: PoseLink) -> None
```

## `unreal.AnimNode_BlendListBase(AnimNode_Base)`

```python
unreal.AnimNode_BlendListBase.__init__() -> None
```

## `unreal.AnimNode_BlendListByBool(AnimNode_BlendListBase)`

```python
unreal.AnimNode_BlendListByBool.__init__() -> None
```

## `unreal.AnimNode_BlendListByEnum(AnimNode_BlendListBase)`

```python
unreal.AnimNode_BlendListByEnum.__init__() -> None
```

## `unreal.AnimNode_BlendListByInt(AnimNode_BlendListBase)`

```python
unreal.AnimNode_BlendListByInt.__init__() -> None
```

## `unreal.AnimNode_BlendSpace(AnimNode_BlendSpacePlayer)`

```python
unreal.AnimNode_BlendSpace.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_BlendSpaceEvaluator(AnimNode_BlendSpacePlayer)`

```python
unreal.AnimNode_BlendSpaceEvaluator.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, normalized_time: float = 0.000000) -> None
unreal.AnimNode_BlendSpaceEvaluator.normalized_time(value: float) -> None
```

## `unreal.AnimNode_BlendSpaceGraph(AnimNode_BlendSpaceGraphBase)`

```python
unreal.AnimNode_BlendSpaceGraph.__init__(x: float = 0.000000, y: float = 0.000000, group_name: Name = "None", group_role: AnimGroupRole = AnimGroupRole.CAN_BE_LEADER) -> None
```

## `unreal.AnimNode_BlendSpaceGraphBase(AnimNode_Base)`

```python
unreal.AnimNode_BlendSpaceGraphBase.__init__(x: float = 0.000000, y: float = 0.000000, group_name: Name = "None", group_role: AnimGroupRole = AnimGroupRole.CAN_BE_LEADER) -> None
unreal.AnimNode_BlendSpaceGraphBase.group_name(value: Name) -> None
unreal.AnimNode_BlendSpaceGraphBase.group_role(value: AnimGroupRole) -> None
unreal.AnimNode_BlendSpaceGraphBase.x(value: float) -> None
unreal.AnimNode_BlendSpaceGraphBase.y(value: float) -> None
```

## `unreal.AnimNode_BlendSpacePlayer(AnimNode_BlendSpacePlayerBase)`

```python
unreal.AnimNode_BlendSpacePlayer.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_BlendSpacePlayerBase(AnimNode_AssetPlayerBase)`

```python
unreal.AnimNode_BlendSpacePlayerBase.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_BlendSpacePlayer_Standalone(AnimNode_BlendSpacePlayerBase)`

```python
unreal.AnimNode_BlendSpacePlayer_Standalone.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_BlendSpaceSampleResult(AnimNode_Root)`

```python
unreal.AnimNode_BlendSpaceSampleResult.__init__(result: PoseLink = []) -> None
```

## `unreal.AnimNode_BoneDrivenController(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_BoneDrivenController.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_CCDIK(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_CCDIK.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_CallFunction(AnimNode_Base)`

```python
unreal.AnimNode_CallFunction.__init__() -> None
```

## `unreal.AnimNode_Constraint(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_Constraint.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_ControlRig(AnimNode_ControlRigBase)`

```python
unreal.AnimNode_ControlRig.__init__() -> None
```

## `unreal.AnimNode_ControlRigBase(AnimNode_CustomProperty)`

```python
unreal.AnimNode_ControlRigBase.__init__() -> None
```

## `unreal.AnimNode_ConvertComponentToLocalSpace(AnimNode_Base)`

```python
unreal.AnimNode_ConvertComponentToLocalSpace.__init__(component_pose: ComponentSpacePoseLink = []) -> None
unreal.AnimNode_ConvertComponentToLocalSpace.component_pose(value: ComponentSpacePoseLink) -> None
```

## `unreal.AnimNode_ConvertLocalToComponentSpace(AnimNode_Base)`

```python
unreal.AnimNode_ConvertLocalToComponentSpace.__init__(local_pose: PoseLink = []) -> None
unreal.AnimNode_ConvertLocalToComponentSpace.local_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_CopyBone(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_CopyBone.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], copy_translation: bool = False, copy_rotation: bool = False, copy_scale: bool = False) -> None
unreal.AnimNode_CopyBone.copy_rotation(value: bool) -> None
unreal.AnimNode_CopyBone.copy_scale(value: bool) -> None
unreal.AnimNode_CopyBone.copy_translation(value: bool) -> None
```

## `unreal.AnimNode_CopyBoneDelta(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_CopyBoneDelta.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], copy_translation: bool = False, copy_rotation: bool = False, copy_scale: bool = False, translation_multiplier: float = 0.000000, rotation_multiplier: float = 0.000000, scale_multiplier: float = 0.000000) -> None
unreal.AnimNode_CopyBoneDelta.copy_rotation(value: bool) -> None
unreal.AnimNode_CopyBoneDelta.copy_scale(value: bool) -> None
unreal.AnimNode_CopyBoneDelta.copy_translation(value: bool) -> None
unreal.AnimNode_CopyBoneDelta.rotation_multiplier(value: float) -> None
unreal.AnimNode_CopyBoneDelta.scale_multiplier(value: float) -> None
unreal.AnimNode_CopyBoneDelta.translation_multiplier(value: float) -> None
```

## `unreal.AnimNode_CopyPoseFromMesh(AnimNode_Base)`

```python
unreal.AnimNode_CopyPoseFromMesh.__init__(source_mesh_component: SkeletalMeshComponent = None, use_attached_parent: bool = False, copy_curves: bool = False, copy_custom_attributes: bool = False, use_mesh_pose: bool = False, root_bone_to_copy: Name = "None") -> None
unreal.AnimNode_CopyPoseFromMesh.copy_curves(value: bool) -> None
unreal.AnimNode_CopyPoseFromMesh.copy_custom_attributes(value: bool) -> None
unreal.AnimNode_CopyPoseFromMesh.root_bone_to_copy(value: Name) -> None
unreal.AnimNode_CopyPoseFromMesh.source_mesh_component(value: SkeletalMeshComponent) -> None
unreal.AnimNode_CopyPoseFromMesh.use_attached_parent(value: bool) -> None
unreal.AnimNode_CopyPoseFromMesh.use_mesh_pose(value: bool) -> None
```

## `unreal.AnimNode_CurveSource(AnimNode_Base)`

```python
unreal.AnimNode_CurveSource.__init__(source_pose: PoseLink = [], source_binding: Name = "None", alpha: float = 0.000000) -> None
unreal.AnimNode_CurveSource.alpha(value: float) -> None
unreal.AnimNode_CurveSource.source_binding(value: Name) -> None
unreal.AnimNode_CurveSource.source_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_CustomProperty(AnimNode_Base)`

```python
unreal.AnimNode_CustomProperty.__init__() -> None
```

## `unreal.AnimNode_DeadBlending(AnimNode_Base)`

```python
unreal.AnimNode_DeadBlending.__init__() -> None
```

## `unreal.AnimNode_Fabrik(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_Fabrik.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], effector_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.AnimNode_Fabrik.effector_transform(value: Transform) -> None
```

## `unreal.AnimNode_HandIKRetargeting(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_HandIKRetargeting.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], per_axis_alpha: Vector = [0.000000, 0.000000, 0.000000], hand_fk_weight: float = 0.000000) -> None
unreal.AnimNode_HandIKRetargeting.hand_fk_weight(value: float) -> None
unreal.AnimNode_HandIKRetargeting.per_axis_alpha(value: Vector) -> None
```

## `unreal.AnimNode_IKRig(AnimNode_CustomProperty)`

```python
unreal.AnimNode_IKRig.__init__(goals: Array[IKRigGoal] = [], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
unreal.AnimNode_IKRig.alpha(value: float) -> None
unreal.AnimNode_IKRig.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_IKRig.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_IKRig.alpha_curve_name(value: Name) -> None
unreal.AnimNode_IKRig.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_IKRig.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_IKRig.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_IKRig.goals(value: Array[IKRigGoal]) -> None
```

## `unreal.AnimNode_Inertialization(AnimNode_Base)`

```python
unreal.AnimNode_Inertialization.__init__() -> None
unreal.AnimNode_Inertialization.preallocate_memory(value: bool) -> None
```

## `unreal.AnimNode_Layer(AnimNode_LinkedAnimLayer)`

```python
unreal.AnimNode_Layer.__init__() -> None
```

## `unreal.AnimNode_LayeredBoneBlend(AnimNode_Base)`

```python
unreal.AnimNode_LayeredBoneBlend.__init__(base_pose: PoseLink = [], blend_poses: Array[PoseLink] = [], blend_weights: Array[float] = [], lod_threshold: int = 0, mesh_space_rotation_blend: bool = False, mesh_space_scale_blend: bool = False, curve_blend_option: CurveBlendOption = CurveBlendOption.OVERRIDE) -> None
unreal.AnimNode_LayeredBoneBlend.base_pose(value: PoseLink) -> None
unreal.AnimNode_LayeredBoneBlend.blend_poses(value: Array[PoseLink]) -> None
unreal.AnimNode_LayeredBoneBlend.blend_weights(value: Array[float]) -> None
unreal.AnimNode_LayeredBoneBlend.curve_blend_option(value: CurveBlendOption) -> None
unreal.AnimNode_LayeredBoneBlend.lod_threshold(value: int) -> None
unreal.AnimNode_LayeredBoneBlend.mesh_space_rotation_blend(value: bool) -> None
unreal.AnimNode_LayeredBoneBlend.mesh_space_scale_blend(value: bool) -> None
```

## `unreal.AnimNode_LegIK(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_LegIK.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_LinkedAnimGraph(AnimNode_CustomProperty)`

```python
unreal.AnimNode_LinkedAnimGraph.__init__() -> None
```

## `unreal.AnimNode_LinkedAnimLayer(AnimNode_LinkedAnimGraph)`

```python
unreal.AnimNode_LinkedAnimLayer.__init__() -> None
```

## `unreal.AnimNode_LinkedInputPose(AnimNode_Base)`

```python
unreal.AnimNode_LinkedInputPose.__init__() -> None
```

## `unreal.AnimNode_LiveLinkPose(AnimNode_Base)`

```python
unreal.AnimNode_LiveLinkPose.__init__(input_pose: PoseLink = [], live_link_subject_name: LiveLinkSubjectName = ["None"], do_live_link_evaluation: bool = False, retarget_asset: Class = None) -> None
unreal.AnimNode_LiveLinkPose.do_live_link_evaluation(value: bool) -> None
unreal.AnimNode_LiveLinkPose.input_pose(value: PoseLink) -> None
unreal.AnimNode_LiveLinkPose.live_link_subject_name(value: LiveLinkSubjectName) -> None
unreal.AnimNode_LiveLinkPose.retarget_asset(value: Class) -> None
```

## `unreal.AnimNode_LookAt(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_LookAt.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], look_at_location: Vector = [0.000000, 0.000000, 0.000000], interpolation_type: InterpolationBlend = InterpolationBlend.LINEAR, look_at_clamp: float = 0.000000, interpolation_time: float = 0.000000, interpolation_trigger_threashold: float = 0.000000) -> None
unreal.AnimNode_LookAt.interpolation_time(value: float) -> None
unreal.AnimNode_LookAt.interpolation_trigger_threashold(value: float) -> None
unreal.AnimNode_LookAt.interpolation_type(value: InterpolationBlend) -> None
unreal.AnimNode_LookAt.look_at_clamp(value: float) -> None
unreal.AnimNode_LookAt.look_at_location(value: Vector) -> None
```

## `unreal.AnimNode_MakeDynamicAdditive(AnimNode_Base)`

```python
unreal.AnimNode_MakeDynamicAdditive.__init__(base: PoseLink = [], additive: PoseLink = [], mesh_space_additive: bool = False) -> None
unreal.AnimNode_MakeDynamicAdditive.additive(value: PoseLink) -> None
unreal.AnimNode_MakeDynamicAdditive.base(value: PoseLink) -> None
unreal.AnimNode_MakeDynamicAdditive.mesh_space_additive(value: bool) -> None
```

## `unreal.AnimNode_MeshSpaceRefPose(AnimNode_Base)`

```python
unreal.AnimNode_MeshSpaceRefPose.__init__() -> None
```

## `unreal.AnimNode_Mirror(AnimNode_MirrorBase)`

```python
unreal.AnimNode_Mirror.__init__() -> None
```

## `unreal.AnimNode_MirrorBase(AnimNode_Base)`

```python
unreal.AnimNode_MirrorBase.__init__() -> None
```

## `unreal.AnimNode_Mirror_Standalone(AnimNode_MirrorBase)`

```python
unreal.AnimNode_Mirror_Standalone.__init__() -> None
```

## `unreal.AnimNode_ModifyBone(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_ModifyBone.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], translation: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.AnimNode_ModifyBone.rotation(value: Rotator) -> None
unreal.AnimNode_ModifyBone.scale(value: Vector) -> None
unreal.AnimNode_ModifyBone.translation(value: Vector) -> None
```

## `unreal.AnimNode_ModifyCurve(AnimNode_Base)`

```python
unreal.AnimNode_ModifyCurve.__init__(source_pose: PoseLink = [], curve_map: Map[Name, float] = {}, curve_values: Array[float] = [], alpha: float = 0.000000, apply_mode: ModifyCurveApplyMode = ModifyCurveApplyMode.ADD) -> None
unreal.AnimNode_ModifyCurve.alpha(value: float) -> None
unreal.AnimNode_ModifyCurve.apply_mode(value: ModifyCurveApplyMode) -> None
unreal.AnimNode_ModifyCurve.curve_map(value: Map[Name, float]) -> None
unreal.AnimNode_ModifyCurve.curve_values(value: Array[float]) -> None
unreal.AnimNode_ModifyCurve.source_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_MultiWayBlend(AnimNode_Base)`

```python
unreal.AnimNode_MultiWayBlend.__init__(poses: Array[PoseLink] = [], desired_alphas: Array[float] = [], alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], additive_node: bool = False, normalize_alpha: bool = False) -> None
unreal.AnimNode_MultiWayBlend.additive_node(value: bool) -> None
unreal.AnimNode_MultiWayBlend.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_MultiWayBlend.desired_alphas(value: Array[float]) -> None
unreal.AnimNode_MultiWayBlend.normalize_alpha(value: bool) -> None
unreal.AnimNode_MultiWayBlend.poses(value: Array[PoseLink]) -> None
```

## `unreal.AnimNode_ObserveBone(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_ObserveBone.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_OrientationDriver(AnimNode_PoseDriver)`

```python
unreal.AnimNode_OrientationDriver.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, pose_asset: PoseAsset = None, source_pose: PoseLink = []) -> None
```

## `unreal.AnimNode_PoseBlendNode(AnimNode_PoseHandler)`

```python
unreal.AnimNode_PoseBlendNode.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, pose_asset: PoseAsset = None, source_pose: PoseLink = []) -> None
unreal.AnimNode_PoseBlendNode.source_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_PoseByName(AnimNode_PoseHandler)`

```python
unreal.AnimNode_PoseByName.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, pose_asset: PoseAsset = None, pose_name: Name = "None", pose_weight: float = 0.000000) -> None
unreal.AnimNode_PoseByName.pose_name(value: Name) -> None
unreal.AnimNode_PoseByName.pose_weight(value: float) -> None
```

## `unreal.AnimNode_PoseDriver(AnimNode_PoseHandler)`

```python
unreal.AnimNode_PoseDriver.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, pose_asset: PoseAsset = None, source_pose: PoseLink = []) -> None
unreal.AnimNode_PoseDriver.source_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_PoseHandler(AnimNode_AssetPlayerBase)`

```python
unreal.AnimNode_PoseHandler.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, pose_asset: PoseAsset = None) -> None
unreal.AnimNode_PoseHandler.pose_asset(value: PoseAsset) -> None
```

## `unreal.AnimNode_PoseSnapshot(AnimNode_Base)`

```python
unreal.AnimNode_PoseSnapshot.__init__(snapshot_name: Name = "None", snapshot: PoseSnapshot = [[], [], "None", "None", False], mode: SnapshotSourceMode = SnapshotSourceMode.NAMED_SNAPSHOT) -> None
unreal.AnimNode_PoseSnapshot.mode(value: SnapshotSourceMode) -> None
unreal.AnimNode_PoseSnapshot.snapshot(value: PoseSnapshot) -> None
unreal.AnimNode_PoseSnapshot.snapshot_name(value: Name) -> None
```

## `unreal.AnimNode_PreviewRetargetPose(AnimNode_Base)`

```python
unreal.AnimNode_PreviewRetargetPose.__init__() -> None
```

## `unreal.AnimNode_Ragdoll(AnimNode_RigidBody)`

```python
unreal.AnimNode_Ragdoll.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], use_local_lod_threshold_only: bool = False) -> None
```

## `unreal.AnimNode_RandomPlayer(AnimNode_AssetPlayerRelevancyBase)`

```python
unreal.AnimNode_RandomPlayer.__init__(entries: Array[RandomPlayerSequenceEntry] = [], blend_weight: float = 0.000000, shuffle_mode: bool = False) -> None
unreal.AnimNode_RandomPlayer.blend_weight(value: float) -> None
unreal.AnimNode_RandomPlayer.entries(value: Array[RandomPlayerSequenceEntry]) -> None
unreal.AnimNode_RandomPlayer.shuffle_mode(value: bool) -> None
```

## `unreal.AnimNode_RefPose(AnimNode_Base)`

```python
unreal.AnimNode_RefPose.__init__() -> None
```

## `unreal.AnimNode_ResetRoot(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_ResetRoot.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_RetargetPoseFromMesh(AnimNode_Base)`

```python
unreal.AnimNode_RetargetPoseFromMesh.__init__(source_mesh_component: SkeletalMeshComponent = None, use_attached_parent: bool = False, ik_retargeter_asset: IKRetargeter = None, custom_retarget_profile: RetargetProfile = [False, "None", False, "None", False, {}, False, [1.000000, 1.000000, 0.000000, [1.000000, 1.000000, 1.000000], 1.000000, 1.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 1.000000, 0.000000], False, [True, True, True, True, False, WarpingDirectionSource.GOALS, BasicAxis.Y, "None", 1.000000, 0.000000, 1.000000]], suppress_warnings: bool = False, copy_curves: bool = False, lod_threshold: int = 0, lod_threshold_for_ik: int = 0) -> None
unreal.AnimNode_RetargetPoseFromMesh.copy_curves(value: bool) -> None
unreal.AnimNode_RetargetPoseFromMesh.custom_retarget_profile(value: RetargetProfile) -> None
unreal.AnimNode_RetargetPoseFromMesh.ik_retargeter_asset(value: IKRetargeter) -> None
unreal.AnimNode_RetargetPoseFromMesh.lod_threshold(value: int) -> None
unreal.AnimNode_RetargetPoseFromMesh.lod_threshold_for_ik(value: int) -> None
unreal.AnimNode_RetargetPoseFromMesh.source_mesh_component(value: SkeletalMeshComponent) -> None
unreal.AnimNode_RetargetPoseFromMesh.suppress_warnings(value: bool) -> None
unreal.AnimNode_RetargetPoseFromMesh.use_attached_parent(value: bool) -> None
```

## `unreal.AnimNode_RigidBody(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_RigidBody.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], use_local_lod_threshold_only: bool = False) -> None
unreal.AnimNode_RigidBody.use_local_lod_threshold_only(value: bool) -> None
```

## `unreal.AnimNode_Root(AnimNode_Base)`

```python
unreal.AnimNode_Root.__init__(result: PoseLink = []) -> None
unreal.AnimNode_Root.group(value: Name) -> None
unreal.AnimNode_Root.result(value: PoseLink) -> None
```

## `unreal.AnimNode_RotateRootBone(AnimNode_Base)`

```python
unreal.AnimNode_RotateRootBone.__init__(base_pose: PoseLink = [], pitch: float = 0.000000, yaw: float = 0.000000, pitch_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], yaw_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], mesh_to_component: Rotator = [0.000000, 0.000000, 0.000000], rotate_root_motion_attribute: bool = False) -> None
unreal.AnimNode_RotateRootBone.base_pose(value: PoseLink) -> None
unreal.AnimNode_RotateRootBone.mesh_to_component(value: Rotator) -> None
unreal.AnimNode_RotateRootBone.pitch(value: float) -> None
unreal.AnimNode_RotateRootBone.pitch_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_RotateRootBone.rotate_root_motion_attribute(value: bool) -> None
unreal.AnimNode_RotateRootBone.yaw(value: float) -> None
unreal.AnimNode_RotateRootBone.yaw_scale_bias_clamp(value: InputScaleBiasClamp) -> None
```

## `unreal.AnimNode_RotationMultiplier(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_RotationMultiplier.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], multiplier: float = 0.000000) -> None
unreal.AnimNode_RotationMultiplier.multiplier(value: float) -> None
```

## `unreal.AnimNode_RotationOffsetBlendSpace(AnimNode_BlendSpacePlayer)`

```python
unreal.AnimNode_RotationOffsetBlendSpace.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000, base_pose: PoseLink = [], lod_threshold: int = 0, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha(value: float) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_curve_name(value: Name) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_RotationOffsetBlendSpace.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_RotationOffsetBlendSpace.base_pose(value: PoseLink) -> None
unreal.AnimNode_RotationOffsetBlendSpace.lod_threshold(value: int) -> None
```

## `unreal.AnimNode_RotationOffsetBlendSpaceGraph(AnimNode_BlendSpaceGraphBase)`

```python
unreal.AnimNode_RotationOffsetBlendSpaceGraph.__init__(x: float = 0.000000, y: float = 0.000000, group_name: Name = "None", group_role: AnimGroupRole = AnimGroupRole.CAN_BE_LEADER, base_pose: PoseLink = [], lod_threshold: int = 0, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha(value: float) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_curve_name(value: Name) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.base_pose(value: PoseLink) -> None
unreal.AnimNode_RotationOffsetBlendSpaceGraph.lod_threshold(value: int) -> None
```

## `unreal.AnimNode_SaveCachedPose(AnimNode_Base)`

```python
unreal.AnimNode_SaveCachedPose.__init__(pose: PoseLink = []) -> None
unreal.AnimNode_SaveCachedPose.pose(value: PoseLink) -> None
```

## `unreal.AnimNode_ScaleChainLength(AnimNode_Base)`

```python
unreal.AnimNode_ScaleChainLength.__init__(default_chain_length: float = 0.000000, target_location: Vector = [0.000000, 0.000000, 0.000000], alpha: float = 0.000000) -> None
unreal.AnimNode_ScaleChainLength.alpha(value: float) -> None
unreal.AnimNode_ScaleChainLength.default_chain_length(value: float) -> None
unreal.AnimNode_ScaleChainLength.target_location(value: Vector) -> None
```

## `unreal.AnimNode_SequenceEvaluator(AnimNode_SequenceEvaluatorBase)`

```python
unreal.AnimNode_SequenceEvaluator.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SequenceEvaluatorBase(AnimNode_AssetPlayerBase)`

```python
unreal.AnimNode_SequenceEvaluatorBase.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SequenceEvaluator_Standalone(AnimNode_SequenceEvaluatorBase)`

```python
unreal.AnimNode_SequenceEvaluator_Standalone.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SequencePlayer(AnimNode_SequencePlayerBase)`

```python
unreal.AnimNode_SequencePlayer.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SequencePlayerBase(AnimNode_AssetPlayerBase)`

```python
unreal.AnimNode_SequencePlayerBase.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SequencePlayer_Standalone(AnimNode_SequencePlayerBase)`

```python
unreal.AnimNode_SequencePlayer_Standalone.__init__(blend_weight: float = 0.000000, internal_time_accumulator: float = 0.000000) -> None
```

## `unreal.AnimNode_SingleNode(AnimNode_Base)`

```python
unreal.AnimNode_SingleNode.__init__(source_pose: PoseLink = []) -> None
unreal.AnimNode_SingleNode.source_pose(value: PoseLink) -> None
```

## `unreal.AnimNode_SkeletalControlBase(AnimNode_Base)`

```python
unreal.AnimNode_SkeletalControlBase.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
unreal.AnimNode_SkeletalControlBase.alpha(value: float) -> None
unreal.AnimNode_SkeletalControlBase.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_SkeletalControlBase.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_SkeletalControlBase.alpha_curve_name(value: Name) -> None
unreal.AnimNode_SkeletalControlBase.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_SkeletalControlBase.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_SkeletalControlBase.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_SkeletalControlBase.component_pose(value: ComponentSpacePoseLink) -> None
unreal.AnimNode_SkeletalControlBase.lod_threshold(value: int) -> None
```

## `unreal.AnimNode_Slot(AnimNode_Base)`

```python
unreal.AnimNode_Slot.__init__(source: PoseLink = [], slot_name: Name = "None", always_update_source_pose: bool = False) -> None
unreal.AnimNode_Slot.always_update_source_pose(value: bool) -> None
unreal.AnimNode_Slot.slot_name(value: Name) -> None
unreal.AnimNode_Slot.source(value: PoseLink) -> None
```

## `unreal.AnimNode_SplineIK(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_SplineIK.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], control_points: Array[Transform] = [], roll: float = 0.000000, twist_start: float = 0.000000, twist_end: float = 0.000000, stretch: float = 0.000000, offset: float = 0.000000) -> None
unreal.AnimNode_SplineIK.control_points(value: Array[Transform]) -> None
unreal.AnimNode_SplineIK.offset(value: float) -> None
unreal.AnimNode_SplineIK.roll(value: float) -> None
unreal.AnimNode_SplineIK.stretch(value: float) -> None
unreal.AnimNode_SplineIK.twist_end(value: float) -> None
unreal.AnimNode_SplineIK.twist_start(value: float) -> None
```

## `unreal.AnimNode_SpringBone(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_SpringBone.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], max_displacement: float = 0.000000) -> None
unreal.AnimNode_SpringBone.max_displacement(value: float) -> None
```

## `unreal.AnimNode_StateMachine(AnimNode_Base)`

```python
unreal.AnimNode_StateMachine.__init__() -> None
```

## `unreal.AnimNode_StateResult(AnimNode_Root)`

```python
unreal.AnimNode_StateResult.__init__(result: PoseLink = []) -> None
```

## `unreal.AnimNode_SubInput(AnimNode_LinkedInputPose)`

```python
unreal.AnimNode_SubInput.__init__() -> None
```

## `unreal.AnimNode_SubInstance(AnimNode_LinkedAnimGraph)`

```python
unreal.AnimNode_SubInstance.__init__() -> None
```

## `unreal.AnimNode_Sync(AnimNode_Base)`

```python
unreal.AnimNode_Sync.__init__() -> None
```

## `unreal.AnimNode_Trail(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_Trail.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], relaxation_speed_scale: float = 0.000000, relaxation_speed_scale_input_processor: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], rotation_offsets: Array[Vector] = []) -> None
unreal.AnimNode_Trail.relaxation_speed_scale(value: float) -> None
unreal.AnimNode_Trail.relaxation_speed_scale_input_processor(value: InputScaleBiasClamp) -> None
unreal.AnimNode_Trail.rotation_offsets(value: Array[Vector]) -> None
```

## `unreal.AnimNode_TransitionPoseEvaluator(AnimNode_Base)`

```python
unreal.AnimNode_TransitionPoseEvaluator.__init__(frames_to_cache_pose: int = 0, data_source: EvaluatorDataSource = EvaluatorDataSource.EDS_SOURCE_POSE, evaluator_mode: EvaluatorMode = EvaluatorMode.EM_STANDARD) -> None
unreal.AnimNode_TransitionPoseEvaluator.data_source(value: EvaluatorDataSource) -> None
unreal.AnimNode_TransitionPoseEvaluator.evaluator_mode(value: EvaluatorMode) -> None
unreal.AnimNode_TransitionPoseEvaluator.frames_to_cache_pose(value: int) -> None
```

## `unreal.AnimNode_TransitionResult(AnimNode_Base)`

```python
unreal.AnimNode_TransitionResult.__init__(can_enter_transition: bool = False) -> None
unreal.AnimNode_TransitionResult.can_enter_transition(value: bool) -> None
```

## `unreal.AnimNode_TwistCorrectiveNode(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_TwistCorrectiveNode.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimNode_TwoBoneIK(AnimNode_SkeletalControlBase)`

```python
unreal.AnimNode_TwoBoneIK.__init__(component_pose: ComponentSpacePoseLink = [], lod_threshold: int = 0, alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000], effector_location: Vector = [0.000000, 0.000000, 0.000000], joint_target_location: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.AnimNode_TwoBoneIK.effector_location(value: Vector) -> None
unreal.AnimNode_TwoBoneIK.joint_target_location(value: Vector) -> None
```

## `unreal.AnimNode_TwoWayBlend(AnimNode_Base)`

```python
unreal.AnimNode_TwoWayBlend.__init__(a: PoseLink = [], b: PoseLink = [], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
unreal.AnimNode_TwoWayBlend.a(value: PoseLink) -> None
unreal.AnimNode_TwoWayBlend.alpha(value: float) -> None
unreal.AnimNode_TwoWayBlend.alpha_bool_blend(value: InputAlphaBoolBlend) -> None
unreal.AnimNode_TwoWayBlend.alpha_bool_enabled(value: bool) -> None
unreal.AnimNode_TwoWayBlend.alpha_curve_name(value: Name) -> None
unreal.AnimNode_TwoWayBlend.alpha_input_type(value: AnimAlphaInputType) -> None
unreal.AnimNode_TwoWayBlend.alpha_scale_bias(value: InputScaleBias) -> None
unreal.AnimNode_TwoWayBlend.alpha_scale_bias_clamp(value: InputScaleBiasClamp) -> None
unreal.AnimNode_TwoWayBlend.b(value: PoseLink) -> None
```

## `unreal.AnimNotify(Object)`

```python
unreal.AnimNotify.get_default_trigger_weight_threshold() -> float
unreal.AnimNotify.get_notify_name() -> str
unreal.AnimNotify.notify_color() -> Color
unreal.AnimNotify.received_notify(mesh_comp: SkeletalMeshComponent, animation: AnimSequenceBase, event_reference: AnimNotifyEventReference) -> bool
unreal.AnimNotify.should_fire_in_editor() -> bool
```

## `unreal.AnimNotifyEvent(AnimLinkableElement)`

```python
unreal.AnimNotifyEvent.__init__(trigger_weight_threshold: float = 0.000000, notify_name: Name = "None", notify: AnimNotify = None, notify_state_class: AnimNotifyState = None, montage_tick_type: MontageNotifyTickType = MontageNotifyTickType.QUEUED, notify_trigger_chance: float = 0.000000, notify_filter_type: NotifyFilterType = NotifyFilterType.NO_FILTERING, notify_filter_lod: int = 0, can_be_filtered_via_request: bool = False, trigger_on_dedicated_server: bool = False, trigger_on_follower: bool = False) -> None
unreal.AnimNotifyEvent.can_be_filtered_via_request(value: bool) -> None
unreal.AnimNotifyEvent.montage_tick_type(value: MontageNotifyTickType) -> None
unreal.AnimNotifyEvent.notify(value: AnimNotify) -> None
unreal.AnimNotifyEvent.notify_filter_lod(value: int) -> None
unreal.AnimNotifyEvent.notify_filter_type(value: NotifyFilterType) -> None
unreal.AnimNotifyEvent.notify_name() -> Name
unreal.AnimNotifyEvent.notify_state_class(value: AnimNotifyState) -> None
unreal.AnimNotifyEvent.notify_trigger_chance(value: float) -> None
unreal.AnimNotifyEvent.trigger_on_dedicated_server(value: bool) -> None
unreal.AnimNotifyEvent.trigger_on_follower(value: bool) -> None
unreal.AnimNotifyEvent.trigger_weight_threshold(value: float) -> None
```

## `unreal.AnimNotifyEventReference(StructBase)`

```python
unreal.AnimNotifyEventReference.__init__() -> None
unreal.AnimNotifyEventReference.get_current_animation_notify_state_time() -> float
unreal.AnimNotifyEventReference.get_current_animation_notify_state_time_ratio() -> float
unreal.AnimNotifyEventReference.get_current_animation_time() -> float
unreal.AnimNotifyEventReference.get_current_animation_time_ratio() -> float
unreal.AnimNotifyEventReference.is_blending_out() -> bool
unreal.AnimNotifyEventReference.notify_state_reached_end() -> bool
```

## `unreal.AnimNotifyState(Object)`

```python
unreal.AnimNotifyState.get_default_trigger_weight_threshold() -> float
unreal.AnimNotifyState.get_notify_name() -> str
unreal.AnimNotifyState.notify_color() -> Color
unreal.AnimNotifyState.received_notify_begin(mesh_comp: SkeletalMeshComponent, animation: AnimSequenceBase, total_duration: float, event_reference: AnimNotifyEventReference) -> bool
unreal.AnimNotifyState.received_notify_end(mesh_comp: SkeletalMeshComponent, animation: AnimSequenceBase, event_reference: AnimNotifyEventReference) -> bool
unreal.AnimNotifyState.received_notify_tick(mesh_comp: SkeletalMeshComponent, animation: AnimSequenceBase, frame_delta_time: float, event_reference: AnimNotifyEventReference) -> bool
unreal.AnimNotifyState.should_fire_in_editor() -> bool
```

## `unreal.AnimNotifyState_Trail(AnimNotifyState)`

```python
unreal.AnimNotifyState_Trail.first_socket_name() -> Name
unreal.AnimNotifyState_Trail.override_ps_template(mesh_comp: SkeletalMeshComponent, animation: AnimSequenceBase) -> ParticleSystem
unreal.AnimNotifyState_Trail.ps_template() -> ParticleSystem
unreal.AnimNotifyState_Trail.recycle_spawned_systems() -> bool
unreal.AnimNotifyState_Trail.second_socket_name() -> Name
unreal.AnimNotifyState_Trail.width_scale_curve() -> Name
unreal.AnimNotifyState_Trail.width_scale_mode() -> TrailWidthMode
```

## `unreal.AnimNotify_GameplayCue(AnimNotify)`

```python
unreal.AnimNotify_GameplayCue.gameplay_cue() -> GameplayCueTag
```

## `unreal.AnimNotify_GameplayCueState(AnimNotifyState)`

```python
unreal.AnimNotify_GameplayCueState.gameplay_cue() -> GameplayCueTag
```

## `unreal.AnimNotify_PlayMontageNotify(AnimNotify)`

```python
unreal.AnimNotify_PlayMontageNotify.notify_name() -> Name
```

## `unreal.AnimNotify_PlayMontageNotifyWindow(AnimNotifyState)`

```python
unreal.AnimNotify_PlayMontageNotifyWindow.notify_name() -> Name
```

## `unreal.AnimNotify_PlayParticleEffect(AnimNotify)`

```python
unreal.AnimNotify_PlayParticleEffect.attached() -> bool
unreal.AnimNotify_PlayParticleEffect.location_offset() -> Vector
unreal.AnimNotify_PlayParticleEffect.ps_template() -> ParticleSystem
unreal.AnimNotify_PlayParticleEffect.rotation_offset() -> Rotator
unreal.AnimNotify_PlayParticleEffect.socket_name() -> Name
```

## `unreal.AnimNotify_PlaySound(AnimNotify)`

```python
unreal.AnimNotify_PlaySound.attach_name() -> Name
unreal.AnimNotify_PlaySound.follow() -> bool
unreal.AnimNotify_PlaySound.pitch_multiplier() -> float
unreal.AnimNotify_PlaySound.sound() -> SoundBase
unreal.AnimNotify_PlaySound.volume_multiplier() -> float
```

## `unreal.AnimPhysBodyDefinition(StructBase)`

```python
unreal.AnimPhysBodyDefinition.__init__() -> None
```

## `unreal.AnimPhysConstraintSetup(StructBase)`

```python
unreal.AnimPhysConstraintSetup.__init__() -> None
```

## `unreal.AnimPhysPlanarLimit(StructBase)`

```python
unreal.AnimPhysPlanarLimit.__init__() -> None
```

## `unreal.AnimPhysSphericalLimit(StructBase)`

```python
unreal.AnimPhysSphericalLimit.__init__() -> None
```

## `unreal.AnimPose(StructBase)`

```python
unreal.AnimPose.__init__() -> None
unreal.AnimPose.evaluate_animation_blueprint_with_input_pose(target_skeletal_mesh: SkeletalMesh, animation_blueprint: AnimBlueprint) -> AnimPose
unreal.AnimPose.get_bone_names() -> Array[Name]
unreal.AnimPose.get_bone_pose(bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.get_curve_names() -> Array[Name]
unreal.AnimPose.get_curve_weight(curve_name: Name) -> float
unreal.AnimPose.get_ref_bone_pose(bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.get_ref_pose_relative_transform(from_bone_name: Name, to_bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.get_relative_to_ref_pose_transform(bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.get_relative_transform(from_bone_name: Name, to_bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.get_socket_names() -> Array[Name]
unreal.AnimPose.get_socket_pose(socket_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPose.is_valid() -> bool
unreal.AnimPose.set_bone_pose(transform: Transform, bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> None
```

## `unreal.AnimPoseContext(AnimExecutionContext)`

```python
unreal.AnimPoseContext.__init__() -> None
```

## `unreal.AnimPoseEvaluationOptions(StructBase)`

```python
unreal.AnimPoseEvaluationOptions.__init__(evaluation_type: AnimDataEvalType = AnimDataEvalType.SOURCE, should_retarget: bool = False, extract_root_motion: bool = False, incorporate_root_motion_into_pose: bool = False, optional_skeletal_mesh: SkeletalMesh = None, retrieve_additive_as_full_pose: bool = False, evaluate_curves: bool = False) -> None
unreal.AnimPoseEvaluationOptions.evaluate_curves(value: bool) -> None
unreal.AnimPoseEvaluationOptions.evaluation_type(value: AnimDataEvalType) -> None
unreal.AnimPoseEvaluationOptions.extract_root_motion(value: bool) -> None
unreal.AnimPoseEvaluationOptions.incorporate_root_motion_into_pose(value: bool) -> None
unreal.AnimPoseEvaluationOptions.optional_skeletal_mesh(value: SkeletalMesh) -> None
unreal.AnimPoseEvaluationOptions.retrieve_additive_as_full_pose(value: bool) -> None
unreal.AnimPoseEvaluationOptions.should_retarget(value: bool) -> None
```

## `unreal.AnimPoseExtensions(BlueprintFunctionLibrary)`

```python
unreal.AnimPoseExtensions.evaluate_animation_blueprint_with_input_pose(input_pose: AnimPose, target_skeletal_mesh: SkeletalMesh, animation_blueprint: AnimBlueprint) -> AnimPose
unreal.AnimPoseExtensions.get_anim_pose_at_frame(animation_sequence_base: AnimSequenceBase, frame_index: int, evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
unreal.AnimPoseExtensions.get_anim_pose_at_time(animation_sequence_base: AnimSequenceBase, time: float, evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
unreal.AnimPoseExtensions.get_bone_names(pose: AnimPose) -> Array[Name]
unreal.AnimPoseExtensions.get_bone_pose(pose: AnimPose, bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.get_curve_names(pose: AnimPose) -> Array[Name]
unreal.AnimPoseExtensions.get_curve_weight(pose: AnimPose, curve_name: Name) -> float
unreal.AnimPoseExtensions.get_ref_bone_pose(pose: AnimPose, bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.get_ref_pose_relative_transform(pose: AnimPose, from_bone_name: Name, to_bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.get_reference_pose(skeleton: Skeleton) -> AnimPose
unreal.AnimPoseExtensions.get_relative_to_ref_pose_transform(pose: AnimPose, bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.get_relative_transform(pose: AnimPose, from_bone_name: Name, to_bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.get_socket_names(pose: AnimPose) -> Array[Name]
unreal.AnimPoseExtensions.get_socket_pose(pose: AnimPose, socket_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
unreal.AnimPoseExtensions.is_valid(pose: AnimPose) -> bool
unreal.AnimPoseExtensions.set_bone_pose(pose: AnimPose, transform: Transform, bone_name: Name, space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> AnimPose
```

## `unreal.AnimSegment(StructBase)`

```python
unreal.AnimSegment.__init__() -> None
```

## `unreal.AnimSeqExportOption(Object)`

```python
unreal.AnimSeqExportOption.curve_interpolation(value: RichCurveInterpMode) -> None
unreal.AnimSeqExportOption.custom_display_rate(value: FrameRate) -> None
unreal.AnimSeqExportOption.custom_end_frame(value: FrameNumber) -> None
unreal.AnimSeqExportOption.custom_start_frame(value: FrameNumber) -> None
unreal.AnimSeqExportOption.delay_before_start(value: FrameNumber) -> None
unreal.AnimSeqExportOption.evaluate_all_skeletal_mesh_components(value: bool) -> None
unreal.AnimSeqExportOption.exclude_animation_names(value: Array[str]) -> None
unreal.AnimSeqExportOption.export_attribute_curves(value: bool) -> None
unreal.AnimSeqExportOption.export_material_curves(value: bool) -> None
unreal.AnimSeqExportOption.export_morph_targets(value: bool) -> None
unreal.AnimSeqExportOption.export_transforms(value: bool) -> None
unreal.AnimSeqExportOption.include_animation_names(value: Array[str]) -> None
unreal.AnimSeqExportOption.interpolation(value: AnimInterpolationType) -> None
unreal.AnimSeqExportOption.record_in_world_space(value: bool) -> None
unreal.AnimSeqExportOption.transact_recording(value: bool) -> None
unreal.AnimSeqExportOption.use_custom_time_range(value: bool) -> None
unreal.AnimSeqExportOption.warm_up_frames(value: FrameNumber) -> None
```

## `unreal.AnimSequence(AnimSequenceBase)`

```python
unreal.AnimSequence.add_bone_float_custom_attribute(bone_name: Name, attribute_name: Name, time_keys: Array[float], value_keys: Array[float]) -> None
unreal.AnimSequence.add_bone_integer_custom_attribute(bone_name: Name, attribute_name: Name, time_keys: Array[float], value_keys: Array[int]) -> None
unreal.AnimSequence.add_bone_string_custom_attribute(bone_name: Name, attribute_name: Name, time_keys: Array[float], value_keys: Array[str]) -> None
unreal.AnimSequence.clear_retarget_source_asset() -> None
unreal.AnimSequence.get_retarget_source_asset() -> SkeletalMesh
unreal.AnimSequence.remove_all_custom_attributes() -> None
unreal.AnimSequence.remove_all_custom_attributes_for_bone(bone_name: Name) -> None
unreal.AnimSequence.remove_custom_attribute(bone_name: Name, attribute_name: Name) -> None
unreal.AnimSequence.set_retarget_source_asset(retarget_source_asset: SkeletalMesh) -> None
unreal.AnimSequence.update_retarget_source_asset_data() -> None
```

## `unreal.AnimSequenceBase(AnimationAsset)`

```python
unreal.AnimSequenceBase.add_transform_attribute(attribute_name: Name, bone_name: Name, keys: Array[float], values: Array[Transform]) -> bool
unreal.AnimSequenceBase.controller() -> AnimationDataController
unreal.AnimSequenceBase.data_model() -> AnimDataModel
unreal.AnimSequenceBase.data_model_interface() -> AnimationDataModel
unreal.AnimSequenceBase.get_anim_pose_at_frame(frame_index: int, evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
unreal.AnimSequenceBase.get_anim_pose_at_time(time: float, evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
unreal.AnimSequenceBase.sequence_length() -> float
```

## `unreal.AnimSequencerController(Object)`

```python
unreal.AnimSequencerController.add_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.add_bone_curve(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimSequencerController.add_bone_track(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimSequencerController.add_curve(curve_id: AnimationCurveIdentifier, curve_flags: int = 4, should_transact: bool = True) -> bool
unreal.AnimSequencerController.close_bracket(should_transact: bool = True) -> None
unreal.AnimSequencerController.duplicate_attribute(attribute_identifier: AnimationAttributeIdentifier, new_attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.duplicate_curve(copy_curve_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.find_or_add_curve_names_on_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimSequencerController.get_model_interface() -> AnimationDataModel
unreal.AnimSequencerController.insert_bone_track(bone_name: Name, desired_index: int, should_transact: bool = True) -> int
unreal.AnimSequencerController.open_bracket(title: Text, should_transact: bool = True) -> None
unreal.AnimSequencerController.remove_all_attributes(should_transact: bool = True) -> int
unreal.AnimSequencerController.remove_all_attributes_for_bone(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimSequencerController.remove_all_bone_tracks(should_transact: bool = True) -> None
unreal.AnimSequencerController.remove_all_curves_of_type(supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimSequencerController.remove_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.remove_attribute_key(attribute_identifier: AnimationAttributeIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimSequencerController.remove_bone_track(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimSequencerController.remove_curve(curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.remove_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimSequencerController.remove_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimSequencerController.rename_curve(curve_to_rename_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimSequencerController.resize(length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimSequencerController.resize_in_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimSequencerController.resize_number_of_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimSequencerController.resize_play_length(new_length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimSequencerController.scale_curve(curve_id: AnimationCurveIdentifier, origin: float, factor: float, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_bone_track_keys(bone_name: Name, positional_keys: Array[Vector], rotational_keys: Array[Quat], scaling_keys: Array[Vector], should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_color(curve_id: AnimationCurveIdentifier, color: LinearColor, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_comment(curve_id: AnimationCurveIdentifier, comment: str = "/**\n\t* Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.\n\t* Currently changing curve comments is only supported for float curves.\n\t*\n\t* @param\tCurveId\t\t\t\tIdentifier of the curve to change the comment for\n\t* @param\tComment\t\t\t\tComment to which the curve is to be set\n\t* @param\tbShouldTransact\t\tWhether or not any undo-redo changes should be generated\n\t*\n\t* @return\tWhether or not the curve comment was successfully changed\n\t*/", should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_flag(curve_id: AnimationCurveIdentifier, flag: AnimAssetCurveFlags, state: bool = True, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_flags(curve_id: AnimationCurveIdentifier, flags: int, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_key(curve_id: AnimationCurveIdentifier, key: RichCurveKey, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_curve_keys(curve_id: AnimationCurveIdentifier, curve_keys: Array[RichCurveKey], should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_frame_rate(frame_rate: FrameRate, should_transact: bool = True) -> None
unreal.AnimSequencerController.set_model(model: AnimationDataModel) -> None
unreal.AnimSequencerController.set_number_of_frames(new_length_in_frames: FrameNumber, should_transact: bool = True) -> None
unreal.AnimSequencerController.set_play_length(length: float, should_transact: bool = True) -> None
unreal.AnimSequencerController.set_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, value: Transform, should_transact: bool = True) -> bool
unreal.AnimSequencerController.set_transform_curve_keys(curve_id: AnimationCurveIdentifier, transform_values: Array[Transform], time_keys: Array[float], should_transact: bool = True) -> bool
unreal.AnimSequencerController.update_curve_names_from_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
```

## `unreal.AnimSharingAdditiveInstance(AnimInstance)`

```python
unreal.AnimSharingAdditiveInstance.additive_animation() -> AnimSequence
unreal.AnimSharingAdditiveInstance.alpha() -> float
unreal.AnimSharingAdditiveInstance.base_component() -> SkeletalMeshComponent
unreal.AnimSharingAdditiveInstance.state_bool() -> bool
```

## `unreal.AnimSharingStateInstance(AnimInstance)`

```python
unreal.AnimSharingStateInstance.animation_to_play() -> AnimSequence
unreal.AnimSharingStateInstance.get_instanced_actors() -> Array[Actor]
unreal.AnimSharingStateInstance.permutation_time_offset() -> float
unreal.AnimSharingStateInstance.play_rate() -> float
unreal.AnimSharingStateInstance.state_bool() -> bool
```

## `unreal.AnimSharingTransitionInstance(AnimInstance)`

```python
unreal.AnimSharingTransitionInstance.blend_bool() -> bool
unreal.AnimSharingTransitionInstance.blend_time() -> float
unreal.AnimSharingTransitionInstance.from_component() -> SkeletalMeshComponent
unreal.AnimSharingTransitionInstance.to_component() -> SkeletalMeshComponent
```

## `unreal.AnimSingleNodeInstance(AnimInstance)`

```python
unreal.AnimSingleNodeInstance.get_animation_asset() -> AnimationAsset
unreal.AnimSingleNodeInstance.get_length() -> float
unreal.AnimSingleNodeInstance.get_mirror_data_table() -> MirrorDataTable
unreal.AnimSingleNodeInstance.play_anim(is_looping: bool = False, play_rate: float = 1.000000, start_position: float = 0.000000) -> None
unreal.AnimSingleNodeInstance.set_animation_asset(new_asset: AnimationAsset, is_looping: bool = True, play_rate: float = 1.000000) -> None
unreal.AnimSingleNodeInstance.set_blend_space_position(position: Vector) -> None
unreal.AnimSingleNodeInstance.set_looping(is_looping: bool) -> None
unreal.AnimSingleNodeInstance.set_mirror_data_table(mirror_data_table: MirrorDataTable) -> None
unreal.AnimSingleNodeInstance.set_play_rate(play_rate: float) -> None
unreal.AnimSingleNodeInstance.set_playing(is_playing: bool) -> None
unreal.AnimSingleNodeInstance.set_position(position: float, fire_notifies: bool = True) -> None
unreal.AnimSingleNodeInstance.set_position_with_previous_time(position: float, previous_time: float, fire_notifies: bool = True) -> None
unreal.AnimSingleNodeInstance.set_preview_curve_override(pose_name: Name, value: float, remove_if_zero: bool) -> None
unreal.AnimSingleNodeInstance.set_reverse(reverse: bool) -> None
unreal.AnimSingleNodeInstance.stop_anim() -> None
```

## `unreal.AnimStateAliasNode(AnimStateNodeBase)`

```python
unreal.AnimStateAliasNode.global_alias(value: bool) -> None
```

## `unreal.AnimStateTransitionNode(AnimStateNodeBase)`

```python
unreal.AnimStateTransitionNode.logic_type(value: TransitionLogicType) -> None
```

## `unreal.AnimSyncMarker(StructBase)`

```python
unreal.AnimSyncMarker.__init__(marker_name: Name = "None", time: float = 0.000000) -> None
unreal.AnimSyncMarker.marker_name() -> Name
unreal.AnimSyncMarker.time() -> float
```

## `unreal.AnimUpdateContext(AnimExecutionContext)`

```python
unreal.AnimUpdateContext.__init__() -> None
```

## `unreal.AnimatedBoneAttribute(StructBase)`

```python
unreal.AnimatedBoneAttribute.__init__(identifier: AnimationAttributeIdentifier = ["None", "None", -1, None, [""]], curve: AttributeCurve = []) -> None
unreal.AnimatedBoneAttribute.curve() -> AttributeCurve
unreal.AnimatedBoneAttribute.identifier() -> AnimationAttributeIdentifier
```

## `unreal.AnimationAsset(Object)`

```python
unreal.AnimationAsset.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.AnimationAsset.create_attribute_identifier(attribute_name: Name, bone_name: Name, attribute_type: ScriptStruct, validate_exists_on_asset: bool = False) -> AnimationAttributeIdentifier
unreal.AnimationAsset.find_meta_data_by_class(meta_data_class: Class) -> AnimMetaData
unreal.AnimationAsset.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.AnimationAsset.get_play_length() -> float
unreal.AnimationAsset.get_skeleton() -> Skeleton
unreal.AnimationAsset.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.AnimationAsset.set_preview_skeletal_mesh(preview_mesh: SkeletalMesh) -> None
```

## `unreal.AnimationAssetExtensions(BlueprintFunctionLibrary)`

```python
unreal.AnimationAssetExtensions.get_skeleton(asset: AnimationAsset) -> Skeleton
```

## `unreal.AnimationAttributeIdentifier(StructBase)`

```python
unreal.AnimationAttributeIdentifier.__init__(name: Name = "None", bone_name: Name = "None", bone_index: int = 0, script_struct: ScriptStruct = None, script_struct_path: SoftObjectPath = [""]) -> None
unreal.AnimationAttributeIdentifier.bone_index() -> int
unreal.AnimationAttributeIdentifier.bone_name() -> Name
unreal.AnimationAttributeIdentifier.is_valid() -> bool
unreal.AnimationAttributeIdentifier.name() -> Name
unreal.AnimationAttributeIdentifier.script_struct() -> ScriptStruct
unreal.AnimationAttributeIdentifier.script_struct_path() -> SoftObjectPath
```

## `unreal.AnimationAttributeIdentifierExtensions(BlueprintFunctionLibrary)`

```python
unreal.AnimationAttributeIdentifierExtensions.create_attribute_identifier(animation_asset: AnimationAsset, attribute_name: Name, bone_name: Name, attribute_type: ScriptStruct, validate_exists_on_asset: bool = False) -> AnimationAttributeIdentifier
unreal.AnimationAttributeIdentifierExtensions.is_valid(identifier: AnimationAttributeIdentifier) -> Optional[AnimationAttributeIdentifier]
```

## `unreal.AnimationCompressionLibraryDatabase(Object)`

```python
unreal.AnimationCompressionLibraryDatabase.get_visual_fidelity(database_asset: AnimationCompressionLibraryDatabase) -> ACLVisualFidelity
unreal.AnimationCompressionLibraryDatabase.set_visual_fidelity(world_context_object: Object, latent_info: LatentActionInfo, database_asset: AnimationCompressionLibraryDatabase, visual_fidelity: ACLVisualFidelity = ACLVisualFidelity.HIGHEST) -> ACLVisualFidelityChangeResult
```

## `unreal.AnimationCurveData(StructBase)`

```python
unreal.AnimationCurveData.__init__(float_curves: Array[FloatCurve] = [], transform_curves: Array[TransformCurve] = []) -> None
unreal.AnimationCurveData.float_curves() -> Array[FloatCurve]
unreal.AnimationCurveData.transform_curves() -> Array[TransformCurve]
```

## `unreal.AnimationCurveIdentifier(StructBase)`

```python
unreal.AnimationCurveIdentifier.__init__() -> None
unreal.AnimationCurveIdentifier.get_name() -> Name
unreal.AnimationCurveIdentifier.get_transform_child_curve_identifier(channel: TransformCurveChannel, axis: VectorCurveChannel) -> bool
unreal.AnimationCurveIdentifier.get_type() -> RawCurveTrackTypes
unreal.AnimationCurveIdentifier.is_valid() -> bool
unreal.AnimationCurveIdentifier.set_curve_identifier(name: Name, curve_type: RawCurveTrackTypes) -> None
```

## `unreal.AnimationCurveIdentifierExtensions(BlueprintFunctionLibrary)`

```python
unreal.AnimationCurveIdentifierExtensions.find_curve_identifier(skeleton: Skeleton, name: Name, curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
unreal.AnimationCurveIdentifierExtensions.get_curve_identifier(skeleton: Skeleton, name: Name, curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
unreal.AnimationCurveIdentifierExtensions.get_curve_identifiers(skeleton: Skeleton, curve_type: RawCurveTrackTypes) -> Array[AnimationCurveIdentifier]
unreal.AnimationCurveIdentifierExtensions.get_name(identifier: AnimationCurveIdentifier) -> Tuple[Name, AnimationCurveIdentifier]
unreal.AnimationCurveIdentifierExtensions.get_transform_child_curve_identifier(out_identifier: AnimationCurveIdentifier, channel: TransformCurveChannel, axis: VectorCurveChannel) -> Optional[AnimationCurveIdentifier]
unreal.AnimationCurveIdentifierExtensions.get_type(identifier: AnimationCurveIdentifier) -> Tuple[RawCurveTrackTypes, AnimationCurveIdentifier]
unreal.AnimationCurveIdentifierExtensions.is_valid(identifier: AnimationCurveIdentifier) -> Optional[AnimationCurveIdentifier]
unreal.AnimationCurveIdentifierExtensions.set_curve_identifier(out_identifier: AnimationCurveIdentifier, name: Name, curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

## `unreal.AnimationCurveMetaData(StructBase)`

```python
unreal.AnimationCurveMetaData.__init__() -> None
```

## `unreal.AnimationDataController(Interface)`

```python
unreal.AnimationDataController.add_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.add_bone_curve(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimationDataController.add_bone_track(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimationDataController.add_curve(curve_id: AnimationCurveIdentifier, curve_flags: int = 4, should_transact: bool = True) -> bool
unreal.AnimationDataController.close_bracket(should_transact: bool = True) -> None
unreal.AnimationDataController.duplicate_attribute(attribute_identifier: AnimationAttributeIdentifier, new_attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.duplicate_curve(copy_curve_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.find_or_add_curve_names_on_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimationDataController.get_model_interface() -> AnimationDataModel
unreal.AnimationDataController.insert_bone_track(bone_name: Name, desired_index: int, should_transact: bool = True) -> int
unreal.AnimationDataController.open_bracket(title: Text, should_transact: bool = True) -> None
unreal.AnimationDataController.remove_all_attributes(should_transact: bool = True) -> int
unreal.AnimationDataController.remove_all_attributes_for_bone(bone_name: Name, should_transact: bool = True) -> int
unreal.AnimationDataController.remove_all_bone_tracks(should_transact: bool = True) -> None
unreal.AnimationDataController.remove_all_curves_of_type(supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
unreal.AnimationDataController.remove_attribute(attribute_identifier: AnimationAttributeIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.remove_attribute_key(attribute_identifier: AnimationAttributeIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimationDataController.remove_bone_track(bone_name: Name, should_transact: bool = True) -> bool
unreal.AnimationDataController.remove_curve(curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.remove_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimationDataController.remove_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, should_transact: bool = True) -> bool
unreal.AnimationDataController.rename_curve(curve_to_rename_id: AnimationCurveIdentifier, new_curve_id: AnimationCurveIdentifier, should_transact: bool = True) -> bool
unreal.AnimationDataController.resize(length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimationDataController.resize_in_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimationDataController.resize_number_of_frames(new_length_in_frames: FrameNumber, t0: FrameNumber, t1: FrameNumber, should_transact: bool = True) -> None
unreal.AnimationDataController.resize_play_length(new_length: float, t0: float, t1: float, should_transact: bool = True) -> None
unreal.AnimationDataController.scale_curve(curve_id: AnimationCurveIdentifier, origin: float, factor: float, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_bone_track_keys(bone_name: Name, positional_keys: Array[Vector], rotational_keys: Array[Quat], scaling_keys: Array[Vector], should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_color(curve_id: AnimationCurveIdentifier, color: LinearColor, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_comment(curve_id: AnimationCurveIdentifier, comment: str = "/**\n\t* Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.\n\t* Currently changing curve comments is only supported for float curves.\n\t*\n\t* @param\tCurveId\t\t\t\tIdentifier of the curve to change the comment for\n\t* @param\tComment\t\t\t\tComment to which the curve is to be set\n\t* @param\tbShouldTransact\t\tWhether or not any undo-redo changes should be generated\n\t*\n\t* @return\tWhether or not the curve comment was successfully changed\n\t*/", should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_flag(curve_id: AnimationCurveIdentifier, flag: AnimAssetCurveFlags, state: bool = True, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_flags(curve_id: AnimationCurveIdentifier, flags: int, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_key(curve_id: AnimationCurveIdentifier, key: RichCurveKey, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_curve_keys(curve_id: AnimationCurveIdentifier, curve_keys: Array[RichCurveKey], should_transact: bool = True) -> bool
unreal.AnimationDataController.set_frame_rate(frame_rate: FrameRate, should_transact: bool = True) -> None
unreal.AnimationDataController.set_model(model: AnimationDataModel) -> None
unreal.AnimationDataController.set_number_of_frames(new_length_in_frames: FrameNumber, should_transact: bool = True) -> None
unreal.AnimationDataController.set_play_length(length: float, should_transact: bool = True) -> None
unreal.AnimationDataController.set_transform_curve_key(curve_id: AnimationCurveIdentifier, time: float, value: Transform, should_transact: bool = True) -> bool
unreal.AnimationDataController.set_transform_curve_keys(curve_id: AnimationCurveIdentifier, transform_values: Array[Transform], time_keys: Array[float], should_transact: bool = True) -> bool
unreal.AnimationDataController.update_curve_names_from_skeleton(skeleton: Skeleton, supported_curve_type: RawCurveTrackTypes, should_transact: bool = True) -> None
```

## `unreal.AnimationDataModel(Interface)`

```python
unreal.AnimationDataModel.get_animation_sequence() -> AnimSequence
unreal.AnimationDataModel.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
unreal.AnimationDataModel.get_bone_track_by_index(track_index: int) -> BoneAnimationTrack
unreal.AnimationDataModel.get_bone_track_by_name(track_name: Name) -> BoneAnimationTrack
unreal.AnimationDataModel.get_bone_track_index(track: BoneAnimationTrack) -> int
unreal.AnimationDataModel.get_bone_track_index_by_name(track_name: Name) -> int
unreal.AnimationDataModel.get_bone_track_names() -> Array[Name]
unreal.AnimationDataModel.get_frame_rate() -> FrameRate
unreal.AnimationDataModel.get_num_bone_tracks() -> int
unreal.AnimationDataModel.get_number_of_float_curves() -> int
unreal.AnimationDataModel.get_number_of_frames() -> int
unreal.AnimationDataModel.get_number_of_keys() -> int
unreal.AnimationDataModel.get_number_of_transform_curves() -> int
unreal.AnimationDataModel.get_play_length() -> float
unreal.AnimationDataModel.is_valid_bone_track_index(track_index: int) -> bool
unreal.AnimationDataModel.is_valid_bone_track_name(track_name: Name) -> bool
```

## `unreal.AnimationDataModelNotifiesExtensions(BlueprintFunctionLibrary)`

```python
unreal.AnimationDataModelNotifiesExtensions.copy_payload(payload: AnimDataModelNotifPayload, expected_struct: ScriptStruct, out_payload: EmptyPayload) -> EmptyPayload
unreal.AnimationDataModelNotifiesExtensions.get_payload(payload: AnimDataModelNotifPayload) -> EmptyPayload
```

## `unreal.AnimationGraph(EdGraph)`

```python
unreal.AnimationGraph.get_graph_nodes_of_class(node_class: Class, include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
```

## `unreal.AnimationLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimationLibrary.add_animation_notify_event(animation_sequence_base: AnimSequenceBase, notify_track_name: Name, start_time: float, notify_class: Class) -> AnimNotify
unreal.AnimationLibrary.add_animation_notify_event_object(animation_sequence_base: AnimSequenceBase, start_time: float, notify: AnimNotify, notify_track_name: Name) -> None
unreal.AnimationLibrary.add_animation_notify_state_event(animation_sequence_base: AnimSequenceBase, notify_track_name: Name, start_time: float, duration: float, notify_state_class: Class) -> AnimNotifyState
unreal.AnimationLibrary.add_animation_notify_state_event_object(animation_sequence_base: AnimSequenceBase, start_time: float, duration: float, notify_state: AnimNotifyState, notify_track_name: Name) -> None
unreal.AnimationLibrary.add_animation_notify_track(animation_sequence_base: AnimSequenceBase, notify_track_name: Name, track_color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000]) -> None
unreal.AnimationLibrary.add_animation_sync_marker(animation_sequence: AnimSequence, marker_name: Name, time: float, notify_track_name: Name) -> None
unreal.AnimationLibrary.add_curve(animation_sequence_base: AnimSequenceBase, curve_name: Name, curve_type: RawCurveTrackTypes = RawCurveTrackTypes.RCT_FLOAT, meta_data_curve: bool = False) -> None
unreal.AnimationLibrary.add_float_curve_key(animation_sequence_base: AnimSequenceBase, curve_name: Name, time: float, value: float) -> None
unreal.AnimationLibrary.add_float_curve_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name, times: Array[float], values: Array[float]) -> None
unreal.AnimationLibrary.add_meta_data(animation_asset: AnimationAsset, meta_data_class: Class) -> AnimMetaData
unreal.AnimationLibrary.add_meta_data_object(animation_asset: AnimationAsset, meta_data_object: AnimMetaData) -> None
unreal.AnimationLibrary.add_node_asset_override(anim_blueprint: AnimBlueprint, target: AnimationAsset, override: AnimationAsset, print_applied_overrides: bool = False) -> None
unreal.AnimationLibrary.add_transformation_curve_key(animation_sequence_base: AnimSequenceBase, curve_name: Name, time: float, transform: Transform) -> None
unreal.AnimationLibrary.add_transformation_curve_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name, times: Array[float], transforms: Array[Transform]) -> None
unreal.AnimationLibrary.add_vector_curve_key(animation_sequence_base: AnimSequenceBase, curve_name: Name, time: float, vector: Vector) -> None
unreal.AnimationLibrary.add_vector_curve_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name, times: Array[float], vectors: Array[Vector]) -> None
unreal.AnimationLibrary.add_virtual_bone(animation_sequence: AnimSequence, source_bone_name: Name, target_bone_name: Name) -> Name
unreal.AnimationLibrary.contains_meta_data_of_class(animation_asset: AnimationAsset, meta_data_class: Class) -> bool
unreal.AnimationLibrary.copy_anim_notifies_from_sequence(source_animation_sequence_base: AnimSequenceBase, destination_animation_sequence_base: AnimSequenceBase, delete_existing_notifies: bool = False) -> None
unreal.AnimationLibrary.copy_animation_curve_names_to_skeleton(old_skeleton: Skeleton, new_skeleton: Skeleton, sequence_base: AnimSequenceBase, curve_type: RawCurveTrackTypes) -> None
unreal.AnimationLibrary.does_bone_name_exist(animation_sequence: AnimSequence, bone_name: Name) -> bool
unreal.AnimationLibrary.does_curve_exist(animation_sequence_base: AnimSequenceBase, curve_name: Name, curve_type: RawCurveTrackTypes) -> bool
unreal.AnimationLibrary.evaluate_bone_timecode_and_slate_attributes_at_time(bone_name: Name, animation_sequence_base: AnimSequenceBase, eval_time: float) -> Optional[Tuple[QualifiedTime, str]]
unreal.AnimationLibrary.evaluate_root_bone_timecode_attributes_at_time(animation_sequence_base: AnimSequenceBase, eval_time: float) -> Optional[QualifiedTime]
unreal.AnimationLibrary.evaluate_root_bone_timecode_subframe_attribute_at_time(animation_sequence_base: AnimSequenceBase, eval_time: float) -> Optional[float]
unreal.AnimationLibrary.extract_root_track_transform(animation_sequence_base: AnimSequenceBase, time: float) -> Transform
unreal.AnimationLibrary.finalize_bone_animation(animation_sequence: AnimSequence) -> None
unreal.AnimationLibrary.find_bone_path_to_root(animation_sequence_base: AnimSequenceBase, bone_name: Name) -> Array[Name]
unreal.AnimationLibrary.get_additive_animation_type(animation_sequence: AnimSequence) -> AdditiveAnimationType
unreal.AnimationLibrary.get_additive_base_pose_type(animation_sequence: AnimSequence) -> AdditiveBasePoseType
unreal.AnimationLibrary.get_anim_notify_event_duration(notify_event: AnimNotifyEvent) -> float
unreal.AnimationLibrary.get_anim_notify_event_trigger_time(notify_event: AnimNotifyEvent) -> float
unreal.AnimationLibrary.get_animation_curve_names(animation_sequence_base: AnimSequenceBase, curve_type: RawCurveTrackTypes) -> Array[Name]
unreal.AnimationLibrary.get_animation_graphs(animation_blueprint: AnimBlueprint) -> Array[AnimationGraph]
unreal.AnimationLibrary.get_animation_interpolation_type(animation_sequence: AnimSequence) -> AnimInterpolationType
unreal.AnimationLibrary.get_animation_notify_event_names(animation_sequence_base: AnimSequenceBase) -> Array[Name]
unreal.AnimationLibrary.get_animation_notify_events(animation_sequence_base: AnimSequenceBase) -> Array[AnimNotifyEvent]
unreal.AnimationLibrary.get_animation_notify_events_for_track(animation_sequence_base: AnimSequenceBase, notify_track_name: Name) -> Array[AnimNotifyEvent]
unreal.AnimationLibrary.get_animation_notify_track_names(animation_sequence_base: AnimSequenceBase) -> Array[Name]
unreal.AnimationLibrary.get_animation_sync_markers(animation_sequence: AnimSequence) -> Array[AnimSyncMarker]
unreal.AnimationLibrary.get_animation_sync_markers_for_track(animation_sequence: AnimSequence, notify_track_name: Name) -> Array[AnimSyncMarker]
unreal.AnimationLibrary.get_animation_track_names(animation_sequence_base: AnimSequenceBase) -> Array[Name]
unreal.AnimationLibrary.get_bone_compression_settings(animation_sequence: AnimSequence) -> AnimBoneCompressionSettings
unreal.AnimationLibrary.get_bone_pose_for_frame(animation_sequence_base: AnimSequenceBase, bone_name: Name, frame: int, extract_root_motion: bool) -> Transform
unreal.AnimationLibrary.get_bone_pose_for_time(animation_sequence_base: AnimSequenceBase, bone_name: Name, time: float, extract_root_motion: bool) -> Transform
unreal.AnimationLibrary.get_bone_poses_for_frame(animation_sequence_base: AnimSequenceBase, bone_names: Array[Name], frame: int, extract_root_motion: bool, preview_mesh: SkeletalMesh = None) -> Array[Transform]
unreal.AnimationLibrary.get_bone_poses_for_time(animation_sequence_base: AnimSequenceBase, bone_names: Array[Name], time: float, extract_root_motion: bool, preview_mesh: SkeletalMesh = None) -> Array[Transform]
unreal.AnimationLibrary.get_curve_compression_settings(animation_sequence: AnimSequence) -> AnimCurveCompressionSettings
unreal.AnimationLibrary.get_float_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name) -> Tuple[Array[float], Array[float]]
unreal.AnimationLibrary.get_float_value_at_time(animation_sequence_base: AnimSequenceBase, curve_name: Name, time: float) -> float
unreal.AnimationLibrary.get_frame_at_time(animation_sequence_base: AnimSequenceBase, time: float) -> int
unreal.AnimationLibrary.get_meta_data(animation_asset: AnimationAsset) -> Array[AnimMetaData]
unreal.AnimationLibrary.get_meta_data_of_class(animation_asset: AnimationAsset, meta_data_class: Class) -> Array[AnimMetaData]
unreal.AnimationLibrary.get_montage_slot_names(animation_montage: AnimMontage) -> Array[Name]
unreal.AnimationLibrary.get_nodes_of_class(animation_blueprint: AnimBlueprint, node_class: Class, include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
unreal.AnimationLibrary.get_num_frames(animation_sequence_base: AnimSequenceBase) -> int
unreal.AnimationLibrary.get_num_keys(animation_sequence_base: AnimSequenceBase) -> int
unreal.AnimationLibrary.get_rate_scale(animation_sequence_base: AnimSequenceBase) -> float
unreal.AnimationLibrary.get_raw_track_data(animation_sequence_base: AnimSequenceBase, track_name: Name) -> Tuple[Array[Vector], Array[Quat], Array[Vector]]
unreal.AnimationLibrary.get_raw_track_position_data(animation_sequence_base: AnimSequenceBase, track_name: Name) -> Array[Vector]
unreal.AnimationLibrary.get_raw_track_rotation_data(animation_sequence_base: AnimSequenceBase, track_name: Name) -> Array[Quat]
unreal.AnimationLibrary.get_raw_track_scale_data(animation_sequence_base: AnimSequenceBase, track_name: Name) -> Array[Vector]
unreal.AnimationLibrary.get_root_motion_lock_type(animation_sequence: AnimSequence) -> RootMotionRootLock
unreal.AnimationLibrary.get_sequence_length(animation_sequence_base: AnimSequenceBase) -> float
unreal.AnimationLibrary.get_time_at_frame(animation_sequence_base: AnimSequenceBase, frame: int) -> float
unreal.AnimationLibrary.get_transformation_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name) -> Tuple[Array[float], Array[Transform]]
unreal.AnimationLibrary.get_unique_marker_names(animation_sequence: AnimSequence) -> Array[Name]
unreal.AnimationLibrary.get_variable_frame_stripping_settings(animation_sequence: AnimSequence) -> VariableFrameStrippingSettings
unreal.AnimationLibrary.get_vector_keys(animation_sequence_base: AnimSequenceBase, curve_name: Name) -> Tuple[Array[float], Array[Vector]]
unreal.AnimationLibrary.is_root_motion_enabled(animation_sequence: AnimSequence) -> bool
unreal.AnimationLibrary.is_root_motion_lock_forced(animation_sequence: AnimSequence) -> bool
unreal.AnimationLibrary.is_valid_anim_notify_track_name(animation_sequence_base: AnimSequenceBase, notify_track_name: Name) -> bool
unreal.AnimationLibrary.is_valid_animation_sync_marker_name(animation_sequence: AnimSequence, marker_name: Name) -> bool
unreal.AnimationLibrary.is_valid_raw_animation_track_name(animation_sequence_base: AnimSequenceBase, track_name: Name) -> bool
unreal.AnimationLibrary.is_valid_time(animation_sequence_base: AnimSequenceBase, time: float) -> bool
unreal.AnimationLibrary.remove_all_animation_notify_tracks(animation_sequence_base: AnimSequenceBase) -> None
unreal.AnimationLibrary.remove_all_animation_sync_markers(animation_sequence: AnimSequence) -> None
unreal.AnimationLibrary.remove_all_bone_animation(animation_sequence: AnimSequence) -> None
unreal.AnimationLibrary.remove_all_curve_data(animation_sequence_base: AnimSequenceBase) -> None
unreal.AnimationLibrary.remove_all_meta_data(animation_asset: AnimationAsset) -> None
unreal.AnimationLibrary.remove_all_virtual_bones(animation_sequence: AnimSequence) -> None
unreal.AnimationLibrary.remove_animation_notify_events_by_name(animation_sequence_base: AnimSequenceBase, notify_name: Name) -> int
unreal.AnimationLibrary.remove_animation_notify_events_by_track(animation_sequence_base: AnimSequenceBase, notify_track_name: Name) -> int
unreal.AnimationLibrary.remove_animation_notify_track(animation_sequence_base: AnimSequenceBase, notify_track_name: Name) -> None
unreal.AnimationLibrary.remove_animation_sync_markers_by_name(animation_sequence: AnimSequence, marker_name: Name) -> int
unreal.AnimationLibrary.remove_animation_sync_markers_by_track(animation_sequence: AnimSequence, notify_track_name: Name) -> int
unreal.AnimationLibrary.remove_bone_animation(animation_sequence: AnimSequence, bone_name: Name, include_children: bool = True, finalize: bool = True) -> None
unreal.AnimationLibrary.remove_curve(animation_sequence_base: AnimSequenceBase, curve_name: Name, remove_name_from_skeleton: bool = False) -> None
unreal.AnimationLibrary.remove_meta_data(animation_asset: AnimationAsset, meta_data_object: AnimMetaData) -> None
unreal.AnimationLibrary.remove_meta_data_of_class(animation_asset: AnimationAsset, meta_data_class: Class) -> None
unreal.AnimationLibrary.remove_virtual_bone(animation_sequence: AnimSequence, virtual_bone_name: Name) -> None
unreal.AnimationLibrary.remove_virtual_bones(animation_sequence: AnimSequence, virtual_bone_names: Array[Name]) -> None
unreal.AnimationLibrary.replace_anim_notifies(animation_sequence_base: AnimSequenceBase, old_notify_class: Class, new_notify_class: Class, on_notify_replaced: OnNotifyReplaced) -> None
unreal.AnimationLibrary.replace_anim_notify_states(animation_sequence_base: AnimSequenceBase, old_notify_class: Class, new_notify_class: Class, on_notify_state_replaced: OnNotifyStateReplaced) -> None
unreal.AnimationLibrary.set_additive_animation_type(animation_sequence: AnimSequence, additive_animation_type: AdditiveAnimationType) -> None
unreal.AnimationLibrary.set_additive_base_pose_type(animation_sequence: AnimSequence, additive_base_pose_type: AdditiveBasePoseType) -> None
unreal.AnimationLibrary.set_animation_interpolation_type(animation_sequence: AnimSequence, interpolation_type: AnimInterpolationType) -> None
unreal.AnimationLibrary.set_bone_compression_settings(animation_sequence: AnimSequence, compression_settings: AnimBoneCompressionSettings) -> None
unreal.AnimationLibrary.set_curve_compression_settings(animation_sequence: AnimSequence, compression_settings: AnimCurveCompressionSettings) -> None
unreal.AnimationLibrary.set_is_root_motion_lock_forced(animation_sequence: AnimSequence, forced: bool) -> None
unreal.AnimationLibrary.set_rate_scale(animation_sequence_base: AnimSequenceBase, rate_scale: float) -> None
unreal.AnimationLibrary.set_root_motion_enabled(animation_sequence: AnimSequence, enabled: bool) -> None
unreal.AnimationLibrary.set_root_motion_lock_type(animation_sequence: AnimSequence, root_motion_lock_type: RootMotionRootLock) -> None
unreal.AnimationLibrary.set_variable_frame_stripping_settings(animation_sequence: AnimSequence, variable_frame_stripping_settings: VariableFrameStrippingSettings) -> None
```

## `unreal.AnimationModifier(Object)`

```python
unreal.AnimationModifier.on_apply(animation_sequence: AnimSequence) -> None
unreal.AnimationModifier.on_revert(animation_sequence: AnimSequence) -> None
```

## `unreal.AnimationNode_TwoWayBlend(AnimNode_TwoWayBlend)`

```python
unreal.AnimationNode_TwoWayBlend.__init__(a: PoseLink = [], b: PoseLink = [], alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT, alpha_bool_enabled: bool = False, alpha: float = 0.000000, alpha_scale_bias: InputScaleBias = [1.000000, 0.000000], alpha_bool_blend: InputAlphaBoolBlend = [0.000000, 0.000000, AlphaBlendOption.LINEAR, None], alpha_curve_name: Name = "None", alpha_scale_bias_clamp: InputScaleBiasClamp = [False, False, False, [0.000000, 1.000000], [0.000000, 1.000000], 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000]) -> None
```

## `unreal.AnimationSequenceBrowserContextMenuContext(Object)`

```python
unreal.AnimationSequenceBrowserContextMenuContext.get_selected_objects() -> Array[Object]
```

## `unreal.AnimationSequencerDataModel(MovieSceneSequence)`

```python
unreal.AnimationSequencerDataModel.get_animation_sequence() -> AnimSequence
unreal.AnimationSequencerDataModel.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
unreal.AnimationSequencerDataModel.get_bone_track_by_index(track_index: int) -> BoneAnimationTrack
unreal.AnimationSequencerDataModel.get_bone_track_by_name(track_name: Name) -> BoneAnimationTrack
unreal.AnimationSequencerDataModel.get_bone_track_index(track: BoneAnimationTrack) -> int
unreal.AnimationSequencerDataModel.get_bone_track_index_by_name(track_name: Name) -> int
unreal.AnimationSequencerDataModel.get_bone_track_names() -> Array[Name]
unreal.AnimationSequencerDataModel.get_frame_rate() -> FrameRate
unreal.AnimationSequencerDataModel.get_num_bone_tracks() -> int
unreal.AnimationSequencerDataModel.get_number_of_float_curves() -> int
unreal.AnimationSequencerDataModel.get_number_of_frames() -> int
unreal.AnimationSequencerDataModel.get_number_of_keys() -> int
unreal.AnimationSequencerDataModel.get_number_of_transform_curves() -> int
unreal.AnimationSequencerDataModel.get_play_length() -> float
unreal.AnimationSequencerDataModel.is_valid_bone_track_index(track_index: int) -> bool
unreal.AnimationSequencerDataModel.is_valid_bone_track_name(track_name: Name) -> bool
unreal.AnimationSequencerDataModel.modified_event(value: AnimDataModelModifiedDynamicEvent) -> None
```

## `unreal.AnimationSettings(DeveloperSettings)`

```python
unreal.AnimationSettings.get_bone_custom_attribute_names_to_import() -> Array[str]
unreal.AnimationSettings.raise_max_error_to_existing(value: bool) -> None
```

## `unreal.AnimationSetup(StructBase)`

```python
unreal.AnimationSetup.__init__() -> None
```

## `unreal.AnimationSharingManager(Object)`

```python
unreal.AnimationSharingManager.animation_sharing_enabled() -> bool
unreal.AnimationSharingManager.create_animation_sharing_manager(world_context_object: Object, setup: AnimationSharingSetup) -> bool
unreal.AnimationSharingManager.get_animation_sharing_manager(world_context_object: Object) -> AnimationSharingManager
unreal.AnimationSharingManager.register_actor_with_skeleton_bp(actor: Actor, sharing_skeleton: Skeleton) -> None
```

## `unreal.AnimationSharingScalability(StructBase)`

```python
unreal.AnimationSharingScalability.__init__() -> None
```

## `unreal.AnimationSharingStateProcessor(Object)`

```python
unreal.AnimationSharingStateProcessor.get_animation_state_enum() -> Enum
unreal.AnimationSharingStateProcessor.process_actor_state(actor: Actor, current_state: int, on_demand_state: int) -> Tuple[int, bool]
```

## `unreal.AnimationStateEntry(StructBase)`

```python
unreal.AnimationStateEntry.__init__() -> None
```

## `unreal.AnimationStateMachineLibrary(BlueprintFunctionLibrary)`

```python
unreal.AnimationStateMachineLibrary.convert_to_animation_state_machine(node: AnimNodeReference) -> Tuple[AnimationStateMachineReference, AnimNodeReferenceConversionResult]
unreal.AnimationStateMachineLibrary.convert_to_animation_state_machine_pure(node: AnimNodeReference) -> Tuple[AnimationStateMachineReference, bool]
unreal.AnimationStateMachineLibrary.convert_to_animation_state_result(node: AnimNodeReference) -> Tuple[AnimationStateResultReference, AnimNodeReferenceConversionResult]
unreal.AnimationStateMachineLibrary.convert_to_animation_state_result_pure(node: AnimNodeReference) -> Tuple[AnimationStateResultReference, bool]
unreal.AnimationStateMachineLibrary.get_relevant_anim_time_remaining(update_context: AnimUpdateContext, node: AnimationStateResultReference) -> float
unreal.AnimationStateMachineLibrary.get_relevant_anim_time_remaining_fraction(update_context: AnimUpdateContext, node: AnimationStateResultReference) -> float
unreal.AnimationStateMachineLibrary.get_state(update_context: AnimUpdateContext, node: AnimationStateMachineReference) -> Name
unreal.AnimationStateMachineLibrary.is_state_blending_in(update_context: AnimUpdateContext, node: AnimationStateResultReference) -> bool
unreal.AnimationStateMachineLibrary.is_state_blending_out(update_context: AnimUpdateContext, node: AnimationStateResultReference) -> bool
unreal.AnimationStateMachineLibrary.set_state(update_context: AnimUpdateContext, node: AnimationStateMachineReference, target_state: Name, duration: float, blend_type: TransitionLogicType, blend_profile: BlendProfile, alpha_blend_option: AlphaBlendOption, custom_blend_curve: CurveFloat) -> None
```

## `unreal.AnimationStateMachineReference(AnimNodeReference)`

```python
unreal.AnimationStateMachineReference.__init__() -> None
```

## `unreal.AnimationStateResultReference(AnimNodeReference)`

```python
unreal.AnimationStateResultReference.__init__() -> None
```

## `unreal.AnimationTrackAddedPayload(AnimationTrackPayload)`

```python
unreal.AnimationTrackAddedPayload.__init__(name: Name = "None", track_index: int = 0) -> None
unreal.AnimationTrackAddedPayload.track_index() -> int
```

## `unreal.AnimationTrackPayload(EmptyPayload)`

```python
unreal.AnimationTrackPayload.__init__(name: Name = "None") -> None
unreal.AnimationTrackPayload.name() -> Name
```

## `unreal.BakingAnimationKeySettings(StructBase)`

```python
unreal.BakingAnimationKeySettings.__init__(start_frame: FrameNumber = [0], end_frame: FrameNumber = [0], baking_key_settings: BakingKeySettings = BakingKeySettings.KEYS_ONLY, frame_increment: int = 0, reduce_keys: bool = False, tolerance: float = 0.000000) -> None
unreal.BakingAnimationKeySettings.baking_key_settings(value: BakingKeySettings) -> None
unreal.BakingAnimationKeySettings.end_frame(value: FrameNumber) -> None
unreal.BakingAnimationKeySettings.frame_increment(value: int) -> None
unreal.BakingAnimationKeySettings.reduce_keys(value: bool) -> None
unreal.BakingAnimationKeySettings.start_frame(value: FrameNumber) -> None
unreal.BakingAnimationKeySettings.tolerance(value: float) -> None
```

## `unreal.BlendBoneByChannelEntry(StructBase)`

```python
unreal.BlendBoneByChannelEntry.__init__() -> None
```

## `unreal.BlueprintCameraPose(StructBase)`

```python
unreal.BlueprintCameraPose.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], target_distance: float = 0.000000, field_of_view: float = 0.000000, focal_length: float = 0.000000, aperture: float = 0.000000, shutter_speed: float = 0.000000, focus_distance: float = 0.000000, sensor_width: float = 0.000000, sensor_height: float = 0.000000, iso: float = 0.000000, squeeze_factor: float = 0.000000, diaphragm_blade_count: int = 0, near_clipping_plane: float = 0.000000, far_clipping_plane: float = 0.000000, enable_physical_camera: bool = False, constrain_aspect_ratio: bool = False, aspect_ratio_axis_constraint: AspectRatioAxisConstraint = AspectRatioAxisConstraint.ASPECT_RATIO_MAINTAIN_YFOV) -> None
unreal.BlueprintCameraPose.aperture(value: float) -> None
unreal.BlueprintCameraPose.aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
unreal.BlueprintCameraPose.constrain_aspect_ratio(value: bool) -> None
unreal.BlueprintCameraPose.diaphragm_blade_count(value: int) -> None
unreal.BlueprintCameraPose.enable_physical_camera(value: bool) -> None
unreal.BlueprintCameraPose.far_clipping_plane(value: float) -> None
unreal.BlueprintCameraPose.field_of_view(value: float) -> None
unreal.BlueprintCameraPose.focal_length(value: float) -> None
unreal.BlueprintCameraPose.focus_distance(value: float) -> None
unreal.BlueprintCameraPose.iso(value: float) -> None
unreal.BlueprintCameraPose.location(value: Vector) -> None
unreal.BlueprintCameraPose.near_clipping_plane(value: float) -> None
unreal.BlueprintCameraPose.rotation(value: Rotator) -> None
unreal.BlueprintCameraPose.sensor_height(value: float) -> None
unreal.BlueprintCameraPose.sensor_width(value: float) -> None
unreal.BlueprintCameraPose.shutter_speed(value: float) -> None
unreal.BlueprintCameraPose.squeeze_factor(value: float) -> None
unreal.BlueprintCameraPose.target_distance(value: float) -> None
```

## `unreal.BlueprintCameraPoseFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.BlueprintCameraPoseFunctionLibrary.get_aim_dir(camera_pose: BlueprintCameraPose) -> Vector
unreal.BlueprintCameraPoseFunctionLibrary.get_aim_ray(camera_pose: BlueprintCameraPose) -> Ray
unreal.BlueprintCameraPoseFunctionLibrary.get_effective_field_of_view(camera_pose: BlueprintCameraPose) -> float
unreal.BlueprintCameraPoseFunctionLibrary.get_field_of_view(camera_pose: BlueprintCameraPose) -> float
unreal.BlueprintCameraPoseFunctionLibrary.get_focal_length(camera_pose: BlueprintCameraPose) -> float
unreal.BlueprintCameraPoseFunctionLibrary.get_location(camera_pose: BlueprintCameraPose) -> Vector
unreal.BlueprintCameraPoseFunctionLibrary.get_rotation(camera_pose: BlueprintCameraPose) -> Rotator
unreal.BlueprintCameraPoseFunctionLibrary.get_sensor_aspect_ratio(camera_pose: BlueprintCameraPose) -> float
unreal.BlueprintCameraPoseFunctionLibrary.get_target(camera_pose: BlueprintCameraPose) -> Vector
unreal.BlueprintCameraPoseFunctionLibrary.get_target_at_distance(camera_pose: BlueprintCameraPose, target_distance: float) -> Vector
unreal.BlueprintCameraPoseFunctionLibrary.get_target_distance(camera_pose: BlueprintCameraPose) -> float
unreal.BlueprintCameraPoseFunctionLibrary.get_transform(camera_pose: BlueprintCameraPose) -> Transform
unreal.BlueprintCameraPoseFunctionLibrary.make_camera_pose_from_camera_component(camera_component: CameraComponent) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.make_camera_pose_from_cine_camera_component(camera_component: CineCameraComponent) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_field_of_view(camera_pose: BlueprintCameraPose, field_of_view: float) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_focal_length(camera_pose: BlueprintCameraPose, focal_length: float) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_location(camera_pose: BlueprintCameraPose, location: Vector) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_rotation(camera_pose: BlueprintCameraPose, rotation: Rotator) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_target_distance(camera_pose: BlueprintCameraPose, target_distance: float) -> BlueprintCameraPose
unreal.BlueprintCameraPoseFunctionLibrary.set_transform(camera_pose: BlueprintCameraPose, transform: Transform) -> BlueprintCameraPose
```

## `unreal.BoneAnimationTrack(StructBase)`

```python
unreal.BoneAnimationTrack.__init__(internal_track_data: RawAnimSequenceTrack = [], bone_tree_index: int = 0, name: Name = "None") -> None
unreal.BoneAnimationTrack.bone_tree_index() -> int
unreal.BoneAnimationTrack.internal_track_data() -> RawAnimSequenceTrack
unreal.BoneAnimationTrack.name() -> Name
```

## `unreal.BoneChain(StructBase)`

```python
unreal.BoneChain.__init__(chain_name: Name = "None", ik_goal_name: Name = "None") -> None
unreal.BoneChain.chain_name(value: Name) -> None
unreal.BoneChain.ik_goal_name() -> Name
```

## `unreal.BoneFilter(StructBase)`

```python
unreal.BoneFilter.__init__() -> None
```

## `unreal.BoneID(ElementID)`

```python
unreal.BoneID.__init__(id_value: int = 0) -> None
```

## `unreal.BoneMirrorInfo(StructBase)`

```python
unreal.BoneMirrorInfo.__init__() -> None
```

## `unreal.BoneNode(StructBase)`

```python
unreal.BoneNode.__init__() -> None
```

## `unreal.BoneReference(StructBase)`

```python
unreal.BoneReference.__init__() -> None
```

## `unreal.BoneReferencePair(StructBase)`

```python
unreal.BoneReferencePair.__init__() -> None
```

## `unreal.BoneSocketTarget(StructBase)`

```python
unreal.BoneSocketTarget.__init__() -> None
```

## `unreal.CachedAnimAssetPlayerData(StructBase)`

```python
unreal.CachedAnimAssetPlayerData.__init__(state_machine_name: Name = "None", state_name: Name = "None") -> None
unreal.CachedAnimAssetPlayerData.state_machine_name() -> Name
unreal.CachedAnimAssetPlayerData.state_name() -> Name
```

## `unreal.CachedAnimDataLibrary(BlueprintFunctionLibrary)`

```python
unreal.CachedAnimDataLibrary.state_machine_get_asset_player_time(anim_instance: AnimInstance, cached_anim_asset_player_data: CachedAnimAssetPlayerData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_asset_player_time_ratio(anim_instance: AnimInstance, cached_anim_asset_player_data: CachedAnimAssetPlayerData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_crossfade_duration(anim_instance: AnimInstance, cached_anim_transition_data: CachedAnimTransitionData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_global_weight(anim_instance: AnimInstance, cached_anim_state_data: CachedAnimStateData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_local_weight(anim_instance: AnimInstance, cached_anim_state_data: CachedAnimStateData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time(anim_instance: AnimInstance, cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time_remaining(anim_instance: AnimInstance, cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time_remaining_fraction(anim_instance: AnimInstance, cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
unreal.CachedAnimDataLibrary.state_machine_get_total_weight(anim_instance: AnimInstance, cached_anim_state_array: CachedAnimStateArray) -> float
unreal.CachedAnimDataLibrary.state_machine_is_full_weight(anim_instance: AnimInstance, cached_anim_state_array: CachedAnimStateArray) -> bool
unreal.CachedAnimDataLibrary.state_machine_is_relevant(anim_instance: AnimInstance, cached_anim_state_array: CachedAnimStateArray) -> bool
unreal.CachedAnimDataLibrary.state_machine_is_state_relevant(anim_instance: AnimInstance, cached_anim_state_data: CachedAnimStateData) -> bool
```

## `unreal.CachedAnimRelevancyData(StructBase)`

```python
unreal.CachedAnimRelevancyData.__init__(state_machine_name: Name = "None", state_name: Name = "None") -> None
unreal.CachedAnimRelevancyData.state_machine_name() -> Name
unreal.CachedAnimRelevancyData.state_name() -> Name
```

## `unreal.CachedAnimStateArray(StructBase)`

```python
unreal.CachedAnimStateArray.__init__(states: Array[CachedAnimStateData] = []) -> None
unreal.CachedAnimStateArray.states() -> Array[CachedAnimStateData]
```

## `unreal.CachedAnimStateData(StructBase)`

```python
unreal.CachedAnimStateData.__init__(state_machine_name: Name = "None", state_name: Name = "None") -> None
unreal.CachedAnimStateData.state_machine_name() -> Name
unreal.CachedAnimStateData.state_name() -> Name
```

## `unreal.CachedAnimTransitionData(StructBase)`

```python
unreal.CachedAnimTransitionData.__init__(state_machine_name: Name = "None", from_state_name: Name = "None", to_state_name: Name = "None") -> None
unreal.CachedAnimTransitionData.from_state_name() -> Name
unreal.CachedAnimTransitionData.state_machine_name() -> Name
unreal.CachedAnimTransitionData.to_state_name() -> Name
```

## `unreal.CameraAnimationCameraModifier(CameraModifier)`

```python
unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier(world_context_object: Object, player_index: int) -> CameraAnimationCameraModifier
unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier_from_id(world_context_object: Object, controller_id: int) -> CameraAnimationCameraModifier
unreal.CameraAnimationCameraModifier.get_camera_animation_camera_modifier_from_player_controller(player_controller: PlayerController) -> CameraAnimationCameraModifier
unreal.CameraAnimationCameraModifier.is_camera_animation_active(handle: CameraAnimationHandle) -> bool
unreal.CameraAnimationCameraModifier.play_camera_animation(sequence: CameraAnimationSequence, params: CameraAnimationParams) -> CameraAnimationHandle
unreal.CameraAnimationCameraModifier.stop_all_camera_animations(immediate: bool = False) -> None
unreal.CameraAnimationCameraModifier.stop_all_camera_animations_of(sequence: CameraAnimationSequence, immediate: bool = False) -> None
unreal.CameraAnimationCameraModifier.stop_camera_animation(handle: CameraAnimationHandle, immediate: bool = False) -> None
```

## `unreal.CameraAnimationHandle(StructBase)`

```python
unreal.CameraAnimationHandle.__init__() -> None
```

## `unreal.CameraAnimationParams(StructBase)`

```python
unreal.CameraAnimationParams.__init__(play_rate: float = 0.000000, scale: float = 0.000000, ease_in_type: CameraAnimationEasingType = CameraAnimationEasingType.LINEAR, ease_in_duration: float = 0.000000, ease_out_type: CameraAnimationEasingType = CameraAnimationEasingType.LINEAR, ease_out_duration: float = 0.000000, loop: bool = False, start_offset: int = 0, random_start_time: bool = False, duration_override: float = 0.000000, play_space: CameraAnimationPlaySpace = CameraAnimationPlaySpace.CAMERA_LOCAL, user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.CameraAnimationParams.duration_override(value: float) -> None
unreal.CameraAnimationParams.ease_in_duration(value: float) -> None
unreal.CameraAnimationParams.ease_in_type(value: CameraAnimationEasingType) -> None
unreal.CameraAnimationParams.ease_out_duration(value: float) -> None
unreal.CameraAnimationParams.ease_out_type(value: CameraAnimationEasingType) -> None
unreal.CameraAnimationParams.loop(value: bool) -> None
unreal.CameraAnimationParams.play_rate(value: float) -> None
unreal.CameraAnimationParams.play_space(value: CameraAnimationPlaySpace) -> None
unreal.CameraAnimationParams.random_start_time(value: bool) -> None
unreal.CameraAnimationParams.scale(value: float) -> None
unreal.CameraAnimationParams.start_offset(value: int) -> None
unreal.CameraAnimationParams.user_play_space_rot(value: Rotator) -> None
```

## `unreal.ComponentSpacePose(StructBase)`

```python
unreal.ComponentSpacePose.__init__(transforms: Array[Transform] = [], names: Array[Name] = []) -> None
unreal.ComponentSpacePose.names(value: Array[Name]) -> None
unreal.ComponentSpacePose.transforms(value: Array[Transform]) -> None
```

## `unreal.ComponentSpacePoseLink(PoseLinkBase)`

```python
unreal.ComponentSpacePoseLink.__init__() -> None
```

## `unreal.ControlRig(RigVMHost)`

```python
unreal.ControlRig.add_physics_solver(name: Name, setup_undo: bool = False, print_python_command: bool = False) -> RigPhysicsSolverID
unreal.ControlRig.clear_control_selection() -> bool
unreal.ControlRig.create_transformable_control_handle(control_name: Name) -> TransformableControlHandle
unreal.ControlRig.current_control_selection() -> Array[Name]
unreal.ControlRig.find_control_rigs(outer: Object, optional_class: Class) -> Array[ControlRig]
unreal.ControlRig.get_hierarchy() -> RigHierarchy
unreal.ControlRig.get_hosting_actor() -> Actor
unreal.ControlRig.is_control_selected(control_name: Name) -> bool
unreal.ControlRig.on_control_selected_bp(value: OnControlSelectedBP) -> None
unreal.ControlRig.request_construction() -> None
unreal.ControlRig.select_control(control_name: Name, select: bool = True) -> None
unreal.ControlRig.supports_backwards_solve() -> bool
```

## `unreal.ControlRigAnimNodeEventName(StructBase)`

```python
unreal.ControlRigAnimNodeEventName.__init__() -> None
```

## `unreal.ControlRigBlueprint(RigVMBlueprint)`

```python
unreal.ControlRigBlueprint.can_turn_into_standalone_rig() -> bool
unreal.ControlRigBlueprint.convert_hierarchy_elements_to_spawner_nodes(hierarchy: RigHierarchy, keys: Array[RigElementKey], remove_elements: bool = True) -> Array[RigVMNode]
unreal.ControlRigBlueprint.create_control_rig() -> ControlRig
unreal.ControlRigBlueprint.find_references_to_module() -> Array[ModuleReferenceData]
unreal.ControlRigBlueprint.get_control_rig_class() -> Class
unreal.ControlRigBlueprint.get_currently_open_rig_blueprints() -> Array[ControlRigBlueprint]
unreal.ControlRigBlueprint.get_debugged_control_rig() -> ControlRig
unreal.ControlRigBlueprint.get_hierarchy_controller() -> RigHierarchyController
unreal.ControlRigBlueprint.get_modular_rig_controller() -> ModularRigController
unreal.ControlRigBlueprint.get_preview_mesh() -> SkeletalMesh
unreal.ControlRigBlueprint.get_rig_module_icon() -> Texture2D
unreal.ControlRigBlueprint.hierarchy() -> RigHierarchy
unreal.ControlRigBlueprint.is_control_rig_module() -> bool
unreal.ControlRigBlueprint.modular_rig_model() -> ModularRigModel
unreal.ControlRigBlueprint.recompile_modular_rig() -> None
unreal.ControlRigBlueprint.set_preview_mesh(preview_mesh: SkeletalMesh, mark_as_dirty: bool = True) -> None
unreal.ControlRigBlueprint.turn_into_control_rig_module() -> bool
unreal.ControlRigBlueprint.turn_into_standalone_rig() -> bool
```

## `unreal.ControlRigBlueprintLibrary(RigVMBlueprintLibrary)`

```python
unreal.ControlRigBlueprintLibrary.cast_to_control_rig_blueprint(object: Object) -> Tuple[CastToControlRigBlueprintCases, ControlRigBlueprint]
unreal.ControlRigBlueprintLibrary.get_available_rig_modules() -> Array[RigModuleDescription]
unreal.ControlRigBlueprintLibrary.get_available_rig_units() -> Array[Struct]
unreal.ControlRigBlueprintLibrary.get_currently_open_rig_blueprints() -> Array[ControlRigBlueprint]
unreal.ControlRigBlueprintLibrary.get_hierarchy(rig_blueprint: ControlRigBlueprint) -> RigHierarchy
unreal.ControlRigBlueprintLibrary.get_hierarchy_controller(rig_blueprint: ControlRigBlueprint) -> RigHierarchyController
unreal.ControlRigBlueprintLibrary.get_preview_mesh(rig_blueprint: ControlRigBlueprint) -> SkeletalMesh
unreal.ControlRigBlueprintLibrary.request_control_rig_init(rig_blueprint: ControlRigBlueprint) -> None
unreal.ControlRigBlueprintLibrary.set_preview_mesh(rig_blueprint: ControlRigBlueprint, preview_mesh: SkeletalMesh, mark_as_dirty: bool = True) -> None
unreal.ControlRigBlueprintLibrary.setup_all_editor_menus() -> None
```

## `unreal.ControlRigComponent(PrimitiveComponent)`

```python
unreal.ControlRigComponent.add_mapped_complete_skeletal_mesh(skeletal_mesh_component: SkeletalMeshComponent, direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection.OUTPUT) -> None
unreal.ControlRigComponent.add_mapped_components(components: Array[ControlRigComponentMappedComponent]) -> None
unreal.ControlRigComponent.add_mapped_elements(new_mapped_elements: Array[ControlRigComponentMappedElement]) -> None
unreal.ControlRigComponent.add_mapped_skeletal_mesh(skeletal_mesh_component: SkeletalMeshComponent, bones: Array[ControlRigComponentMappedBone], curves: Array[ControlRigComponentMappedCurve], direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection.OUTPUT) -> None
unreal.ControlRigComponent.can_execute() -> bool
unreal.ControlRigComponent.clear_mapped_elements() -> None
unreal.ControlRigComponent.control_rig_class(value: Class) -> None
unreal.ControlRigComponent.does_element_exist(name: Name, element_type: RigElementType = RigElementType.BONE) -> bool
unreal.ControlRigComponent.get_absolute_time() -> float
unreal.ControlRigComponent.get_bone_transform(bone_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.get_control_bool(control_name: Name) -> bool
unreal.ControlRigComponent.get_control_float(control_name: Name) -> float
unreal.ControlRigComponent.get_control_int(control_name: Name) -> int
unreal.ControlRigComponent.get_control_offset(control_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.get_control_position(control_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> Vector
unreal.ControlRigComponent.get_control_rig() -> ControlRig
unreal.ControlRigComponent.get_control_rotator(control_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> Rotator
unreal.ControlRigComponent.get_control_scale(control_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> Vector
unreal.ControlRigComponent.get_control_transform(control_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.get_control_vector2d(control_name: Name) -> Vector2D
unreal.ControlRigComponent.get_element_names(element_type: RigElementType = RigElementType.BONE) -> Array[Name]
unreal.ControlRigComponent.get_initial_bone_transform(bone_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.get_initial_space_transform(space_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.get_space_transform(space_name: Name, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> Transform
unreal.ControlRigComponent.initialize() -> None
unreal.ControlRigComponent.on_post_construction(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_post_construction_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_post_forwards_solve(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_post_forwards_solve_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_post_initialize(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_post_initialize_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_post_setup_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_post_update_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_pre_construction(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_pre_construction_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_pre_forwards_solve(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_pre_forwards_solve_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_pre_initialize(component: ControlRigComponent) -> None
unreal.ControlRigComponent.on_pre_initialize_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_pre_setup_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.on_pre_update_delegate(value: ControlRigComponentDelegate) -> None
unreal.ControlRigComponent.set_bone_initial_transforms_from_skeletal_mesh(skeletal_mesh: SkeletalMesh) -> None
unreal.ControlRigComponent.set_bone_transform(bone_name: Name, transform: Transform, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE, weight: float = 1.000000, propagate_to_children: bool = True) -> None
unreal.ControlRigComponent.set_control_bool(control_name: Name, value: bool) -> None
unreal.ControlRigComponent.set_control_float(control_name: Name, value: float) -> None
unreal.ControlRigComponent.set_control_int(control_name: Name, value: int) -> None
unreal.ControlRigComponent.set_control_offset(control_name: Name, offset_transform: Transform, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> None
unreal.ControlRigComponent.set_control_position(control_name: Name, value: Vector, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> None
unreal.ControlRigComponent.set_control_rig_class(control_rig_class: Class) -> None
unreal.ControlRigComponent.set_control_rotator(control_name: Name, value: Rotator, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> None
unreal.ControlRigComponent.set_control_scale(control_name: Name, value: Vector, space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE) -> None
unreal.ControlRigComponent.set_control_transform(control_name: Name, value: Transform, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> None
unreal.ControlRigComponent.set_control_vector2d(control_name: Name, value: Vector2D) -> None
unreal.ControlRigComponent.set_initial_bone_transform(bone_name: Name, initial_transform: Transform, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE, propagate_to_children: bool = False) -> None
unreal.ControlRigComponent.set_initial_space_transform(space_name: Name, initial_transform: Transform, space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE) -> None
unreal.ControlRigComponent.set_mapped_elements(new_mapped_elements: Array[ControlRigComponentMappedElement]) -> None
unreal.ControlRigComponent.set_object_binding(object_to_bind: Object) -> None
unreal.ControlRigComponent.update(delta_time: float = 0.000000) -> None
```

## `unreal.ControlRigComponentDelegate(MulticastDelegateBase)`

```python
unreal.ControlRigComponentDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ControlRigComponentMappedBone(StructBase)`

```python
unreal.ControlRigComponentMappedBone.__init__(source: Name = "None", target: Name = "None") -> None
unreal.ControlRigComponentMappedBone.source(value: Name) -> None
unreal.ControlRigComponentMappedBone.target(value: Name) -> None
```

## `unreal.ControlRigComponentMappedComponent(StructBase)`

```python
unreal.ControlRigComponentMappedComponent.__init__(component: SceneComponent = None, element_name: Name = "None", element_type: RigElementType = RigElementType.NONE, direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection.INPUT) -> None
unreal.ControlRigComponentMappedComponent.component(value: SceneComponent) -> None
unreal.ControlRigComponentMappedComponent.direction(value: ControlRigComponentMapDirection) -> None
unreal.ControlRigComponentMappedComponent.element_name(value: Name) -> None
unreal.ControlRigComponentMappedComponent.element_type(value: RigElementType) -> None
```

## `unreal.ControlRigComponentMappedCurve(StructBase)`

```python
unreal.ControlRigComponentMappedCurve.__init__(source: Name = "None", target: Name = "None") -> None
unreal.ControlRigComponentMappedCurve.source(value: Name) -> None
unreal.ControlRigComponentMappedCurve.target(value: Name) -> None
```

## `unreal.ControlRigComponentMappedElement(StructBase)`

```python
unreal.ControlRigComponentMappedElement.__init__(component_reference: SoftComponentReference = [None, "None"], transform_index: int = 0, transform_name: Name = "None", element_type: RigElementType = RigElementType.NONE, element_name: Name = "None", direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection.INPUT, offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], weight: float = 0.000000, space: ControlRigComponentSpace = ControlRigComponentSpace.WORLD_SPACE) -> None
unreal.ControlRigComponentMappedElement.component_reference(value: SoftComponentReference) -> None
unreal.ControlRigComponentMappedElement.direction(value: ControlRigComponentMapDirection) -> None
unreal.ControlRigComponentMappedElement.element_name(value: Name) -> None
unreal.ControlRigComponentMappedElement.element_type(value: RigElementType) -> None
unreal.ControlRigComponentMappedElement.offset(value: Transform) -> None
unreal.ControlRigComponentMappedElement.space(value: ControlRigComponentSpace) -> None
unreal.ControlRigComponentMappedElement.transform_index(value: int) -> None
unreal.ControlRigComponentMappedElement.transform_name(value: Name) -> None
unreal.ControlRigComponentMappedElement.weight(value: float) -> None
```

## `unreal.ControlRigContextMenuContext(Object)`

```python
unreal.ControlRigContextMenuContext.get_control_rig() -> ControlRig
unreal.ControlRigContextMenuContext.get_control_rig_blueprint() -> ControlRigBlueprint
unreal.ControlRigContextMenuContext.get_graph_node_context_menu_context() -> ControlRigGraphNodeContextMenuContext
unreal.ControlRigContextMenuContext.get_rig_hierarchy_drag_and_drop_context() -> ControlRigRigHierarchyDragAndDropContext
unreal.ControlRigContextMenuContext.get_rig_hierarchy_to_graph_drag_and_drop_context() -> ControlRigRigHierarchyToGraphDragAndDropContext
unreal.ControlRigContextMenuContext.is_alt_down() -> bool
```

## `unreal.ControlRigControlPose(StructBase)`

```python
unreal.ControlRigControlPose.__init__(copy_of_controls: Array[RigControlCopy] = []) -> None
unreal.ControlRigControlPose.copy_of_controls(value: Array[RigControlCopy]) -> None
```

## `unreal.ControlRigDrawContainer(RigVMDrawContainer)`

```python
unreal.ControlRigDrawContainer.__init__() -> None
```

## `unreal.ControlRigDrawInstruction(RigVMDrawInstruction)`

```python
unreal.ControlRigDrawInstruction.__init__() -> None
```

## `unreal.ControlRigEnumControlProxyValue(StructBase)`

```python
unreal.ControlRigEnumControlProxyValue.__init__() -> None
```

## `unreal.ControlRigExecuteContext(RigVMExecuteContext)`

```python
unreal.ControlRigExecuteContext.__init__() -> None
```

## `unreal.ControlRigGizmoDefinition(ControlRigShapeDefinition)`

```python
unreal.ControlRigGizmoDefinition.__init__(shape_name: Name = "None", static_mesh: StaticMesh = None, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
```

## `unreal.ControlRigGraphNodeContextMenuContext(StructBase)`

```python
unreal.ControlRigGraphNodeContextMenuContext.__init__(graph: RigVMGraph = None, node: RigVMNode = None, pin: RigVMPin = None) -> None
unreal.ControlRigGraphNodeContextMenuContext.graph() -> RigVMGraph
unreal.ControlRigGraphNodeContextMenuContext.node() -> RigVMNode
unreal.ControlRigGraphNodeContextMenuContext.pin() -> RigVMPin
```

## `unreal.ControlRigPoseAsset(Object)`

```python
unreal.ControlRigPoseAsset.does_mirror_match(control_rig: ControlRig, control_name: Name) -> bool
unreal.ControlRigPoseAsset.get_control_names() -> Array[Name]
unreal.ControlRigPoseAsset.get_current_pose(control_rig: ControlRig) -> ControlRigControlPose
unreal.ControlRigPoseAsset.paste_pose(control_rig: ControlRig, do_key: bool = False, do_mirror: bool = False) -> None
unreal.ControlRigPoseAsset.pose(value: ControlRigControlPose) -> None
unreal.ControlRigPoseAsset.replace_control_name(current_name: Name, new_name: Name) -> None
unreal.ControlRigPoseAsset.save_pose(control_rig: ControlRig, use_all: bool) -> None
unreal.ControlRigPoseAsset.select_controls(control_rig: ControlRig, do_mirror: bool = False) -> None
```

## `unreal.ControlRigPoseMirrorSettings(Object)`

```python
unreal.ControlRigPoseMirrorSettings.axis_to_flip(value: AxisType) -> None
unreal.ControlRigPoseMirrorSettings.left_side(value: str) -> None
unreal.ControlRigPoseMirrorSettings.mirror_axis(value: AxisType) -> None
unreal.ControlRigPoseMirrorSettings.right_side(value: str) -> None
```

## `unreal.ControlRigPoseProjectSettings(Object)`

```python
unreal.ControlRigPoseProjectSettings.root_save_dirs(value: Array[DirectoryPath]) -> None
```

## `unreal.ControlRigPythonSettings(RigVMPythonSettings)`

```python
unreal.ControlRigPythonSettings.__init__() -> None
```

## `unreal.ControlRigReference(AnimNodeReference)`

```python
unreal.ControlRigReference.__init__() -> None
```

## `unreal.ControlRigRigHierarchyDragAndDropContext(StructBase)`

```python
unreal.ControlRigRigHierarchyDragAndDropContext.__init__(dragged_element_keys: Array[RigElementKey] = [], target_element_key: RigElementKey = [RigElementType.NONE, "None"]) -> None
unreal.ControlRigRigHierarchyDragAndDropContext.dragged_element_keys() -> Array[RigElementKey]
unreal.ControlRigRigHierarchyDragAndDropContext.target_element_key() -> RigElementKey
```

## `unreal.ControlRigRigHierarchyToGraphDragAndDropContext(StructBase)`

```python
unreal.ControlRigRigHierarchyToGraphDragAndDropContext.__init__(dragged_element_keys: Array[RigElementKey] = []) -> None
unreal.ControlRigRigHierarchyToGraphDragAndDropContext.dragged_element_keys() -> Array[RigElementKey]
```

## `unreal.ControlRigSequencerBindingProxy(StructBase)`

```python
unreal.ControlRigSequencerBindingProxy.__init__(proxy: MovieSceneBindingProxy = [[], None], control_rig: ControlRig = None, track: MovieSceneControlRigParameterTrack = None) -> None
unreal.ControlRigSequencerBindingProxy.control_rig() -> ControlRig
unreal.ControlRigSequencerBindingProxy.proxy() -> MovieSceneBindingProxy
unreal.ControlRigSequencerBindingProxy.track() -> MovieSceneControlRigParameterTrack
```

## `unreal.ControlRigSequencerLibrary(BlueprintFunctionLibrary)`

```python
unreal.ControlRigSequencerLibrary.add_anim_layer_from_selection() -> int
unreal.ControlRigSequencerLibrary.add_constraint(world: World, type: TransformConstraintType, child: TransformableHandle, parent: TransformableHandle, maintain_offset: bool) -> TickableConstraint
unreal.ControlRigSequencerLibrary.bake_constraint(world: World, constraint: TickableConstraint, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.bake_constraints(world: World, settings: BakingAnimationKeySettings) -> Optional[Array[TickableConstraint]]
unreal.ControlRigSequencerLibrary.bake_control_rig_space(sequence: LevelSequence, control_rig: ControlRig, control_names: Array[Name], settings: RigSpacePickerBakeSettings, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.bake_to_control_rig(world: World, level_sequence: LevelSequence, control_rig_class: Class, export_options: AnimSeqExportOption, reduce_keys: bool, tolerance: float, binding: MovieSceneBindingProxy, reset_controls: bool = True) -> bool
unreal.ControlRigSequencerLibrary.blend_values_on_selected(level_sequence: LevelSequence, blend_operation: AnimToolBlendOperation, blend_value: float) -> bool
unreal.ControlRigSequencerLibrary.collapse_control_rig_anim_layers(sequence: LevelSequence, track: MovieSceneControlRigParameterTrack, key_reduce: bool = False, tolerance: float = 0.001000) -> bool
unreal.ControlRigSequencerLibrary.collapse_control_rig_anim_layers_with_settings(sequence: LevelSequence, track: MovieSceneControlRigParameterTrack, settings: BakingAnimationKeySettings) -> bool
unreal.ControlRigSequencerLibrary.compensate(constraint: TickableConstraint, time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.compensate_all(constraint: TickableConstraint) -> bool
unreal.ControlRigSequencerLibrary.delete_anim_layer(index: int) -> bool
unreal.ControlRigSequencerLibrary.delete_constraint_key(constraint: TickableConstraint, constraint_section: MovieSceneSection, time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.delete_control_rig_space(sequence: LevelSequence, control_rig: ControlRig, control_name: Name, time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.duplicate_anim_layer(index: int) -> int
unreal.ControlRigSequencerLibrary.export_fbx_from_control_rig_section(sequence: LevelSequence, section: MovieSceneControlRigParameterSection, export_fbx_control_rig_settings: MovieSceneUserExportFBXControlRigSettings) -> bool
unreal.ControlRigSequencerLibrary.find_or_create_control_rig_component_track(world: World, level_sequence: LevelSequence, binding: MovieSceneBindingProxy) -> Array[MovieSceneTrack]
unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(world: World, level_sequence: LevelSequence, control_rig_class: Class, binding: MovieSceneBindingProxy, is_layered_control_rig: bool = False) -> MovieSceneTrack
unreal.ControlRigSequencerLibrary.get_actor_world_transform(level_sequence: LevelSequence, actor: Actor, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
unreal.ControlRigSequencerLibrary.get_actor_world_transforms(level_sequence: LevelSequence, actor: Actor, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
unreal.ControlRigSequencerLibrary.get_anim_layer_index(anim_layer: AnimLayer) -> int
unreal.ControlRigSequencerLibrary.get_anim_layers() -> Array[AnimLayer]
unreal.ControlRigSequencerLibrary.get_constraint_keys(constraint: TickableConstraint, constraint_section: MovieSceneSection, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Optional[Tuple[Array[bool], Array[FrameNumber]]]
unreal.ControlRigSequencerLibrary.get_constraints_for_handle(world: World, child: TransformableHandle) -> Array[TickableConstraint]
unreal.ControlRigSequencerLibrary.get_control_rig_priority_order(section: MovieSceneTrack) -> int
unreal.ControlRigSequencerLibrary.get_control_rig_world_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
unreal.ControlRigSequencerLibrary.get_control_rig_world_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
unreal.ControlRigSequencerLibrary.get_control_rigs(level_sequence: LevelSequence) -> Array[ControlRigSequencerBindingProxy]
unreal.ControlRigSequencerLibrary.get_controls_mask(section: MovieSceneSection, control_name: Name) -> bool
unreal.ControlRigSequencerLibrary.get_default_parent_key() -> RigElementKey
unreal.ControlRigSequencerLibrary.get_fk_control_rig_apply_mode(control_rig: ControlRig) -> ControlRigFKRigExecuteMode
unreal.ControlRigSequencerLibrary.get_local_control_rig_bool(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.get_local_control_rig_bools(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[bool]
unreal.ControlRigSequencerLibrary.get_local_control_rig_euler_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> EulerTransform
unreal.ControlRigSequencerLibrary.get_local_control_rig_euler_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[EulerTransform]
unreal.ControlRigSequencerLibrary.get_local_control_rig_float(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> float
unreal.ControlRigSequencerLibrary.get_local_control_rig_floats(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[float]
unreal.ControlRigSequencerLibrary.get_local_control_rig_int(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.ControlRigSequencerLibrary.get_local_control_rig_ints(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[int]
unreal.ControlRigSequencerLibrary.get_local_control_rig_position(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Vector
unreal.ControlRigSequencerLibrary.get_local_control_rig_positions(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector]
unreal.ControlRigSequencerLibrary.get_local_control_rig_rotator(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Rotator
unreal.ControlRigSequencerLibrary.get_local_control_rig_rotators(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Rotator]
unreal.ControlRigSequencerLibrary.get_local_control_rig_scale(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Vector
unreal.ControlRigSequencerLibrary.get_local_control_rig_scales(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector]
unreal.ControlRigSequencerLibrary.get_local_control_rig_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Transform
unreal.ControlRigSequencerLibrary.get_local_control_rig_transform_no_scale(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> TransformNoScale
unreal.ControlRigSequencerLibrary.get_local_control_rig_transform_no_scales(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[TransformNoScale]
unreal.ControlRigSequencerLibrary.get_local_control_rig_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Transform]
unreal.ControlRigSequencerLibrary.get_local_control_rig_vector2_ds(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[Vector2D]
unreal.ControlRigSequencerLibrary.get_local_control_rig_vector2d(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Vector2D
unreal.ControlRigSequencerLibrary.get_skeletal_mesh_component_world_transform(level_sequence: LevelSequence, skeletal_mesh_component: SkeletalMeshComponent, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, reference_name: Name = "None") -> Transform
unreal.ControlRigSequencerLibrary.get_skeletal_mesh_component_world_transforms(level_sequence: LevelSequence, skeletal_mesh_component: SkeletalMeshComponent, frames: Array[FrameNumber], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, reference_name: Name = "None") -> Array[Transform]
unreal.ControlRigSequencerLibrary.get_visible_control_rigs() -> Array[ControlRig]
unreal.ControlRigSequencerLibrary.get_world_space_reference_key() -> RigElementKey
unreal.ControlRigSequencerLibrary.hide_all_controls(section: MovieSceneSection) -> None
unreal.ControlRigSequencerLibrary.import_fbx_to_control_rig_track(world: World, sequence: LevelSequence, track: MovieSceneControlRigParameterTrack, section: MovieSceneControlRigParameterSection, selected_control_rig_names: Array[str], import_fbx_control_rig_settings: MovieSceneUserImportFBXControlRigSettings, import_filename: str) -> bool
unreal.ControlRigSequencerLibrary.is_fk_control_rig(control_rig: ControlRig) -> bool
unreal.ControlRigSequencerLibrary.is_layered_control_rig(control_rig: ControlRig) -> bool
unreal.ControlRigSequencerLibrary.load_anim_sequence_into_control_rig_section(movie_scene_section: MovieSceneSection, anim_sequence: AnimSequence, skel_mesh_comp: SkeletalMeshComponent, start_frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, key_reduce: bool = False, tolerance: float = 0.001000, interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.SMART_AUTO, reset_controls: bool = True) -> bool
unreal.ControlRigSequencerLibrary.merge_anim_layers(indices: Array[int]) -> bool
unreal.ControlRigSequencerLibrary.move_constraint_key(constraint: TickableConstraint, constraint_section: MovieSceneSection, time: FrameNumber, new_time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.move_control_rig_space(sequence: LevelSequence, control_rig: ControlRig, control_name: Name, time: FrameNumber, new_time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.rename_control_rig_control_channels(sequence: LevelSequence, control_rig: ControlRig, old_control_names: Array[Name], new_control_names: Array[Name]) -> bool
unreal.ControlRigSequencerLibrary.set_constraint_active_key(constraint: TickableConstraint, active: bool, frame: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.set_control_rig_apply_mode(control_rig: ControlRig, apply_mode: ControlRigFKRigExecuteMode) -> bool
unreal.ControlRigSequencerLibrary.set_control_rig_layered_mode(track: MovieSceneControlRigParameterTrack, set_is_layered: bool) -> bool
unreal.ControlRigSequencerLibrary.set_control_rig_priority_order(section: MovieSceneTrack, priority_order: int) -> None
unreal.ControlRigSequencerLibrary.set_control_rig_space(sequence: LevelSequence, control_rig: ControlRig, control_name: Name, space_key: RigElementKey, time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.set_control_rig_world_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, world_transform: Transform, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_control_rig_world_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], world_transforms: Array[Transform], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_controls_mask(section: MovieSceneSection, control_names: Array[Name], visible: bool) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_bool(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: bool, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_bools(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[bool], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_euler_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: EulerTransform, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_euler_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[EulerTransform], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_float(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: float, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_floats(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[float], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_int(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: int, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_ints(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[int], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_position(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: Vector, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_positions(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[Vector], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_rotator(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: Rotator, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_rotators(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[Rotator], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_scale(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: Vector, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_scales(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[Vector], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_transform(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: Transform, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_transform_no_scale(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: TransformNoScale, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_transform_no_scales(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[TransformNoScale], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_transforms(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[Transform], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2_ds(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frames: Array[FrameNumber], values: Array[Vector2D], time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d(level_sequence: LevelSequence, control_rig: ControlRig, control_name: Name, frame: FrameNumber, value: Vector2D, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, set_key: bool = True) -> None
unreal.ControlRigSequencerLibrary.show_all_controls(section: MovieSceneSection) -> None
unreal.ControlRigSequencerLibrary.smart_reduce(movie_scene_section: MovieSceneSection) -> Optional[SmartReduceParams]
unreal.ControlRigSequencerLibrary.snap_control_rig(level_sequence: LevelSequence, start_frame: FrameNumber, end_frame: FrameNumber, children_to_snap: ControlRigSnapperSelection, parent_to_snap: ControlRigSnapperSelection, snap_settings: ControlRigSnapSettings, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.space_compensate(control_rig: ControlRig, time: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> bool
unreal.ControlRigSequencerLibrary.tween_control_rig(level_sequence: LevelSequence, control_rig: ControlRig, tween_value: float) -> bool
```

## `unreal.ControlRigShapeDefinition(StructBase)`

```python
unreal.ControlRigShapeDefinition.__init__(shape_name: Name = "None", static_mesh: StaticMesh = None, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.ControlRigShapeDefinition.gizmo_name() -> Name
unreal.ControlRigShapeDefinition.shape_name() -> Name
unreal.ControlRigShapeDefinition.static_mesh() -> StaticMesh
unreal.ControlRigShapeDefinition.transform() -> Transform
```

## `unreal.ControlRigShapeLibraryLink(NameSpacedUserData)`

```python
unreal.ControlRigShapeLibraryLink.shape_library(value: ControlRigShapeLibrary) -> None
```

## `unreal.ControlRigSnapSettings(Object)`

```python
unreal.ControlRigSnapSettings.baking_key_settings(value: BakingKeySettings) -> None
unreal.ControlRigSnapSettings.frame_increment(value: int) -> None
unreal.ControlRigSnapSettings.keep_offset(value: bool) -> None
unreal.ControlRigSnapSettings.reduce_keys(value: bool) -> None
unreal.ControlRigSnapSettings.snap_position(value: bool) -> None
unreal.ControlRigSnapSettings.snap_rotation(value: bool) -> None
unreal.ControlRigSnapSettings.snap_scale(value: bool) -> None
unreal.ControlRigSnapSettings.tolerance(value: float) -> None
```

## `unreal.ControlRigSnapperSelection(StructBase)`

```python
unreal.ControlRigSnapperSelection.__init__(actors: Array[ActorForWorldTransforms] = [], control_rigs: Array[ControlRigForWorldTransforms] = []) -> None
unreal.ControlRigSnapperSelection.actors(value: Array[ActorForWorldTransforms]) -> None
unreal.ControlRigSnapperSelection.control_rigs(value: Array[ControlRigForWorldTransforms]) -> None
```

## `unreal.ControlRigSpline(StructBase)`

```python
unreal.ControlRigSpline.__init__() -> None
```

## `unreal.ControlRigTestData(Object)`

```python
unreal.ControlRigTestData.control_rig_object_path() -> SoftObjectPath
unreal.ControlRigTestData.create_new_asset(desired_package_path: str, blueprint_path_name: str) -> ControlRigTestData
unreal.ControlRigTestData.frames_to_skip() -> Array[int]
unreal.ControlRigTestData.get_frame_index_for_time(seconds: float, input: bool = False) -> int
unreal.ControlRigTestData.get_playback_mode() -> ControlRigTestDataPlaybackMode
unreal.ControlRigTestData.get_time_range(input: bool = False) -> Vector2D
unreal.ControlRigTestData.initial() -> ControlRigTestDataFrame
unreal.ControlRigTestData.input_frames() -> Array[ControlRigTestDataFrame]
unreal.ControlRigTestData.is_recording() -> bool
unreal.ControlRigTestData.is_replaying() -> bool
unreal.ControlRigTestData.output_frames() -> Array[ControlRigTestDataFrame]
unreal.ControlRigTestData.record(control_rig: ControlRig, recording_duration: float = 0.000000) -> bool
unreal.ControlRigTestData.release_replay() -> None
unreal.ControlRigTestData.setup_replay(control_rig: ControlRig, ground_truth: bool = True) -> bool
unreal.ControlRigTestData.tolerance() -> float
```

## `unreal.ControlRigTestDataFrame(StructBase)`

```python
unreal.ControlRigTestDataFrame.__init__(absolute_time: float = 0.000000, delta_time: float = 0.000000, variables: Array[ControlRigTestDataVariable] = [], pose: RigPose = []) -> None
unreal.ControlRigTestDataFrame.absolute_time() -> float
unreal.ControlRigTestDataFrame.delta_time() -> float
unreal.ControlRigTestDataFrame.pose() -> RigPose
unreal.ControlRigTestDataFrame.variables() -> Array[ControlRigTestDataVariable]
```

## `unreal.ControlRigTestDataVariable(StructBase)`

```python
unreal.ControlRigTestDataVariable.__init__(name: Name = "None", cpp_type: Name = "None", value: str = "") -> None
unreal.ControlRigTestDataVariable.cpp_type() -> Name
unreal.ControlRigTestDataVariable.name() -> Name
unreal.ControlRigTestDataVariable.value() -> str
```

## `unreal.ControlRigWorkflowOptions(RigVMUserWorkflowOptions)`

```python
unreal.ControlRigWorkflowOptions.ensure_at_least_one_rig_element_selected() -> bool
unreal.ControlRigWorkflowOptions.hierarchy(value: RigHierarchy) -> None
unreal.ControlRigWorkflowOptions.selection(value: Array[RigElementKey]) -> None
```

## `unreal.ControlRig_OnControlSelectedBP(MulticastDelegateBase)`

```python
unreal.ControlRig_OnControlSelectedBP.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CopyBonesModifier(AnimationModifier)`

```python
unreal.CopyBonesModifier.bone_pairs() -> Array[BoneReferencePair]
unreal.CopyBonesModifier.bone_pose_space() -> AnimPoseSpaces
```

## `unreal.CustomAttributePerBoneData(StructBase)`

```python
unreal.CustomAttributePerBoneData.__init__() -> None
```

## `unreal.EncodeRootBoneWeightedBone(StructBase)`

```python
unreal.EncodeRootBoneWeightedBone.__init__() -> None
```

## `unreal.EncodeRootBoneWeightedBoneAxis(EncodeRootBoneWeightedBone)`

```python
unreal.EncodeRootBoneWeightedBoneAxis.__init__() -> None
```

## `unreal.EngineCameraAnimationFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.EngineCameraAnimationFunctionLibrary.conv_camera_animation_camera_modifier(player_camera_manager: PlayerCameraManager) -> CameraAnimationCameraModifier
unreal.EngineCameraAnimationFunctionLibrary.conv_camera_animation_play_space(camera_shake_play_space: CameraShakePlaySpace) -> CameraAnimationPlaySpace
unreal.EngineCameraAnimationFunctionLibrary.conv_camera_shake_play_space(camera_animation_play_space: CameraAnimationPlaySpace) -> CameraShakePlaySpace
```

## `unreal.FBIKBoneLimit(StructBase)`

```python
unreal.FBIKBoneLimit.__init__() -> None
```

## `unreal.FloatAnimationAttribute(StructBase)`

```python
unreal.FloatAnimationAttribute.__init__(value: float = 0.000000) -> None
unreal.FloatAnimationAttribute.value(value: float) -> None
```

## `unreal.FootstepAnimEventsModifier(AnimationModifier)`

```python
unreal.FootstepAnimEventsModifier.foot_definitions() -> Array[FootDefinition]
unreal.FootstepAnimEventsModifier.ground_threshold() -> float
unreal.FootstepAnimEventsModifier.sample_rate() -> int
unreal.FootstepAnimEventsModifier.should_remove_pre_existing_notifies_or_sync_markers() -> bool
unreal.FootstepAnimEventsModifier.speed_threshold() -> float
```

## `unreal.GeometryScriptBoneInfo(StructBase)`

```python
unreal.GeometryScriptBoneInfo.__init__(index: int = 0, name: Name = "None", parent_index: int = 0, local_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], world_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptBoneInfo.color(value: LinearColor) -> None
unreal.GeometryScriptBoneInfo.index(value: int) -> None
unreal.GeometryScriptBoneInfo.local_transform(value: Transform) -> None
unreal.GeometryScriptBoneInfo.name(value: Name) -> None
unreal.GeometryScriptBoneInfo.parent_index(value: int) -> None
unreal.GeometryScriptBoneInfo.world_transform(value: Transform) -> None
```

## `unreal.GeometryScriptBoneWeight(StructBase)`

```python
unreal.GeometryScriptBoneWeight.__init__(bone_index: int = 0, weight: float = 0.000000) -> None
unreal.GeometryScriptBoneWeight.bone_index(value: int) -> None
unreal.GeometryScriptBoneWeight.weight(value: float) -> None
```

## `unreal.GeometryScriptBoneWeightProfile(StructBase)`

```python
unreal.GeometryScriptBoneWeightProfile.__init__(profile_name: Name = "None") -> None
unreal.GeometryScriptBoneWeightProfile.profile_name(value: Name) -> None
```

## `unreal.GeometryScriptCopyBonesFromMeshOptions(StructBase)`

```python
unreal.GeometryScriptCopyBonesFromMeshOptions.__init__(reindex_weights: bool = False, bones_to_copy_from_source: BonesToCopyFromSource = BonesToCopyFromSource.ALL_BONES) -> None
unreal.GeometryScriptCopyBonesFromMeshOptions.bones_to_copy_from_source(value: BonesToCopyFromSource) -> None
unreal.GeometryScriptCopyBonesFromMeshOptions.reindex_weights(value: bool) -> None
```

## `unreal.GeometryScriptPruneBoneWeightsOptions(StructBase)`

```python
unreal.GeometryScriptPruneBoneWeightsOptions.__init__(reassignment_type: GeometryScriptPruneBoneWeightsAssignmentType = GeometryScriptPruneBoneWeightsAssignmentType.RENORMALIZE_REMAINING, ignored_invalid_bones: bool = False) -> None
unreal.GeometryScriptPruneBoneWeightsOptions.ignored_invalid_bones(value: bool) -> None
unreal.GeometryScriptPruneBoneWeightsOptions.reassignment_type(value: GeometryScriptPruneBoneWeightsAssignmentType) -> None
```

## `unreal.GeometryScriptSmoothBoneWeightsOptions(StructBase)`

```python
unreal.GeometryScriptSmoothBoneWeightsOptions.__init__(distance_weighing_type: GeometryScriptSmoothBoneWeightsType = GeometryScriptSmoothBoneWeightsType.DIRECT_DISTANCE, stiffness: float = 0.000000, max_influences: int = 0, voxel_resolution: int = 0) -> None
unreal.GeometryScriptSmoothBoneWeightsOptions.distance_weighing_type(value: GeometryScriptSmoothBoneWeightsType) -> None
unreal.GeometryScriptSmoothBoneWeightsOptions.max_influences(value: int) -> None
unreal.GeometryScriptSmoothBoneWeightsOptions.stiffness(value: float) -> None
unreal.GeometryScriptSmoothBoneWeightsOptions.voxel_resolution(value: int) -> None
```

## `unreal.GeometryScriptTransferBoneWeightsOptions(StructBase)`

```python
unreal.GeometryScriptTransferBoneWeightsOptions.__init__(transfer_method: TransferBoneWeightsMethod = TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE, output_target_mesh_bones: OutputTargetMeshBones = OutputTargetMeshBones.SOURCE_BONES, source_profile: GeometryScriptBoneWeightProfile = ["Default"], target_profile: GeometryScriptBoneWeightProfile = ["Default"], radius_percentage: float = 0.000000, normal_threshold: float = 0.000000, layered_mesh_support: bool = False, num_smoothing_iterations: int = 0, smoothing_strength: float = 0.000000, inpaint_mask: Name = "None") -> None
unreal.GeometryScriptTransferBoneWeightsOptions.inpaint_mask(value: Name) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.layered_mesh_support(value: bool) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.normal_threshold(value: float) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.num_smoothing_iterations(value: int) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.output_target_mesh_bones(value: OutputTargetMeshBones) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.radius_percentage(value: float) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.smoothing_strength(value: float) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.source_profile(value: GeometryScriptBoneWeightProfile) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.target_profile(value: GeometryScriptBoneWeightProfile) -> None
unreal.GeometryScriptTransferBoneWeightsOptions.transfer_method(value: TransferBoneWeightsMethod) -> None
```

## `unreal.GeometryScript_BoneWeights(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_BoneWeights.blend_bone_weights(bone_weights_a: Array[GeometryScriptBoneWeight], bone_weights_b: Array[GeometryScriptBoneWeight], alpha: float, debug: GeometryScriptDebug = None) -> Array[GeometryScriptBoneWeight]
unreal.GeometryScript_BoneWeights.compute_smooth_bone_weights(target_mesh: DynamicMesh, skeleton: Skeleton, options: GeometryScriptSmoothBoneWeightsOptions, profile: GeometryScriptBoneWeightProfile = ["Default"], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.copy_bones_from_mesh(source_mesh: DynamicMesh, target_mesh: DynamicMesh, options: GeometryScriptCopyBonesFromMeshOptions = [False, BonesToCopyFromSource.ALL_BONES], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.copy_bones_from_skeleton(source_skeleton: Skeleton, target_mesh: DynamicMesh, options: GeometryScriptCopyBonesFromMeshOptions = [False, BonesToCopyFromSource.ALL_BONES], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.discard_bones_from_mesh(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.get_all_bones_info(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[GeometryScriptBoneInfo]]
unreal.GeometryScript_BoneWeights.get_bone_children(target_mesh: DynamicMesh, bone_name: Name, recursive: bool, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, Array[GeometryScriptBoneInfo]]
unreal.GeometryScript_BoneWeights.get_bone_index(target_mesh: DynamicMesh, bone_name: Name, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, int]
unreal.GeometryScript_BoneWeights.get_bone_info(target_mesh: DynamicMesh, bone_name: Name, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, GeometryScriptBoneInfo]
unreal.GeometryScript_BoneWeights.get_largest_vertex_bone_weight(target_mesh: DynamicMesh, vertex_id: int, profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, GeometryScriptBoneWeight, bool]
unreal.GeometryScript_BoneWeights.get_max_bone_weight_index(target_mesh: DynamicMesh, profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, bool, int]
unreal.GeometryScript_BoneWeights.get_root_bone_name(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Name]
unreal.GeometryScript_BoneWeights.get_vertex_bone_weights(target_mesh: DynamicMesh, vertex_id: int, profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, Array[GeometryScriptBoneWeight], bool]
unreal.GeometryScript_BoneWeights.mesh_copy_bone_weights(target_mesh: DynamicMesh, target_profile: GeometryScriptBoneWeightProfile, source_profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_BoneWeights.mesh_create_bone_weights(target_mesh: DynamicMesh, replace_existing_profile: bool = False, profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_BoneWeights.mesh_has_bone_weights(target_mesh: DynamicMesh, profile: GeometryScriptBoneWeightProfile = ["Default"]) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_BoneWeights.prune_bone_weights(target_mesh: DynamicMesh, bones_to_prune: Array[Name], options: GeometryScriptPruneBoneWeightsOptions, profile: GeometryScriptBoneWeightProfile = ["Default"], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.set_all_vertex_bone_weights(target_mesh: DynamicMesh, bone_weights: Array[GeometryScriptBoneWeight], profile: GeometryScriptBoneWeightProfile = ["Default"], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_BoneWeights.set_vertex_bone_weights(target_mesh: DynamicMesh, vertex_id: int, bone_weights: Array[GeometryScriptBoneWeight], profile: GeometryScriptBoneWeightProfile = ["Default"], debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_BoneWeights.transfer_bone_weights_from_mesh(source_mesh: DynamicMesh, target_mesh: DynamicMesh, options: GeometryScriptTransferBoneWeightsOptions = [TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE, OutputTargetMeshBones.SOURCE_BONES, ["Default"], ["Default"], -1.000000, -1.000000, True, 0, 0.000000, "None"], selection: GeometryScriptMeshSelection = [], debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GroomAnimationInfo(StructBase)`

```python
unreal.GroomAnimationInfo.__init__() -> None
```

## `unreal.GroomAsset(Object)`

```python
unreal.GroomAsset.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GroomAsset.deformed_skeletal_mesh() -> SkeletalMesh
unreal.GroomAsset.enable_global_interpolation(value: bool) -> None
unreal.GroomAsset.enable_simulation_cache(value: bool) -> None
unreal.GroomAsset.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.GroomAsset.hair_groups_cards(value: Array[HairGroupsCardsSourceDescription]) -> None
unreal.GroomAsset.hair_groups_interpolation(value: Array[HairGroupsInterpolation]) -> None
unreal.GroomAsset.hair_groups_lod(value: Array[HairGroupsLOD]) -> None
unreal.GroomAsset.hair_groups_materials(value: Array[HairGroupsMaterial]) -> None
unreal.GroomAsset.hair_groups_meshes(value: Array[HairGroupsMeshesSourceDescription]) -> None
unreal.GroomAsset.hair_groups_physics(value: Array[HairGroupsPhysics]) -> None
unreal.GroomAsset.hair_groups_rendering(value: Array[HairGroupsRendering]) -> None
unreal.GroomAsset.hair_interpolation_type(value: GroomInterpolationType) -> None
unreal.GroomAsset.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GroomAsset.rigged_skeletal_mesh() -> SkeletalMesh
```

## `unreal.GroomBindingAsset(Object)`

```python
unreal.GroomBindingAsset.groom(value: GroomAsset) -> None
unreal.GroomBindingAsset.groom_binding_type() -> GroomBindingMeshType
unreal.GroomBindingAsset.group_infos(value: Array[GoomBindingGroupInfo]) -> None
unreal.GroomBindingAsset.matching_section() -> int
unreal.GroomBindingAsset.num_interpolation_points() -> int
unreal.GroomBindingAsset.source_geometry_cache() -> GeometryCache
unreal.GroomBindingAsset.source_skeletal_mesh(value: SkeletalMesh) -> None
unreal.GroomBindingAsset.target_geometry_cache() -> GeometryCache
unreal.GroomBindingAsset.target_skeletal_mesh(value: SkeletalMesh) -> None
```

## `unreal.GroomBuildSettings(StructBase)`

```python
unreal.GroomBuildSettings.__init__(override_guides: bool = False, hair_to_guide_density: float = 0.000000, interpolation_quality: GroomInterpolationQuality = GroomInterpolationQuality.LOW, interpolation_distance: GroomInterpolationWeight = GroomInterpolationWeight.PARAMETRIC, randomize_guide: bool = False, use_unique_guide: bool = False) -> None
unreal.GroomBuildSettings.hair_to_guide_density(value: float) -> None
unreal.GroomBuildSettings.interpolation_distance(value: GroomInterpolationWeight) -> None
unreal.GroomBuildSettings.interpolation_quality(value: GroomInterpolationQuality) -> None
unreal.GroomBuildSettings.override_guides(value: bool) -> None
unreal.GroomBuildSettings.randomize_guide(value: bool) -> None
unreal.GroomBuildSettings.use_unique_guide(value: bool) -> None
```

## `unreal.GroomCache(Object)`

```python
unreal.GroomCache.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GroomCache.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.GroomCache.has_asset_user_data_of_class(user_data_class: Class) -> bool
```

## `unreal.GroomCacheImportOptions(Object)`

```python
unreal.GroomCacheImportOptions.import_settings(value: GroomCacheImportSettings) -> None
```

## `unreal.GroomCacheImportSettings(StructBase)`

```python
unreal.GroomCacheImportSettings.__init__(import_groom_cache: bool = False, import_type: GroomCacheImportType = 0, frame_start: int = 0, frame_end: int = 0, skip_empty_frames: bool = False, import_groom_asset: bool = False, groom_asset: SoftObjectPath = [""], override_conversion_settings: bool = False, conversion_settings: GroomConversionSettings = [[0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.GroomCacheImportSettings.conversion_settings(value: GroomConversionSettings) -> None
unreal.GroomCacheImportSettings.frame_end(value: int) -> None
unreal.GroomCacheImportSettings.frame_start(value: int) -> None
unreal.GroomCacheImportSettings.groom_asset(value: SoftObjectPath) -> None
unreal.GroomCacheImportSettings.hair_strands_asset(value: SoftObjectPath) -> None
unreal.GroomCacheImportSettings.import_groom_asset(value: bool) -> None
unreal.GroomCacheImportSettings.import_groom_cache(value: bool) -> None
unreal.GroomCacheImportSettings.import_type(value: GroomCacheImportType) -> None
unreal.GroomCacheImportSettings.override_conversion_settings(value: bool) -> None
unreal.GroomCacheImportSettings.skip_empty_frames(value: bool) -> None
```

## `unreal.GroomCacheInfo(StructBase)`

```python
unreal.GroomCacheInfo.__init__() -> None
```

## `unreal.GroomComponent(MeshComponent)`

```python
unreal.GroomComponent.add_collision_component(skeletal_mesh_component: SkeletalMeshComponent) -> None
unreal.GroomComponent.attachment_name(value: str) -> None
unreal.GroomComponent.binding_asset() -> GroomBindingAsset
unreal.GroomComponent.get_is_hair_length_scale_enabled() -> bool
unreal.GroomComponent.get_niagara_component(group_index: int) -> NiagaraComponent
unreal.GroomComponent.groom_asset(value: GroomAsset) -> None
unreal.GroomComponent.groom_cache(value: GroomCache) -> None
unreal.GroomComponent.groom_groups_desc(value: Array[HairGroupDesc]) -> None
unreal.GroomComponent.hair_strands_asset(value: GroomAsset) -> None
unreal.GroomComponent.mesh_deformer() -> MeshDeformer
unreal.GroomComponent.mesh_deformer_instance() -> MeshDeformerInstance
unreal.GroomComponent.mesh_deformer_instance_settings() -> MeshDeformerInstanceSettings
unreal.GroomComponent.physics_asset(value: PhysicsAsset) -> None
unreal.GroomComponent.reset_collision_components() -> None
unreal.GroomComponent.reset_simulation() -> None
unreal.GroomComponent.set_binding_asset(binding: GroomBindingAsset) -> None
unreal.GroomComponent.set_enable_simulation(enable_simulation: bool) -> None
unreal.GroomComponent.set_groom_asset(asset: GroomAsset) -> None
unreal.GroomComponent.set_groom_cache(groom_cache: GroomCache) -> None
unreal.GroomComponent.set_hair_length_scale(scale: float) -> None
unreal.GroomComponent.set_hair_length_scale_enable(enable: bool) -> None
unreal.GroomComponent.set_mesh_deformer(mesh_deformer: MeshDeformer) -> None
unreal.GroomComponent.set_physics_asset(physics_asset: PhysicsAsset) -> None
unreal.GroomComponent.simulation_settings(value: HairSimulationSettings) -> None
unreal.GroomComponent.use_cards(value: bool) -> None
```

## `unreal.GroomConversionSettings(StructBase)`

```python
unreal.GroomConversionSettings.__init__(rotation: Vector = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GroomConversionSettings.rotation(value: Vector) -> None
unreal.GroomConversionSettings.scale(value: Vector) -> None
```

## `unreal.GroomCreateBindingOptions(Object)`

```python
unreal.GroomCreateBindingOptions.groom_binding_type(value: GroomBindingMeshType) -> None
unreal.GroomCreateBindingOptions.matching_section(value: int) -> None
unreal.GroomCreateBindingOptions.num_interpolation_points(value: int) -> None
unreal.GroomCreateBindingOptions.source_geometry_cache(value: GeometryCache) -> None
unreal.GroomCreateBindingOptions.source_skeletal_mesh(value: SkeletalMesh) -> None
unreal.GroomCreateBindingOptions.target_geometry_cache(value: GeometryCache) -> None
unreal.GroomCreateBindingOptions.target_skeletal_mesh(value: SkeletalMesh) -> None
```

## `unreal.GroomCreateFollicleMaskOptions(Object)`

```python
unreal.GroomCreateFollicleMaskOptions.grooms(value: Array[FollicleMaskOptions]) -> None
unreal.GroomCreateFollicleMaskOptions.resolution(value: int) -> None
unreal.GroomCreateFollicleMaskOptions.root_radius(value: int) -> None
```

## `unreal.GroomHairGroupPreview(StructBase)`

```python
unreal.GroomHairGroupPreview.__init__(group_name: Name = "None", group_id: int = 0, curve_count: int = 0, guide_count: int = 0, interpolation_settings: HairGroupsInterpolation = []) -> None
unreal.GroomHairGroupPreview.curve_count() -> int
unreal.GroomHairGroupPreview.group_id() -> int
unreal.GroomHairGroupPreview.group_name() -> Name
unreal.GroomHairGroupPreview.guide_count() -> int
unreal.GroomHairGroupPreview.interpolation_settings(value: HairGroupsInterpolation) -> None
```

## `unreal.GroomHairGroupsPreview(Object)`

```python
unreal.GroomHairGroupsPreview.groups(value: Array[GroomHairGroupPreview]) -> None
```

## `unreal.GroomImportOptions(Object)`

```python
unreal.GroomImportOptions.conversion_settings(value: GroomConversionSettings) -> None
unreal.GroomImportOptions.interpolation_settings() -> Array[HairGroupsInterpolation]
```

## `unreal.GroomLibrary(BlueprintFunctionLibrary)`

```python
unreal.GroomLibrary.create_new_geometry_cache_groom_binding_asset(groom_asset: GroomAsset, geometry_cache: GeometryCache, num_interpolation_points: int = 100, source_geometry_cache_for_transfer: GeometryCache = None, matching_section: int = 0) -> GroomBindingAsset
unreal.GroomLibrary.create_new_geometry_cache_groom_binding_asset_with_path(desired_package_path: str, groom_asset: GroomAsset, geometry_cache: GeometryCache, num_interpolation_points: int = 100, source_geometry_cache_for_transfer: GeometryCache = None, matching_section: int = 0) -> GroomBindingAsset
unreal.GroomLibrary.create_new_groom_binding_asset(groom_asset: GroomAsset, skeletal_mesh: SkeletalMesh, num_interpolation_points: int = 100, source_skeletal_mesh_for_transfer: SkeletalMesh = None, matching_section: int = 0) -> GroomBindingAsset
unreal.GroomLibrary.create_new_groom_binding_asset_with_path(desired_package_path: str, groom_asset: GroomAsset, skeletal_mesh: SkeletalMesh, num_interpolation_points: int = 100, source_skeletal_mesh_for_transfer: SkeletalMesh = None, matching_section: int = 0) -> GroomBindingAsset
unreal.GroomLibrary.is_hair_strands_supported_in_world(world_context_object: Object) -> bool
```

## `unreal.IKRetargetPose(StructBase)`

```python
unreal.IKRetargetPose.__init__() -> None
```

## `unreal.IKRigComponent(ActorComponent)`

```python
unreal.IKRigComponent.add_ik_goals() -> Map[Name, IKRigGoal]
unreal.IKRigComponent.clear_all_goals() -> None
unreal.IKRigComponent.set_ik_rig_goal(goal: IKRigGoal) -> None
unreal.IKRigComponent.set_ik_rig_goal_position_and_rotation(goal_name: Name, position: Vector, rotation: Quat, position_alpha: float, rotation_alpha: float) -> None
unreal.IKRigComponent.set_ik_rig_goal_transform(goal_name: Name, transform: Transform, position_alpha: float, rotation_alpha: float) -> None
```

## `unreal.IKRigController(Object)`

```python
unreal.IKRigController.add_bone_setting(bone_name: Name, solver_index: int) -> bool
unreal.IKRigController.add_new_goal(goal_name: Name, bone_name: Name) -> Name
unreal.IKRigController.add_retarget_chain(chain_name: Name, start_bone_name: Name, end_bone_name: Name, goal_name: Name) -> Name
unreal.IKRigController.add_solver(solver_class: Class) -> int
unreal.IKRigController.apply_auto_fbik() -> bool
unreal.IKRigController.apply_auto_generated_retarget_definition() -> bool
unreal.IKRigController.connect_goal_to_solver(goal_name: Name, solver_index: int) -> bool
unreal.IKRigController.disconnect_goal_from_solver(goal_to_remove: Name, solver_index: int) -> bool
unreal.IKRigController.get_all_goals() -> Array[IKRigEffectorGoal]
unreal.IKRigController.get_bone_excluded(bone_name: Name) -> bool
unreal.IKRigController.get_bone_for_goal(goal_name: Name) -> Name
unreal.IKRigController.get_bone_settings(bone_name: Name, solver_index: int) -> Object
unreal.IKRigController.get_controller(ik_rig_definition: IKRigDefinition) -> IKRigController
unreal.IKRigController.get_end_bone(solver_index: int) -> Name
unreal.IKRigController.get_goal(goal_name: Name) -> IKRigEffectorGoal
unreal.IKRigController.get_goal_name_for_bone(bone_name: Name) -> Name
unreal.IKRigController.get_goal_settings_for_solver(goal_name: Name, solver_index: int) -> Object
unreal.IKRigController.get_index_of_solver(solver: IKRigSolver) -> int
unreal.IKRigController.get_num_solvers() -> int
unreal.IKRigController.get_ref_pose_transform_of_bone(bone_name: Name) -> Transform
unreal.IKRigController.get_retarget_chain_end_bone(chain_name: Name) -> Name
unreal.IKRigController.get_retarget_chain_goal(chain_name: Name) -> Name
unreal.IKRigController.get_retarget_chain_start_bone(chain_name: Name) -> Name
unreal.IKRigController.get_retarget_chains() -> Array[BoneChain]
unreal.IKRigController.get_retarget_root() -> Name
unreal.IKRigController.get_root_bone(solver_index: int) -> Name
unreal.IKRigController.get_skeletal_mesh() -> SkeletalMesh
unreal.IKRigController.get_solver_at_index(index: int) -> IKRigSolver
unreal.IKRigController.get_solver_enabled(solver_index: int) -> bool
unreal.IKRigController.is_goal_connected_to_any_solver(goal_name: Name) -> bool
unreal.IKRigController.is_goal_connected_to_solver(goal_name: Name, solver_index: int) -> bool
unreal.IKRigController.is_skeletal_mesh_compatible(skeletal_mesh_to_check: SkeletalMesh) -> bool
unreal.IKRigController.move_solver_in_stack(solver_to_move_index: int, target_solver_index: int) -> bool
unreal.IKRigController.remove_bone_setting(bone_name: Name, solver_index: int) -> bool
unreal.IKRigController.remove_goal(goal_name: Name) -> bool
unreal.IKRigController.remove_retarget_chain(chain_name: Name) -> bool
unreal.IKRigController.remove_solver(solver_index: int) -> bool
unreal.IKRigController.rename_goal(old_name: Name, potential_new_name: Name) -> Name
unreal.IKRigController.rename_retarget_chain(chain_name: Name, new_chain_name: Name) -> Name
unreal.IKRigController.set_bone_excluded(bone_name: Name, exclude: bool) -> bool
unreal.IKRigController.set_end_bone(end_bone_name: Name, solver_index: int) -> bool
unreal.IKRigController.set_goal_bone(goal_name: Name, new_bone_name: Name) -> bool
unreal.IKRigController.set_retarget_chain_end_bone(chain_name: Name, end_bone_name: Name) -> bool
unreal.IKRigController.set_retarget_chain_goal(chain_name: Name, goal_name: Name) -> bool
unreal.IKRigController.set_retarget_chain_start_bone(chain_name: Name, start_bone_name: Name) -> bool
unreal.IKRigController.set_retarget_root(root_bone_name: Name) -> bool
unreal.IKRigController.set_root_bone(root_bone_name: Name, solver_index: int) -> bool
unreal.IKRigController.set_skeletal_mesh(skeletal_mesh: SkeletalMesh) -> bool
unreal.IKRigController.set_solver_enabled(solver_index: int, is_enabled: bool) -> bool
```

## `unreal.IKRigEffectorGoal(Object)`

```python
unreal.IKRigEffectorGoal.bone_name() -> Name
unreal.IKRigEffectorGoal.current_transform(value: Transform) -> None
unreal.IKRigEffectorGoal.expose_position(value: bool) -> None
unreal.IKRigEffectorGoal.expose_rotation(value: bool) -> None
unreal.IKRigEffectorGoal.goal_name() -> Name
unreal.IKRigEffectorGoal.initial_transform() -> Transform
unreal.IKRigEffectorGoal.position_alpha(value: float) -> None
unreal.IKRigEffectorGoal.preview_mode(value: IKRigGoalPreviewMode) -> None
unreal.IKRigEffectorGoal.rotation_alpha(value: float) -> None
unreal.IKRigEffectorGoal.size_multiplier(value: float) -> None
unreal.IKRigEffectorGoal.thickness_multiplier(value: float) -> None
```

## `unreal.IKRigFBIKSolver(IKRigSolver)`

```python
unreal.IKRigFBIKSolver.allow_stretch(value: bool) -> None
unreal.IKRigFBIKSolver.get_bone_settings() -> Array[IKRig_FBIKBoneSettings]
unreal.IKRigFBIKSolver.get_effectors() -> Array[IKRig_FBIKEffector]
unreal.IKRigFBIKSolver.iterations(value: int) -> None
unreal.IKRigFBIKSolver.mass_multiplier(value: float) -> None
unreal.IKRigFBIKSolver.max_angle(value: float) -> None
unreal.IKRigFBIKSolver.over_relaxation(value: float) -> None
unreal.IKRigFBIKSolver.pre_pull_root_settings(value: RootPrePullSettings) -> None
unreal.IKRigFBIKSolver.pull_chain_alpha(value: float) -> None
unreal.IKRigFBIKSolver.root_behavior(value: PBIKRootBehavior) -> None
unreal.IKRigFBIKSolver.root_bone() -> Name
unreal.IKRigFBIKSolver.sub_iterations(value: int) -> None
```

## `unreal.IKRigGoal(StructBase)`

```python
unreal.IKRigGoal.__init__(name: Name = "None", transform_source: IKRigGoalTransformSource = IKRigGoalTransformSource.MANUAL, position: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], position_alpha: float = 0.000000, rotation_alpha: float = 0.000000, position_space: IKRigGoalSpace = IKRigGoalSpace.COMPONENT, rotation_space: IKRigGoalSpace = IKRigGoalSpace.COMPONENT) -> None
unreal.IKRigGoal.name(value: Name) -> None
unreal.IKRigGoal.position(value: Vector) -> None
unreal.IKRigGoal.position_alpha(value: float) -> None
unreal.IKRigGoal.position_space(value: IKRigGoalSpace) -> None
unreal.IKRigGoal.rotation(value: Rotator) -> None
unreal.IKRigGoal.rotation_alpha(value: float) -> None
unreal.IKRigGoal.rotation_space(value: IKRigGoalSpace) -> None
unreal.IKRigGoal.transform_source(value: IKRigGoalTransformSource) -> None
```

## `unreal.IKRig_BodyMover(IKRigSolver)`

```python
unreal.IKRig_BodyMover.position_alpha(value: float) -> None
unreal.IKRig_BodyMover.position_negative_x(value: float) -> None
unreal.IKRig_BodyMover.position_negative_y(value: float) -> None
unreal.IKRig_BodyMover.position_negative_z(value: float) -> None
unreal.IKRig_BodyMover.position_positive_x(value: float) -> None
unreal.IKRig_BodyMover.position_positive_y(value: float) -> None
unreal.IKRig_BodyMover.position_positive_z(value: float) -> None
unreal.IKRig_BodyMover.rotate_x_alpha(value: float) -> None
unreal.IKRig_BodyMover.rotate_y_alpha(value: float) -> None
unreal.IKRig_BodyMover.rotate_z_alpha(value: float) -> None
unreal.IKRig_BodyMover.rotation_alpha(value: float) -> None
```

## `unreal.IKRig_BodyMoverEffector(Object)`

```python
unreal.IKRig_BodyMoverEffector.bone_name() -> Name
unreal.IKRig_BodyMoverEffector.goal_name() -> Name
unreal.IKRig_BodyMoverEffector.influence_multiplier(value: float) -> None
```

## `unreal.IKRig_FBIKBoneSettings(Object)`

```python
unreal.IKRig_FBIKBoneSettings.bone() -> Name
unreal.IKRig_FBIKBoneSettings.max_x(value: float) -> None
unreal.IKRig_FBIKBoneSettings.max_y(value: float) -> None
unreal.IKRig_FBIKBoneSettings.max_z(value: float) -> None
unreal.IKRig_FBIKBoneSettings.min_x(value: float) -> None
unreal.IKRig_FBIKBoneSettings.min_y(value: float) -> None
unreal.IKRig_FBIKBoneSettings.min_z(value: float) -> None
unreal.IKRig_FBIKBoneSettings.position_stiffness(value: float) -> None
unreal.IKRig_FBIKBoneSettings.preferred_angles(value: Vector) -> None
unreal.IKRig_FBIKBoneSettings.rotation_stiffness(value: float) -> None
unreal.IKRig_FBIKBoneSettings.use_preferred_angles(value: bool) -> None
unreal.IKRig_FBIKBoneSettings.x(value: PBIKLimitType) -> None
unreal.IKRig_FBIKBoneSettings.y(value: PBIKLimitType) -> None
unreal.IKRig_FBIKBoneSettings.z(value: PBIKLimitType) -> None
```

## `unreal.IKRig_FBIKEffector(Object)`

```python
unreal.IKRig_FBIKEffector.bone_name() -> Name
unreal.IKRig_FBIKEffector.chain_depth(value: int) -> None
unreal.IKRig_FBIKEffector.goal_name() -> Name
unreal.IKRig_FBIKEffector.pin_rotation(value: float) -> None
unreal.IKRig_FBIKEffector.pull_chain_alpha(value: float) -> None
unreal.IKRig_FBIKEffector.strength_alpha(value: float) -> None
```

## `unreal.IKRig_LimbEffector(Object)`

```python
unreal.IKRig_LimbEffector.bone_name() -> Name
unreal.IKRig_LimbEffector.goal_name() -> Name
```

## `unreal.IKRig_LimbSolver(IKRigSolver)`

```python
unreal.IKRig_LimbSolver.average_pull(value: bool) -> None
unreal.IKRig_LimbSolver.enable_limit(value: bool) -> None
unreal.IKRig_LimbSolver.enable_twist_correction(value: bool) -> None
unreal.IKRig_LimbSolver.end_bone_forward_axis(value: AxisType) -> None
unreal.IKRig_LimbSolver.hinge_rotation_axis(value: AxisType) -> None
unreal.IKRig_LimbSolver.max_iterations(value: int) -> None
unreal.IKRig_LimbSolver.min_rotation_angle(value: float) -> None
unreal.IKRig_LimbSolver.pull_distribution(value: float) -> None
unreal.IKRig_LimbSolver.reach_precision(value: float) -> None
unreal.IKRig_LimbSolver.reach_step_alpha(value: float) -> None
unreal.IKRig_LimbSolver.root_name() -> Name
```

## `unreal.IKRig_PoleSolverEffector(Object)`

```python
unreal.IKRig_PoleSolverEffector.alpha(value: float) -> None
unreal.IKRig_PoleSolverEffector.bone_name() -> Name
unreal.IKRig_PoleSolverEffector.goal_name() -> Name
```

## `unreal.InputBlendPose(StructBase)`

```python
unreal.InputBlendPose.__init__() -> None
```

## `unreal.IntegerAnimationAttribute(StructBase)`

```python
unreal.IntegerAnimationAttribute.__init__(value: int = 0) -> None
unreal.IntegerAnimationAttribute.value(value: int) -> None
```

## `unreal.InterchangeAnimationPayLoadKey(StructBase)`

```python
unreal.InterchangeAnimationPayLoadKey.__init__(unique_id: str = "", type: InterchangeAnimationPayLoadType = InterchangeAnimationPayLoadType.NONE) -> None
unreal.InterchangeAnimationPayLoadKey.type(value: InterchangeAnimationPayLoadType) -> None
unreal.InterchangeAnimationPayLoadKey.unique_id(value: str) -> None
```

## `unreal.InterchangeAnimationTrackBaseNode(InterchangeBaseNode)`

```python
unreal.InterchangeAnimationTrackBaseNode.get_custom_completion_mode() -> Optional[int]
unreal.InterchangeAnimationTrackBaseNode.set_custom_completion_mode(attribute_value: int) -> bool
```

## `unreal.InterchangeAnimationTrackNode(InterchangeAnimationTrackBaseNode)`

```python
unreal.InterchangeAnimationTrackNode.get_custom_actor_dependency_uid() -> Optional[str]
unreal.InterchangeAnimationTrackNode.get_custom_animation_payload_key() -> Optional[InterchangeAnimationPayLoadKey]
unreal.InterchangeAnimationTrackNode.get_custom_frame_count() -> Optional[int]
unreal.InterchangeAnimationTrackNode.get_custom_property_track() -> Optional[InterchangePropertyTracks]
unreal.InterchangeAnimationTrackNode.set_custom_actor_dependency_uid(dependency_uid: str) -> bool
unreal.InterchangeAnimationTrackNode.set_custom_animation_payload_key(unique_id: str, type: InterchangeAnimationPayLoadType) -> bool
unreal.InterchangeAnimationTrackNode.set_custom_frame_count(attribute_value: int) -> bool
unreal.InterchangeAnimationTrackNode.set_custom_property_track(property_track: InterchangePropertyTracks) -> bool
```

## `unreal.InterchangeAnimationTrackSetInstanceNode(InterchangeAnimationTrackBaseNode)`

```python
unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_duration() -> Optional[int]
unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_start_frame() -> Optional[int]
unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_time_scale() -> Optional[float]
unreal.InterchangeAnimationTrackSetInstanceNode.get_custom_track_set_dependency_uid() -> Optional[str]
unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_duration(attribute_value: int) -> bool
unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_start_frame(attribute_value: int) -> bool
unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_time_scale(attribute_value: float) -> bool
unreal.InterchangeAnimationTrackSetInstanceNode.set_custom_track_set_dependency_uid(attribute_value: str) -> bool
```

## `unreal.InterchangeAnimationTrackSetNode(InterchangeBaseNode)`

```python
unreal.InterchangeAnimationTrackSetNode.add_custom_animation_track_uid(animation_track_uid: str) -> bool
unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uid(index: int) -> str
unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uid_count() -> int
unreal.InterchangeAnimationTrackSetNode.get_custom_animation_track_uids() -> Array[str]
unreal.InterchangeAnimationTrackSetNode.get_custom_frame_rate() -> Optional[float]
unreal.InterchangeAnimationTrackSetNode.remove_custom_animation_track_uid(animation_track_uid: str) -> bool
unreal.InterchangeAnimationTrackSetNode.set_custom_frame_rate(attribute_value: float) -> bool
```

## `unreal.InterchangeGenericAnimationPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericAnimationPipeline.add_curve_metadata_to_skeleton(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.animation_range(value: InterchangeAnimationRange) -> None
unreal.InterchangeGenericAnimationPipeline.custom_bone_animation_sample_rate(value: int) -> None
unreal.InterchangeGenericAnimationPipeline.delete_existing_custom_attribute_curves(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.delete_existing_morph_target_curves(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.delete_existing_non_curve_custom_attributes(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.do_not_import_curve_with_zero(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.frame_import_range(value: Int32Interval) -> None
unreal.InterchangeGenericAnimationPipeline.import_animations(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.import_bone_tracks(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.import_custom_attribute(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.material_curve_suffixes(value: Array[str]) -> None
unreal.InterchangeGenericAnimationPipeline.remove_curve_redundant_keys(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.set_material_drive_parameter_on_custom_attribute(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.snap_to_closest_frame_boundary(value: bool) -> None
unreal.InterchangeGenericAnimationPipeline.use30_hz_to_bake_bone_animation(value: bool) -> None
```

## `unreal.InterchangeSkeletalAnimationTrackNode(InterchangeAnimationTrackBaseNode)`

```python
unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_sample_rate() -> Optional[float]
unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_start_time() -> Optional[float]
unreal.InterchangeSkeletalAnimationTrackNode.get_custom_animation_stop_time() -> Optional[float]
unreal.InterchangeSkeletalAnimationTrackNode.get_custom_skeleton_node_uid() -> Optional[str]
unreal.InterchangeSkeletalAnimationTrackNode.get_morph_target_node_animation_payload_keys() -> Tuple[Map[str, str], Map[str, int]]
unreal.InterchangeSkeletalAnimationTrackNode.get_scene_node_animation_payload_keys() -> Tuple[Map[str, str], Map[str, int]]
unreal.InterchangeSkeletalAnimationTrackNode.is_node_animated_with_baked_curve(scene_node_uid: str) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_animation_payload_key_for_morph_target_node_uid(morph_target_node_uid: str, unique_id: str, type: InterchangeAnimationPayLoadType) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_animation_payload_key_for_scene_node_uid(scene_node_uid: str, unique_id: str, type: InterchangeAnimationPayLoadType) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_sample_rate(sample_rate: float) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_start_time(start_time: float) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_custom_animation_stop_time(stop_time: float) -> bool
unreal.InterchangeSkeletalAnimationTrackNode.set_custom_skeleton_node_uid(attribute_value: str) -> bool
```

## `unreal.LayeredBoneBlendLibrary(BlueprintFunctionLibrary)`

```python
unreal.LayeredBoneBlendLibrary.convert_to_layered_blend_per_bone_pure(node: AnimNodeReference) -> Tuple[LayeredBoneBlendReference, bool]
unreal.LayeredBoneBlendLibrary.convert_to_layered_bone_blend(node: AnimNodeReference) -> Tuple[LayeredBoneBlendReference, AnimNodeReferenceConversionResult]
unreal.LayeredBoneBlendLibrary.get_num_poses(layered_bone_blend: LayeredBoneBlendReference) -> int
unreal.LayeredBoneBlendLibrary.set_blend_mask(update_context: AnimUpdateContext, layered_bone_blend: LayeredBoneBlendReference, pose_index: int, blend_mask_name: Name) -> LayeredBoneBlendReference
```

## `unreal.LayeredBoneBlendReference(AnimNodeReference)`

```python
unreal.LayeredBoneBlendReference.__init__() -> None
```

## `unreal.LinkedAnimGraphLibrary(BlueprintFunctionLibrary)`

```python
unreal.LinkedAnimGraphLibrary.convert_to_linked_anim_graph(node: AnimNodeReference) -> Tuple[LinkedAnimGraphReference, AnimNodeReferenceConversionResult]
unreal.LinkedAnimGraphLibrary.convert_to_linked_anim_graph_pure(node: AnimNodeReference) -> Tuple[LinkedAnimGraphReference, bool]
unreal.LinkedAnimGraphLibrary.get_linked_anim_instance(node: LinkedAnimGraphReference) -> AnimInstance
unreal.LinkedAnimGraphLibrary.has_linked_anim_instance(node: LinkedAnimGraphReference) -> bool
```

## `unreal.LinkedAnimGraphReference(AnimNodeReference)`

```python
unreal.LinkedAnimGraphReference.__init__() -> None
```

## `unreal.LiveLinkAnimationFrameData(LiveLinkBaseFrameData)`

```python
unreal.LiveLinkAnimationFrameData.__init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]], property_values: Array[float] = [], transforms: Array[Transform] = []) -> None
unreal.LiveLinkAnimationFrameData.transforms(value: Array[Transform]) -> None
```

## `unreal.LiveLinkSkeletonStaticData(LiveLinkBaseStaticData)`

```python
unreal.LiveLinkSkeletonStaticData.__init__(property_names: Array[Name] = [], bone_names: Array[Name] = [], bone_parents: Array[int] = []) -> None
unreal.LiveLinkSkeletonStaticData.bone_names(value: Array[Name]) -> None
unreal.LiveLinkSkeletonStaticData.bone_parents(value: Array[int]) -> None
```

## `unreal.LocalSpacePose(StructBase)`

```python
unreal.LocalSpacePose.__init__(transforms: Array[Transform] = [], names: Array[Name] = []) -> None
unreal.LocalSpacePose.names(value: Array[Name]) -> None
unreal.LocalSpacePose.transforms(value: Array[Transform]) -> None
```

## `unreal.MarkerSyncAnimPosition(StructBase)`

```python
unreal.MarkerSyncAnimPosition.__init__(previous_marker_name: Name = "None", next_marker_name: Name = "None", position_between_markers: float = 0.000000) -> None
unreal.MarkerSyncAnimPosition.next_marker_name(value: Name) -> None
unreal.MarkerSyncAnimPosition.position_between_markers(value: float) -> None
unreal.MarkerSyncAnimPosition.previous_marker_name(value: Name) -> None
```

## `unreal.MirrorAnimLibrary(BlueprintFunctionLibrary)`

```python
unreal.MirrorAnimLibrary.convert_to_mirror_node(node: AnimNodeReference) -> Tuple[MirrorAnimNodeReference, AnimNodeReferenceConversionResult]
unreal.MirrorAnimLibrary.convert_to_mirror_node_pure(node: AnimNodeReference) -> Tuple[MirrorAnimNodeReference, bool]
unreal.MirrorAnimLibrary.get_mirror(mirror_node: MirrorAnimNodeReference) -> bool
unreal.MirrorAnimLibrary.get_mirror_data_table(mirror_node: MirrorAnimNodeReference) -> MirrorDataTable
unreal.MirrorAnimLibrary.get_mirror_transition_blend_time(mirror_node: MirrorAnimNodeReference) -> float
unreal.MirrorAnimLibrary.set_mirror(mirror_node: MirrorAnimNodeReference, mirror: bool) -> MirrorAnimNodeReference
unreal.MirrorAnimLibrary.set_mirror_transition_blend_time(mirror_node: MirrorAnimNodeReference, blend_time: float) -> MirrorAnimNodeReference
```

## `unreal.MirrorAnimNodeReference(AnimNodeReference)`

```python
unreal.MirrorAnimNodeReference.__init__() -> None
```

## `unreal.ModifyCurveAnimLibrary(BlueprintFunctionLibrary)`

```python
unreal.ModifyCurveAnimLibrary.convert_to_modify_curve_node(node: AnimNodeReference) -> Tuple[ModifyCurveAnimNodeReference, AnimNodeReferenceConversionResult]
unreal.ModifyCurveAnimLibrary.convert_to_modify_curve_node_pure(node: AnimNodeReference) -> Tuple[ModifyCurveAnimNodeReference, bool]
unreal.ModifyCurveAnimLibrary.get_alpha(modify_curve_node: ModifyCurveAnimNodeReference) -> float
unreal.ModifyCurveAnimLibrary.get_apply_mode(modify_curve_node: ModifyCurveAnimNodeReference) -> ModifyCurveApplyMode
unreal.ModifyCurveAnimLibrary.set_alpha(modify_curve_node: ModifyCurveAnimNodeReference, alpha: float) -> ModifyCurveAnimNodeReference
unreal.ModifyCurveAnimLibrary.set_apply_mode(modify_curve_node: ModifyCurveAnimNodeReference, mode: ModifyCurveApplyMode) -> ModifyCurveAnimNodeReference
unreal.ModifyCurveAnimLibrary.set_curve_map(modify_curve_node: ModifyCurveAnimNodeReference, curve_map: Map[Name, float]) -> ModifyCurveAnimNodeReference
```

## `unreal.ModifyCurveAnimNodeReference(AnimNodeReference)`

```python
unreal.ModifyCurveAnimNodeReference.__init__() -> None
```

## `unreal.MontageBlendSettings(StructBase)`

```python
unreal.MontageBlendSettings.__init__(blend_profile: BlendProfile = None, blend: AlphaBlendArgs = [None, 0.200000, AlphaBlendOption.LINEAR], blend_mode: MontageBlendMode = MontageBlendMode.STANDARD) -> None
unreal.MontageBlendSettings.blend(value: AlphaBlendArgs) -> None
unreal.MontageBlendSettings.blend_mode(value: MontageBlendMode) -> None
unreal.MontageBlendSettings.blend_profile(value: BlendProfile) -> None
```

## `unreal.MontageWaitSimpleDelegate(MulticastDelegateBase)`

```python
unreal.MontageWaitSimpleDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MovieSceneAnimationTrackRecorderEditorSettings(MovieSceneTrackRecorderSettings)`

```python
unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_asset_name(value: str) -> None
unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_sub_directory(value: str) -> None
unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_track_name(value: Text) -> None
unreal.MovieSceneAnimationTrackRecorderEditorSettings.remove_root_animation(value: bool) -> None
unreal.MovieSceneAnimationTrackRecorderEditorSettings.timecode_bone_method(value: TimecodeBoneMethod) -> None
```

## `unreal.MovieSceneGroomCacheParams(StructBase)`

```python
unreal.MovieSceneGroomCacheParams.__init__() -> None
```

## `unreal.MovieSceneSkeletalAnimationParams(StructBase)`

```python
unreal.MovieSceneSkeletalAnimationParams.__init__(animation: AnimSequenceBase = None, first_loop_start_frame_offset: FrameNumber = [0], start_frame_offset: FrameNumber = [0], end_frame_offset: FrameNumber = [0], play_rate: MovieSceneTimeWarpVariant = [1.000000], reverse: bool = False, slot_name: Name = "None", mirror_data_table: MirrorDataTable = None, skip_anim_notifiers: bool = False, force_custom_mode: bool = False, swap_root_bone: SwapRootBone = SwapRootBone.SWAP_ROOT_BONE_COMPONENT) -> None
unreal.MovieSceneSkeletalAnimationParams.animation(value: AnimSequenceBase) -> None
unreal.MovieSceneSkeletalAnimationParams.end_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSkeletalAnimationParams.first_loop_start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSkeletalAnimationParams.force_custom_mode(value: bool) -> None
unreal.MovieSceneSkeletalAnimationParams.mirror_data_table(value: MirrorDataTable) -> None
unreal.MovieSceneSkeletalAnimationParams.play_rate(value: MovieSceneTimeWarpVariant) -> None
unreal.MovieSceneSkeletalAnimationParams.reverse(value: bool) -> None
unreal.MovieSceneSkeletalAnimationParams.skip_anim_notifiers(value: bool) -> None
unreal.MovieSceneSkeletalAnimationParams.slot_name(value: Name) -> None
unreal.MovieSceneSkeletalAnimationParams.start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSkeletalAnimationParams.swap_root_bone(value: SwapRootBone) -> None
```

## `unreal.MovieSceneSkeletalAnimationSection(MovieSceneSection)`

```python
unreal.MovieSceneSkeletalAnimationSection.matched_location_offset() -> Vector
unreal.MovieSceneSkeletalAnimationSection.matched_rotation_offset() -> Rotator
unreal.MovieSceneSkeletalAnimationSection.params(value: MovieSceneSkeletalAnimationParams) -> None
unreal.MovieSceneSkeletalAnimationSection.show_skeleton(value: bool) -> None
unreal.MovieSceneSkeletalAnimationSection.start_location_offset(value: Vector) -> None
unreal.MovieSceneSkeletalAnimationSection.start_rotation_offset(value: Rotator) -> None
```

## `unreal.MovieSceneSkeletalAnimationTrack(MovieSceneNameableTrack)`

```python
unreal.MovieSceneSkeletalAnimationTrack.swap_root_bone(value: SwapRootBone) -> None
```

## `unreal.MovieSceneUserExportFBXControlRigSettings(Object)`

```python
unreal.MovieSceneUserExportFBXControlRigSettings.ascii(value: bool) -> None
unreal.MovieSceneUserExportFBXControlRigSettings.export_local_time(value: bool) -> None
unreal.MovieSceneUserExportFBXControlRigSettings.fbx_export_compatibility(value: FbxExportCompatibility) -> None
unreal.MovieSceneUserExportFBXControlRigSettings.load_control_mappings_from_preset(meta_human_preset: bool) -> None
```

## `unreal.MovieSceneUserImportFBXControlRigSettings(Object)`

```python
unreal.MovieSceneUserImportFBXControlRigSettings.load_control_mappings_from_preset(meta_human_preset: bool) -> None
```

## `unreal.NonBlendableFloatAnimationAttribute(FloatAnimationAttribute)`

```python
unreal.NonBlendableFloatAnimationAttribute.__init__(value: float = 0.000000) -> None
```

## `unreal.NonBlendableIntegerAnimationAttribute(IntegerAnimationAttribute)`

```python
unreal.NonBlendableIntegerAnimationAttribute.__init__(value: int = 0) -> None
```

## `unreal.NonBlendableQuaternionAnimationAttribute(QuaternionAnimationAttribute)`

```python
unreal.NonBlendableQuaternionAnimationAttribute.__init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

## `unreal.NonBlendableVectorAnimationAttribute(VectorAnimationAttribute)`

```python
unreal.NonBlendableVectorAnimationAttribute.__init__(value: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

## `unreal.OnAllMontageInstancesEndedMCDelegate(MulticastDelegateBase)`

```python
unreal.OnAllMontageInstancesEndedMCDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAnimInitialized(MulticastDelegateBase)`

```python
unreal.OnAnimInitialized.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMontageBlendedInEndedMCDelegate(MulticastDelegateBase)`

```python
unreal.OnMontageBlendedInEndedMCDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMontageBlendingOutStartedMCDelegate(MulticastDelegateBase)`

```python
unreal.OnMontageBlendingOutStartedMCDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMontageEndedMCDelegate(MulticastDelegateBase)`

```python
unreal.OnMontageEndedMCDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMontagePlayDelegate(MulticastDelegateBase)`

```python
unreal.OnMontagePlayDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMontageStartedMCDelegate(MulticastDelegateBase)`

```python
unreal.OnMontageStartedMCDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnWidgetAnimationPlaybackStatusChanged(MulticastDelegateBase)`

```python
unreal.OnWidgetAnimationPlaybackStatusChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OptimusAdvancedSkeletonDataProvider(ComputeDataProvider)`

```python
unreal.OptimusAdvancedSkeletonDataProvider.skeletal_mesh(value: SkeletalMeshComponent) -> None
```

## `unreal.OptimusAnimAttributeDataProvider(ComputeDataProvider)`

```python
unreal.OptimusAnimAttributeDataProvider.skeletal_mesh(value: SkeletalMeshComponent) -> None
```

## `unreal.OptimusGroomDataProvider(ComputeDataProvider)`

```python
unreal.OptimusGroomDataProvider.groom(value: GroomComponent) -> None
```

## `unreal.OptimusGroomGuideDataProvider(ComputeDataProvider)`

```python
unreal.OptimusGroomGuideDataProvider.groom(value: GroomComponent) -> None
```

## `unreal.OptimusGroomWriteDataProvider(ComputeDataProvider)`

```python
unreal.OptimusGroomWriteDataProvider.groom_component(value: GroomComponent) -> None
```

## `unreal.OptimusSkeletonDataProvider(ComputeDataProvider)`

```python
unreal.OptimusSkeletonDataProvider.skinned_mesh(value: SkinnedMeshComponent) -> None
```

## `unreal.PBIKBoneSetting(StructBase)`

```python
unreal.PBIKBoneSetting.__init__(bone: Name = "None", rotation_stiffness: float = 0.000000, position_stiffness: float = 0.000000, x: PBIKLimitType = PBIKLimitType.FREE, min_x: float = 0.000000, max_x: float = 0.000000, y: PBIKLimitType = PBIKLimitType.FREE, min_y: float = 0.000000, max_y: float = 0.000000, z: PBIKLimitType = PBIKLimitType.FREE, min_z: float = 0.000000, max_z: float = 0.000000, use_preferred_angles: bool = False, preferred_angles: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.PBIKBoneSetting.bone(value: Name) -> None
unreal.PBIKBoneSetting.max_x(value: float) -> None
unreal.PBIKBoneSetting.max_y(value: float) -> None
unreal.PBIKBoneSetting.max_z(value: float) -> None
unreal.PBIKBoneSetting.min_x(value: float) -> None
unreal.PBIKBoneSetting.min_y(value: float) -> None
unreal.PBIKBoneSetting.min_z(value: float) -> None
unreal.PBIKBoneSetting.position_stiffness(value: float) -> None
unreal.PBIKBoneSetting.preferred_angles(value: Vector) -> None
unreal.PBIKBoneSetting.rotation_stiffness(value: float) -> None
unreal.PBIKBoneSetting.use_preferred_angles(value: bool) -> None
unreal.PBIKBoneSetting.x(value: PBIKLimitType) -> None
unreal.PBIKBoneSetting.y(value: PBIKLimitType) -> None
unreal.PBIKBoneSetting.z(value: PBIKLimitType) -> None
```

## `unreal.PerBoneBlendWeight(StructBase)`

```python
unreal.PerBoneBlendWeight.__init__() -> None
```

## `unreal.PerBoneBlendWeights(StructBase)`

```python
unreal.PerBoneBlendWeights.__init__() -> None
```

## `unreal.PerBoneInterpolation(StructBase)`

```python
unreal.PerBoneInterpolation.__init__() -> None
```

## `unreal.PerSkeletonAnimationSharingSetup(StructBase)`

```python
unreal.PerSkeletonAnimationSharingSetup.__init__() -> None
```

## `unreal.PhysicalAnimationComponent(ActorComponent)`

```python
unreal.PhysicalAnimationComponent.apply_physical_animation_profile_below(body_name: Name, profile_name: Name, include_self: bool = True, clear_not_found: bool = False) -> None
unreal.PhysicalAnimationComponent.apply_physical_animation_settings(body_name: Name, physical_animation_data: PhysicalAnimationData) -> None
unreal.PhysicalAnimationComponent.apply_physical_animation_settings_below(body_name: Name, physical_animation_data: PhysicalAnimationData, include_self: bool = True) -> None
unreal.PhysicalAnimationComponent.get_body_target_transform(body_name: Name) -> Transform
unreal.PhysicalAnimationComponent.set_skeletal_mesh_component(skeletal_mesh_component: SkeletalMeshComponent) -> None
unreal.PhysicalAnimationComponent.set_strength_multiplyer(strength_multiplyer: float) -> None
unreal.PhysicalAnimationComponent.strength_multiplyer() -> float
```

## `unreal.PhysicalAnimationData(StructBase)`

```python
unreal.PhysicalAnimationData.__init__(is_local_simulation: bool = False, orientation_strength: float = 0.000000, angular_velocity_strength: float = 0.000000, position_strength: float = 0.000000, velocity_strength: float = 0.000000, max_linear_force: float = 0.000000, max_angular_force: float = 0.000000) -> None
unreal.PhysicalAnimationData.angular_velocity_strength(value: float) -> None
unreal.PhysicalAnimationData.is_local_simulation(value: bool) -> None
unreal.PhysicalAnimationData.max_angular_force(value: float) -> None
unreal.PhysicalAnimationData.max_linear_force(value: float) -> None
unreal.PhysicalAnimationData.orientation_strength(value: float) -> None
unreal.PhysicalAnimationData.position_strength(value: float) -> None
unreal.PhysicalAnimationData.velocity_strength(value: float) -> None
```

## `unreal.PinBoneData(StructBase)`

```python
unreal.PinBoneData.__init__() -> None
```

## `unreal.PlayAnimWaitSimpleDelegate(MulticastDelegateBase)`

```python
unreal.PlayAnimWaitSimpleDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PlayMontageAnimNotifyDelegate(MulticastDelegateBase)`

```python
unreal.PlayMontageAnimNotifyDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PlayMontageCallbackProxy(Object)`

```python
unreal.PlayMontageCallbackProxy.on_blend_out(value: OnMontagePlayDelegate) -> None
unreal.PlayMontageCallbackProxy.on_completed(value: OnMontagePlayDelegate) -> None
unreal.PlayMontageCallbackProxy.on_interrupted(value: OnMontagePlayDelegate) -> None
unreal.PlayMontageCallbackProxy.on_notify_begin(value: OnMontagePlayDelegate) -> None
unreal.PlayMontageCallbackProxy.on_notify_end(value: OnMontagePlayDelegate) -> None
```

## `unreal.PoseAsset(AnimationAsset)`

```python
unreal.PoseAsset.clear_retarget_source_asset() -> None
unreal.PoseAsset.get_base_pose_name() -> Name
unreal.PoseAsset.get_pose_names() -> Array[Name]
unreal.PoseAsset.get_retarget_source_asset() -> SkeletalMesh
unreal.PoseAsset.rename_pose(original_pose_name: Name, new_pose_name: Name) -> None
unreal.PoseAsset.set_base_pose_name(new_base_pose_name: Name) -> bool
unreal.PoseAsset.set_retarget_source_asset(retarget_source_asset: SkeletalMesh) -> None
unreal.PoseAsset.update_pose_from_animation(anim_sequence: AnimSequence) -> None
unreal.PoseAsset.update_retarget_source_asset_data() -> None
```

## `unreal.PoseDriverTarget(StructBase)`

```python
unreal.PoseDriverTarget.__init__() -> None
```

## `unreal.PoseLink(PoseLinkBase)`

```python
unreal.PoseLink.__init__() -> None
```

## `unreal.PoseLinkBase(StructBase)`

```python
unreal.PoseLinkBase.__init__() -> None
```

## `unreal.PoseSnapshot(StructBase)`

```python
unreal.PoseSnapshot.__init__(local_transforms: Array[Transform] = [], bone_names: Array[Name] = [], skeletal_mesh_name: Name = "None", snapshot_name: Name = "None", is_valid: bool = False) -> None
unreal.PoseSnapshot.bone_names(value: Array[Name]) -> None
unreal.PoseSnapshot.is_valid(value: bool) -> None
unreal.PoseSnapshot.local_transforms(value: Array[Transform]) -> None
unreal.PoseSnapshot.skeletal_mesh_name(value: Name) -> None
unreal.PoseSnapshot.snapshot_name(value: Name) -> None
```

## `unreal.PoseableMeshComponent(SkinnedMeshComponent)`

```python
unreal.PoseableMeshComponent.copy_pose_from_skeletal_component(component_to_copy: SkeletalMeshComponent) -> None
unreal.PoseableMeshComponent.get_bone_location_by_name(bone_name: Name, bone_space: BoneSpaces) -> Vector
unreal.PoseableMeshComponent.get_bone_rotation_by_name(bone_name: Name, bone_space: BoneSpaces) -> Rotator
unreal.PoseableMeshComponent.get_bone_scale_by_name(bone_name: Name, bone_space: BoneSpaces) -> Vector
unreal.PoseableMeshComponent.get_bone_transform_by_name(bone_name: Name, bone_space: BoneSpaces) -> Transform
unreal.PoseableMeshComponent.reset_bone_transform_by_name(bone_name: Name) -> None
unreal.PoseableMeshComponent.set_bone_location_by_name(bone_name: Name, location: Vector, bone_space: BoneSpaces) -> None
unreal.PoseableMeshComponent.set_bone_rotation_by_name(bone_name: Name, rotation: Rotator, bone_space: BoneSpaces) -> None
unreal.PoseableMeshComponent.set_bone_scale_by_name(bone_name: Name, scale3d: Vector, bone_space: BoneSpaces) -> None
unreal.PoseableMeshComponent.set_bone_transform_by_name(bone_name: Name, transform: Transform, bone_space: BoneSpaces) -> None
```

## `unreal.PostEvaluateAnimEvent(DelegateBase)`

```python
unreal.PostEvaluateAnimEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PythonControlRigLib(BlueprintFunctionLibrary)`

```python
unreal.PythonControlRigLib.get_control_shape_transform(rig_hierarchy: RigHierarchy, control_element: RigElementKey, initial: bool = True) -> Transform
```

## `unreal.QuaternionAnimationAttribute(StructBase)`

```python
unreal.QuaternionAnimationAttribute.__init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.QuaternionAnimationAttribute.value(value: Quat) -> None
```

## `unreal.RawAnimSequenceTrack(StructBase)`

```python
unreal.RawAnimSequenceTrack.__init__() -> None
unreal.RawAnimSequenceTrack.get_positional_keys() -> Array[Vector]
unreal.RawAnimSequenceTrack.get_rotational_keys() -> Array[Quat]
unreal.RawAnimSequenceTrack.get_scale_keys() -> Array[Vector]
```

## `unreal.RawAnimSequenceTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.RawAnimSequenceTrackExtensions.get_positional_keys(track: RawAnimSequenceTrack) -> Array[Vector]
unreal.RawAnimSequenceTrackExtensions.get_rotational_keys(track: RawAnimSequenceTrack) -> Array[Quat]
unreal.RawAnimSequenceTrackExtensions.get_scale_keys(track: RawAnimSequenceTrack) -> Array[Vector]
```

## `unreal.ReOrientRootBoneModifier(AnimationModifier)`

```python
unreal.ReOrientRootBoneModifier.rotator() -> Rotator
```

## `unreal.ReferenceBoneFrame(StructBase)`

```python
unreal.ReferenceBoneFrame.__init__() -> None
```

## `unreal.RigBone(RigElement)`

```python
unreal.RigBone.__init__(name: Name = "None", index: int = 0, parent_name: Name = "None", initial_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], global_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], local_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], type: RigBoneType = RigBoneType.IMPORTED) -> None
unreal.RigBone.global_transform() -> Transform
unreal.RigBone.initial_transform() -> Transform
unreal.RigBone.local_transform() -> Transform
unreal.RigBone.parent_name() -> Name
unreal.RigBone.type() -> RigBoneType
```

## `unreal.RigBoneElement(RigSingleParentElement)`

```python
unreal.RigBoneElement.__init__(key: RigElementKey = [RigElementType.NONE, "None"], index: int = 0, sub_index: int = 0, created_at_instruction_index: int = 0, selected: bool = False, bone_type: RigBoneType = RigBoneType.IMPORTED) -> None
unreal.RigBoneElement.bone_type() -> RigBoneType
```

## `unreal.RigDispatch_AnimAttributeBase(RigDispatchFactory)`

```python
unreal.RigDispatch_AnimAttributeBase.__init__() -> None
```

## `unreal.RigDispatch_GetAnimAttribute(RigDispatch_AnimAttributeBase)`

```python
unreal.RigDispatch_GetAnimAttribute.__init__() -> None
```

## `unreal.RigDispatch_SetAnimAttribute(RigDispatch_AnimAttributeBase)`

```python
unreal.RigDispatch_SetAnimAttribute.__init__() -> None
```

## `unreal.RigPose(StructBase)`

```python
unreal.RigPose.__init__() -> None
```

## `unreal.RigPoseElement(StructBase)`

```python
unreal.RigPoseElement.__init__() -> None
```

## `unreal.RigUnit_AimBone(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_AimBone.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", primary: RigUnit_AimBone_Target = [1.000000, [1.000000, 0.000000, 0.000000], [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, "None"], secondary: RigUnit_AimBone_Target = [1.000000, [1.000000, 0.000000, 0.000000], [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, "None"], weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_AimBone_DebugSettings = [False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_AimBone.bone(value: Name) -> None
unreal.RigUnit_AimBone.debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
unreal.RigUnit_AimBone.primary(value: RigUnit_AimBone_Target) -> None
unreal.RigUnit_AimBone.propagate_to_children() -> bool
unreal.RigUnit_AimBone.secondary(value: RigUnit_AimBone_Target) -> None
unreal.RigUnit_AimBone.weight(value: float) -> None
```

## `unreal.RigUnit_AimBoneMath(RigUnit_HighlevelBase)`

```python
unreal.RigUnit_AimBoneMath.__init__(input_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], primary: RigUnit_AimItem_Target = [1.000000, [1.000000, 0.000000, 0.000000], [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, [RigElementType.BONE, "None"]], secondary: RigUnit_AimItem_Target = [1.000000, [1.000000, 0.000000, 0.000000], [1.000000, 0.000000, 0.000000], ControlRigVectorKind.LOCATION, [RigElementType.BONE, "None"]], weight: float = 0.000000, result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], debug_settings: RigUnit_AimBone_DebugSettings = [False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_AimBoneMath.debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
unreal.RigUnit_AimBoneMath.input_transform(value: Transform) -> None
unreal.RigUnit_AimBoneMath.primary(value: RigUnit_AimItem_Target) -> None
unreal.RigUnit_AimBoneMath.result() -> Transform
unreal.RigUnit_AimBoneMath.secondary(value: RigUnit_AimItem_Target) -> None
unreal.RigUnit_AimBoneMath.weight(value: float) -> None
```

## `unreal.RigUnit_AimBone_DebugSettings(StructBase)`

```python
unreal.RigUnit_AimBone_DebugSettings.__init__(enabled: bool = False, scale: float = 0.000000, world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_AimBone_DebugSettings.enabled(value: bool) -> None
unreal.RigUnit_AimBone_DebugSettings.scale(value: float) -> None
unreal.RigUnit_AimBone_DebugSettings.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_AimBone_Target(StructBase)`

```python
unreal.RigUnit_AimBone_Target.__init__(weight: float = 0.000000, axis: Vector = [0.000000, 0.000000, 0.000000], target: Vector = [0.000000, 0.000000, 0.000000], kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION, space: Name = "None") -> None
unreal.RigUnit_AimBone_Target.axis(value: Vector) -> None
unreal.RigUnit_AimBone_Target.kind(value: ControlRigVectorKind) -> None
unreal.RigUnit_AimBone_Target.space(value: Name) -> None
unreal.RigUnit_AimBone_Target.target(value: Vector) -> None
unreal.RigUnit_AimBone_Target.weight(value: float) -> None
```

## `unreal.RigUnit_AnimBase(RigVMFunction_AnimBase)`

```python
unreal.RigUnit_AnimBase.__init__() -> None
```

## `unreal.RigUnit_AnimEasing(RigVMFunction_AnimEasing)`

```python
unreal.RigUnit_AnimEasing.__init__(value: float = 0.000000, type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, source_minimum: float = 0.000000, source_maximum: float = 0.000000, target_minimum: float = 0.000000, target_maximum: float = 0.000000, result: float = 0.000000) -> None
```

## `unreal.RigUnit_AnimEasingType(RigVMFunction_AnimEasingType)`

```python
unreal.RigUnit_AnimEasingType.__init__(type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR) -> None
```

## `unreal.RigUnit_AnimEvalRichCurve(RigVMFunction_AnimEvalRichCurve)`

```python
unreal.RigUnit_AnimEvalRichCurve.__init__(value: float = 0.000000, curve: RuntimeFloatCurve = [], source_minimum: float = 0.000000, source_maximum: float = 0.000000, target_minimum: float = 0.000000, target_maximum: float = 0.000000, result: float = 0.000000) -> None
```

## `unreal.RigUnit_AnimRichCurve(RigVMFunction_AnimRichCurve)`

```python
unreal.RigUnit_AnimRichCurve.__init__(curve: RuntimeFloatCurve = []) -> None
```

## `unreal.RigUnit_BoneHarmonics(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_BoneHarmonics.__init__(execute_context: ControlRigExecuteContext = [], bones: Array[RigUnit_BoneHarmonics_BoneTarget] = [], wave_speed: Vector = [0.000000, 0.000000, 0.000000], wave_frequency: Vector = [0.000000, 0.000000, 0.000000], wave_amplitude: Vector = [0.000000, 0.000000, 0.000000], wave_offset: Vector = [0.000000, 0.000000, 0.000000], wave_noise: Vector = [0.000000, 0.000000, 0.000000], wave_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, wave_minimum: float = 0.000000, wave_maximum: float = 0.000000, rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ, propagate_to_children: bool = False) -> None
unreal.RigUnit_BoneHarmonics.bones() -> Array[RigUnit_BoneHarmonics_BoneTarget]
unreal.RigUnit_BoneHarmonics.propagate_to_children() -> bool
unreal.RigUnit_BoneHarmonics.rotation_order(value: EulerRotationOrder) -> None
unreal.RigUnit_BoneHarmonics.wave_amplitude(value: Vector) -> None
unreal.RigUnit_BoneHarmonics.wave_ease(value: RigVMAnimEasingType) -> None
unreal.RigUnit_BoneHarmonics.wave_frequency(value: Vector) -> None
unreal.RigUnit_BoneHarmonics.wave_maximum(value: float) -> None
unreal.RigUnit_BoneHarmonics.wave_minimum(value: float) -> None
unreal.RigUnit_BoneHarmonics.wave_noise(value: Vector) -> None
unreal.RigUnit_BoneHarmonics.wave_offset(value: Vector) -> None
unreal.RigUnit_BoneHarmonics.wave_speed(value: Vector) -> None
```

## `unreal.RigUnit_BoneHarmonics_BoneTarget(StructBase)`

```python
unreal.RigUnit_BoneHarmonics_BoneTarget.__init__(bone: Name = "None", ratio: float = 0.000000) -> None
unreal.RigUnit_BoneHarmonics_BoneTarget.bone(value: Name) -> None
unreal.RigUnit_BoneHarmonics_BoneTarget.ratio() -> float
```

## `unreal.RigUnit_BoneName(RigUnit)`

```python
unreal.RigUnit_BoneName.__init__(bone: Name = "None") -> None
unreal.RigUnit_BoneName.bone(value: Name) -> None
```

## `unreal.RigUnit_ClosestParameterFromControlRigSpline(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_ClosestParameterFromControlRigSpline.__init__(spline: ControlRigSpline = [], position: Vector = [0.000000, 0.000000, 0.000000], u: float = 0.000000) -> None
unreal.RigUnit_ClosestParameterFromControlRigSpline.position(value: Vector) -> None
unreal.RigUnit_ClosestParameterFromControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_ClosestParameterFromControlRigSpline.u() -> float
```

## `unreal.RigUnit_ControlRigSplineBase(RigUnit)`

```python
unreal.RigUnit_ControlRigSplineBase.__init__() -> None
```

## `unreal.RigUnit_ControlRigSplineFromPoints(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_ControlRigSplineFromPoints.__init__(points: Array[Vector] = [], spline_mode: SplineType = SplineType.B_SPLINE, closed: bool = False, samples_per_segment: int = 0, compression: float = 0.000000, stretch: float = 0.000000, spline: ControlRigSpline = []) -> None
unreal.RigUnit_ControlRigSplineFromPoints.closed(value: bool) -> None
unreal.RigUnit_ControlRigSplineFromPoints.compression(value: float) -> None
unreal.RigUnit_ControlRigSplineFromPoints.points(value: Array[Vector]) -> None
unreal.RigUnit_ControlRigSplineFromPoints.samples_per_segment(value: int) -> None
unreal.RigUnit_ControlRigSplineFromPoints.spline() -> ControlRigSpline
unreal.RigUnit_ControlRigSplineFromPoints.spline_mode(value: SplineType) -> None
unreal.RigUnit_ControlRigSplineFromPoints.stretch(value: float) -> None
```

## `unreal.RigUnit_DebugPose(RigVMFunction_DebugBase)`

```python
unreal.RigUnit_DebugPose.__init__(execute_context: ControlRigExecuteContext = [], pose: RigPose = [], items: Array[RigElementKey] = [], scale: float = 0.000000, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], enabled: bool = False) -> None
unreal.RigUnit_DebugPose.color(value: LinearColor) -> None
unreal.RigUnit_DebugPose.enabled(value: bool) -> None
unreal.RigUnit_DebugPose.execute_context(value: ControlRigExecuteContext) -> None
unreal.RigUnit_DebugPose.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_DebugPose.pose(value: RigPose) -> None
unreal.RigUnit_DebugPose.scale(value: float) -> None
unreal.RigUnit_DebugPose.thickness(value: float) -> None
unreal.RigUnit_DebugPose.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_DrawControlRigSpline(RigUnitMutable)`

```python
unreal.RigUnit_DrawControlRigSpline.__init__(execute_context: ControlRigExecuteContext = [], spline: ControlRigSpline = [], color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], thickness: float = 0.000000, detail: int = 0) -> None
unreal.RigUnit_DrawControlRigSpline.color(value: LinearColor) -> None
unreal.RigUnit_DrawControlRigSpline.detail(value: int) -> None
unreal.RigUnit_DrawControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_DrawControlRigSpline.thickness(value: float) -> None
```

## `unreal.RigUnit_GetAnimationChannelBase(RigUnit)`

```python
unreal.RigUnit_GetAnimationChannelBase.__init__(control: Name = "None", channel: Name = "None", initial: bool = False) -> None
unreal.RigUnit_GetAnimationChannelBase.channel(value: Name) -> None
unreal.RigUnit_GetAnimationChannelBase.control(value: Name) -> None
unreal.RigUnit_GetAnimationChannelBase.initial(value: bool) -> None
```

## `unreal.RigUnit_GetAnimationChannelFromItemBase(RigUnit)`

```python
unreal.RigUnit_GetAnimationChannelFromItemBase.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False) -> None
unreal.RigUnit_GetAnimationChannelFromItemBase.initial(value: bool) -> None
unreal.RigUnit_GetAnimationChannelFromItemBase.item(value: RigElementKey) -> None
```

## `unreal.RigUnit_GetBoolAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetBoolAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: bool = False) -> None
unreal.RigUnit_GetBoolAnimationChannel.value() -> bool
```

## `unreal.RigUnit_GetBoolAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetBoolAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: bool = False) -> None
unreal.RigUnit_GetBoolAnimationChannelFromItem.value() -> bool
```

## `unreal.RigUnit_GetFloatAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetFloatAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: float = 0.000000) -> None
unreal.RigUnit_GetFloatAnimationChannel.value() -> float
```

## `unreal.RigUnit_GetFloatAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetFloatAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: float = 0.000000) -> None
unreal.RigUnit_GetFloatAnimationChannelFromItem.value() -> float
```

## `unreal.RigUnit_GetIntAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetIntAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: int = 0) -> None
unreal.RigUnit_GetIntAnimationChannel.value() -> int
```

## `unreal.RigUnit_GetIntAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetIntAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: int = 0) -> None
unreal.RigUnit_GetIntAnimationChannelFromItem.value() -> int
```

## `unreal.RigUnit_GetLengthAtParamControlRigSpline(RigUnit)`

```python
unreal.RigUnit_GetLengthAtParamControlRigSpline.__init__(spline: ControlRigSpline = [], u: float = 0.000000, length: float = 0.000000) -> None
unreal.RigUnit_GetLengthAtParamControlRigSpline.length() -> float
unreal.RigUnit_GetLengthAtParamControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_GetLengthAtParamControlRigSpline.u(value: float) -> None
```

## `unreal.RigUnit_GetLengthControlRigSpline(RigUnit)`

```python
unreal.RigUnit_GetLengthControlRigSpline.__init__(spline: ControlRigSpline = [], length: float = 0.000000) -> None
unreal.RigUnit_GetLengthControlRigSpline.length() -> float
unreal.RigUnit_GetLengthControlRigSpline.spline(value: ControlRigSpline) -> None
```

## `unreal.RigUnit_GetRotatorAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetRotatorAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_GetRotatorAnimationChannel.value() -> Rotator
```

## `unreal.RigUnit_GetRotatorAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetRotatorAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_GetRotatorAnimationChannelFromItem.value() -> Rotator
```

## `unreal.RigUnit_GetVector2DAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetVector2DAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: Vector2D = [0.000000, 0.000000]) -> None
unreal.RigUnit_GetVector2DAnimationChannel.value() -> Vector2D
```

## `unreal.RigUnit_GetVector2DAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetVector2DAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: Vector2D = [0.000000, 0.000000]) -> None
unreal.RigUnit_GetVector2DAnimationChannelFromItem.value() -> Vector2D
```

## `unreal.RigUnit_GetVectorAnimationChannel(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_GetVectorAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_GetVectorAnimationChannel.value() -> Vector
```

## `unreal.RigUnit_GetVectorAnimationChannelFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_GetVectorAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_GetVectorAnimationChannelFromItem.value() -> Vector
```

## `unreal.RigUnit_HierarchyAddAnimationChannel2DLimitSettings(RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings)`

```python
unreal.RigUnit_HierarchyAddAnimationChannel2DLimitSettings.__init__(x: RigControlLimitEnabled = [False, False], y: RigControlLimitEnabled = [False, False]) -> None
unreal.RigUnit_HierarchyAddAnimationChannel2DLimitSettings.x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddAnimationChannel2DLimitSettings.y(value: RigControlLimitEnabled) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelBool(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelBool.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: bool = False, minimum_value: bool = False, maximum_value: bool = False, limits_enabled: RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings = []) -> None
unreal.RigUnit_HierarchyAddAnimationChannelBool.initial_value(value: bool) -> None
unreal.RigUnit_HierarchyAddAnimationChannelBool.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelBool.maximum_value(value: bool) -> None
unreal.RigUnit_HierarchyAddAnimationChannelBool.minimum_value(value: bool) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings.__init__() -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelFloat(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelFloat.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: float = 0.000000, minimum_value: float = 0.000000, maximum_value: float = 0.000000, limits_enabled: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings = [[True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelFloat.initial_value(value: float) -> None
unreal.RigUnit_HierarchyAddAnimationChannelFloat.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelFloat.maximum_value(value: float) -> None
unreal.RigUnit_HierarchyAddAnimationChannelFloat.minimum_value(value: float) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelInteger(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelInteger.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: int = 0, minimum_value: int = 0, maximum_value: int = 0, limits_enabled: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings = [[True, True]], control_enum: Enum = None) -> None
unreal.RigUnit_HierarchyAddAnimationChannelInteger.control_enum(value: Enum) -> None
unreal.RigUnit_HierarchyAddAnimationChannelInteger.initial_value(value: int) -> None
unreal.RigUnit_HierarchyAddAnimationChannelInteger.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelInteger.maximum_value(value: int) -> None
unreal.RigUnit_HierarchyAddAnimationChannelInteger.minimum_value(value: int) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelRotator(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelRotator.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: Rotator = [0.000000, 0.000000, 0.000000], minimum_value: Rotator = [0.000000, 0.000000, 0.000000], maximum_value: Rotator = [0.000000, 0.000000, 0.000000], limits_enabled: RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings = [[True, True], [True, True], [True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotator.initial_value(value: Rotator) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotator.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotator.maximum_value(value: Rotator) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotator.minimum_value(value: Rotator) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings(RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings.__init__(pitch: RigControlLimitEnabled = [False, False], yaw: RigControlLimitEnabled = [False, False], roll: RigControlLimitEnabled = [False, False]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings.pitch(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings.roll(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddAnimationChannelRotatorLimitSettings.yaw(value: RigControlLimitEnabled) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: float = 0.000000, minimum_value: float = 0.000000, maximum_value: float = 0.000000, limits_enabled: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings = [[True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.initial_value(value: float) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelSingleLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.maximum_value(value: float) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleFloat.minimum_value(value: float) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelScaleVector(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelScaleVector.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: Vector = [0.000000, 0.000000, 0.000000], minimum_value: Vector = [0.000000, 0.000000, 0.000000], maximum_value: Vector = [0.000000, 0.000000, 0.000000], limits_enabled: RigUnit_HierarchyAddAnimationChannelVectorLimitSettings = [[True, True], [True, True], [True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleVector.initial_value(value: Vector) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleVector.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelVectorLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleVector.maximum_value(value: Vector) -> None
unreal.RigUnit_HierarchyAddAnimationChannelScaleVector.minimum_value(value: Vector) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelSingleLimitSettings(RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelSingleLimitSettings.__init__(enabled: RigControlLimitEnabled = [False, False]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelSingleLimitSettings.enabled(value: RigControlLimitEnabled) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelVector(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelVector.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: Vector = [0.000000, 0.000000, 0.000000], minimum_value: Vector = [0.000000, 0.000000, 0.000000], maximum_value: Vector = [0.000000, 0.000000, 0.000000], limits_enabled: RigUnit_HierarchyAddAnimationChannelVectorLimitSettings = [[True, True], [True, True], [True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector.initial_value(value: Vector) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector.limits_enabled(value: RigUnit_HierarchyAddAnimationChannelVectorLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector.maximum_value(value: Vector) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector.minimum_value(value: Vector) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelVector2D(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelVector2D.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], initial_value: Vector2D = [0.000000, 0.000000], minimum_value: Vector2D = [0.000000, 0.000000], maximum_value: Vector2D = [0.000000, 0.000000], limits_enabled: RigUnit_HierarchyAddAnimationChannel2DLimitSettings = [[True, True], [True, True]]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector2D.initial_value(value: Vector2D) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector2D.limits_enabled(value: RigUnit_HierarchyAddAnimationChannel2DLimitSettings) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector2D.maximum_value(value: Vector2D) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVector2D.minimum_value(value: Vector2D) -> None
```

## `unreal.RigUnit_HierarchyAddAnimationChannelVectorLimitSettings(RigUnit_HierarchyAddAnimationChannelEmptyLimitSettings)`

```python
unreal.RigUnit_HierarchyAddAnimationChannelVectorLimitSettings.__init__(x: RigControlLimitEnabled = [False, False], y: RigControlLimitEnabled = [False, False], z: RigControlLimitEnabled = [False, False]) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVectorLimitSettings.x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVectorLimitSettings.y(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddAnimationChannelVectorLimitSettings.z(value: RigControlLimitEnabled) -> None
```

## `unreal.RigUnit_HierarchyAddBone(RigUnit_HierarchyAddElement)`

```python
unreal.RigUnit_HierarchyAddBone.__init__(execute_context: ControlRigExecuteContext = [], parent: RigElementKey = [RigElementType.NONE, "None"], name: Name = "None", item: RigElementKey = [RigElementType.NONE, "None"], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
unreal.RigUnit_HierarchyAddBone.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchyAddBone.transform(value: Transform) -> None
```

## `unreal.RigUnit_HierarchyCreatePoseItemArray(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_HierarchyCreatePoseItemArray.__init__(entries: Array[RigUnit_HierarchyCreatePoseItemArray_Entry] = [], pose: RigPose = []) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray.entries(value: Array[RigUnit_HierarchyCreatePoseItemArray_Entry]) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray.pose() -> RigPose
```

## `unreal.RigUnit_HierarchyCreatePoseItemArray_Entry(StructBase)`

```python
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.__init__(item: RigElementKey = [RigElementType.NONE, "None"], local_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], global_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], use_euler_angles: bool = False, euler_angles: Vector = [0.000000, 0.000000, 0.000000], curve_value: float = 0.000000) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.curve_value(value: float) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.euler_angles(value: Vector) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.global_transform(value: Transform) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.item(value: RigElementKey) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.local_transform(value: Transform) -> None
unreal.RigUnit_HierarchyCreatePoseItemArray_Entry.use_euler_angles(value: bool) -> None
```

## `unreal.RigUnit_HierarchyGetPose(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_HierarchyGetPose.__init__(initial: bool = False, element_type: RigElementType = RigElementType.NONE, items_to_get: RigElementKeyCollection = [[]], pose: RigPose = []) -> None
unreal.RigUnit_HierarchyGetPose.element_type(value: RigElementType) -> None
unreal.RigUnit_HierarchyGetPose.initial(value: bool) -> None
unreal.RigUnit_HierarchyGetPose.items_to_get(value: RigElementKeyCollection) -> None
unreal.RigUnit_HierarchyGetPose.pose() -> RigPose
```

## `unreal.RigUnit_HierarchyGetPoseItemArray(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_HierarchyGetPoseItemArray.__init__(initial: bool = False, element_type: RigElementType = RigElementType.NONE, items_to_get: Array[RigElementKey] = [], pose: RigPose = []) -> None
unreal.RigUnit_HierarchyGetPoseItemArray.element_type(value: RigElementType) -> None
unreal.RigUnit_HierarchyGetPoseItemArray.initial(value: bool) -> None
unreal.RigUnit_HierarchyGetPoseItemArray.items_to_get(value: Array[RigElementKey]) -> None
unreal.RigUnit_HierarchyGetPoseItemArray.pose() -> RigPose
```

## `unreal.RigUnit_HierarchyImportFromSkeleton(RigUnit_DynamicHierarchyBaseMutable)`

```python
unreal.RigUnit_HierarchyImportFromSkeleton.__init__(execute_context: ControlRigExecuteContext = [], name_space: Name = "None", include_curves: bool = False, items: Array[RigElementKey] = []) -> None
unreal.RigUnit_HierarchyImportFromSkeleton.include_curves(value: bool) -> None
unreal.RigUnit_HierarchyImportFromSkeleton.items() -> Array[RigElementKey]
unreal.RigUnit_HierarchyImportFromSkeleton.name_space(value: Name) -> None
```

## `unreal.RigUnit_HierarchySetPose(RigUnit_HierarchyBaseMutable)`

```python
unreal.RigUnit_HierarchySetPose.__init__(execute_context: ControlRigExecuteContext = [], pose: RigPose = [], element_type: RigElementType = RigElementType.NONE, space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, items_to_set: RigElementKeyCollection = [[]], weight: float = 0.000000) -> None
unreal.RigUnit_HierarchySetPose.element_type(value: RigElementType) -> None
unreal.RigUnit_HierarchySetPose.items_to_set(value: RigElementKeyCollection) -> None
unreal.RigUnit_HierarchySetPose.pose(value: RigPose) -> None
unreal.RigUnit_HierarchySetPose.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchySetPose.weight(value: float) -> None
```

## `unreal.RigUnit_HierarchySetPoseItemArray(RigUnit_HierarchyBaseMutable)`

```python
unreal.RigUnit_HierarchySetPoseItemArray.__init__(execute_context: ControlRigExecuteContext = [], pose: RigPose = [], element_type: RigElementType = RigElementType.NONE, space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, items_to_set: Array[RigElementKey] = [], weight: float = 0.000000) -> None
unreal.RigUnit_HierarchySetPoseItemArray.element_type(value: RigElementType) -> None
unreal.RigUnit_HierarchySetPoseItemArray.items_to_set(value: Array[RigElementKey]) -> None
unreal.RigUnit_HierarchySetPoseItemArray.pose(value: RigPose) -> None
unreal.RigUnit_HierarchySetPoseItemArray.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchySetPoseItemArray.weight(value: float) -> None
```

## `unreal.RigUnit_PointSimulation_BoneTarget(StructBase)`

```python
unreal.RigUnit_PointSimulation_BoneTarget.__init__(bone: Name = "None", translation_point: int = 0, primary_aim_point: int = 0, secondary_aim_point: int = 0) -> None
unreal.RigUnit_PointSimulation_BoneTarget.bone(value: Name) -> None
unreal.RigUnit_PointSimulation_BoneTarget.primary_aim_point() -> int
unreal.RigUnit_PointSimulation_BoneTarget.secondary_aim_point() -> int
unreal.RigUnit_PointSimulation_BoneTarget.translation_point() -> int
```

## `unreal.RigUnit_PoseGetCurve(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetCurve.__init__(pose: RigPose = [], curve: Name = "None", valid: bool = False, curve_value: float = 0.000000) -> None
unreal.RigUnit_PoseGetCurve.curve(value: Name) -> None
unreal.RigUnit_PoseGetCurve.curve_value() -> float
unreal.RigUnit_PoseGetCurve.pose(value: RigPose) -> None
unreal.RigUnit_PoseGetCurve.valid() -> bool
```

## `unreal.RigUnit_PoseGetDelta(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetDelta.__init__(pose_a: RigPose = [], pose_b: RigPose = [], position_threshold: float = 0.000000, rotation_threshold: float = 0.000000, scale_threshold: float = 0.000000, curve_threshold: float = 0.000000, element_type: RigElementType = RigElementType.NONE, space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, items_to_compare: RigElementKeyCollection = [[]], poses_are_equal: bool = False, items_with_delta: RigElementKeyCollection = [[]]) -> None
unreal.RigUnit_PoseGetDelta.curve_threshold(value: float) -> None
unreal.RigUnit_PoseGetDelta.element_type(value: RigElementType) -> None
unreal.RigUnit_PoseGetDelta.items_to_compare(value: RigElementKeyCollection) -> None
unreal.RigUnit_PoseGetDelta.items_with_delta() -> RigElementKeyCollection
unreal.RigUnit_PoseGetDelta.pose_a(value: RigPose) -> None
unreal.RigUnit_PoseGetDelta.pose_b(value: RigPose) -> None
unreal.RigUnit_PoseGetDelta.poses_are_equal() -> bool
unreal.RigUnit_PoseGetDelta.position_threshold(value: float) -> None
unreal.RigUnit_PoseGetDelta.rotation_threshold(value: float) -> None
unreal.RigUnit_PoseGetDelta.scale_threshold(value: float) -> None
unreal.RigUnit_PoseGetDelta.space(value: RigVMTransformSpace) -> None
```

## `unreal.RigUnit_PoseGetItems(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetItems.__init__(pose: RigPose = [], element_type: RigElementType = RigElementType.NONE, items: RigElementKeyCollection = [[]]) -> None
unreal.RigUnit_PoseGetItems.element_type(value: RigElementType) -> None
unreal.RigUnit_PoseGetItems.items() -> RigElementKeyCollection
unreal.RigUnit_PoseGetItems.pose(value: RigPose) -> None
```

## `unreal.RigUnit_PoseGetItemsItemArray(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseGetItemsItemArray.__init__(pose: RigPose = [], element_type: RigElementType = RigElementType.NONE, items: Array[RigElementKey] = []) -> None
unreal.RigUnit_PoseGetItemsItemArray.element_type(value: RigElementType) -> None
unreal.RigUnit_PoseGetItemsItemArray.items() -> Array[RigElementKey]
unreal.RigUnit_PoseGetItemsItemArray.pose(value: RigPose) -> None
```

## `unreal.RigUnit_PoseIsEmpty(RigUnit_HierarchyBase)`

```python
unreal.RigUnit_PoseIsEmpty.__init__(pose: RigPose = [], is_empty: bool = False) -> None
unreal.RigUnit_PoseIsEmpty.is_empty() -> bool
unreal.RigUnit_PoseIsEmpty.pose(value: RigPose) -> None
```

## `unreal.RigUnit_PoseLoop(RigUnit_HierarchyBaseMutable)`

```python
unreal.RigUnit_PoseLoop.__init__(execute_context: ControlRigExecuteContext = [], pose: RigPose = [], item: RigElementKey = [RigElementType.NONE, "None"], global_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], local_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], curve_value: float = 0.000000, index: int = 0, count: int = 0, ratio: float = 0.000000, completed: ControlRigExecuteContext = []) -> None
unreal.RigUnit_PoseLoop.completed() -> ControlRigExecuteContext
unreal.RigUnit_PoseLoop.count() -> int
unreal.RigUnit_PoseLoop.curve_value() -> float
unreal.RigUnit_PoseLoop.global_transform() -> Transform
unreal.RigUnit_PoseLoop.index() -> int
unreal.RigUnit_PoseLoop.item() -> RigElementKey
unreal.RigUnit_PoseLoop.local_transform() -> Transform
unreal.RigUnit_PoseLoop.pose(value: RigPose) -> None
unreal.RigUnit_PoseLoop.ratio() -> float
```

## `unreal.RigUnit_PositionFromControlRigSpline(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_PositionFromControlRigSpline.__init__(spline: ControlRigSpline = [], u: float = 0.000000, position: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_PositionFromControlRigSpline.position() -> Vector
unreal.RigUnit_PositionFromControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_PositionFromControlRigSpline.u(value: float) -> None
```

## `unreal.RigUnit_SetAnimationChannelBase(RigUnit_GetAnimationChannelBase)`

```python
unreal.RigUnit_SetAnimationChannelBase.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = []) -> None
unreal.RigUnit_SetAnimationChannelBase.execute_context(value: ControlRigExecuteContext) -> None
```

## `unreal.RigUnit_SetAnimationChannelBaseFromItem(RigUnit_GetAnimationChannelFromItemBase)`

```python
unreal.RigUnit_SetAnimationChannelBaseFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = []) -> None
unreal.RigUnit_SetAnimationChannelBaseFromItem.execute_context(value: ControlRigExecuteContext) -> None
```

## `unreal.RigUnit_SetBoneRotation(RigUnitMutable)`

```python
unreal.RigUnit_SetBoneRotation.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetBoneRotation.bone(value: Name) -> None
unreal.RigUnit_SetBoneRotation.propagate_to_children() -> bool
unreal.RigUnit_SetBoneRotation.rotation(value: Quat) -> None
unreal.RigUnit_SetBoneRotation.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetBoneRotation.weight(value: float) -> None
```

## `unreal.RigUnit_SetBoneTranslation(RigUnitMutable)`

```python
unreal.RigUnit_SetBoneTranslation.__init__(execute_context: ControlRigExecuteContext = [], bone: Name = "None", translation: Vector = [0.000000, 0.000000, 0.000000], space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_SetBoneTranslation.bone(value: Name) -> None
unreal.RigUnit_SetBoneTranslation.propagate_to_children() -> bool
unreal.RigUnit_SetBoneTranslation.space(value: RigVMTransformSpace) -> None
unreal.RigUnit_SetBoneTranslation.translation(value: Vector) -> None
unreal.RigUnit_SetBoneTranslation.weight(value: float) -> None
```

## `unreal.RigUnit_SetBoolAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetBoolAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: bool = False) -> None
unreal.RigUnit_SetBoolAnimationChannel.value(value: bool) -> None
```

## `unreal.RigUnit_SetBoolAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetBoolAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: bool = False) -> None
unreal.RigUnit_SetBoolAnimationChannelFromItem.value(value: bool) -> None
```

## `unreal.RigUnit_SetFloatAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetFloatAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: float = 0.000000) -> None
unreal.RigUnit_SetFloatAnimationChannel.value(value: float) -> None
```

## `unreal.RigUnit_SetFloatAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetFloatAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: float = 0.000000) -> None
unreal.RigUnit_SetFloatAnimationChannelFromItem.value(value: float) -> None
```

## `unreal.RigUnit_SetIntAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetIntAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: int = 0) -> None
unreal.RigUnit_SetIntAnimationChannel.value(value: int) -> None
```

## `unreal.RigUnit_SetIntAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetIntAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: int = 0) -> None
unreal.RigUnit_SetIntAnimationChannelFromItem.value(value: int) -> None
```

## `unreal.RigUnit_SetRotatorAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetRotatorAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_SetRotatorAnimationChannel.value(value: Rotator) -> None
```

## `unreal.RigUnit_SetRotatorAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetRotatorAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_SetRotatorAnimationChannelFromItem.value(value: Rotator) -> None
```

## `unreal.RigUnit_SetVector2DAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetVector2DAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Vector2D = [0.000000, 0.000000]) -> None
unreal.RigUnit_SetVector2DAnimationChannel.value(value: Vector2D) -> None
```

## `unreal.RigUnit_SetVector2DAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetVector2DAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Vector2D = [0.000000, 0.000000]) -> None
unreal.RigUnit_SetVector2DAnimationChannelFromItem.value(value: Vector2D) -> None
```

## `unreal.RigUnit_SetVectorAnimationChannel(RigUnit_SetAnimationChannelBase)`

```python
unreal.RigUnit_SetVectorAnimationChannel.__init__(control: Name = "None", channel: Name = "None", initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_SetVectorAnimationChannel.value(value: Vector) -> None
```

## `unreal.RigUnit_SetVectorAnimationChannelFromItem(RigUnit_SetAnimationChannelBaseFromItem)`

```python
unreal.RigUnit_SetVectorAnimationChannelFromItem.__init__(item: RigElementKey = [RigElementType.NONE, "None"], initial: bool = False, execute_context: ControlRigExecuteContext = [], value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_SetVectorAnimationChannelFromItem.value(value: Vector) -> None
```

## `unreal.RigUnit_SphericalPoseReader(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_SphericalPoseReader.__init__(execute_context: ControlRigExecuteContext = [], output_param: float = 0.000000, driver_item: RigElementKey = [RigElementType.NONE, "None"], driver_axis: Vector = [0.000000, 0.000000, 0.000000], rotation_offset: Vector = [0.000000, 0.000000, 0.000000], active_region_size: float = 0.000000, active_region_scale_factors: RegionScaleFactors = [1.000000, 1.000000, 1.000000, 1.000000], falloff_size: float = 0.000000, falloff_region_scale_factors: RegionScaleFactors = [1.000000, 1.000000, 1.000000, 1.000000], flip_width_scaling: bool = False, flip_height_scaling: bool = False, optional_parent_item: RigElementKey = [RigElementType.NONE, "None"], debug: SphericalPoseReaderDebugSettings = [True, False, False, 25.000000, 20, 0.250000]) -> None
unreal.RigUnit_SphericalPoseReader.active_region_scale_factors(value: RegionScaleFactors) -> None
unreal.RigUnit_SphericalPoseReader.active_region_size(value: float) -> None
unreal.RigUnit_SphericalPoseReader.debug(value: SphericalPoseReaderDebugSettings) -> None
unreal.RigUnit_SphericalPoseReader.driver_axis(value: Vector) -> None
unreal.RigUnit_SphericalPoseReader.driver_item(value: RigElementKey) -> None
unreal.RigUnit_SphericalPoseReader.falloff_region_scale_factors(value: RegionScaleFactors) -> None
unreal.RigUnit_SphericalPoseReader.falloff_size(value: float) -> None
unreal.RigUnit_SphericalPoseReader.flip_height_scaling(value: bool) -> None
unreal.RigUnit_SphericalPoseReader.flip_width_scaling(value: bool) -> None
unreal.RigUnit_SphericalPoseReader.optional_parent_item(value: RigElementKey) -> None
unreal.RigUnit_SphericalPoseReader.output_param() -> float
unreal.RigUnit_SphericalPoseReader.rotation_offset(value: Vector) -> None
```

## `unreal.RigUnit_TangentFromControlRigSpline(RigUnit_ControlRigSplineBase)`

```python
unreal.RigUnit_TangentFromControlRigSpline.__init__(spline: ControlRigSpline = [], u: float = 0.000000, tangent: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_TangentFromControlRigSpline.spline(value: ControlRigSpline) -> None
unreal.RigUnit_TangentFromControlRigSpline.tangent() -> Vector
unreal.RigUnit_TangentFromControlRigSpline.u(value: float) -> None
```

## `unreal.RigUnit_TwistBones(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TwistBones.__init__(execute_context: ControlRigExecuteContext = [], start_bone: Name = "None", end_bone: Name = "None", twist_axis: Vector = [0.000000, 0.000000, 0.000000], pole_axis: Vector = [0.000000, 0.000000, 0.000000], twist_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_TwistBones.end_bone(value: Name) -> None
unreal.RigUnit_TwistBones.pole_axis() -> Vector
unreal.RigUnit_TwistBones.propagate_to_children() -> bool
unreal.RigUnit_TwistBones.start_bone(value: Name) -> None
unreal.RigUnit_TwistBones.twist_axis() -> Vector
unreal.RigUnit_TwistBones.twist_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_TwistBones.weight(value: float) -> None
```

## `unreal.RigUnit_TwistBonesPerItem(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TwistBonesPerItem.__init__(execute_context: ControlRigExecuteContext = [], items: RigElementKeyCollection = [[]], twist_axis: Vector = [0.000000, 0.000000, 0.000000], pole_axis: Vector = [0.000000, 0.000000, 0.000000], twist_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False) -> None
unreal.RigUnit_TwistBonesPerItem.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_TwistBonesPerItem.pole_axis() -> Vector
unreal.RigUnit_TwistBonesPerItem.propagate_to_children() -> bool
unreal.RigUnit_TwistBonesPerItem.twist_axis() -> Vector
unreal.RigUnit_TwistBonesPerItem.twist_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_TwistBonesPerItem.weight(value: float) -> None
```

## `unreal.RigUnit_TwoBoneIKFK(RigUnitMutable)`

```python
unreal.RigUnit_TwoBoneIKFK.__init__(execute_context: ControlRigExecuteContext = [], start_joint: Name = "None", end_joint: Name = "None", pole_target: Vector = [0.000000, 0.000000, 0.000000], spin: float = 0.000000, end_effector: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], ik_blend: float = 0.000000) -> None
unreal.RigUnit_TwoBoneIKFK.end_effector(value: Transform) -> None
unreal.RigUnit_TwoBoneIKFK.end_joint(value: Name) -> None
unreal.RigUnit_TwoBoneIKFK.ik_blend(value: float) -> None
unreal.RigUnit_TwoBoneIKFK.pole_target(value: Vector) -> None
unreal.RigUnit_TwoBoneIKFK.spin(value: float) -> None
unreal.RigUnit_TwoBoneIKFK.start_joint(value: Name) -> None
```

## `unreal.RigUnit_TwoBoneIKSimple(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TwoBoneIKSimple.__init__(execute_context: ControlRigExecuteContext = [], bone_a: Name = "None", bone_b: Name = "None", effector_bone: Name = "None", effector: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis_weight: float = 0.000000, pole_vector: Vector = [0.000000, 0.000000, 0.000000], pole_vector_kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION, pole_vector_space: Name = "None", enable_stretch: bool = False, stretch_start_ratio: float = 0.000000, stretch_maximum_ratio: float = 0.000000, weight: float = 0.000000, bone_a_length: float = 0.000000, bone_b_length: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_TwoBoneIKSimple_DebugSettings = [False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_TwoBoneIKSimple.bone_a(value: Name) -> None
unreal.RigUnit_TwoBoneIKSimple.bone_a_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple.bone_b(value: Name) -> None
unreal.RigUnit_TwoBoneIKSimple.bone_b_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple.debug_settings(value: RigUnit_TwoBoneIKSimple_DebugSettings) -> None
unreal.RigUnit_TwoBoneIKSimple.effector(value: Transform) -> None
unreal.RigUnit_TwoBoneIKSimple.effector_bone(value: Name) -> None
unreal.RigUnit_TwoBoneIKSimple.enable_stretch(value: bool) -> None
unreal.RigUnit_TwoBoneIKSimple.pole_vector(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimple.pole_vector_kind(value: ControlRigVectorKind) -> None
unreal.RigUnit_TwoBoneIKSimple.pole_vector_space(value: Name) -> None
unreal.RigUnit_TwoBoneIKSimple.primary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimple.propagate_to_children() -> bool
unreal.RigUnit_TwoBoneIKSimple.secondary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimple.secondary_axis_weight(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple.stretch_maximum_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple.stretch_start_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple.weight(value: float) -> None
```

## `unreal.RigUnit_TwoBoneIKSimplePerItem(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_TwoBoneIKSimplePerItem.__init__(execute_context: ControlRigExecuteContext = [], item_a: RigElementKey = [RigElementType.NONE, "None"], item_b: RigElementKey = [RigElementType.NONE, "None"], effector_item: RigElementKey = [RigElementType.NONE, "None"], effector: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis_weight: float = 0.000000, pole_vector: Vector = [0.000000, 0.000000, 0.000000], pole_vector_kind: ControlRigVectorKind = ControlRigVectorKind.DIRECTION, pole_vector_space: RigElementKey = [RigElementType.NONE, "None"], enable_stretch: bool = False, stretch_start_ratio: float = 0.000000, stretch_maximum_ratio: float = 0.000000, weight: float = 0.000000, item_a_length: float = 0.000000, item_b_length: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_TwoBoneIKSimple_DebugSettings = [False, 10.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.debug_settings(value: RigUnit_TwoBoneIKSimple_DebugSettings) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.effector(value: Transform) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.effector_item(value: RigElementKey) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.enable_stretch(value: bool) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.item_a(value: RigElementKey) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.item_a_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.item_b(value: RigElementKey) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.item_b_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.pole_vector(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.pole_vector_kind(value: ControlRigVectorKind) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.pole_vector_space(value: RigElementKey) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.primary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.propagate_to_children() -> bool
unreal.RigUnit_TwoBoneIKSimplePerItem.secondary_axis(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.secondary_axis_weight(value: float) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.stretch_maximum_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.stretch_start_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimplePerItem.weight(value: float) -> None
```

## `unreal.RigUnit_TwoBoneIKSimpleVectors(RigUnit_HighlevelBase)`

```python
unreal.RigUnit_TwoBoneIKSimpleVectors.__init__(root: Vector = [0.000000, 0.000000, 0.000000], pole_vector: Vector = [0.000000, 0.000000, 0.000000], effector: Vector = [0.000000, 0.000000, 0.000000], enable_stretch: bool = False, stretch_start_ratio: float = 0.000000, stretch_maximum_ratio: float = 0.000000, bone_a_length: float = 0.000000, bone_b_length: float = 0.000000, elbow: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.bone_a_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.bone_b_length(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.effector(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.elbow() -> Vector
unreal.RigUnit_TwoBoneIKSimpleVectors.enable_stretch(value: bool) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.pole_vector(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.root(value: Vector) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_maximum_ratio(value: float) -> None
unreal.RigUnit_TwoBoneIKSimpleVectors.stretch_start_ratio(value: float) -> None
```

## `unreal.RigUnit_TwoBoneIKSimple_DebugSettings(StructBase)`

```python
unreal.RigUnit_TwoBoneIKSimple_DebugSettings.__init__(enabled: bool = False, scale: float = 0.000000, world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_TwoBoneIKSimple_DebugSettings.enabled(value: bool) -> None
unreal.RigUnit_TwoBoneIKSimple_DebugSettings.scale(value: float) -> None
unreal.RigUnit_TwoBoneIKSimple_DebugSettings.world_offset(value: Transform) -> None
```

## `unreal.RigVMFunction_AnimBase(RigVMStruct)`

```python
unreal.RigVMFunction_AnimBase.__init__() -> None
```

## `unreal.RigVMFunction_AnimEasing(RigVMFunction_AnimBase)`

```python
unreal.RigVMFunction_AnimEasing.__init__(value: float = 0.000000, type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, source_minimum: float = 0.000000, source_maximum: float = 0.000000, target_minimum: float = 0.000000, target_maximum: float = 0.000000, result: float = 0.000000) -> None
unreal.RigVMFunction_AnimEasing.result() -> float
unreal.RigVMFunction_AnimEasing.source_maximum(value: float) -> None
unreal.RigVMFunction_AnimEasing.source_minimum(value: float) -> None
unreal.RigVMFunction_AnimEasing.target_maximum(value: float) -> None
unreal.RigVMFunction_AnimEasing.target_minimum(value: float) -> None
unreal.RigVMFunction_AnimEasing.type(value: RigVMAnimEasingType) -> None
unreal.RigVMFunction_AnimEasing.value(value: float) -> None
```

## `unreal.RigVMFunction_AnimEasingType(RigVMFunction_AnimBase)`

```python
unreal.RigVMFunction_AnimEasingType.__init__(type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR) -> None
unreal.RigVMFunction_AnimEasingType.type(value: RigVMAnimEasingType) -> None
```

## `unreal.RigVMFunction_AnimEvalRichCurve(RigVMFunction_AnimBase)`

```python
unreal.RigVMFunction_AnimEvalRichCurve.__init__(value: float = 0.000000, curve: RuntimeFloatCurve = [], source_minimum: float = 0.000000, source_maximum: float = 0.000000, target_minimum: float = 0.000000, target_maximum: float = 0.000000, result: float = 0.000000) -> None
unreal.RigVMFunction_AnimEvalRichCurve.curve(value: RuntimeFloatCurve) -> None
unreal.RigVMFunction_AnimEvalRichCurve.result() -> float
unreal.RigVMFunction_AnimEvalRichCurve.source_maximum(value: float) -> None
unreal.RigVMFunction_AnimEvalRichCurve.source_minimum(value: float) -> None
unreal.RigVMFunction_AnimEvalRichCurve.target_maximum(value: float) -> None
unreal.RigVMFunction_AnimEvalRichCurve.target_minimum(value: float) -> None
unreal.RigVMFunction_AnimEvalRichCurve.value(value: float) -> None
```

## `unreal.RigVMFunction_AnimRichCurve(RigVMFunction_AnimBase)`

```python
unreal.RigVMFunction_AnimRichCurve.__init__(curve: RuntimeFloatCurve = []) -> None
unreal.RigVMFunction_AnimRichCurve.curve() -> RuntimeFloatCurve
```

## `unreal.RigidBodyAnimNodeReference(AnimNodeReference)`

```python
unreal.RigidBodyAnimNodeReference.__init__() -> None
```

## `unreal.SequencerAnimationOverride(Interface)`

```python
unreal.SequencerAnimationOverride.allows_cinematic_override() -> bool
unreal.SequencerAnimationOverride.get_sequencer_anim_slot_names() -> Array[Name]
```

## `unreal.SingleAnimationPlayData(StructBase)`

```python
unreal.SingleAnimationPlayData.__init__(anim_to_play: AnimationAsset = None, saved_looping: bool = False, saved_playing: bool = False, saved_position: float = 0.000000, saved_play_rate: float = 0.000000) -> None
unreal.SingleAnimationPlayData.anim_to_play(value: AnimationAsset) -> None
unreal.SingleAnimationPlayData.saved_looping(value: bool) -> None
unreal.SingleAnimationPlayData.saved_play_rate(value: float) -> None
unreal.SingleAnimationPlayData.saved_playing(value: bool) -> None
unreal.SingleAnimationPlayData.saved_position(value: float) -> None
```

## `unreal.Skeleton(Object)`

```python
unreal.Skeleton.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.Skeleton.add_compatible_skeleton(source_skeleton: Skeleton) -> None
unreal.Skeleton.add_compatible_skeleton_soft(source_skeleton: Skeleton) -> None
unreal.Skeleton.compatible_skeletons() -> Array[Skeleton]
unreal.Skeleton.copy_bones_from_skeleton(target_mesh: DynamicMesh, options: GeometryScriptCopyBonesFromMeshOptions = [False, BonesToCopyFromSource.ALL_BONES], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.Skeleton.find_curve_identifier(name: Name, curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
unreal.Skeleton.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.Skeleton.get_blend_profile(profile_name: Name) -> BlendProfile
unreal.Skeleton.get_curve_identifier(name: Name, curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
unreal.Skeleton.get_curve_identifiers(curve_type: RawCurveTrackTypes) -> Array[AnimationCurveIdentifier]
unreal.Skeleton.get_reference_pose() -> AnimPose
unreal.Skeleton.has_asset_user_data_of_class(user_data_class: Class) -> bool
```

## `unreal.SkeletonModifier(Object)`

```python
unreal.SkeletonModifier.add_bone(bone_name: Name, parent_name: Name, transform: Transform) -> bool
unreal.SkeletonModifier.add_bones(bones_name: Array[Name], parents_name: Array[Name], transforms: Array[Transform]) -> bool
unreal.SkeletonModifier.commit_skeleton_to_skeletal_mesh() -> bool
unreal.SkeletonModifier.get_all_bone_names() -> Array[Name]
unreal.SkeletonModifier.get_bone_transform(bone_name: Name, global_: bool = False) -> Transform
unreal.SkeletonModifier.get_children_names(bone_name: Name, recursive: bool = False) -> Array[Name]
unreal.SkeletonModifier.get_parent_name(bone_name: Name) -> Name
unreal.SkeletonModifier.mirror_bone(bone_name: Name, options: MirrorOptions = [AxisType.X, True, "_l", "_r", True]) -> bool
unreal.SkeletonModifier.mirror_bones(bones_name: Array[Name], options: MirrorOptions = [AxisType.X, True, "_l", "_r", True]) -> bool
unreal.SkeletonModifier.orient_bone(bone_name: Name, options: OrientOptions = [OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True, [0.000000, 1.000000, 0.000000], True]) -> bool
unreal.SkeletonModifier.orient_bones(bone_names: Array[Name], options: OrientOptions = [OrientAxis.POSITIVE_X, OrientAxis.POSITIVE_Y, True, [0.000000, 1.000000, 0.000000], True]) -> bool
unreal.SkeletonModifier.parent_bone(bone_name: Name, parent_name: Name) -> bool
unreal.SkeletonModifier.parent_bones(bone_names: Array[Name], parent_names: Array[Name]) -> bool
unreal.SkeletonModifier.remove_bone(bone_name: Name, remove_children: bool) -> bool
unreal.SkeletonModifier.remove_bones(bone_names: Array[Name], remove_children: bool) -> bool
unreal.SkeletonModifier.rename_bone(old_bone_name: Name, new_bone_name: Name) -> bool
unreal.SkeletonModifier.rename_bones(old_bone_names: Array[Name], new_bone_names: Array[Name]) -> bool
unreal.SkeletonModifier.set_bone_transform(bone_name: Name, new_transform: Transform, move_children: bool) -> bool
unreal.SkeletonModifier.set_bones_transforms(bone_names: Array[Name], new_transforms: Array[Transform], move_children: bool) -> bool
unreal.SkeletonModifier.set_skeletal_mesh(skeletal_mesh: SkeletalMesh) -> bool
```

## `unreal.SphericalPoseReaderDebugSettings(StructBase)`

```python
unreal.SphericalPoseReaderDebugSettings.__init__(draw_debug: bool = False, draw2d: bool = False, draw_local_axes: bool = False, debug_scale: float = 0.000000, debug_segments: int = 0, debug_thickness: float = 0.000000) -> None
unreal.SphericalPoseReaderDebugSettings.debug_scale(value: float) -> None
unreal.SphericalPoseReaderDebugSettings.debug_segments(value: int) -> None
unreal.SphericalPoseReaderDebugSettings.debug_thickness(value: float) -> None
unreal.SphericalPoseReaderDebugSettings.draw2d(value: bool) -> None
unreal.SphericalPoseReaderDebugSettings.draw_debug(value: bool) -> None
unreal.SphericalPoseReaderDebugSettings.draw_local_axes(value: bool) -> None
```

## `unreal.StringAnimationAttribute(StructBase)`

```python
unreal.StringAnimationAttribute.__init__(value: str = "") -> None
unreal.StringAnimationAttribute.value(value: str) -> None
```

## `unreal.TimecodeBoneMethod(StructBase)`

```python
unreal.TimecodeBoneMethod.__init__(bone_mode: TimecodeBoneMode = TimecodeBoneMode.ALL, bone_name: Name = "None") -> None
unreal.TimecodeBoneMethod.bone_mode(value: TimecodeBoneMode) -> None
unreal.TimecodeBoneMethod.bone_name(value: Name) -> None
```

## `unreal.TravelAnimationSettings(StructBase)`

```python
unreal.TravelAnimationSettings.__init__(e_animation_blend_features: int = 0, travel_anim_type: TravelAnimType = TravelAnimType.TAT_LINEAR, curve_scale: float = 0.000000, path: Map[float, Vector] = {}) -> None
unreal.TravelAnimationSettings.curve_scale(value: float) -> None
unreal.TravelAnimationSettings.e_animation_blend_features(value: int) -> None
unreal.TravelAnimationSettings.path(value: Map[float, Vector]) -> None
unreal.TravelAnimationSettings.travel_anim_type(value: TravelAnimType) -> None
```

## `unreal.UAnimNotifyLibrary(BlueprintFunctionLibrary)`

```python
unreal.UAnimNotifyLibrary.get_current_animation_notify_state_time(event_reference: AnimNotifyEventReference) -> float
unreal.UAnimNotifyLibrary.get_current_animation_notify_state_time_ratio(event_reference: AnimNotifyEventReference) -> float
unreal.UAnimNotifyLibrary.get_current_animation_time(event_reference: AnimNotifyEventReference) -> float
unreal.UAnimNotifyLibrary.get_current_animation_time_ratio(event_reference: AnimNotifyEventReference) -> float
unreal.UAnimNotifyLibrary.is_blending_out(event_reference: AnimNotifyEventReference) -> bool
unreal.UAnimNotifyLibrary.notify_state_reached_end(event_reference: AnimNotifyEventReference) -> bool
```

## `unreal.UAnimNotifyMirrorInspectionLibrary(BlueprintFunctionLibrary)`

```python
unreal.UAnimNotifyMirrorInspectionLibrary.get_mirror_data_table(event_reference: AnimNotifyEventReference) -> MirrorDataTable
unreal.UAnimNotifyMirrorInspectionLibrary.is_triggered_by_mirrored_animation(event_reference: AnimNotifyEventReference) -> bool
```

## `unreal.UAnimNotifyStateMachineInspectionLibrary(BlueprintFunctionLibrary)`

```python
unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state(event_reference: AnimNotifyEventReference, anim_instance: AnimInstance, state_name: Name) -> bool
unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state_in_state_machine(event_reference: AnimNotifyEventReference, anim_instance: AnimInstance, state_machine_name: Name, state_name: Name) -> bool
unreal.UAnimNotifyStateMachineInspectionLibrary.is_triggered_by_state_machine(event_reference: AnimNotifyEventReference, anim_instance: AnimInstance, state_machine_name: Name) -> bool
```

## `unreal.VectorAnimationAttribute(StructBase)`

```python
unreal.VectorAnimationAttribute.__init__(value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.VectorAnimationAttribute.value(value: Vector) -> None
```

## `unreal.WDPCameraAnimationData(StructBase)`

```python
unreal.WDPCameraAnimationData.__init__() -> None
```

## `unreal.WDPGetCameraAnimationResult(ResultBase)`

```python
unreal.WDPGetCameraAnimationResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, show_touch_effect: bool = False, show_rotate_icon: bool = False) -> None
unreal.WDPGetCameraAnimationResult.show_rotate_icon(value: bool) -> None
unreal.WDPGetCameraAnimationResult.show_touch_effect(value: bool) -> None
```

## `unreal.WDPGetCameraPoseResult(ResultBase)`

```python
unreal.WDPGetCameraPoseResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, location: Vector = [0.000000, 0.000000, 0.000000], rotation: CameraPresetRotator = [0.000000, 0.000000]) -> None
unreal.WDPGetCameraPoseResult.location(value: Vector) -> None
unreal.WDPGetCameraPoseResult.rotation(value: CameraPresetRotator) -> None
```

## `unreal.WDPResetCameraPoseParams(ParamsBase)`

```python
unreal.WDPResetCameraPoseParams.__init__(state: WdpResetCameraPoseState = WdpResetCameraPoseState.DEFAULT, fly_time: float = 0.000000) -> None
unreal.WDPResetCameraPoseParams.fly_time(value: float) -> None
unreal.WDPResetCameraPoseParams.state(value: WdpResetCameraPoseState) -> None
```

## `unreal.WDPSetCameraAnimationParams(ParamsBase)`

```python
unreal.WDPSetCameraAnimationParams.__init__(show_touch_effect: bool = False, show_rotate_icon: bool = False) -> None
unreal.WDPSetCameraAnimationParams.show_rotate_icon(value: bool) -> None
unreal.WDPSetCameraAnimationParams.show_touch_effect(value: bool) -> None
```

## `unreal.WDPSetCameraPoseParams(ParamsBase)`

```python
unreal.WDPSetCameraPoseParams.__init__(location: Vector = [0.000000, 0.000000, 0.000000], rotation: CameraPresetRotator = [0.000000, 0.000000], fly_time: float = 0.000000) -> None
unreal.WDPSetCameraPoseParams.fly_time(value: float) -> None
unreal.WDPSetCameraPoseParams.location(value: Vector) -> None
unreal.WDPSetCameraPoseParams.rotation(value: CameraPresetRotator) -> None
```

## `unreal.WdpBasePawn_OnTravelAnimationFinished(MulticastDelegateBase)`

```python
unreal.WdpBasePawn_OnTravelAnimationFinished.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WidgetAnimation(MovieSceneSequence)`

```python
unreal.WidgetAnimation.get_end_time() -> float
unreal.WidgetAnimation.get_start_time() -> float
```

## `unreal.WidgetAnimationDynamicEvent(DelegateBase)`

```python
unreal.WidgetAnimationDynamicEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WidgetAnimationDynamicEvents(MulticastDelegateBase)`

```python
unreal.WidgetAnimationDynamicEvents.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WidgetAnimationPlayCallbackProxy(Object)`

```python
unreal.WidgetAnimationPlayCallbackProxy.finished(value: WidgetAnimationResult) -> None
```

## `unreal.WidgetAnimationResult(MulticastDelegateBase)`

```python
unreal.WidgetAnimationResult.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ZeroOutRootBoneModifier(AnimationModifier)`

```python
unreal.ZeroOutRootBoneModifier.clip_end_frames_with_no_motion() -> bool
unreal.ZeroOutRootBoneModifier.clip_start_frames_with_no_motion() -> bool
```

## `unreal.glTFRuntimeAnimationCurve(CurveBase)`

```python
unreal.glTFRuntimeAnimationCurve.get_transform_value(time: float) -> Transform
unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_duration() -> float
unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_index() -> int
unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_name() -> str
```

## `unreal.glTFRuntimeAnimationCurveRemapper(DelegateBase)`

```python
unreal.glTFRuntimeAnimationCurveRemapper.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeAnimationFrameRotationRemapper(DelegateBase)`

```python
unreal.glTFRuntimeAnimationFrameRotationRemapper.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeAnimationFrameTranslationRemapper(DelegateBase)`

```python
unreal.glTFRuntimeAnimationFrameTranslationRemapper.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeBone(StructBase)`

```python
unreal.glTFRuntimeBone.__init__(bone_name: str = "", parent_index: int = 0, transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.glTFRuntimeBone.bone_name(value: str) -> None
unreal.glTFRuntimeBone.parent_index(value: int) -> None
unreal.glTFRuntimeBone.transform(value: Transform) -> None
```

## `unreal.glTFRuntimeBoneBoundsFilter(DelegateBase)`

```python
unreal.glTFRuntimeBoneBoundsFilter.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeBoneBoundsFilterHook(StructBase)`

```python
unreal.glTFRuntimeBoneBoundsFilterHook.__init__(filter: glTFRuntimeBoneBoundsFilter = glTFRuntimeBoneBoundsFilter(), context: Object = None) -> None
unreal.glTFRuntimeBoneBoundsFilterHook.context(value: Object) -> None
unreal.glTFRuntimeBoneBoundsFilterHook.filter(value: glTFRuntimeBoneBoundsFilter) -> None
```

## `unreal.glTFRuntimeBoneRemapper(DelegateBase)`

```python
unreal.glTFRuntimeBoneRemapper.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeSkeletalAnimationConfig(StructBase)`

```python
unreal.glTFRuntimeSkeletalAnimationConfig.__init__(cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE, root_node_index: int = 0, root_motion: bool = False, remove_root_motion: bool = False, root_motion_root_lock: RootMotionRootLock = RootMotionRootLock.REF_POSE, remove_translations: bool = False, remove_rotations: bool = False, remove_scales: bool = False, remove_morph_targets: bool = False, override_track_name_from_extension: Array[glTFRuntimePathItem] = [], remove_tracks: Array[str] = [], curve_remapper: glTFRuntimeSkeletalAnimationCurveRemapperHook = [glTFRuntimeAnimationCurveRemapper(), None], retarget_to: Skeleton = None, retarget_to_skeletal_mesh: SkeletalMesh = None, transform_pose: Map[str, Transform] = {}, frame_translation_remapper: glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook = [glTFRuntimeAnimationFrameTranslationRemapper(), None], frame_rotation_remapper: glTFRuntimeSkeletalAnimationFrameRotationRemapperHook = [glTFRuntimeAnimationFrameRotationRemapper(), None], frames_per_second: float = 0.000000, fill_all_curves: bool = False, curves_name_map: Map[str, str] = {}, retarget_skin_index: int = 0, pose_for_retargeting: PoseAsset = None) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.cache_mode(value: EglTFRuntimeCacheMode) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.curve_remapper(value: glTFRuntimeSkeletalAnimationCurveRemapperHook) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.curves_name_map(value: Map[str, str]) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.fill_all_curves(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.frame_rotation_remapper(value: glTFRuntimeSkeletalAnimationFrameRotationRemapperHook) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.frame_translation_remapper(value: glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.frames_per_second(value: float) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.override_track_name_from_extension(value: Array[glTFRuntimePathItem]) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.pose_for_retargeting(value: PoseAsset) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_morph_targets(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_root_motion(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_rotations(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_scales(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_tracks(value: Array[str]) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.remove_translations(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.retarget_skin_index(value: int) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to(value: Skeleton) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to_skeletal_mesh(value: SkeletalMesh) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.root_motion(value: bool) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.root_motion_root_lock(value: RootMotionRootLock) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.root_node_index(value: int) -> None
unreal.glTFRuntimeSkeletalAnimationConfig.transform_pose(value: Map[str, Transform]) -> None
```

## `unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook(StructBase)`

```python
unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.__init__(remapper: glTFRuntimeAnimationCurveRemapper = glTFRuntimeAnimationCurveRemapper(), context: Object = None) -> None
unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.context(value: Object) -> None
unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.remapper(value: glTFRuntimeAnimationCurveRemapper) -> None
```

## `unreal.glTFRuntimeSkeletalAnimationFrameRotationRemapperHook(StructBase)`

```python
unreal.glTFRuntimeSkeletalAnimationFrameRotationRemapperHook.__init__(remapper: glTFRuntimeAnimationFrameRotationRemapper = glTFRuntimeAnimationFrameRotationRemapper(), context: Object = None) -> None
unreal.glTFRuntimeSkeletalAnimationFrameRotationRemapperHook.context(value: Object) -> None
unreal.glTFRuntimeSkeletalAnimationFrameRotationRemapperHook.remapper(value: glTFRuntimeAnimationFrameRotationRemapper) -> None
```

## `unreal.glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook(StructBase)`

```python
unreal.glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook.__init__(remapper: glTFRuntimeAnimationFrameTranslationRemapper = glTFRuntimeAnimationFrameTranslationRemapper(), context: Object = None) -> None
unreal.glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook.context(value: Object) -> None
unreal.glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook.remapper(value: glTFRuntimeAnimationFrameTranslationRemapper) -> None
```

## `unreal.glTFRuntimeSkeletonBoneRemapperHook(StructBase)`

```python
unreal.glTFRuntimeSkeletonBoneRemapperHook.__init__(remapper: glTFRuntimeBoneRemapper = glTFRuntimeBoneRemapper(), context: Object = None) -> None
unreal.glTFRuntimeSkeletonBoneRemapperHook.context(value: Object) -> None
unreal.glTFRuntimeSkeletonBoneRemapperHook.remapper(value: glTFRuntimeBoneRemapper) -> None
```

## `unreal.glTFRuntimeSkeletonConfig(StructBase)`

```python
unreal.glTFRuntimeSkeletonConfig.__init__(cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE, add_root_bone: bool = False, root_bone_name: str = "", bones_name_map: Map[str, str] = {}, assign_unmapped_bones_to_parent: bool = False, bones_transform_map: Map[str, Transform] = {}, normalize_skeleton_scale: bool = False, root_node_index: int = 0, sockets: Map[str, glTFRuntimeSocket] = {}, clear_rotations: bool = False, copy_rotations_from: Skeleton = None, skip_already_existent_bone_names: bool = False, force_root_node: str = "", bones_delta_transform_map: Map[str, Transform] = {}, bone_remapper: glTFRuntimeSkeletonBoneRemapperHook = [glTFRuntimeBoneRemapper(), None], append_node_index_on_name_collision: bool = False, fallback_to_nodes_tree: bool = False, apply_parent_nodes_transforms_to_root: bool = False, max_nodes_tree_depth: int = 0, apply_unmapped_bones_transforms: bool = False, node_bones_delta_transform_map: Map[str, Transform] = {}, add_root_node_if_missing: bool = False) -> None
unreal.glTFRuntimeSkeletonConfig.add_root_bone(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.add_root_node_if_missing(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.append_node_index_on_name_collision(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.apply_parent_nodes_transforms_to_root(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.apply_unmapped_bones_transforms(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.assign_unmapped_bones_to_parent(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.bone_remapper(value: glTFRuntimeSkeletonBoneRemapperHook) -> None
unreal.glTFRuntimeSkeletonConfig.bones_delta_transform_map(value: Map[str, Transform]) -> None
unreal.glTFRuntimeSkeletonConfig.bones_name_map(value: Map[str, str]) -> None
unreal.glTFRuntimeSkeletonConfig.bones_transform_map(value: Map[str, Transform]) -> None
unreal.glTFRuntimeSkeletonConfig.cache_mode(value: EglTFRuntimeCacheMode) -> None
unreal.glTFRuntimeSkeletonConfig.clear_rotations(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.copy_rotations_from(value: Skeleton) -> None
unreal.glTFRuntimeSkeletonConfig.fallback_to_nodes_tree(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.force_root_node(value: str) -> None
unreal.glTFRuntimeSkeletonConfig.max_nodes_tree_depth(value: int) -> None
unreal.glTFRuntimeSkeletonConfig.node_bones_delta_transform_map(value: Map[str, Transform]) -> None
unreal.glTFRuntimeSkeletonConfig.normalize_skeleton_scale(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.root_bone_name(value: str) -> None
unreal.glTFRuntimeSkeletonConfig.root_node_index(value: int) -> None
unreal.glTFRuntimeSkeletonConfig.skip_already_existent_bone_names(value: bool) -> None
unreal.glTFRuntimeSkeletonConfig.sockets(value: Map[str, glTFRuntimeSocket]) -> None
```

## `unreal.set_bone_reference_pose(ToolMenuEntryScript)`

```python
unreal.set_bone_reference_pose.__init__(*args: Any, **kwargs: Any) -> None
```

