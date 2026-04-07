# Unreal Python API — Sequencer Movie

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.FixedSampleSequenceRulerStyle(SlateWidgetStyle)`

```python
unreal.FixedSampleSequenceRulerStyle.__init__(handle_width: float = 0.000000, handle_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], handle_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], ticks_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], ticks_text_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], ticks_text_font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000], ticks_text_offset: float = 0.000000, background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], desired_width: float = 0.000000, desired_height: float = 0.000000) -> None
unreal.FixedSampleSequenceRulerStyle.background_brush(value: SlateBrush) -> None
unreal.FixedSampleSequenceRulerStyle.background_color(value: SlateColor) -> None
unreal.FixedSampleSequenceRulerStyle.desired_height(value: float) -> None
unreal.FixedSampleSequenceRulerStyle.desired_width(value: float) -> None
unreal.FixedSampleSequenceRulerStyle.handle_brush(value: SlateBrush) -> None
unreal.FixedSampleSequenceRulerStyle.handle_color(value: SlateColor) -> None
unreal.FixedSampleSequenceRulerStyle.handle_width(value: float) -> None
unreal.FixedSampleSequenceRulerStyle.ticks_color(value: SlateColor) -> None
unreal.FixedSampleSequenceRulerStyle.ticks_text_color(value: SlateColor) -> None
unreal.FixedSampleSequenceRulerStyle.ticks_text_font(value: SlateFontInfo) -> None
unreal.FixedSampleSequenceRulerStyle.ticks_text_offset(value: float) -> None
```

## `unreal.InterchangeAssetImportData(AssetImportData)`

```python
unreal.InterchangeAssetImportData.get_node_container() -> InterchangeBaseNodeContainer
unreal.InterchangeAssetImportData.get_number_of_pipelines() -> int
unreal.InterchangeAssetImportData.get_pipelines() -> Array[Object]
unreal.InterchangeAssetImportData.get_stored_factory_node(node_unique_id: str) -> InterchangeFactoryBaseNode
unreal.InterchangeAssetImportData.get_stored_node(node_unique_id: str) -> InterchangeBaseNode
unreal.InterchangeAssetImportData.get_translator_settings() -> InterchangeTranslatorSettings
unreal.InterchangeAssetImportData.node_container(value: InterchangeBaseNodeContainer) -> None
unreal.InterchangeAssetImportData.pipelines(value: Array[Object]) -> None
unreal.InterchangeAssetImportData.script_extract_display_labels() -> Array[str]
unreal.InterchangeAssetImportData.script_extract_filenames() -> Array[str]
unreal.InterchangeAssetImportData.script_get_first_filename() -> str
unreal.InterchangeAssetImportData.set_node_container(node_container: InterchangeBaseNodeContainer) -> None
unreal.InterchangeAssetImportData.set_pipelines(pipelines: Array[Object]) -> None
unreal.InterchangeAssetImportData.set_translator_settings(translator_settings: InterchangeTranslatorSettings) -> None
```

## `unreal.InterchangeEditorSettings(DeveloperSettings)`

```python
unreal.InterchangeEditorSettings.get_used_group_name() -> Name
unreal.InterchangeEditorSettings.set_used_group_name(used_group_name: Name) -> None
```

## `unreal.InterchangeFilePickerBase(Object)`

```python
unreal.InterchangeFilePickerBase.scripted_file_picker_for_translator_asset_type(translator_asset_type: InterchangeTranslatorAssetType) -> Optional[Tuple[InterchangeFilePickerParameters, Array[str]]]
unreal.InterchangeFilePickerBase.scripted_file_picker_for_translator_type(translator_type: InterchangeTranslatorType) -> Optional[Tuple[InterchangeFilePickerParameters, Array[str]]]
```

## `unreal.InterchangeFilePickerParameters(StructBase)`

```python
unreal.InterchangeFilePickerParameters.__init__() -> None
```

## `unreal.InterchangeGLTFPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGLTFPipeline.pipeline_display_name(value: str) -> None
```

## `unreal.InterchangeGenericAssetsPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericAssetsPipeline.animation_pipeline() -> InterchangeGenericAnimationPipeline
unreal.InterchangeGenericAssetsPipeline.asset_name(value: str) -> None
unreal.InterchangeGenericAssetsPipeline.common_meshes_properties() -> InterchangeGenericCommonMeshesProperties
unreal.InterchangeGenericAssetsPipeline.common_skeletal_meshes_and_animations_properties() -> InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties
unreal.InterchangeGenericAssetsPipeline.import_offset_rotation(value: Rotator) -> None
unreal.InterchangeGenericAssetsPipeline.import_offset_translation(value: Vector) -> None
unreal.InterchangeGenericAssetsPipeline.import_offset_uniform_scale(value: float) -> None
unreal.InterchangeGenericAssetsPipeline.material_pipeline() -> InterchangeGenericMaterialPipeline
unreal.InterchangeGenericAssetsPipeline.mesh_pipeline() -> InterchangeGenericMeshPipeline
unreal.InterchangeGenericAssetsPipeline.pipeline_display_name(value: str) -> None
unreal.InterchangeGenericAssetsPipeline.reimport_strategy(value: ReimportStrategyFlags) -> None
unreal.InterchangeGenericAssetsPipeline.use_source_name_for_asset(value: bool) -> None
```

## `unreal.InterchangeGenericCommonMeshesProperties(InterchangePipelineBase)`

```python
unreal.InterchangeGenericCommonMeshesProperties.auto_detect_mesh_type(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.bake_meshes(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.bake_pivot_meshes(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.compute_weighted_normals(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.force_all_mesh_as_type(value: InterchangeForceMeshType) -> None
unreal.InterchangeGenericCommonMeshesProperties.import_lods(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.keep_sections_separate(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.recompute_normals(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.recompute_tangents(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.remove_degenerates(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.use_full_precision_u_vs(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.use_high_precision_tangent_basis(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.use_mikk_t_space(value: bool) -> None
unreal.InterchangeGenericCommonMeshesProperties.vertex_color_import_option(value: InterchangeVertexColorImportOption) -> None
unreal.InterchangeGenericCommonMeshesProperties.vertex_override_color(value: Color) -> None
```

## `unreal.InterchangeGenericMeshPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericMeshPipeline.auto_compute_lod_screen_sizes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.bone_influence_limit(value: int) -> None
unreal.InterchangeGenericMeshPipeline.build_nanite(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.build_reversed_index_buffer(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.build_scale3d(value: Vector) -> None
unreal.InterchangeGenericMeshPipeline.collision(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.combine_skeletal_meshes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.combine_static_meshes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.create_physics_asset(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.distance_field_replacement_mesh(value: StaticMesh) -> None
unreal.InterchangeGenericMeshPipeline.distance_field_resolution_scale(value: float) -> None
unreal.InterchangeGenericMeshPipeline.dst_lightmap_index(value: int) -> None
unreal.InterchangeGenericMeshPipeline.fallback_collision_type(value: InterchangeMeshCollision) -> None
unreal.InterchangeGenericMeshPipeline.generate_distance_field_as_if_two_sided(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.generate_lightmap_u_vs(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_collision(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_collision_according_to_mesh_name(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_morph_targets(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_skeletal_meshes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_static_meshes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.import_vertex_attributes(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.lod_group(value: Name) -> None
unreal.InterchangeGenericMeshPipeline.lod_screen_sizes(value: Array[float]) -> None
unreal.InterchangeGenericMeshPipeline.max_lumen_mesh_cards(value: int) -> None
unreal.InterchangeGenericMeshPipeline.merge_morph_targets_with_same_name(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.min_lightmap_resolution(value: int) -> None
unreal.InterchangeGenericMeshPipeline.morph_threshold_position(value: float) -> None
unreal.InterchangeGenericMeshPipeline.one_convex_hull_per_ucx(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.physics_asset(value: PhysicsAsset) -> None
unreal.InterchangeGenericMeshPipeline.skeletal_mesh_import_content_type(value: InterchangeSkeletalMeshContentType) -> None
unreal.InterchangeGenericMeshPipeline.src_lightmap_index(value: int) -> None
unreal.InterchangeGenericMeshPipeline.support_face_remap(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.threshold_position(value: float) -> None
unreal.InterchangeGenericMeshPipeline.threshold_tangent_normal(value: float) -> None
unreal.InterchangeGenericMeshPipeline.threshold_uv(value: float) -> None
unreal.InterchangeGenericMeshPipeline.update_skeleton_reference_pose(value: bool) -> None
unreal.InterchangeGenericMeshPipeline.use_high_precision_skin_weights(value: bool) -> None
```

## `unreal.InterchangeImportTestPlan(Object)`

```python
unreal.InterchangeImportTestPlan.run_this_test() -> None
```

## `unreal.InterchangeManager(Object)`

```python
unreal.InterchangeManager.create_source_data(file_name: str) -> InterchangeSourceData
unreal.InterchangeManager.export_asset(asset: Object, is_automated: bool = False) -> bool
unreal.InterchangeManager.export_scene(world: Object, is_automated: bool = False) -> bool
unreal.InterchangeManager.get_interchange_manager_scripted() -> InterchangeManager
unreal.InterchangeManager.get_registered_factory_class(class_to_make: Class) -> Class
unreal.InterchangeManager.import_asset(content_path: str, source_data: InterchangeSourceData, import_asset_parameters: ImportAssetParameters) -> Optional[Array[Object]]
unreal.InterchangeManager.import_scene(content_path: str, source_data: InterchangeSourceData, import_asset_parameters: ImportAssetParameters) -> bool
unreal.InterchangeManager.scripted_import_asset_async(content_path: str, source_data: InterchangeSourceData, import_asset_parameters: ImportAssetParameters) -> bool
unreal.InterchangeManager.scripted_import_scene_async(content_path: str, source_data: InterchangeSourceData, import_asset_parameters: ImportAssetParameters) -> bool
```

## `unreal.InterchangeMeshInstance(StructBase)`

```python
unreal.InterchangeMeshInstance.__init__() -> None
```

## `unreal.InterchangeMeshPayLoadKey(StructBase)`

```python
unreal.InterchangeMeshPayLoadKey.__init__(unique_id: str = "", type: InterchangeMeshPayLoadType = InterchangeMeshPayLoadType.NONE) -> None
unreal.InterchangeMeshPayLoadKey.type(value: InterchangeMeshPayLoadType) -> None
unreal.InterchangeMeshPayLoadKey.unique_id(value: str) -> None
```

## `unreal.InterchangeMeshUtilities(Object)`

```python
unreal.InterchangeMeshUtilities.scripted_import_morph_target(skeletal_mesh: SkeletalMesh, lod_index: int, source_data: InterchangeSourceData, morph_target_name: str) -> bool
```

## `unreal.InterchangePipelineBase(Object)`

```python
unreal.InterchangePipelineBase.does_property_states_exist(property_path: Name) -> bool
unreal.InterchangePipelineBase.find_or_add_property_states(property_path: Name) -> InterchangePipelinePropertyStates
unreal.InterchangePipelineBase.scripted_execute_export_pipeline(base_node_container: InterchangeBaseNodeContainer) -> None
unreal.InterchangePipelineBase.scripted_execute_pipeline(base_node_container: InterchangeBaseNodeContainer, source_datas: Array[InterchangeSourceData], content_base_path: str) -> None
unreal.InterchangePipelineBase.scripted_execute_post_broadcast_pipeline(base_node_container: InterchangeBaseNodeContainer, factory_node_key: str, created_asset: Object, is_a_reimport: bool) -> None
unreal.InterchangePipelineBase.scripted_execute_post_factory_pipeline(base_node_container: InterchangeBaseNodeContainer, factory_node_key: str, created_asset: Object, is_a_reimport: bool) -> None
unreal.InterchangePipelineBase.scripted_execute_post_import_pipeline(base_node_container: InterchangeBaseNodeContainer, factory_node_key: str, created_asset: Object, is_a_reimport: bool) -> None
unreal.InterchangePipelineBase.scripted_get_pipeline_display_name() -> str
unreal.InterchangePipelineBase.scripted_set_reimport_source_index(reimport_object_class: Class, source_file_index: int) -> None
```

## `unreal.InterchangePipelineConfigurationBase(Object)`

```python
unreal.InterchangePipelineConfigurationBase.scripted_show_pipeline_configuration_dialog(source_data: InterchangeSourceData, translator: InterchangeTranslatorBase, base_node_container: InterchangeBaseNodeContainer) -> Tuple[InterchangePipelineConfigurationDialogResult, Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
unreal.InterchangePipelineConfigurationBase.scripted_show_reimport_pipeline_configuration_dialog(source_data: InterchangeSourceData, translator: InterchangeTranslatorBase, base_node_container: InterchangeBaseNodeContainer, reimport_asset: Object) -> Tuple[InterchangePipelineConfigurationDialogResult, Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
unreal.InterchangePipelineConfigurationBase.scripted_show_scene_pipeline_configuration_dialog(source_data: InterchangeSourceData, translator: InterchangeTranslatorBase, base_node_container: InterchangeBaseNodeContainer) -> Tuple[InterchangePipelineConfigurationDialogResult, Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
```

## `unreal.InterchangePipelineMeshesUtilities(Object)`

```python
unreal.InterchangePipelineMeshesUtilities.create_interchange_pipeline_meshes_utilities(base_node_container: InterchangeBaseNodeContainer) -> InterchangePipelineMeshesUtilities
unreal.InterchangePipelineMeshesUtilities.get_all_mesh_geometry() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_mesh_geometry_not_instanced() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_mesh_instance_uids() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_mesh_instance_uids_using_mesh_geometry_uid(mesh_geometry_uid: str) -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_skinned_mesh_geometry() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_skinned_mesh_instance() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_static_mesh_geometry() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_all_static_mesh_instance() -> Array[str]
unreal.InterchangePipelineMeshesUtilities.get_mesh_geometry_by_uid(mesh_geometry_uid: str) -> InterchangeMeshGeometry
unreal.InterchangePipelineMeshesUtilities.get_mesh_geometry_skeleton_root_uid(mesh_geometry_uid: str) -> str
unreal.InterchangePipelineMeshesUtilities.get_mesh_instance_by_uid(mesh_instance_uid: str) -> InterchangeMeshInstance
unreal.InterchangePipelineMeshesUtilities.get_mesh_instance_skeleton_root_uid(mesh_instance_uid: str) -> str
unreal.InterchangePipelineMeshesUtilities.is_valid_mesh_geometry_uid(mesh_geometry_uid: str) -> bool
unreal.InterchangePipelineMeshesUtilities.is_valid_mesh_instance_uid(mesh_instance_uid: str) -> bool
unreal.InterchangePipelineMeshesUtilities.set_context(context: InterchangePipelineMeshesUtilitiesContext) -> None
```

## `unreal.InterchangePipelineMeshesUtilitiesContext(StructBase)`

```python
unreal.InterchangePipelineMeshesUtilitiesContext.__init__(convert_static_mesh_to_skeletal_mesh: bool = False, convert_skeletal_mesh_to_static_mesh: bool = False, convert_statics_with_morph_targets_to_skeletals: bool = False, import_meshes_in_bone_hierarchy: bool = False, query_geometry_only_if_no_instance: bool = False, ignore_static_meshes: bool = False) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.convert_skeletal_mesh_to_static_mesh(value: bool) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.convert_static_mesh_to_skeletal_mesh(value: bool) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.convert_statics_with_morph_targets_to_skeletals(value: bool) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.ignore_static_meshes(value: bool) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.import_meshes_in_bone_hierarchy(value: bool) -> None
unreal.InterchangePipelineMeshesUtilitiesContext.query_geometry_only_if_no_instance(value: bool) -> None
```

## `unreal.InterchangePipelinePropertyStatePerContext(StructBase)`

```python
unreal.InterchangePipelinePropertyStatePerContext.__init__(visible: bool = False) -> None
unreal.InterchangePipelinePropertyStatePerContext.visible(value: bool) -> None
```

## `unreal.InterchangePipelinePropertyStates(StructBase)`

```python
unreal.InterchangePipelinePropertyStates.__init__(locked: bool = False, pre_dialog_reset: bool = False, basic_layout_states: InterchangePipelinePropertyStatePerContext = [True], import_states: InterchangePipelinePropertyStatePerContext = [True], reimport_states: InterchangePipelinePropertyStatePerContext = [True]) -> None
unreal.InterchangePipelinePropertyStates.basic_layout_states(value: InterchangePipelinePropertyStatePerContext) -> None
unreal.InterchangePipelinePropertyStates.import_states(value: InterchangePipelinePropertyStatePerContext) -> None
unreal.InterchangePipelinePropertyStates.locked(value: bool) -> None
unreal.InterchangePipelinePropertyStates.pre_dialog_reset(value: bool) -> None
unreal.InterchangePipelinePropertyStates.reimport_states(value: InterchangePipelinePropertyStatePerContext) -> None
```

## `unreal.InterchangePipelineStackOverride(Object)`

```python
unreal.InterchangePipelineStackOverride.add_blueprint_pipeline(pipeline_base: InterchangeBlueprintPipelineBase) -> None
unreal.InterchangePipelineStackOverride.add_pipeline(pipeline_base: InterchangePipelineBase) -> None
unreal.InterchangePipelineStackOverride.add_python_pipeline(pipeline_base: InterchangePythonPipelineBase) -> None
unreal.InterchangePipelineStackOverride.override_pipelines(value: Array[SoftObjectPath]) -> None
```

## `unreal.InterchangeSourceData(Object)`

```python
unreal.InterchangeSourceData.get_filename() -> str
unreal.InterchangeSourceData.set_filename(filename: str) -> bool
```

## `unreal.InterchangeStackInfo(StructBase)`

```python
unreal.InterchangeStackInfo.__init__(stack_name: Name = "None", pipelines: Array[InterchangePipelineBase] = []) -> None
unreal.InterchangeStackInfo.pipelines(value: Array[InterchangePipelineBase]) -> None
unreal.InterchangeStackInfo.stack_name(value: Name) -> None
```

## `unreal.InterchangeTestFunction(StructBase)`

```python
unreal.InterchangeTestFunction.__init__() -> None
```

## `unreal.InterchangeTranslatorSettings(Object)`

```python
unreal.InterchangeTranslatorSettings.load_settings() -> None
unreal.InterchangeTranslatorSettings.save_settings() -> None
```

## `unreal.InterchangeUserData(AssetUserData)`

```python
unreal.InterchangeUserData.metadata() -> Map[str, str]
```

## `unreal.MovieScene3DAttachSection(MovieScene3DConstraintSection)`

```python
unreal.MovieScene3DAttachSection.attach_component_name(value: Name) -> None
unreal.MovieScene3DAttachSection.attach_socket_name(value: Name) -> None
unreal.MovieScene3DAttachSection.attachment_location_rule(value: AttachmentRule) -> None
unreal.MovieScene3DAttachSection.attachment_rotation_rule(value: AttachmentRule) -> None
unreal.MovieScene3DAttachSection.attachment_scale_rule(value: AttachmentRule) -> None
unreal.MovieScene3DAttachSection.detachment_location_rule(value: DetachmentRule) -> None
unreal.MovieScene3DAttachSection.detachment_rotation_rule(value: DetachmentRule) -> None
unreal.MovieScene3DAttachSection.detachment_scale_rule(value: DetachmentRule) -> None
```

## `unreal.MovieScene3DPathSection(MovieScene3DConstraintSection)`

```python
unreal.MovieScene3DPathSection.follow(value: bool) -> None
unreal.MovieScene3DPathSection.force_upright(value: bool) -> None
unreal.MovieScene3DPathSection.front_axis_enum(value: MovieScene3DPathSection_Axis) -> None
unreal.MovieScene3DPathSection.reverse(value: bool) -> None
unreal.MovieScene3DPathSection.up_axis_enum(value: MovieScene3DPathSection_Axis) -> None
```

## `unreal.MovieSceneAsyncAction_SequencePrediction(BlueprintAsyncActionBase)`

```python
unreal.MovieSceneAsyncAction_SequencePrediction.failure(value: MovieSceneActorPredictionFailure) -> None
unreal.MovieSceneAsyncAction_SequencePrediction.predict_local_transform_at_frame(player: MovieSceneSequencePlayer, target_component: SceneComponent, frame_time: FrameTime) -> MovieSceneAsyncAction_SequencePrediction
unreal.MovieSceneAsyncAction_SequencePrediction.predict_local_transform_at_time(player: MovieSceneSequencePlayer, target_component: SceneComponent, time_in_seconds: float) -> MovieSceneAsyncAction_SequencePrediction
unreal.MovieSceneAsyncAction_SequencePrediction.predict_world_transform_at_frame(player: MovieSceneSequencePlayer, target_component: SceneComponent, frame_time: FrameTime) -> MovieSceneAsyncAction_SequencePrediction
unreal.MovieSceneAsyncAction_SequencePrediction.predict_world_transform_at_time(player: MovieSceneSequencePlayer, target_component: SceneComponent, time_in_seconds: float) -> MovieSceneAsyncAction_SequencePrediction
unreal.MovieSceneAsyncAction_SequencePrediction.result(value: MovieSceneActorPredictionResult) -> None
```

## `unreal.MovieSceneBaseCacheParams(StructBase)`

```python
unreal.MovieSceneBaseCacheParams.__init__() -> None
```

## `unreal.MovieSceneBindingEventReceiverInterface(Interface)`

```python
unreal.MovieSceneBindingEventReceiverInterface.on_object_bound_by_sequencer(player: MovieSceneSequencePlayer, binding_id: MovieSceneObjectBindingID) -> None
unreal.MovieSceneBindingEventReceiverInterface.on_object_unbound_by_sequencer(player: MovieSceneSequencePlayer, binding_id: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneBindingExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneBindingExtensions.add_track(binding: MovieSceneBindingProxy, track_type: Class) -> MovieSceneTrack
unreal.MovieSceneBindingExtensions.find_tracks_by_exact_type(binding: MovieSceneBindingProxy, track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneBindingExtensions.find_tracks_by_type(binding: MovieSceneBindingProxy, track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneBindingExtensions.get_child_possessables(binding: MovieSceneBindingProxy) -> Array[MovieSceneBindingProxy]
unreal.MovieSceneBindingExtensions.get_display_name(binding: MovieSceneBindingProxy) -> Text
unreal.MovieSceneBindingExtensions.get_id(binding: MovieSceneBindingProxy) -> Guid
unreal.MovieSceneBindingExtensions.get_name(binding: MovieSceneBindingProxy) -> str
unreal.MovieSceneBindingExtensions.get_object_template(binding: MovieSceneBindingProxy) -> Object
unreal.MovieSceneBindingExtensions.get_parent(binding: MovieSceneBindingProxy) -> MovieSceneBindingProxy
unreal.MovieSceneBindingExtensions.get_possessed_object_class(binding: MovieSceneBindingProxy) -> Class
unreal.MovieSceneBindingExtensions.get_sorting_order(binding: MovieSceneBindingProxy) -> int
unreal.MovieSceneBindingExtensions.get_tracks(binding: MovieSceneBindingProxy) -> Array[MovieSceneTrack]
unreal.MovieSceneBindingExtensions.is_valid(binding: MovieSceneBindingProxy) -> bool
unreal.MovieSceneBindingExtensions.move_binding_contents(source_binding_id: MovieSceneBindingProxy, destination_binding_id: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingExtensions.remove(binding: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingExtensions.remove_track(binding: MovieSceneBindingProxy, track_to_remove: MovieSceneTrack) -> None
unreal.MovieSceneBindingExtensions.set_display_name(binding: MovieSceneBindingProxy, display_name: Text) -> None
unreal.MovieSceneBindingExtensions.set_name(binding: MovieSceneBindingProxy, name: str) -> None
unreal.MovieSceneBindingExtensions.set_parent(binding: MovieSceneBindingProxy, parent_binding: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingExtensions.set_sorting_order(binding: MovieSceneBindingProxy, sorting_order: int) -> None
unreal.MovieSceneBindingExtensions.set_spawnable_binding_id(binding: MovieSceneBindingProxy, spawnable_binding_id: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneBindingOverrideData(StructBase)`

```python
unreal.MovieSceneBindingOverrideData.__init__() -> None
```

## `unreal.MovieSceneBindingProxy(StructBase)`

```python
unreal.MovieSceneBindingProxy.__init__(binding_id: Guid = [], sequence: MovieSceneSequence = None) -> None
unreal.MovieSceneBindingProxy.add_track(track_type: Class) -> MovieSceneTrack
unreal.MovieSceneBindingProxy.binding_id() -> Guid
unreal.MovieSceneBindingProxy.find_tracks_by_exact_type(track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneBindingProxy.find_tracks_by_type(track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneBindingProxy.get_child_possessables() -> Array[MovieSceneBindingProxy]
unreal.MovieSceneBindingProxy.get_display_name() -> Text
unreal.MovieSceneBindingProxy.get_id() -> Guid
unreal.MovieSceneBindingProxy.get_name() -> str
unreal.MovieSceneBindingProxy.get_object_template() -> Object
unreal.MovieSceneBindingProxy.get_parent() -> MovieSceneBindingProxy
unreal.MovieSceneBindingProxy.get_possessed_object_class() -> Class
unreal.MovieSceneBindingProxy.get_sorting_order() -> int
unreal.MovieSceneBindingProxy.get_tracks() -> Array[MovieSceneTrack]
unreal.MovieSceneBindingProxy.is_valid() -> bool
unreal.MovieSceneBindingProxy.move_binding_contents(destination_binding_id: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingProxy.remove() -> None
unreal.MovieSceneBindingProxy.remove_track(track_to_remove: MovieSceneTrack) -> None
unreal.MovieSceneBindingProxy.sequence() -> MovieSceneSequence
unreal.MovieSceneBindingProxy.set_display_name(display_name: Text) -> None
unreal.MovieSceneBindingProxy.set_name(name: str) -> None
unreal.MovieSceneBindingProxy.set_parent(parent_binding: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingProxy.set_sorting_order(sorting_order: int) -> None
unreal.MovieSceneBindingProxy.set_spawnable_binding_id(spawnable_binding_id: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneBindingResolveContext(StructBase)`

```python
unreal.MovieSceneBindingResolveContext.__init__(world_context: Object = None, binding: MovieSceneBindingProxy = [[], None]) -> None
unreal.MovieSceneBindingResolveContext.binding(value: MovieSceneBindingProxy) -> None
unreal.MovieSceneBindingResolveContext.world_context(value: Object) -> None
```

## `unreal.MovieSceneBindingResolveResult(StructBase)`

```python
unreal.MovieSceneBindingResolveResult.__init__(object: Object = None) -> None
unreal.MovieSceneBindingResolveResult.object(value: Object) -> None
```

## `unreal.MovieSceneBoundObjectProxy(Interface)`

```python
unreal.MovieSceneBoundObjectProxy.bp_get_bound_object_for_sequencer(resolved_object: Object) -> Object
```

## `unreal.MovieSceneBuiltInEasingFunction(Object)`

```python
unreal.MovieSceneBuiltInEasingFunction.on_evaluate(interp: float) -> float
```

## `unreal.MovieSceneByteTrack(MovieScenePropertyTrack)`

```python
unreal.MovieSceneByteTrack.get_byte_track_enum() -> Enum
unreal.MovieSceneByteTrack.set_byte_track_enum(enum: Enum) -> None
```

## `unreal.MovieSceneCVarOverrides(StructBase)`

```python
unreal.MovieSceneCVarOverrides.__init__() -> None
```

## `unreal.MovieSceneCVarSection(MovieSceneSection)`

```python
unreal.MovieSceneCVarSection.get_string() -> str
unreal.MovieSceneCVarSection.set_from_string(string: str) -> None
```

## `unreal.MovieSceneCameraCutSection(MovieSceneSection)`

```python
unreal.MovieSceneCameraCutSection.get_camera_binding_id() -> MovieSceneObjectBindingID
unreal.MovieSceneCameraCutSection.set_camera_binding_id(camera_binding_id: MovieSceneObjectBindingID) -> None
```

## `unreal.MovieSceneCameraShakeSectionData(StructBase)`

```python
unreal.MovieSceneCameraShakeSectionData.__init__() -> None
```

## `unreal.MovieSceneCameraShakeSourceTrigger(StructBase)`

```python
unreal.MovieSceneCameraShakeSourceTrigger.__init__(shake_class: Class = None, play_scale: float = 0.000000, play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL, user_defined_play_space: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.MovieSceneCameraShakeSourceTrigger.play_scale(value: float) -> None
unreal.MovieSceneCameraShakeSourceTrigger.play_space(value: CameraShakePlaySpace) -> None
unreal.MovieSceneCameraShakeSourceTrigger.shake_class(value: Class) -> None
unreal.MovieSceneCameraShakeSourceTrigger.user_defined_play_space(value: Rotator) -> None
```

## `unreal.MovieSceneCapture(Object)`

```python
unreal.MovieSceneCapture.additional_command_line_arguments(value: str) -> None
unreal.MovieSceneCapture.close_editor_when_capture_starts(value: bool) -> None
unreal.MovieSceneCapture.get_audio_capture_protocol() -> MovieSceneCaptureProtocolBase
unreal.MovieSceneCapture.get_image_capture_protocol() -> MovieSceneCaptureProtocolBase
unreal.MovieSceneCapture.inherited_command_line_arguments(value: str) -> None
unreal.MovieSceneCapture.set_audio_capture_protocol_type(protocol_type: Class) -> None
unreal.MovieSceneCapture.set_image_capture_protocol_type(protocol_type: Class) -> None
unreal.MovieSceneCapture.settings(value: MovieSceneCaptureSettings) -> None
unreal.MovieSceneCapture.use_separate_process(value: bool) -> None
```

## `unreal.MovieSceneCaptureEnvironment(Object)`

```python
unreal.MovieSceneCaptureEnvironment.find_audio_capture_protocol() -> MovieSceneAudioCaptureProtocolBase
unreal.MovieSceneCaptureEnvironment.find_image_capture_protocol() -> MovieSceneImageCaptureProtocolBase
unreal.MovieSceneCaptureEnvironment.get_capture_elapsed_time() -> float
unreal.MovieSceneCaptureEnvironment.get_capture_frame_number() -> int
unreal.MovieSceneCaptureEnvironment.is_capture_in_progress() -> bool
```

## `unreal.MovieSceneCaptureProtocolBase(Object)`

```python
unreal.MovieSceneCaptureProtocolBase.get_state() -> MovieSceneCaptureProtocolState
unreal.MovieSceneCaptureProtocolBase.is_capturing() -> bool
```

## `unreal.MovieSceneCaptureSettings(StructBase)`

```python
unreal.MovieSceneCaptureSettings.__init__(output_directory: DirectoryPath = [""], game_mode_override: Class = None, output_format: str = "", overwrite_existing: bool = False, use_relative_frame_numbers: bool = False, handle_frames: int = 0, movie_extension: str = "", zero_pad_frame_numbers: int = 0, frame_rate: FrameRate = [60000, 1], use_custom_frame_rate: bool = False, custom_frame_rate: FrameRate = [60000, 1], resolution: CaptureResolution = [0, 0], enable_texture_streaming: bool = False, cinematic_engine_scalability: bool = False, cinematic_mode: bool = False, allow_movement: bool = False, allow_turning: bool = False, show_player: bool = False, show_hud: bool = False, use_path_tracer: bool = False, path_tracer_sample_per_pixel: int = 0) -> None
unreal.MovieSceneCaptureSettings.allow_movement(value: bool) -> None
unreal.MovieSceneCaptureSettings.allow_turning(value: bool) -> None
unreal.MovieSceneCaptureSettings.cinematic_engine_scalability(value: bool) -> None
unreal.MovieSceneCaptureSettings.cinematic_mode(value: bool) -> None
unreal.MovieSceneCaptureSettings.custom_frame_rate(value: FrameRate) -> None
unreal.MovieSceneCaptureSettings.enable_texture_streaming(value: bool) -> None
unreal.MovieSceneCaptureSettings.frame_rate() -> FrameRate
unreal.MovieSceneCaptureSettings.game_mode_override(value: Class) -> None
unreal.MovieSceneCaptureSettings.handle_frames(value: int) -> None
unreal.MovieSceneCaptureSettings.movie_extension(value: str) -> None
unreal.MovieSceneCaptureSettings.output_directory(value: DirectoryPath) -> None
unreal.MovieSceneCaptureSettings.output_format(value: str) -> None
unreal.MovieSceneCaptureSettings.overwrite_existing(value: bool) -> None
unreal.MovieSceneCaptureSettings.path_tracer_sample_per_pixel(value: int) -> None
unreal.MovieSceneCaptureSettings.resolution(value: CaptureResolution) -> None
unreal.MovieSceneCaptureSettings.show_hud(value: bool) -> None
unreal.MovieSceneCaptureSettings.show_player(value: bool) -> None
unreal.MovieSceneCaptureSettings.use_custom_frame_rate(value: bool) -> None
unreal.MovieSceneCaptureSettings.use_path_tracer(value: bool) -> None
unreal.MovieSceneCaptureSettings.use_relative_frame_numbers(value: bool) -> None
unreal.MovieSceneCaptureSettings.zero_pad_frame_numbers(value: int) -> None
```

## `unreal.MovieSceneCinematicShotSection(MovieSceneSubSection)`

```python
unreal.MovieSceneCinematicShotSection.get_shot_display_name() -> str
unreal.MovieSceneCinematicShotSection.set_shot_display_name(shot_display_name: str) -> None
```

## `unreal.MovieSceneCondition(MovieSceneSignedObject)`

```python
unreal.MovieSceneCondition.bp_evaluate_condition(condition_context: MovieSceneConditionContext) -> bool
unreal.MovieSceneCondition.bp_get_check_frequency() -> MovieSceneConditionCheckFrequency
unreal.MovieSceneCondition.bp_get_scope() -> MovieSceneConditionScope
unreal.MovieSceneCondition.editor_force_true(value: bool) -> None
unreal.MovieSceneCondition.invert(value: bool) -> None
```

## `unreal.MovieSceneConditionContainer(StructBase)`

```python
unreal.MovieSceneConditionContainer.__init__(condition: MovieSceneCondition = None) -> None
unreal.MovieSceneConditionContainer.condition(value: MovieSceneCondition) -> None
```

## `unreal.MovieSceneConditionContext(StructBase)`

```python
unreal.MovieSceneConditionContext.__init__(world_context: Object = None, binding: MovieSceneBindingProxy = [[], None], bound_objects: Array[Object] = []) -> None
unreal.MovieSceneConditionContext.binding(value: MovieSceneBindingProxy) -> None
unreal.MovieSceneConditionContext.bound_objects(value: Array[Object]) -> None
unreal.MovieSceneConditionContext.world_context(value: Object) -> None
```

## `unreal.MovieSceneConsoleVariableCollection(StructBase)`

```python
unreal.MovieSceneConsoleVariableCollection.__init__() -> None
```

## `unreal.MovieSceneCustomBinding(Object)`

```python
unreal.MovieSceneCustomBinding.get_base_custom_priority() -> int
unreal.MovieSceneCustomBinding.get_base_engine_priority() -> int
```

## `unreal.MovieSceneDataLayerSection(MovieSceneSection)`

```python
unreal.MovieSceneDataLayerSection.get_data_layer_assets() -> Array[DataLayerAsset]
unreal.MovieSceneDataLayerSection.get_desired_state() -> DataLayerRuntimeState
unreal.MovieSceneDataLayerSection.get_flush_on_activated() -> bool
unreal.MovieSceneDataLayerSection.get_flush_on_unload() -> bool
unreal.MovieSceneDataLayerSection.get_preroll_state() -> DataLayerRuntimeState
unreal.MovieSceneDataLayerSection.set_data_layer_assets(data_layer_assets: Array[DataLayerAsset]) -> None
unreal.MovieSceneDataLayerSection.set_desired_state(desired_state: DataLayerRuntimeState) -> None
unreal.MovieSceneDataLayerSection.set_flush_on_activated(flush_on_activated: bool) -> None
unreal.MovieSceneDataLayerSection.set_flush_on_unload(flush_on_unload: bool) -> None
unreal.MovieSceneDataLayerSection.set_preroll_state(preroll_state: DataLayerRuntimeState) -> None
```

## `unreal.MovieSceneDoubleVectorTrack(MovieScenePropertyTrack)`

```python
unreal.MovieSceneDoubleVectorTrack.get_num_channels_used() -> int
unreal.MovieSceneDoubleVectorTrack.set_num_channels_used(num_channels_used: int) -> None
```

## `unreal.MovieSceneDoubleVectorTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneDoubleVectorTrackExtensions.get_num_channels_used(track: MovieSceneDoubleVectorTrack) -> int
unreal.MovieSceneDoubleVectorTrackExtensions.set_num_channels_used(track: MovieSceneDoubleVectorTrack, num_channels_used: int) -> None
```

## `unreal.MovieSceneDynamicBinding(StructBase)`

```python
unreal.MovieSceneDynamicBinding.__init__() -> None
```

## `unreal.MovieSceneDynamicBindingPayloadVariable(StructBase)`

```python
unreal.MovieSceneDynamicBindingPayloadVariable.__init__() -> None
```

## `unreal.MovieSceneDynamicBindingResolveParams(StructBase)`

```python
unreal.MovieSceneDynamicBindingResolveParams.__init__(sequence: MovieSceneSequence = None, object_binding_id: Guid = [], root_sequence: MovieSceneSequence = None) -> None
unreal.MovieSceneDynamicBindingResolveParams.object_binding_id(value: Guid) -> None
unreal.MovieSceneDynamicBindingResolveParams.root_sequence(value: MovieSceneSequence) -> None
unreal.MovieSceneDynamicBindingResolveParams.sequence(value: MovieSceneSequence) -> None
```

## `unreal.MovieSceneDynamicBindingResolveResult(StructBase)`

```python
unreal.MovieSceneDynamicBindingResolveResult.__init__(object: Object = None, is_possessed_object: bool = False) -> None
unreal.MovieSceneDynamicBindingResolveResult.is_possessed_object(value: bool) -> None
unreal.MovieSceneDynamicBindingResolveResult.object(value: Object) -> None
```

## `unreal.MovieSceneEasingFunction(Interface)`

```python
unreal.MovieSceneEasingFunction.on_evaluate(interp: float) -> float
```

## `unreal.MovieSceneEasingSettings(StructBase)`

```python
unreal.MovieSceneEasingSettings.__init__() -> None
```

## `unreal.MovieSceneEvent(StructBase)`

```python
unreal.MovieSceneEvent.__init__() -> None
unreal.MovieSceneEvent.get_bound_object_property_class() -> Class
```

## `unreal.MovieSceneEventParameters(StructBase)`

```python
unreal.MovieSceneEventParameters.__init__() -> None
```

## `unreal.MovieSceneEventPayloadVariable(StructBase)`

```python
unreal.MovieSceneEventPayloadVariable.__init__() -> None
```

## `unreal.MovieSceneEventPtrs(StructBase)`

```python
unreal.MovieSceneEventPtrs.__init__() -> None
```

## `unreal.MovieSceneEventTrack(MovieSceneNameableTrack)`

```python
unreal.MovieSceneEventTrack.add_event_repeater_section() -> MovieSceneEventRepeaterSection
unreal.MovieSceneEventTrack.add_event_trigger_section() -> MovieSceneEventTriggerSection
```

## `unreal.MovieSceneEventTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneEventTrackExtensions.add_event_repeater_section(track: MovieSceneEventTrack) -> MovieSceneEventRepeaterSection
unreal.MovieSceneEventTrackExtensions.add_event_trigger_section(track: MovieSceneEventTrack) -> MovieSceneEventTriggerSection
unreal.MovieSceneEventTrackExtensions.get_bound_object_property_class(event_key: MovieSceneEvent) -> Class
```

## `unreal.MovieSceneFloatVectorTrack(MovieScenePropertyTrack)`

```python
unreal.MovieSceneFloatVectorTrack.get_num_channels_used() -> int
unreal.MovieSceneFloatVectorTrack.set_num_channels_used(num_channels_used: int) -> None
```

## `unreal.MovieSceneFloatVectorTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneFloatVectorTrackExtensions.get_num_channels_used(track: MovieSceneFloatVectorTrack) -> int
unreal.MovieSceneFloatVectorTrackExtensions.set_num_channels_used(track: MovieSceneFloatVectorTrack, num_channels_used: int) -> None
```

## `unreal.MovieSceneFolder(Object)`

```python
unreal.MovieSceneFolder.add_child_folder(folder_to_add: MovieSceneFolder) -> bool
unreal.MovieSceneFolder.add_child_object_binding(object_binding: MovieSceneBindingProxy) -> bool
unreal.MovieSceneFolder.add_child_track(track: MovieSceneTrack) -> bool
unreal.MovieSceneFolder.get_child_folders() -> Array[MovieSceneFolder]
unreal.MovieSceneFolder.get_child_object_bindings() -> Array[MovieSceneBindingProxy]
unreal.MovieSceneFolder.get_child_tracks() -> Array[MovieSceneTrack]
unreal.MovieSceneFolder.get_folder_color() -> Color
unreal.MovieSceneFolder.get_folder_name() -> Name
unreal.MovieSceneFolder.remove_child_folder(folder_to_remove: MovieSceneFolder) -> bool
unreal.MovieSceneFolder.remove_child_object_binding(object_binding: MovieSceneBindingProxy) -> bool
unreal.MovieSceneFolder.remove_child_track(track: MovieSceneTrack) -> bool
unreal.MovieSceneFolder.set_folder_color(folder_color: Color) -> bool
unreal.MovieSceneFolder.set_folder_name(folder_name: Name) -> bool
```

## `unreal.MovieSceneFolderExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneFolderExtensions.add_child_folder(target_folder: MovieSceneFolder, folder_to_add: MovieSceneFolder) -> bool
unreal.MovieSceneFolderExtensions.add_child_object_binding(folder: MovieSceneFolder, object_binding: MovieSceneBindingProxy) -> bool
unreal.MovieSceneFolderExtensions.add_child_track(folder: MovieSceneFolder, track: MovieSceneTrack) -> bool
unreal.MovieSceneFolderExtensions.get_child_folders(folder: MovieSceneFolder) -> Array[MovieSceneFolder]
unreal.MovieSceneFolderExtensions.get_child_object_bindings(folder: MovieSceneFolder) -> Array[MovieSceneBindingProxy]
unreal.MovieSceneFolderExtensions.get_child_tracks(folder: MovieSceneFolder) -> Array[MovieSceneTrack]
unreal.MovieSceneFolderExtensions.get_folder_color(folder: MovieSceneFolder) -> Color
unreal.MovieSceneFolderExtensions.get_folder_name(folder: MovieSceneFolder) -> Name
unreal.MovieSceneFolderExtensions.remove_child_folder(target_folder: MovieSceneFolder, folder_to_remove: MovieSceneFolder) -> bool
unreal.MovieSceneFolderExtensions.remove_child_object_binding(folder: MovieSceneFolder, object_binding: MovieSceneBindingProxy) -> bool
unreal.MovieSceneFolderExtensions.remove_child_track(folder: MovieSceneFolder, track: MovieSceneTrack) -> bool
unreal.MovieSceneFolderExtensions.set_folder_color(folder: MovieSceneFolder, folder_color: Color) -> bool
unreal.MovieSceneFolderExtensions.set_folder_name(folder: MovieSceneFolder, folder_name: Name) -> bool
```

## `unreal.MovieSceneFrameRange(StructBase)`

```python
unreal.MovieSceneFrameRange.__init__() -> None
```

## `unreal.MovieSceneGameplayCueEvent(DelegateBase)`

```python
unreal.MovieSceneGameplayCueEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MovieSceneGameplayCueKey(StructBase)`

```python
unreal.MovieSceneGameplayCueKey.__init__() -> None
```

## `unreal.MovieSceneGameplayCueTrack(MovieSceneNameableTrack)`

```python
unreal.MovieSceneGameplayCueTrack.set_sequencer_track_handler(gameplay_cue_track_handler: MovieSceneGameplayCueEvent) -> None
```

## `unreal.MovieSceneGroupCondition(MovieSceneCondition)`

```python
unreal.MovieSceneGroupCondition.operator(value: MovieSceneGroupConditionOperator) -> None
unreal.MovieSceneGroupCondition.sub_conditions(value: Array[MovieSceneConditionContainer]) -> None
```

## `unreal.MovieSceneMarkedFrame(StructBase)`

```python
unreal.MovieSceneMarkedFrame.__init__(frame_number: FrameNumber = [0], label: str = "", is_determinism_fence: bool = False, is_inclusive_time: bool = False) -> None
unreal.MovieSceneMarkedFrame.frame_number(value: FrameNumber) -> None
unreal.MovieSceneMarkedFrame.is_determinism_fence(value: bool) -> None
unreal.MovieSceneMarkedFrame.is_inclusive_time(value: bool) -> None
unreal.MovieSceneMarkedFrame.label(value: str) -> None
```

## `unreal.MovieSceneMediaPlayerPropertySection(MovieSceneSection)`

```python
unreal.MovieSceneMediaPlayerPropertySection.loop(value: bool) -> None
unreal.MovieSceneMediaPlayerPropertySection.media_source(value: MediaSource) -> None
```

## `unreal.MovieSceneMediaSection(MovieSceneSection)`

```python
unreal.MovieSceneMediaSection.cache_settings(value: MediaSourceCacheSettings) -> None
unreal.MovieSceneMediaSection.external_media_player(value: MediaPlayer) -> None
unreal.MovieSceneMediaSection.looping(value: bool) -> None
unreal.MovieSceneMediaSection.media_sound_component(value: MediaSoundComponent) -> None
unreal.MovieSceneMediaSection.media_source(value: MediaSource) -> None
unreal.MovieSceneMediaSection.media_source_proxy_index(value: int) -> None
unreal.MovieSceneMediaSection.media_texture(value: MediaTexture) -> None
unreal.MovieSceneMediaSection.start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneMediaSection.texture_index(value: int) -> None
unreal.MovieSceneMediaSection.use_external_media_player(value: bool) -> None
```

## `unreal.MovieSceneMetaData(Object)`

```python
unreal.MovieSceneMetaData.get_author() -> str
unreal.MovieSceneMetaData.get_created() -> DateTime
unreal.MovieSceneMetaData.get_notes() -> str
unreal.MovieSceneMetaData.set_author(author: str) -> None
unreal.MovieSceneMetaData.set_created(created: DateTime) -> None
unreal.MovieSceneMetaData.set_notes(notes: str) -> None
```

## `unreal.MovieSceneNumericVariant(StructBase)`

```python
unreal.MovieSceneNumericVariant.__init__() -> None
```

## `unreal.MovieSceneObjectBindingID(StructBase)`

```python
unreal.MovieSceneObjectBindingID.__init__() -> None
```

## `unreal.MovieSceneObjectBindingPtr(MovieSceneObjectBindingID)`

```python
unreal.MovieSceneObjectBindingPtr.__init__() -> None
```

## `unreal.MovieSceneObjectPropertyTrack(MovieScenePropertyTrack)`

```python
unreal.MovieSceneObjectPropertyTrack.get_object_property_class() -> Class
unreal.MovieSceneObjectPropertyTrack.set_object_property_class(property_class: Class) -> None
```

## `unreal.MovieSceneParameterSection(MovieSceneSection)`

```python
unreal.MovieSceneParameterSection.add_bool_parameter_key(parameter_name: Name, time: FrameNumber, value: bool) -> None
unreal.MovieSceneParameterSection.add_color_parameter_key(parameter_name: Name, time: FrameNumber, value: LinearColor) -> None
unreal.MovieSceneParameterSection.add_scalar_parameter_key(parameter_name: Name, time: FrameNumber, value: float) -> None
unreal.MovieSceneParameterSection.add_transform_parameter_key(parameter_name: Name, time: FrameNumber, value: Transform) -> None
unreal.MovieSceneParameterSection.add_vector2d_parameter_key(parameter_name: Name, time: FrameNumber, value: Vector2D) -> None
unreal.MovieSceneParameterSection.add_vector_parameter_key(parameter_name: Name, time: FrameNumber, value: Vector) -> None
unreal.MovieSceneParameterSection.get_parameter_names() -> Set[Name]
unreal.MovieSceneParameterSection.remove_bool_parameter(parameter_name: Name) -> bool
unreal.MovieSceneParameterSection.remove_color_parameter(parameter_name: Name) -> bool
unreal.MovieSceneParameterSection.remove_scalar_parameter(parameter_name: Name) -> bool
unreal.MovieSceneParameterSection.remove_transform_parameter(parameter_name: Name) -> bool
unreal.MovieSceneParameterSection.remove_vector2d_parameter(parameter_name: Name) -> bool
unreal.MovieSceneParameterSection.remove_vector_parameter(parameter_name: Name) -> bool
```

## `unreal.MovieScenePasteBindingsParams(StructBase)`

```python
unreal.MovieScenePasteBindingsParams.__init__(bindings: Array[MovieSceneBindingProxy] = [], parent_folder: MovieSceneFolder = None, folders: Array[MovieSceneFolder] = [], duplicate_existing_actors: bool = False, pasted_actors: Map[Name, Actor] = {}) -> None
unreal.MovieScenePasteBindingsParams.bindings(value: Array[MovieSceneBindingProxy]) -> None
unreal.MovieScenePasteBindingsParams.duplicate_existing_actors(value: bool) -> None
unreal.MovieScenePasteBindingsParams.folders(value: Array[MovieSceneFolder]) -> None
unreal.MovieScenePasteBindingsParams.parent_folder(value: MovieSceneFolder) -> None
unreal.MovieScenePasteBindingsParams.pasted_actors(value: Map[Name, Actor]) -> None
```

## `unreal.MovieScenePasteFoldersParams(StructBase)`

```python
unreal.MovieScenePasteFoldersParams.__init__(sequence: MovieSceneSequence = None, parent_folder: MovieSceneFolder = None) -> None
unreal.MovieScenePasteFoldersParams.parent_folder(value: MovieSceneFolder) -> None
unreal.MovieScenePasteFoldersParams.sequence(value: MovieSceneSequence) -> None
```

## `unreal.MovieScenePasteSectionsParams(StructBase)`

```python
unreal.MovieScenePasteSectionsParams.__init__(tracks: Array[MovieSceneTrack] = [], track_row_indices: Array[int] = [], time: FrameTime = [[0], 0.000000]) -> None
unreal.MovieScenePasteSectionsParams.time(value: FrameTime) -> None
unreal.MovieScenePasteSectionsParams.track_row_indices(value: Array[int]) -> None
unreal.MovieScenePasteSectionsParams.tracks(value: Array[MovieSceneTrack]) -> None
```

## `unreal.MovieScenePasteTracksParams(StructBase)`

```python
unreal.MovieScenePasteTracksParams.__init__(sequence: MovieSceneSequence = None, bindings: Array[MovieSceneBindingProxy] = [], parent_folder: MovieSceneFolder = None, folders: Array[MovieSceneFolder] = []) -> None
unreal.MovieScenePasteTracksParams.bindings(value: Array[MovieSceneBindingProxy]) -> None
unreal.MovieScenePasteTracksParams.folders(value: Array[MovieSceneFolder]) -> None
unreal.MovieScenePasteTracksParams.parent_folder(value: MovieSceneFolder) -> None
unreal.MovieScenePasteTracksParams.sequence(value: MovieSceneSequence) -> None
```

## `unreal.MovieScenePropertyTrack(MovieSceneNameableTrack)`

```python
unreal.MovieScenePropertyTrack.get_property_name() -> Name
unreal.MovieScenePropertyTrack.get_property_path() -> str
unreal.MovieScenePropertyTrack.get_unique_track_name() -> Name
unreal.MovieScenePropertyTrack.set_property_name_and_path(property_name: Name, property_path: str) -> None
```

## `unreal.MovieScenePropertyTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieScenePropertyTrackExtensions.get_byte_track_enum(track: MovieSceneByteTrack) -> Enum
unreal.MovieScenePropertyTrackExtensions.get_object_property_class(track: MovieSceneObjectPropertyTrack) -> Class
unreal.MovieScenePropertyTrackExtensions.get_property_name(track: MovieScenePropertyTrack) -> Name
unreal.MovieScenePropertyTrackExtensions.get_property_path(track: MovieScenePropertyTrack) -> str
unreal.MovieScenePropertyTrackExtensions.get_unique_track_name(track: MovieScenePropertyTrack) -> Name
unreal.MovieScenePropertyTrackExtensions.set_byte_track_enum(track: MovieSceneByteTrack, enum: Enum) -> None
unreal.MovieScenePropertyTrackExtensions.set_object_property_class(track: MovieSceneObjectPropertyTrack, property_class: Class) -> None
unreal.MovieScenePropertyTrackExtensions.set_property_name_and_path(track: MovieScenePropertyTrack, property_name: Name, property_path: str) -> None
```

## `unreal.MovieSceneReplaceableBindingBase(MovieSceneCustomBinding)`

```python
unreal.MovieSceneReplaceableBindingBase.preview_spawnable() -> MovieSceneSpawnableBindingBase
```

## `unreal.MovieSceneScriptingBoolChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingBoolChannel.add_key(time: FrameNumber, new_value: bool, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingBoolKey
unreal.MovieSceneScriptingBoolChannel.compute_effective_range() -> SequencerScriptingRange
unreal.MovieSceneScriptingBoolChannel.evaluate_keys(range: SequencerScriptingRange, frame_rate: FrameRate) -> Array[bool]
unreal.MovieSceneScriptingBoolChannel.get_default() -> bool
unreal.MovieSceneScriptingBoolChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingBoolChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingBoolChannel.get_num_keys() -> int
unreal.MovieSceneScriptingBoolChannel.has_default() -> bool
unreal.MovieSceneScriptingBoolChannel.remove_default() -> None
unreal.MovieSceneScriptingBoolChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingBoolChannel.set_default(default_value: bool) -> None
```

## `unreal.MovieSceneScriptingBoolKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingBoolKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingBoolKey.get_value() -> bool
unreal.MovieSceneScriptingBoolKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingBoolKey.set_value(new_value: bool) -> None
```

## `unreal.MovieSceneScriptingByteChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingByteChannel.add_key(time: FrameNumber, new_value: int, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.AUTO) -> MovieSceneScriptingByteKey
unreal.MovieSceneScriptingByteChannel.get_default() -> int
unreal.MovieSceneScriptingByteChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingByteChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingByteChannel.has_default() -> bool
unreal.MovieSceneScriptingByteChannel.remove_default() -> None
unreal.MovieSceneScriptingByteChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingByteChannel.set_default(default_value: int) -> None
```

## `unreal.MovieSceneScriptingByteKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingByteKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingByteKey.get_value() -> int
unreal.MovieSceneScriptingByteKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingByteKey.set_value(new_value: int) -> None
```

## `unreal.MovieSceneScriptingChannel(Object)`

```python
unreal.MovieSceneScriptingChannel.channel_name() -> Name
```

## `unreal.MovieSceneScriptingDoubleChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingDoubleChannel.add_key(time: FrameNumber, new_value: float, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.AUTO) -> MovieSceneScriptingDoubleKey
unreal.MovieSceneScriptingDoubleChannel.compute_effective_range() -> SequencerScriptingRange
unreal.MovieSceneScriptingDoubleChannel.evaluate_keys(range: SequencerScriptingRange, frame_rate: FrameRate) -> Array[float]
unreal.MovieSceneScriptingDoubleChannel.get_default() -> float
unreal.MovieSceneScriptingDoubleChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingDoubleChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingDoubleChannel.get_num_keys() -> int
unreal.MovieSceneScriptingDoubleChannel.get_post_infinity_extrapolation() -> RichCurveExtrapolation
unreal.MovieSceneScriptingDoubleChannel.get_pre_infinity_extrapolation() -> RichCurveExtrapolation
unreal.MovieSceneScriptingDoubleChannel.has_default() -> bool
unreal.MovieSceneScriptingDoubleChannel.remove_default() -> None
unreal.MovieSceneScriptingDoubleChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingDoubleChannel.set_default(default_value: float) -> None
unreal.MovieSceneScriptingDoubleChannel.set_post_infinity_extrapolation(extrapolation: RichCurveExtrapolation) -> None
unreal.MovieSceneScriptingDoubleChannel.set_pre_infinity_extrapolation(extrapolation: RichCurveExtrapolation) -> None
```

## `unreal.MovieSceneScriptingDoubleKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingDoubleKey.get_arrive_tangent() -> float
unreal.MovieSceneScriptingDoubleKey.get_arrive_tangent_weight() -> float
unreal.MovieSceneScriptingDoubleKey.get_interpolation_mode() -> RichCurveInterpMode
unreal.MovieSceneScriptingDoubleKey.get_leave_tangent() -> float
unreal.MovieSceneScriptingDoubleKey.get_leave_tangent_weight() -> float
unreal.MovieSceneScriptingDoubleKey.get_tangent_mode() -> RichCurveTangentMode
unreal.MovieSceneScriptingDoubleKey.get_tangent_weight_mode() -> RichCurveTangentWeightMode
unreal.MovieSceneScriptingDoubleKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingDoubleKey.get_value() -> float
unreal.MovieSceneScriptingDoubleKey.set_arrive_tangent(new_value: float) -> None
unreal.MovieSceneScriptingDoubleKey.set_arrive_tangent_weight(new_value: float) -> None
unreal.MovieSceneScriptingDoubleKey.set_interpolation_mode(new_value: RichCurveInterpMode) -> None
unreal.MovieSceneScriptingDoubleKey.set_leave_tangent(new_value: float) -> None
unreal.MovieSceneScriptingDoubleKey.set_leave_tangent_weight(new_value: float) -> None
unreal.MovieSceneScriptingDoubleKey.set_tangent_mode(new_value: RichCurveTangentMode) -> None
unreal.MovieSceneScriptingDoubleKey.set_tangent_weight_mode(new_value: RichCurveTangentWeightMode) -> None
unreal.MovieSceneScriptingDoubleKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingDoubleKey.set_value(new_value: float) -> None
```

## `unreal.MovieSceneScriptingEventChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingEventChannel.add_key(time: FrameNumber, new_value: MovieSceneEvent, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingEventKey
unreal.MovieSceneScriptingEventChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingEventChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingEventChannel.remove_key(key: MovieSceneScriptingKey) -> None
```

## `unreal.MovieSceneScriptingEventKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingEventKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingEventKey.get_value() -> MovieSceneEvent
unreal.MovieSceneScriptingEventKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingEventKey.set_value(new_value: MovieSceneEvent) -> None
```

## `unreal.MovieSceneScriptingFloatChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingFloatChannel.add_key(time: FrameNumber, new_value: float, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE, interpolation: MovieSceneKeyInterpolation = MovieSceneKeyInterpolation.AUTO) -> MovieSceneScriptingFloatKey
unreal.MovieSceneScriptingFloatChannel.compute_effective_range() -> SequencerScriptingRange
unreal.MovieSceneScriptingFloatChannel.evaluate_keys(range: SequencerScriptingRange, frame_rate: FrameRate) -> Array[float]
unreal.MovieSceneScriptingFloatChannel.get_default() -> float
unreal.MovieSceneScriptingFloatChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingFloatChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingFloatChannel.get_num_keys() -> int
unreal.MovieSceneScriptingFloatChannel.get_post_infinity_extrapolation() -> RichCurveExtrapolation
unreal.MovieSceneScriptingFloatChannel.get_pre_infinity_extrapolation() -> RichCurveExtrapolation
unreal.MovieSceneScriptingFloatChannel.has_default() -> bool
unreal.MovieSceneScriptingFloatChannel.remove_default() -> None
unreal.MovieSceneScriptingFloatChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingFloatChannel.set_default(default_value: float) -> None
unreal.MovieSceneScriptingFloatChannel.set_post_infinity_extrapolation(extrapolation: RichCurveExtrapolation) -> None
unreal.MovieSceneScriptingFloatChannel.set_pre_infinity_extrapolation(extrapolation: RichCurveExtrapolation) -> None
```

## `unreal.MovieSceneScriptingFloatKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingFloatKey.get_arrive_tangent() -> float
unreal.MovieSceneScriptingFloatKey.get_arrive_tangent_weight() -> float
unreal.MovieSceneScriptingFloatKey.get_interpolation_mode() -> RichCurveInterpMode
unreal.MovieSceneScriptingFloatKey.get_leave_tangent() -> float
unreal.MovieSceneScriptingFloatKey.get_leave_tangent_weight() -> float
unreal.MovieSceneScriptingFloatKey.get_tangent_mode() -> RichCurveTangentMode
unreal.MovieSceneScriptingFloatKey.get_tangent_weight_mode() -> RichCurveTangentWeightMode
unreal.MovieSceneScriptingFloatKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingFloatKey.get_value() -> float
unreal.MovieSceneScriptingFloatKey.set_arrive_tangent(new_value: float) -> None
unreal.MovieSceneScriptingFloatKey.set_arrive_tangent_weight(new_value: float) -> None
unreal.MovieSceneScriptingFloatKey.set_interpolation_mode(new_value: RichCurveInterpMode) -> None
unreal.MovieSceneScriptingFloatKey.set_leave_tangent(new_value: float) -> None
unreal.MovieSceneScriptingFloatKey.set_leave_tangent_weight(new_value: float) -> None
unreal.MovieSceneScriptingFloatKey.set_tangent_mode(new_value: RichCurveTangentMode) -> None
unreal.MovieSceneScriptingFloatKey.set_tangent_weight_mode(new_value: RichCurveTangentWeightMode) -> None
unreal.MovieSceneScriptingFloatKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingFloatKey.set_value(new_value: float) -> None
```

## `unreal.MovieSceneScriptingIntegerChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingIntegerChannel.add_key(time: FrameNumber, new_value: int, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingIntegerKey
unreal.MovieSceneScriptingIntegerChannel.evaluate_keys(range: SequencerScriptingRange, frame_rate: FrameRate) -> Array[int]
unreal.MovieSceneScriptingIntegerChannel.get_default() -> int
unreal.MovieSceneScriptingIntegerChannel.get_interpolate_linear_keys() -> bool
unreal.MovieSceneScriptingIntegerChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingIntegerChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingIntegerChannel.get_num_keys() -> int
unreal.MovieSceneScriptingIntegerChannel.has_default() -> bool
unreal.MovieSceneScriptingIntegerChannel.remove_default() -> None
unreal.MovieSceneScriptingIntegerChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingIntegerChannel.set_default(default_value: int) -> None
unreal.MovieSceneScriptingIntegerChannel.set_interpolate_linear_keys(interpolate_linear_keys: bool) -> None
```

## `unreal.MovieSceneScriptingIntegerKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingIntegerKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingIntegerKey.get_value() -> int
unreal.MovieSceneScriptingIntegerKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingIntegerKey.set_value(new_value: int) -> None
```

## `unreal.MovieSceneScriptingObjectPathChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingObjectPathChannel.add_key(time: FrameNumber, new_value: Object, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingObjectPathKey
unreal.MovieSceneScriptingObjectPathChannel.get_default() -> Object
unreal.MovieSceneScriptingObjectPathChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingObjectPathChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingObjectPathChannel.has_default() -> bool
unreal.MovieSceneScriptingObjectPathChannel.remove_default() -> None
unreal.MovieSceneScriptingObjectPathChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingObjectPathChannel.set_default(default_value: Object) -> None
```

## `unreal.MovieSceneScriptingObjectPathKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingObjectPathKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingObjectPathKey.get_value() -> Object
unreal.MovieSceneScriptingObjectPathKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingObjectPathKey.set_value(new_value: Object) -> None
```

## `unreal.MovieSceneScriptingParams(StructBase)`

```python
unreal.MovieSceneScriptingParams.__init__(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingParams.time_unit(value: MovieSceneTimeUnit) -> None
```

## `unreal.MovieSceneScriptingStringChannel(MovieSceneScriptingChannel)`

```python
unreal.MovieSceneScriptingStringChannel.add_key(time: FrameNumber, new_value: str, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> MovieSceneScriptingStringKey
unreal.MovieSceneScriptingStringChannel.get_default() -> str
unreal.MovieSceneScriptingStringChannel.get_keys() -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingStringChannel.get_keys_by_index(indices: Array[int]) -> Array[MovieSceneScriptingKey]
unreal.MovieSceneScriptingStringChannel.has_default() -> bool
unreal.MovieSceneScriptingStringChannel.remove_default() -> None
unreal.MovieSceneScriptingStringChannel.remove_key(key: MovieSceneScriptingKey) -> None
unreal.MovieSceneScriptingStringChannel.set_default(default_value: str) -> None
```

## `unreal.MovieSceneScriptingStringKey(MovieSceneScriptingKey)`

```python
unreal.MovieSceneScriptingStringKey.get_time(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameTime
unreal.MovieSceneScriptingStringKey.get_value() -> str
unreal.MovieSceneScriptingStringKey.set_time(new_frame_number: FrameNumber, sub_frame: float = 0.000000, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneScriptingStringKey.set_value(new_value: str) -> None
```

## `unreal.MovieSceneSection(MovieSceneSignedObject)`

```python
unreal.MovieSceneSection.get_all_channels() -> Array[MovieSceneScriptingChannel]
unreal.MovieSceneSection.get_auto_size_end_frame() -> int
unreal.MovieSceneSection.get_auto_size_end_frame_seconds() -> float
unreal.MovieSceneSection.get_auto_size_has_end_frame() -> bool
unreal.MovieSceneSection.get_auto_size_has_start_frame() -> bool
unreal.MovieSceneSection.get_auto_size_start_frame() -> int
unreal.MovieSceneSection.get_auto_size_start_frame_seconds() -> float
unreal.MovieSceneSection.get_blend_type() -> OptionalMovieSceneBlendType
unreal.MovieSceneSection.get_channel(channel_name: Name) -> MovieSceneScriptingChannel
unreal.MovieSceneSection.get_channels_by_type(channel_type: Class) -> Array[MovieSceneScriptingChannel]
unreal.MovieSceneSection.get_color_tint() -> Color
unreal.MovieSceneSection.get_completion_mode() -> MovieSceneCompletionMode
unreal.MovieSceneSection.get_end_frame() -> int
unreal.MovieSceneSection.get_end_frame_seconds() -> float
unreal.MovieSceneSection.get_overlap_priority() -> int
unreal.MovieSceneSection.get_post_roll_frames() -> int
unreal.MovieSceneSection.get_pre_roll_frames() -> int
unreal.MovieSceneSection.get_row_index() -> int
unreal.MovieSceneSection.get_start_frame() -> int
unreal.MovieSceneSection.get_start_frame_seconds() -> float
unreal.MovieSceneSection.has_end_frame() -> bool
unreal.MovieSceneSection.has_start_frame() -> bool
unreal.MovieSceneSection.is_active() -> bool
unreal.MovieSceneSection.is_locked() -> bool
unreal.MovieSceneSection.set_blend_type(blend_type: MovieSceneBlendType) -> None
unreal.MovieSceneSection.set_color_tint(color_tint: Color) -> None
unreal.MovieSceneSection.set_completion_mode(completion_mode: MovieSceneCompletionMode) -> None
unreal.MovieSceneSection.set_end_frame(end_frame: int) -> None
unreal.MovieSceneSection.set_end_frame_bounded(is_bounded: bool) -> None
unreal.MovieSceneSection.set_end_frame_seconds(end_time: float) -> None
unreal.MovieSceneSection.set_is_active(is_active: bool) -> None
unreal.MovieSceneSection.set_is_locked(is_locked: bool) -> None
unreal.MovieSceneSection.set_overlap_priority(new_priority: int) -> None
unreal.MovieSceneSection.set_post_roll_frames(post_roll_frames: int) -> None
unreal.MovieSceneSection.set_pre_roll_frames(pre_roll_frames: int) -> None
unreal.MovieSceneSection.set_range(start_frame: int, end_frame: int) -> None
unreal.MovieSceneSection.set_range_seconds(start_time: float, end_time: float) -> None
unreal.MovieSceneSection.set_row_index(new_row_index: int) -> None
unreal.MovieSceneSection.set_start_frame(start_frame: int) -> None
unreal.MovieSceneSection.set_start_frame_bounded(is_bounded: bool) -> None
unreal.MovieSceneSection.set_start_frame_seconds(start_time: float) -> None
```

## `unreal.MovieSceneSectionEvalOptions(StructBase)`

```python
unreal.MovieSceneSectionEvalOptions.__init__() -> None
```

## `unreal.MovieSceneSectionExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneSectionExtensions.get_all_channels(section: MovieSceneSection) -> Array[MovieSceneScriptingChannel]
unreal.MovieSceneSectionExtensions.get_auto_size_end_frame(section: MovieSceneSection) -> int
unreal.MovieSceneSectionExtensions.get_auto_size_end_frame_seconds(section: MovieSceneSection) -> float
unreal.MovieSceneSectionExtensions.get_auto_size_has_end_frame(section: MovieSceneSection) -> bool
unreal.MovieSceneSectionExtensions.get_auto_size_has_start_frame(section: MovieSceneSection) -> bool
unreal.MovieSceneSectionExtensions.get_auto_size_start_frame(section: MovieSceneSection) -> int
unreal.MovieSceneSectionExtensions.get_auto_size_start_frame_seconds(section: MovieSceneSection) -> float
unreal.MovieSceneSectionExtensions.get_channel(section: MovieSceneSection, channel_name: Name) -> MovieSceneScriptingChannel
unreal.MovieSceneSectionExtensions.get_channels_by_type(section: MovieSceneSection, channel_type: Class) -> Array[MovieSceneScriptingChannel]
unreal.MovieSceneSectionExtensions.get_end_frame(section: MovieSceneSection) -> int
unreal.MovieSceneSectionExtensions.get_end_frame_seconds(section: MovieSceneSection) -> float
unreal.MovieSceneSectionExtensions.get_parent_sequence_frame(section: MovieSceneSubSection, frame: int, parent_sequence: MovieSceneSequence) -> int
unreal.MovieSceneSectionExtensions.get_start_frame(section: MovieSceneSection) -> int
unreal.MovieSceneSectionExtensions.get_start_frame_seconds(section: MovieSceneSection) -> float
unreal.MovieSceneSectionExtensions.has_end_frame(section: MovieSceneSection) -> bool
unreal.MovieSceneSectionExtensions.has_start_frame(section: MovieSceneSection) -> bool
unreal.MovieSceneSectionExtensions.set_end_frame(section: MovieSceneSection, end_frame: int) -> None
unreal.MovieSceneSectionExtensions.set_end_frame_bounded(section: MovieSceneSection, is_bounded: bool) -> None
unreal.MovieSceneSectionExtensions.set_end_frame_seconds(section: MovieSceneSection, end_time: float) -> None
unreal.MovieSceneSectionExtensions.set_range(section: MovieSceneSection, start_frame: int, end_frame: int) -> None
unreal.MovieSceneSectionExtensions.set_range_seconds(section: MovieSceneSection, start_time: float, end_time: float) -> None
unreal.MovieSceneSectionExtensions.set_start_frame(section: MovieSceneSection, start_frame: int) -> None
unreal.MovieSceneSectionExtensions.set_start_frame_bounded(section: MovieSceneSection, is_bounded: bool) -> None
unreal.MovieSceneSectionExtensions.set_start_frame_seconds(section: MovieSceneSection, start_time: float) -> None
```

## `unreal.MovieSceneSectionParameters(StructBase)`

```python
unreal.MovieSceneSectionParameters.__init__(start_frame_offset: FrameNumber = [0], can_loop: bool = False, end_frame_offset: FrameNumber = [0], first_loop_start_frame_offset: FrameNumber = [0], time_scale: MovieSceneTimeWarpVariant = [1.000000], hierarchical_bias: int = 0, flags: MovieSceneSubSectionFlags = MovieSceneSubSectionFlags.NONE) -> None
unreal.MovieSceneSectionParameters.can_loop(value: bool) -> None
unreal.MovieSceneSectionParameters.end_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionParameters.first_loop_start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionParameters.flags(value: MovieSceneSubSectionFlags) -> None
unreal.MovieSceneSectionParameters.hierarchical_bias(value: int) -> None
unreal.MovieSceneSectionParameters.start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionParameters.time_scale(value: MovieSceneTimeWarpVariant) -> None
```

## `unreal.MovieSceneSectionTimingParametersFrames(StructBase)`

```python
unreal.MovieSceneSectionTimingParametersFrames.__init__(play_rate: MovieSceneTimeWarpVariant = [1.000000], inner_start_offset: FrameNumber = [0], inner_end_offset: FrameNumber = [0], first_loop_start_offset: FrameNumber = [0], loop: bool = False, clamp: bool = False, reverse: bool = False) -> None
unreal.MovieSceneSectionTimingParametersFrames.clamp(value: bool) -> None
unreal.MovieSceneSectionTimingParametersFrames.first_loop_start_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionTimingParametersFrames.inner_end_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionTimingParametersFrames.inner_start_offset(value: FrameNumber) -> None
unreal.MovieSceneSectionTimingParametersFrames.loop(value: bool) -> None
unreal.MovieSceneSectionTimingParametersFrames.play_rate(value: MovieSceneTimeWarpVariant) -> None
unreal.MovieSceneSectionTimingParametersFrames.reverse(value: bool) -> None
```

## `unreal.MovieSceneSectionTimingParametersSeconds(StructBase)`

```python
unreal.MovieSceneSectionTimingParametersSeconds.__init__(play_rate: MovieSceneTimeWarpVariant = [1.000000], inner_start_offset: float = 0.000000, inner_end_offset: float = 0.000000, first_loop_start_offset: float = 0.000000, loop: bool = False, clamp: bool = False, reverse: bool = False) -> None
unreal.MovieSceneSectionTimingParametersSeconds.clamp(value: bool) -> None
unreal.MovieSceneSectionTimingParametersSeconds.first_loop_start_offset(value: float) -> None
unreal.MovieSceneSectionTimingParametersSeconds.inner_end_offset(value: float) -> None
unreal.MovieSceneSectionTimingParametersSeconds.inner_start_offset(value: float) -> None
unreal.MovieSceneSectionTimingParametersSeconds.loop(value: bool) -> None
unreal.MovieSceneSectionTimingParametersSeconds.play_rate(value: MovieSceneTimeWarpVariant) -> None
unreal.MovieSceneSectionTimingParametersSeconds.reverse(value: bool) -> None
```

## `unreal.MovieSceneSequence(MovieSceneSignedObject)`

```python
unreal.MovieSceneSequence.add_marked_frame(marked_frame: MovieSceneMarkedFrame) -> int
unreal.MovieSceneSequence.add_marked_frame_to_sequence(marked_frame: MovieSceneMarkedFrame, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequence.add_possessable(object_to_possess: Object) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.add_root_folder_to_sequence(new_folder_name: str) -> MovieSceneFolder
unreal.MovieSceneSequence.add_spawnable_from_class(class_to_spawn: Class) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.add_spawnable_from_instance(object_to_spawn: Object) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.add_track(track_type: Class) -> MovieSceneTrack
unreal.MovieSceneSequence.are_marked_frames_locked() -> bool
unreal.MovieSceneSequence.delete_marked_frame(delete_index: int) -> None
unreal.MovieSceneSequence.delete_marked_frames() -> None
unreal.MovieSceneSequence.find_binding_by_id(binding_id: Guid) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.find_binding_by_name(name: str) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.find_binding_by_tag(binding_name: Name) -> MovieSceneObjectBindingID
unreal.MovieSceneSequence.find_bindings_by_tag(binding_name: Name) -> Array[MovieSceneObjectBindingID]
unreal.MovieSceneSequence.find_marked_frame_by_frame_number(frame_number: FrameNumber) -> int
unreal.MovieSceneSequence.find_marked_frame_by_frame_number_in_sequence(frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequence.find_marked_frame_by_label(label: str) -> int
unreal.MovieSceneSequence.find_next_marked_frame(frame_number: FrameNumber, forward: bool) -> int
unreal.MovieSceneSequence.find_next_marked_frame_in_sequence(frame_number: FrameNumber, forward: bool, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequence.find_tracks_by_exact_type(track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneSequence.find_tracks_by_type(track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneSequence.get_binding_id(binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
unreal.MovieSceneSequence.get_bindings() -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequence.get_clock_source() -> UpdateClockSource
unreal.MovieSceneSequence.get_display_rate() -> FrameRate
unreal.MovieSceneSequence.get_earliest_timecode_source() -> MovieSceneTimecodeSource
unreal.MovieSceneSequence.get_evaluation_type() -> MovieSceneEvaluationType
unreal.MovieSceneSequence.get_marked_frames() -> Array[MovieSceneMarkedFrame]
unreal.MovieSceneSequence.get_marked_frames_from_sequence(time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[MovieSceneMarkedFrame]
unreal.MovieSceneSequence.get_movie_scene() -> MovieScene
unreal.MovieSceneSequence.get_playback_end() -> int
unreal.MovieSceneSequence.get_playback_end_seconds() -> float
unreal.MovieSceneSequence.get_playback_range() -> SequencerScriptingRange
unreal.MovieSceneSequence.get_playback_start() -> int
unreal.MovieSceneSequence.get_playback_start_seconds() -> float
unreal.MovieSceneSequence.get_portable_binding_id(destination_sequence: MovieSceneSequence, binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
unreal.MovieSceneSequence.get_possessables() -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequence.get_root_folders_in_sequence() -> Array[MovieSceneFolder]
unreal.MovieSceneSequence.get_spawnables() -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequence.get_tick_resolution() -> FrameRate
unreal.MovieSceneSequence.get_tracks() -> Array[MovieSceneTrack]
unreal.MovieSceneSequence.get_view_range_end() -> float
unreal.MovieSceneSequence.get_view_range_start() -> float
unreal.MovieSceneSequence.get_work_range_end() -> float
unreal.MovieSceneSequence.get_work_range_start() -> float
unreal.MovieSceneSequence.is_playback_range_locked() -> bool
unreal.MovieSceneSequence.is_read_only() -> bool
unreal.MovieSceneSequence.locate_bound_objects(binding: MovieSceneBindingProxy, context: Object) -> Array[Object]
unreal.MovieSceneSequence.make_range(start_frame: int, duration: int) -> SequencerScriptingRange
unreal.MovieSceneSequence.make_range_seconds(start_time: float, duration: float) -> SequencerScriptingRange
unreal.MovieSceneSequence.remove_root_folder_from_sequence(folder: MovieSceneFolder) -> None
unreal.MovieSceneSequence.remove_track(track: MovieSceneTrack) -> bool
unreal.MovieSceneSequence.resolve_binding_id(object_binding_id: MovieSceneObjectBindingID) -> MovieSceneBindingProxy
unreal.MovieSceneSequence.set_clock_source(clock_source: UpdateClockSource) -> None
unreal.MovieSceneSequence.set_display_rate(display_rate: FrameRate) -> None
unreal.MovieSceneSequence.set_evaluation_type(evaluation_type: MovieSceneEvaluationType) -> None
unreal.MovieSceneSequence.set_marked_frame(mark_index: int, frame_number: FrameNumber) -> None
unreal.MovieSceneSequence.set_marked_frame_in_sequence(mark_index: int, frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneSequence.set_marked_frames_locked(locked: bool) -> None
unreal.MovieSceneSequence.set_playback_end(end_frame: int) -> None
unreal.MovieSceneSequence.set_playback_end_seconds(end_time: float) -> None
unreal.MovieSceneSequence.set_playback_range_locked(locked: bool) -> None
unreal.MovieSceneSequence.set_playback_start(start_frame: int) -> None
unreal.MovieSceneSequence.set_playback_start_seconds(start_time: float) -> None
unreal.MovieSceneSequence.set_read_only(read_only: bool) -> None
unreal.MovieSceneSequence.set_tick_resolution(tick_resolution: FrameRate) -> None
unreal.MovieSceneSequence.set_tick_resolution_directly(tick_resolution: FrameRate) -> None
unreal.MovieSceneSequence.set_view_range_end(end_time_in_seconds: float) -> None
unreal.MovieSceneSequence.set_view_range_start(start_time_in_seconds: float) -> None
unreal.MovieSceneSequence.set_work_range_end(end_time_in_seconds: float) -> None
unreal.MovieSceneSequence.set_work_range_start(start_time_in_seconds: float) -> None
unreal.MovieSceneSequence.sort_marked_frames() -> None
```

## `unreal.MovieSceneSequenceExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneSequenceExtensions.add_marked_frame(sequence: MovieSceneSequence, marked_frame: MovieSceneMarkedFrame) -> int
unreal.MovieSceneSequenceExtensions.add_marked_frame_to_sequence(sequence: MovieSceneSequence, marked_frame: MovieSceneMarkedFrame, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequenceExtensions.add_possessable(sequence: MovieSceneSequence, object_to_possess: Object) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.add_root_folder_to_sequence(sequence: MovieSceneSequence, new_folder_name: str) -> MovieSceneFolder
unreal.MovieSceneSequenceExtensions.add_spawnable_from_class(sequence: MovieSceneSequence, class_to_spawn: Class) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.add_spawnable_from_instance(sequence: MovieSceneSequence, object_to_spawn: Object) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.add_track(sequence: MovieSceneSequence, track_type: Class) -> MovieSceneTrack
unreal.MovieSceneSequenceExtensions.are_marked_frames_locked(sequence: MovieSceneSequence) -> bool
unreal.MovieSceneSequenceExtensions.delete_marked_frame(sequence: MovieSceneSequence, delete_index: int) -> None
unreal.MovieSceneSequenceExtensions.delete_marked_frames(sequence: MovieSceneSequence) -> None
unreal.MovieSceneSequenceExtensions.find_binding_by_id(sequence: MovieSceneSequence, binding_id: Guid) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.find_binding_by_name(sequence: MovieSceneSequence, name: str) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.find_marked_frame_by_frame_number(sequence: MovieSceneSequence, frame_number: FrameNumber) -> int
unreal.MovieSceneSequenceExtensions.find_marked_frame_by_frame_number_in_sequence(sequence: MovieSceneSequence, frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequenceExtensions.find_marked_frame_by_label(sequence: MovieSceneSequence, label: str) -> int
unreal.MovieSceneSequenceExtensions.find_next_marked_frame(sequence: MovieSceneSequence, frame_number: FrameNumber, forward: bool) -> int
unreal.MovieSceneSequenceExtensions.find_next_marked_frame_in_sequence(sequence: MovieSceneSequence, frame_number: FrameNumber, forward: bool, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> int
unreal.MovieSceneSequenceExtensions.find_tracks_by_exact_type(sequence: MovieSceneSequence, track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneSequenceExtensions.find_tracks_by_type(sequence: MovieSceneSequence, track_type: Class) -> Array[MovieSceneTrack]
unreal.MovieSceneSequenceExtensions.get_binding_id(sequence: MovieSceneSequence, binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
unreal.MovieSceneSequenceExtensions.get_bindings(sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequenceExtensions.get_clock_source(sequence: MovieSceneSequence) -> UpdateClockSource
unreal.MovieSceneSequenceExtensions.get_display_rate(sequence: MovieSceneSequence) -> FrameRate
unreal.MovieSceneSequenceExtensions.get_evaluation_type(sequence: MovieSceneSequence) -> MovieSceneEvaluationType
unreal.MovieSceneSequenceExtensions.get_marked_frames(sequence: MovieSceneSequence) -> Array[MovieSceneMarkedFrame]
unreal.MovieSceneSequenceExtensions.get_marked_frames_from_sequence(sequence: MovieSceneSequence, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> Array[MovieSceneMarkedFrame]
unreal.MovieSceneSequenceExtensions.get_movie_scene(sequence: MovieSceneSequence) -> MovieScene
unreal.MovieSceneSequenceExtensions.get_playback_end(sequence: MovieSceneSequence) -> int
unreal.MovieSceneSequenceExtensions.get_playback_end_seconds(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.get_playback_range(sequence: MovieSceneSequence) -> SequencerScriptingRange
unreal.MovieSceneSequenceExtensions.get_playback_start(sequence: MovieSceneSequence) -> int
unreal.MovieSceneSequenceExtensions.get_playback_start_seconds(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.get_portable_binding_id(root_sequence: MovieSceneSequence, destination_sequence: MovieSceneSequence, binding: MovieSceneBindingProxy) -> MovieSceneObjectBindingID
unreal.MovieSceneSequenceExtensions.get_possessables(sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequenceExtensions.get_root_folders_in_sequence(sequence: MovieSceneSequence) -> Array[MovieSceneFolder]
unreal.MovieSceneSequenceExtensions.get_spawnables(sequence: MovieSceneSequence) -> Array[MovieSceneBindingProxy]
unreal.MovieSceneSequenceExtensions.get_tick_resolution(sequence: MovieSceneSequence) -> FrameRate
unreal.MovieSceneSequenceExtensions.get_tracks(sequence: MovieSceneSequence) -> Array[MovieSceneTrack]
unreal.MovieSceneSequenceExtensions.get_view_range_end(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.get_view_range_start(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.get_work_range_end(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.get_work_range_start(sequence: MovieSceneSequence) -> float
unreal.MovieSceneSequenceExtensions.is_playback_range_locked(sequence: MovieSceneSequence) -> bool
unreal.MovieSceneSequenceExtensions.is_read_only(sequence: MovieSceneSequence) -> bool
unreal.MovieSceneSequenceExtensions.locate_bound_objects(sequence: MovieSceneSequence, binding: MovieSceneBindingProxy, context: Object) -> Array[Object]
unreal.MovieSceneSequenceExtensions.make_range(sequence: MovieSceneSequence, start_frame: int, duration: int) -> SequencerScriptingRange
unreal.MovieSceneSequenceExtensions.make_range_seconds(sequence: MovieSceneSequence, start_time: float, duration: float) -> SequencerScriptingRange
unreal.MovieSceneSequenceExtensions.remove_root_folder_from_sequence(sequence: MovieSceneSequence, folder: MovieSceneFolder) -> None
unreal.MovieSceneSequenceExtensions.remove_track(sequence: MovieSceneSequence, track: MovieSceneTrack) -> bool
unreal.MovieSceneSequenceExtensions.resolve_binding_id(root_sequence: MovieSceneSequence, object_binding_id: MovieSceneObjectBindingID) -> MovieSceneBindingProxy
unreal.MovieSceneSequenceExtensions.set_clock_source(sequence: MovieSceneSequence, clock_source: UpdateClockSource) -> None
unreal.MovieSceneSequenceExtensions.set_display_rate(sequence: MovieSceneSequence, display_rate: FrameRate) -> None
unreal.MovieSceneSequenceExtensions.set_evaluation_type(sequence: MovieSceneSequence, evaluation_type: MovieSceneEvaluationType) -> None
unreal.MovieSceneSequenceExtensions.set_marked_frame(sequence: MovieSceneSequence, mark_index: int, frame_number: FrameNumber) -> None
unreal.MovieSceneSequenceExtensions.set_marked_frame_in_sequence(sequence: MovieSceneSequence, mark_index: int, frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> None
unreal.MovieSceneSequenceExtensions.set_marked_frames_locked(sequence: MovieSceneSequence, locked: bool) -> None
unreal.MovieSceneSequenceExtensions.set_playback_end(sequence: MovieSceneSequence, end_frame: int) -> None
unreal.MovieSceneSequenceExtensions.set_playback_end_seconds(sequence: MovieSceneSequence, end_time: float) -> None
unreal.MovieSceneSequenceExtensions.set_playback_range_locked(sequence: MovieSceneSequence, locked: bool) -> None
unreal.MovieSceneSequenceExtensions.set_playback_start(sequence: MovieSceneSequence, start_frame: int) -> None
unreal.MovieSceneSequenceExtensions.set_playback_start_seconds(sequence: MovieSceneSequence, start_time: float) -> None
unreal.MovieSceneSequenceExtensions.set_read_only(sequence: MovieSceneSequence, read_only: bool) -> None
unreal.MovieSceneSequenceExtensions.set_tick_resolution(sequence: MovieSceneSequence, tick_resolution: FrameRate) -> None
unreal.MovieSceneSequenceExtensions.set_tick_resolution_directly(sequence: MovieSceneSequence, tick_resolution: FrameRate) -> None
unreal.MovieSceneSequenceExtensions.set_view_range_end(sequence: MovieSceneSequence, end_time_in_seconds: float) -> None
unreal.MovieSceneSequenceExtensions.set_view_range_start(sequence: MovieSceneSequence, start_time_in_seconds: float) -> None
unreal.MovieSceneSequenceExtensions.set_work_range_end(sequence: MovieSceneSequence, end_time_in_seconds: float) -> None
unreal.MovieSceneSequenceExtensions.set_work_range_start(sequence: MovieSceneSequence, start_time_in_seconds: float) -> None
unreal.MovieSceneSequenceExtensions.sort_marked_frames(sequence: MovieSceneSequence) -> None
```

## `unreal.MovieSceneSequenceLoopCount(StructBase)`

```python
unreal.MovieSceneSequenceLoopCount.__init__(value: int = 0) -> None
unreal.MovieSceneSequenceLoopCount.value(value: int) -> None
```

## `unreal.MovieSceneSequencePlayToParams(StructBase)`

```python
unreal.MovieSceneSequencePlayToParams.__init__(exclusive: bool = False) -> None
unreal.MovieSceneSequencePlayToParams.exclusive(value: bool) -> None
```

## `unreal.MovieSceneSequencePlaybackParams(StructBase)`

```python
unreal.MovieSceneSequencePlaybackParams.__init__(frame: FrameTime = [[0], 0.000000], time: float = 0.000000, marked_frame: str = "", timecode: Timecode = [0, 0, 0, 0, 0.000000, False], position_type: MovieScenePositionType = MovieScenePositionType.FRAME, update_method: UpdatePositionMethod = UpdatePositionMethod.PLAY, has_jumped: bool = False) -> None
unreal.MovieSceneSequencePlaybackParams.frame(value: FrameTime) -> None
unreal.MovieSceneSequencePlaybackParams.has_jumped(value: bool) -> None
unreal.MovieSceneSequencePlaybackParams.marked_frame(value: str) -> None
unreal.MovieSceneSequencePlaybackParams.position_type(value: MovieScenePositionType) -> None
unreal.MovieSceneSequencePlaybackParams.time(value: float) -> None
unreal.MovieSceneSequencePlaybackParams.timecode(value: Timecode) -> None
unreal.MovieSceneSequencePlaybackParams.update_method(value: UpdatePositionMethod) -> None
```

## `unreal.MovieSceneSequencePlaybackSettings(StructBase)`

```python
unreal.MovieSceneSequencePlaybackSettings.__init__(auto_play: bool = False, loop_count: MovieSceneSequenceLoopCount = [0], tick_interval: MovieSceneSequenceTickInterval = [0.000000, 0.000000, False, True], play_rate: float = 0.000000, start_time: float = 0.000000, random_start_time: bool = False, disable_movement_input: bool = False, disable_look_at_input: bool = False, hide_player: bool = False, hide_hud: bool = False, disable_camera_cuts: bool = False, finish_completion_state_override: MovieSceneCompletionModeOverride = MovieSceneCompletionModeOverride.NONE, pause_at_end: bool = False) -> None
unreal.MovieSceneSequencePlaybackSettings.auto_play(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.disable_camera_cuts(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.disable_look_at_input(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.disable_movement_input(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.finish_completion_state_override(value: MovieSceneCompletionModeOverride) -> None
unreal.MovieSceneSequencePlaybackSettings.hide_hud(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.hide_player(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.loop_count(value: MovieSceneSequenceLoopCount) -> None
unreal.MovieSceneSequencePlaybackSettings.pause_at_end(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.play_rate(value: float) -> None
unreal.MovieSceneSequencePlaybackSettings.random_start_time(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.restore_state(value: bool) -> None
unreal.MovieSceneSequencePlaybackSettings.start_time(value: float) -> None
unreal.MovieSceneSequencePlaybackSettings.tick_interval(value: MovieSceneSequenceTickInterval) -> None
```

## `unreal.MovieSceneSequencePlayer(Object)`

```python
unreal.MovieSceneSequencePlayer.change_playback_direction() -> None
unreal.MovieSceneSequencePlayer.get_bound_objects(object_binding: MovieSceneObjectBindingID) -> Array[Object]
unreal.MovieSceneSequencePlayer.get_completion_mode_override() -> MovieSceneCompletionModeOverride
unreal.MovieSceneSequencePlayer.get_current_time() -> QualifiedTime
unreal.MovieSceneSequencePlayer.get_disable_camera_cuts() -> bool
unreal.MovieSceneSequencePlayer.get_duration() -> QualifiedTime
unreal.MovieSceneSequencePlayer.get_end_time() -> QualifiedTime
unreal.MovieSceneSequencePlayer.get_frame_duration() -> int
unreal.MovieSceneSequencePlayer.get_frame_rate() -> FrameRate
unreal.MovieSceneSequencePlayer.get_hide_hud() -> bool
unreal.MovieSceneSequencePlayer.get_object_bindings(object: Object) -> Array[MovieSceneObjectBindingID]
unreal.MovieSceneSequencePlayer.get_play_rate() -> float
unreal.MovieSceneSequencePlayer.get_sequence() -> MovieSceneSequence
unreal.MovieSceneSequencePlayer.get_sequence_name(add_client_info: bool = False) -> str
unreal.MovieSceneSequencePlayer.get_start_time() -> QualifiedTime
unreal.MovieSceneSequencePlayer.go_to_end_and_stop() -> None
unreal.MovieSceneSequencePlayer.is_paused() -> bool
unreal.MovieSceneSequencePlayer.is_playing() -> bool
unreal.MovieSceneSequencePlayer.is_reversed() -> bool
unreal.MovieSceneSequencePlayer.on_finished(value: OnMovieSceneSequencePlayerEvent) -> None
unreal.MovieSceneSequencePlayer.on_pause(value: OnMovieSceneSequencePlayerEvent) -> None
unreal.MovieSceneSequencePlayer.on_play(value: OnMovieSceneSequencePlayerEvent) -> None
unreal.MovieSceneSequencePlayer.on_play_reverse(value: OnMovieSceneSequencePlayerEvent) -> None
unreal.MovieSceneSequencePlayer.on_stop(value: OnMovieSceneSequencePlayerEvent) -> None
unreal.MovieSceneSequencePlayer.pause() -> None
unreal.MovieSceneSequencePlayer.play() -> None
unreal.MovieSceneSequencePlayer.play_looping(num_loops: int = -1) -> None
unreal.MovieSceneSequencePlayer.play_reverse() -> None
unreal.MovieSceneSequencePlayer.play_to(playback_params: MovieSceneSequencePlaybackParams, play_to_params: MovieSceneSequencePlayToParams) -> None
unreal.MovieSceneSequencePlayer.remove_weight() -> None
unreal.MovieSceneSequencePlayer.request_invalidate_binding(object_binding: MovieSceneObjectBindingID) -> None
unreal.MovieSceneSequencePlayer.restore_state() -> None
unreal.MovieSceneSequencePlayer.scrub() -> None
unreal.MovieSceneSequencePlayer.set_completion_mode_override(completion_mode_override: MovieSceneCompletionModeOverride) -> None
unreal.MovieSceneSequencePlayer.set_disable_camera_cuts(disable_camera_cuts: bool) -> None
unreal.MovieSceneSequencePlayer.set_frame_range(start_frame: int, duration: int, sub_frames: float = 0.000000) -> None
unreal.MovieSceneSequencePlayer.set_frame_rate(frame_rate: FrameRate) -> None
unreal.MovieSceneSequencePlayer.set_hide_hud(hide_hud: bool) -> None
unreal.MovieSceneSequencePlayer.set_play_rate(play_rate: float) -> None
unreal.MovieSceneSequencePlayer.set_playback_position(playback_params: MovieSceneSequencePlaybackParams) -> None
unreal.MovieSceneSequencePlayer.set_time_range(start_time: float, duration: float) -> None
unreal.MovieSceneSequencePlayer.set_weight(weight: float) -> None
unreal.MovieSceneSequencePlayer.stop() -> None
unreal.MovieSceneSequencePlayer.stop_at_current_time() -> None
```

## `unreal.MovieSceneSequenceTickInterval(StructBase)`

```python
unreal.MovieSceneSequenceTickInterval.__init__(tick_interval_seconds: float = 0.000000, evaluation_budget_microseconds: float = 0.000000, tick_when_paused: bool = False, allow_rounding: bool = False) -> None
unreal.MovieSceneSequenceTickInterval.allow_rounding(value: bool) -> None
unreal.MovieSceneSequenceTickInterval.evaluation_budget_microseconds(value: float) -> None
unreal.MovieSceneSequenceTickInterval.tick_interval_seconds(value: float) -> None
unreal.MovieSceneSequenceTickInterval.tick_when_paused(value: bool) -> None
```

## `unreal.MovieSceneSpawnableBindingBase(MovieSceneCustomBinding)`

```python
unreal.MovieSceneSpawnableBindingBase.continuously_respawn(value: bool) -> None
unreal.MovieSceneSpawnableBindingBase.spawn_ownership(value: SpawnOwnership) -> None
```

## `unreal.MovieSceneSubSection(MovieSceneSection)`

```python
unreal.MovieSceneSubSection.get_parent_sequence_frame(frame: int, parent_sequence: MovieSceneSequence) -> int
unreal.MovieSceneSubSection.get_sequence() -> MovieSceneSequence
unreal.MovieSceneSubSection.parameters(value: MovieSceneSectionParameters) -> None
unreal.MovieSceneSubSection.set_sequence(sequence: MovieSceneSequence) -> None
```

## `unreal.MovieSceneTakeSettings(Object)`

```python
unreal.MovieSceneTakeSettings.frames_name(value: str) -> None
unreal.MovieSceneTakeSettings.hours_name(value: str) -> None
unreal.MovieSceneTakeSettings.minutes_name(value: str) -> None
unreal.MovieSceneTakeSettings.rate_name(value: str) -> None
unreal.MovieSceneTakeSettings.seconds_name(value: str) -> None
unreal.MovieSceneTakeSettings.slate_name(value: str) -> None
unreal.MovieSceneTakeSettings.sub_frames_name(value: str) -> None
```

## `unreal.MovieSceneTimeWarpExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneTimeWarpExtensions.break_time_warp(time_warp: MovieSceneTimeWarpVariant) -> float
unreal.MovieSceneTimeWarpExtensions.conv_play_rate_to_time_warp_variant(constant_play_rate: float) -> MovieSceneTimeWarpVariant
unreal.MovieSceneTimeWarpExtensions.conv_time_warp_variant_to_play_rate(time_warp: MovieSceneTimeWarpVariant) -> float
unreal.MovieSceneTimeWarpExtensions.make_time_warp(fixed_play_rate: float) -> MovieSceneTimeWarpVariant
unreal.MovieSceneTimeWarpExtensions.set_fixed_play_rate(time_warp: MovieSceneTimeWarpVariant, fixed_play_rate: float) -> MovieSceneTimeWarpVariant
unreal.MovieSceneTimeWarpExtensions.to_fixed_play_rate(time_warp: MovieSceneTimeWarpVariant) -> float
```

## `unreal.MovieSceneTimeWarpVariant(StructBase)`

```python
unreal.MovieSceneTimeWarpVariant.__init__(fixed_play_rate: float = 0.000000) -> None
unreal.MovieSceneTimeWarpVariant.set_fixed_play_rate(fixed_play_rate: float) -> None
unreal.MovieSceneTimeWarpVariant.to_fixed_play_rate() -> float
```

## `unreal.MovieSceneTimecodeSource(StructBase)`

```python
unreal.MovieSceneTimecodeSource.__init__(timecode: Timecode = [0, 0, 0, 0, 0.000000, False]) -> None
unreal.MovieSceneTimecodeSource.timecode() -> Timecode
```

## `unreal.MovieSceneTrack(MovieSceneSignedObject)`

```python
unreal.MovieSceneTrack.add_section() -> MovieSceneSection
unreal.MovieSceneTrack.get_color_tint() -> Color
unreal.MovieSceneTrack.get_display_name() -> Text
unreal.MovieSceneTrack.get_section_to_key() -> MovieSceneSection
unreal.MovieSceneTrack.get_sections() -> Array[MovieSceneSection]
unreal.MovieSceneTrack.get_sorting_order() -> int
unreal.MovieSceneTrack.get_track_row_display_name(row_index: int) -> Text
unreal.MovieSceneTrack.remove_section(section: MovieSceneSection) -> None
unreal.MovieSceneTrack.set_color_tint(color_tint: Color) -> None
unreal.MovieSceneTrack.set_display_name(name: Text) -> None
unreal.MovieSceneTrack.set_section_to_key(section: MovieSceneSection) -> None
unreal.MovieSceneTrack.set_sorting_order(sorting_order: int) -> None
unreal.MovieSceneTrack.set_track_row_display_name(name: Text, row_index: int) -> None
```

## `unreal.MovieSceneTrackDisplayOptions(StructBase)`

```python
unreal.MovieSceneTrackDisplayOptions.__init__() -> None
```

## `unreal.MovieSceneTrackEvalOptions(StructBase)`

```python
unreal.MovieSceneTrackEvalOptions.__init__() -> None
```

## `unreal.MovieSceneTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneTrackExtensions.add_section(track: MovieSceneTrack) -> MovieSceneSection
unreal.MovieSceneTrackExtensions.get_color_tint(track: MovieSceneTrack) -> Color
unreal.MovieSceneTrackExtensions.get_display_name(track: MovieSceneTrack) -> Text
unreal.MovieSceneTrackExtensions.get_section_to_key(track: MovieSceneTrack) -> MovieSceneSection
unreal.MovieSceneTrackExtensions.get_sections(track: MovieSceneTrack) -> Array[MovieSceneSection]
unreal.MovieSceneTrackExtensions.get_sorting_order(track: MovieSceneTrack) -> int
unreal.MovieSceneTrackExtensions.get_track_row_display_name(track: MovieSceneTrack, row_index: int) -> Text
unreal.MovieSceneTrackExtensions.remove_section(track: MovieSceneTrack, section: MovieSceneSection) -> None
unreal.MovieSceneTrackExtensions.set_color_tint(track: MovieSceneTrack, color_tint: Color) -> None
unreal.MovieSceneTrackExtensions.set_display_name(track: MovieSceneTrack, name: Text) -> None
unreal.MovieSceneTrackExtensions.set_section_to_key(track: MovieSceneTrack, section: MovieSceneSection) -> None
unreal.MovieSceneTrackExtensions.set_sorting_order(track: MovieSceneTrack, sorting_order: int) -> None
unreal.MovieSceneTrackExtensions.set_track_row_display_name(track: MovieSceneTrack, name: Text, row_index: int) -> None
```

## `unreal.OnMovieSceneSequencePlayerEvent(MulticastDelegateBase)`

```python
unreal.OnMovieSceneSequencePlayerEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OptionalMovieSceneBlendType(StructBase)`

```python
unreal.OptionalMovieSceneBlendType.__init__(blend_type: MovieSceneBlendType = 0, is_valid: bool = False) -> None
unreal.OptionalMovieSceneBlendType.blend_type() -> MovieSceneBlendType
unreal.OptionalMovieSceneBlendType.is_valid() -> bool
```

## `unreal.SequenceRecorderLibrary(BlueprintFunctionLibrary)`

```python
unreal.SequenceRecorderLibrary.is_recording_sequence() -> bool
unreal.SequenceRecorderLibrary.start_recording_sequence(actors_to_record: Array[Actor]) -> None
unreal.SequenceRecorderLibrary.stop_recording_sequence() -> None
```

## `unreal.SequencerBindingProxy(MovieSceneBindingProxy)`

```python
unreal.SequencerBindingProxy.__init__(binding_id: Guid = [], sequence: MovieSceneSequence = None) -> None
```

## `unreal.SequencerBoundObjects(StructBase)`

```python
unreal.SequencerBoundObjects.__init__(binding_proxy: MovieSceneBindingProxy = [[], None], bound_objects: Array[Object] = []) -> None
unreal.SequencerBoundObjects.binding_proxy(value: MovieSceneBindingProxy) -> None
unreal.SequencerBoundObjects.bound_objects(value: Array[Object]) -> None
```

## `unreal.SequencerChannelProxy(StructBase)`

```python
unreal.SequencerChannelProxy.__init__(channel_name: Name = "None", section: MovieSceneSection = None) -> None
unreal.SequencerChannelProxy.channel_name(value: Name) -> None
unreal.SequencerChannelProxy.section(value: MovieSceneSection) -> None
```

## `unreal.SequencerExportFBXParams(StructBase)`

```python
unreal.SequencerExportFBXParams.__init__(world: World = None, sequence: LevelSequence = None, root_sequence: LevelSequence = None, bindings: Array[MovieSceneBindingProxy] = [], tracks: Array[MovieSceneTrack] = [], override_options: FbxExportOption = None, fbx_file_name: str = "") -> None
unreal.SequencerExportFBXParams.bindings(value: Array[MovieSceneBindingProxy]) -> None
unreal.SequencerExportFBXParams.fbx_file_name(value: str) -> None
unreal.SequencerExportFBXParams.override_options(value: FbxExportOption) -> None
unreal.SequencerExportFBXParams.root_sequence(value: LevelSequence) -> None
unreal.SequencerExportFBXParams.sequence(value: LevelSequence) -> None
unreal.SequencerExportFBXParams.tracks(value: Array[MovieSceneTrack]) -> None
unreal.SequencerExportFBXParams.world(value: World) -> None
```

## `unreal.SequencerExportTask(AssetExportTask)`

```python
unreal.SequencerExportTask.sequencer_context(value: Object) -> None
```

## `unreal.SequencerModuleOutlinerScriptingObject(SequencerOutlinerScriptingObject)`

```python
unreal.SequencerModuleOutlinerScriptingObject.get_next_key(nodes: Array[SequencerViewModelScriptingStruct], frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameNumber
unreal.SequencerModuleOutlinerScriptingObject.get_previous_key(nodes: Array[SequencerViewModelScriptingStruct], frame_number: FrameNumber, time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE) -> FrameNumber
```

## `unreal.SequencerModuleScriptingLayer(SequencerScriptingLayer)`

```python
unreal.SequencerModuleScriptingLayer.get_outliner() -> SequencerModuleOutlinerScriptingObject
```

## `unreal.SequencerOutlinerScriptingObject(Object)`

```python
unreal.SequencerOutlinerScriptingObject.get_children(node: SequencerViewModelScriptingStruct, type_name: Name = "None") -> Array[SequencerViewModelScriptingStruct]
unreal.SequencerOutlinerScriptingObject.get_root_node() -> SequencerViewModelScriptingStruct
unreal.SequencerOutlinerScriptingObject.get_selection() -> Array[SequencerViewModelScriptingStruct]
unreal.SequencerOutlinerScriptingObject.on_selection_changed(value: SequencerOutlinerSelectionChanged) -> None
unreal.SequencerOutlinerScriptingObject.set_selection(selection: Array[SequencerViewModelScriptingStruct]) -> None
```

## `unreal.SequencerOutlinerSelectionChanged(MulticastDelegateBase)`

```python
unreal.SequencerOutlinerSelectionChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.SequencerQuickBindingResult(StructBase)`

```python
unreal.SequencerQuickBindingResult.__init__(payload_names: Array[str] = []) -> None
unreal.SequencerQuickBindingResult.payload_names() -> Array[str]
```

## `unreal.SequencerScriptingLayer(Object)`

```python
unreal.SequencerScriptingLayer.outliner() -> SequencerOutlinerScriptingObject
```

## `unreal.SequencerScriptingRange(StructBase)`

```python
unreal.SequencerScriptingRange.__init__(has_start_value: bool = False, has_end_value: bool = False, inclusive_start: int = 0, exclusive_end: int = 0) -> None
unreal.SequencerScriptingRange.exclusive_end(value: int) -> None
unreal.SequencerScriptingRange.get_end_frame() -> int
unreal.SequencerScriptingRange.get_end_seconds() -> float
unreal.SequencerScriptingRange.get_start_frame() -> int
unreal.SequencerScriptingRange.get_start_seconds() -> float
unreal.SequencerScriptingRange.has_end() -> bool
unreal.SequencerScriptingRange.has_end_value(value: bool) -> None
unreal.SequencerScriptingRange.has_start() -> bool
unreal.SequencerScriptingRange.has_start_value(value: bool) -> None
unreal.SequencerScriptingRange.inclusive_start(value: int) -> None
unreal.SequencerScriptingRange.remove_end() -> None
unreal.SequencerScriptingRange.remove_start() -> None
unreal.SequencerScriptingRange.set_end_frame(end: int) -> None
unreal.SequencerScriptingRange.set_end_seconds(end: float) -> None
unreal.SequencerScriptingRange.set_start_frame(start: int) -> None
unreal.SequencerScriptingRange.set_start_seconds(start: float) -> None
```

## `unreal.SequencerScriptingRangeExtensions(BlueprintFunctionLibrary)`

```python
unreal.SequencerScriptingRangeExtensions.get_end_frame(range: SequencerScriptingRange) -> int
unreal.SequencerScriptingRangeExtensions.get_end_seconds(range: SequencerScriptingRange) -> float
unreal.SequencerScriptingRangeExtensions.get_start_frame(range: SequencerScriptingRange) -> int
unreal.SequencerScriptingRangeExtensions.get_start_seconds(range: SequencerScriptingRange) -> float
unreal.SequencerScriptingRangeExtensions.has_end(range: SequencerScriptingRange) -> bool
unreal.SequencerScriptingRangeExtensions.has_start(range: SequencerScriptingRange) -> bool
unreal.SequencerScriptingRangeExtensions.remove_end(range: SequencerScriptingRange) -> SequencerScriptingRange
unreal.SequencerScriptingRangeExtensions.remove_start(range: SequencerScriptingRange) -> SequencerScriptingRange
unreal.SequencerScriptingRangeExtensions.set_end_frame(range: SequencerScriptingRange, end: int) -> SequencerScriptingRange
unreal.SequencerScriptingRangeExtensions.set_end_seconds(range: SequencerScriptingRange, end: float) -> SequencerScriptingRange
unreal.SequencerScriptingRangeExtensions.set_start_frame(range: SequencerScriptingRange, start: int) -> SequencerScriptingRange
unreal.SequencerScriptingRangeExtensions.set_start_seconds(range: SequencerScriptingRange, start: float) -> SequencerScriptingRange
```

## `unreal.SequencerTools(BlueprintFunctionLibrary)`

```python
unreal.SequencerTools.cancel_movie_render() -> None
unreal.SequencerTools.clear_linked_anim_sequences(level_sequence: LevelSequence) -> None
unreal.SequencerTools.create_event(sequence: MovieSceneSequence, section: MovieSceneEventSectionBase, endpoint: SequencerQuickBindingResult, payload: Array[str]) -> MovieSceneEvent
unreal.SequencerTools.create_quick_binding(sequence: MovieSceneSequence, object: Object, function_name: str, call_in_editor: bool) -> SequencerQuickBindingResult
unreal.SequencerTools.export_anim_sequence(world: World, sequence: LevelSequence, anim_sequence: AnimSequence, export_option: AnimSeqExportOption, binding: MovieSceneBindingProxy, create_link: bool) -> bool
unreal.SequencerTools.export_fbx_from_control_rig(sequence: LevelSequence, actor_with_control_rig_track: str, export_fbx_control_rig_settings: MovieSceneUserExportFBXControlRigSettings) -> bool
unreal.SequencerTools.export_level_sequence_fbx(params: SequencerExportFBXParams) -> bool
unreal.SequencerTools.get_anim_sequence_link_from_level_sequence(level_sequence: LevelSequence) -> LevelSequenceAnimSequenceLink
unreal.SequencerTools.get_bound_objects(world: World, sequence: LevelSequence, bindings: Array[MovieSceneBindingProxy], range: SequencerScriptingRange) -> Array[SequencerBoundObjects]
unreal.SequencerTools.get_level_sequence_link_from_anim_sequence(anim_sequence: AnimSequence) -> AnimSequenceLevelSequenceLink
unreal.SequencerTools.get_object_bindings(world: World, sequence: LevelSequence, object: Array[Object], range: SequencerScriptingRange) -> Array[SequencerBoundObjects]
unreal.SequencerTools.import_fbx_to_control_rig(world: World, sequence: LevelSequence, actor_with_control_rig_track: str, selected_control_rig_names: Array[str], import_fbx_control_rig_settings: MovieSceneUserImportFBXControlRigSettings, import_filename: str) -> bool
unreal.SequencerTools.import_level_sequence_fbx(world: World, sequence: LevelSequence, bindings: Array[MovieSceneBindingProxy], import_fbx_settings: MovieSceneUserImportFBXSettings, import_filename: str) -> bool
unreal.SequencerTools.is_event_endpoint_valid(endpoint: SequencerQuickBindingResult) -> bool
unreal.SequencerTools.is_rendering_movie() -> bool
unreal.SequencerTools.link_anim_sequence(sequence: LevelSequence, anim_sequence: AnimSequence, export_options: AnimSeqExportOption, binding: MovieSceneBindingProxy) -> bool
unreal.SequencerTools.render_movie(capture_settings: MovieSceneCapture, on_finished_callback: OnRenderMovieStopped) -> bool
```

## `unreal.SequencerViewModelScriptingStruct(StructBase)`

```python
unreal.SequencerViewModelScriptingStruct.__init__(type: Name = "None") -> None
unreal.SequencerViewModelScriptingStruct.get_label() -> str
unreal.SequencerViewModelScriptingStruct.get_path() -> str
unreal.SequencerViewModelScriptingStruct.type() -> Name
```

## `unreal.SequencerViewModelStructExtensions(BlueprintFunctionLibrary)`

```python
unreal.SequencerViewModelStructExtensions.get_label(view_model: SequencerViewModelScriptingStruct) -> str
unreal.SequencerViewModelStructExtensions.get_path(view_model: SequencerViewModelScriptingStruct) -> str
```

