# Unreal Python API — Editor Tools

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AISenseConfig(Object)`

```python
unreal.AISenseConfig.debug_color() -> Color
unreal.AISenseConfig.max_age() -> float
unreal.AISenseConfig.starts_enabled() -> bool
```

## `unreal.AISenseConfig_Hearing(AISenseConfig)`

```python
unreal.AISenseConfig_Hearing.detection_by_affiliation() -> AISenseAffiliationFilter
unreal.AISenseConfig_Hearing.hearing_range() -> float
unreal.AISenseConfig_Hearing.implementation() -> Class
unreal.AISenseConfig_Hearing.lo_s_hearing_range() -> float
```

## `unreal.AISenseConfig_Sight(AISenseConfig)`

```python
unreal.AISenseConfig_Sight.auto_success_range_from_last_seen_location() -> float
unreal.AISenseConfig_Sight.detection_by_affiliation() -> AISenseAffiliationFilter
unreal.AISenseConfig_Sight.implementation() -> Class
unreal.AISenseConfig_Sight.lose_sight_radius() -> float
unreal.AISenseConfig_Sight.near_clipping_radius() -> float
unreal.AISenseConfig_Sight.peripheral_vision_angle_degrees() -> float
unreal.AISenseConfig_Sight.point_of_view_backward_offset() -> float
unreal.AISenseConfig_Sight.sight_radius() -> float
```

## `unreal.AISenseConfig_Touch(AISenseConfig)`

```python
unreal.AISenseConfig_Touch.detection_by_affiliation() -> AISenseAffiliationFilter
```

## `unreal.AbcCompressionSettings(StructBase)`

```python
unreal.AbcCompressionSettings.__init__(merge_meshes: bool = False, bake_matrix_animation: bool = False, base_calculation_type: BaseCalculationType = 0, percentage_of_total_bases: float = 0.000000, max_number_of_bases: int = 0, minimum_number_of_vertex_influence_percentage: float = 0.000000) -> None
unreal.AbcCompressionSettings.bake_matrix_animation(value: bool) -> None
unreal.AbcCompressionSettings.base_calculation_type(value: BaseCalculationType) -> None
unreal.AbcCompressionSettings.max_number_of_bases(value: int) -> None
unreal.AbcCompressionSettings.merge_meshes(value: bool) -> None
unreal.AbcCompressionSettings.minimum_number_of_vertex_influence_percentage(value: float) -> None
unreal.AbcCompressionSettings.percentage_of_total_bases(value: float) -> None
```

## `unreal.AbcConversionSettings(StructBase)`

```python
unreal.AbcConversionSettings.__init__(preset: AbcConversionPreset = AbcConversionPreset.MAYA, flip_u: bool = False, flip_v: bool = False, scale: Vector = [0.000000, 0.000000, 0.000000], rotation: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.AbcConversionSettings.flip_u(value: bool) -> None
unreal.AbcConversionSettings.flip_v(value: bool) -> None
unreal.AbcConversionSettings.preset(value: AbcConversionPreset) -> None
unreal.AbcConversionSettings.rotation(value: Vector) -> None
unreal.AbcConversionSettings.scale(value: Vector) -> None
```

## `unreal.AbcImportSettings(Object)`

```python
unreal.AbcImportSettings.compression_settings(value: AbcCompressionSettings) -> None
unreal.AbcImportSettings.conversion_settings(value: AbcConversionSettings) -> None
unreal.AbcImportSettings.geometry_cache_settings(value: AbcGeometryCacheSettings) -> None
unreal.AbcImportSettings.import_type(value: AlembicImportType) -> None
unreal.AbcImportSettings.material_settings(value: AbcMaterialSettings) -> None
unreal.AbcImportSettings.normal_generation_settings(value: AbcNormalGenerationSettings) -> None
unreal.AbcImportSettings.sampling_settings(value: AbcSamplingSettings) -> None
unreal.AbcImportSettings.static_mesh_settings(value: AbcStaticMeshSettings) -> None
```

## `unreal.AbcNormalGenerationSettings(StructBase)`

```python
unreal.AbcNormalGenerationSettings.__init__(force_one_smoothing_group_per_object: bool = False, hard_edge_angle_threshold: float = 0.000000, recompute_normals: bool = False, ignore_degenerate_triangles: bool = False, skip_computing_tangents: bool = False) -> None
unreal.AbcNormalGenerationSettings.force_one_smoothing_group_per_object(value: bool) -> None
unreal.AbcNormalGenerationSettings.hard_edge_angle_threshold(value: float) -> None
unreal.AbcNormalGenerationSettings.ignore_degenerate_triangles(value: bool) -> None
unreal.AbcNormalGenerationSettings.recompute_normals(value: bool) -> None
unreal.AbcNormalGenerationSettings.skip_computing_tangents(value: bool) -> None
```

## `unreal.AbcSamplingSettings(StructBase)`

```python
unreal.AbcSamplingSettings.__init__(sampling_type: AlembicSamplingType = AlembicSamplingType.PER_FRAME, frame_steps: int = 0, time_steps: float = 0.000000, frame_start: int = 0, frame_end: int = 0, skip_empty: bool = False) -> None
unreal.AbcSamplingSettings.frame_end(value: int) -> None
unreal.AbcSamplingSettings.frame_start(value: int) -> None
unreal.AbcSamplingSettings.frame_steps(value: int) -> None
unreal.AbcSamplingSettings.sampling_type(value: AlembicSamplingType) -> None
unreal.AbcSamplingSettings.skip_empty(value: bool) -> None
unreal.AbcSamplingSettings.time_steps(value: float) -> None
```

## `unreal.AesAssetSettings(DeveloperSettings)`

```python
unreal.AesAssetSettings.region_libraries(value: Array[AesAssetRegionLibrary]) -> None
unreal.AesAssetSettings.summary_library(value: SoftObjectPath) -> None
```

## `unreal.AesEditorCommand(Object)`

```python
unreal.AesEditorCommand.execute() -> bool
unreal.AesEditorCommand.finish() -> bool
unreal.AesEditorCommand.get_command_params() -> AesEditorPropertyProvider
unreal.AesEditorCommand.set_extra_data(extra_data: str) -> None
unreal.AesEditorCommand.set_frozen(frozen: bool) -> None
unreal.AesEditorCommand.set_mouse_position(mouse_position: Vector2D) -> None
unreal.AesEditorCommand.set_nick_name(nick_name: str) -> None
unreal.AesEditorCommand.set_param_key(param_key: str) -> None
```

## `unreal.AesEditorDataInfo(StructBase)`

```python
unreal.AesEditorDataInfo.__init__() -> None
```

## `unreal.AesEditorDefaultMessage(StructBase)`

```python
unreal.AesEditorDefaultMessage.__init__() -> None
```

## `unreal.AesEditorEntitiesRemoveMessage(StructBase)`

```python
unreal.AesEditorEntitiesRemoveMessage.__init__(layer_name: Name = "None", entity_ids: Array[int] = []) -> None
unreal.AesEditorEntitiesRemoveMessage.entity_ids(value: Array[int]) -> None
unreal.AesEditorEntitiesRemoveMessage.layer_name(value: Name) -> None
```

## `unreal.AesEditorEntityAddMessage(StructBase)`

```python
unreal.AesEditorEntityAddMessage.__init__(entity_id: int = 0) -> None
unreal.AesEditorEntityAddMessage.entity_id(value: int) -> None
```

## `unreal.AesEditorModeMessage(StructBase)`

```python
unreal.AesEditorModeMessage.__init__() -> None
```

## `unreal.AesEditorModeSettings(DeveloperSettings)`

```python
unreal.AesEditorModeSettings.angle_snap_threshold() -> float
```

## `unreal.AesEditorModeSettingsLibrary(BlueprintFunctionLibrary)`

```python
unreal.AesEditorModeSettingsLibrary.get_camera_speed() -> int
unreal.AesEditorModeSettingsLibrary.get_camera_speed_scalar() -> float
unreal.AesEditorModeSettingsLibrary.get_camera_speed_zoom() -> float
unreal.AesEditorModeSettingsLibrary.set_camera_speed(camera_speed: int) -> None
unreal.AesEditorModeSettingsLibrary.set_camera_speed_scalar(camera_speed_scalar: float) -> None
unreal.AesEditorModeSettingsLibrary.set_camera_speed_zoom(camera_speed_zoom: float) -> None
```

## `unreal.AesEditorRoadModifyStyle(StructBase)`

```python
unreal.AesEditorRoadModifyStyle.__init__() -> None
```

## `unreal.AesEditorUIHideEvent(MulticastDelegateBase)`

```python
unreal.AesEditorUIHideEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AesEditorUISetting(DeveloperSettings)`

```python
unreal.AesEditorUISetting.main_ui_class(value: SoftClassPath) -> None
```

## `unreal.AesEditorUIShowEvent(MulticastDelegateBase)`

```python
unreal.AesEditorUIShowEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AesEditorVectorStyle(StructBase)`

```python
unreal.AesEditorVectorStyle.__init__() -> None
```

## `unreal.AesEntitySettings(DeveloperSettings)`

```python
unreal.AesEntitySettings.entity_library(value: SoftObjectPath) -> None
```

## `unreal.AssetEditorToolkitMenuContext(Object)`

```python
unreal.AssetEditorToolkitMenuContext.get_editing_objects() -> Array[Object]
```

## `unreal.AsyncEditorDelay(EditorUtilityBlueprintAsyncActionBase)`

```python
unreal.AsyncEditorDelay.complete(value: AsyncDelayComplete) -> None
```

## `unreal.AttenuationSettings(SoundAttenuationSettings)`

```python
unreal.AttenuationSettings.__init__(distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.LINEAR, attenuation_shape: AttenuationShape = AttenuationShape.SPHERE, falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES, d_b_attenuation_at_max: float = 0.000000, attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000], cone_offset: float = 0.000000, falloff_distance: float = 0.000000, cone_sphere_radius: float = 0.000000, cone_sphere_falloff_distance: float = 0.000000, custom_attenuation_curve: RuntimeFloatCurve = [], attenuate: bool = False, spatialize: bool = False, attenuate_with_lpf: bool = False, enable_listener_focus: bool = False, enable_focus_interpolation: bool = False, enable_occlusion: bool = False, use_complex_collision_for_occlusion: bool = False, enable_reverb_send: bool = False, enable_priority_attenuation: bool = False, apply_normalization_to_stereo_sounds: bool = False, enable_log_frequency_scaling: bool = False, enable_submix_sends: bool = False, enable_source_data_override: bool = False, enable_send_to_audio_link: bool = False, spatialization_algorithm: SoundSpatializationAlgorithm = SoundSpatializationAlgorithm.SPATIALIZATION_DEFAULT, audio_link_settings_override: AudioLinkSettingsAbstract = None, binaural_radius: float = 0.000000, custom_lowpass_air_absorption_curve: RuntimeFloatCurve = [], custom_highpass_air_absorption_curve: RuntimeFloatCurve = [], absorption_method: AirAbsorptionMethod = AirAbsorptionMethod.LINEAR, occlusion_trace_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, reverb_send_method: ReverbSendMethod = ReverbSendMethod.LINEAR, priority_attenuation_method: PriorityAttenuationMethod = PriorityAttenuationMethod.LINEAR, non_spatialized_radius_start: float = 0.000000, non_spatialized_radius_end: float = 0.000000, non_spatialized_radius_mode: NonSpatializedRadiusSpeakerMapMode = NonSpatializedRadiusSpeakerMapMode.OMNI_DIRECTIONAL, stereo_spread: float = 0.000000, lpf_radius_min: float = 0.000000, lpf_radius_max: float = 0.000000, lpf_frequency_at_min: float = 0.000000, lpf_frequency_at_max: float = 0.000000, hpf_frequency_at_min: float = 0.000000, hpf_frequency_at_max: float = 0.000000, focus_azimuth: float = 0.000000, non_focus_azimuth: float = 0.000000, focus_distance_scale: float = 0.000000, non_focus_distance_scale: float = 0.000000, focus_priority_scale: float = 0.000000, non_focus_priority_scale: float = 0.000000, focus_volume_attenuation: float = 0.000000, non_focus_volume_attenuation: float = 0.000000, focus_attack_interp_speed: float = 0.000000, focus_release_interp_speed: float = 0.000000, occlusion_low_pass_filter_frequency: float = 0.000000, occlusion_volume_attenuation: float = 0.000000, occlusion_interpolation_time: float = 0.000000, reverb_wet_level_min: float = 0.000000, reverb_wet_level_max: float = 0.000000, reverb_distance_min: float = 0.000000, reverb_distance_max: float = 0.000000, manual_reverb_send_level: float = 0.000000, priority_attenuation_min: float = 0.000000, priority_attenuation_max: float = 0.000000, priority_attenuation_distance_min: float = 0.000000, priority_attenuation_distance_max: float = 0.000000, manual_priority_attenuation: float = 0.000000, custom_reverb_send_curve: RuntimeFloatCurve = [], submix_send_settings: Array[AttenuationSubmixSendSettings] = [], custom_priority_attenuation_curve: RuntimeFloatCurve = [], plugin_settings: SoundAttenuationPluginSettings = [[], [], [], []]) -> None
```

## `unreal.AttenuationSubmixSendSettings(SoundSubmixSendInfoBase)`

```python
unreal.AttenuationSubmixSendSettings.__init__(send_level_control_method: SendLevelControlMethod = SendLevelControlMethod.LINEAR, sound_submix: SoundSubmixBase = None, send_level: float = 0.000000, disable_manual_send_clamp: bool = False, min_send_level: float = 0.000000, max_send_level: float = 0.000000, min_send_distance: float = 0.000000, max_send_distance: float = 0.000000, custom_send_level_curve: RuntimeFloatCurve = []) -> None
```

## `unreal.AutoMovementSettings(StructBase)`

```python
unreal.AutoMovementSettings.__init__(use_speed_mode: bool = False, move_direction: Vector = [0.000000, 0.000000, 0.000000], speed: float = 0.000000, move_duration: float = 0.000000, move_distance: float = 0.000000, auto_stop_when_user_input: bool = False) -> None
unreal.AutoMovementSettings.auto_stop_when_user_input(value: bool) -> None
unreal.AutoMovementSettings.move_direction(value: Vector) -> None
unreal.AutoMovementSettings.move_distance(value: float) -> None
unreal.AutoMovementSettings.move_duration(value: float) -> None
unreal.AutoMovementSettings.speed(value: float) -> None
unreal.AutoMovementSettings.use_speed_mode(value: bool) -> None
```

## `unreal.AutoRotationSettings(StructBase)`

```python
unreal.AutoRotationSettings.__init__(rotate_direction: AutoCameraRotateDirection = AutoCameraRotateDirection.ACR_AUTO, duration: float = 0.000000, loop_count: int = 0, auto_stop_when_user_input: bool = False, enable_zoom_input_when_rotate: bool = False) -> None
unreal.AutoRotationSettings.auto_stop_when_user_input(value: bool) -> None
unreal.AutoRotationSettings.duration(value: float) -> None
unreal.AutoRotationSettings.enable_zoom_input_when_rotate(value: bool) -> None
unreal.AutoRotationSettings.loop_count(value: int) -> None
unreal.AutoRotationSettings.rotate_direction(value: AutoCameraRotateDirection) -> None
```

## `unreal.AutoSelfRotationSettings(StructBase)`

```python
unreal.AutoSelfRotationSettings.__init__(use_speed_mode: bool = False, rotate_value: Vector2D = [0.000000, 0.000000], duration: float = 0.000000, auto_stop_when_user_input: bool = False) -> None
unreal.AutoSelfRotationSettings.auto_stop_when_user_input(value: bool) -> None
unreal.AutoSelfRotationSettings.duration(value: float) -> None
unreal.AutoSelfRotationSettings.rotate_value(value: Vector2D) -> None
unreal.AutoSelfRotationSettings.use_speed_mode(value: bool) -> None
```

## `unreal.AutomationEditorTask(Object)`

```python
unreal.AutomationEditorTask.is_task_done() -> bool
unreal.AutomationEditorTask.is_valid_task() -> bool
```

## `unreal.BaseAttenuationSettings(StructBase)`

```python
unreal.BaseAttenuationSettings.__init__(distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.LINEAR, attenuation_shape: AttenuationShape = AttenuationShape.SPHERE, falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES, d_b_attenuation_at_max: float = 0.000000, attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000], cone_offset: float = 0.000000, falloff_distance: float = 0.000000, cone_sphere_radius: float = 0.000000, cone_sphere_falloff_distance: float = 0.000000, custom_attenuation_curve: RuntimeFloatCurve = []) -> None
unreal.BaseAttenuationSettings.attenuation_shape(value: AttenuationShape) -> None
unreal.BaseAttenuationSettings.attenuation_shape_extents(value: Vector) -> None
unreal.BaseAttenuationSettings.cone_offset(value: float) -> None
unreal.BaseAttenuationSettings.cone_sphere_falloff_distance(value: float) -> None
unreal.BaseAttenuationSettings.cone_sphere_radius(value: float) -> None
unreal.BaseAttenuationSettings.custom_attenuation_curve(value: RuntimeFloatCurve) -> None
unreal.BaseAttenuationSettings.d_b_attenuation_at_max(value: float) -> None
unreal.BaseAttenuationSettings.distance_algorithm(value: AttenuationDistanceModel) -> None
unreal.BaseAttenuationSettings.falloff_distance(value: float) -> None
unreal.BaseAttenuationSettings.falloff_mode(value: NaturalSoundFalloffMode) -> None
```

## `unreal.BatchRetargetSettings(Object)`

```python
unreal.BatchRetargetSettings.auto_generate_retargeter(value: bool) -> None
unreal.BatchRetargetSettings.retarget_asset(value: IKRetargeter) -> None
unreal.BatchRetargetSettings.source_skeletal_mesh(value: SkeletalMesh) -> None
unreal.BatchRetargetSettings.target_skeletal_mesh(value: SkeletalMesh) -> None
```

## `unreal.BroadphaseSettings(StructBase)`

```python
unreal.BroadphaseSettings.__init__() -> None
```

## `unreal.CSVImportSettings(StructBase)`

```python
unreal.CSVImportSettings.__init__(import_row_struct: ScriptStruct = None, import_type: CSVImportType = CSVImportType.ECSV_DATA_TABLE, import_curve_interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_LINEAR) -> None
unreal.CSVImportSettings.import_curve_interp_mode(value: RichCurveInterpMode) -> None
unreal.CSVImportSettings.import_row_struct(value: ScriptStruct) -> None
unreal.CSVImportSettings.import_type(value: CSVImportType) -> None
```

## `unreal.ColorGradePerRangeSettings(StructBase)`

```python
unreal.ColorGradePerRangeSettings.__init__(saturation: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], contrast: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], gamma: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], gain: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], offset: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.ColorGradePerRangeSettings.contrast(value: Vector4) -> None
unreal.ColorGradePerRangeSettings.gain(value: Vector4) -> None
unreal.ColorGradePerRangeSettings.gamma(value: Vector4) -> None
unreal.ColorGradePerRangeSettings.offset(value: Vector4) -> None
unreal.ColorGradePerRangeSettings.saturation(value: Vector4) -> None
```

## `unreal.ColorGradingSettings(StructBase)`

```python
unreal.ColorGradingSettings.__init__(global_: ColorGradePerRangeSettings = [[1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000, 0.000000]], shadows: ColorGradePerRangeSettings = [[1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000, 0.000000]], midtones: ColorGradePerRangeSettings = [[1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000, 0.000000]], highlights: ColorGradePerRangeSettings = [[1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000, 0.000000]], shadows_max: float = 0.000000, highlights_min: float = 0.000000, highlights_max: float = 0.000000) -> None
unreal.ColorGradingSettings.global_(value: ColorGradePerRangeSettings) -> None
unreal.ColorGradingSettings.highlights(value: ColorGradePerRangeSettings) -> None
unreal.ColorGradingSettings.highlights_max(value: float) -> None
unreal.ColorGradingSettings.highlights_min(value: float) -> None
unreal.ColorGradingSettings.midtones(value: ColorGradePerRangeSettings) -> None
unreal.ColorGradingSettings.shadows(value: ColorGradePerRangeSettings) -> None
unreal.ColorGradingSettings.shadows_max(value: float) -> None
```

## `unreal.ComputeDistanceFieldSettings(StructBase)`

```python
unreal.ComputeDistanceFieldSettings.__init__(compute_mode: DistanceFieldComputeMode = DistanceFieldComputeMode.NARROW_BAND, narrow_band_width: float = 0.000000, narrow_band_units: DistanceFieldUnits = DistanceFieldUnits.NUMBER_OF_VOXELS, voxels_per_dimensions: IntVector = [0, 0, 0], require_power2: bool = False) -> None
unreal.ComputeDistanceFieldSettings.compute_mode(value: DistanceFieldComputeMode) -> None
unreal.ComputeDistanceFieldSettings.narrow_band_units(value: DistanceFieldUnits) -> None
unreal.ComputeDistanceFieldSettings.narrow_band_width(value: float) -> None
unreal.ComputeDistanceFieldSettings.require_power2(value: bool) -> None
unreal.ComputeDistanceFieldSettings.voxels_per_dimensions(value: IntVector) -> None
```

## `unreal.ConstantQNRTSettings(AudioSynesthesiaNRTSettings)`

```python
unreal.ConstantQNRTSettings.analysis_period() -> float
unreal.ConstantQNRTSettings.band_width_stretch() -> float
unreal.ConstantQNRTSettings.cqt_normalization() -> ConstantQNormalizationEnum
unreal.ConstantQNRTSettings.downmix_to_mono() -> bool
unreal.ConstantQNRTSettings.fft_size() -> ConstantQFFTSizeEnum
unreal.ConstantQNRTSettings.noise_floor_db() -> float
unreal.ConstantQNRTSettings.num_bands() -> int
unreal.ConstantQNRTSettings.num_bands_per_octave() -> float
unreal.ConstantQNRTSettings.spectrum_type() -> AudioSpectrumType
unreal.ConstantQNRTSettings.starting_frequency() -> float
unreal.ConstantQNRTSettings.window_type() -> FFTWindowType
```

## `unreal.ConstantQSettings(AudioSynesthesiaSettings)`

```python
unreal.ConstantQSettings.analysis_period_in_seconds() -> float
unreal.ConstantQSettings.band_width_stretch() -> float
unreal.ConstantQSettings.cqt_normalization() -> ConstantQNormalizationEnum
unreal.ConstantQSettings.downmix_to_mono() -> bool
unreal.ConstantQSettings.fft_size() -> ConstantQFFTSizeEnum
unreal.ConstantQSettings.noise_floor_db() -> float
unreal.ConstantQSettings.num_bands() -> int
unreal.ConstantQSettings.num_bands_per_octave() -> float
unreal.ConstantQSettings.spectrum_type() -> AudioSpectrumType
unreal.ConstantQSettings.starting_frequency_hz() -> float
unreal.ConstantQSettings.window_type() -> FFTWindowType
```

## `unreal.ConvolutionBloomSettings(StructBase)`

```python
unreal.ConvolutionBloomSettings.__init__(texture: Texture2D = None, scatter_dispersion: float = 0.000000, size: float = 0.000000, center_uv: Vector2D = [0.000000, 0.000000], pre_filter_min: float = 0.000000, pre_filter_max: float = 0.000000, pre_filter_mult: float = 0.000000, buffer_scale: float = 0.000000) -> None
unreal.ConvolutionBloomSettings.buffer_scale(value: float) -> None
unreal.ConvolutionBloomSettings.center_uv(value: Vector2D) -> None
unreal.ConvolutionBloomSettings.pre_filter_max(value: float) -> None
unreal.ConvolutionBloomSettings.pre_filter_min(value: float) -> None
unreal.ConvolutionBloomSettings.pre_filter_mult(value: float) -> None
unreal.ConvolutionBloomSettings.scatter_dispersion(value: float) -> None
unreal.ConvolutionBloomSettings.size(value: float) -> None
unreal.ConvolutionBloomSettings.texture(value: Texture2D) -> None
```

## `unreal.DynamicsBandSettings(StructBase)`

```python
unreal.DynamicsBandSettings.__init__(crossover_top_frequency: float = 0.000000, attack_time_msec: float = 0.000000, release_time_msec: float = 0.000000, threshold_db: float = 0.000000, ratio: float = 0.000000, knee_bandwidth_db: float = 0.000000, input_gain_db: float = 0.000000, output_gain_db: float = 0.000000) -> None
unreal.DynamicsBandSettings.attack_time_msec(value: float) -> None
unreal.DynamicsBandSettings.crossover_top_frequency(value: float) -> None
unreal.DynamicsBandSettings.input_gain_db(value: float) -> None
unreal.DynamicsBandSettings.knee_bandwidth_db(value: float) -> None
unreal.DynamicsBandSettings.output_gain_db(value: float) -> None
unreal.DynamicsBandSettings.ratio(value: float) -> None
unreal.DynamicsBandSettings.release_time_msec(value: float) -> None
unreal.DynamicsBandSettings.threshold_db(value: float) -> None
```

## `unreal.EarthBuildingSettings(EarthLayerSettingsBase)`

```python
unreal.EarthBuildingSettings.__init__(use_bake_board: bool = False, use_earth_prefab: bool = False, build_parallel: bool = False, batch_entity_size: int = 0, debug_mode: bool = False, max_instance_count_per_ism: int = 0, default_regional_prefab_asset_library: SoftObjectPath = [""], regional_prefab_asset_libraries: Array[SoftObjectPath] = [], is_visible: bool = False, use_collision: bool = False) -> None
unreal.EarthBuildingSettings.batch_entity_size(value: int) -> None
unreal.EarthBuildingSettings.build_parallel(value: bool) -> None
unreal.EarthBuildingSettings.debug_mode(value: bool) -> None
unreal.EarthBuildingSettings.default_regional_prefab_asset_library(value: SoftObjectPath) -> None
unreal.EarthBuildingSettings.is_visible(value: bool) -> None
unreal.EarthBuildingSettings.max_instance_count_per_ism(value: int) -> None
unreal.EarthBuildingSettings.regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
unreal.EarthBuildingSettings.use_collision(value: bool) -> None
unreal.EarthBuildingSettings.use_earth_prefab(value: bool) -> None
```

## `unreal.EarthCustomLayerConfig(StructBase)`

```python
unreal.EarthCustomLayerConfig.__init__(layer_type: LayerType = 0, prefab_type: ScriptStruct = None, level_config: Array[int] = [], build_pcg_point: bool = False, build_parallel: bool = False, batch_entity_size: int = 0, debug_mode: bool = False) -> None
unreal.EarthCustomLayerConfig.batch_entity_size(value: int) -> None
unreal.EarthCustomLayerConfig.build_parallel(value: bool) -> None
unreal.EarthCustomLayerConfig.build_pcg_point(value: bool) -> None
unreal.EarthCustomLayerConfig.debug_mode(value: bool) -> None
unreal.EarthCustomLayerConfig.layer_type(value: LayerType) -> None
unreal.EarthCustomLayerConfig.level_config(value: Array[int]) -> None
unreal.EarthCustomLayerConfig.prefab_type(value: ScriptStruct) -> None
```

## `unreal.EarthCustomSettings(EarthLayerSettingsBase)`

```python
unreal.EarthCustomSettings.__init__(use_bake_board: bool = False, layer_configs: Array[EarthCustomLayerConfig] = [], default_regional_prefab_asset_library: SoftObjectPath = [""], regional_prefab_asset_libraries: Array[SoftObjectPath] = []) -> None
unreal.EarthCustomSettings.default_regional_prefab_asset_library(value: SoftObjectPath) -> None
unreal.EarthCustomSettings.layer_configs(value: Array[EarthCustomLayerConfig]) -> None
unreal.EarthCustomSettings.regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
```

## `unreal.EarthDebuggerSettingsData(StructBase)`

```python
unreal.EarthDebuggerSettingsData.__init__() -> None
```

## `unreal.EarthDemOverlayerSettings(EarthTextureOverlayerSettings)`

```python
unreal.EarthDemOverlayerSettings.__init__() -> None
```

## `unreal.EarthDomOverlayerSettings(EarthTextureOverlayerSettings)`

```python
unreal.EarthDomOverlayerSettings.__init__() -> None
```

## `unreal.EarthDomProcessSettings(StructBase)`

```python
unreal.EarthDomProcessSettings.__init__() -> None
```

## `unreal.EarthEditorAPI(StandardApiClassBase)`

```python
unreal.EarthEditorAPI.enter_earth_editor(params: EnterEarthEditorParams) -> Optional[ResultBase]
unreal.EarthEditorAPI.update_earth_tiles(params: UpdateEarthTilesParams) -> Optional[ResultBase]
```

## `unreal.EarthEditorSaveAtom(EntityAtomBase)`

```python
unreal.EarthEditorSaveAtom.save_content(value: str) -> None
```

## `unreal.EarthEmbankmentSettings(EarthLayerSettingsBase)`

```python
unreal.EarthEmbankmentSettings.__init__(use_bake_board: bool = False, build_parallel: bool = False, batch_entity_size: int = 0, debug_mode: bool = False, max_instance_count_per_ism: int = 0, default_regional_prefab_asset_library: SoftObjectPath = [""], regional_prefab_asset_libraries: Array[SoftObjectPath] = [], is_visible: bool = False, use_collision: bool = False) -> None
unreal.EarthEmbankmentSettings.batch_entity_size(value: int) -> None
unreal.EarthEmbankmentSettings.build_parallel(value: bool) -> None
unreal.EarthEmbankmentSettings.debug_mode(value: bool) -> None
unreal.EarthEmbankmentSettings.default_regional_prefab_asset_library(value: SoftObjectPath) -> None
unreal.EarthEmbankmentSettings.is_visible(value: bool) -> None
unreal.EarthEmbankmentSettings.max_instance_count_per_ism(value: int) -> None
unreal.EarthEmbankmentSettings.regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
unreal.EarthEmbankmentSettings.use_collision(value: bool) -> None
```

## `unreal.EarthFeatureIdSettings(EarthLayerSettingsBase)`

```python
unreal.EarthFeatureIdSettings.__init__(use_bake_board: bool = False) -> None
```

## `unreal.EarthGlobalSettings(StructBase)`

```python
unreal.EarthGlobalSettings.__init__() -> None
```

## `unreal.EarthLayerSettingsBase(StructBase)`

```python
unreal.EarthLayerSettingsBase.__init__(use_bake_board: bool = False) -> None
unreal.EarthLayerSettingsBase.use_bake_board(value: bool) -> None
```

## `unreal.EarthOutputMergeConfigFragment(EarthExternalFragment)`

```python
unreal.EarthOutputMergeConfigFragment.__init__(validated: bool = False, valid: bool = False, max_instance_count: int = 0) -> None
unreal.EarthOutputMergeConfigFragment.max_instance_count(value: int) -> None
```

## `unreal.EarthRoadEditorFragment(EarthPropertyFragment)`

```python
unreal.EarthRoadEditorFragment.__init__(validated: bool = False, valid: bool = False, level: int = 0, lanes: IntPoint = [0, 0], lane_width: float = 0.000000, chamfer_corner: bool = False, chamfer_length: float = 0.000000) -> None
unreal.EarthRoadEditorFragment.chamfer_corner(value: bool) -> None
unreal.EarthRoadEditorFragment.chamfer_length(value: float) -> None
unreal.EarthRoadEditorFragment.lane_width(value: float) -> None
unreal.EarthRoadEditorFragment.lanes(value: IntPoint) -> None
unreal.EarthRoadEditorFragment.level(value: int) -> None
```

## `unreal.EarthRoadModifierEditorFragment(EarthPropertyFragment)`

```python
unreal.EarthRoadModifierEditorFragment.__init__(validated: bool = False, valid: bool = False, target_road_lanes: Array[EarthModelerEditorRoadLaneType] = [], modifier_type: EarthRoadModifierType = EarthRoadModifierType.CUT, modifier_range: EarthRoadModifierRange = EarthRoadModifierRange.BOTH, replacement_lane_asset: EarthPrefabAsset = None) -> None
unreal.EarthRoadModifierEditorFragment.modifier_range(value: EarthRoadModifierRange) -> None
unreal.EarthRoadModifierEditorFragment.modifier_type(value: EarthRoadModifierType) -> None
unreal.EarthRoadModifierEditorFragment.replacement_lane_asset(value: EarthPrefabAsset) -> None
unreal.EarthRoadModifierEditorFragment.target_road_lanes(value: Array[EarthModelerEditorRoadLaneType]) -> None
```

## `unreal.EarthRoadSettings(EarthLayerSettingsBase)`

```python
unreal.EarthRoadSettings.__init__(use_bake_board: bool = False, use_road_feature_lod: bool = False, build_underground_road: bool = False, is_visible: bool = False, is_visible_traffic: bool = False, use_collision: bool = False, use_earth_prefab: bool = False, build_parallel: bool = False, batch_entity_size: int = 0, debug_mode: bool = False, max_instance_count_per_ism: int = 0, default_regional_prefab_asset_library: SoftObjectPath = [""], regional_prefab_asset_libraries: Array[SoftObjectPath] = []) -> None
unreal.EarthRoadSettings.b_use_earth_prefab_road(value: bool) -> None
unreal.EarthRoadSettings.batch_entity_size(value: int) -> None
unreal.EarthRoadSettings.build_parallel(value: bool) -> None
unreal.EarthRoadSettings.build_underground_road(value: bool) -> None
unreal.EarthRoadSettings.debug_mode(value: bool) -> None
unreal.EarthRoadSettings.default_regional_prefab_asset_library(value: SoftObjectPath) -> None
unreal.EarthRoadSettings.is_visible(value: bool) -> None
unreal.EarthRoadSettings.is_visible_traffic(value: bool) -> None
unreal.EarthRoadSettings.max_instance_count_per_ism(value: int) -> None
unreal.EarthRoadSettings.regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
unreal.EarthRoadSettings.use_collision(value: bool) -> None
unreal.EarthRoadSettings.use_earth_prefab(value: bool) -> None
unreal.EarthRoadSettings.use_road_feature_lod(value: bool) -> None
```

## `unreal.EarthRoadTerrainBufferSettings(StructBase)`

```python
unreal.EarthRoadTerrainBufferSettings.__init__() -> None
```

## `unreal.EarthScenerySettings(EarthLayerSettingsBase)`

```python
unreal.EarthScenerySettings.__init__(use_bake_board: bool = False, is_visible: bool = False) -> None
unreal.EarthScenerySettings.is_visible(value: bool) -> None
```

## `unreal.EarthTerrainSettings(EarthLayerSettingsBase)`

```python
unreal.EarthTerrainSettings.__init__(use_bake_board: bool = False, is_visible: bool = False) -> None
unreal.EarthTerrainSettings.is_visible(value: bool) -> None
```

## `unreal.EarthVegetationSettings(EarthLayerSettingsBase)`

```python
unreal.EarthVegetationSettings.__init__(use_bake_board: bool = False, default_vegetation_biome_rule_data_table: SoftObjectPath = [""], city_vegetation_biome_rule_data_table: SoftObjectPath = [""], is_visible: bool = False, halton_base: IntPoint = [0, 0], use_default_eco_id: bool = False, default_eco_id: int = 0, random_seed: int = 0, total_scale: float = 0.000000, vgmthreshhold: IntPoint = [0, 0], use_random_offset: bool = False, random_offset: Vector = [0.000000, 0.000000, 0.000000], use_random_rotation: bool = False, use_dispersed_degree_samples: bool = False, degree_range: IntPoint = [0, 0], dispersed_degrees: Array[int] = [], global_density_scale: float = 0.000000, fix_dom_sample_level: bool = False, fixed_dom_sample_level: int = 0, use_parallel_sample: bool = False, sample_slice_factor: int = 0, cast_shadow: bool = False, use_distance_cull: bool = False, desired_max_draw_distance: float = 0.000000, max_register_instance_num: int = 0, use_instance_component_pool: bool = False, preallocate_instance_components: int = 0, preallocate_instance_component_instance_num: int = 0, max_concurrent_batch: int = 0, instance_register_slice_factor: int = 0, world_position_offset_disable_distance: int = 0) -> None
unreal.EarthVegetationSettings.cast_shadow(value: bool) -> None
unreal.EarthVegetationSettings.city_vegetation_biome_rule_data_table(value: SoftObjectPath) -> None
unreal.EarthVegetationSettings.default_eco_id(value: int) -> None
unreal.EarthVegetationSettings.default_vegetation_biome_rule_data_table(value: SoftObjectPath) -> None
unreal.EarthVegetationSettings.degree_range(value: IntPoint) -> None
unreal.EarthVegetationSettings.desired_max_draw_distance(value: float) -> None
unreal.EarthVegetationSettings.dispersed_degrees(value: Array[int]) -> None
unreal.EarthVegetationSettings.fix_dom_sample_level(value: bool) -> None
unreal.EarthVegetationSettings.fixed_dom_sample_level(value: int) -> None
unreal.EarthVegetationSettings.global_density_scale(value: float) -> None
unreal.EarthVegetationSettings.halton_base(value: IntPoint) -> None
unreal.EarthVegetationSettings.instance_register_slice_factor(value: int) -> None
unreal.EarthVegetationSettings.is_visible(value: bool) -> None
unreal.EarthVegetationSettings.max_concurrent_batch(value: int) -> None
unreal.EarthVegetationSettings.max_register_instance_num(value: int) -> None
unreal.EarthVegetationSettings.preallocate_instance_component_instance_num(value: int) -> None
unreal.EarthVegetationSettings.preallocate_instance_components(value: int) -> None
unreal.EarthVegetationSettings.random_offset(value: Vector) -> None
unreal.EarthVegetationSettings.random_seed(value: int) -> None
unreal.EarthVegetationSettings.sample_slice_factor(value: int) -> None
unreal.EarthVegetationSettings.total_scale(value: float) -> None
unreal.EarthVegetationSettings.use_default_eco_id(value: bool) -> None
unreal.EarthVegetationSettings.use_dispersed_degree_samples(value: bool) -> None
unreal.EarthVegetationSettings.use_distance_cull(value: bool) -> None
unreal.EarthVegetationSettings.use_instance_component_pool(value: bool) -> None
unreal.EarthVegetationSettings.use_parallel_sample(value: bool) -> None
unreal.EarthVegetationSettings.use_random_offset(value: bool) -> None
unreal.EarthVegetationSettings.use_random_rotation(value: bool) -> None
unreal.EarthVegetationSettings.vgmthreshhold(value: IntPoint) -> None
unreal.EarthVegetationSettings.world_position_offset_disable_distance(value: int) -> None
```

## `unreal.EditorDialog(BlueprintFunctionLibrary)`

```python
unreal.EditorDialog.show_message(title: Text, message: Text, message_type: AppMsgType, default_value: AppReturnType = AppReturnType.NO, message_category: AppMsgCategory = AppMsgCategory.WARNING) -> AppReturnType
unreal.EditorDialog.show_object_details_view(title: Text, out_object: Object, options: EditorDialogLibraryObjectDetailsViewOptions = [True, True, False, 0, 0, 0.600000]) -> bool
unreal.EditorDialog.show_objects_details_view(title: Text, out_objects: Array[Object], options: EditorDialogLibraryObjectDetailsViewOptions = [True, True, False, 0, 0, 0.600000]) -> bool
unreal.EditorDialog.show_suppressable_warning_dialog(title: Text, message: Text, ini_setting_name: str, ini_setting_file_name_override: str = "", default_value: bool = True) -> bool
```

## `unreal.EditorDialogLibraryObjectDetailsViewOptions(StructBase)`

```python
unreal.EditorDialogLibraryObjectDetailsViewOptions.__init__(show_object_name: bool = False, allow_search: bool = False, allow_resizing: bool = False, min_width: int = 0, min_height: int = 0, value_column_width_ratio: float = 0.000000) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_resizing(value: bool) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.allow_search(value: bool) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.min_height(value: int) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.min_width(value: int) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.show_object_name(value: bool) -> None
unreal.EditorDialogLibraryObjectDetailsViewOptions.value_column_width_ratio(value: float) -> None
```

## `unreal.EditorFilterLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorFilterLibrary.by_actor_label(target_array: Array[Actor], name_sub_string: str, string_match: EditorScriptingStringMatchType = EditorScriptingStringMatchType.CONTAINS, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE, ignore_case: bool = True) -> Array[Actor]
unreal.EditorFilterLibrary.by_actor_tag(target_array: Array[Actor], tag: Name, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Actor]
unreal.EditorFilterLibrary.by_class(target_array: Array[Object], object_class: Class, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Object]
unreal.EditorFilterLibrary.by_id_name(target_array: Array[Object], name_sub_string: str, string_match: EditorScriptingStringMatchType = EditorScriptingStringMatchType.CONTAINS, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Object]
unreal.EditorFilterLibrary.by_layer(target_array: Array[Actor], layer_name: Name, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Actor]
unreal.EditorFilterLibrary.by_level_name(target_array: Array[Actor], level_name: Name, filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Actor]
unreal.EditorFilterLibrary.by_selection(target_array: Array[Actor], filter_type: EditorScriptingFilterType = EditorScriptingFilterType.INCLUDE) -> Array[Actor]
```

## `unreal.EditorLoadingAndSavingUtils(Object)`

```python
unreal.EditorLoadingAndSavingUtils.export_scene(export_selected_actors_only: bool) -> None
unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages() -> Array[Package]
unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages() -> Array[Package]
unreal.EditorLoadingAndSavingUtils.import_scene(filename: str) -> None
unreal.EditorLoadingAndSavingUtils.load_map(filename: str) -> World
unreal.EditorLoadingAndSavingUtils.load_map_with_dialog() -> World
unreal.EditorLoadingAndSavingUtils.new_blank_map(save_existing_map: bool) -> World
unreal.EditorLoadingAndSavingUtils.new_map_from_template(path_to_template_level: str, save_existing_map: bool) -> World
unreal.EditorLoadingAndSavingUtils.reload_packages(packages_to_reload: Array[Package], interaction_mode: ReloadPackagesInteractionMode = ReloadPackagesInteractionMode.INTERACTIVE) -> Tuple[bool, Text]
unreal.EditorLoadingAndSavingUtils.save_current_level() -> bool
unreal.EditorLoadingAndSavingUtils.save_dirty_packages(save_map_packages: bool, save_content_packages: bool) -> bool
unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(save_map_packages: bool, save_content_packages: bool) -> bool
unreal.EditorLoadingAndSavingUtils.save_map(world: World, asset_path: str) -> bool
unreal.EditorLoadingAndSavingUtils.save_packages(packages_to_save: Array[Package], only_dirty: bool) -> bool
unreal.EditorLoadingAndSavingUtils.save_packages_with_dialog(packages_to_save: Array[Package], only_dirty: bool) -> bool
unreal.EditorLoadingAndSavingUtils.unload_packages(packages_to_unload: Array[Package]) -> Tuple[bool, Text]
```

## `unreal.EditorParameterGroup(StructBase)`

```python
unreal.EditorParameterGroup.__init__() -> None
```

## `unreal.EditorPythonScripting(BlueprintFunctionLibrary)`

```python
unreal.EditorPythonScripting.get_keep_python_script_alive() -> bool
unreal.EditorPythonScripting.set_keep_python_script_alive(new_keep_alive: bool) -> None
```

## `unreal.EditorValidatorBase(Object)`

```python
unreal.EditorValidatorBase.asset_fails(asset: Object, message: Text) -> None
unreal.EditorValidatorBase.asset_passes(asset: Object) -> None
unreal.EditorValidatorBase.asset_warning(asset: Object, message: Text) -> None
unreal.EditorValidatorBase.can_validate(usecase: DataValidationUsecase) -> bool
unreal.EditorValidatorBase.can_validate_asset(asset: Object) -> bool
unreal.EditorValidatorBase.get_validation_result() -> DataValidationResult
unreal.EditorValidatorBase.k2_can_validate(usecase: DataValidationUsecase) -> bool
unreal.EditorValidatorBase.k2_can_validate_asset(asset: Object) -> bool
unreal.EditorValidatorBase.k2_validate_loaded_asset(asset: Object) -> DataValidationResult
unreal.EditorValidatorBase.validate_loaded_asset(asset: Object) -> DataValidationResult
```

## `unreal.EnterEarthEditorParams(ParamsBase)`

```python
unreal.EnterEarthEditorParams.__init__(language: str = "") -> None
unreal.EnterEarthEditorParams.language(value: str) -> None
```

## `unreal.ExtendMPCSettings_51(StructBase)`

```python
unreal.ExtendMPCSettings_51.__init__(spring: float = 0.000000, summer: float = 0.000000, autumn: float = 0.000000, winter: float = 0.000000) -> None
unreal.ExtendMPCSettings_51.autumn(value: float) -> None
unreal.ExtendMPCSettings_51.spring(value: float) -> None
unreal.ExtendMPCSettings_51.summer(value: float) -> None
unreal.ExtendMPCSettings_51.winter(value: float) -> None
```

## `unreal.ExtendSettings_51(StructBase)`

```python
unreal.ExtendSettings_51.__init__(use_cloud_map_offset: bool = False, cloud_map_offset: Vector2D = [0.000000, 0.000000], cloud_map_offset_curve: CurveVector = None, sunrise_time: float = 0.000000, sunset_time: float = 0.000000, sun_elevation: float = 0.000000, sun_azimuth: float = 0.000000, moonrise_time: float = 0.000000, moonset_time: float = 0.000000, moon_elevation: float = 0.000000, moon_azimuth: float = 0.000000) -> None
unreal.ExtendSettings_51.cloud_map_offset(value: Vector2D) -> None
unreal.ExtendSettings_51.cloud_map_offset_curve(value: CurveVector) -> None
unreal.ExtendSettings_51.moon_azimuth(value: float) -> None
unreal.ExtendSettings_51.moon_elevation(value: float) -> None
unreal.ExtendSettings_51.moonrise_time(value: float) -> None
unreal.ExtendSettings_51.moonset_time(value: float) -> None
unreal.ExtendSettings_51.sun_azimuth(value: float) -> None
unreal.ExtendSettings_51.sun_elevation(value: float) -> None
unreal.ExtendSettings_51.sunrise_time(value: float) -> None
unreal.ExtendSettings_51.sunset_time(value: float) -> None
unreal.ExtendSettings_51.use_cloud_map_offset(value: bool) -> None
```

## `unreal.FilmStockSettings(StructBase)`

```python
unreal.FilmStockSettings.__init__(slope: float = 0.000000, toe: float = 0.000000, shoulder: float = 0.000000, black_clip: float = 0.000000, white_clip: float = 0.000000) -> None
unreal.FilmStockSettings.black_clip(value: float) -> None
unreal.FilmStockSettings.shoulder(value: float) -> None
unreal.FilmStockSettings.slope(value: float) -> None
unreal.FilmStockSettings.toe(value: float) -> None
unreal.FilmStockSettings.white_clip(value: float) -> None
```

## `unreal.FontOutlineSettings(StructBase)`

```python
unreal.FontOutlineSettings.__init__(outline_size: int = 0, mitered_corners: bool = False, separate_fill_alpha: bool = False, apply_outline_to_drop_shadows: bool = False, outline_material: Object = None, outline_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.FontOutlineSettings.apply_outline_to_drop_shadows(value: bool) -> None
unreal.FontOutlineSettings.mitered_corners(value: bool) -> None
unreal.FontOutlineSettings.outline_color(value: LinearColor) -> None
unreal.FontOutlineSettings.outline_material(value: Object) -> None
unreal.FontOutlineSettings.outline_size(value: int) -> None
unreal.FontOutlineSettings.separate_fill_alpha(value: bool) -> None
```

## `unreal.FontSdfSettings(StructBase)`

```python
unreal.FontSdfSettings.__init__() -> None
```

## `unreal.ForceFeedbackAttenuationSettings(BaseAttenuationSettings)`

```python
unreal.ForceFeedbackAttenuationSettings.__init__(distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.LINEAR, attenuation_shape: AttenuationShape = AttenuationShape.SPHERE, falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES, d_b_attenuation_at_max: float = 0.000000, attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000], cone_offset: float = 0.000000, falloff_distance: float = 0.000000, cone_sphere_radius: float = 0.000000, cone_sphere_falloff_distance: float = 0.000000, custom_attenuation_curve: RuntimeFloatCurve = []) -> None
```

## `unreal.GameMapsSettings(Object)`

```python
unreal.GameMapsSettings.get_game_maps_settings() -> GameMapsSettings
unreal.GameMapsSettings.get_skip_assigning_gamepad_to_player1() -> bool
unreal.GameMapsSettings.set_skip_assigning_gamepad_to_player1(skip_first_player: bool = True) -> None
```

## `unreal.GameUserSettings(Object)`

```python
unreal.GameUserSettings.apply_hardware_benchmark_results() -> None
unreal.GameUserSettings.apply_non_resolution_settings() -> None
unreal.GameUserSettings.apply_resolution_settings(check_for_command_line_overrides: bool) -> None
unreal.GameUserSettings.apply_settings(check_for_command_line_overrides: bool = True) -> None
unreal.GameUserSettings.confirm_video_mode() -> None
unreal.GameUserSettings.enable_hdr_display_output(enable: bool, display_nits: int = 1000) -> None
unreal.GameUserSettings.get_anti_aliasing_quality() -> int
unreal.GameUserSettings.get_audio_quality_level() -> int
unreal.GameUserSettings.get_current_hdr_display_nits() -> int
unreal.GameUserSettings.get_default_resolution() -> IntPoint
unreal.GameUserSettings.get_default_resolution_scale() -> float
unreal.GameUserSettings.get_default_window_mode() -> WindowMode
unreal.GameUserSettings.get_default_window_position() -> IntPoint
unreal.GameUserSettings.get_desktop_resolution() -> IntPoint
unreal.GameUserSettings.get_foliage_quality() -> int
unreal.GameUserSettings.get_frame_pace() -> int
unreal.GameUserSettings.get_frame_rate_limit() -> float
unreal.GameUserSettings.get_fullscreen_mode() -> WindowMode
unreal.GameUserSettings.get_game_user_settings() -> GameUserSettings
unreal.GameUserSettings.get_global_illumination_quality() -> int
unreal.GameUserSettings.get_last_confirmed_fullscreen_mode() -> WindowMode
unreal.GameUserSettings.get_last_confirmed_screen_resolution() -> IntPoint
unreal.GameUserSettings.get_overall_scalability_level() -> int
unreal.GameUserSettings.get_post_processing_quality() -> int
unreal.GameUserSettings.get_preferred_fullscreen_mode() -> WindowMode
unreal.GameUserSettings.get_recommended_resolution_scale() -> float
unreal.GameUserSettings.get_reflection_quality() -> int
unreal.GameUserSettings.get_resolution_scale_information_ex() -> Tuple[float, float, float, float]
unreal.GameUserSettings.get_resolution_scale_normalized() -> float
unreal.GameUserSettings.get_screen_resolution() -> IntPoint
unreal.GameUserSettings.get_shading_quality() -> int
unreal.GameUserSettings.get_shadow_quality() -> int
unreal.GameUserSettings.get_sync_interval() -> int
unreal.GameUserSettings.get_texture_quality() -> int
unreal.GameUserSettings.get_view_distance_quality() -> int
unreal.GameUserSettings.get_visual_effect_quality() -> int
unreal.GameUserSettings.is_dirty() -> bool
unreal.GameUserSettings.is_dynamic_resolution_dirty() -> bool
unreal.GameUserSettings.is_dynamic_resolution_enabled() -> bool
unreal.GameUserSettings.is_fullscreen_mode_dirty() -> bool
unreal.GameUserSettings.is_hdr_enabled() -> bool
unreal.GameUserSettings.is_screen_resolution_dirty() -> bool
unreal.GameUserSettings.is_v_sync_dirty() -> bool
unreal.GameUserSettings.is_v_sync_enabled() -> bool
unreal.GameUserSettings.load_settings(force_reload: bool = False) -> None
unreal.GameUserSettings.on_game_user_settings_ui_needs_update(value: OnGameUserSettingsUINeedsUpdate) -> None
unreal.GameUserSettings.reset_to_current_settings() -> None
unreal.GameUserSettings.revert_video_mode() -> None
unreal.GameUserSettings.run_hardware_benchmark(work_scale: int = 10, cpu_multiplier: float = 1.000000, gpu_multiplier: float = 1.000000) -> None
unreal.GameUserSettings.save_settings() -> None
unreal.GameUserSettings.set_anti_aliasing_quality(value: int) -> None
unreal.GameUserSettings.set_audio_quality_level(quality_level: int) -> None
unreal.GameUserSettings.set_benchmark_fallback_values() -> None
unreal.GameUserSettings.set_dynamic_resolution_enabled(enable: bool) -> None
unreal.GameUserSettings.set_foliage_quality(value: int) -> None
unreal.GameUserSettings.set_frame_rate_limit(new_limit: float) -> None
unreal.GameUserSettings.set_fullscreen_mode(fullscreen_mode: WindowMode) -> None
unreal.GameUserSettings.set_global_illumination_quality(value: int) -> None
unreal.GameUserSettings.set_overall_scalability_level(value: int) -> None
unreal.GameUserSettings.set_post_processing_quality(value: int) -> None
unreal.GameUserSettings.set_reflection_quality(value: int) -> None
unreal.GameUserSettings.set_resolution_scale_normalized(new_scale_normalized: float) -> None
unreal.GameUserSettings.set_resolution_scale_value_ex(new_scale_value: float) -> None
unreal.GameUserSettings.set_screen_resolution(resolution: IntPoint) -> None
unreal.GameUserSettings.set_shading_quality(value: int) -> None
unreal.GameUserSettings.set_shadow_quality(value: int) -> None
unreal.GameUserSettings.set_texture_quality(value: int) -> None
unreal.GameUserSettings.set_to_defaults() -> None
unreal.GameUserSettings.set_v_sync_enabled(enable: bool) -> None
unreal.GameUserSettings.set_view_distance_quality(value: int) -> None
unreal.GameUserSettings.set_visual_effect_quality(value: int) -> None
unreal.GameUserSettings.supports_hdr_display_output() -> bool
unreal.GameUserSettings.validate_settings() -> None
```

## `unreal.GameplayModEvaluationChannelSettings(StructBase)`

```python
unreal.GameplayModEvaluationChannelSettings.__init__() -> None
```

## `unreal.GaussianSumBloomSettings(StructBase)`

```python
unreal.GaussianSumBloomSettings.__init__(intensity: float = 0.000000, threshold: float = 0.000000, size_scale: float = 0.000000, filter1_size: float = 0.000000, filter2_size: float = 0.000000, filter3_size: float = 0.000000, filter4_size: float = 0.000000, filter5_size: float = 0.000000, filter6_size: float = 0.000000, filter1_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], filter2_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], filter3_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], filter4_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], filter5_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], filter6_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.GaussianSumBloomSettings.filter1_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter1_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.filter2_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter2_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.filter3_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter3_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.filter4_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter4_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.filter5_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter5_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.filter6_size(value: float) -> None
unreal.GaussianSumBloomSettings.filter6_tint(value: LinearColor) -> None
unreal.GaussianSumBloomSettings.intensity(value: float) -> None
unreal.GaussianSumBloomSettings.size_scale(value: float) -> None
unreal.GaussianSumBloomSettings.threshold(value: float) -> None
```

## `unreal.GeoReferencingEditorBPLibrary(BlueprintFunctionLibrary)`

```python
unreal.GeoReferencingEditorBPLibrary.get_viewport_cursor_information() -> Tuple[bool, Vector2D, Vector, Vector]
unreal.GeoReferencingEditorBPLibrary.get_viewport_cursor_location() -> Tuple[bool, Vector2D]
unreal.GeoReferencingEditorBPLibrary.line_trace(world_location: Vector, world_direction: Vector, actors_to_ignore: Array[Actor], trace_complex: bool, show_trace: bool) -> Tuple[bool, HitResult]
unreal.GeoReferencingEditorBPLibrary.line_trace_viewport(actors_to_ignore: Array[Actor], trace_complex: bool, show_trace: bool) -> Tuple[Vector2D, bool, HitResult]
```

## `unreal.HLODBuilderInstancingSettings(HLODBuilderSettings)`

```python
unreal.HLODBuilderInstancingSettings.disallow_nanite(value: bool) -> None
```

## `unreal.HairDecimationSettings(StructBase)`

```python
unreal.HairDecimationSettings.__init__() -> None
```

## `unreal.HairDeformationSettings(StructBase)`

```python
unreal.HairDeformationSettings.__init__() -> None
```

## `unreal.HairInterpolationSettings(StructBase)`

```python
unreal.HairInterpolationSettings.__init__(guide_type: GroomGuideType = GroomGuideType.IMPORTED, hair_to_guide_density: float = 0.000000, rigged_guide_num_curves: int = 0, rigged_guide_num_points: int = 0, interpolation_quality: HairInterpolationQuality = HairInterpolationQuality.LOW, interpolation_distance: HairInterpolationWeight = HairInterpolationWeight.PARAMETRIC, randomize_guide: bool = False, use_unique_guide: bool = False) -> None
unreal.HairInterpolationSettings.guide_type(value: GroomGuideType) -> None
unreal.HairInterpolationSettings.hair_to_guide_density(value: float) -> None
unreal.HairInterpolationSettings.interpolation_distance(value: HairInterpolationWeight) -> None
unreal.HairInterpolationSettings.interpolation_quality(value: HairInterpolationQuality) -> None
unreal.HairInterpolationSettings.randomize_guide(value: bool) -> None
unreal.HairInterpolationSettings.rigged_guide_num_curves() -> int
unreal.HairInterpolationSettings.rigged_guide_num_points() -> int
unreal.HairInterpolationSettings.use_unique_guide(value: bool) -> None
```

## `unreal.HairLODSettings(StructBase)`

```python
unreal.HairLODSettings.__init__() -> None
```

## `unreal.HairShadowSettings(StructBase)`

```python
unreal.HairShadowSettings.__init__(hair_shadow_density: float = 0.000000, hair_raytracing_radius_scale: float = 0.000000, use_hair_raytracing_geometry: bool = False, voxelize: bool = False) -> None
unreal.HairShadowSettings.hair_raytracing_radius_scale(value: float) -> None
unreal.HairShadowSettings.hair_shadow_density(value: float) -> None
unreal.HairShadowSettings.use_hair_raytracing_geometry(value: bool) -> None
unreal.HairShadowSettings.voxelize(value: bool) -> None
```

## `unreal.HairSimulationSettings(StructBase)`

```python
unreal.HairSimulationSettings.__init__(override_settings: bool = False, simulation_setup: HairSimulationSetup = [False, False, True, 1.000000, 1.000000, "root", 50.000000], solver_settings: HairSimulationSolver = [False], external_forces: HairSimulationForces = [[0.000000, 0.000000, -981.000000], 0.100000, [0.000000, 0.000000, 0.000000]], material_constraints: HairSimulationConstraints = [0.001000, 0.010000, 0.001000, 1.000000, 0.100000, 0.100000, 1.000000, 0.001000]) -> None
unreal.HairSimulationSettings.external_forces(value: HairSimulationForces) -> None
unreal.HairSimulationSettings.material_constraints(value: HairSimulationConstraints) -> None
unreal.HairSimulationSettings.override_settings(value: bool) -> None
unreal.HairSimulationSettings.simulation_setup(value: HairSimulationSetup) -> None
unreal.HairSimulationSettings.solver_settings(value: HairSimulationSolver) -> None
```

## `unreal.HairSolverSettings(StructBase)`

```python
unreal.HairSolverSettings.__init__() -> None
```

## `unreal.InteriorSettings(StructBase)`

```python
unreal.InteriorSettings.__init__(exterior_volume: float = 0.000000, exterior_time: float = 0.000000, exterior_lpf: float = 0.000000, exterior_lpf_time: float = 0.000000, interior_volume: float = 0.000000, interior_time: float = 0.000000, interior_lpf: float = 0.000000, interior_lpf_time: float = 0.000000) -> None
unreal.InteriorSettings.exterior_lpf(value: float) -> None
unreal.InteriorSettings.exterior_lpf_time(value: float) -> None
unreal.InteriorSettings.exterior_time(value: float) -> None
unreal.InteriorSettings.exterior_volume(value: float) -> None
unreal.InteriorSettings.interior_lpf(value: float) -> None
unreal.InteriorSettings.interior_lpf_time(value: float) -> None
unreal.InteriorSettings.interior_time(value: float) -> None
unreal.InteriorSettings.interior_volume(value: float) -> None
```

## `unreal.LaneBlockStyleSettings(StructBase)`

```python
unreal.LaneBlockStyleSettings.__init__() -> None
```

## `unreal.LensBloomSettings(StructBase)`

```python
unreal.LensBloomSettings.__init__(gaussian_sum: GaussianSumBloomSettings = [0.675000, -1.000000, 4.000000, 0.300000, 1.000000, 2.000000, 10.000000, 30.000000, 64.000000, [0.346500, 0.346500, 0.346500, 1.000000], [0.138000, 0.138000, 0.138000, 1.000000], [0.117600, 0.117600, 0.117600, 1.000000], [0.066000, 0.066000, 0.066000, 1.000000], [0.066000, 0.066000, 0.066000, 1.000000], [0.061000, 0.061000, 0.061000, 1.000000]], convolution: ConvolutionBloomSettings = [None, 1.000000, 1.000000, [0.500000, 0.500000], 7.000000, 15000.000000, 15.000000, 0.133000], method: BloomMethod = BloomMethod.BM_SOG) -> None
unreal.LensBloomSettings.convolution(value: ConvolutionBloomSettings) -> None
unreal.LensBloomSettings.gaussian_sum(value: GaussianSumBloomSettings) -> None
unreal.LensBloomSettings.method(value: BloomMethod) -> None
```

## `unreal.LensImperfectionSettings(StructBase)`

```python
unreal.LensImperfectionSettings.__init__(dirt_mask: Texture = None, dirt_mask_intensity: float = 0.000000, dirt_mask_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.LensImperfectionSettings.dirt_mask(value: Texture) -> None
unreal.LensImperfectionSettings.dirt_mask_intensity(value: float) -> None
unreal.LensImperfectionSettings.dirt_mask_tint(value: LinearColor) -> None
```

## `unreal.LensSettings(StructBase)`

```python
unreal.LensSettings.__init__(bloom: LensBloomSettings = [[0.675000, -1.000000, 4.000000, 0.300000, 1.000000, 2.000000, 10.000000, 30.000000, 64.000000, [0.346500, 0.346500, 0.346500, 1.000000], [0.138000, 0.138000, 0.138000, 1.000000], [0.117600, 0.117600, 0.117600, 1.000000], [0.066000, 0.066000, 0.066000, 1.000000], [0.066000, 0.066000, 0.066000, 1.000000], [0.061000, 0.061000, 0.061000, 1.000000]], [None, 1.000000, 1.000000, [0.500000, 0.500000], 7.000000, 15000.000000, 15.000000, 0.133000], BloomMethod.BM_SOG], imperfections: LensImperfectionSettings = [None, 0.000000, [0.500000, 0.500000, 0.500000, 1.000000]], chromatic_aberration: float = 0.000000) -> None
unreal.LensSettings.bloom(value: LensBloomSettings) -> None
unreal.LensSettings.chromatic_aberration(value: float) -> None
unreal.LensSettings.imperfections(value: LensImperfectionSettings) -> None
```

## `unreal.LidarPointCloudImportSettings_ASCII_Columns(StructBase)`

```python
unreal.LidarPointCloudImportSettings_ASCII_Columns.__init__(location_x: int = 0, location_y: int = 0, location_z: int = 0, red: int = 0, green: int = 0, blue: int = 0, intensity: int = 0, normal_x: int = 0, normal_y: int = 0, normal_z: int = 0) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.blue(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.green(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.intensity(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.location_x(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.location_y(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.location_z(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_x(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_y(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_z(value: int) -> None
unreal.LidarPointCloudImportSettings_ASCII_Columns.red(value: int) -> None
```

## `unreal.LiveLinkSourceBufferManagementSettings(StructBase)`

```python
unreal.LiveLinkSourceBufferManagementSettings.__init__() -> None
```

## `unreal.LoudnessNRTSettings(AudioSynesthesiaNRTSettings)`

```python
unreal.LoudnessNRTSettings.analysis_period() -> float
unreal.LoudnessNRTSettings.curve_type() -> LoudnessNRTCurveTypeEnum
unreal.LoudnessNRTSettings.maximum_frequency() -> float
unreal.LoudnessNRTSettings.minimum_frequency() -> float
unreal.LoudnessNRTSettings.noise_floor_db() -> float
```

## `unreal.LoudnessSettings(AudioSynesthesiaSettings)`

```python
unreal.LoudnessSettings.analysis_period() -> float
unreal.LoudnessSettings.curve_type() -> LoudnessCurveTypeEnum
unreal.LoudnessSettings.expected_max_loudness() -> float
unreal.LoudnessSettings.maximum_frequency() -> float
unreal.LoudnessSettings.minimum_frequency() -> float
unreal.LoudnessSettings.noise_floor_db() -> float
```

## `unreal.MRMeshConfiguration(StructBase)`

```python
unreal.MRMeshConfiguration.__init__() -> None
```

## `unreal.MediaSourceCacheSettings(StructBase)`

```python
unreal.MediaSourceCacheSettings.__init__() -> None
```

## `unreal.MeshApproximationSettings(StructBase)`

```python
unreal.MeshApproximationSettings.__init__(output_type: MeshApproximationType = MeshApproximationType.MESH_AND_MATERIALS, approximation_accuracy: float = 0.000000, clamp_voxel_dimension: int = 0, attempt_auto_thickening: bool = False, target_min_thickness_multiplier: float = 0.000000, ignore_tiny_parts: bool = False, tiny_part_size_multiplier: float = 0.000000, base_capping: MeshApproximationBaseCappingType = MeshApproximationBaseCappingType.NO_BASE_CAPPING, winding_threshold: float = 0.000000, fill_gaps: bool = False, gap_distance: float = 0.000000, occlusion_method: OccludedGeometryFilteringPolicy = OccludedGeometryFilteringPolicy.NO_OCCLUSION_FILTERING, occlude_from_bottom: bool = False, simplify_method: MeshApproximationSimplificationPolicy = MeshApproximationSimplificationPolicy.FIXED_TRIANGLE_COUNT, target_tri_count: int = 0, triangles_per_m: float = 0.000000, geometric_deviation: float = 0.000000, ground_clipping: MeshApproximationGroundPlaneClippingPolicy = MeshApproximationGroundPlaneClippingPolicy.NO_GROUND_CLIPPING, ground_clipping_z_height: float = 0.000000, estimate_hard_normals: bool = False, hard_normal_angle: float = 0.000000, uv_generation_method: MeshApproximationUVGenerationPolicy = MeshApproximationUVGenerationPolicy.PREFER_UV_ATLAS, initial_patch_count: int = 0, curvature_alignment: float = 0.000000, merging_threshold: float = 0.000000, max_angle_deviation: float = 0.000000, generate_nanite_enabled_mesh: bool = False, nanite_fallback_target: NaniteFallbackTarget = NaniteFallbackTarget.AUTO, nanite_fallback_percent_triangles: float = 0.000000, nanite_fallback_relative_error: float = 0.000000, support_ray_tracing: bool = False, allow_distance_field: bool = False, multi_sampling_aa: int = 0, render_capture_resolution: int = 0, material_settings: MaterialProxySettings = [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], capture_field_of_view: float = 0.000000, near_plane_dist: float = 0.000000, use_render_lod_meshes: bool = False, enable_simplify_pre_pass: bool = False, enable_parallel_baking: bool = False, print_debug_messages: bool = False, emit_full_debug_mesh: bool = False) -> None
unreal.MeshApproximationSettings.allow_distance_field(value: bool) -> None
unreal.MeshApproximationSettings.approximation_accuracy(value: float) -> None
unreal.MeshApproximationSettings.attempt_auto_thickening(value: bool) -> None
unreal.MeshApproximationSettings.base_capping(value: MeshApproximationBaseCappingType) -> None
unreal.MeshApproximationSettings.capture_field_of_view(value: float) -> None
unreal.MeshApproximationSettings.clamp_voxel_dimension(value: int) -> None
unreal.MeshApproximationSettings.curvature_alignment(value: float) -> None
unreal.MeshApproximationSettings.emit_full_debug_mesh(value: bool) -> None
unreal.MeshApproximationSettings.enable_parallel_baking(value: bool) -> None
unreal.MeshApproximationSettings.enable_simplify_pre_pass(value: bool) -> None
unreal.MeshApproximationSettings.estimate_hard_normals(value: bool) -> None
unreal.MeshApproximationSettings.fill_gaps(value: bool) -> None
unreal.MeshApproximationSettings.gap_distance(value: float) -> None
unreal.MeshApproximationSettings.generate_nanite_enabled_mesh(value: bool) -> None
unreal.MeshApproximationSettings.geometric_deviation(value: float) -> None
unreal.MeshApproximationSettings.ground_clipping(value: MeshApproximationGroundPlaneClippingPolicy) -> None
unreal.MeshApproximationSettings.ground_clipping_z_height(value: float) -> None
unreal.MeshApproximationSettings.hard_normal_angle(value: float) -> None
unreal.MeshApproximationSettings.ignore_tiny_parts(value: bool) -> None
unreal.MeshApproximationSettings.initial_patch_count(value: int) -> None
unreal.MeshApproximationSettings.material_settings(value: MaterialProxySettings) -> None
unreal.MeshApproximationSettings.max_angle_deviation(value: float) -> None
unreal.MeshApproximationSettings.merging_threshold(value: float) -> None
unreal.MeshApproximationSettings.multi_sampling_aa(value: int) -> None
unreal.MeshApproximationSettings.nanite_fallback_percent_triangles(value: float) -> None
unreal.MeshApproximationSettings.nanite_fallback_relative_error(value: float) -> None
unreal.MeshApproximationSettings.nanite_fallback_target(value: NaniteFallbackTarget) -> None
unreal.MeshApproximationSettings.near_plane_dist(value: float) -> None
unreal.MeshApproximationSettings.occlude_from_bottom(value: bool) -> None
unreal.MeshApproximationSettings.occlusion_method(value: OccludedGeometryFilteringPolicy) -> None
unreal.MeshApproximationSettings.output_type(value: MeshApproximationType) -> None
unreal.MeshApproximationSettings.print_debug_messages(value: bool) -> None
unreal.MeshApproximationSettings.render_capture_resolution(value: int) -> None
unreal.MeshApproximationSettings.simplify_method(value: MeshApproximationSimplificationPolicy) -> None
unreal.MeshApproximationSettings.support_ray_tracing(value: bool) -> None
unreal.MeshApproximationSettings.target_min_thickness_multiplier(value: float) -> None
unreal.MeshApproximationSettings.target_tri_count(value: int) -> None
unreal.MeshApproximationSettings.tiny_part_size_multiplier(value: float) -> None
unreal.MeshApproximationSettings.triangles_per_m(value: float) -> None
unreal.MeshApproximationSettings.use_render_lod_meshes(value: bool) -> None
unreal.MeshApproximationSettings.uv_generation_method(value: MeshApproximationUVGenerationPolicy) -> None
unreal.MeshApproximationSettings.winding_threshold(value: float) -> None
```

## `unreal.MeshBuildSettings(StructBase)`

```python
unreal.MeshBuildSettings.__init__(use_mikk_t_space: bool = False, recompute_normals: bool = False, recompute_tangents: bool = False, compute_weighted_normals: bool = False, remove_degenerates: bool = False, build_reversed_index_buffer: bool = False, use_high_precision_tangent_basis: bool = False, use_full_precision_u_vs: bool = False, use_backwards_compatible_f16_trunc_u_vs: bool = False, generate_lightmap_u_vs: bool = False, generate_distance_field_as_if_two_sided: bool = False, support_face_remap: bool = False, min_lightmap_resolution: int = 0, src_lightmap_index: int = 0, dst_lightmap_index: int = 0, build_scale3d: Vector = [0.000000, 0.000000, 0.000000], distance_field_resolution_scale: float = 0.000000, distance_field_replacement_mesh: StaticMesh = None, max_lumen_mesh_cards: int = 0) -> None
unreal.MeshBuildSettings.build_reversed_index_buffer(value: bool) -> None
unreal.MeshBuildSettings.build_scale3d(value: Vector) -> None
unreal.MeshBuildSettings.compute_weighted_normals(value: bool) -> None
unreal.MeshBuildSettings.distance_field_replacement_mesh(value: StaticMesh) -> None
unreal.MeshBuildSettings.distance_field_resolution_scale(value: float) -> None
unreal.MeshBuildSettings.dst_lightmap_index(value: int) -> None
unreal.MeshBuildSettings.generate_distance_field_as_if_two_sided(value: bool) -> None
unreal.MeshBuildSettings.generate_lightmap_u_vs(value: bool) -> None
unreal.MeshBuildSettings.max_lumen_mesh_cards(value: int) -> None
unreal.MeshBuildSettings.min_lightmap_resolution(value: int) -> None
unreal.MeshBuildSettings.recompute_normals(value: bool) -> None
unreal.MeshBuildSettings.recompute_tangents(value: bool) -> None
unreal.MeshBuildSettings.remove_degenerates(value: bool) -> None
unreal.MeshBuildSettings.src_lightmap_index(value: int) -> None
unreal.MeshBuildSettings.support_face_remap(value: bool) -> None
unreal.MeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
unreal.MeshBuildSettings.use_full_precision_u_vs(value: bool) -> None
unreal.MeshBuildSettings.use_high_precision_tangent_basis(value: bool) -> None
unreal.MeshBuildSettings.use_mikk_t_space(value: bool) -> None
```

## `unreal.MeshInstancingSettings(StructBase)`

```python
unreal.MeshInstancingSettings.__init__(actor_class_to_use: Class = None, instance_replacement_threshold: int = 0, skip_meshes_with_vertex_colors: bool = False, use_hlod_volumes: bool = False, ism_component_to_use: Class = None) -> None
unreal.MeshInstancingSettings.actor_class_to_use(value: Class) -> None
unreal.MeshInstancingSettings.instance_replacement_threshold(value: int) -> None
unreal.MeshInstancingSettings.ism_component_to_use(value: Class) -> None
unreal.MeshInstancingSettings.skip_meshes_with_vertex_colors(value: bool) -> None
unreal.MeshInstancingSettings.use_hlod_volumes(value: bool) -> None
```

## `unreal.MeshMergingSettings(StructBase)`

```python
unreal.MeshMergingSettings.__init__(target_light_map_resolution: int = 0, material_settings: MaterialProxySettings = [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], lod_selection_type: MeshLODSelectionType = MeshLODSelectionType.ALL_LO_DS, specific_lod: int = 0, generate_light_map_uv: bool = False, computed_light_map_resolution: bool = False, pivot_point_at_zero: bool = False, merge_physics_data: bool = False, merge_mesh_sockets: bool = False, merge_materials: bool = False, bake_vertex_data_to_mesh: bool = False, use_vertex_data_for_baking_material: bool = False, use_texture_binning: bool = False, use_landscape_culling: bool = False, include_imposters: bool = False, support_ray_tracing: bool = False, nanite_settings: MeshNaniteSettings = [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]) -> None
unreal.MeshMergingSettings.bake_vertex_data_to_mesh(value: bool) -> None
unreal.MeshMergingSettings.computed_light_map_resolution(value: bool) -> None
unreal.MeshMergingSettings.generate_light_map_uv(value: bool) -> None
unreal.MeshMergingSettings.include_imposters(value: bool) -> None
unreal.MeshMergingSettings.lod_selection_type(value: MeshLODSelectionType) -> None
unreal.MeshMergingSettings.material_settings(value: MaterialProxySettings) -> None
unreal.MeshMergingSettings.merge_materials(value: bool) -> None
unreal.MeshMergingSettings.merge_mesh_sockets(value: bool) -> None
unreal.MeshMergingSettings.merge_physics_data(value: bool) -> None
unreal.MeshMergingSettings.nanite_settings(value: MeshNaniteSettings) -> None
unreal.MeshMergingSettings.pivot_point_at_zero(value: bool) -> None
unreal.MeshMergingSettings.specific_lod(value: int) -> None
unreal.MeshMergingSettings.support_ray_tracing(value: bool) -> None
unreal.MeshMergingSettings.target_light_map_resolution(value: int) -> None
unreal.MeshMergingSettings.use_landscape_culling(value: bool) -> None
unreal.MeshMergingSettings.use_texture_binning(value: bool) -> None
unreal.MeshMergingSettings.use_vertex_data_for_baking_material(value: bool) -> None
```

## `unreal.MeshProxySettings(StructBase)`

```python
unreal.MeshProxySettings.__init__(screen_size: int = 0, voxel_size: float = 0.000000, material_settings: MaterialProxySettings = [TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, 5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000, 0.000000, 0.500000, 1.000000, 1.000000, 1.000000, BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False, False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]], merge_distance: float = 0.000000, unresolved_geometry_color: Color = [0, 0, 0, 0], max_ray_cast_dist: float = 0.000000, hard_angle_threshold: float = 0.000000, light_map_resolution: int = 0, normal_calculation_method: ProxyNormalComputationMethod = ProxyNormalComputationMethod.ANGLE_WEIGHTED, landscape_culling_precision: LandscapeCullingPrecision = LandscapeCullingPrecision.HIGH, calculate_correct_lod_model: bool = False, override_voxel_size: bool = False, override_transfer_distance: bool = False, use_hard_angle_threshold: bool = False, compute_light_map_resolution: bool = False, recalculate_normals: bool = False, use_landscape_culling: bool = False, support_ray_tracing: bool = False, allow_distance_field: bool = False, reuse_mesh_lightmap_u_vs: bool = False, group_identical_meshes_for_baking: bool = False, create_collision: bool = False, allow_vertex_colors: bool = False, generate_lightmap_u_vs: bool = False, nanite_settings: MeshNaniteSettings = [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0]) -> None
unreal.MeshProxySettings.allow_distance_field(value: bool) -> None
unreal.MeshProxySettings.allow_vertex_colors(value: bool) -> None
unreal.MeshProxySettings.calculate_correct_lod_model(value: bool) -> None
unreal.MeshProxySettings.compute_light_map_resolution(value: bool) -> None
unreal.MeshProxySettings.create_collision(value: bool) -> None
unreal.MeshProxySettings.generate_lightmap_u_vs(value: bool) -> None
unreal.MeshProxySettings.group_identical_meshes_for_baking(value: bool) -> None
unreal.MeshProxySettings.hard_angle_threshold(value: float) -> None
unreal.MeshProxySettings.landscape_culling_precision(value: LandscapeCullingPrecision) -> None
unreal.MeshProxySettings.light_map_resolution(value: int) -> None
unreal.MeshProxySettings.material_settings(value: MaterialProxySettings) -> None
unreal.MeshProxySettings.max_ray_cast_dist(value: float) -> None
unreal.MeshProxySettings.merge_distance(value: float) -> None
unreal.MeshProxySettings.nanite_settings(value: MeshNaniteSettings) -> None
unreal.MeshProxySettings.normal_calculation_method(value: ProxyNormalComputationMethod) -> None
unreal.MeshProxySettings.override_transfer_distance(value: bool) -> None
unreal.MeshProxySettings.override_voxel_size(value: bool) -> None
unreal.MeshProxySettings.recalculate_normals(value: bool) -> None
unreal.MeshProxySettings.reuse_mesh_lightmap_u_vs(value: bool) -> None
unreal.MeshProxySettings.screen_size(value: int) -> None
unreal.MeshProxySettings.support_ray_tracing(value: bool) -> None
unreal.MeshProxySettings.unresolved_geometry_color(value: Color) -> None
unreal.MeshProxySettings.use_hard_angle_threshold(value: bool) -> None
unreal.MeshProxySettings.use_landscape_culling(value: bool) -> None
unreal.MeshProxySettings.voxel_size(value: float) -> None
```

## `unreal.MeshReductionSettings(StructBase)`

```python
unreal.MeshReductionSettings.__init__(percent_triangles: float = 0.000000, percent_vertices: float = 0.000000, max_deviation: float = 0.000000, pixel_error: float = 0.000000, welding_threshold: float = 0.000000, hard_angle_threshold: float = 0.000000, base_lod_model: int = 0, silhouette_importance: MeshFeatureImportance = MeshFeatureImportance.OFF, texture_importance: MeshFeatureImportance = MeshFeatureImportance.OFF, shading_importance: MeshFeatureImportance = MeshFeatureImportance.OFF, recalculate_normals: bool = False, generate_unique_lightmap_u_vs: bool = False, keep_symmetry: bool = False, visibility_aided: bool = False, cull_occluded: bool = False, termination_criterion: StaticMeshReductionTerimationCriterion = StaticMeshReductionTerimationCriterion.TRIANGLES, visibility_aggressiveness: MeshFeatureImportance = MeshFeatureImportance.OFF, vertex_color_importance: MeshFeatureImportance = MeshFeatureImportance.OFF) -> None
unreal.MeshReductionSettings.base_lod_model(value: int) -> None
unreal.MeshReductionSettings.cull_occluded(value: bool) -> None
unreal.MeshReductionSettings.generate_unique_lightmap_u_vs(value: bool) -> None
unreal.MeshReductionSettings.hard_angle_threshold(value: float) -> None
unreal.MeshReductionSettings.keep_symmetry(value: bool) -> None
unreal.MeshReductionSettings.max_deviation(value: float) -> None
unreal.MeshReductionSettings.percent_triangles(value: float) -> None
unreal.MeshReductionSettings.percent_vertices(value: float) -> None
unreal.MeshReductionSettings.pixel_error(value: float) -> None
unreal.MeshReductionSettings.recalculate_normals(value: bool) -> None
unreal.MeshReductionSettings.shading_importance(value: MeshFeatureImportance) -> None
unreal.MeshReductionSettings.silhouette_importance(value: MeshFeatureImportance) -> None
unreal.MeshReductionSettings.termination_criterion(value: StaticMeshReductionTerimationCriterion) -> None
unreal.MeshReductionSettings.texture_importance(value: MeshFeatureImportance) -> None
unreal.MeshReductionSettings.vertex_color_importance(value: MeshFeatureImportance) -> None
unreal.MeshReductionSettings.visibility_aggressiveness(value: MeshFeatureImportance) -> None
unreal.MeshReductionSettings.visibility_aided(value: bool) -> None
unreal.MeshReductionSettings.welding_threshold(value: float) -> None
```

## `unreal.MeterSettings(AudioSynesthesiaSettings)`

```python
unreal.MeterSettings.analysis_period() -> float
unreal.MeterSettings.clipping_threshold() -> float
unreal.MeterSettings.meter_attack_time() -> int
unreal.MeterSettings.meter_release_time() -> int
unreal.MeterSettings.peak_hold_time() -> int
unreal.MeterSettings.peak_mode() -> MeterPeakType
```

## `unreal.NavDataConfig(NavAgentProperties)`

```python
unreal.NavDataConfig.__init__(can_crouch: bool = False, can_jump: bool = False, can_walk: bool = False, can_swim: bool = False, can_fly: bool = False, agent_radius: float = 0.000000, agent_height: float = 0.000000, agent_step_height: float = 0.000000, nav_walking_search_height_scale: float = 0.000000, preferred_nav_data: SoftClassPath = [""], name: Name = "None", color: Color = [0, 0, 0, 0], default_query_extent: Vector = [0.000000, 0.000000, 0.000000], nav_data_class: Class = None) -> None
unreal.NavDataConfig.color(value: Color) -> None
unreal.NavDataConfig.default_query_extent() -> Vector
unreal.NavDataConfig.name(value: Name) -> None
unreal.NavDataConfig.nav_data_class(value: Class) -> None
unreal.NavDataConfig.navigation_data_class_name(value: Class) -> None
```

## `unreal.NavLinkGenerationJumpDownConfig(StructBase)`

```python
unreal.NavLinkGenerationJumpDownConfig.__init__() -> None
```

## `unreal.NavSystemConfigOverride(Actor)`

```python
unreal.NavSystemConfigOverride.load_on_client(value: bool) -> None
unreal.NavSystemConfigOverride.navigation_system_config() -> NavigationSystemConfig
unreal.NavSystemConfigOverride.override_policy() -> NavSystemOverridePolicy
```

## `unreal.OnGameUserSettingsUINeedsUpdate(MulticastDelegateBase)`

```python
unreal.OnGameUserSettingsUINeedsUpdate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnsetNRTSettings(AudioSynesthesiaNRTSettings)`

```python
unreal.OnsetNRTSettings.downmix_to_mono() -> bool
unreal.OnsetNRTSettings.granularity_in_seconds() -> float
unreal.OnsetNRTSettings.maximum_frequency() -> float
unreal.OnsetNRTSettings.minimum_frequency() -> float
unreal.OnsetNRTSettings.sensitivity() -> float
```

## `unreal.PBIKSolverSettings(StructBase)`

```python
unreal.PBIKSolverSettings.__init__(iterations: int = 0, sub_iterations: int = 0, mass_multiplier: float = 0.000000, allow_stretch: bool = False, root_behavior: PBIKRootBehavior = PBIKRootBehavior.PRE_PULL, pre_pull_root_settings: RootPrePullSettings = [0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000], global_pull_chain_alpha: float = 0.000000, max_angle: float = 0.000000, over_relaxation: float = 0.000000) -> None
unreal.PBIKSolverSettings.allow_stretch(value: bool) -> None
unreal.PBIKSolverSettings.global_pull_chain_alpha(value: float) -> None
unreal.PBIKSolverSettings.iterations(value: int) -> None
unreal.PBIKSolverSettings.mass_multiplier(value: float) -> None
unreal.PBIKSolverSettings.max_angle(value: float) -> None
unreal.PBIKSolverSettings.over_relaxation(value: float) -> None
unreal.PBIKSolverSettings.pre_pull_root_settings(value: RootPrePullSettings) -> None
unreal.PBIKSolverSettings.root_behavior(value: PBIKRootBehavior) -> None
unreal.PBIKSolverSettings.sub_iterations(value: int) -> None
```

## `unreal.PerPlatformSettings(StructBase)`

```python
unreal.PerPlatformSettings.__init__() -> None
```

## `unreal.PlateCropSettings(StructBase)`

```python
unreal.PlateCropSettings.__init__(aspect_ratio: float = 0.000000) -> None
unreal.PlateCropSettings.aspect_ratio(value: float) -> None
```

## `unreal.PropertyEditorTestBasicStruct(StructBase)`

```python
unreal.PropertyEditorTestBasicStruct.__init__() -> None
```

## `unreal.PropertyEditorTestEditCondition(StructBase)`

```python
unreal.PropertyEditorTestEditCondition.__init__() -> None
```

## `unreal.PropertyEditorTestInstancedStruct(StructBase)`

```python
unreal.PropertyEditorTestInstancedStruct.__init__() -> None
```

## `unreal.PropertyEditorTestSubStruct(StructBase)`

```python
unreal.PropertyEditorTestSubStruct.__init__() -> None
```

## `unreal.RadialBoxSettings(StructBase)`

```python
unreal.RadialBoxSettings.__init__() -> None
```

## `unreal.RetargetChainSettings(Object)`

```python
unreal.RetargetChainSettings.settings(value: TargetChainSettings) -> None
unreal.RetargetChainSettings.source_chain() -> Name
unreal.RetargetChainSettings.target_chain() -> Name
```

## `unreal.RetargetGlobalSettings(StructBase)`

```python
unreal.RetargetGlobalSettings.__init__(enable_root: bool = False, enable_fk: bool = False, enable_ik: bool = False, enable_post: bool = False, warping: bool = False, direction_source: WarpingDirectionSource = WarpingDirectionSource.GOALS, forward_direction: BasicAxis = BasicAxis.X, direction_chain: Name = "None", warp_forwards: float = 0.000000, sideways_offset: float = 0.000000, warp_splay: float = 0.000000) -> None
unreal.RetargetGlobalSettings.direction_chain(value: Name) -> None
unreal.RetargetGlobalSettings.direction_source(value: WarpingDirectionSource) -> None
unreal.RetargetGlobalSettings.enable_fk(value: bool) -> None
unreal.RetargetGlobalSettings.enable_ik(value: bool) -> None
unreal.RetargetGlobalSettings.enable_post(value: bool) -> None
unreal.RetargetGlobalSettings.enable_root(value: bool) -> None
unreal.RetargetGlobalSettings.forward_direction(value: BasicAxis) -> None
unreal.RetargetGlobalSettings.sideways_offset(value: float) -> None
unreal.RetargetGlobalSettings.warp_forwards(value: float) -> None
unreal.RetargetGlobalSettings.warp_splay(value: float) -> None
unreal.RetargetGlobalSettings.warping(value: bool) -> None
```

## `unreal.ReverbSettings(StructBase)`

```python
unreal.ReverbSettings.__init__(apply_reverb: bool = False, reverb_effect: ReverbEffect = None, reverb_plugin_effect: SoundEffectSubmixPreset = None, volume: float = 0.000000, fade_time: float = 0.000000) -> None
unreal.ReverbSettings.apply_reverb(value: bool) -> None
unreal.ReverbSettings.fade_time(value: float) -> None
unreal.ReverbSettings.reverb_effect(value: ReverbEffect) -> None
unreal.ReverbSettings.reverb_plugin_effect(value: SoundEffectSubmixPreset) -> None
unreal.ReverbSettings.volume(value: float) -> None
```

## `unreal.RigConnectorSettings(StructBase)`

```python
unreal.RigConnectorSettings.__init__(description: str = "", type: ConnectorType = ConnectorType.PRIMARY, optional: bool = False, rules: Array[RigConnectionRuleStash] = []) -> None
unreal.RigConnectorSettings.description(value: str) -> None
unreal.RigConnectorSettings.optional(value: bool) -> None
unreal.RigConnectorSettings.rules(value: Array[RigConnectionRuleStash]) -> None
unreal.RigConnectorSettings.type(value: ConnectorType) -> None
```

## `unreal.RigControlSettings(StructBase)`

```python
unreal.RigControlSettings.__init__(animation_type: RigControlAnimationType = RigControlAnimationType.ANIMATION_CONTROL, control_type: RigControlType = RigControlType.BOOL, display_name: Name = "None", primary_axis: RigControlAxis = RigControlAxis.X, limit_enabled: Array[RigControlLimitEnabled] = [], draw_limits: bool = False, minimum_value: RigControlValue = [], maximum_value: RigControlValue = [], shape_visible: bool = False, shape_visibility: RigControlVisibility = RigControlVisibility.USER_DEFINED, shape_name: Name = "None", shape_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], is_transient_control: bool = False, control_enum: Enum = None, customization: RigControlElementCustomization = [[], []], driven_controls: Array[RigElementKey] = [], group_with_parent_control: bool = False, restrict_space_switching: bool = False, filtered_channels: Array[RigControlTransformChannel] = [], preferred_rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ, use_preferred_rotation_order: bool = False) -> None
unreal.RigControlSettings.animatable(value: bool) -> None
unreal.RigControlSettings.animation_type(value: RigControlAnimationType) -> None
unreal.RigControlSettings.b_gizmo_enabled(value: bool) -> None
unreal.RigControlSettings.b_gizmo_visible(value: bool) -> None
unreal.RigControlSettings.control_enum() -> Enum
unreal.RigControlSettings.control_type(value: RigControlType) -> None
unreal.RigControlSettings.customization() -> RigControlElementCustomization
unreal.RigControlSettings.display_name(value: Name) -> None
unreal.RigControlSettings.draw_limits(value: bool) -> None
unreal.RigControlSettings.driven_controls() -> Array[RigElementKey]
unreal.RigControlSettings.filtered_channels() -> Array[RigControlTransformChannel]
unreal.RigControlSettings.gizmo_color(value: LinearColor) -> None
unreal.RigControlSettings.gizmo_name(value: Name) -> None
unreal.RigControlSettings.group_with_parent_control() -> bool
unreal.RigControlSettings.is_transient_control(value: bool) -> None
unreal.RigControlSettings.limit_enabled(value: Array[RigControlLimitEnabled]) -> None
unreal.RigControlSettings.maximum_value(value: RigControlValue) -> None
unreal.RigControlSettings.minimum_value(value: RigControlValue) -> None
unreal.RigControlSettings.preferred_rotation_order() -> EulerRotationOrder
unreal.RigControlSettings.primary_axis(value: RigControlAxis) -> None
unreal.RigControlSettings.restrict_space_switching() -> bool
unreal.RigControlSettings.shape_color(value: LinearColor) -> None
unreal.RigControlSettings.shape_enabled(value: bool) -> None
unreal.RigControlSettings.shape_name(value: Name) -> None
unreal.RigControlSettings.shape_visibility(value: RigControlVisibility) -> None
unreal.RigControlSettings.shape_visible(value: bool) -> None
unreal.RigControlSettings.use_preferred_rotation_order() -> bool
```

## `unreal.RigHierarchySettings(StructBase)`

```python
unreal.RigHierarchySettings.__init__() -> None
```

## `unreal.RigMirrorSettings(RigVMMirrorSettings)`

```python
unreal.RigMirrorSettings.__init__(mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, search_string: str = "", replace_string: str = "") -> None
```

## `unreal.RigModuleSettings(StructBase)`

```python
unreal.RigModuleSettings.__init__(identifier: RigModuleIdentifier = ["", "Module"], icon: SoftObjectPath = [""], category: str = "", keywords: str = "", description: str = "", exposed_connectors: Array[RigModuleConnector] = []) -> None
unreal.RigModuleSettings.category(value: str) -> None
unreal.RigModuleSettings.description(value: str) -> None
unreal.RigModuleSettings.exposed_connectors() -> Array[RigModuleConnector]
unreal.RigModuleSettings.icon(value: SoftObjectPath) -> None
unreal.RigModuleSettings.identifier(value: RigModuleIdentifier) -> None
unreal.RigModuleSettings.keywords(value: str) -> None
```

## `unreal.RigSpacePickerBakeSettings(StructBase)`

```python
unreal.RigSpacePickerBakeSettings.__init__(target_space: RigElementKey = [RigElementType.NONE, "None"], settings: BakingAnimationKeySettings = [[0], [100], BakingKeySettings.KEYS_ONLY, 1, False, 0.001000]) -> None
unreal.RigSpacePickerBakeSettings.end_frame(value: FrameNumber) -> None
unreal.RigSpacePickerBakeSettings.reduce_keys(value: bool) -> None
unreal.RigSpacePickerBakeSettings.settings(value: BakingAnimationKeySettings) -> None
unreal.RigSpacePickerBakeSettings.start_frame(value: FrameNumber) -> None
unreal.RigSpacePickerBakeSettings.target_space(value: RigElementKey) -> None
unreal.RigSpacePickerBakeSettings.tolerance(value: float) -> None
```

## `unreal.RigUnit_HierarchyAddControlFloat_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlFloat_LimitSettings.__init__(limit: RigControlLimitEnabled = [False, False], min_value: float = 0.000000, max_value: float = 0.000000, draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlFloat_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlFloat_LimitSettings.limit(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlFloat_LimitSettings.max_value(value: float) -> None
unreal.RigUnit_HierarchyAddControlFloat_LimitSettings.min_value(value: float) -> None
```

## `unreal.RigUnit_HierarchyAddControlFloat_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlFloat_Settings.__init__(display_name: Name = "None", primary_axis: RigControlAxis = RigControlAxis.X, is_scale: bool = False, limits: RigUnit_HierarchyAddControlFloat_LimitSettings = [[True, True], 0.000000, 100.000000, True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION]) -> None
unreal.RigUnit_HierarchyAddControlFloat_Settings.is_scale(value: bool) -> None
unreal.RigUnit_HierarchyAddControlFloat_Settings.limits(value: RigUnit_HierarchyAddControlFloat_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlFloat_Settings.primary_axis(value: RigControlAxis) -> None
unreal.RigUnit_HierarchyAddControlFloat_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlFloat_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_HierarchyAddControlInteger_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.__init__(limit: RigControlLimitEnabled = [False, False], min_value: int = 0, max_value: int = 0, draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.limit(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.max_value(value: int) -> None
unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.min_value(value: int) -> None
```

## `unreal.RigUnit_HierarchyAddControlInteger_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlInteger_Settings.__init__(display_name: Name = "None", primary_axis: RigControlAxis = RigControlAxis.X, control_enum: Enum = None, limits: RigUnit_HierarchyAddControlInteger_LimitSettings = [[True, True], 0, 100, True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION]) -> None
unreal.RigUnit_HierarchyAddControlInteger_Settings.control_enum(value: Enum) -> None
unreal.RigUnit_HierarchyAddControlInteger_Settings.limits(value: RigUnit_HierarchyAddControlInteger_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlInteger_Settings.primary_axis(value: RigControlAxis) -> None
unreal.RigUnit_HierarchyAddControlInteger_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlInteger_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_HierarchyAddControlRotator_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.__init__(limit_pitch: RigControlLimitEnabled = [False, False], limit_yaw: RigControlLimitEnabled = [False, False], limit_roll: RigControlLimitEnabled = [False, False], min_value: Rotator = [0.000000, 0.000000, 0.000000], max_value: Rotator = [0.000000, 0.000000, 0.000000], draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_pitch(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_roll(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_yaw(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.max_value(value: Rotator) -> None
unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.min_value(value: Rotator) -> None
```

## `unreal.RigUnit_HierarchyAddControlRotator_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlRotator_Settings.__init__(display_name: Name = "None", initial_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, limits: RigUnit_HierarchyAddControlRotator_LimitSettings = [[False, False], [False, False], [False, False], [-180.000000, -180.000000, -180.000000], [180.000000, 180.000000, 180.000000], True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION], filtered_channels: Array[RigControlTransformChannel] = []) -> None
unreal.RigUnit_HierarchyAddControlRotator_Settings.filtered_channels(value: Array[RigControlTransformChannel]) -> None
unreal.RigUnit_HierarchyAddControlRotator_Settings.initial_space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchyAddControlRotator_Settings.limits(value: RigUnit_HierarchyAddControlRotator_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlRotator_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlRotator_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.__init__(limit_x: RigControlLimitEnabled = [False, False], limit_y: RigControlLimitEnabled = [False, False], min_value: Vector2D = [0.000000, 0.000000], max_value: Vector2D = [0.000000, 0.000000], draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.limit_y(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.max_value(value: Vector2D) -> None
unreal.RigUnit_HierarchyAddControlVector2D_LimitSettings.min_value(value: Vector2D) -> None
```

## `unreal.RigUnit_HierarchyAddControlVector2D_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlVector2D_Settings.__init__(display_name: Name = "None", primary_axis: RigControlAxis = RigControlAxis.X, limits: RigUnit_HierarchyAddControlVector2D_LimitSettings = [[True, True], [True, True], [0.000000, 0.000000], [1.000000, 1.000000], True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION], filtered_channels: Array[RigControlTransformChannel] = []) -> None
unreal.RigUnit_HierarchyAddControlVector2D_Settings.filtered_channels(value: Array[RigControlTransformChannel]) -> None
unreal.RigUnit_HierarchyAddControlVector2D_Settings.limits(value: RigUnit_HierarchyAddControlVector2D_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlVector2D_Settings.primary_axis(value: RigControlAxis) -> None
unreal.RigUnit_HierarchyAddControlVector2D_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlVector2D_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_HierarchyAddControlVector_LimitSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.__init__(limit_x: RigControlLimitEnabled = [False, False], limit_y: RigControlLimitEnabled = [False, False], limit_z: RigControlLimitEnabled = [False, False], min_value: Vector = [0.000000, 0.000000, 0.000000], max_value: Vector = [0.000000, 0.000000, 0.000000], draw_limits: bool = False) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.draw_limits(value: bool) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_x(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_y(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_z(value: RigControlLimitEnabled) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.max_value(value: Vector) -> None
unreal.RigUnit_HierarchyAddControlVector_LimitSettings.min_value(value: Vector) -> None
```

## `unreal.RigUnit_HierarchyAddControlVector_Settings(RigUnit_HierarchyAddControl_Settings)`

```python
unreal.RigUnit_HierarchyAddControlVector_Settings.__init__(display_name: Name = "None", initial_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE, is_position: bool = False, limits: RigUnit_HierarchyAddControlVector_LimitSettings = [[False, False], [False, False], [False, False], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000], True], shape: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]], proxy: RigUnit_HierarchyAddControl_ProxySettings = [False, [], RigControlVisibility.BASED_ON_SELECTION], filtered_channels: Array[RigControlTransformChannel] = []) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.filtered_channels(value: Array[RigControlTransformChannel]) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.initial_space(value: RigVMTransformSpace) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.is_position(value: bool) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.limits(value: RigUnit_HierarchyAddControlVector_LimitSettings) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.proxy(value: RigUnit_HierarchyAddControl_ProxySettings) -> None
unreal.RigUnit_HierarchyAddControlVector_Settings.shape(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_HierarchyAddControl_ProxySettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControl_ProxySettings.__init__(is_proxy: bool = False, driven_controls: Array[RigElementKey] = [], shape_visibility: RigControlVisibility = RigControlVisibility.USER_DEFINED) -> None
unreal.RigUnit_HierarchyAddControl_ProxySettings.driven_controls(value: Array[RigElementKey]) -> None
unreal.RigUnit_HierarchyAddControl_ProxySettings.is_proxy(value: bool) -> None
unreal.RigUnit_HierarchyAddControl_ProxySettings.shape_visibility(value: RigControlVisibility) -> None
```

## `unreal.RigUnit_HierarchyAddControl_Settings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControl_Settings.__init__(display_name: Name = "None") -> None
unreal.RigUnit_HierarchyAddControl_Settings.display_name(value: Name) -> None
```

## `unreal.RigUnit_HierarchyAddControl_ShapeSettings(StructBase)`

```python
unreal.RigUnit_HierarchyAddControl_ShapeSettings.__init__(visible: bool = False, name: Name = "None", color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_HierarchyAddControl_ShapeSettings.color(value: LinearColor) -> None
unreal.RigUnit_HierarchyAddControl_ShapeSettings.name(value: Name) -> None
unreal.RigUnit_HierarchyAddControl_ShapeSettings.transform(value: Transform) -> None
unreal.RigUnit_HierarchyAddControl_ShapeSettings.visible(value: bool) -> None
```

## `unreal.RigUnit_HierarchyGetShapeSettings(RigUnit_DynamicHierarchyBase)`

```python
unreal.RigUnit_HierarchyGetShapeSettings.__init__(item: RigElementKey = [RigElementType.NONE, "None"], settings: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_HierarchyGetShapeSettings.item(value: RigElementKey) -> None
unreal.RigUnit_HierarchyGetShapeSettings.settings() -> RigUnit_HierarchyAddControl_ShapeSettings
```

## `unreal.RigUnit_HierarchySetShapeSettings(RigUnit_DynamicHierarchyBaseMutable)`

```python
unreal.RigUnit_HierarchySetShapeSettings.__init__(execute_context: ControlRigExecuteContext = [], item: RigElementKey = [RigElementType.NONE, "None"], settings: RigUnit_HierarchyAddControl_ShapeSettings = [True, "Default", [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_HierarchySetShapeSettings.item(value: RigElementKey) -> None
unreal.RigUnit_HierarchySetShapeSettings.settings(value: RigUnit_HierarchyAddControl_ShapeSettings) -> None
```

## `unreal.RigUnit_PointSimulation_DebugSettings(StructBase)`

```python
unreal.RigUnit_PointSimulation_DebugSettings.__init__(enabled: bool = False, scale: float = 0.000000, collision_scale: float = 0.000000, draw_points_as_spheres: bool = False, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_PointSimulation_DebugSettings.collision_scale(value: float) -> None
unreal.RigUnit_PointSimulation_DebugSettings.color(value: LinearColor) -> None
unreal.RigUnit_PointSimulation_DebugSettings.draw_points_as_spheres(value: bool) -> None
unreal.RigUnit_PointSimulation_DebugSettings.enabled(value: bool) -> None
unreal.RigUnit_PointSimulation_DebugSettings.scale(value: float) -> None
unreal.RigUnit_PointSimulation_DebugSettings.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_SpringIK_DebugSettings(StructBase)`

```python
unreal.RigUnit_SpringIK_DebugSettings.__init__(enabled: bool = False, scale: float = 0.000000, color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_SpringIK_DebugSettings.color(value: LinearColor) -> None
unreal.RigUnit_SpringIK_DebugSettings.enabled(value: bool) -> None
unreal.RigUnit_SpringIK_DebugSettings.scale(value: float) -> None
unreal.RigUnit_SpringIK_DebugSettings.world_offset(value: Transform) -> None
```

## `unreal.RigVMCompileSettings(StructBase)`

```python
unreal.RigVMCompileSettings.__init__(surpress_info_messages: bool = False, surpress_warnings: bool = False, surpress_errors: bool = False, enable_pin_watches: bool = False, ast_settings: RigVMParserASTSettings = [True]) -> None
unreal.RigVMCompileSettings.ast_settings(value: RigVMParserASTSettings) -> None
unreal.RigVMCompileSettings.enable_pin_watches(value: bool) -> None
unreal.RigVMCompileSettings.surpress_errors(value: bool) -> None
unreal.RigVMCompileSettings.surpress_info_messages(value: bool) -> None
unreal.RigVMCompileSettings.surpress_warnings(value: bool) -> None
```

## `unreal.RigVMEditorMenuContext(Object)`

```python
unreal.RigVMEditorMenuContext.get_graph_menu_context() -> RigVMEditorGraphMenuContext
unreal.RigVMEditorMenuContext.get_rig_vm_blueprint() -> RigVMBlueprint
unreal.RigVMEditorMenuContext.get_rig_vm_host() -> RigVMHost
unreal.RigVMEditorMenuContext.is_alt_down() -> bool
```

## `unreal.RigVMMirrorSettings(StructBase)`

```python
unreal.RigVMMirrorSettings.__init__(mirror_axis: AxisType = AxisType.NONE, axis_to_flip: AxisType = AxisType.NONE, search_string: str = "", replace_string: str = "") -> None
unreal.RigVMMirrorSettings.axis_to_flip(value: AxisType) -> None
unreal.RigVMMirrorSettings.mirror_axis(value: AxisType) -> None
unreal.RigVMMirrorSettings.replace_string(value: str) -> None
unreal.RigVMMirrorSettings.search_string(value: str) -> None
```

## `unreal.RigVMParserASTSettings(StructBase)`

```python
unreal.RigVMParserASTSettings.__init__(setup_traits: bool = False) -> None
unreal.RigVMParserASTSettings.setup_traits(value: bool) -> None
```

## `unreal.RigVMProjectSettings(DeveloperSettings)`

```python
unreal.RigVMProjectSettings.get_tag(tag_name: Name) -> RigVMTag
```

## `unreal.RigVMPythonSettings(StructBase)`

```python
unreal.RigVMPythonSettings.__init__() -> None
```

## `unreal.RigVMRuntimeSettings(StructBase)`

```python
unreal.RigVMRuntimeSettings.__init__() -> None
```

## `unreal.RigVMTrait_OptimusDeformerSettings(RigVMTrait)`

```python
unreal.RigVMTrait_OptimusDeformerSettings.__init__(execution_phase: OptimusDeformerExecutionPhase = OptimusDeformerExecutionPhase.AFTER_DEFAULT_DEFORMER, execution_group: int = 0, deform_child_components: bool = False, exclude_child_components_with_tag: Name = "None") -> None
unreal.RigVMTrait_OptimusDeformerSettings.deform_child_components(value: bool) -> None
unreal.RigVMTrait_OptimusDeformerSettings.exclude_child_components_with_tag(value: Name) -> None
unreal.RigVMTrait_OptimusDeformerSettings.execution_group(value: int) -> None
unreal.RigVMTrait_OptimusDeformerSettings.execution_phase(value: OptimusDeformerExecutionPhase) -> None
```

## `unreal.RootPrePullSettings(StructBase)`

```python
unreal.RootPrePullSettings.__init__(rotation_alpha: float = 0.000000, rotation_alpha_x: float = 0.000000, rotation_alpha_y: float = 0.000000, rotation_alpha_z: float = 0.000000, position_alpha: float = 0.000000, position_alpha_x: float = 0.000000, position_alpha_y: float = 0.000000, position_alpha_z: float = 0.000000) -> None
unreal.RootPrePullSettings.position_alpha(value: float) -> None
unreal.RootPrePullSettings.position_alpha_x(value: float) -> None
unreal.RootPrePullSettings.position_alpha_y(value: float) -> None
unreal.RootPrePullSettings.position_alpha_z(value: float) -> None
unreal.RootPrePullSettings.rotation_alpha(value: float) -> None
unreal.RootPrePullSettings.rotation_alpha_x(value: float) -> None
unreal.RootPrePullSettings.rotation_alpha_y(value: float) -> None
unreal.RootPrePullSettings.rotation_alpha_z(value: float) -> None
```

## `unreal.ScopedEditorTransaction(object)`

```python
unreal.ScopedEditorTransaction.__init__(desc: Union[Text, str]) -> None
unreal.ScopedEditorTransaction.cancel() -> None
```

## `unreal.SimSpaceSettings(StructBase)`

```python
unreal.SimSpaceSettings.__init__(world_alpha: float = 0.000000, velocity_scale_z: float = 0.000000, max_linear_velocity: float = 0.000000, max_angular_velocity: float = 0.000000, max_linear_acceleration: float = 0.000000, max_angular_acceleration: float = 0.000000, external_linear_drag_v: Vector = [0.000000, 0.000000, 0.000000], external_linear_velocity: Vector = [0.000000, 0.000000, 0.000000], external_angular_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.SimSpaceSettings.external_angular_velocity(value: Vector) -> None
unreal.SimSpaceSettings.external_linear_drag(value: float) -> None
unreal.SimSpaceSettings.external_linear_drag_v(value: Vector) -> None
unreal.SimSpaceSettings.external_linear_velocity(value: Vector) -> None
unreal.SimSpaceSettings.master_alpha(value: float) -> None
unreal.SimSpaceSettings.max_angular_acceleration(value: float) -> None
unreal.SimSpaceSettings.max_angular_velocity(value: float) -> None
unreal.SimSpaceSettings.max_linear_acceleration(value: float) -> None
unreal.SimSpaceSettings.max_linear_velocity(value: float) -> None
unreal.SimSpaceSettings.velocity_scale_z(value: float) -> None
unreal.SimSpaceSettings.world_alpha(value: float) -> None
```

## `unreal.SkyCreatorBackgroundCloudSettings(StructBase)`

```python
unreal.SkyCreatorBackgroundCloudSettings.__init__(background_clouds_intensity: float = 0.000000, background_clouds_color_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], background_clouds_layer_a: float = 0.000000, background_clouds_layer_b: float = 0.000000, background_clouds_layer_c: float = 0.000000, background_clouds_lightning_phase: float = 0.000000) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_color_tint(value: LinearColor) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_intensity(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_a(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_b(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_c(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings.background_clouds_lightning_phase(value: float) -> None
```

## `unreal.SkyCreatorBackgroundCloudSettings_51(StructBase)`

```python
unreal.SkyCreatorBackgroundCloudSettings_51.__init__(use_background_clouds_intensity: bool = False, background_clouds_intensity: float = 0.000000, background_clouds_intensity_curve: CurveFloat = None, use_background_clouds_color_tint: bool = False, background_clouds_color_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], background_clouds_color_tint_curve: CurveLinearColor = None, use_background_clouds_layer_a: bool = False, background_clouds_layer_a: float = 0.000000, background_clouds_layer_a_curve: CurveFloat = None, use_background_clouds_layer_b: bool = False, background_clouds_layer_b: float = 0.000000, background_clouds_layer_b_curve: CurveFloat = None, use_background_clouds_layer_c: bool = False, background_clouds_layer_c: float = 0.000000, background_clouds_layer_c_curve: CurveFloat = None, use_background_clouds_lightning_phase: bool = False, background_clouds_lightning_phase: float = 0.000000, background_clouds_lightning_phase_curve: CurveFloat = None) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint(value: LinearColor) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a_curve(value: CurveFloat) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b_curve(value: CurveFloat) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c_curve(value: CurveFloat) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase(value: float) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase_curve(value: CurveFloat) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_color_tint(value: bool) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_intensity(value: bool) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_a(value: bool) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_b(value: bool) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_c(value: bool) -> None
unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_lightning_phase(value: bool) -> None
```

## `unreal.SkyCreatorExponentialHeightFogSettings(StructBase)`

```python
unreal.SkyCreatorExponentialHeightFogSettings.__init__(fog_density: float = 0.000000, fog_height_falloff: float = 0.000000, fog_inscattering_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], fog_start_distance: float = 0.000000, second_fog_density: float = 0.000000, second_fog_height_falloff: float = 0.000000, directional_inscattering_exponent: float = 0.000000, directional_inscattering_start_distance: float = 0.000000, directional_inscattering_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], volumetric_fog_scattering_distribution: float = 0.000000, volumetric_fog_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], volumetric_fog_emissive: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], volumetric_fog_extinction_scale: float = 0.000000) -> None
unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_color(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_exponent(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_start_distance(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.fog_density(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.fog_height_falloff(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.fog_inscattering_color(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings.fog_start_distance(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.second_fog_density(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.second_fog_height_falloff(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_albedo(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_emissive(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_extinction_scale(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_scattering_distribution(value: float) -> None
```

## `unreal.SkyCreatorExponentialHeightFogSettings_51(StructBase)`

```python
unreal.SkyCreatorExponentialHeightFogSettings_51.__init__(use_fog_density: bool = False, fog_density: float = 0.000000, fog_density_curve: CurveFloat = None, use_fog_height_falloff: bool = False, fog_height_falloff: float = 0.000000, fog_height_falloff_curve: CurveFloat = None, use_fog_inscattering_color: bool = False, fog_inscattering_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], fog_inscattering_color_curve: CurveLinearColor = None, use_fog_start_distance: bool = False, fog_start_distance: float = 0.000000, fog_start_distance_curve: CurveFloat = None, use_second_fog_density: bool = False, second_fog_density: float = 0.000000, second_fog_density_curve: CurveFloat = None, use_second_fog_height_falloff: bool = False, second_fog_height_falloff: float = 0.000000, second_fog_height_falloff_curve: CurveFloat = None, use_directional_inscattering_exponent: bool = False, directional_inscattering_exponent: float = 0.000000, directional_inscattering_exponent_curve: CurveFloat = None, use_directional_inscattering_start_distance: bool = False, directional_inscattering_start_distance: float = 0.000000, directional_inscattering_start_distance_curve: CurveFloat = None, use_directional_inscattering_color: bool = False, directional_inscattering_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], directional_inscattering_color_curve: CurveLinearColor = None, use_volumetric_fog_scattering_distribution: bool = False, volumetric_fog_scattering_distribution: float = 0.000000, volumetric_fog_scattering_distribution_curve: CurveFloat = None, use_volumetric_fog_albedo: bool = False, volumetric_fog_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], volumetric_fog_albedo_curve: CurveLinearColor = None, use_volumetric_fog_emissive: bool = False, volumetric_fog_emissive: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], volumetric_fog_emissive_curve: CurveLinearColor = None, use_volumetric_fog_extinction_scale: bool = False, volumetric_fog_extinction_scale: float = 0.000000, volumetric_fog_extinction_scale_curve: CurveFloat = None) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_color(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_exponent(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_exponent_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_start_distance(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.directional_inscattering_start_distance_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_density(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_density_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_height_falloff(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_height_falloff_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_inscattering_color(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_inscattering_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_start_distance(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.fog_start_distance_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.second_fog_density(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.second_fog_density_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.second_fog_height_falloff(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.second_fog_height_falloff_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_directional_inscattering_color(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_directional_inscattering_exponent(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_directional_inscattering_start_distance(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_fog_density(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_fog_height_falloff(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_fog_inscattering_color(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_fog_start_distance(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_second_fog_density(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_second_fog_height_falloff(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_volumetric_fog_albedo(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_volumetric_fog_emissive(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_volumetric_fog_extinction_scale(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.use_volumetric_fog_scattering_distribution(value: bool) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_albedo(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_albedo_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_emissive(value: LinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_emissive_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_extinction_scale(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_extinction_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_scattering_distribution(value: float) -> None
unreal.SkyCreatorExponentialHeightFogSettings_51.volumetric_fog_scattering_distribution_curve(value: CurveFloat) -> None
```

## `unreal.SkyCreatorExposureSettings_51(StructBase)`

```python
unreal.SkyCreatorExposureSettings_51.__init__(use_exposure_priority: bool = False, exposure_priority: float = 0.000000, exposure_priority_curve: CurveFloat = None, use_auto_exposure_bias_override: bool = False, use_auto_exposure_bias: bool = False, auto_exposure_bias: float = 0.000000, auto_exposure_bias_curve: CurveFloat = None, use_min_ev100_override: bool = False, use_min_ev100: bool = False, min_ev100: float = 0.000000, min_ev100_curve: CurveFloat = None, use_max_ev100_override: bool = False, use_max_ev100: bool = False, max_ev100: float = 0.000000, max_ev100_curve: CurveFloat = None, use_highlight_contrast_scale_override: bool = False, use_highlight_contrast_scale: bool = False, highlight_contrast_scale: float = 0.000000, highlight_contrast_scale_curve: CurveFloat = None, use_shadow_contrast_scale_override: bool = False, use_shadow_contrast_scale: bool = False, shadow_contrast_scale: float = 0.000000, shadow_contrast_scale_curve: CurveFloat = None, use_detail_strength_override: bool = False, use_detail_strength: bool = False, detail_strength: float = 0.000000, detail_strength_curve: CurveFloat = None, shadow_contrast_scale_blend_curve: CurveFloat = None, use_bloom_intensity_override: bool = False, use_bloom_intensity: bool = False, bloom_intensity: float = 0.000000, bloom_intensity_curve: CurveFloat = None, use_bloom_threshold_override: bool = False, use_bloom_threshold: bool = False, bloom_threshold: float = 0.000000, bloom_threshold_curve: CurveFloat = None) -> None
unreal.SkyCreatorExposureSettings_51.auto_exposure_bias(value: float) -> None
unreal.SkyCreatorExposureSettings_51.auto_exposure_bias_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.bloom_intensity(value: float) -> None
unreal.SkyCreatorExposureSettings_51.bloom_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.bloom_threshold(value: float) -> None
unreal.SkyCreatorExposureSettings_51.bloom_threshold_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.detail_strength(value: float) -> None
unreal.SkyCreatorExposureSettings_51.detail_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.exposure_priority(value: float) -> None
unreal.SkyCreatorExposureSettings_51.exposure_priority_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale(value: float) -> None
unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.max_ev100(value: float) -> None
unreal.SkyCreatorExposureSettings_51.max_ev100_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.min_ev100(value: float) -> None
unreal.SkyCreatorExposureSettings_51.min_ev100_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale(value: float) -> None
unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_blend_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_bloom_intensity(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_bloom_intensity_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_bloom_threshold(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_bloom_threshold_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_detail_strength(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_detail_strength_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_exposure_priority(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_max_ev100(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_max_ev100_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_min_ev100(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_min_ev100_override(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale(value: bool) -> None
unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale_override(value: bool) -> None
```

## `unreal.SkyCreatorSkyAtmosphereSettings(StructBase)`

```python
unreal.SkyCreatorSkyAtmosphereSettings.__init__(rayleigh_scattering_scale: float = 0.000000, rayleigh_scattering: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rayleigh_exponential_distribution: float = 0.000000, mie_scattering_scale: float = 0.000000, mie_scattering: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], mie_absorption_scale: float = 0.000000, mie_absorption: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], mie_anisotropy: float = 0.000000, mie_exponential_distribution: float = 0.000000, absorption_scale: float = 0.000000, absorption: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], sky_luminance_factor: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], ground_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], height_fog_contribution: float = 0.000000) -> None
unreal.SkyCreatorSkyAtmosphereSettings.absorption(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings.absorption_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.ground_albedo(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings.height_fog_contribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_anisotropy(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_exponential_distribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_exponential_distribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings.sky_luminance_factor(value: LinearColor) -> None
```

## `unreal.SkyCreatorSkyAtmosphereSettings_51(StructBase)`

```python
unreal.SkyCreatorSkyAtmosphereSettings_51.__init__(use_rayleigh_scattering_scale: bool = False, rayleigh_scattering_scale: float = 0.000000, rayleigh_scattering_scale_curve: CurveFloat = None, use_rayleigh_scattering: bool = False, rayleigh_scattering: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rayleigh_scattering_curve: CurveLinearColor = None, use_rayleigh_exponential_distribution: bool = False, rayleigh_exponential_distribution: float = 0.000000, rayleigh_exponential_distribution_curve: CurveFloat = None, use_mie_scattering_scale: bool = False, mie_scattering_scale: float = 0.000000, mie_scattering_scale_curve: CurveFloat = None, use_mie_scattering: bool = False, mie_scattering: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], mie_scattering_curve: CurveLinearColor = None, use_mie_absorption_scale: bool = False, mie_absorption_scale: float = 0.000000, mie_absorption_scale_curve: CurveFloat = None, use_mie_absorption: bool = False, mie_absorption: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], mie_absorption_curve: CurveLinearColor = None, use_mie_anisotropy: bool = False, mie_anisotropy: float = 0.000000, mie_anisotropy_curve: CurveFloat = None, use_mie_exponential_distribution: bool = False, mie_exponential_distribution: float = 0.000000, mie_exponential_distribution_curve: CurveFloat = None, use_absorption_scale: bool = False, absorption_scale: float = 0.000000, absorption_scale_curve: CurveFloat = None, use_absorption: bool = False, absorption: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], absorption_curve: CurveLinearColor = None, use_sky_luminance_factor: bool = False, sky_luminance_factor: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], sky_luminance_factor_curve: CurveLinearColor = None, use_ground_albedo: bool = False, ground_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], ground_albedo_curve: CurveLinearColor = None, use_height_fog_contribution: bool = False, height_fog_contribution: float = 0.000000, height_fog_contribution_curve: CurveFloat = None) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.absorption(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale(value: float) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor(value: LinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption_scale(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_ground_albedo(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_height_fog_contribution(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption_scale(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_anisotropy(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_exponential_distribution(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering_scale(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_exponential_distribution(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering_scale(value: bool) -> None
unreal.SkyCreatorSkyAtmosphereSettings_51.use_sky_luminance_factor(value: bool) -> None
```

## `unreal.SkyCreatorStarMapSettings(StructBase)`

```python
unreal.SkyCreatorStarMapSettings.__init__(star_map_intensity: float = 0.000000, star_map_color_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], star_map_twinkle_intensity: float = 0.000000, star_map_twinkle_saturation: float = 0.000000, star_map_twinkle_speed: float = 0.000000, star_map_horizon_threshold: float = 0.000000, star_map_atmosphere_threshold: float = 0.000000, night_horizon_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], night_zenith_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.SkyCreatorStarMapSettings.night_horizon_color(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings.night_zenith_color(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings.star_map_atmosphere_threshold(value: float) -> None
unreal.SkyCreatorStarMapSettings.star_map_color_tint(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings.star_map_horizon_threshold(value: float) -> None
unreal.SkyCreatorStarMapSettings.star_map_intensity(value: float) -> None
unreal.SkyCreatorStarMapSettings.star_map_twinkle_intensity(value: float) -> None
unreal.SkyCreatorStarMapSettings.star_map_twinkle_saturation(value: float) -> None
unreal.SkyCreatorStarMapSettings.star_map_twinkle_speed(value: float) -> None
```

## `unreal.SkyCreatorStarMapSettings_51(StructBase)`

```python
unreal.SkyCreatorStarMapSettings_51.__init__(use_star_map_intensity: bool = False, star_map_intensity: float = 0.000000, star_map_intensity_curve: CurveFloat = None, use_star_map_color_tint: bool = False, star_map_color_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], star_map_color_tint_curve: CurveLinearColor = None, use_star_map_twinkle_intensity: bool = False, star_map_twinkle_intensity: float = 0.000000, star_map_twinkle_intensity_curve: CurveFloat = None, use_star_map_twinkle_saturation: bool = False, star_map_twinkle_saturation: float = 0.000000, star_map_twinkle_saturation_curve: CurveFloat = None, use_star_map_twinkle_speed: bool = False, star_map_twinkle_speed: float = 0.000000, star_map_twinkle_speed_curve: CurveFloat = None, use_star_map_horizon_threshold: bool = False, star_map_horizon_threshold: float = 0.000000, star_map_horizon_threshold_curve: CurveFloat = None, use_star_map_atmosphere_threshold: bool = False, star_map_atmosphere_threshold: float = 0.000000, star_map_atmosphere_threshold_curve: CurveFloat = None, use_night_horizon_color: bool = False, night_horizon_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], night_horizon_color_curve: CurveLinearColor = None, use_night_zenith_color: bool = False, night_zenith_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], night_zenith_color_curve: CurveLinearColor = None) -> None
unreal.SkyCreatorStarMapSettings_51.night_horizon_color(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.night_horizon_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.night_zenith_color(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.night_zenith_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_color_tint(value: LinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_color_tint_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_intensity(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed(value: float) -> None
unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed_curve(value: CurveFloat) -> None
unreal.SkyCreatorStarMapSettings_51.use_night_horizon_color(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_night_zenith_color(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_atmosphere_threshold(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_color_tint(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_horizon_threshold(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_intensity(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_intensity(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_saturation(value: bool) -> None
unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_speed(value: bool) -> None
```

## `unreal.SkyCreatorVolumetricCloudSettings(StructBase)`

```python
unreal.SkyCreatorVolumetricCloudSettings.__init__(stratus_coverage: float = 0.000000, stratus_coverage_variation: float = 0.000000, stratus_height_variation: float = 0.000000, stratocumulus_coverage: float = 0.000000, stratocumulus_coverage_variation: float = 0.000000, stratocumulus_height_variation: float = 0.000000, cumulus_coverage: float = 0.000000, cumulus_coverage_variation: float = 0.000000, cumulus_height_variation: float = 0.000000, cumulonimbus_coverage: float = 0.000000, cumulonimbus_anvil: float = 0.000000, cumulonimbus_height_variation: float = 0.000000, density_bottom: float = 0.000000, density_middle: float = 0.000000, density_top: float = 0.000000, albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], ground_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], beers_powder_intensity: float = 0.000000, beers_powder_depth: float = 0.000000, bottom_occlusion: float = 0.000000, bottom_occlusion_height: float = 0.000000, night_emissive: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], phase_g: float = 0.000000, phase_g2: float = 0.000000, phase_blend: float = 0.000000, multi_scattering_contribution: float = 0.000000, multi_scattering_occlusion: float = 0.000000, multi_scattering_eccentricity: float = 0.000000, noise_shape_intensity_a: float = 0.000000, noise_shape_intensity_b: float = 0.000000, noise_shape_intensity_c: float = 0.000000, noise_shape_intensity_d: float = 0.000000, turbulence_intensity: float = 0.000000) -> None
unreal.SkyCreatorVolumetricCloudSettings.albedo(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings.beers_powder_depth(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.beers_powder_intensity(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion_height(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_anvil(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.cumulus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.density_bottom(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.density_middle(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.density_top(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.ground_albedo(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_contribution(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_eccentricity(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_occlusion(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.night_emissive(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_a(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_b(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_c(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_d(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.phase_blend(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.phase_g(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.phase_g2(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.stratus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings.turbulence_intensity(value: float) -> None
```

## `unreal.SkyCreatorVolumetricCloudSettings_51(StructBase)`

```python
unreal.SkyCreatorVolumetricCloudSettings_51.__init__(use_stratus_coverage: bool = False, stratus_coverage: float = 0.000000, stratus_coverage_curve: CurveFloat = None, use_stratus_coverage_variation: bool = False, stratus_coverage_variation: float = 0.000000, stratus_coverage_variation_curve: CurveFloat = None, use_stratus_height_variation: bool = False, stratus_height_variation: float = 0.000000, stratus_height_variation_curve: CurveFloat = None, use_stratocumulus_coverage: bool = False, stratocumulus_coverage: float = 0.000000, stratocumulus_coverage_curve: CurveFloat = None, use_stratocumulus_coverage_variation: bool = False, stratocumulus_coverage_variation: float = 0.000000, stratocumulus_coverage_variation_curve: CurveFloat = None, use_stratocumulus_height_variation: bool = False, stratocumulus_height_variation: float = 0.000000, stratocumulus_height_variation_curve: CurveFloat = None, use_cumulus_coverage: bool = False, cumulus_coverage: float = 0.000000, cumulus_coverage_curve: CurveFloat = None, use_cumulus_coverage_variation: bool = False, cumulus_coverage_variation: float = 0.000000, cumulus_coverage_variation_curve: CurveFloat = None, use_cumulus_height_variation: bool = False, cumulus_height_variation: float = 0.000000, cumulus_height_variation_curve: CurveFloat = None, use_cumulonimbus_coverage: bool = False, cumulonimbus_coverage: float = 0.000000, cumulonimbus_coverage_curve: CurveFloat = None, use_cumulonimbus_anvil: bool = False, cumulonimbus_anvil: float = 0.000000, cumulonimbus_anvil_curve: CurveFloat = None, use_cumulonimbus_height_variation: bool = False, cumulonimbus_height_variation: float = 0.000000, cumulonimbus_height_variation_curve: CurveFloat = None, use_density_bottom: bool = False, density_bottom: float = 0.000000, density_bottom_curve: CurveFloat = None, use_density_middle: bool = False, density_middle: float = 0.000000, density_middle_curve: CurveFloat = None, use_density_top: bool = False, density_top: float = 0.000000, density_top_curve: CurveFloat = None, use_albedo: bool = False, albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], albedo_curve: CurveLinearColor = None, use_ground_albedo: bool = False, ground_albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], ground_albedo_curve: CurveLinearColor = None, use_beers_powder_intensity: bool = False, beers_powder_intensity: float = 0.000000, beers_powder_intensity_curve: CurveFloat = None, use_beers_powder_depth: bool = False, beers_powder_depth: float = 0.000000, beers_powder_depth_curve: CurveFloat = None, use_bottom_occlusion: bool = False, bottom_occlusion: float = 0.000000, bottom_occlusion_curve: CurveFloat = None, use_bottom_occlusion_height: bool = False, bottom_occlusion_height: float = 0.000000, bottom_occlusion_height_curve: CurveFloat = None, use_night_emissive: bool = False, night_emissive: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], night_emissive_curve: CurveLinearColor = None, use_phase_g: bool = False, phase_g: float = 0.000000, phase_g_curve: CurveFloat = None, use_phase_g2: bool = False, phase_g2: float = 0.000000, phase_g2_curve: CurveFloat = None, use_phase_blend: bool = False, phase_blend: float = 0.000000, phase_blend_curve: CurveFloat = None, use_multi_scattering_contribution: bool = False, multi_scattering_contribution: float = 0.000000, multi_scattering_contribution_curve: CurveFloat = None, use_multi_scattering_occlusion: bool = False, multi_scattering_occlusion: float = 0.000000, multi_scattering_occlusion_curve: CurveFloat = None, use_multi_scattering_eccentricity: bool = False, multi_scattering_eccentricity: float = 0.000000, multi_scattering_eccentricity_curve: CurveFloat = None, use_noise_shape_intensity_a: bool = False, noise_shape_intensity_a: float = 0.000000, noise_shape_intensity_a_curve: CurveFloat = None, use_noise_shape_intensity_b: bool = False, noise_shape_intensity_b: float = 0.000000, noise_shape_intensity_b_curve: CurveFloat = None, use_noise_shape_intensity_c: bool = False, noise_shape_intensity_c: float = 0.000000, noise_shape_intensity_c_curve: CurveFloat = None, use_noise_shape_intensity_d: bool = False, noise_shape_intensity_d: float = 0.000000, noise_shape_intensity_d_curve: CurveFloat = None, use_turbulence_intensity: bool = False, turbulence_intensity: float = 0.000000, turbulence_intensity_curve: CurveFloat = None) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.albedo(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.albedo_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_middle(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_middle_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_top(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.density_top_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive(value: LinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_g(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.phase_g_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity(value: float) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_albedo(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_depth(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_intensity(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion_height(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_anvil(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_coverage(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_height_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_height_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_density_bottom(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_density_middle(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_density_top(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_ground_albedo(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_contribution(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_eccentricity(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_occlusion(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_night_emissive(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_a(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_b(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_c(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_d(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_blend(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g2(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_height_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_height_variation(value: bool) -> None
unreal.SkyCreatorVolumetricCloudSettings_51.use_turbulence_intensity(value: bool) -> None
```

## `unreal.SkyCreatorWeatherFXSettings(StructBase)`

```python
unreal.SkyCreatorWeatherFXSettings.__init__(rain_amount: float = 0.000000, rain_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rain_gravity: float = 0.000000, rain_lifetime_min: float = 0.000000, rain_lifetime_max: float = 0.000000, rain_size_min: float = 0.000000, rain_size_max: float = 0.000000, rain_splash_lifetime_min: float = 0.000000, rain_splash_lifetime_max: float = 0.000000, rain_splash_size_min: Vector2D = [0.000000, 0.000000], rain_splash_size_max: Vector2D = [0.000000, 0.000000], snow_amount: float = 0.000000, snow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], snow_gravity: float = 0.000000, snow_turbulence: float = 0.000000, snow_lifetime_min: float = 0.000000, snow_lifetime_max: float = 0.000000, snow_size_min: float = 0.000000, snow_size_max: float = 0.000000, enable_lightnings: bool = False, lightning_spawn_interval_min: float = 0.000000, lightning_spawn_interval_max: float = 0.000000, lightning_color_min: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lightning_color_max: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lightning_lifetime: float = 0.000000, lightning_bolt_spawn_chance: float = 0.000000, lightning_bolt_width_min: float = 0.000000, lightning_bolt_width_max: float = 0.000000, lightning_bolt_length_min: float = 0.000000, lightning_bolt_length_max: float = 0.000000, lightning_bolt_curve_frequency: float = 0.000000, lightning_bolt_curve_strength_min: float = 0.000000, lightning_bolt_curve_strength_max: float = 0.000000, lightning_bolt_jitter_strength: float = 0.000000, lightning_branch_spawn_chance: float = 0.000000, lightning_branch_scale_min: float = 0.000000, lightning_branch_scale_max: float = 0.000000, rainbow_amount: float = 0.000000, rainbow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rainbow_radius: float = 0.000000, rainbow_thickness: float = 0.000000, secondary_rainbow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], secondary_rainbow_radius: float = 0.000000, secondary_rainbow_thickness: float = 0.000000) -> None
unreal.SkyCreatorWeatherFXSettings.enable_lightnings(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_frequency(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_jitter_strength(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_spawn_chance(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_branch_spawn_chance(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_color_max(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_color_min(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_lifetime(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.rain_gravity(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_size_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_size_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rain_splash_size_max(value: Vector2D) -> None
unreal.SkyCreatorWeatherFXSettings.rain_splash_size_min(value: Vector2D) -> None
unreal.SkyCreatorWeatherFXSettings.rainbow_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rainbow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.rainbow_radius(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.rainbow_thickness(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_radius(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_thickness(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings.snow_gravity(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_size_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_size_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings.snow_turbulence(value: float) -> None
```

## `unreal.SkyCreatorWeatherFXSettings_51(StructBase)`

```python
unreal.SkyCreatorWeatherFXSettings_51.__init__(use_rain_amount: bool = False, rain_amount: float = 0.000000, rain_amount_curve: CurveFloat = None, use_rain_color: bool = False, rain_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rain_color_curve: CurveLinearColor = None, use_rain_gravity: bool = False, rain_gravity: float = 0.000000, rain_gravity_curve: CurveFloat = None, use_rain_lifetime_min: bool = False, rain_lifetime_min: float = 0.000000, rain_lifetime_min_curve: CurveFloat = None, use_rain_lifetime_max: bool = False, rain_lifetime_max: float = 0.000000, rain_lifetime_max_curve: CurveFloat = None, use_rain_size_min: bool = False, rain_size_min: float = 0.000000, rain_size_min_curve: CurveFloat = None, use_rain_size_max: bool = False, rain_size_max: float = 0.000000, rain_size_max_curve: CurveFloat = None, use_rain_emissive: bool = False, rain_emissive: float = 0.000000, rain_emissive_curve: CurveFloat = None, use_rain_splash_lifetime_min: bool = False, rain_splash_lifetime_min: float = 0.000000, rain_splash_lifetime_min_curve: CurveFloat = None, use_rain_splash_lifetime_max: bool = False, rain_splash_lifetime_max: float = 0.000000, rain_splash_lifetime_max_curve: CurveFloat = None, use_rain_splash_size_min: bool = False, rain_splash_size_min: Vector2D = [0.000000, 0.000000], rain_splash_size_min_curve: CurveVector = None, use_rain_splash_size_max: bool = False, rain_splash_size_max: Vector2D = [0.000000, 0.000000], rain_splash_size_max_curve: CurveVector = None, use_snow_amount: bool = False, snow_amount: float = 0.000000, snow_amount_curve: CurveFloat = None, use_snow_color: bool = False, snow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], snow_color_curve: CurveLinearColor = None, use_snow_gravity: bool = False, snow_gravity: float = 0.000000, snow_gravity_curve: CurveFloat = None, use_snow_turbulence: bool = False, snow_turbulence: float = 0.000000, snow_turbulence_curve: CurveFloat = None, use_snow_lifetime_min: bool = False, snow_lifetime_min: float = 0.000000, snow_lifetime_min_curve: CurveFloat = None, use_snow_lifetime_max: bool = False, snow_lifetime_max: float = 0.000000, snow_lifetime_max_curve: CurveFloat = None, use_snow_size_min: bool = False, snow_size_min: float = 0.000000, snow_size_min_curve: CurveFloat = None, use_snow_size_max: bool = False, snow_size_max: float = 0.000000, snow_size_max_curve: CurveFloat = None, use_snow_emissive: bool = False, snow_emissive: float = 0.000000, snow_emissive_curve: CurveFloat = None, use_fog_amount: bool = False, fog_amount: float = 0.000000, fog_amount_curve: CurveFloat = None, enable_lightnings: bool = False, use_lightning_spawn_interval_min: bool = False, lightning_spawn_interval_min: float = 0.000000, lightning_spawn_interval_min_curve: CurveFloat = None, use_lightning_spawn_interval_max: bool = False, lightning_spawn_interval_max: float = 0.000000, lightning_spawn_interval_max_curve: CurveFloat = None, use_lightning_color_min: bool = False, lightning_color_min: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lightning_color_min_curve: CurveLinearColor = None, use_lightning_color_max: bool = False, lightning_color_max: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lightning_color_max_curve: CurveLinearColor = None, use_lightning_lifetime: bool = False, lightning_lifetime: float = 0.000000, lightning_lifetime_curve: CurveFloat = None, use_lightning_bolt_spawn_chance: bool = False, lightning_bolt_spawn_chance: float = 0.000000, lightning_bolt_spawn_chance_curve: CurveFloat = None, use_lightning_bolt_width_min: bool = False, lightning_bolt_width_min: float = 0.000000, lightning_bolt_width_min_curve: CurveFloat = None, use_lightning_bolt_width_max: bool = False, lightning_bolt_width_max: float = 0.000000, lightning_bolt_width_max_curve: CurveFloat = None, use_lightning_bolt_length_min: bool = False, lightning_bolt_length_min: float = 0.000000, lightning_bolt_length_min_curve: CurveFloat = None, use_lightning_bolt_length_max: bool = False, lightning_bolt_length_max: float = 0.000000, lightning_bolt_length_max_curve: CurveFloat = None, use_lightning_bolt_curve_frequency: bool = False, lightning_bolt_curve_frequency: float = 0.000000, lightning_bolt_curve_frequency_curve: CurveFloat = None, use_lightning_bolt_curve_strength_min: bool = False, lightning_bolt_curve_strength_min: float = 0.000000, lightning_bolt_curve_strength_min_curve: CurveFloat = None, use_lightning_bolt_curve_strength_max: bool = False, lightning_bolt_curve_strength_max: float = 0.000000, lightning_bolt_curve_strength_max_curve: CurveFloat = None, use_lightning_bolt_jitter_strength: bool = False, lightning_bolt_jitter_strength: float = 0.000000, lightning_bolt_jitter_strength_curve: CurveFloat = None, use_lightning_branch_spawn_chance: bool = False, lightning_branch_spawn_chance: float = 0.000000, lightning_branch_spawn_chance_curve: CurveFloat = None, use_lightning_branch_scale_min: bool = False, lightning_branch_scale_min: float = 0.000000, lightning_branch_scale_min_curve: CurveFloat = None, use_lightning_branch_scale_max: bool = False, lightning_branch_scale_max: float = 0.000000, lightning_branch_scale_max_curve: CurveFloat = None, use_rainbow_amount: bool = False, rainbow_amount: float = 0.000000, rainbow_amount_curve: CurveFloat = None, use_rainbow_color: bool = False, rainbow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rainbow_color_curve: CurveLinearColor = None, use_rainbow_radius: bool = False, rainbow_radius: float = 0.000000, rainbow_radius_curve: CurveFloat = None, use_rainbow_thickness: bool = False, rainbow_thickness: float = 0.000000, rainbow_thickness_curve: CurveFloat = None, use_secondary_rainbow_color: bool = False, secondary_rainbow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], secondary_rainbow_color_curve: CurveLinearColor = None, use_secondary_rainbow_radius: bool = False, secondary_rainbow_radius: float = 0.000000, secondary_rainbow_radius_curve: CurveFloat = None, use_secondary_rainbow_thickness: bool = False, secondary_rainbow_thickness: float = 0.000000, secondary_rainbow_thickness_curve: CurveFloat = None) -> None
unreal.SkyCreatorWeatherFXSettings_51.enable_lightnings(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.fog_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.fog_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_emissive(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_emissive_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_gravity(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_gravity_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_size_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_size_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_size_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_size_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max(value: Vector2D) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max_curve(value: CurveVector) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min(value: Vector2D) -> None
unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min_curve(value: CurveVector) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_amount(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_emissive(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_emissive_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_gravity(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_gravity_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_size_max(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_size_max_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_size_min(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_size_min_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence(value: float) -> None
unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_fog_amount(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_frequency(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_jitter_strength(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_spawn_chance(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_spawn_chance(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_lifetime(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_amount(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_color(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_emissive(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_gravity(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_amount(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_color(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_radius(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_thickness(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_color(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_radius(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_thickness(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_amount(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_color(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_emissive(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_gravity(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_max(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_min(value: bool) -> None
unreal.SkyCreatorWeatherFXSettings_51.use_snow_turbulence(value: bool) -> None
```

## `unreal.SkyCreatorWeatherSettings(StructBase)`

```python
unreal.SkyCreatorWeatherSettings.__init__(sky_atmosphere_settings: SkyCreatorSkyAtmosphereSettings = [0.033100, [0.175287, 0.409607, 1.000000, 1.000000], 8.000000, 0.003996, [1.000000, 1.000000, 1.000000, 1.000000], 0.000444, [1.000000, 1.000000, 1.000000, 1.000000], 0.800000, 1.200000, 0.001881, [0.345561, 1.000000, 0.045189, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], [0.401978, 0.401978, 0.401978, 1.000000], 1.000000], volumetric_cloud_settings: SkyCreatorVolumetricCloudSettings = [0.000000, 0.500000, 0.500000, 0.750000, 0.500000, 0.500000, 0.750000, 0.500000, 0.500000, 0.000000, 0.000000, 0.500000, 0.001000, 0.050000, 0.100000, [1.000000, 1.000000, 1.000000, 1.000000], [0.250000, 0.250000, 0.250000, 1.000000], 0.250000, 100.000000, 0.000000, 0.250000, [0.010725, 0.015880, 0.025000, 1.000000], 0.600000, -0.400000, 0.500000, 0.500000, 0.100000, 0.500000, 0.500000, 0.625000, 0.250000, 0.125000, 0.250000], background_cloud_settings: SkyCreatorBackgroundCloudSettings = [1.000000, [1.000000, 1.000000, 1.000000, 1.000000], 0.500000, 0.500000, 0.500000, 0.800000], sky_light_settings: SkyCreatorSkyLightSettings = [1.000000, 4.000000, [1.000000, 1.000000, 1.000000, 1.000000], [0.000600, 0.000700, 0.001000, 1.000000], 0.250000], sun_light_settings: SkyCreatorSunLightSettings = [10.000000, [1.000000, 1.000000, 0.900000, 1.000000], 5500.000000, 1.000000, [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.500000, 0.900000], moon_light_settings: SkyCreatorMoonLightSettings = [0.040000, [0.480000, 0.740000, 1.000000, 1.000000], 8500.000000, 1.000000, [1.000000, 0.880000, 0.400000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.500000, 0.900000], exponential_height_fog_settings: SkyCreatorExponentialHeightFogSettings = [0.002000, 0.060000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000, 0.000000, 0.600000, 8.000000, 2000.000000, [0.000000, 0.000000, 0.000000, 1.000000], 0.200000, [1.000000, 1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000, 1.000000], 1.000000], star_map_settings: SkyCreatorStarMapSettings = [0.250000, [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.250000, 1.000000, 8.000000, 4.000000, [0.019600, 0.027609, 0.040000, 1.000000], [0.001384, 0.002343, 0.004000, 1.000000]], weather_fx_settings: SkyCreatorWeatherFXSettings = [0.000000, [0.500000, 0.500000, 0.500000, 0.500000], -1000.000000, 0.300000, 0.600000, 0.100000, 0.800000, 0.200000, 0.300000, [16.000000, 16.000000], [24.000000, 24.000000], 0.000000, [1.000000, 1.000000, 1.000000, 1.000000], -100.000000, 100.000000, 1.000000, 2.000000, 1.000000, 2.000000, False, 1.000000, 10.000000, [1.000000, 1.000000, 1.000000, 1.000000], [1.000000, 1.000000, 1.000000, 1.000000], 0.250000, 50.000000, 0.004000, 0.008000, 2.000000, 4.000000, 0.500000, 0.020000, 0.080000, 0.002500, 10.000000, 0.000400, 0.000800, 0.000000, [0.200000, 0.200000, 0.200000, 1.000000], 10000.000000, 800.000000, [0.050000, 0.050000, 0.050000, 1.000000], 14000.000000, 1600.000000], weather_material_fx_settings: SkyCreatorWeatherMaterialFXSettings = [0.000000, [0.500000, 0.500000, 0.500000, 1.000000], 0.000000, [0.300000, 0.300000, 0.300000, 1.000000], 0.000000, 0.100000, 0.500000, 1.000000, 2.000000, 8.000000, 0.050000, 0.250000, 1.000000, 0.000000, [0.900000, 0.900000, 0.900000, 1.000000], 0.500000, 0.950000], wind_settings: SkyCreatorWindSettings = [0.000000, 0.000000, 0.000000, 0.000000, 2.000000, 0.000000, 0.000000], post_process_settings: SkyCreatorPostProcessSettings = [0.675000, -1.000000, 1.000000]) -> None
unreal.SkyCreatorWeatherSettings.background_cloud_settings(value: SkyCreatorBackgroundCloudSettings) -> None
unreal.SkyCreatorWeatherSettings.exponential_height_fog_settings(value: SkyCreatorExponentialHeightFogSettings) -> None
unreal.SkyCreatorWeatherSettings.moon_light_settings(value: SkyCreatorMoonLightSettings) -> None
unreal.SkyCreatorWeatherSettings.post_process_settings(value: SkyCreatorPostProcessSettings) -> None
unreal.SkyCreatorWeatherSettings.sky_atmosphere_settings(value: SkyCreatorSkyAtmosphereSettings) -> None
unreal.SkyCreatorWeatherSettings.sky_light_settings(value: SkyCreatorSkyLightSettings) -> None
unreal.SkyCreatorWeatherSettings.star_map_settings(value: SkyCreatorStarMapSettings) -> None
unreal.SkyCreatorWeatherSettings.sun_light_settings(value: SkyCreatorSunLightSettings) -> None
unreal.SkyCreatorWeatherSettings.volumetric_cloud_settings(value: SkyCreatorVolumetricCloudSettings) -> None
unreal.SkyCreatorWeatherSettings.weather_fx_settings(value: SkyCreatorWeatherFXSettings) -> None
unreal.SkyCreatorWeatherSettings.weather_material_fx_settings(value: SkyCreatorWeatherMaterialFXSettings) -> None
unreal.SkyCreatorWeatherSettings.wind_settings(value: SkyCreatorWindSettings) -> None
```

## `unreal.SkyCreatorWindSettings(StructBase)`

```python
unreal.SkyCreatorWindSettings.__init__(cloud_wind_direction: float = 0.000000, cloud_wind_speed: float = 0.000000, cloud_noise_shape_wind_direction: float = 0.000000, cloud_noise_shape_wind_speed_horizontal: float = 0.000000, cloud_noise_detail_wind_speed_vertical: float = 0.000000, precipitation_wind_direction: float = 0.000000, precipitation_wind_speed: float = 0.000000) -> None
unreal.SkyCreatorWindSettings.cloud_noise_detail_wind_speed_vertical(value: float) -> None
unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_speed_horizontal(value: float) -> None
unreal.SkyCreatorWindSettings.cloud_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings.cloud_wind_speed(value: float) -> None
unreal.SkyCreatorWindSettings.precipitation_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings.precipitation_wind_speed(value: float) -> None
```

## `unreal.SkyCreatorWindSettings_51(StructBase)`

```python
unreal.SkyCreatorWindSettings_51.__init__(use_cloud_wind_direction: bool = False, cloud_wind_direction: float = 0.000000, cloud_wind_direction_curve: CurveFloat = None, use_cloud_wind_speed: bool = False, cloud_wind_speed: float = 0.000000, cloud_wind_speed_curve: CurveFloat = None, use_cloud_noise_shape_wind_direction: bool = False, cloud_noise_shape_wind_direction: float = 0.000000, cloud_noise_shape_wind_direction_curve: CurveFloat = None, use_cloud_noise_shape_wind_speed_horizontal: bool = False, cloud_noise_shape_wind_speed_horizontal: float = 0.000000, cloud_noise_shape_wind_speed_horizontal_curve: CurveFloat = None, use_cloud_noise_detail_wind_speed_vertical: bool = False, cloud_noise_detail_wind_speed_vertical: float = 0.000000, cloud_noise_detail_wind_speed_vertical_curve: CurveFloat = None, use_precipitation_wind_direction: bool = False, precipitation_wind_direction: float = 0.000000, precipitation_wind_direction_curve: CurveFloat = None, use_precipitation_wind_speed: bool = False, precipitation_wind_speed: float = 0.000000, precipitation_wind_speed_curve: CurveFloat = None) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical(value: float) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal(value: float) -> None
unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.cloud_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings_51.cloud_wind_direction_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.cloud_wind_speed(value: float) -> None
unreal.SkyCreatorWindSettings_51.cloud_wind_speed_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.precipitation_wind_direction(value: float) -> None
unreal.SkyCreatorWindSettings_51.precipitation_wind_direction_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.precipitation_wind_speed(value: float) -> None
unreal.SkyCreatorWindSettings_51.precipitation_wind_speed_curve(value: CurveFloat) -> None
unreal.SkyCreatorWindSettings_51.use_cloud_noise_detail_wind_speed_vertical(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_direction(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_speed_horizontal(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_cloud_wind_direction(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_cloud_wind_speed(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_precipitation_wind_direction(value: bool) -> None
unreal.SkyCreatorWindSettings_51.use_precipitation_wind_speed(value: bool) -> None
```

## `unreal.SolverBreakingFilterSettings(StructBase)`

```python
unreal.SolverBreakingFilterSettings.__init__(filter_enabled: bool = False, min_mass: float = 0.000000, min_speed: float = 0.000000, min_volume: float = 0.000000) -> None
unreal.SolverBreakingFilterSettings.filter_enabled(value: bool) -> None
unreal.SolverBreakingFilterSettings.min_mass(value: float) -> None
unreal.SolverBreakingFilterSettings.min_speed(value: float) -> None
unreal.SolverBreakingFilterSettings.min_volume(value: float) -> None
```

## `unreal.SolverRemovalFilterSettings(StructBase)`

```python
unreal.SolverRemovalFilterSettings.__init__(filter_enabled: bool = False, min_mass: float = 0.000000, min_volume: float = 0.000000) -> None
unreal.SolverRemovalFilterSettings.filter_enabled(value: bool) -> None
unreal.SolverRemovalFilterSettings.min_mass(value: float) -> None
unreal.SolverRemovalFilterSettings.min_volume(value: float) -> None
```

## `unreal.SolverTrailingFilterSettings(StructBase)`

```python
unreal.SolverTrailingFilterSettings.__init__(filter_enabled: bool = False, min_mass: float = 0.000000, min_speed: float = 0.000000, min_volume: float = 0.000000) -> None
unreal.SolverTrailingFilterSettings.filter_enabled(value: bool) -> None
unreal.SolverTrailingFilterSettings.min_mass(value: float) -> None
unreal.SolverTrailingFilterSettings.min_speed(value: float) -> None
unreal.SolverTrailingFilterSettings.min_volume(value: float) -> None
```

## `unreal.SourceEffectBitCrusherBaseSettings(StructBase)`

```python
unreal.SourceEffectBitCrusherBaseSettings.__init__(sample_rate: float = 0.000000, bit_depth: float = 0.000000) -> None
unreal.SourceEffectBitCrusherBaseSettings.asset_sample_rate(value: float) -> None
unreal.SourceEffectBitCrusherBaseSettings.bit_depth(value: float) -> None
unreal.SourceEffectBitCrusherBaseSettings.sample_rate(value: float) -> None
```

## `unreal.SourceEffectBitCrusherSettings(StructBase)`

```python
unreal.SourceEffectBitCrusherSettings.__init__(sample_rate_modulation: SoundModulationDestinationSettings = [1.000000, []], bit_modulation: SoundModulationDestinationSettings = [1.000000, []]) -> None
unreal.SourceEffectBitCrusherSettings.bit_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectBitCrusherSettings.sample_rate_modulation(value: SoundModulationDestinationSettings) -> None
```

## `unreal.SourceEffectChorusBaseSettings(StructBase)`

```python
unreal.SourceEffectChorusBaseSettings.__init__(depth: float = 0.000000, frequency: float = 0.000000, feedback: float = 0.000000, wet_level: float = 0.000000, dry_level: float = 0.000000, spread: float = 0.000000) -> None
unreal.SourceEffectChorusBaseSettings.depth(value: float) -> None
unreal.SourceEffectChorusBaseSettings.dry_level(value: float) -> None
unreal.SourceEffectChorusBaseSettings.feedback(value: float) -> None
unreal.SourceEffectChorusBaseSettings.frequency(value: float) -> None
unreal.SourceEffectChorusBaseSettings.spread(value: float) -> None
unreal.SourceEffectChorusBaseSettings.wet_level(value: float) -> None
```

## `unreal.SourceEffectChorusSettings(StructBase)`

```python
unreal.SourceEffectChorusSettings.__init__(depth_modulation: SoundModulationDestinationSettings = [1.000000, []], frequency_modulation: SoundModulationDestinationSettings = [1.000000, []], feedback_modulation: SoundModulationDestinationSettings = [1.000000, []], wet_modulation: SoundModulationDestinationSettings = [1.000000, []], dry_modulation: SoundModulationDestinationSettings = [1.000000, []], spread_modulation: SoundModulationDestinationSettings = [1.000000, []]) -> None
unreal.SourceEffectChorusSettings.depth(value: float) -> None
unreal.SourceEffectChorusSettings.depth_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectChorusSettings.dry_level(value: float) -> None
unreal.SourceEffectChorusSettings.dry_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectChorusSettings.feedback(value: float) -> None
unreal.SourceEffectChorusSettings.feedback_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectChorusSettings.frequency(value: float) -> None
unreal.SourceEffectChorusSettings.frequency_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectChorusSettings.spread(value: float) -> None
unreal.SourceEffectChorusSettings.spread_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SourceEffectChorusSettings.wet_level(value: float) -> None
unreal.SourceEffectChorusSettings.wet_modulation(value: SoundModulationDestinationSettings) -> None
```

## `unreal.SourceEffectConvolutionReverbSettings(StructBase)`

```python
unreal.SourceEffectConvolutionReverbSettings.__init__(wet_volume_db: float = 0.000000, dry_volume_db: float = 0.000000, bypass: bool = False) -> None
unreal.SourceEffectConvolutionReverbSettings.bypass(value: bool) -> None
unreal.SourceEffectConvolutionReverbSettings.dry_volume_db(value: float) -> None
unreal.SourceEffectConvolutionReverbSettings.wet_volume_db(value: float) -> None
```

## `unreal.SourceEffectDynamicsProcessorSettings(StructBase)`

```python
unreal.SourceEffectDynamicsProcessorSettings.__init__(dynamics_processor_type: SourceEffectDynamicsProcessorType = SourceEffectDynamicsProcessorType.COMPRESSOR, peak_mode: SourceEffectDynamicsPeakMode = SourceEffectDynamicsPeakMode.MEAN_SQUARED, look_ahead_msec: float = 0.000000, attack_time_msec: float = 0.000000, release_time_msec: float = 0.000000, threshold_db: float = 0.000000, ratio: float = 0.000000, knee_bandwidth_db: float = 0.000000, input_gain_db: float = 0.000000, output_gain_db: float = 0.000000, stereo_linked: bool = False, analog_mode: bool = False) -> None
unreal.SourceEffectDynamicsProcessorSettings.analog_mode(value: bool) -> None
unreal.SourceEffectDynamicsProcessorSettings.attack_time_msec(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.dynamics_processor_type(value: SourceEffectDynamicsProcessorType) -> None
unreal.SourceEffectDynamicsProcessorSettings.input_gain_db(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.knee_bandwidth_db(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.look_ahead_msec(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.output_gain_db(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.peak_mode(value: SourceEffectDynamicsPeakMode) -> None
unreal.SourceEffectDynamicsProcessorSettings.ratio(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.release_time_msec(value: float) -> None
unreal.SourceEffectDynamicsProcessorSettings.stereo_linked(value: bool) -> None
unreal.SourceEffectDynamicsProcessorSettings.threshold_db(value: float) -> None
```

## `unreal.SourceEffectEnvelopeFollowerSettings(StructBase)`

```python
unreal.SourceEffectEnvelopeFollowerSettings.__init__(attack_time: float = 0.000000, release_time: float = 0.000000, peak_mode: EnvelopeFollowerPeakMode = EnvelopeFollowerPeakMode.MEAN_SQUARED, is_analog_mode: bool = False) -> None
unreal.SourceEffectEnvelopeFollowerSettings.attack_time(value: float) -> None
unreal.SourceEffectEnvelopeFollowerSettings.is_analog_mode(value: bool) -> None
unreal.SourceEffectEnvelopeFollowerSettings.peak_mode(value: EnvelopeFollowerPeakMode) -> None
unreal.SourceEffectEnvelopeFollowerSettings.release_time(value: float) -> None
```

## `unreal.SourceEffectFilterSettings(StructBase)`

```python
unreal.SourceEffectFilterSettings.__init__(filter_circuit: SourceEffectFilterCircuit = SourceEffectFilterCircuit.ONE_POLE, filter_type: SourceEffectFilterType = SourceEffectFilterType.LOW_PASS, cutoff_frequency: float = 0.000000, filter_q: float = 0.000000, audio_bus_modulation: Array[SourceEffectFilterAudioBusModulationSettings] = []) -> None
unreal.SourceEffectFilterSettings.audio_bus_modulation(value: Array[SourceEffectFilterAudioBusModulationSettings]) -> None
unreal.SourceEffectFilterSettings.cutoff_frequency(value: float) -> None
unreal.SourceEffectFilterSettings.filter_circuit(value: SourceEffectFilterCircuit) -> None
unreal.SourceEffectFilterSettings.filter_q(value: float) -> None
unreal.SourceEffectFilterSettings.filter_type(value: SourceEffectFilterType) -> None
```

## `unreal.SourceEffectFoldbackDistortionSettings(StructBase)`

```python
unreal.SourceEffectFoldbackDistortionSettings.__init__(input_gain_db: float = 0.000000, threshold_db: float = 0.000000, output_gain_db: float = 0.000000) -> None
unreal.SourceEffectFoldbackDistortionSettings.input_gain_db(value: float) -> None
unreal.SourceEffectFoldbackDistortionSettings.output_gain_db(value: float) -> None
unreal.SourceEffectFoldbackDistortionSettings.threshold_db(value: float) -> None
```

## `unreal.SourceEffectIndividualFilterSettings(StructBase)`

```python
unreal.SourceEffectIndividualFilterSettings.__init__(filter_circuit: SourceEffectMotionFilterCircuit = SourceEffectMotionFilterCircuit.ONE_POLE, filter_type: SourceEffectMotionFilterType = SourceEffectMotionFilterType.LOW_PASS, cutoff_frequency: float = 0.000000, filter_q: float = 0.000000) -> None
unreal.SourceEffectIndividualFilterSettings.cutoff_frequency(value: float) -> None
unreal.SourceEffectIndividualFilterSettings.filter_circuit(value: SourceEffectMotionFilterCircuit) -> None
unreal.SourceEffectIndividualFilterSettings.filter_q(value: float) -> None
unreal.SourceEffectIndividualFilterSettings.filter_type(value: SourceEffectMotionFilterType) -> None
```

## `unreal.SourceEffectMidSideSpreaderSettings(StructBase)`

```python
unreal.SourceEffectMidSideSpreaderSettings.__init__(spread_amount: float = 0.000000, input_mode: StereoChannelMode = StereoChannelMode.MID_SIDE, output_mode: StereoChannelMode = StereoChannelMode.MID_SIDE, equal_power: bool = False) -> None
unreal.SourceEffectMidSideSpreaderSettings.equal_power(value: bool) -> None
unreal.SourceEffectMidSideSpreaderSettings.input_mode(value: StereoChannelMode) -> None
unreal.SourceEffectMidSideSpreaderSettings.output_mode(value: StereoChannelMode) -> None
unreal.SourceEffectMidSideSpreaderSettings.spread_amount(value: float) -> None
```

## `unreal.SourceEffectMotionFilterModulationSettings(StructBase)`

```python
unreal.SourceEffectMotionFilterModulationSettings.__init__(modulation_source: SourceEffectMotionFilterModSource = SourceEffectMotionFilterModSource.DISTANCE_FROM_LISTENER, modulation_input_range: Vector2D = [0.000000, 0.000000], modulation_output_minimum_range: Vector2D = [0.000000, 0.000000], modulation_output_maximum_range: Vector2D = [0.000000, 0.000000], update_ease_ms: float = 0.000000) -> None
unreal.SourceEffectMotionFilterModulationSettings.modulation_input_range(value: Vector2D) -> None
unreal.SourceEffectMotionFilterModulationSettings.modulation_output_maximum_range(value: Vector2D) -> None
unreal.SourceEffectMotionFilterModulationSettings.modulation_output_minimum_range(value: Vector2D) -> None
unreal.SourceEffectMotionFilterModulationSettings.modulation_source(value: SourceEffectMotionFilterModSource) -> None
unreal.SourceEffectMotionFilterModulationSettings.update_ease_ms(value: float) -> None
```

## `unreal.SourceEffectMotionFilterSettings(StructBase)`

```python
unreal.SourceEffectMotionFilterSettings.__init__(motion_filter_topology: SourceEffectMotionFilterTopology = SourceEffectMotionFilterTopology.SERIAL_MODE, motion_filter_mix: float = 0.000000, filter_a_settings: SourceEffectIndividualFilterSettings = [SourceEffectMotionFilterCircuit.LADDER, SourceEffectMotionFilterType.LOW_PASS, 800.000000, 2.000000], filter_b_settings: SourceEffectIndividualFilterSettings = [SourceEffectMotionFilterCircuit.LADDER, SourceEffectMotionFilterType.LOW_PASS, 800.000000, 2.000000], modulation_mappings: Map[SourceEffectMotionFilterModDestination, SourceEffectMotionFilterModulationSettings] = {}, dry_volume_db: float = 0.000000) -> None
unreal.SourceEffectMotionFilterSettings.dry_volume_db(value: float) -> None
unreal.SourceEffectMotionFilterSettings.filter_a_settings(value: SourceEffectIndividualFilterSettings) -> None
unreal.SourceEffectMotionFilterSettings.filter_b_settings(value: SourceEffectIndividualFilterSettings) -> None
unreal.SourceEffectMotionFilterSettings.modulation_mappings(value: Map[SourceEffectMotionFilterModDestination, SourceEffectMotionFilterModulationSettings]) -> None
unreal.SourceEffectMotionFilterSettings.motion_filter_mix(value: float) -> None
unreal.SourceEffectMotionFilterSettings.motion_filter_topology(value: SourceEffectMotionFilterTopology) -> None
```

## `unreal.SourceEffectPannerSettings(StructBase)`

```python
unreal.SourceEffectPannerSettings.__init__(spread: float = 0.000000, pan: float = 0.000000) -> None
unreal.SourceEffectPannerSettings.pan(value: float) -> None
unreal.SourceEffectPannerSettings.spread(value: float) -> None
```

## `unreal.SourceEffectPhaserSettings(StructBase)`

```python
unreal.SourceEffectPhaserSettings.__init__(wet_level: float = 0.000000, frequency: float = 0.000000, feedback: float = 0.000000, lfo_type: PhaserLFOType = PhaserLFOType.SINE, use_quadrature_phase: bool = False) -> None
unreal.SourceEffectPhaserSettings.feedback(value: float) -> None
unreal.SourceEffectPhaserSettings.frequency(value: float) -> None
unreal.SourceEffectPhaserSettings.lfo_type(value: PhaserLFOType) -> None
unreal.SourceEffectPhaserSettings.use_quadrature_phase(value: bool) -> None
unreal.SourceEffectPhaserSettings.wet_level(value: float) -> None
```

## `unreal.SourceEffectRingModulationSettings(StructBase)`

```python
unreal.SourceEffectRingModulationSettings.__init__(modulator_type: RingModulatorTypeSourceEffect = RingModulatorTypeSourceEffect.SINE, frequency: float = 0.000000, depth: float = 0.000000, dry_level: float = 0.000000, wet_level: float = 0.000000, audio_bus_modulator: AudioBus = None) -> None
unreal.SourceEffectRingModulationSettings.audio_bus_modulator(value: AudioBus) -> None
unreal.SourceEffectRingModulationSettings.depth(value: float) -> None
unreal.SourceEffectRingModulationSettings.dry_level(value: float) -> None
unreal.SourceEffectRingModulationSettings.frequency(value: float) -> None
unreal.SourceEffectRingModulationSettings.modulator_type(value: RingModulatorTypeSourceEffect) -> None
unreal.SourceEffectRingModulationSettings.wet_level(value: float) -> None
```

## `unreal.SourceEffectSimpleDelaySettings(StructBase)`

```python
unreal.SourceEffectSimpleDelaySettings.__init__(speed_of_sound: float = 0.000000, delay_amount: float = 0.000000, dry_amount: float = 0.000000, wet_amount: float = 0.000000, feedback: float = 0.000000, delay_based_on_distance: bool = False, use_distance_override: bool = False) -> None
unreal.SourceEffectSimpleDelaySettings.delay_amount(value: float) -> None
unreal.SourceEffectSimpleDelaySettings.delay_based_on_distance(value: bool) -> None
unreal.SourceEffectSimpleDelaySettings.dry_amount(value: float) -> None
unreal.SourceEffectSimpleDelaySettings.feedback(value: float) -> None
unreal.SourceEffectSimpleDelaySettings.speed_of_sound(value: float) -> None
unreal.SourceEffectSimpleDelaySettings.use_distance_override(value: bool) -> None
unreal.SourceEffectSimpleDelaySettings.wet_amount(value: float) -> None
```

## `unreal.SourceEffectStereoDelaySettings(StructBase)`

```python
unreal.SourceEffectStereoDelaySettings.__init__(delay_mode: StereoDelaySourceEffect = StereoDelaySourceEffect.NORMAL, delay_time_msec: float = 0.000000, feedback: float = 0.000000, delay_ratio: float = 0.000000, wet_level: float = 0.000000, dry_level: float = 0.000000, filter_enabled: bool = False, filter_type: StereoDelayFiltertype = StereoDelayFiltertype.LOWPASS, filter_frequency: float = 0.000000, filter_q: float = 0.000000) -> None
unreal.SourceEffectStereoDelaySettings.delay_mode(value: StereoDelaySourceEffect) -> None
unreal.SourceEffectStereoDelaySettings.delay_ratio(value: float) -> None
unreal.SourceEffectStereoDelaySettings.delay_time_msec(value: float) -> None
unreal.SourceEffectStereoDelaySettings.dry_level(value: float) -> None
unreal.SourceEffectStereoDelaySettings.feedback(value: float) -> None
unreal.SourceEffectStereoDelaySettings.filter_enabled(value: bool) -> None
unreal.SourceEffectStereoDelaySettings.filter_frequency(value: float) -> None
unreal.SourceEffectStereoDelaySettings.filter_q(value: float) -> None
unreal.SourceEffectStereoDelaySettings.filter_type(value: StereoDelayFiltertype) -> None
unreal.SourceEffectStereoDelaySettings.wet_level(value: float) -> None
```

## `unreal.SourceEffectWaveShaperSettings(StructBase)`

```python
unreal.SourceEffectWaveShaperSettings.__init__(amount: float = 0.000000, output_gain_db: float = 0.000000) -> None
unreal.SourceEffectWaveShaperSettings.amount(value: float) -> None
unreal.SourceEffectWaveShaperSettings.output_gain_db(value: float) -> None
```

## `unreal.SubmixEffectConvolutionReverbSettings(StructBase)`

```python
unreal.SubmixEffectConvolutionReverbSettings.__init__(wet_volume_db: float = 0.000000, dry_volume_db: float = 0.000000, bypass: bool = False, mix_input_channel_format_to_impulse_response_format: bool = False, mix_reverb_output_to_output_channel_format: bool = False, surround_rear_channel_bleed_db: float = 0.000000, invert_rear_channel_bleed_phase: bool = False, surround_rear_channel_flip: bool = False) -> None
unreal.SubmixEffectConvolutionReverbSettings.allow_hardware_acceleration(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.bypass(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.dry_volume_db(value: float) -> None
unreal.SubmixEffectConvolutionReverbSettings.impulse_response(value: AudioImpulseResponse) -> None
unreal.SubmixEffectConvolutionReverbSettings.invert_rear_channel_bleed_phase(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.mix_input_channel_format_to_impulse_response_format(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.mix_reverb_output_to_output_channel_format(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_amount(value: float) -> None
unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_bleed_db(value: float) -> None
unreal.SubmixEffectConvolutionReverbSettings.surround_rear_channel_flip(value: bool) -> None
unreal.SubmixEffectConvolutionReverbSettings.wet_volume_db(value: float) -> None
```

## `unreal.SubmixEffectDelaySettings(StructBase)`

```python
unreal.SubmixEffectDelaySettings.__init__(maximum_delay_length: float = 0.000000, interpolation_time: float = 0.000000, delay_length: float = 0.000000) -> None
unreal.SubmixEffectDelaySettings.delay_length(value: float) -> None
unreal.SubmixEffectDelaySettings.interpolation_time(value: float) -> None
unreal.SubmixEffectDelaySettings.maximum_delay_length(value: float) -> None
```

## `unreal.SubmixEffectDynamicProcessorFilterSettings(StructBase)`

```python
unreal.SubmixEffectDynamicProcessorFilterSettings.__init__(enabled: bool = False, cutoff: float = 0.000000, gain_db: float = 0.000000) -> None
unreal.SubmixEffectDynamicProcessorFilterSettings.cutoff(value: float) -> None
unreal.SubmixEffectDynamicProcessorFilterSettings.enabled(value: bool) -> None
unreal.SubmixEffectDynamicProcessorFilterSettings.gain_db(value: float) -> None
```

## `unreal.SubmixEffectDynamicsProcessorSettings(StructBase)`

```python
unreal.SubmixEffectDynamicsProcessorSettings.__init__(dynamics_processor_type: SubmixEffectDynamicsProcessorType = SubmixEffectDynamicsProcessorType.COMPRESSOR, peak_mode: SubmixEffectDynamicsPeakMode = SubmixEffectDynamicsPeakMode.MEAN_SQUARED, link_mode: SubmixEffectDynamicsChannelLinkMode = SubmixEffectDynamicsChannelLinkMode.DISABLED, input_gain_db: float = 0.000000, threshold_db: float = 0.000000, ratio: float = 0.000000, knee_bandwidth_db: float = 0.000000, look_ahead_msec: float = 0.000000, attack_time_msec: float = 0.000000, release_time_msec: float = 0.000000, key_source: SubmixEffectDynamicsKeySource = SubmixEffectDynamicsKeySource.DEFAULT, external_audio_bus: AudioBus = None, external_submix: SoundSubmix = None, analog_mode: bool = False, bypass: bool = False, key_audition: bool = False, key_gain_db: float = 0.000000, output_gain_db: float = 0.000000, key_highshelf: SubmixEffectDynamicProcessorFilterSettings = [False, 20.000000, 0.000000], key_lowshelf: SubmixEffectDynamicProcessorFilterSettings = [False, 20.000000, 0.000000]) -> None
unreal.SubmixEffectDynamicsProcessorSettings.analog_mode(value: bool) -> None
unreal.SubmixEffectDynamicsProcessorSettings.attack_time_msec(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.bypass(value: bool) -> None
unreal.SubmixEffectDynamicsProcessorSettings.dynamics_processor_type(value: SubmixEffectDynamicsProcessorType) -> None
unreal.SubmixEffectDynamicsProcessorSettings.external_audio_bus(value: AudioBus) -> None
unreal.SubmixEffectDynamicsProcessorSettings.external_submix(value: SoundSubmix) -> None
unreal.SubmixEffectDynamicsProcessorSettings.input_gain_db(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.key_audition(value: bool) -> None
unreal.SubmixEffectDynamicsProcessorSettings.key_gain_db(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.key_highshelf(value: SubmixEffectDynamicProcessorFilterSettings) -> None
unreal.SubmixEffectDynamicsProcessorSettings.key_lowshelf(value: SubmixEffectDynamicProcessorFilterSettings) -> None
unreal.SubmixEffectDynamicsProcessorSettings.key_source(value: SubmixEffectDynamicsKeySource) -> None
unreal.SubmixEffectDynamicsProcessorSettings.knee_bandwidth_db(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.link_mode(value: SubmixEffectDynamicsChannelLinkMode) -> None
unreal.SubmixEffectDynamicsProcessorSettings.look_ahead_msec(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.output_gain_db(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.peak_mode(value: SubmixEffectDynamicsPeakMode) -> None
unreal.SubmixEffectDynamicsProcessorSettings.ratio(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.release_time_msec(value: float) -> None
unreal.SubmixEffectDynamicsProcessorSettings.threshold_db(value: float) -> None
```

## `unreal.SubmixEffectFilterSettings(StructBase)`

```python
unreal.SubmixEffectFilterSettings.__init__(filter_type: SubmixFilterType = SubmixFilterType.LOW_PASS, filter_algorithm: SubmixFilterAlgorithm = SubmixFilterAlgorithm.ONE_POLE, filter_frequency: float = 0.000000, filter_q: float = 0.000000) -> None
unreal.SubmixEffectFilterSettings.filter_algorithm(value: SubmixFilterAlgorithm) -> None
unreal.SubmixEffectFilterSettings.filter_frequency(value: float) -> None
unreal.SubmixEffectFilterSettings.filter_q(value: float) -> None
unreal.SubmixEffectFilterSettings.filter_type(value: SubmixFilterType) -> None
```

## `unreal.SubmixEffectFlexiverbSettings(StructBase)`

```python
unreal.SubmixEffectFlexiverbSettings.__init__(pre_delay: float = 0.000000, decay_time: float = 0.000000, room_dampening: float = 0.000000, complexity: int = 0) -> None
unreal.SubmixEffectFlexiverbSettings.complexity(value: int) -> None
unreal.SubmixEffectFlexiverbSettings.decay_time(value: float) -> None
unreal.SubmixEffectFlexiverbSettings.pre_delay(value: float) -> None
unreal.SubmixEffectFlexiverbSettings.room_dampening(value: float) -> None
```

## `unreal.SubmixEffectMultibandCompressorSettings(StructBase)`

```python
unreal.SubmixEffectMultibandCompressorSettings.__init__(dynamics_processor_type: SubmixEffectDynamicsProcessorType = SubmixEffectDynamicsProcessorType.COMPRESSOR, peak_mode: SubmixEffectDynamicsPeakMode = SubmixEffectDynamicsPeakMode.MEAN_SQUARED, link_mode: SubmixEffectDynamicsChannelLinkMode = SubmixEffectDynamicsChannelLinkMode.DISABLED, look_ahead_msec: float = 0.000000, analog_mode: bool = False, four_pole: bool = False, bypass: bool = False, key_source: SubmixEffectDynamicsKeySource = SubmixEffectDynamicsKeySource.DEFAULT, external_audio_bus: AudioBus = None, external_submix: SoundSubmix = None, key_gain_db: float = 0.000000, key_audition: bool = False, bands: Array[DynamicsBandSettings] = []) -> None
unreal.SubmixEffectMultibandCompressorSettings.analog_mode(value: bool) -> None
unreal.SubmixEffectMultibandCompressorSettings.bands(value: Array[DynamicsBandSettings]) -> None
unreal.SubmixEffectMultibandCompressorSettings.bypass(value: bool) -> None
unreal.SubmixEffectMultibandCompressorSettings.dynamics_processor_type(value: SubmixEffectDynamicsProcessorType) -> None
unreal.SubmixEffectMultibandCompressorSettings.external_audio_bus(value: AudioBus) -> None
unreal.SubmixEffectMultibandCompressorSettings.external_submix(value: SoundSubmix) -> None
unreal.SubmixEffectMultibandCompressorSettings.four_pole(value: bool) -> None
unreal.SubmixEffectMultibandCompressorSettings.key_audition(value: bool) -> None
unreal.SubmixEffectMultibandCompressorSettings.key_gain_db(value: float) -> None
unreal.SubmixEffectMultibandCompressorSettings.key_source(value: SubmixEffectDynamicsKeySource) -> None
unreal.SubmixEffectMultibandCompressorSettings.link_mode(value: SubmixEffectDynamicsChannelLinkMode) -> None
unreal.SubmixEffectMultibandCompressorSettings.look_ahead_msec(value: float) -> None
unreal.SubmixEffectMultibandCompressorSettings.peak_mode(value: SubmixEffectDynamicsPeakMode) -> None
```

## `unreal.SubmixEffectReverbFastSettings(SubmixEffectReverbSettings)`

```python
unreal.SubmixEffectReverbFastSettings.__init__(bypass_early_reflections: bool = False, reflections_delay: float = 0.000000, gain_hf: float = 0.000000, reflections_gain: float = 0.000000, bypass_late_reflections: bool = False, late_delay: float = 0.000000, decay_time: float = 0.000000, density: float = 0.000000, diffusion: float = 0.000000, air_absorption_gain_hf: float = 0.000000, decay_hf_ratio: float = 0.000000, late_gain: float = 0.000000, gain: float = 0.000000, wet_level: float = 0.000000, dry_level: float = 0.000000, bypass: bool = False) -> None
```

## `unreal.SubmixEffectReverbSettings(StructBase)`

```python
unreal.SubmixEffectReverbSettings.__init__(bypass_early_reflections: bool = False, reflections_delay: float = 0.000000, gain_hf: float = 0.000000, reflections_gain: float = 0.000000, bypass_late_reflections: bool = False, late_delay: float = 0.000000, decay_time: float = 0.000000, density: float = 0.000000, diffusion: float = 0.000000, air_absorption_gain_hf: float = 0.000000, decay_hf_ratio: float = 0.000000, late_gain: float = 0.000000, gain: float = 0.000000, wet_level: float = 0.000000, dry_level: float = 0.000000, bypass: bool = False) -> None
unreal.SubmixEffectReverbSettings.air_absorption_gain_hf(value: float) -> None
unreal.SubmixEffectReverbSettings.bypass(value: bool) -> None
unreal.SubmixEffectReverbSettings.bypass_early_reflections(value: bool) -> None
unreal.SubmixEffectReverbSettings.bypass_late_reflections(value: bool) -> None
unreal.SubmixEffectReverbSettings.decay_hf_ratio(value: float) -> None
unreal.SubmixEffectReverbSettings.decay_time(value: float) -> None
unreal.SubmixEffectReverbSettings.density(value: float) -> None
unreal.SubmixEffectReverbSettings.diffusion(value: float) -> None
unreal.SubmixEffectReverbSettings.dry_level(value: float) -> None
unreal.SubmixEffectReverbSettings.gain(value: float) -> None
unreal.SubmixEffectReverbSettings.gain_hf(value: float) -> None
unreal.SubmixEffectReverbSettings.late_delay(value: float) -> None
unreal.SubmixEffectReverbSettings.late_gain(value: float) -> None
unreal.SubmixEffectReverbSettings.reflections_delay(value: float) -> None
unreal.SubmixEffectReverbSettings.reflections_gain(value: float) -> None
unreal.SubmixEffectReverbSettings.wet_level(value: float) -> None
```

## `unreal.SubmixEffectStereoDelaySettings(StructBase)`

```python
unreal.SubmixEffectStereoDelaySettings.__init__(delay_mode: StereoDelaySourceEffect = StereoDelaySourceEffect.NORMAL, delay_time_msec: float = 0.000000, feedback: float = 0.000000, delay_ratio: float = 0.000000, wet_level: float = 0.000000, dry_level: float = 0.000000, filter_enabled: bool = False, filter_type: StereoDelayFiltertype = StereoDelayFiltertype.LOWPASS, filter_frequency: float = 0.000000, filter_q: float = 0.000000) -> None
unreal.SubmixEffectStereoDelaySettings.delay_mode(value: StereoDelaySourceEffect) -> None
unreal.SubmixEffectStereoDelaySettings.delay_ratio(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.delay_time_msec(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.dry_level(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.feedback(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.filter_enabled(value: bool) -> None
unreal.SubmixEffectStereoDelaySettings.filter_frequency(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.filter_q(value: float) -> None
unreal.SubmixEffectStereoDelaySettings.filter_type(value: StereoDelayFiltertype) -> None
unreal.SubmixEffectStereoDelaySettings.wet_level(value: float) -> None
```

## `unreal.SubmixEffectStereoToQuadSettings(StructBase)`

```python
unreal.SubmixEffectStereoToQuadSettings.__init__(flip_channels: bool = False, rear_channel_gain: float = 0.000000) -> None
unreal.SubmixEffectStereoToQuadSettings.flip_channels(value: bool) -> None
unreal.SubmixEffectStereoToQuadSettings.rear_channel_gain(value: float) -> None
```

## `unreal.SubmixEffectTapDelaySettings(StructBase)`

```python
unreal.SubmixEffectTapDelaySettings.__init__(maximum_delay_length: float = 0.000000, interpolation_time: float = 0.000000, taps: Array[TapDelayInfo] = []) -> None
unreal.SubmixEffectTapDelaySettings.interpolation_time(value: float) -> None
unreal.SubmixEffectTapDelaySettings.maximum_delay_length(value: float) -> None
unreal.SubmixEffectTapDelaySettings.taps(value: Array[TapDelayInfo]) -> None
```

## `unreal.SubobjectEditorMenuContext(Object)`

```python
unreal.SubobjectEditorMenuContext.get_selected_objects() -> Array[Object]
```

## `unreal.SynesthesiaSpectrumAnalysisSettings(AudioSynesthesiaSettings)`

```python
unreal.SynesthesiaSpectrumAnalysisSettings.analysis_period() -> float
unreal.SynesthesiaSpectrumAnalysisSettings.downmix_to_mono() -> bool
unreal.SynesthesiaSpectrumAnalysisSettings.fft_size() -> FFTSize
unreal.SynesthesiaSpectrumAnalysisSettings.spectrum_type() -> AudioSpectrumType
unreal.SynesthesiaSpectrumAnalysisSettings.window_type() -> FFTWindowType
```

## `unreal.TakeRecorderProjectSettings(Object)`

```python
unreal.TakeRecorderProjectSettings.settings() -> TakeRecorderProjectParameters
```

## `unreal.TakeRecorderPropertyTrackSettings(StructBase)`

```python
unreal.TakeRecorderPropertyTrackSettings.__init__() -> None
```

## `unreal.TakeRecorderTrackSettings(StructBase)`

```python
unreal.TakeRecorderTrackSettings.__init__() -> None
```

## `unreal.TakeRecorderUserSettings(Object)`

```python
unreal.TakeRecorderUserSettings.settings() -> TakeRecorderUserParameters
```

## `unreal.TargetChainFKSettings(StructBase)`

```python
unreal.TargetChainFKSettings.__init__(enable_fk: bool = False, rotation_mode: RetargetRotationMode = RetargetRotationMode.INTERPOLATED, rotation_alpha: float = 0.000000, translation_mode: RetargetTranslationMode = RetargetTranslationMode.NONE, translation_alpha: float = 0.000000, pole_vector_matching: float = 0.000000, pole_vector_maintain_offset: bool = False, pole_vector_offset: float = 0.000000) -> None
unreal.TargetChainFKSettings.enable_fk(value: bool) -> None
unreal.TargetChainFKSettings.pole_vector_maintain_offset(value: bool) -> None
unreal.TargetChainFKSettings.pole_vector_matching(value: float) -> None
unreal.TargetChainFKSettings.pole_vector_offset(value: float) -> None
unreal.TargetChainFKSettings.rotation_alpha(value: float) -> None
unreal.TargetChainFKSettings.rotation_mode(value: RetargetRotationMode) -> None
unreal.TargetChainFKSettings.translation_alpha(value: float) -> None
unreal.TargetChainFKSettings.translation_mode(value: RetargetTranslationMode) -> None
```

## `unreal.TargetChainIKSettings(StructBase)`

```python
unreal.TargetChainIKSettings.__init__(enable_ik: bool = False, blend_to_source: float = 0.000000, blend_to_source_weights: Vector = [0.000000, 0.000000, 0.000000], static_offset: Vector = [0.000000, 0.000000, 0.000000], static_local_offset: Vector = [0.000000, 0.000000, 0.000000], static_rotation_offset: Rotator = [0.000000, 0.000000, 0.000000], scale_vertical: float = 0.000000, extension: float = 0.000000, affected_by_ik_warping: bool = False) -> None
unreal.TargetChainIKSettings.affected_by_ik_warping(value: bool) -> None
unreal.TargetChainIKSettings.blend_to_source(value: float) -> None
unreal.TargetChainIKSettings.blend_to_source_weights(value: Vector) -> None
unreal.TargetChainIKSettings.enable_ik(value: bool) -> None
unreal.TargetChainIKSettings.extension(value: float) -> None
unreal.TargetChainIKSettings.scale_vertical(value: float) -> None
unreal.TargetChainIKSettings.static_local_offset(value: Vector) -> None
unreal.TargetChainIKSettings.static_offset(value: Vector) -> None
unreal.TargetChainIKSettings.static_rotation_offset(value: Rotator) -> None
```

## `unreal.TargetChainSettings(StructBase)`

```python
unreal.TargetChainSettings.__init__(fk: TargetChainFKSettings = [True, RetargetRotationMode.INTERPOLATED, 1.000000, RetargetTranslationMode.NONE, 1.000000, 0.000000, False, 0.000000], ik: TargetChainIKSettings = [True, 0.000000, [1.000000, 1.000000, 1.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], 1.000000, 1.000000, True], speed_planting: TargetChainSpeedPlantSettings = [False, "None", 15.000000, 250.000000, 1.000000]) -> None
unreal.TargetChainSettings.fk(value: TargetChainFKSettings) -> None
unreal.TargetChainSettings.ik(value: TargetChainIKSettings) -> None
unreal.TargetChainSettings.speed_planting(value: TargetChainSpeedPlantSettings) -> None
```

## `unreal.TargetChainSpeedPlantSettings(StructBase)`

```python
unreal.TargetChainSpeedPlantSettings.__init__(enable_speed_planting: bool = False, speed_curve_name: Name = "None", speed_threshold: float = 0.000000, unplant_stiffness: float = 0.000000, unplant_critical_damping: float = 0.000000) -> None
unreal.TargetChainSpeedPlantSettings.enable_speed_planting(value: bool) -> None
unreal.TargetChainSpeedPlantSettings.speed_curve_name(value: Name) -> None
unreal.TargetChainSpeedPlantSettings.speed_threshold(value: float) -> None
unreal.TargetChainSpeedPlantSettings.unplant_critical_damping(value: float) -> None
unreal.TargetChainSpeedPlantSettings.unplant_stiffness(value: float) -> None
```

## `unreal.TargetRootSettings(StructBase)`

```python
unreal.TargetRootSettings.__init__(rotation_alpha: float = 0.000000, translation_alpha: float = 0.000000, blend_to_source: float = 0.000000, blend_to_source_weights: Vector = [0.000000, 0.000000, 0.000000], scale_horizontal: float = 0.000000, scale_vertical: float = 0.000000, translation_offset: Vector = [0.000000, 0.000000, 0.000000], rotation_offset: Rotator = [0.000000, 0.000000, 0.000000], affect_ik_horizontal: float = 0.000000, affect_ik_vertical: float = 0.000000) -> None
unreal.TargetRootSettings.affect_ik_horizontal(value: float) -> None
unreal.TargetRootSettings.affect_ik_vertical(value: float) -> None
unreal.TargetRootSettings.blend_to_source(value: float) -> None
unreal.TargetRootSettings.blend_to_source_weights(value: Vector) -> None
unreal.TargetRootSettings.rotation_alpha(value: float) -> None
unreal.TargetRootSettings.rotation_offset(value: Rotator) -> None
unreal.TargetRootSettings.scale_horizontal(value: float) -> None
unreal.TargetRootSettings.scale_vertical(value: float) -> None
unreal.TargetRootSettings.translation_alpha(value: float) -> None
unreal.TargetRootSettings.translation_offset(value: Vector) -> None
```

## `unreal.TilingConfig(StructBase)`

```python
unreal.TilingConfig.__init__(alignment: int = 0, overlap: int = 0, max_size: int = 0, min_size: int = 0) -> None
unreal.TilingConfig.alignment(value: int) -> None
unreal.TilingConfig.max_size(value: int) -> None
unreal.TilingConfig.min_size(value: int) -> None
unreal.TilingConfig.overlap(value: int) -> None
```

## `unreal.TimecodeCustomAttributeNameSettings(StructBase)`

```python
unreal.TimecodeCustomAttributeNameSettings.__init__() -> None
```

## `unreal.UVMapSettings(StructBase)`

```python
unreal.UVMapSettings.__init__(size: Vector = [0.000000, 0.000000, 0.000000], uv_tile: Vector2D = [0.000000, 0.000000], position: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.UVMapSettings.position(value: Vector) -> None
unreal.UVMapSettings.rotation(value: Rotator) -> None
unreal.UVMapSettings.scale(value: Vector) -> None
unreal.UVMapSettings.size(value: Vector) -> None
unreal.UVMapSettings.uv_tile(value: Vector2D) -> None
```

## `unreal.UrbanEntityEditorBp(BlueprintFunctionLibrary)`

```python
unreal.UrbanEntityEditorBp.build_prefabs_in_path(root_path: str, save_hip: bool) -> None
```

## `unreal.UrbanEntityEditorScene(Actor)`

```python
unreal.UrbanEntityEditorScene.entity_data_source() -> UrbanEntityDataSource_Imp
```

## `unreal.VREditorFloatingUICreationContext(StructBase)`

```python
unreal.VREditorFloatingUICreationContext.__init__(widget_class: Class = None, panel_id: Name = "None", parent_actor: Actor = None, panel_spawn_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], panel_size: Vector2D = [0.000000, 0.000000], panel_mesh: StaticMesh = None, editor_ui_size: float = 0.000000, hide_window_handles: bool = False, mask_out_widget_background: bool = False, no_close_button: bool = False) -> None
unreal.VREditorFloatingUICreationContext.editor_ui_size(value: float) -> None
unreal.VREditorFloatingUICreationContext.hide_window_handles(value: bool) -> None
unreal.VREditorFloatingUICreationContext.mask_out_widget_background(value: bool) -> None
unreal.VREditorFloatingUICreationContext.no_close_button(value: bool) -> None
unreal.VREditorFloatingUICreationContext.panel_id(value: Name) -> None
unreal.VREditorFloatingUICreationContext.panel_mesh(value: StaticMesh) -> None
unreal.VREditorFloatingUICreationContext.panel_size(value: Vector2D) -> None
unreal.VREditorFloatingUICreationContext.panel_spawn_offset(value: Transform) -> None
unreal.VREditorFloatingUICreationContext.parent_actor(value: Actor) -> None
unreal.VREditorFloatingUICreationContext.widget_class(value: Class) -> None
```

## `unreal.VREditorMode(VREditorModeBase)`

```python
unreal.VREditorMode.get_world_scale_factor() -> float
unreal.VREditorMode.interactor_class(value: Class) -> None
unreal.VREditorMode.is_in_game_view() -> bool
unreal.VREditorMode.set_game_view(game_view: bool) -> None
unreal.VREditorMode.teleporter_class(value: Class) -> None
```

## `unreal.VREditorTeleporter(Actor)`

```python
unreal.VREditorTeleporter.do_teleport() -> None
unreal.VREditorTeleporter.get_interactor_trying_teleport() -> ViewportInteractor
unreal.VREditorTeleporter.get_slide_delta(interactor: VREditorInteractor, axis: bool) -> float
unreal.VREditorTeleporter.get_vr_mode() -> VREditorMode
unreal.VREditorTeleporter.init(mode: VREditorMode) -> None
unreal.VREditorTeleporter.is_aiming() -> bool
unreal.VREditorTeleporter.is_teleporting() -> bool
unreal.VREditorTeleporter.set_color(color: LinearColor) -> None
unreal.VREditorTeleporter.set_visibility(visible: bool) -> None
unreal.VREditorTeleporter.shutdown() -> None
unreal.VREditorTeleporter.start_aiming(interactor: ViewportInteractor) -> None
unreal.VREditorTeleporter.start_teleport() -> None
unreal.VREditorTeleporter.stop_aiming() -> None
unreal.VREditorTeleporter.teleport_done() -> None
```

## `unreal.ValidateAssetsSettings(StructBase)`

```python
unreal.ValidateAssetsSettings.__init__(skip_excluded_directories: bool = False, show_if_no_failures: bool = False, collect_per_asset_details: bool = False, validation_usecase: DataValidationUsecase = DataValidationUsecase.NONE, load_assets_for_validation: bool = False, capture_asset_load_logs: bool = False, capture_logs_during_validation: bool = False, capture_warnings_during_validation_as_errors: bool = False, max_assets_to_validate: int = 0, validate_referencers_of_deleted_assets: bool = False) -> None
unreal.ValidateAssetsSettings.capture_asset_load_logs(value: bool) -> None
unreal.ValidateAssetsSettings.capture_logs_during_validation(value: bool) -> None
unreal.ValidateAssetsSettings.capture_warnings_during_validation_as_errors(value: bool) -> None
unreal.ValidateAssetsSettings.collect_per_asset_details(value: bool) -> None
unreal.ValidateAssetsSettings.load_assets_for_validation(value: bool) -> None
unreal.ValidateAssetsSettings.max_assets_to_validate(value: int) -> None
unreal.ValidateAssetsSettings.show_if_no_failures(value: bool) -> None
unreal.ValidateAssetsSettings.skip_excluded_directories(value: bool) -> None
unreal.ValidateAssetsSettings.validate_referencers_of_deleted_assets(value: bool) -> None
unreal.ValidateAssetsSettings.validation_usecase(value: DataValidationUsecase) -> None
```

## `unreal.VoiceSettings(StructBase)`

```python
unreal.VoiceSettings.__init__(component_to_attach_to: SceneComponent = None, attenuation_settings: SoundAttenuation = None, source_effect_chain: SoundEffectSourcePresetChain = None) -> None
unreal.VoiceSettings.attenuation_settings(value: SoundAttenuation) -> None
unreal.VoiceSettings.component_to_attach_to(value: SceneComponent) -> None
unreal.VoiceSettings.source_effect_chain(value: SoundEffectSourcePresetChain) -> None
```

## `unreal.WaveTableSettings(StructBase)`

```python
unreal.WaveTableSettings.__init__() -> None
```

## `unreal.WdpActionSettingsAPI(StandardApiClassBase)`

```python
unreal.WdpActionSettingsAPI.set_default_action_setting(params: WdpSetDefaultActionSettingParams) -> Optional[ResultBase]
unreal.WdpActionSettingsAPI.set_edit_shape_action_setting(params: WdpSetShapeEditorEditModeParams) -> Optional[ResultBase]
```

## `unreal.WdpGlobalSettingsAPI(StandardApiClassBase)`

```python
unreal.WdpGlobalSettingsAPI.get_api_version(params: ParamsBase) -> Optional[WdpGlobalGetVersionParams]
unreal.WdpGlobalSettingsAPI.get_coord_z_ref(params: ParamsBase) -> Optional[WdpGlobalGetCoordZTypeParams]
unreal.WdpGlobalSettingsAPI.get_frame_rate_limit(params: ParamsBase) -> Optional[WdpGlobalSettingsFPSResults]
unreal.WdpGlobalSettingsAPI.get_resolution(params: ParamsBase) -> Optional[WdpGlobalSettingsResolutionResults]
unreal.WdpGlobalSettingsAPI.get_screen_percentage(params: ParamsBase) -> Optional[WdpGlobalSettingsScreenPercentageResults]
unreal.WdpGlobalSettingsAPI.set_audio_volume(params: WdpGlobalSettingsSoundParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_coord_z_ref(params: WdpGlobalSetCoordZTypeParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_frame_rate_limit(params: WdpGlobalSettingsFPSParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_gizmo_setting(params: WdpSetGizmoSettingParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_interactive_mode(params: WdpSetInteractiveModeParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_resolution(params: WdpGlobalSettingsResolutionParams) -> Optional[ResultBase]
unreal.WdpGlobalSettingsAPI.set_screen_percentage(params: WdpGlobalSettingsScreenPercentageParams) -> Optional[ResultBase]
```

## `unreal.WdpGlobalSettingsFPSParams(ParamsBase)`

```python
unreal.WdpGlobalSettingsFPSParams.__init__(max_fps: int = 0) -> None
unreal.WdpGlobalSettingsFPSParams.max_fps(value: int) -> None
```

## `unreal.WdpGlobalSettingsFPSResults(ResultBase)`

```python
unreal.WdpGlobalSettingsFPSResults.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, max_fps: int = 0) -> None
unreal.WdpGlobalSettingsFPSResults.max_fps(value: int) -> None
```

## `unreal.WdpGlobalSettingsManager(WorldSubsystem)`

```python
unreal.WdpGlobalSettingsManager.get() -> WdpGlobalSettingsManager
unreal.WdpGlobalSettingsManager.get_coord_z_ref() -> Coord_Z_Ref
unreal.WdpGlobalSettingsManager.get_frame_rate_limit() -> float
unreal.WdpGlobalSettingsManager.get_resolution() -> Vector2D
unreal.WdpGlobalSettingsManager.set_audio_volume(volume: float) -> bool
unreal.WdpGlobalSettingsManager.set_coord_z_ref(coord_z_type_value: Coord_Z_Ref) -> None
unreal.WdpGlobalSettingsManager.set_frame_rate_limit(max_fps: int) -> bool
unreal.WdpGlobalSettingsManager.set_resolution(size_x: int, size_y: int) -> bool
```

## `unreal.WdpGlobalSettingsResolutionParams(ParamsBase)`

```python
unreal.WdpGlobalSettingsResolutionParams.__init__(resolution_x: int = 0, resolution_y: int = 0) -> None
unreal.WdpGlobalSettingsResolutionParams.resolution_x(value: int) -> None
unreal.WdpGlobalSettingsResolutionParams.resolution_y(value: int) -> None
```

## `unreal.WdpGlobalSettingsResolutionResults(ResultBase)`

```python
unreal.WdpGlobalSettingsResolutionResults.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, resolution_x: float = 0.000000, resolution_y: float = 0.000000) -> None
unreal.WdpGlobalSettingsResolutionResults.resolution_x(value: float) -> None
unreal.WdpGlobalSettingsResolutionResults.resolution_y(value: float) -> None
```

## `unreal.WdpGlobalSettingsScreenPercentageParams(ParamsBase)`

```python
unreal.WdpGlobalSettingsScreenPercentageParams.__init__(screen_percentage: float = 0.000000) -> None
unreal.WdpGlobalSettingsScreenPercentageParams.screen_percentage(value: float) -> None
```

## `unreal.WdpGlobalSettingsScreenPercentageResults(ResultBase)`

```python
unreal.WdpGlobalSettingsScreenPercentageResults.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, screen_percentage: float = 0.000000) -> None
unreal.WdpGlobalSettingsScreenPercentageResults.screen_percentage(value: float) -> None
```

## `unreal.WdpSetShapeEditorEditModeParams(ParamsBase)`

```python
unreal.WdpSetShapeEditorEditModeParams.__init__(edit_mode: WdpShapeEditorEditMode = WdpShapeEditorEditMode.NONE, line_width: float = 0.000000) -> None
unreal.WdpSetShapeEditorEditModeParams.edit_mode(value: WdpShapeEditorEditMode) -> None
unreal.WdpSetShapeEditorEditModeParams.line_width(value: float) -> None
```

## `unreal.WdpShapeEditorAPI(StandardApiClassBase)`

```python
unreal.WdpShapeEditorAPI.range_pick_shape_points(params: WdpRangePickShapePointsParams) -> Optional[ResultBase]
unreal.WdpShapeEditorAPI.update_shape_points(params: WdpUpdateShapePointsParams) -> Optional[ResultBase]
```

## `unreal.glTFRuntimeConfig(StructBase)`

```python
unreal.glTFRuntimeConfig.__init__(transform_base_type: EglTFRuntimeTransformBaseType = EglTFRuntimeTransformBaseType.DEFAULT, basis_matrix: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000]], base_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], basis_vector_matrix: glTFRuntimeBasisMatrix = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], scene_scale: float = 0.000000, content_plugins_to_scan: Array[str] = [], allow_external_files: bool = False, override_base_directory: str = "", override_base_directory_from_content_dir: bool = False, archive_entry_point: str = "", archive_auto_entry_point_extensions: str = "", runtime_context_object: Object = None, runtime_context_string: str = "", as_blob: bool = False, prefix_for_unnamed_nodes: str = "", encryption_key: str = "") -> None
unreal.glTFRuntimeConfig.allow_external_files(value: bool) -> None
unreal.glTFRuntimeConfig.archive_auto_entry_point_extensions(value: str) -> None
unreal.glTFRuntimeConfig.archive_entry_point(value: str) -> None
unreal.glTFRuntimeConfig.as_blob(value: bool) -> None
unreal.glTFRuntimeConfig.base_transform(value: Transform) -> None
unreal.glTFRuntimeConfig.basis_matrix(value: Matrix) -> None
unreal.glTFRuntimeConfig.basis_vector_matrix(value: glTFRuntimeBasisMatrix) -> None
unreal.glTFRuntimeConfig.content_plugins_to_scan(value: Array[str]) -> None
unreal.glTFRuntimeConfig.encryption_key(value: str) -> None
unreal.glTFRuntimeConfig.override_base_directory(value: str) -> None
unreal.glTFRuntimeConfig.override_base_directory_from_content_dir(value: bool) -> None
unreal.glTFRuntimeConfig.prefix_for_unnamed_nodes(value: str) -> None
unreal.glTFRuntimeConfig.runtime_context_object(value: Object) -> None
unreal.glTFRuntimeConfig.runtime_context_string(value: str) -> None
unreal.glTFRuntimeConfig.scene_scale(value: float) -> None
unreal.glTFRuntimeConfig.transform_base_type(value: EglTFRuntimeTransformBaseType) -> None
```

## `unreal.glTFRuntimeImagesConfig(StructBase)`

```python
unreal.glTFRuntimeImagesConfig.__init__(compression: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, group: TextureGroup = TextureGroup.TEXTUREGROUP_WORLD, srgb: bool = False, max_width: int = 0, max_height: int = 0, vertical_flip: bool = False, force_hdr: bool = False, compress_mips: bool = False, streaming: bool = False, lod_bias: int = 0) -> None
unreal.glTFRuntimeImagesConfig.compress_mips(value: bool) -> None
unreal.glTFRuntimeImagesConfig.compression(value: TextureCompressionSettings) -> None
unreal.glTFRuntimeImagesConfig.force_hdr(value: bool) -> None
unreal.glTFRuntimeImagesConfig.group(value: TextureGroup) -> None
unreal.glTFRuntimeImagesConfig.lod_bias(value: int) -> None
unreal.glTFRuntimeImagesConfig.max_height(value: int) -> None
unreal.glTFRuntimeImagesConfig.max_width(value: int) -> None
unreal.glTFRuntimeImagesConfig.srgb(value: bool) -> None
unreal.glTFRuntimeImagesConfig.streaming(value: bool) -> None
unreal.glTFRuntimeImagesConfig.vertical_flip(value: bool) -> None
```

