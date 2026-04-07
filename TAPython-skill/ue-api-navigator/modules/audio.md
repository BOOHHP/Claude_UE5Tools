# Unreal Python API — Audio

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AesModularBuildingAssetTagData(StructBase)`

```python
unreal.AesModularBuildingAssetTagData.__init__(height: float = 0.000000, min_height: float = 0.000000, foundation_depth: float = 0.000000, levels: int = 0, min_level: int = 0, land_cover: LandCover = LandCover.CULTIVATED_LAND, type: Name = "None", color: Color = [0, 0, 0, 0], roof_height: float = 0.000000, roof_levels: int = 0, roof_shape: RoofShape = RoofShape.FLAT, roof_color: Color = [0, 0, 0, 0], prefab_type: AesBuildingPrefabType = AesBuildingPrefabType.NONE, prefab_id: str = "", facade_asset: AesAssetChildMetaData = [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], facade_assets: Array[AesAssetChildMetaData] = [], roof_asset: AesAssetChildMetaData = [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], parapet_asset: AesAssetChildMetaData = [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], roof_prop_asset: AesAssetChildMetaData = [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], foundation_asset: AesAssetChildMetaData = [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], mono_assets: Array[AesAssetChildMetaData] = [], outlines: Array[Vector] = [], area: float = 0.000000) -> None
unreal.AesModularBuildingAssetTagData.area() -> float
unreal.AesModularBuildingAssetTagData.color(value: Color) -> None
unreal.AesModularBuildingAssetTagData.facade_asset(value: AesAssetChildMetaData) -> None
unreal.AesModularBuildingAssetTagData.facade_assets(value: Array[AesAssetChildMetaData]) -> None
unreal.AesModularBuildingAssetTagData.foundation_asset(value: AesAssetChildMetaData) -> None
unreal.AesModularBuildingAssetTagData.foundation_depth(value: float) -> None
unreal.AesModularBuildingAssetTagData.height(value: float) -> None
unreal.AesModularBuildingAssetTagData.land_cover(value: LandCover) -> None
unreal.AesModularBuildingAssetTagData.levels(value: int) -> None
unreal.AesModularBuildingAssetTagData.min_height(value: float) -> None
unreal.AesModularBuildingAssetTagData.min_level(value: int) -> None
unreal.AesModularBuildingAssetTagData.mono_assets(value: Array[AesAssetChildMetaData]) -> None
unreal.AesModularBuildingAssetTagData.outlines(value: Array[Vector]) -> None
unreal.AesModularBuildingAssetTagData.parapet_asset(value: AesAssetChildMetaData) -> None
unreal.AesModularBuildingAssetTagData.prefab_id(value: str) -> None
unreal.AesModularBuildingAssetTagData.prefab_type(value: AesBuildingPrefabType) -> None
unreal.AesModularBuildingAssetTagData.roof_asset(value: AesAssetChildMetaData) -> None
unreal.AesModularBuildingAssetTagData.roof_color(value: Color) -> None
unreal.AesModularBuildingAssetTagData.roof_height(value: float) -> None
unreal.AesModularBuildingAssetTagData.roof_levels(value: int) -> None
unreal.AesModularBuildingAssetTagData.roof_prop_asset(value: AesAssetChildMetaData) -> None
unreal.AesModularBuildingAssetTagData.roof_shape(value: RoofShape) -> None
unreal.AesModularBuildingAssetTagData.type(value: Name) -> None
```

## `unreal.AmbientSound(Actor)`

```python
unreal.AmbientSound.adjust_volume(adjust_volume_duration: float, adjust_volume_level: float) -> None
unreal.AmbientSound.audio_component() -> AudioComponent
unreal.AmbientSound.fade_in(fade_in_duration: float, fade_volume_level: float = 1.000000) -> None
unreal.AmbientSound.fade_out(fade_out_duration: float, fade_volume_level: float) -> None
unreal.AmbientSound.play(start_time: float = 0.000000) -> None
unreal.AmbientSound.stop() -> None
```

## `unreal.AudioAnalyzer(Object)`

```python
unreal.AudioAnalyzer.start_analyzing(world_context_object: Object, audio_bus_to_analyze: AudioBus) -> None
unreal.AudioAnalyzer.stop_analyzing(world_context_object: Object = None) -> None
```

## `unreal.AudioAnalyzerNRT(AudioAnalyzerAssetBase)`

```python
unreal.AudioAnalyzerNRT.duration_in_seconds() -> float
unreal.AudioAnalyzerNRT.sound() -> SoundWave
```

## `unreal.AudioBasedVibrationData(StructBase)`

```python
unreal.AudioBasedVibrationData.__init__(sound: SoundBase = None) -> None
unreal.AudioBasedVibrationData.sound(value: SoundBase) -> None
```

## `unreal.AudioCapture(AudioGenerator)`

```python
unreal.AudioCapture.get_audio_capture_device_info() -> Optional[AudioCaptureDeviceInfo]
unreal.AudioCapture.is_capturing_audio() -> bool
unreal.AudioCapture.start_capturing_audio() -> None
unreal.AudioCapture.stop_capturing_audio() -> None
```

## `unreal.AudioCaptureComponent(SynthComponent)`

```python
unreal.AudioCaptureComponent.jitter_latency_frames(value: int) -> None
```

## `unreal.AudioCaptureDeviceInfo(StructBase)`

```python
unreal.AudioCaptureDeviceInfo.__init__(device_name: Name = "None", num_input_channels: int = 0, sample_rate: int = 0) -> None
unreal.AudioCaptureDeviceInfo.device_name() -> Name
unreal.AudioCaptureDeviceInfo.num_input_channels() -> int
unreal.AudioCaptureDeviceInfo.sample_rate() -> int
```

## `unreal.AudioCaptureFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.AudioCaptureFunctionLibrary.create_audio_capture() -> AudioCapture
```

## `unreal.AudioCaptureLibrary(BlueprintFunctionLibrary)`

```python
unreal.AudioCaptureLibrary.conv_audio_input_device_info_to_string(info: AudioInputDeviceInfo) -> str
unreal.AudioCaptureLibrary.get_available_audio_input_devices(world_context_object: Object, on_obtain_devices_event: OnAudioInputDevicesObtained) -> None
```

## `unreal.AudioComponent(SceneComponent)`

```python
unreal.AudioComponent.add_modulation_routing(modulators: Set[SoundModulatorBase], destination: ModulationDestination) -> None
unreal.AudioComponent.adjust_attenuation(attenuation_settings: SoundAttenuationSettings) -> None
unreal.AudioComponent.adjust_volume(adjust_volume_duration: float, adjust_volume_level: float, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.AudioComponent.allow_spatialization(value: bool) -> None
unreal.AudioComponent.attenuation_overrides(value: SoundAttenuationSettings) -> None
unreal.AudioComponent.attenuation_settings(value: SoundAttenuation) -> None
unreal.AudioComponent.auto_attach_location_rule(value: AttachmentRule) -> None
unreal.AudioComponent.auto_attach_parent() -> SceneComponent
unreal.AudioComponent.auto_attach_rotation_rule(value: AttachmentRule) -> None
unreal.AudioComponent.auto_attach_scale_rule(value: AttachmentRule) -> None
unreal.AudioComponent.auto_attach_socket_name(value: Name) -> None
unreal.AudioComponent.auto_manage_attachment() -> bool
unreal.AudioComponent.can_play_multiple_instances(value: bool) -> None
unreal.AudioComponent.concurrency_set(value: Set[SoundConcurrency]) -> None
unreal.AudioComponent.default_parameters(value: Array[AudioParameter]) -> None
unreal.AudioComponent.disable_parameter_updates_while_playing(value: bool) -> None
unreal.AudioComponent.enable_high_pass_filter(value: bool) -> None
unreal.AudioComponent.enable_low_pass_filter(value: bool) -> None
unreal.AudioComponent.envelope_follower_attack_time(value: int) -> None
unreal.AudioComponent.envelope_follower_release_time(value: int) -> None
unreal.AudioComponent.fade_in(fade_in_duration: float, fade_volume_level: float = 1.000000, start_time: float = 0.000000, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.AudioComponent.fade_out(fade_out_duration: float, fade_volume_level: float, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.AudioComponent.get_attenuation_settings_to_apply() -> Optional[SoundAttenuationSettings]
unreal.AudioComponent.get_cooked_envelope_data() -> Optional[float]
unreal.AudioComponent.get_cooked_envelope_data_for_all_playing_sounds() -> Optional[Array[SoundWaveEnvelopeDataPerSound]]
unreal.AudioComponent.get_cooked_fft_data(frequencies_to_get: Array[float]) -> Optional[Array[SoundWaveSpectralData]]
unreal.AudioComponent.get_cooked_fft_data_for_all_playing_sounds() -> Optional[Array[SoundWaveSpectralDataPerSound]]
unreal.AudioComponent.get_modulators(destination: ModulationDestination) -> Set[SoundModulatorBase]
unreal.AudioComponent.get_play_state() -> AudioComponentPlayState
unreal.AudioComponent.has_cooked_amplitude_envelope_data() -> bool
unreal.AudioComponent.has_cooked_fft_data() -> bool
unreal.AudioComponent.high_pass_filter_frequency(value: float) -> None
unreal.AudioComponent.instance_parameters(value: Array[AudioParameter]) -> None
unreal.AudioComponent.is_playing() -> bool
unreal.AudioComponent.is_ui_sound(value: bool) -> None
unreal.AudioComponent.is_virtualized() -> bool
unreal.AudioComponent.low_pass_filter_frequency(value: float) -> None
unreal.AudioComponent.modulation_routing(value: SoundModulationDefaultRoutingSettings) -> None
unreal.AudioComponent.on_audio_finished(value: OnAudioFinished) -> None
unreal.AudioComponent.on_audio_multi_envelope_value(value: OnAudioMultiEnvelopeValue) -> None
unreal.AudioComponent.on_audio_play_state_changed(value: OnAudioPlayStateChanged) -> None
unreal.AudioComponent.on_audio_playback_percent(value: OnAudioPlaybackPercent) -> None
unreal.AudioComponent.on_audio_single_envelope_value(value: OnAudioSingleEnvelopeValue) -> None
unreal.AudioComponent.on_audio_virtualization_changed(value: OnAudioVirtualizationChanged) -> None
unreal.AudioComponent.override_attenuation(value: bool) -> None
unreal.AudioComponent.override_priority(value: bool) -> None
unreal.AudioComponent.override_subtitle_priority(value: bool) -> None
unreal.AudioComponent.pitch_modulation_max(value: float) -> None
unreal.AudioComponent.pitch_modulation_min(value: float) -> None
unreal.AudioComponent.pitch_multiplier(value: float) -> None
unreal.AudioComponent.pitch_multiplier_max(value: float) -> None
unreal.AudioComponent.pitch_multiplier_min(value: float) -> None
unreal.AudioComponent.play(start_time: float = 0.000000) -> None
unreal.AudioComponent.play_quantized(world_context_object: Object, clock_handle: QuartzClockHandle, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, start_time: float = 0.000000, fade_in_duration: float = 0.000000, fade_volume_level: float = 1.000000, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> Tuple[QuartzClockHandle, QuartzQuantizationBoundary]
unreal.AudioComponent.priority(value: float) -> None
unreal.AudioComponent.remove_modulation_routing(modulators: Set[SoundModulatorBase], destination: ModulationDestination) -> None
unreal.AudioComponent.reset_parameters() -> None
unreal.AudioComponent.set_audio_bus_send_post_effect(audio_bus: AudioBus, audio_bus_send_level: float) -> None
unreal.AudioComponent.set_audio_bus_send_pre_effect(audio_bus: AudioBus, audio_bus_send_level: float) -> None
unreal.AudioComponent.set_bool_array_parameter(name: Name, value: Array[bool]) -> None
unreal.AudioComponent.set_bool_parameter(name: Name, bool: bool) -> None
unreal.AudioComponent.set_float_array_parameter(name: Name, value: Array[float]) -> None
unreal.AudioComponent.set_float_parameter(name: Name, float: float) -> None
unreal.AudioComponent.set_high_pass_filter_enabled(high_pass_filter_enabled: bool) -> None
unreal.AudioComponent.set_high_pass_filter_frequency(high_pass_filter_frequency: float) -> None
unreal.AudioComponent.set_int_array_parameter(name: Name, value: Array[int]) -> None
unreal.AudioComponent.set_int_parameter(name: Name, int: int) -> None
unreal.AudioComponent.set_low_pass_filter_enabled(low_pass_filter_enabled: bool) -> None
unreal.AudioComponent.set_low_pass_filter_frequency(low_pass_filter_frequency: float) -> None
unreal.AudioComponent.set_modulation_routing(modulators: Set[SoundModulatorBase], destination: ModulationDestination, routing_method: ModulationRouting = ModulationRouting.INHERIT) -> None
unreal.AudioComponent.set_object_array_parameter(name: Name, value: Array[Object]) -> None
unreal.AudioComponent.set_object_parameter(name: Name, value: Object) -> None
unreal.AudioComponent.set_output_to_bus_only(output_to_bus_only: bool) -> None
unreal.AudioComponent.set_parameters_blueprint(parameters: Array[AudioParameter]) -> None
unreal.AudioComponent.set_paused(pause: bool) -> None
unreal.AudioComponent.set_pitch_multiplier(new_pitch_multiplier: float) -> None
unreal.AudioComponent.set_sound(new_sound: SoundBase) -> None
unreal.AudioComponent.set_source_bus_send_post_effect(sound_source_bus: SoundSourceBus, source_bus_send_level: float) -> None
unreal.AudioComponent.set_source_bus_send_pre_effect(sound_source_bus: SoundSourceBus, source_bus_send_level: float) -> None
unreal.AudioComponent.set_string_array_parameter(name: Name, value: Array[str]) -> None
unreal.AudioComponent.set_string_parameter(name: Name, value: str) -> None
unreal.AudioComponent.set_submix_send(submix: SoundSubmixBase, send_level: float) -> None
unreal.AudioComponent.set_trigger_parameter(name: Name) -> None
unreal.AudioComponent.set_ui_sound(ui_sound: bool) -> None
unreal.AudioComponent.set_volume_multiplier(new_volume_multiplier: float) -> None
unreal.AudioComponent.set_wave_parameter(name: Name, wave: SoundWave) -> None
unreal.AudioComponent.sound(value: SoundBase) -> None
unreal.AudioComponent.source_effect_chain(value: SoundEffectSourcePresetChain) -> None
unreal.AudioComponent.stop() -> None
unreal.AudioComponent.stop_delayed(delay_time: float) -> None
unreal.AudioComponent.subtitle_priority(value: float) -> None
unreal.AudioComponent.suppress_subtitles(value: bool) -> None
unreal.AudioComponent.volume_modulation_max(value: float) -> None
unreal.AudioComponent.volume_modulation_min(value: float) -> None
unreal.AudioComponent.volume_multiplier(value: float) -> None
unreal.AudioComponent.volume_multiplier_max(value: float) -> None
unreal.AudioComponent.volume_multiplier_min(value: float) -> None
```

## `unreal.AudioComponentParam(AudioParameter)`

```python
unreal.AudioComponentParam.__init__(param_name: Name = "None", float_param: float = 0.000000, bool_param: bool = False, int_param: int = 0, object_param: Object = None, string_param: str = "", array_float_param: Array[float] = [], array_bool_param: Array[bool] = [], array_int_param: Array[int] = [], array_object_param: Array[Object] = [], array_string_param: Array[str] = [], param_type: AudioParameterType = AudioParameterType.NONE, sound_wave_param: SoundWave = None) -> None
unreal.AudioComponentParam.sound_wave_param(value: SoundWave) -> None
```

## `unreal.AudioEQEffect(AudioEffectParameters)`

```python
unreal.AudioEQEffect.__init__() -> None
```

## `unreal.AudioEffectParameters(StructBase)`

```python
unreal.AudioEffectParameters.__init__() -> None
```

## `unreal.AudioImpulseResponse(Object)`

```python
unreal.AudioImpulseResponse.ir_data(value: Array[float]) -> None
unreal.AudioImpulseResponse.normalization_volume_db() -> float
unreal.AudioImpulseResponse.true_stereo() -> bool
```

## `unreal.AudioInputDeviceChannelProperty(StructBase)`

```python
unreal.AudioInputDeviceChannelProperty.__init__(audio_input_device_channel: int = 0) -> None
unreal.AudioInputDeviceChannelProperty.audio_input_device_channel(value: int) -> None
```

## `unreal.AudioInputDeviceInfo(StructBase)`

```python
unreal.AudioInputDeviceInfo.__init__(device_name: str = "", device_id: str = "", input_channels: int = 0, preferred_sample_rate: int = 0, supports_hardware_aec: bool = False) -> None
unreal.AudioInputDeviceInfo.device_id() -> str
unreal.AudioInputDeviceInfo.device_name() -> str
unreal.AudioInputDeviceInfo.input_channels() -> int
unreal.AudioInputDeviceInfo.preferred_sample_rate() -> int
unreal.AudioInputDeviceInfo.supports_hardware_aec() -> bool
```

## `unreal.AudioInputDeviceInfoProperty(StructBase)`

```python
unreal.AudioInputDeviceInfoProperty.__init__(device_name: str = "", device_id: str = "", input_channels: int = 0, preferred_sample_rate: int = 0, is_default_device: bool = False) -> None
unreal.AudioInputDeviceInfoProperty.device_id() -> str
unreal.AudioInputDeviceInfoProperty.device_name() -> str
unreal.AudioInputDeviceInfoProperty.input_channels() -> int
unreal.AudioInputDeviceInfoProperty.is_default_device() -> bool
unreal.AudioInputDeviceInfoProperty.preferred_sample_rate() -> int
```

## `unreal.AudioInputDeviceProperty(StructBase)`

```python
unreal.AudioInputDeviceProperty.__init__(use_system_default_audio_device: bool = False, device_info_array: Array[AudioInputDeviceInfoProperty] = [], device_id: str = "", audio_input_buffer_size: int = 0) -> None
unreal.AudioInputDeviceProperty.audio_input_buffer_size(value: int) -> None
unreal.AudioInputDeviceProperty.device_id(value: str) -> None
unreal.AudioInputDeviceProperty.device_info_array() -> Array[AudioInputDeviceInfoProperty]
unreal.AudioInputDeviceProperty.use_system_default_audio_device(value: bool) -> None
```

## `unreal.AudioMeter(Widget)`

```python
unreal.AudioMeter.background_color() -> LinearColor
unreal.AudioMeter.get_meter_channel_info() -> Array[MeterChannelInfo]
unreal.AudioMeter.meter_background_color() -> LinearColor
unreal.AudioMeter.meter_clipping_color() -> LinearColor
unreal.AudioMeter.meter_peak_color() -> LinearColor
unreal.AudioMeter.meter_scale_color() -> LinearColor
unreal.AudioMeter.meter_scale_label_color() -> LinearColor
unreal.AudioMeter.meter_value_color() -> LinearColor
unreal.AudioMeter.orientation() -> Orientation
unreal.AudioMeter.set_background_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_background_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_channel_info(meter_channel_info: Array[MeterChannelInfo]) -> None
unreal.AudioMeter.set_meter_clipping_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_peak_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_scale_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_scale_label_color(value: LinearColor) -> None
unreal.AudioMeter.set_meter_value_color(value: LinearColor) -> None
unreal.AudioMeter.widget_style(value: AudioMeterStyle) -> None
```

## `unreal.AudioMeterDefaultColorStyle(SlateWidgetStyle)`

```python
unreal.AudioMeterDefaultColorStyle.__init__(meter_background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_value_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_peak_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_clipping_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_scale_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_scale_label_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.AudioMeterDefaultColorStyle.meter_background_color(value: LinearColor) -> None
unreal.AudioMeterDefaultColorStyle.meter_clipping_color(value: LinearColor) -> None
unreal.AudioMeterDefaultColorStyle.meter_peak_color(value: LinearColor) -> None
unreal.AudioMeterDefaultColorStyle.meter_scale_color(value: LinearColor) -> None
unreal.AudioMeterDefaultColorStyle.meter_scale_label_color(value: LinearColor) -> None
unreal.AudioMeterDefaultColorStyle.meter_value_color(value: LinearColor) -> None
```

## `unreal.AudioMeterStyle(SlateWidgetStyle)`

```python
unreal.AudioMeterStyle.__init__(meter_value_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], meter_background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], meter_value_background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], meter_peak_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], meter_size: Vector2D = [0.000000, 0.000000], meter_padding: Vector2D = [0.000000, 0.000000], meter_value_padding: float = 0.000000, peak_value_width: float = 0.000000, value_range_db: Vector2D = [0.000000, 0.000000], show_scale: bool = False, scale_side: bool = False, scale_hash_offset: float = 0.000000, scale_hash_width: float = 0.000000, scale_hash_height: float = 0.000000, decibels_per_hash: int = 0, font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000]) -> None
unreal.AudioMeterStyle.background_image(value: SlateBrush) -> None
unreal.AudioMeterStyle.decibels_per_hash(value: int) -> None
unreal.AudioMeterStyle.font(value: SlateFontInfo) -> None
unreal.AudioMeterStyle.meter_background_image(value: SlateBrush) -> None
unreal.AudioMeterStyle.meter_padding(value: Vector2D) -> None
unreal.AudioMeterStyle.meter_peak_image(value: SlateBrush) -> None
unreal.AudioMeterStyle.meter_size(value: Vector2D) -> None
unreal.AudioMeterStyle.meter_value_background_image(value: SlateBrush) -> None
unreal.AudioMeterStyle.meter_value_image(value: SlateBrush) -> None
unreal.AudioMeterStyle.meter_value_padding(value: float) -> None
unreal.AudioMeterStyle.peak_value_width(value: float) -> None
unreal.AudioMeterStyle.scale_hash_height(value: float) -> None
unreal.AudioMeterStyle.scale_hash_offset(value: float) -> None
unreal.AudioMeterStyle.scale_hash_width(value: float) -> None
unreal.AudioMeterStyle.scale_side(value: bool) -> None
unreal.AudioMeterStyle.show_scale(value: bool) -> None
unreal.AudioMeterStyle.value_range_db(value: Vector2D) -> None
```

## `unreal.AudioMeter_GetMeterChannelInfo(DelegateBase)`

```python
unreal.AudioMeter_GetMeterChannelInfo.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioMixerLibrary(BlueprintFunctionLibrary)`

```python
unreal.AudioMixerLibrary.add_master_submix_effect(world_context_object: Object, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.add_source_effect_to_preset_chain(world_context_object: Object, preset_chain: SoundEffectSourcePresetChain, entry: SourceEffectChainEntry) -> None
unreal.AudioMixerLibrary.add_submix_effect(world_context_object: Object, sound_submix: SoundSubmix, submix_effect_preset: SoundEffectSubmixPreset) -> int
unreal.AudioMixerLibrary.clear_master_submix_effects(world_context_object: Object) -> None
unreal.AudioMixerLibrary.clear_submix_effect_chain_override(world_context_object: Object, sound_submix: SoundSubmix, fade_time_sec: float) -> None
unreal.AudioMixerLibrary.clear_submix_effects(world_context_object: Object, sound_submix: SoundSubmix) -> None
unreal.AudioMixerLibrary.conv_audio_output_device_info_to_string(info: AudioOutputDeviceInfo) -> str
unreal.AudioMixerLibrary.get_available_audio_output_devices(world_context_object: Object, on_obtain_devices_event: OnAudioOutputDevicesObtained) -> None
unreal.AudioMixerLibrary.get_current_audio_output_device_name(world_context_object: Object, on_obtain_current_device_event: OnMainAudioOutputDeviceObtained) -> None
unreal.AudioMixerLibrary.get_magnitude_for_frequencies(world_context_object: Object, frequencies: Array[float], submix_to_analyze: SoundSubmix = None) -> Array[float]
unreal.AudioMixerLibrary.get_number_of_entries_in_source_effect_chain(world_context_object: Object, preset_chain: SoundEffectSourcePresetChain) -> int
unreal.AudioMixerLibrary.get_phase_for_frequencies(world_context_object: Object, frequencies: Array[float], submix_to_analyze: SoundSubmix = None) -> Array[float]
unreal.AudioMixerLibrary.is_audio_bus_active(world_context_object: Object, audio_bus: AudioBus) -> bool
unreal.AudioMixerLibrary.make_full_spectrum_spectral_analysis_band_settings(num_bands: int = 30, minimum_frequency: float = 40.000000, maximum_frequency: float = 16000.000000, attack_time_msec: int = 10, release_time_msec: int = 10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
unreal.AudioMixerLibrary.make_musical_spectral_analysis_band_settings(num_semitones: int = 60, starting_musical_note: MusicalNoteName = MusicalNoteName.C, starting_octave: int = 2, attack_time_msec: int = 10, release_time_msec: int = 10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
unreal.AudioMixerLibrary.make_preset_spectral_analysis_band_settings(band_preset_type: AudioSpectrumBandPresetType, num_bands: int = 10, attack_time_msec: int = 10, release_time_msec: int = 10) -> Array[SoundSubmixSpectralAnalysisBandSettings]
unreal.AudioMixerLibrary.pause_recording_output(world_context_object: Object, submix_to_pause: SoundSubmix = None) -> None
unreal.AudioMixerLibrary.prime_sound_cue_for_playback(sound_cue: SoundCue) -> None
unreal.AudioMixerLibrary.prime_sound_for_playback(sound_wave: SoundWave, on_load_completion: OnSoundLoadComplete) -> None
unreal.AudioMixerLibrary.register_audio_bus_to_submix(world_context_object: Object, sound_submix: SoundSubmix, audio_bus: AudioBus) -> None
unreal.AudioMixerLibrary.remove_master_submix_effect(world_context_object: Object, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.remove_source_effect_from_preset_chain(world_context_object: Object, preset_chain: SoundEffectSourcePresetChain, entry_index: int) -> None
unreal.AudioMixerLibrary.remove_submix_effect(world_context_object: Object, sound_submix: SoundSubmix, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.remove_submix_effect_at_index(world_context_object: Object, sound_submix: SoundSubmix, submix_chain_index: int) -> None
unreal.AudioMixerLibrary.remove_submix_effect_preset(world_context_object: Object, sound_submix: SoundSubmix, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.remove_submix_effect_preset_at_index(world_context_object: Object, sound_submix: SoundSubmix, submix_chain_index: int) -> None
unreal.AudioMixerLibrary.replace_sound_effect_submix(world_context_object: Object, sound_submix: SoundSubmix, submix_chain_index: int, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.replace_submix_effect(world_context_object: Object, sound_submix: SoundSubmix, submix_chain_index: int, submix_effect_preset: SoundEffectSubmixPreset) -> None
unreal.AudioMixerLibrary.resume_recording_output(world_context_object: Object, submix_to_pause: SoundSubmix = None) -> None
unreal.AudioMixerLibrary.set_bypass_source_effect_chain_entry(world_context_object: Object, preset_chain: SoundEffectSourcePresetChain, entry_index: int, bypassed: bool) -> None
unreal.AudioMixerLibrary.set_submix_effect_chain_override(world_context_object: Object, sound_submix: SoundSubmix, submix_effect_preset_chain: Array[SoundEffectSubmixPreset], fade_time_sec: float) -> None
unreal.AudioMixerLibrary.start_analyzing_output(world_context_object: Object, submix_to_analyze: SoundSubmix = None, fft_size: FFTSize = FFTSize.DEFAULT_SIZE, interpolation_method: FFTPeakInterpolationMethod = FFTPeakInterpolationMethod.LINEAR, window_type: FFTWindowType = FFTWindowType.HANN, hop_size: float = 0.000000, spectrum_type: AudioSpectrumType = AudioSpectrumType.MAGNITUDE_SPECTRUM) -> None
unreal.AudioMixerLibrary.start_audio_bus(world_context_object: Object, audio_bus: AudioBus) -> None
unreal.AudioMixerLibrary.start_recording_output(world_context_object: Object, expected_duration: float, submix_to_record: SoundSubmix = None) -> None
unreal.AudioMixerLibrary.stop_analyzing_output(world_context_object: Object, submix_to_stop_analyzing: SoundSubmix = None) -> None
unreal.AudioMixerLibrary.stop_audio_bus(world_context_object: Object, audio_bus: AudioBus) -> None
unreal.AudioMixerLibrary.stop_recording_output(world_context_object: Object, export_type: AudioRecordingExportType, name: str, path: str, submix_to_record: SoundSubmix = None, existing_sound_wave_to_overwrite: SoundWave = None) -> SoundWave
unreal.AudioMixerLibrary.swap_audio_output_device(world_context_object: Object, new_device_id: str, on_completed_device_swap: OnCompletedDeviceSwap) -> None
unreal.AudioMixerLibrary.trim_audio_cache(megabytes_to_free: float) -> float
unreal.AudioMixerLibrary.unregister_audio_bus_from_submix(world_context_object: Object, sound_submix: SoundSubmix, audio_bus: AudioBus) -> None
```

## `unreal.AudioOscilloscope(Widget)`

```python
unreal.AudioOscilloscope.amplitude_grid_labels_unit() -> YAxisLabelsUnit
unreal.AudioOscilloscope.analysis_period_ms() -> float
unreal.AudioOscilloscope.audio_bus() -> AudioBus
unreal.AudioOscilloscope.channel_to_analyze() -> int
unreal.AudioOscilloscope.max_time_window_ms() -> float
unreal.AudioOscilloscope.oscilloscope_style() -> AudioOscilloscopePanelStyle
unreal.AudioOscilloscope.panel_layout_type() -> AudioPanelLayoutType
unreal.AudioOscilloscope.show_amplitude_grid() -> bool
unreal.AudioOscilloscope.show_amplitude_labels() -> bool
unreal.AudioOscilloscope.show_time_grid() -> bool
unreal.AudioOscilloscope.start_processing() -> None
unreal.AudioOscilloscope.stop_processing() -> None
unreal.AudioOscilloscope.time_grid_labels_unit() -> XAxisLabelsUnit
unreal.AudioOscilloscope.time_window_ms() -> float
unreal.AudioOscilloscope.trigger_mode() -> AudioOscilloscopeTriggerMode
unreal.AudioOscilloscope.trigger_threshold() -> float
```

## `unreal.AudioOscilloscope_GetOscilloscopeAudioSamples(DelegateBase)`

```python
unreal.AudioOscilloscope_GetOscilloscopeAudioSamples.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioOutputDeviceInfo(StructBase)`

```python
unreal.AudioOutputDeviceInfo.__init__(name: str = "", device_id: str = "", num_channels: int = 0, sample_rate: int = 0, format: AudioMixerStreamDataFormatType = AudioMixerStreamDataFormatType.UNKNOWN, output_channel_array: Array[AudioMixerChannelType] = [], is_system_default: bool = False, is_current_device: bool = False) -> None
unreal.AudioOutputDeviceInfo.device_id() -> str
unreal.AudioOutputDeviceInfo.format() -> AudioMixerStreamDataFormatType
unreal.AudioOutputDeviceInfo.is_current_device() -> bool
unreal.AudioOutputDeviceInfo.is_system_default() -> bool
unreal.AudioOutputDeviceInfo.name() -> str
unreal.AudioOutputDeviceInfo.num_channels() -> int
unreal.AudioOutputDeviceInfo.output_channel_array() -> Array[AudioMixerChannelType]
unreal.AudioOutputDeviceInfo.sample_rate() -> int
```

## `unreal.AudioParameter(StructBase)`

```python
unreal.AudioParameter.__init__(param_name: Name = "None", float_param: float = 0.000000, bool_param: bool = False, int_param: int = 0, object_param: Object = None, string_param: str = "", array_float_param: Array[float] = [], array_bool_param: Array[bool] = [], array_int_param: Array[int] = [], array_object_param: Array[Object] = [], array_string_param: Array[str] = [], param_type: AudioParameterType = AudioParameterType.NONE) -> None
unreal.AudioParameter.array_bool_param(value: Array[bool]) -> None
unreal.AudioParameter.array_float_param(value: Array[float]) -> None
unreal.AudioParameter.array_int_param(value: Array[int]) -> None
unreal.AudioParameter.array_object_param(value: Array[Object]) -> None
unreal.AudioParameter.array_string_param(value: Array[str]) -> None
unreal.AudioParameter.bool_param(value: bool) -> None
unreal.AudioParameter.float_param(value: float) -> None
unreal.AudioParameter.int_param(value: int) -> None
unreal.AudioParameter.object_param(value: Object) -> None
unreal.AudioParameter.param_name(value: Name) -> None
unreal.AudioParameter.param_type(value: AudioParameterType) -> None
unreal.AudioParameter.sound_wave_param(value: Object) -> None
unreal.AudioParameter.string_param(value: str) -> None
```

## `unreal.AudioParameterControllerInterface(Interface)`

```python
unreal.AudioParameterControllerInterface.reset_parameters() -> None
unreal.AudioParameterControllerInterface.set_bool_array_parameter(name: Name, value: Array[bool]) -> None
unreal.AudioParameterControllerInterface.set_bool_parameter(name: Name, bool: bool) -> None
unreal.AudioParameterControllerInterface.set_float_array_parameter(name: Name, value: Array[float]) -> None
unreal.AudioParameterControllerInterface.set_float_parameter(name: Name, float: float) -> None
unreal.AudioParameterControllerInterface.set_int_array_parameter(name: Name, value: Array[int]) -> None
unreal.AudioParameterControllerInterface.set_int_parameter(name: Name, int: int) -> None
unreal.AudioParameterControllerInterface.set_object_array_parameter(name: Name, value: Array[Object]) -> None
unreal.AudioParameterControllerInterface.set_object_parameter(name: Name, value: Object) -> None
unreal.AudioParameterControllerInterface.set_parameters_blueprint(parameters: Array[AudioParameter]) -> None
unreal.AudioParameterControllerInterface.set_string_array_parameter(name: Name, value: Array[str]) -> None
unreal.AudioParameterControllerInterface.set_string_parameter(name: Name, value: str) -> None
unreal.AudioParameterControllerInterface.set_trigger_parameter(name: Name) -> None
```

## `unreal.AudioParameterConversionStatics(BlueprintFunctionLibrary)`

```python
unreal.AudioParameterConversionStatics.boolean_array_to_audio_parameter(name: Name, bools: Array[bool]) -> AudioParameter
unreal.AudioParameterConversionStatics.boolean_to_audio_parameter(name: Name, bool: bool) -> AudioParameter
unreal.AudioParameterConversionStatics.float_array_to_audio_parameter(name: Name, floats: Array[float]) -> AudioParameter
unreal.AudioParameterConversionStatics.float_to_audio_parameter(name: Name, float: float) -> AudioParameter
unreal.AudioParameterConversionStatics.integer_array_to_audio_parameter(name: Name, integers: Array[int]) -> AudioParameter
unreal.AudioParameterConversionStatics.integer_to_audio_parameter(name: Name, integer: int) -> AudioParameter
unreal.AudioParameterConversionStatics.object_array_to_audio_parameter(name: Name, objects: Array[Object]) -> AudioParameter
unreal.AudioParameterConversionStatics.object_to_audio_parameter(name: Name, object: Object) -> AudioParameter
unreal.AudioParameterConversionStatics.string_array_to_audio_parameter(name: Name, strings: Array[str]) -> AudioParameter
unreal.AudioParameterConversionStatics.string_to_audio_parameter(name: Name, string: str) -> AudioParameter
```

## `unreal.AudioPropertiesSheetAssetBase(Object)`

```python
unreal.AudioPropertiesSheetAssetBase.copy_to_object_properties(target_object: Object) -> bool
```

## `unreal.AudioRadialSlider(Widget)`

```python
unreal.AudioRadialSlider.get_output_value(slider_value: float) -> float
unreal.AudioRadialSlider.get_slider_value(output_value: float) -> float
unreal.AudioRadialSlider.on_value_changed(value: OnAudioRadialSliderValueChangedEvent) -> None
unreal.AudioRadialSlider.set_center_background_color(value: LinearColor) -> None
unreal.AudioRadialSlider.set_hand_start_end_ratio(hand_start_end_ratio: Vector2D) -> None
unreal.AudioRadialSlider.set_output_range(output_range: Vector2D) -> None
unreal.AudioRadialSlider.set_show_label_only_on_hover(show_label_only_on_hover: bool) -> None
unreal.AudioRadialSlider.set_show_units_text(show_units_text: bool) -> None
unreal.AudioRadialSlider.set_slider_bar_color(value: LinearColor) -> None
unreal.AudioRadialSlider.set_slider_progress_color(value: LinearColor) -> None
unreal.AudioRadialSlider.set_slider_thickness(thickness: float) -> None
unreal.AudioRadialSlider.set_text_label_background_color(color: SlateColor) -> None
unreal.AudioRadialSlider.set_units_text(units: Text) -> None
unreal.AudioRadialSlider.set_units_text_read_only(is_read_only: bool) -> None
unreal.AudioRadialSlider.set_value_text_read_only(is_read_only: bool) -> None
unreal.AudioRadialSlider.set_widget_layout(layout: AudioRadialSliderLayout) -> None
```

## `unreal.AudioRadialSliderStyle(SlateWidgetStyle)`

```python
unreal.AudioRadialSliderStyle.__init__(text_box_style: AudioTextBoxStyle = [[[[0.000000, 0.000000, 0.000000, 0.000000], 0], SlateBrushDrawType.ROUNDED_BOX, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[4.000000, 4.000000, 4.000000, 4.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.FIXED_RADIUS, False]], [[0.000000, 0.000000, 0.000000, 0.000000], 0]], center_background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], slider_bar_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], slider_progress_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], label_padding: float = 0.000000, default_slider_radius: float = 0.000000) -> None
unreal.AudioRadialSliderStyle.center_background_color(value: SlateColor) -> None
unreal.AudioRadialSliderStyle.default_slider_radius(value: float) -> None
unreal.AudioRadialSliderStyle.label_padding(value: float) -> None
unreal.AudioRadialSliderStyle.slider_bar_color(value: SlateColor) -> None
unreal.AudioRadialSliderStyle.slider_progress_color(value: SlateColor) -> None
unreal.AudioRadialSliderStyle.text_box_style(value: AudioTextBoxStyle) -> None
```

## `unreal.AudioSlider(AudioSliderBase)`

```python
unreal.AudioSlider.lin_to_output_curve(value: CurveFloat) -> None
unreal.AudioSlider.output_to_lin_curve(value: CurveFloat) -> None
```

## `unreal.AudioSliderBase(Widget)`

```python
unreal.AudioSliderBase.get_lin_value(output_value: float) -> float
unreal.AudioSliderBase.get_output_value(slider_value: float) -> float
unreal.AudioSliderBase.get_slider_value(output_value: float) -> float
unreal.AudioSliderBase.on_value_changed(value: OnFloatValueChangedEvent) -> None
unreal.AudioSliderBase.orientation() -> Orientation
unreal.AudioSliderBase.set_show_label_only_on_hover(show_label_only_on_hover: bool) -> None
unreal.AudioSliderBase.set_show_units_text(show_units_text: bool) -> None
unreal.AudioSliderBase.set_slider_background_color(value: LinearColor) -> None
unreal.AudioSliderBase.set_slider_bar_color(value: LinearColor) -> None
unreal.AudioSliderBase.set_slider_thumb_color(value: LinearColor) -> None
unreal.AudioSliderBase.set_text_label_background_color(color: SlateColor) -> None
unreal.AudioSliderBase.set_units_text(units: Text) -> None
unreal.AudioSliderBase.set_units_text_read_only(is_read_only: bool) -> None
unreal.AudioSliderBase.set_value_text_read_only(is_read_only: bool) -> None
unreal.AudioSliderBase.set_widget_background_color(value: LinearColor) -> None
```

## `unreal.AudioSliderStyle(SlateWidgetStyle)`

```python
unreal.AudioSliderStyle.__init__(slider_style: SliderStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 2.000000], text_box_style: AudioTextBoxStyle = [[[[0.000000, 0.000000, 0.000000, 0.000000], 0], SlateBrushDrawType.ROUNDED_BOX, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[4.000000, 4.000000, 4.000000, 4.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.FIXED_RADIUS, False]], [[0.000000, 0.000000, 0.000000, 0.000000], 0]], widget_background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], slider_background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], slider_background_size: Vector2D = [0.000000, 0.000000], label_padding: float = 0.000000, slider_bar_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], slider_thumb_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], widget_background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED]) -> None
unreal.AudioSliderStyle.label_padding(value: float) -> None
unreal.AudioSliderStyle.slider_background_color(value: SlateColor) -> None
unreal.AudioSliderStyle.slider_background_size(value: Vector2D) -> None
unreal.AudioSliderStyle.slider_bar_color(value: SlateColor) -> None
unreal.AudioSliderStyle.slider_style(value: SliderStyle) -> None
unreal.AudioSliderStyle.slider_thumb_color(value: SlateColor) -> None
unreal.AudioSliderStyle.text_box_style(value: AudioTextBoxStyle) -> None
unreal.AudioSliderStyle.widget_background_color(value: SlateColor) -> None
unreal.AudioSliderStyle.widget_background_image(value: SlateBrush) -> None
```

## `unreal.AudioSpectrumPlotStyle(SlateWidgetStyle)`

```python
unreal.AudioSpectrumPlotStyle.__init__(background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], grid_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], axis_label_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], axis_label_font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000], spectrum_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], crosshair_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], crosshair_label_font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000]) -> None
unreal.AudioSpectrumPlotStyle.axis_label_color(value: SlateColor) -> None
unreal.AudioSpectrumPlotStyle.axis_label_font(value: SlateFontInfo) -> None
unreal.AudioSpectrumPlotStyle.background_color(value: SlateColor) -> None
unreal.AudioSpectrumPlotStyle.crosshair_color(value: SlateColor) -> None
unreal.AudioSpectrumPlotStyle.crosshair_label_font(value: SlateFontInfo) -> None
unreal.AudioSpectrumPlotStyle.grid_color(value: SlateColor) -> None
unreal.AudioSpectrumPlotStyle.spectrum_color(value: SlateColor) -> None
```

## `unreal.AudioTextBoxStyle(SlateWidgetStyle)`

```python
unreal.AudioTextBoxStyle.__init__(background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED]) -> None
unreal.AudioTextBoxStyle.background_color(value: SlateColor) -> None
unreal.AudioTextBoxStyle.background_image(value: SlateBrush) -> None
```

## `unreal.AudioVectorscope(Widget)`

```python
unreal.AudioVectorscope.audio_bus() -> AudioBus
unreal.AudioVectorscope.display_persistence_ms() -> float
unreal.AudioVectorscope.grid_divisions() -> int
unreal.AudioVectorscope.max_display_persistence_ms() -> float
unreal.AudioVectorscope.panel_layout_type() -> AudioPanelLayoutType
unreal.AudioVectorscope.scale() -> float
unreal.AudioVectorscope.show_grid() -> bool
unreal.AudioVectorscope.start_processing() -> None
unreal.AudioVectorscope.stop_processing() -> None
unreal.AudioVectorscope.vectorscope_style() -> AudioVectorscopePanelStyle
```

## `unreal.AudioVectorscope_GetVectorscopeAudioSamples(DelegateBase)`

```python
unreal.AudioVectorscope_GetVectorscopeAudioSamples.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioVolume(Volume)`

```python
unreal.AudioVolume.ambient_zone_settings() -> InteriorSettings
unreal.AudioVolume.enabled() -> bool
unreal.AudioVolume.priority() -> float
unreal.AudioVolume.set_enabled(new_enabled: bool) -> None
unreal.AudioVolume.set_interior_settings(new_interior_settings: InteriorSettings) -> None
unreal.AudioVolume.set_priority(new_priority: float) -> None
unreal.AudioVolume.set_reverb_settings(new_reverb_settings: ReverbSettings) -> None
unreal.AudioVolume.set_submix_override_settings(new_submix_override_settings: Array[AudioVolumeSubmixOverrideSettings]) -> None
unreal.AudioVolume.set_submix_send_settings(new_submix_send_settings: Array[AudioVolumeSubmixSendSettings]) -> None
unreal.AudioVolume.settings() -> ReverbSettings
unreal.AudioVolume.submix_override_settings() -> Array[AudioVolumeSubmixOverrideSettings]
unreal.AudioVolume.submix_send_settings() -> Array[AudioVolumeSubmixSendSettings]
```

## `unreal.AudioVolumeSubmixOverrideSettings(StructBase)`

```python
unreal.AudioVolumeSubmixOverrideSettings.__init__(submix: SoundSubmix = None, submix_effect_chain: Array[SoundEffectSubmixPreset] = [], crossfade_time: float = 0.000000) -> None
unreal.AudioVolumeSubmixOverrideSettings.crossfade_time() -> float
unreal.AudioVolumeSubmixOverrideSettings.submix(value: SoundSubmix) -> None
unreal.AudioVolumeSubmixOverrideSettings.submix_effect_chain() -> Array[SoundEffectSubmixPreset]
```

## `unreal.AudioVolumeSubmixSendSettings(StructBase)`

```python
unreal.AudioVolumeSubmixSendSettings.__init__(listener_location_state: AudioVolumeLocationState = AudioVolumeLocationState.INSIDE_THE_VOLUME, submix_sends: Array[SoundSubmixSendInfo] = []) -> None
unreal.AudioVolumeSubmixSendSettings.listener_location_state(value: AudioVolumeLocationState) -> None
unreal.AudioVolumeSubmixSendSettings.submix_sends(value: Array[SoundSubmixSendInfo]) -> None
```

## `unreal.EpicSynth1Patch(StructBase)`

```python
unreal.EpicSynth1Patch.__init__(patch_source: Synth1PatchSource = Synth1PatchSource.LFO1, patch_cables: Array[Synth1PatchCable] = []) -> None
unreal.EpicSynth1Patch.patch_cables(value: Array[Synth1PatchCable]) -> None
unreal.EpicSynth1Patch.patch_source(value: Synth1PatchSource) -> None
```

## `unreal.GameplayCueNotify_SoundInfo(StructBase)`

```python
unreal.GameplayCueNotify_SoundInfo.__init__(spawn_condition_override: GameplayCueNotify_SpawnCondition = [GameplayCueNotify_LocallyControlledSource.INSTIGATOR_ACTOR, GameplayCueNotify_LocallyControlledPolicy.ALWAYS, 1.000000, [], []], placement_info_override: GameplayCueNotify_PlacementInfo = ["None", GameplayCueNotify_AttachPolicy.DO_NOT_ATTACH, AttachmentRule.KEEP_WORLD, False, True, [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], sound: SoundBase = None, looping_fade_out_duration: float = 0.000000, looping_fade_volume_level: float = 0.000000, sound_parameter_interface_info: GameplayCueNotify_SoundParameterInterfaceInfo = ["OnStop"], override_spawn_condition: bool = False, override_placement_info: bool = False, use_sound_parameter_interface: bool = False) -> None
unreal.GameplayCueNotify_SoundInfo.looping_fade_out_duration() -> float
unreal.GameplayCueNotify_SoundInfo.looping_fade_volume_level() -> float
unreal.GameplayCueNotify_SoundInfo.override_placement_info() -> bool
unreal.GameplayCueNotify_SoundInfo.override_spawn_condition() -> bool
unreal.GameplayCueNotify_SoundInfo.placement_info_override() -> GameplayCueNotify_PlacementInfo
unreal.GameplayCueNotify_SoundInfo.sound() -> SoundBase
unreal.GameplayCueNotify_SoundInfo.sound_cue(value: SoundBase) -> None
unreal.GameplayCueNotify_SoundInfo.sound_parameter_interface_info() -> GameplayCueNotify_SoundParameterInterfaceInfo
unreal.GameplayCueNotify_SoundInfo.spawn_condition_override() -> GameplayCueNotify_SpawnCondition
unreal.GameplayCueNotify_SoundInfo.use_sound_parameter_interface() -> bool
```

## `unreal.GameplayCueNotify_SoundParameterInterfaceInfo(StructBase)`

```python
unreal.GameplayCueNotify_SoundParameterInterfaceInfo.__init__(stop_trigger_name: Name = "None") -> None
unreal.GameplayCueNotify_SoundParameterInterfaceInfo.stop_trigger_name() -> Name
```

## `unreal.GranularSynth(SynthComponent)`

```python
unreal.GranularSynth.get_current_playhead_time() -> float
unreal.GranularSynth.get_sample_duration() -> float
unreal.GranularSynth.is_loaded() -> bool
unreal.GranularSynth.note_off(note: float, kill: bool = False) -> None
unreal.GranularSynth.note_on(note: float, velocity: int, duration: float = -1.000000) -> None
unreal.GranularSynth.set_attack_time(attack_time_msec: float) -> None
unreal.GranularSynth.set_decay_time(decay_time_msec: float) -> None
unreal.GranularSynth.set_grain_duration(base_duration_msec: float, duration_range: Vector2D = [0.000000, 0.000000]) -> None
unreal.GranularSynth.set_grain_envelope_type(envelope_type: GranularSynthEnvelopeType) -> None
unreal.GranularSynth.set_grain_pan(base_pan: float, pan_range: Vector2D = [0.000000, 0.000000]) -> None
unreal.GranularSynth.set_grain_pitch(base_pitch: float, pitch_range: Vector2D = [0.000000, 0.000000]) -> None
unreal.GranularSynth.set_grain_probability(grain_probability: float) -> None
unreal.GranularSynth.set_grain_volume(base_volume: float, volume_range: Vector2D = [0.000000, 0.000000]) -> None
unreal.GranularSynth.set_grains_per_second(grains_per_second: float) -> None
unreal.GranularSynth.set_playback_speed(playhead_rate: float) -> None
unreal.GranularSynth.set_playhead_time(position_sec: float, lerp_time_sec: float = 0.000000, seek_type: GranularSynthSeekType = GranularSynthSeekType.FROM_BEGINNING) -> None
unreal.GranularSynth.set_release_time_msec(release_time_msec: float) -> None
unreal.GranularSynth.set_scrub_mode(scrub_mode: bool) -> None
unreal.GranularSynth.set_sound_wave(sound_wave: SoundWave) -> None
unreal.GranularSynth.set_sustain_gain(sustain_gain: float) -> None
```

## `unreal.InitialActiveSoundParams(Object)`

```python
unreal.InitialActiveSoundParams.audio_params(value: Array[AudioParameter]) -> None
```

## `unreal.InputDeviceAudioBasedVibrationProperty(InputDeviceProperty)`

```python
unreal.InputDeviceAudioBasedVibrationProperty.data(value: AudioBasedVibrationData) -> None
unreal.InputDeviceAudioBasedVibrationProperty.device_override_data(value: Map[Name, AudioBasedVibrationData]) -> None
```

## `unreal.MasterAudioSubmixCaptureProtocol(MovieSceneAudioCaptureProtocolBase)`

```python
unreal.MasterAudioSubmixCaptureProtocol.file_name(value: str) -> None
```

## `unreal.MediaSoundComponent(SynthComponent)`

```python
unreal.MediaSoundComponent.get_attenuation_settings_to_apply() -> Optional[SoundAttenuationSettings]
unreal.MediaSoundComponent.get_envelope_value() -> float
unreal.MediaSoundComponent.get_media_player() -> MediaPlayer
unreal.MediaSoundComponent.get_normalized_spectral_data() -> Array[MediaSoundComponentSpectralData]
unreal.MediaSoundComponent.get_spectral_data() -> Array[MediaSoundComponentSpectralData]
unreal.MediaSoundComponent.set_enable_envelope_following(envelope_following: bool) -> None
unreal.MediaSoundComponent.set_enable_spectral_analysis(spectral_analysis_enabled: bool) -> None
unreal.MediaSoundComponent.set_envelope_followingsettings(attack_time_msec: int, release_time_msec: int) -> None
unreal.MediaSoundComponent.set_media_player(new_media_player: MediaPlayer) -> None
unreal.MediaSoundComponent.set_spectral_analysis_settings(frequencies_to_analyze: Array[float], fft_size: MediaSoundComponentFFTSize = MediaSoundComponentFFTSize.MEDIUM_512) -> None
```

## `unreal.MediaSoundComponentSpectralData(StructBase)`

```python
unreal.MediaSoundComponentSpectralData.__init__(frequency_hz: float = 0.000000, magnitude: float = 0.000000) -> None
unreal.MediaSoundComponentSpectralData.frequency_hz(value: float) -> None
unreal.MediaSoundComponentSpectralData.magnitude(value: float) -> None
```

## `unreal.MetaSoundAssetDirectory(StructBase)`

```python
unreal.MetaSoundAssetDirectory.__init__(directory: DirectoryPath = [""]) -> None
unreal.MetaSoundAssetDirectory.directory(value: DirectoryPath) -> None
```

## `unreal.MetaSoundBuilderBase(Object)`

```python
unreal.MetaSoundBuilderBase.add_graph_input_node(name: Name, data_type: Name, default_value: MetasoundFrontendLiteral, is_constructor_input: bool = False) -> Tuple[MetaSoundBuilderNodeOutputHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.add_graph_output_node(name: Name, data_type: Name, default_value: MetasoundFrontendLiteral, is_constructor_output: bool = False) -> Tuple[MetaSoundBuilderNodeInputHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.add_interface(interface_name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.add_node(node_class: MetaSoundDocumentInterface) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.add_node_by_class_name(class_name: MetasoundFrontendClassName, major_version: int = 1) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.build(parent: Object, options: MetaSoundBuilderOptions) -> MetaSoundDocumentInterface
unreal.MetaSoundBuilderBase.build_and_overwrite_meta_sound(existing_meta_sound: MetaSoundDocumentInterface, force_unique_class_name: bool = False) -> None
unreal.MetaSoundBuilderBase.build_new_meta_sound(name_base: Name) -> MetaSoundDocumentInterface
unreal.MetaSoundBuilderBase.class_name(value: MetasoundFrontendClassName) -> None
unreal.MetaSoundBuilderBase.connect_node_input_to_graph_input(graph_input_name: Name, node_input_handle: MetaSoundBuilderNodeInputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.connect_node_inputs_to_matching_graph_interface_inputs(node_handle: MetaSoundNodeHandle) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.connect_node_output_to_graph_output(graph_output_name: Name, node_output_handle: MetaSoundBuilderNodeOutputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.connect_node_outputs_to_matching_graph_interface_outputs(node_handle: MetaSoundNodeHandle) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.connect_nodes(node_output_handle: MetaSoundBuilderNodeOutputHandle, node_input_handle: MetaSoundBuilderNodeInputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.connect_nodes_by_interface_bindings(from_node_handle: MetaSoundNodeHandle, to_node_handle: MetaSoundNodeHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.contains_node(node: MetaSoundNodeHandle) -> bool
unreal.MetaSoundBuilderBase.contains_node_input(input: MetaSoundBuilderNodeInputHandle) -> bool
unreal.MetaSoundBuilderBase.contains_node_output(output: MetaSoundBuilderNodeOutputHandle) -> bool
unreal.MetaSoundBuilderBase.convert_from_preset() -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.convert_to_preset(referenced_node_class: MetaSoundDocumentInterface) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.disconnect_node_input(node_input_handle: MetaSoundBuilderNodeInputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.disconnect_node_output(node_output_handle: MetaSoundBuilderNodeOutputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.disconnect_nodes(node_output_handle: MetaSoundBuilderNodeOutputHandle, node_input_handle: MetaSoundBuilderNodeInputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.disconnect_nodes_by_interface_bindings(from_node_handle: MetaSoundNodeHandle, to_node_handle: MetaSoundNodeHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.find_graph_input_node(input_name: Name) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_graph_output_node(output_name: Name) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_interface_input_nodes(interface_name: Name) -> Tuple[Array[MetaSoundNodeHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_interface_output_nodes(interface_name: Name) -> Tuple[Array[MetaSoundNodeHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_class_version(node_handle: MetaSoundNodeHandle) -> Tuple[MetasoundFrontendVersion, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_input_by_name(node_handle: MetaSoundNodeHandle, input_name: Name) -> Tuple[MetaSoundBuilderNodeInputHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_input_parent(input_handle: MetaSoundBuilderNodeInputHandle) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_inputs(node_handle: MetaSoundNodeHandle) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_inputs_by_data_type(node_handle: MetaSoundNodeHandle, data_type: Name) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_output_by_name(node_handle: MetaSoundNodeHandle, output_name: Name) -> Tuple[MetaSoundBuilderNodeOutputHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_output_parent(output_handle: MetaSoundBuilderNodeOutputHandle) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_outputs(node_handle: MetaSoundNodeHandle) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.find_node_outputs_by_data_type(node_handle: MetaSoundNodeHandle, data_type: Name) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.get_node_input_class_default(input_handle: MetaSoundBuilderNodeInputHandle) -> Tuple[MetasoundFrontendLiteral, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.get_node_input_data(input_handle: MetaSoundBuilderNodeInputHandle) -> Tuple[Name, Name, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.get_node_input_default(input_handle: MetaSoundBuilderNodeInputHandle) -> Tuple[MetasoundFrontendLiteral, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.get_node_input_is_constructor_pin(input_handle: MetaSoundBuilderNodeInputHandle) -> bool
unreal.MetaSoundBuilderBase.get_node_output_data(output_handle: MetaSoundBuilderNodeOutputHandle) -> Tuple[Name, Name, MetaSoundBuilderResult]
unreal.MetaSoundBuilderBase.get_node_output_is_constructor_pin(output_handle: MetaSoundBuilderNodeOutputHandle) -> bool
unreal.MetaSoundBuilderBase.get_referenced_preset_asset() -> Object
unreal.MetaSoundBuilderBase.get_root_graph_class_name() -> MetasoundFrontendClassName
unreal.MetaSoundBuilderBase.interface_is_declared(interface_name: Name) -> bool
unreal.MetaSoundBuilderBase.is_attached(value: bool) -> None
unreal.MetaSoundBuilderBase.is_preset() -> bool
unreal.MetaSoundBuilderBase.node_input_is_connected(input_handle: MetaSoundBuilderNodeInputHandle) -> bool
unreal.MetaSoundBuilderBase.node_output_is_connected(output_handle: MetaSoundBuilderNodeOutputHandle) -> bool
unreal.MetaSoundBuilderBase.nodes_are_connected(output_handle: MetaSoundBuilderNodeOutputHandle, input_handle: MetaSoundBuilderNodeInputHandle) -> bool
unreal.MetaSoundBuilderBase.remove_graph_input(name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.remove_graph_output(name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.remove_interface(interface_name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.remove_node(node_handle: MetaSoundNodeHandle, remove_unused_dependencies: bool = True) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.remove_node_input_default(input_handle: MetaSoundBuilderNodeInputHandle) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.remove_unused_dependencies() -> None
unreal.MetaSoundBuilderBase.set_graph_input_access_type(input_name: Name, access_type: MetasoundFrontendVertexAccessType) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_input_data_type(input_name: Name, data_type: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_input_default(input_name: Name, literal: MetasoundFrontendLiteral) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_input_name(input_name: Name, new_name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_output_access_type(output_name: Name, access_type: MetasoundFrontendVertexAccessType) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_output_data_type(output_name: Name, data_type: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_graph_output_name(output_name: Name, new_name: Name) -> MetaSoundBuilderResult
unreal.MetaSoundBuilderBase.set_node_input_default(node_input_handle: MetaSoundBuilderNodeInputHandle, literal: MetasoundFrontendLiteral) -> MetaSoundBuilderResult
```

## `unreal.MetaSoundBuilderOptions(StructBase)`

```python
unreal.MetaSoundBuilderOptions.__init__(name: Name = "None", force_unique_class_name: bool = False) -> None
unreal.MetaSoundBuilderOptions.force_unique_class_name(value: bool) -> None
unreal.MetaSoundBuilderOptions.name(value: Name) -> None
```

## `unreal.MetaSoundOutput(SoundGeneratorOutput)`

```python
unreal.MetaSoundOutput.__init__(name: Name = "None") -> None
```

## `unreal.MetaSoundPatch(Object)`

```python
unreal.MetaSoundPatch.graph(value: MetasoundEditorGraphBase) -> None
```

## `unreal.MetaSoundSource(SoundWaveProcedural)`

```python
unreal.MetaSoundSource.block_rate_override() -> PerPlatformFloat
unreal.MetaSoundSource.graph(value: MetasoundEditorGraphBase) -> None
unreal.MetaSoundSource.output_format() -> MetaSoundOutputAudioFormat
unreal.MetaSoundSource.quality_setting(value: Name) -> None
unreal.MetaSoundSource.sample_rate_override() -> PerPlatformInt
```

## `unreal.MetaSoundSourceBuilder(MetaSoundBuilderBase)`

```python
unreal.MetaSoundSourceBuilder.audition(parent: Object, audio_component: AudioComponent, on_create_generator: OnCreateAuditionGeneratorHandleDelegate, live_updates_enabled: bool = False) -> None
unreal.MetaSoundSourceBuilder.get_live_updates_enabled() -> bool
unreal.MetaSoundSourceBuilder.set_block_rate_override(block_rate: float) -> None
unreal.MetaSoundSourceBuilder.set_format(output_format: MetaSoundOutputAudioFormat) -> MetaSoundBuilderResult
unreal.MetaSoundSourceBuilder.set_quality(quality: Name) -> None
unreal.MetaSoundSourceBuilder.set_sample_rate_override(sample_rate: int) -> None
```

## `unreal.MetasoundFrontendClass(StructBase)`

```python
unreal.MetasoundFrontendClass.__init__() -> None
```

## `unreal.MetasoundFrontendClassEnvironmentVariable(StructBase)`

```python
unreal.MetasoundFrontendClassEnvironmentVariable.__init__() -> None
```

## `unreal.MetasoundFrontendClassInput(MetasoundFrontendClassVertex)`

```python
unreal.MetasoundFrontendClassInput.__init__() -> None
```

## `unreal.MetasoundFrontendClassInputDefault(StructBase)`

```python
unreal.MetasoundFrontendClassInputDefault.__init__() -> None
```

## `unreal.MetasoundFrontendClassInterface(StructBase)`

```python
unreal.MetasoundFrontendClassInterface.__init__() -> None
```

## `unreal.MetasoundFrontendClassMetadata(StructBase)`

```python
unreal.MetasoundFrontendClassMetadata.__init__() -> None
```

## `unreal.MetasoundFrontendClassName(StructBase)`

```python
unreal.MetasoundFrontendClassName.__init__(namespace: Name = "None", name: Name = "None", variant: Name = "None") -> None
unreal.MetasoundFrontendClassName.name(value: Name) -> None
unreal.MetasoundFrontendClassName.namespace(value: Name) -> None
unreal.MetasoundFrontendClassName.variant(value: Name) -> None
```

## `unreal.MetasoundFrontendClassOutput(MetasoundFrontendClassVertex)`

```python
unreal.MetasoundFrontendClassOutput.__init__() -> None
```

## `unreal.MetasoundFrontendClassVertex(MetasoundFrontendVertex)`

```python
unreal.MetasoundFrontendClassVertex.__init__() -> None
```

## `unreal.MetasoundFrontendDocument(StructBase)`

```python
unreal.MetasoundFrontendDocument.__init__() -> None
unreal.MetasoundFrontendDocument.archetype_version(value: MetasoundFrontendVersion) -> None
unreal.MetasoundFrontendDocument.interface_versions(value: Array[MetasoundFrontendVersion]) -> None
```

## `unreal.MetasoundFrontendDocumentMetadata(StructBase)`

```python
unreal.MetasoundFrontendDocumentMetadata.__init__() -> None
```

## `unreal.MetasoundFrontendLiteral(StructBase)`

```python
unreal.MetasoundFrontendLiteral.__init__() -> None
```

## `unreal.MetasoundFrontendVersion(StructBase)`

```python
unreal.MetasoundFrontendVersion.__init__(name: Name = "None", number: MetasoundFrontendVersionNumber = [1, 0]) -> None
unreal.MetasoundFrontendVersion.name() -> Name
unreal.MetasoundFrontendVersion.number() -> MetasoundFrontendVersionNumber
```

## `unreal.MetasoundFrontendVersionNumber(StructBase)`

```python
unreal.MetasoundFrontendVersionNumber.__init__(major: int = 0, minor: int = 0) -> None
unreal.MetasoundFrontendVersionNumber.major() -> int
unreal.MetasoundFrontendVersionNumber.minor() -> int
```

## `unreal.MetasoundFrontendVertex(StructBase)`

```python
unreal.MetasoundFrontendVertex.__init__() -> None
```

## `unreal.MetasoundFrontendVertexHandle(StructBase)`

```python
unreal.MetasoundFrontendVertexHandle.__init__() -> None
```

## `unreal.MetasoundFrontendVertexMetadata(StructBase)`

```python
unreal.MetasoundFrontendVertexMetadata.__init__() -> None
```

## `unreal.MetasoundGeneratorHandle(Object)`

```python
unreal.MetasoundGeneratorHandle.apply_parameter_pack(pack: MetasoundParameterPack) -> bool
unreal.MetasoundGeneratorHandle.create_meta_sound_generator_handle(on_component: AudioComponent) -> MetasoundGeneratorHandle
unreal.MetasoundGeneratorHandle.enable_runtime_render_timing(enable: bool) -> None
unreal.MetasoundGeneratorHandle.get_cpu_core_utilization() -> float
unreal.MetasoundGeneratorHandle.update_watchers() -> None
unreal.MetasoundGeneratorHandle.watch_output(output_name: Name, on_output_value_changed: OnMetasoundOutputValueChanged, analyzer_name: Name = "None", analyzer_output_name: Name = "None") -> bool
```

## `unreal.MetasoundParameterPack(Object)`

```python
unreal.MetasoundParameterPack.get_bool(parameter_name: Name) -> Optional[SetParamResult]
unreal.MetasoundParameterPack.get_float(parameter_name: Name) -> Tuple[float, SetParamResult]
unreal.MetasoundParameterPack.get_int(parameter_name: Name) -> Tuple[int, SetParamResult]
unreal.MetasoundParameterPack.get_string(parameter_name: Name) -> Tuple[str, SetParamResult]
unreal.MetasoundParameterPack.get_trigger(parameter_name: Name) -> Optional[SetParamResult]
unreal.MetasoundParameterPack.has_bool(parameter_name: Name) -> bool
unreal.MetasoundParameterPack.has_float(parameter_name: Name) -> bool
unreal.MetasoundParameterPack.has_int(parameter_name: Name) -> bool
unreal.MetasoundParameterPack.has_string(parameter_name: Name) -> bool
unreal.MetasoundParameterPack.has_trigger(parameter_name: Name) -> bool
unreal.MetasoundParameterPack.make_metasound_parameter_pack() -> MetasoundParameterPack
unreal.MetasoundParameterPack.set_bool(parameter_name: Name, value: bool, only_if_exists: bool = True) -> SetParamResult
unreal.MetasoundParameterPack.set_float(parameter_name: Name, value: float, only_if_exists: bool = True) -> SetParamResult
unreal.MetasoundParameterPack.set_int(parameter_name: Name, value: int, only_if_exists: bool = True) -> SetParamResult
unreal.MetasoundParameterPack.set_string(parameter_name: Name, value: str, only_if_exists: bool = True) -> SetParamResult
unreal.MetasoundParameterPack.set_trigger(parameter_name: Name, only_if_exists: bool = True) -> SetParamResult
```

## `unreal.ModularRigConnections(StructBase)`

```python
unreal.ModularRigConnections.__init__() -> None
```

## `unreal.ModularRigController(Object)`

```python
unreal.ModularRigController.add_module(module_name: Name, class_: Class, parent_module_path: str, setup_undo: bool = True) -> str
unreal.ModularRigController.auto_connect_modules(module_paths: Array[str], replace_existing_connections: bool, setup_undo: bool = True) -> bool
unreal.ModularRigController.auto_connect_secondary_connectors(connector_keys: Array[RigElementKey], replace_existing_connections: bool, setup_undo: bool = True) -> bool
unreal.ModularRigController.bind_module_variable(module_path: str, variable_name: Name, source_path: str, setup_undo: bool = True) -> bool
unreal.ModularRigController.can_connect_connector_to_element(connector_key: RigElementKey, target_key: RigElementKey) -> Optional[Text]
unreal.ModularRigController.connect_connector_to_element(connector_key: RigElementKey, target_key: RigElementKey, setup_undo: bool = True, auto_resolve_other_connectors: bool = True, check_valid_connection: bool = True) -> bool
unreal.ModularRigController.delete_module(module_path: str, setup_undo: bool = True) -> bool
unreal.ModularRigController.deselect_module(module_path: str) -> bool
unreal.ModularRigController.disconnect_connector(connector_key: RigElementKey, disconnect_sub_modules: bool = False, setup_undo: bool = True) -> bool
unreal.ModularRigController.disconnect_cyclic_connectors(setup_undo: bool = True) -> Array[RigElementKey]
unreal.ModularRigController.get_selected_modules() -> Array[str]
unreal.ModularRigController.mirror_module(module_path: str, settings: RigVMMirrorSettings, setup_undo: bool = True) -> str
unreal.ModularRigController.rename_module(module_path: str, new_name: Name, setup_undo: bool = True) -> str
unreal.ModularRigController.reparent_module(module_path: str, new_parent_module_path: str, setup_undo: bool = True) -> str
unreal.ModularRigController.select_module(module_path: str, selected: bool = True) -> bool
unreal.ModularRigController.set_config_value_in_module(module_path: str, variable_name: Name, value: str, setup_undo: bool = True) -> bool
unreal.ModularRigController.set_module_selection(module_paths: Array[str]) -> bool
unreal.ModularRigController.set_module_short_name(module_path: str, new_short_name: str, setup_undo: bool = True) -> bool
unreal.ModularRigController.swap_module_class(module_path: str, new_class: Class, setup_undo: bool = True) -> bool
unreal.ModularRigController.swap_modules_of_class(old_class: Class, new_class: Class, setup_undo: bool = True) -> bool
unreal.ModularRigController.un_bind_module_variable(module_path: str, variable_name: Name, setup_undo: bool = True) -> bool
```

## `unreal.ModularRigModel(StructBase)`

```python
unreal.ModularRigModel.__init__() -> None
```

## `unreal.ModularRigResolveResult(StructBase)`

```python
unreal.ModularRigResolveResult.__init__() -> None
```

## `unreal.ModularRigSettings(StructBase)`

```python
unreal.ModularRigSettings.__init__(auto_resolve: bool = False) -> None
unreal.ModularRigSettings.auto_resolve(value: bool) -> None
```

## `unreal.ModularRigSingleConnection(StructBase)`

```python
unreal.ModularRigSingleConnection.__init__() -> None
```

## `unreal.ModularSynthComponent(SynthComponent)`

```python
unreal.ModularSynthComponent.create_patch(patch_source: Synth1PatchSource, patch_cables: Array[Synth1PatchCable], enable_by_default: bool) -> PatchId
unreal.ModularSynthComponent.note_off(note: float, all_notes_off: bool = False, kill_all_notes: bool = False) -> None
unreal.ModularSynthComponent.note_on(note: float, velocity: int, duration: float = -1.000000) -> None
unreal.ModularSynthComponent.set_attack_time(attack_time_msec: float) -> None
unreal.ModularSynthComponent.set_chorus_depth(depth: float) -> None
unreal.ModularSynthComponent.set_chorus_enabled(enable_chorus: bool) -> None
unreal.ModularSynthComponent.set_chorus_feedback(feedback: float) -> None
unreal.ModularSynthComponent.set_chorus_frequency(frequency: float) -> None
unreal.ModularSynthComponent.set_decay_time(decay_time_msec: float) -> None
unreal.ModularSynthComponent.set_enable_legato(legato_enabled: bool) -> None
unreal.ModularSynthComponent.set_enable_patch(patch_id: PatchId, is_enabled: bool) -> bool
unreal.ModularSynthComponent.set_enable_polyphony(enable_polyphony: bool) -> None
unreal.ModularSynthComponent.set_enable_retrigger(retrigger_enabled: bool) -> None
unreal.ModularSynthComponent.set_enable_unison(enable_unison: bool) -> None
unreal.ModularSynthComponent.set_filter_algorithm(filter_algorithm: SynthFilterAlgorithm) -> None
unreal.ModularSynthComponent.set_filter_frequency(filter_frequency_hz: float) -> None
unreal.ModularSynthComponent.set_filter_frequency_mod(filter_frequency_hz: float) -> None
unreal.ModularSynthComponent.set_filter_q(filter_q: float) -> None
unreal.ModularSynthComponent.set_filter_q_mod(filter_q: float) -> None
unreal.ModularSynthComponent.set_filter_type(filter_type: SynthFilterType) -> None
unreal.ModularSynthComponent.set_gain_db(gain_db: float) -> None
unreal.ModularSynthComponent.set_lfo_frequency(lfo_index: int, frequency_hz: float) -> None
unreal.ModularSynthComponent.set_lfo_frequency_mod(lfo_index: int, frequency_mod_hz: float) -> None
unreal.ModularSynthComponent.set_lfo_gain(lfo_index: int, gain: float) -> None
unreal.ModularSynthComponent.set_lfo_gain_mod(lfo_index: int, gain_mod: float) -> None
unreal.ModularSynthComponent.set_lfo_mode(lfo_index: int, lfo_mode: SynthLFOMode) -> None
unreal.ModularSynthComponent.set_lfo_patch(lfo_index: int, lfo_patch_type: SynthLFOPatchType) -> None
unreal.ModularSynthComponent.set_lfo_type(lfo_index: int, lfo_type: SynthLFOType) -> None
unreal.ModularSynthComponent.set_mod_env_attack_time(attack_time_msec: float) -> None
unreal.ModularSynthComponent.set_mod_env_bias_invert(invert: bool) -> None
unreal.ModularSynthComponent.set_mod_env_bias_patch(patch_type: SynthModEnvBiasPatch) -> None
unreal.ModularSynthComponent.set_mod_env_decay_time(decay_time_msec: float) -> None
unreal.ModularSynthComponent.set_mod_env_depth(depth: float) -> None
unreal.ModularSynthComponent.set_mod_env_invert(invert: bool) -> None
unreal.ModularSynthComponent.set_mod_env_patch(patch_type: SynthModEnvPatch) -> None
unreal.ModularSynthComponent.set_mod_env_release_time(release: float) -> None
unreal.ModularSynthComponent.set_mod_env_sustain_gain(sustain_gain: float) -> None
unreal.ModularSynthComponent.set_osc_cents(osc_index: int, cents: float) -> None
unreal.ModularSynthComponent.set_osc_frequency_mod(osc_index: int, osc_freq_mod: float) -> None
unreal.ModularSynthComponent.set_osc_gain(osc_index: int, osc_gain: float) -> None
unreal.ModularSynthComponent.set_osc_gain_mod(osc_index: int, osc_gain_mod: float) -> None
unreal.ModularSynthComponent.set_osc_octave(osc_index: int, octave: float) -> None
unreal.ModularSynthComponent.set_osc_pulsewidth(osc_index: int, pulsewidth: float) -> None
unreal.ModularSynthComponent.set_osc_semitones(osc_index: int, semitones: float) -> None
unreal.ModularSynthComponent.set_osc_sync(is_synced: bool) -> None
unreal.ModularSynthComponent.set_osc_type(osc_index: int, osc_type: Synth1OscType) -> None
unreal.ModularSynthComponent.set_pan(pan: float) -> None
unreal.ModularSynthComponent.set_pitch_bend(pitch_bend: float) -> None
unreal.ModularSynthComponent.set_portamento(portamento: float) -> None
unreal.ModularSynthComponent.set_release_time(release_time_msec: float) -> None
unreal.ModularSynthComponent.set_spread(spread: float) -> None
unreal.ModularSynthComponent.set_stereo_delay_feedback(delay_feedback: float) -> None
unreal.ModularSynthComponent.set_stereo_delay_is_enabled(stereo_delay_enabled: bool) -> None
unreal.ModularSynthComponent.set_stereo_delay_mode(stereo_delay_mode: SynthStereoDelayMode) -> None
unreal.ModularSynthComponent.set_stereo_delay_ratio(delay_ratio: float) -> None
unreal.ModularSynthComponent.set_stereo_delay_time(delay_time_msec: float) -> None
unreal.ModularSynthComponent.set_stereo_delay_wetlevel(delay_wetlevel: float) -> None
unreal.ModularSynthComponent.set_sustain_gain(sustain_gain: float) -> None
unreal.ModularSynthComponent.set_synth_preset(synth_preset: ModularSynthPreset) -> None
unreal.ModularSynthComponent.voice_count() -> int
```

## `unreal.ModularSynthLibrary(BlueprintFunctionLibrary)`

```python
unreal.ModularSynthLibrary.add_modular_synth_preset_to_bank_asset(bank: ModularSynthPresetBank, preset: ModularSynthPreset, preset_name: str) -> None
```

## `unreal.ModularSynthPreset(TableRowBase)`

```python
unreal.ModularSynthPreset.__init__(enable_polyphony: bool = False, osc1_type: Synth1OscType = Synth1OscType.SINE, osc1_gain: float = 0.000000, osc1_octave: float = 0.000000, osc1_semitones: float = 0.000000, osc1_cents: float = 0.000000, osc1_pulse_width: float = 0.000000, osc2_type: Synth1OscType = Synth1OscType.SINE, osc2_gain: float = 0.000000, osc2_octave: float = 0.000000, osc2_semitones: float = 0.000000, osc2_cents: float = 0.000000, osc2_pulse_width: float = 0.000000, portamento: float = 0.000000, enable_unison: bool = False, enable_oscillator_sync: bool = False, spread: float = 0.000000, pan: float = 0.000000, lfo1_frequency: float = 0.000000, lfo1_gain: float = 0.000000, lfo1_type: SynthLFOType = SynthLFOType.SINE, lfo1_mode: SynthLFOMode = SynthLFOMode.SYNC, lfo1_patch_type: SynthLFOPatchType = SynthLFOPatchType.PATCH_TO_NONE, lfo2_frequency: float = 0.000000, lfo2_gain: float = 0.000000, lfo2_type: SynthLFOType = SynthLFOType.SINE, lfo2_mode: SynthLFOMode = SynthLFOMode.SYNC, lfo2_patch_type: SynthLFOPatchType = SynthLFOPatchType.PATCH_TO_NONE, gain_db: float = 0.000000, attack_time: float = 0.000000, decay_time: float = 0.000000, sustain_gain: float = 0.000000, release_time: float = 0.000000, mod_env_patch_type: SynthModEnvPatch = SynthModEnvPatch.PATCH_TO_NONE, mod_env_bias_patch_type: SynthModEnvBiasPatch = SynthModEnvBiasPatch.PATCH_TO_NONE, invert_modulation_envelope: bool = False, invert_modulation_envelope_bias: bool = False, modulation_envelope_depth: float = 0.000000, modulation_envelope_attack_time: float = 0.000000, modulation_envelope_decay_time: float = 0.000000, modulation_envelope_sustain_gain: float = 0.000000, modulation_envelope_release_time: float = 0.000000, legato: bool = False, retrigger: bool = False, filter_frequency: float = 0.000000, filter_q: float = 0.000000, filter_type: SynthFilterType = SynthFilterType.LOW_PASS, filter_algorithm: SynthFilterAlgorithm = SynthFilterAlgorithm.ONE_POLE, stereo_delay_enabled: bool = False, stereo_delay_mode: SynthStereoDelayMode = SynthStereoDelayMode.NORMAL, stereo_delay_time: float = 0.000000, stereo_delay_feedback: float = 0.000000, stereo_delay_wetlevel: float = 0.000000, stereo_delay_ratio: float = 0.000000, chorus_enabled: bool = False, chorus_depth: float = 0.000000, chorus_feedback: float = 0.000000, chorus_frequency: float = 0.000000, patches: Array[EpicSynth1Patch] = []) -> None
unreal.ModularSynthPreset.attack_time(value: float) -> None
unreal.ModularSynthPreset.chorus_depth(value: float) -> None
unreal.ModularSynthPreset.chorus_enabled(value: bool) -> None
unreal.ModularSynthPreset.chorus_feedback(value: float) -> None
unreal.ModularSynthPreset.chorus_frequency(value: float) -> None
unreal.ModularSynthPreset.decay_time(value: float) -> None
unreal.ModularSynthPreset.enable_oscillator_sync(value: bool) -> None
unreal.ModularSynthPreset.enable_polyphony(value: bool) -> None
unreal.ModularSynthPreset.enable_unison(value: bool) -> None
unreal.ModularSynthPreset.filter_algorithm(value: SynthFilterAlgorithm) -> None
unreal.ModularSynthPreset.filter_frequency(value: float) -> None
unreal.ModularSynthPreset.filter_q(value: float) -> None
unreal.ModularSynthPreset.filter_type(value: SynthFilterType) -> None
unreal.ModularSynthPreset.gain_db(value: float) -> None
unreal.ModularSynthPreset.invert_modulation_envelope(value: bool) -> None
unreal.ModularSynthPreset.invert_modulation_envelope_bias(value: bool) -> None
unreal.ModularSynthPreset.legato(value: bool) -> None
unreal.ModularSynthPreset.lfo1_frequency(value: float) -> None
unreal.ModularSynthPreset.lfo1_gain(value: float) -> None
unreal.ModularSynthPreset.lfo1_mode(value: SynthLFOMode) -> None
unreal.ModularSynthPreset.lfo1_patch_type(value: SynthLFOPatchType) -> None
unreal.ModularSynthPreset.lfo1_type(value: SynthLFOType) -> None
unreal.ModularSynthPreset.lfo2_frequency(value: float) -> None
unreal.ModularSynthPreset.lfo2_gain(value: float) -> None
unreal.ModularSynthPreset.lfo2_mode(value: SynthLFOMode) -> None
unreal.ModularSynthPreset.lfo2_patch_type(value: SynthLFOPatchType) -> None
unreal.ModularSynthPreset.lfo2_type(value: SynthLFOType) -> None
unreal.ModularSynthPreset.mod_env_bias_patch_type(value: SynthModEnvBiasPatch) -> None
unreal.ModularSynthPreset.mod_env_patch_type(value: SynthModEnvPatch) -> None
unreal.ModularSynthPreset.modulation_envelope_attack_time(value: float) -> None
unreal.ModularSynthPreset.modulation_envelope_decay_time(value: float) -> None
unreal.ModularSynthPreset.modulation_envelope_depth(value: float) -> None
unreal.ModularSynthPreset.modulation_envelope_release_time(value: float) -> None
unreal.ModularSynthPreset.modulation_envelope_sustain_gain(value: float) -> None
unreal.ModularSynthPreset.osc1_cents(value: float) -> None
unreal.ModularSynthPreset.osc1_gain(value: float) -> None
unreal.ModularSynthPreset.osc1_octave(value: float) -> None
unreal.ModularSynthPreset.osc1_pulse_width(value: float) -> None
unreal.ModularSynthPreset.osc1_semitones(value: float) -> None
unreal.ModularSynthPreset.osc1_type(value: Synth1OscType) -> None
unreal.ModularSynthPreset.osc2_cents(value: float) -> None
unreal.ModularSynthPreset.osc2_gain(value: float) -> None
unreal.ModularSynthPreset.osc2_octave(value: float) -> None
unreal.ModularSynthPreset.osc2_pulse_width(value: float) -> None
unreal.ModularSynthPreset.osc2_semitones(value: float) -> None
unreal.ModularSynthPreset.osc2_type(value: Synth1OscType) -> None
unreal.ModularSynthPreset.pan(value: float) -> None
unreal.ModularSynthPreset.patches(value: Array[EpicSynth1Patch]) -> None
unreal.ModularSynthPreset.portamento(value: float) -> None
unreal.ModularSynthPreset.release_time(value: float) -> None
unreal.ModularSynthPreset.retrigger(value: bool) -> None
unreal.ModularSynthPreset.spread(value: float) -> None
unreal.ModularSynthPreset.stereo_delay_enabled(value: bool) -> None
unreal.ModularSynthPreset.stereo_delay_feedback(value: float) -> None
unreal.ModularSynthPreset.stereo_delay_mode(value: SynthStereoDelayMode) -> None
unreal.ModularSynthPreset.stereo_delay_ratio(value: float) -> None
unreal.ModularSynthPreset.stereo_delay_time(value: float) -> None
unreal.ModularSynthPreset.stereo_delay_wetlevel(value: float) -> None
unreal.ModularSynthPreset.sustain_gain(value: float) -> None
```

## `unreal.ModularSynthPresetBank(Object)`

```python
unreal.ModularSynthPresetBank.presets(value: Array[ModularSynthPresetBankEntry]) -> None
```

## `unreal.ModularSynthPresetBankEntry(StructBase)`

```python
unreal.ModularSynthPresetBankEntry.__init__(preset_name: str = "", preset: ModularSynthPreset = [False, Synth1OscType.SAW, 1.000000, 0.000000, 0.000000, 0.000000, 0.500000, Synth1OscType.SAW, 1.000000, 0.000000, 0.000000, 2.500000, 0.500000, 0.000000, False, False, 0.500000, 0.000000, 1.000000, 0.000000, SynthLFOType.SINE, SynthLFOMode.SYNC, SynthLFOPatchType.PATCH_TO_NONE, 1.000000, 0.000000, SynthLFOType.SINE, SynthLFOMode.SYNC, SynthLFOPatchType.PATCH_TO_NONE, -3.000000, 10.000000, 100.000000, 0.707000, 5000.000000, SynthModEnvPatch.PATCH_TO_NONE, SynthModEnvBiasPatch.PATCH_TO_NONE, False, False, 1.000000, 10.000000, 100.000000, 0.707000, 5000.000000, True, False, 8000.000000, 2.000000, SynthFilterType.LOW_PASS, SynthFilterAlgorithm.LADDER, True, SynthStereoDelayMode.PING_PONG, 700.000000, 0.700000, 0.300000, 0.200000, False, 0.200000, 0.500000, 2.000000, []]) -> None
unreal.ModularSynthPresetBankEntry.preset(value: ModularSynthPreset) -> None
unreal.ModularSynthPresetBankEntry.preset_name(value: str) -> None
```

## `unreal.MonoWaveTableSynthPreset(Object)`

```python
unreal.MonoWaveTableSynthPreset.lock_keyframes_to_grid() -> int
unreal.MonoWaveTableSynthPreset.lock_keyframes_to_grid_bool() -> bool
unreal.MonoWaveTableSynthPreset.normalize_wave_tables(value: bool) -> None
unreal.MonoWaveTableSynthPreset.preset_name(value: str) -> None
unreal.MonoWaveTableSynthPreset.wave_table() -> Array[RuntimeFloatCurve]
unreal.MonoWaveTableSynthPreset.wave_table_resolution() -> int
```

## `unreal.MovieSceneAudioSection(MovieSceneSection)`

```python
unreal.MovieSceneAudioSection.get_attenuation_settings() -> SoundAttenuation
unreal.MovieSceneAudioSection.get_looping() -> bool
unreal.MovieSceneAudioSection.get_override_attenuation() -> bool
unreal.MovieSceneAudioSection.get_sound() -> SoundBase
unreal.MovieSceneAudioSection.get_start_offset() -> FrameNumber
unreal.MovieSceneAudioSection.get_suppress_subtitles() -> bool
unreal.MovieSceneAudioSection.set_attenuation_settings(attenuation_settings: SoundAttenuation) -> None
unreal.MovieSceneAudioSection.set_looping(looping: bool) -> None
unreal.MovieSceneAudioSection.set_override_attenuation(override_attenuation: bool) -> None
unreal.MovieSceneAudioSection.set_sound(sound: SoundBase) -> None
unreal.MovieSceneAudioSection.set_start_offset(start_offset: FrameNumber) -> None
unreal.MovieSceneAudioSection.set_suppress_subtitles(suppress_subtitles: bool) -> None
unreal.MovieSceneAudioSection.sound(value: SoundBase) -> None
```

## `unreal.OnAudioDefaultDeviceChanged(MulticastDelegateBase)`

```python
unreal.OnAudioDefaultDeviceChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioDeviceChange(MulticastDelegateBase)`

```python
unreal.OnAudioDeviceChange.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioDeviceStateChanged(MulticastDelegateBase)`

```python
unreal.OnAudioDeviceStateChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioFadeChangeSignature(MulticastDelegateBase)`

```python
unreal.OnAudioFadeChangeSignature.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioFinished(MulticastDelegateBase)`

```python
unreal.OnAudioFinished.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioInputDevicesObtained(DelegateBase)`

```python
unreal.OnAudioInputDevicesObtained.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioMultiEnvelopeValue(MulticastDelegateBase)`

```python
unreal.OnAudioMultiEnvelopeValue.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioOutputDevicesObtained(DelegateBase)`

```python
unreal.OnAudioOutputDevicesObtained.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioPlayStateChanged(MulticastDelegateBase)`

```python
unreal.OnAudioPlayStateChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioPlaybackPercent(MulticastDelegateBase)`

```python
unreal.OnAudioPlaybackPercent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioRadialSliderValueChangedEvent(MulticastDelegateBase)`

```python
unreal.OnAudioRadialSliderValueChangedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioSingleEnvelopeValue(MulticastDelegateBase)`

```python
unreal.OnAudioSingleEnvelopeValue.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnAudioVirtualizationChanged(MulticastDelegateBase)`

```python
unreal.OnAudioVirtualizationChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnControllerCaptureBeginEventSynth2D(MulticastDelegateBase)`

```python
unreal.OnControllerCaptureBeginEventSynth2D.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnControllerCaptureEndEventSynth2D(MulticastDelegateBase)`

```python
unreal.OnControllerCaptureEndEventSynth2D.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnFloatValueChangedEventSynth2D(MulticastDelegateBase)`

```python
unreal.OnFloatValueChangedEventSynth2D.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMainAudioOutputDeviceObtained(DelegateBase)`

```python
unreal.OnMainAudioOutputDeviceObtained.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMetasoundOutputValueChanged(DelegateBase)`

```python
unreal.OnMetasoundOutputValueChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMetasoundOutputValueChangedMulticast(MulticastDelegateBase)`

```python
unreal.OnMetasoundOutputValueChangedMulticast.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMouseCaptureBeginEventSynth2D(MulticastDelegateBase)`

```python
unreal.OnMouseCaptureBeginEventSynth2D.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnMouseCaptureEndEventSynth2D(MulticastDelegateBase)`

```python
unreal.OnMouseCaptureEndEventSynth2D.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQuartzCommandEvent(MulticastDelegateBase)`

```python
unreal.OnQuartzCommandEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQuartzCommandEventBP(DelegateBase)`

```python
unreal.OnQuartzCommandEventBP.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQuartzMetronomeEvent(MulticastDelegateBase)`

```python
unreal.OnQuartzMetronomeEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQuartzMetronomeEventBP(DelegateBase)`

```python
unreal.OnQuartzMetronomeEventBP.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnSoundLoadComplete(DelegateBase)`

```python
unreal.OnSoundLoadComplete.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnSynthEnvelopeValue(MulticastDelegateBase)`

```python
unreal.OnSynthEnvelopeValue.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PassiveSoundMixModifier(StructBase)`

```python
unreal.PassiveSoundMixModifier.__init__(sound_mix: SoundMix = None, min_volume_threshold: float = 0.000000, max_volume_threshold: float = 0.000000) -> None
unreal.PassiveSoundMixModifier.max_volume_threshold() -> float
unreal.PassiveSoundMixModifier.min_volume_threshold() -> float
unreal.PassiveSoundMixModifier.sound_mix() -> SoundMix
unreal.PassiveSoundMixModifier.volume_threshold() -> float
```

## `unreal.PixelStreaming51CloudAudioComponent(SynthComponent)`

```python
unreal.PixelStreaming51CloudAudioComponent.auto_find_peer(value: bool) -> None
unreal.PixelStreaming51CloudAudioComponent.is_listening_to_player() -> bool
unreal.PixelStreaming51CloudAudioComponent.listen_to(player_to_listen_to: str) -> bool
unreal.PixelStreaming51CloudAudioComponent.player_to_hear(value: str) -> None
unreal.PixelStreaming51CloudAudioComponent.reset() -> None
unreal.PixelStreaming51CloudAudioComponent.streamer_listen_to(streamer_id: str, player_to_listen_to: str) -> bool
unreal.PixelStreaming51CloudAudioComponent.streamer_to_hear(value: str) -> None
```

## `unreal.QuartzClockHandle(Object)`

```python
unreal.QuartzClockHandle.get_beat_progress_percent(quantization_boundary: QuartzCommandQuantization = QuartzCommandQuantization.BEAT, phase_offset: float = 0.000000, ms_offset: float = 0.000000) -> float
unreal.QuartzClockHandle.get_beats_per_minute(world_context_object: Object) -> float
unreal.QuartzClockHandle.get_current_timestamp(world_context_object: Object) -> QuartzTransportTimeStamp
unreal.QuartzClockHandle.get_duration_of_quantization_type_in_seconds(world_context_object: Object, quantization_type: QuartzCommandQuantization, multiplier: float = 1.000000) -> float
unreal.QuartzClockHandle.get_estimated_run_time(world_context_object: Object) -> float
unreal.QuartzClockHandle.get_milliseconds_per_tick(world_context_object: Object) -> float
unreal.QuartzClockHandle.get_seconds_per_tick(world_context_object: Object) -> float
unreal.QuartzClockHandle.get_thirty_second_notes_per_minute(world_context_object: Object) -> float
unreal.QuartzClockHandle.get_ticks_per_second(world_context_object: Object) -> float
unreal.QuartzClockHandle.is_clock_running(world_context_object: Object) -> bool
unreal.QuartzClockHandle.notify_on_quantization_boundary(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, ms_offset: float = 0.000000) -> None
unreal.QuartzClockHandle.pause_clock(world_context_object: Object) -> QuartzClockHandle
unreal.QuartzClockHandle.reset_transport(world_context_object: Object, delegate: OnQuartzCommandEventBP) -> None
unreal.QuartzClockHandle.reset_transport_quantized(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP) -> QuartzClockHandle
unreal.QuartzClockHandle.resume_clock(world_context_object: Object) -> QuartzClockHandle
unreal.QuartzClockHandle.set_beats_per_minute(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, beats_per_minute: float = 60.000000) -> QuartzClockHandle
unreal.QuartzClockHandle.set_milliseconds_per_tick(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, milliseconds_per_tick: float = 100.000000) -> QuartzClockHandle
unreal.QuartzClockHandle.set_seconds_per_tick(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, seconds_per_tick: float = 0.250000) -> QuartzClockHandle
unreal.QuartzClockHandle.set_thirty_second_notes_per_minute(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, thirty_seconds_notes_per_minute: float = 960.000000) -> QuartzClockHandle
unreal.QuartzClockHandle.set_ticks_per_second(world_context_object: Object, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP, ticks_per_second: float = 10.000000) -> QuartzClockHandle
unreal.QuartzClockHandle.start_clock(world_context_object: Object) -> QuartzClockHandle
unreal.QuartzClockHandle.start_other_clock(world_context_object: Object, other_clock_name: Name, quantization_boundary: QuartzQuantizationBoundary, delegate: OnQuartzCommandEventBP) -> None
unreal.QuartzClockHandle.stop_clock(world_context_object: Object, cancel_pending_events: bool) -> QuartzClockHandle
unreal.QuartzClockHandle.subscribe_to_all_quantization_events(world_context_object: Object, on_quantization_event: OnQuartzMetronomeEventBP) -> QuartzClockHandle
unreal.QuartzClockHandle.subscribe_to_quantization_event(world_context_object: Object, quantization_boundary: QuartzCommandQuantization, on_quantization_event: OnQuartzMetronomeEventBP) -> QuartzClockHandle
unreal.QuartzClockHandle.unsubscribe_from_all_time_divisions(world_context_object: Object) -> QuartzClockHandle
unreal.QuartzClockHandle.unsubscribe_from_time_division(world_context_object: Object, quantization_boundary: QuartzCommandQuantization) -> QuartzClockHandle
```

## `unreal.QuartzClockSettings(StructBase)`

```python
unreal.QuartzClockSettings.__init__(time_signature: QuartzTimeSignature = [4, QuartzTimeSignatureQuantization.QUARTER_NOTE, []], ignore_level_change: bool = False) -> None
unreal.QuartzClockSettings.ignore_level_change(value: bool) -> None
unreal.QuartzClockSettings.time_signature(value: QuartzTimeSignature) -> None
```

## `unreal.QuartzPulseOverrideStep(StructBase)`

```python
unreal.QuartzPulseOverrideStep.__init__(number_of_pulses: int = 0, pulse_duration: QuartzCommandQuantization = QuartzCommandQuantization.BAR) -> None
unreal.QuartzPulseOverrideStep.number_of_pulses(value: int) -> None
unreal.QuartzPulseOverrideStep.pulse_duration(value: QuartzCommandQuantization) -> None
```

## `unreal.QuartzQuantizationBoundary(StructBase)`

```python
unreal.QuartzQuantizationBoundary.__init__(quantization: QuartzCommandQuantization = QuartzCommandQuantization.BAR, multiplier: float = 0.000000, counting_reference_point: QuarztQuantizationReference = QuarztQuantizationReference.BAR_RELATIVE, fire_on_clock_start: bool = False, cancel_command_if_clock_is_not_running: bool = False, reset_clock_on_queued: bool = False, resume_clock_on_queued: bool = False) -> None
unreal.QuartzQuantizationBoundary.cancel_command_if_clock_is_not_running(value: bool) -> None
unreal.QuartzQuantizationBoundary.counting_reference_point(value: QuarztQuantizationReference) -> None
unreal.QuartzQuantizationBoundary.fire_on_clock_start(value: bool) -> None
unreal.QuartzQuantizationBoundary.multiplier(value: float) -> None
unreal.QuartzQuantizationBoundary.quantization(value: QuartzCommandQuantization) -> None
unreal.QuartzQuantizationBoundary.reset_clock_on_queued(value: bool) -> None
unreal.QuartzQuantizationBoundary.resume_clock_on_queued(value: bool) -> None
```

## `unreal.QuartzTimeSignature(StructBase)`

```python
unreal.QuartzTimeSignature.__init__(num_beats: int = 0, beat_type: QuartzTimeSignatureQuantization = QuartzTimeSignatureQuantization.HALF_NOTE, optional_pulse_override: Array[QuartzPulseOverrideStep] = []) -> None
unreal.QuartzTimeSignature.beat_type(value: QuartzTimeSignatureQuantization) -> None
unreal.QuartzTimeSignature.num_beats(value: int) -> None
unreal.QuartzTimeSignature.optional_pulse_override(value: Array[QuartzPulseOverrideStep]) -> None
```

## `unreal.QuartzTransportTimeStamp(StructBase)`

```python
unreal.QuartzTransportTimeStamp.__init__(bars: int = 0, beat: int = 0, beat_fraction: float = 0.000000, seconds: float = 0.000000) -> None
unreal.QuartzTransportTimeStamp.bars() -> int
unreal.QuartzTransportTimeStamp.beat() -> int
unreal.QuartzTransportTimeStamp.beat_fraction() -> float
unreal.QuartzTransportTimeStamp.seconds() -> float
```

## `unreal.ResonanceAudioReverbPluginPreset(SoundEffectSubmixPreset)`

```python
unreal.ResonanceAudioReverbPluginPreset.set_enable_room_effects(enable_room_effects: bool) -> None
unreal.ResonanceAudioReverbPluginPreset.set_reflection_scalar(reflection_scalar: float) -> None
unreal.ResonanceAudioReverbPluginPreset.set_reverb_brightness(reverb_brightness: float) -> None
unreal.ResonanceAudioReverbPluginPreset.set_reverb_gain(reverb_gain: float) -> None
unreal.ResonanceAudioReverbPluginPreset.set_reverb_time_modifier(reverb_time_modifier: float) -> None
unreal.ResonanceAudioReverbPluginPreset.set_room_dimensions(dimensions: Vector) -> None
unreal.ResonanceAudioReverbPluginPreset.set_room_materials(materials: Array[RaMaterialName]) -> None
unreal.ResonanceAudioReverbPluginPreset.set_room_position(position: Vector) -> None
unreal.ResonanceAudioReverbPluginPreset.set_room_rotation(rotation: Quat) -> None
```

## `unreal.ResonanceAudioReverbPluginSettings(StructBase)`

```python
unreal.ResonanceAudioReverbPluginSettings.__init__(enable_room_effects: bool = False, room_position: Vector = [0.000000, 0.000000, 0.000000], room_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], room_dimensions: Vector = [0.000000, 0.000000, 0.000000], left_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT, right_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT, floor_material: RaMaterialName = RaMaterialName.TRANSPARENT, ceiling_material: RaMaterialName = RaMaterialName.TRANSPARENT, front_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT, back_wall_material: RaMaterialName = RaMaterialName.TRANSPARENT, reflection_scalar: float = 0.000000, reverb_gain: float = 0.000000, reverb_time_modifier: float = 0.000000, reverb_brightness: float = 0.000000) -> None
unreal.ResonanceAudioReverbPluginSettings.back_wall_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.ceiling_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.enable_room_effects(value: bool) -> None
unreal.ResonanceAudioReverbPluginSettings.floor_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.front_wall_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.left_wall_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.reflection_scalar(value: float) -> None
unreal.ResonanceAudioReverbPluginSettings.reverb_brightness(value: float) -> None
unreal.ResonanceAudioReverbPluginSettings.reverb_gain(value: float) -> None
unreal.ResonanceAudioReverbPluginSettings.reverb_time_modifier(value: float) -> None
unreal.ResonanceAudioReverbPluginSettings.right_wall_material(value: RaMaterialName) -> None
unreal.ResonanceAudioReverbPluginSettings.room_dimensions(value: Vector) -> None
unreal.ResonanceAudioReverbPluginSettings.room_position(value: Vector) -> None
unreal.ResonanceAudioReverbPluginSettings.room_rotation(value: Quat) -> None
```

## `unreal.ResonanceAudioSoundfieldSettings(SoundfieldEncodingSettingsBase)`

```python
unreal.ResonanceAudioSoundfieldSettings.render_mode() -> ResonanceRenderMode
```

## `unreal.ResonanceAudioSpatializationSourceSettings(SpatializationPluginSourceSettingsBase)`

```python
unreal.ResonanceAudioSpatializationSourceSettings.set_sound_source_directivity(pattern: float, sharpness: float) -> None
unreal.ResonanceAudioSpatializationSourceSettings.set_sound_source_spread(spread: float) -> None
```

## `unreal.SoundAttenuation(Object)`

```python
unreal.SoundAttenuation.attenuation(value: SoundAttenuationSettings) -> None
```

## `unreal.SoundAttenuationPluginSettings(StructBase)`

```python
unreal.SoundAttenuationPluginSettings.__init__(spatialization_plugin_settings_array: Array[SpatializationPluginSourceSettingsBase] = [], occlusion_plugin_settings_array: Array[OcclusionPluginSourceSettingsBase] = [], reverb_plugin_settings_array: Array[ReverbPluginSourceSettingsBase] = [], source_data_override_plugin_settings_array: Array[SourceDataOverridePluginSourceSettingsBase] = []) -> None
unreal.SoundAttenuationPluginSettings.occlusion_plugin_settings_array(value: Array[OcclusionPluginSourceSettingsBase]) -> None
unreal.SoundAttenuationPluginSettings.reverb_plugin_settings_array(value: Array[ReverbPluginSourceSettingsBase]) -> None
unreal.SoundAttenuationPluginSettings.source_data_override_plugin_settings_array(value: Array[SourceDataOverridePluginSourceSettingsBase]) -> None
unreal.SoundAttenuationPluginSettings.spatialization_plugin_settings_array(value: Array[SpatializationPluginSourceSettingsBase]) -> None
```

## `unreal.SoundAttenuationSettings(BaseAttenuationSettings)`

```python
unreal.SoundAttenuationSettings.__init__(distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.LINEAR, attenuation_shape: AttenuationShape = AttenuationShape.SPHERE, falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES, d_b_attenuation_at_max: float = 0.000000, attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000], cone_offset: float = 0.000000, falloff_distance: float = 0.000000, cone_sphere_radius: float = 0.000000, cone_sphere_falloff_distance: float = 0.000000, custom_attenuation_curve: RuntimeFloatCurve = [], attenuate: bool = False, spatialize: bool = False, attenuate_with_lpf: bool = False, enable_listener_focus: bool = False, enable_focus_interpolation: bool = False, enable_occlusion: bool = False, use_complex_collision_for_occlusion: bool = False, enable_reverb_send: bool = False, enable_priority_attenuation: bool = False, apply_normalization_to_stereo_sounds: bool = False, enable_log_frequency_scaling: bool = False, enable_submix_sends: bool = False, enable_source_data_override: bool = False, enable_send_to_audio_link: bool = False, spatialization_algorithm: SoundSpatializationAlgorithm = SoundSpatializationAlgorithm.SPATIALIZATION_DEFAULT, audio_link_settings_override: AudioLinkSettingsAbstract = None, binaural_radius: float = 0.000000, custom_lowpass_air_absorption_curve: RuntimeFloatCurve = [], custom_highpass_air_absorption_curve: RuntimeFloatCurve = [], absorption_method: AirAbsorptionMethod = AirAbsorptionMethod.LINEAR, occlusion_trace_channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC, reverb_send_method: ReverbSendMethod = ReverbSendMethod.LINEAR, priority_attenuation_method: PriorityAttenuationMethod = PriorityAttenuationMethod.LINEAR, non_spatialized_radius_start: float = 0.000000, non_spatialized_radius_end: float = 0.000000, non_spatialized_radius_mode: NonSpatializedRadiusSpeakerMapMode = NonSpatializedRadiusSpeakerMapMode.OMNI_DIRECTIONAL, stereo_spread: float = 0.000000, lpf_radius_min: float = 0.000000, lpf_radius_max: float = 0.000000, lpf_frequency_at_min: float = 0.000000, lpf_frequency_at_max: float = 0.000000, hpf_frequency_at_min: float = 0.000000, hpf_frequency_at_max: float = 0.000000, focus_azimuth: float = 0.000000, non_focus_azimuth: float = 0.000000, focus_distance_scale: float = 0.000000, non_focus_distance_scale: float = 0.000000, focus_priority_scale: float = 0.000000, non_focus_priority_scale: float = 0.000000, focus_volume_attenuation: float = 0.000000, non_focus_volume_attenuation: float = 0.000000, focus_attack_interp_speed: float = 0.000000, focus_release_interp_speed: float = 0.000000, occlusion_low_pass_filter_frequency: float = 0.000000, occlusion_volume_attenuation: float = 0.000000, occlusion_interpolation_time: float = 0.000000, reverb_wet_level_min: float = 0.000000, reverb_wet_level_max: float = 0.000000, reverb_distance_min: float = 0.000000, reverb_distance_max: float = 0.000000, manual_reverb_send_level: float = 0.000000, priority_attenuation_min: float = 0.000000, priority_attenuation_max: float = 0.000000, priority_attenuation_distance_min: float = 0.000000, priority_attenuation_distance_max: float = 0.000000, manual_priority_attenuation: float = 0.000000, custom_reverb_send_curve: RuntimeFloatCurve = [], submix_send_settings: Array[AttenuationSubmixSendSettings] = [], custom_priority_attenuation_curve: RuntimeFloatCurve = [], plugin_settings: SoundAttenuationPluginSettings = [[], [], [], []]) -> None
unreal.SoundAttenuationSettings.absorption_method(value: AirAbsorptionMethod) -> None
unreal.SoundAttenuationSettings.apply_normalization_to_stereo_sounds(value: bool) -> None
unreal.SoundAttenuationSettings.attenuate(value: bool) -> None
unreal.SoundAttenuationSettings.attenuate_with_lpf(value: bool) -> None
unreal.SoundAttenuationSettings.audio_link_settings_override(value: AudioLinkSettingsAbstract) -> None
unreal.SoundAttenuationSettings.binaural_radius(value: float) -> None
unreal.SoundAttenuationSettings.custom_highpass_air_absorption_curve(value: RuntimeFloatCurve) -> None
unreal.SoundAttenuationSettings.custom_lowpass_air_absorption_curve(value: RuntimeFloatCurve) -> None
unreal.SoundAttenuationSettings.custom_priority_attenuation_curve(value: RuntimeFloatCurve) -> None
unreal.SoundAttenuationSettings.custom_reverb_send_curve(value: RuntimeFloatCurve) -> None
unreal.SoundAttenuationSettings.enable_focus_interpolation(value: bool) -> None
unreal.SoundAttenuationSettings.enable_listener_focus(value: bool) -> None
unreal.SoundAttenuationSettings.enable_log_frequency_scaling(value: bool) -> None
unreal.SoundAttenuationSettings.enable_occlusion(value: bool) -> None
unreal.SoundAttenuationSettings.enable_priority_attenuation(value: bool) -> None
unreal.SoundAttenuationSettings.enable_reverb_send(value: bool) -> None
unreal.SoundAttenuationSettings.enable_send_to_audio_link(value: bool) -> None
unreal.SoundAttenuationSettings.enable_source_data_override(value: bool) -> None
unreal.SoundAttenuationSettings.enable_submix_sends(value: bool) -> None
unreal.SoundAttenuationSettings.focus_attack_interp_speed(value: float) -> None
unreal.SoundAttenuationSettings.focus_azimuth(value: float) -> None
unreal.SoundAttenuationSettings.focus_distance_scale(value: float) -> None
unreal.SoundAttenuationSettings.focus_priority_scale(value: float) -> None
unreal.SoundAttenuationSettings.focus_release_interp_speed(value: float) -> None
unreal.SoundAttenuationSettings.focus_volume_attenuation(value: float) -> None
unreal.SoundAttenuationSettings.hpf_frequency_at_max(value: float) -> None
unreal.SoundAttenuationSettings.hpf_frequency_at_min(value: float) -> None
unreal.SoundAttenuationSettings.lpf_frequency_at_max(value: float) -> None
unreal.SoundAttenuationSettings.lpf_frequency_at_min(value: float) -> None
unreal.SoundAttenuationSettings.lpf_radius_max(value: float) -> None
unreal.SoundAttenuationSettings.lpf_radius_min(value: float) -> None
unreal.SoundAttenuationSettings.manual_priority_attenuation(value: float) -> None
unreal.SoundAttenuationSettings.manual_reverb_send_level(value: float) -> None
unreal.SoundAttenuationSettings.non_focus_azimuth(value: float) -> None
unreal.SoundAttenuationSettings.non_focus_distance_scale(value: float) -> None
unreal.SoundAttenuationSettings.non_focus_priority_scale(value: float) -> None
unreal.SoundAttenuationSettings.non_focus_volume_attenuation(value: float) -> None
unreal.SoundAttenuationSettings.non_spatialized_radius_end(value: float) -> None
unreal.SoundAttenuationSettings.non_spatialized_radius_mode(value: NonSpatializedRadiusSpeakerMapMode) -> None
unreal.SoundAttenuationSettings.non_spatialized_radius_start(value: float) -> None
unreal.SoundAttenuationSettings.occlusion_interpolation_time(value: float) -> None
unreal.SoundAttenuationSettings.occlusion_low_pass_filter_frequency(value: float) -> None
unreal.SoundAttenuationSettings.occlusion_trace_channel(value: CollisionChannel) -> None
unreal.SoundAttenuationSettings.occlusion_volume_attenuation(value: float) -> None
unreal.SoundAttenuationSettings.omni_radius(value: float) -> None
unreal.SoundAttenuationSettings.plugin_settings(value: SoundAttenuationPluginSettings) -> None
unreal.SoundAttenuationSettings.priority_attenuation_distance_max(value: float) -> None
unreal.SoundAttenuationSettings.priority_attenuation_distance_min(value: float) -> None
unreal.SoundAttenuationSettings.priority_attenuation_max(value: float) -> None
unreal.SoundAttenuationSettings.priority_attenuation_method(value: PriorityAttenuationMethod) -> None
unreal.SoundAttenuationSettings.priority_attenuation_min(value: float) -> None
unreal.SoundAttenuationSettings.reverb_distance_max(value: float) -> None
unreal.SoundAttenuationSettings.reverb_distance_min(value: float) -> None
unreal.SoundAttenuationSettings.reverb_send_method(value: ReverbSendMethod) -> None
unreal.SoundAttenuationSettings.reverb_wet_level_max(value: float) -> None
unreal.SoundAttenuationSettings.reverb_wet_level_min(value: float) -> None
unreal.SoundAttenuationSettings.spatialization_algorithm(value: SoundSpatializationAlgorithm) -> None
unreal.SoundAttenuationSettings.spatialize(value: bool) -> None
unreal.SoundAttenuationSettings.stereo_spread(value: float) -> None
unreal.SoundAttenuationSettings.submix_send_settings(value: Array[AttenuationSubmixSendSettings]) -> None
unreal.SoundAttenuationSettings.use_complex_collision_for_occlusion(value: bool) -> None
```

## `unreal.SoundBase(Object)`

```python
unreal.SoundBase.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.SoundBase.bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
unreal.SoundBase.bypass_volume_scale_for_priority(value: bool) -> None
unreal.SoundBase.concurrency_overrides(value: SoundConcurrencySettings) -> None
unreal.SoundBase.concurrency_set(value: Set[SoundConcurrency]) -> None
unreal.SoundBase.duration() -> float
unreal.SoundBase.enable_bus_sends(value: bool) -> None
unreal.SoundBase.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.SoundBase.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.SoundBase.max_distance() -> float
unreal.SoundBase.override_concurrency(value: bool) -> None
unreal.SoundBase.pre_effect_bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
unreal.SoundBase.priority(value: float) -> None
unreal.SoundBase.sound_class_object() -> SoundClass
unreal.SoundBase.sound_submix_object(value: SoundSubmixBase) -> None
unreal.SoundBase.sound_submix_sends(value: Array[SoundSubmixSendInfo]) -> None
unreal.SoundBase.source_effect_chain(value: SoundEffectSourcePresetChain) -> None
unreal.SoundBase.total_samples() -> float
unreal.SoundBase.virtualization_mode(value: VirtualizationMode) -> None
```

## `unreal.SoundClass(Object)`

```python
unreal.SoundClass.child_classes() -> Array[SoundClass]
unreal.SoundClass.parent_class() -> SoundClass
unreal.SoundClass.passive_sound_mix_modifiers() -> Array[PassiveSoundMixModifier]
unreal.SoundClass.properties() -> SoundClassProperties
```

## `unreal.SoundClassAdjuster(StructBase)`

```python
unreal.SoundClassAdjuster.__init__(sound_class_object: SoundClass = None, volume_adjuster: float = 0.000000, pitch_adjuster: float = 0.000000, low_pass_filter_frequency: float = 0.000000, apply_to_children: bool = False, voice_center_channel_volume_adjuster: float = 0.000000) -> None
unreal.SoundClassAdjuster.apply_to_children() -> bool
unreal.SoundClassAdjuster.low_pass_filter_frequency() -> float
unreal.SoundClassAdjuster.pitch_adjuster() -> float
unreal.SoundClassAdjuster.sound_class_object() -> SoundClass
unreal.SoundClassAdjuster.voice_center_channel_volume_adjuster() -> float
unreal.SoundClassAdjuster.volume_adjuster() -> float
```

## `unreal.SoundClassProperties(StructBase)`

```python
unreal.SoundClassProperties.__init__(volume: float = 0.000000, pitch: float = 0.000000, low_pass_filter_frequency: float = 0.000000, attenuation_distance_scale: float = 0.000000, lfe_bleed: float = 0.000000, voice_center_channel_volume: float = 0.000000, radio_filter_volume: float = 0.000000, radio_filter_volume_threshold: float = 0.000000, apply_effects: bool = False, always_play: bool = False, is_ui_sound: bool = False, is_music: bool = False, center_channel_only: bool = False, apply_ambient_volumes: bool = False, reverb: bool = False, default2d_reverb_send_amount: float = 0.000000, modulation_settings: SoundModulationDefaultSettings = [[0.000000, []], [0.000000, []], [20.000000, []], [20000.000000, []]], output_target: AudioOutputTarget = AudioOutputTarget.SPEAKER, loading_behavior: SoundWaveLoadingBehavior = SoundWaveLoadingBehavior.INHERITED, default_submix: SoundSubmix = None) -> None
unreal.SoundClassProperties.always_play() -> bool
unreal.SoundClassProperties.apply_ambient_volumes() -> bool
unreal.SoundClassProperties.apply_effects() -> bool
unreal.SoundClassProperties.attenuation_distance_scale() -> float
unreal.SoundClassProperties.center_channel_only() -> bool
unreal.SoundClassProperties.default2d_reverb_send_amount() -> float
unreal.SoundClassProperties.default_submix() -> SoundSubmix
unreal.SoundClassProperties.is_music() -> bool
unreal.SoundClassProperties.is_ui_sound() -> bool
unreal.SoundClassProperties.lfe_bleed() -> float
unreal.SoundClassProperties.loading_behavior() -> SoundWaveLoadingBehavior
unreal.SoundClassProperties.low_pass_filter_frequency() -> float
unreal.SoundClassProperties.modulation_settings() -> SoundModulationDefaultSettings
unreal.SoundClassProperties.output_target() -> AudioOutputTarget
unreal.SoundClassProperties.pitch() -> float
unreal.SoundClassProperties.radio_filter_volume() -> float
unreal.SoundClassProperties.radio_filter_volume_threshold() -> float
unreal.SoundClassProperties.reverb() -> bool
unreal.SoundClassProperties.voice_center_channel_volume() -> float
unreal.SoundClassProperties.volume() -> float
```

## `unreal.SoundConcurrency(Object)`

```python
unreal.SoundConcurrency.concurrency() -> SoundConcurrencySettings
```

## `unreal.SoundConcurrencySettings(StructBase)`

```python
unreal.SoundConcurrencySettings.__init__(max_count: int = 0, limit_to_owner: bool = False, volume_scale_can_release: bool = False, resolution_rule: MaxConcurrentResolutionRule = MaxConcurrentResolutionRule.PREVENT_NEW, retrigger_time: float = 0.000000, volume_scale_mode: ConcurrencyVolumeScaleMode = ConcurrencyVolumeScaleMode.DEFAULT, volume_scale_attack_time: float = 0.000000, volume_scale_release_time: float = 0.000000, voice_steal_release_time: float = 0.000000) -> None
unreal.SoundConcurrencySettings.limit_to_owner(value: bool) -> None
unreal.SoundConcurrencySettings.max_count(value: int) -> None
unreal.SoundConcurrencySettings.resolution_rule(value: MaxConcurrentResolutionRule) -> None
unreal.SoundConcurrencySettings.retrigger_time(value: float) -> None
unreal.SoundConcurrencySettings.voice_steal_release_time(value: float) -> None
unreal.SoundConcurrencySettings.volume_scale_attack_time(value: float) -> None
unreal.SoundConcurrencySettings.volume_scale_can_release(value: bool) -> None
unreal.SoundConcurrencySettings.volume_scale_mode(value: ConcurrencyVolumeScaleMode) -> None
unreal.SoundConcurrencySettings.volume_scale_release_time(value: float) -> None
```

## `unreal.SoundCue(SoundBase)`

```python
unreal.SoundCue.first_node() -> SoundNode
unreal.SoundCue.pitch_multiplier() -> float
unreal.SoundCue.volume_multiplier() -> float
```

## `unreal.SoundGeneratorOutput(StructBase)`

```python
unreal.SoundGeneratorOutput.__init__(name: Name = "None") -> None
unreal.SoundGeneratorOutput.name() -> Name
```

## `unreal.SoundMix(Object)`

```python
unreal.SoundMix.sound_class_effects() -> Array[SoundClassAdjuster]
```

## `unreal.SoundModulationDefaultRoutingSettings(SoundModulationDefaultSettings)`

```python
unreal.SoundModulationDefaultRoutingSettings.__init__(volume_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], pitch_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], highpass_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], lowpass_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], volume_routing: ModulationRouting = ModulationRouting.DISABLE, pitch_routing: ModulationRouting = ModulationRouting.DISABLE, highpass_routing: ModulationRouting = ModulationRouting.DISABLE, lowpass_routing: ModulationRouting = ModulationRouting.DISABLE) -> None
unreal.SoundModulationDefaultRoutingSettings.highpass_routing(value: ModulationRouting) -> None
unreal.SoundModulationDefaultRoutingSettings.lowpass_routing(value: ModulationRouting) -> None
unreal.SoundModulationDefaultRoutingSettings.pitch_routing(value: ModulationRouting) -> None
unreal.SoundModulationDefaultRoutingSettings.volume_routing(value: ModulationRouting) -> None
```

## `unreal.SoundModulationDefaultSettings(StructBase)`

```python
unreal.SoundModulationDefaultSettings.__init__(volume_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], pitch_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], highpass_modulation_destination: SoundModulationDestinationSettings = [1.000000, []], lowpass_modulation_destination: SoundModulationDestinationSettings = [1.000000, []]) -> None
unreal.SoundModulationDefaultSettings.highpass_modulation_destination(value: SoundModulationDestinationSettings) -> None
unreal.SoundModulationDefaultSettings.lowpass_modulation_destination(value: SoundModulationDestinationSettings) -> None
unreal.SoundModulationDefaultSettings.pitch_modulation_destination(value: SoundModulationDestinationSettings) -> None
unreal.SoundModulationDefaultSettings.volume_modulation_destination(value: SoundModulationDestinationSettings) -> None
```

## `unreal.SoundModulationDestinationSettings(StructBase)`

```python
unreal.SoundModulationDestinationSettings.__init__(value: float = 0.000000, modulators: Set[SoundModulatorBase] = []) -> None
unreal.SoundModulationDestinationSettings.modulator(value: SoundModulatorBase) -> None
unreal.SoundModulationDestinationSettings.modulators(value: Set[SoundModulatorBase]) -> None
unreal.SoundModulationDestinationSettings.value(value: float) -> None
```

## `unreal.SoundSourceBus(SoundWave)`

```python
unreal.SoundSourceBus.auto_deactivate_when_silent(value: bool) -> None
```

## `unreal.SoundSourceBusSendInfo(StructBase)`

```python
unreal.SoundSourceBusSendInfo.__init__(min_send_level: float = 0.000000, max_send_level: float = 0.000000, min_send_distance: float = 0.000000, max_send_distance: float = 0.000000, custom_send_level_curve: RuntimeFloatCurve = []) -> None
unreal.SoundSourceBusSendInfo.custom_send_level_curve(value: RuntimeFloatCurve) -> None
unreal.SoundSourceBusSendInfo.max_send_distance(value: float) -> None
unreal.SoundSourceBusSendInfo.max_send_level(value: float) -> None
unreal.SoundSourceBusSendInfo.min_send_distance(value: float) -> None
unreal.SoundSourceBusSendInfo.min_send_level(value: float) -> None
```

## `unreal.SoundSubmix(SoundSubmixWithParentBase)`

```python
unreal.SoundSubmix.add_envelope_follower_delegate(world_context_object: Object, on_submix_envelope_bp: OnSubmixEnvelopeBP) -> None
unreal.SoundSubmix.add_spectral_analysis_delegate(world_context_object: Object, band_settings: Array[SoundSubmixSpectralAnalysisBandSettings], on_submix_spectral_analysis_bp: OnSubmixSpectralAnalysisBP, update_rate: float = 10.000000, decibel_noise_floor: float = -40.000000, do_normalize: bool = True, do_auto_range: bool = False, auto_range_attack_time: float = 0.100000, auto_range_release_time: float = 60.000000) -> None
unreal.SoundSubmix.ambisonics_plugin_settings(value: SoundfieldEncodingSettingsBase) -> None
unreal.SoundSubmix.audio_link_settings(value: AudioLinkSettingsAbstract) -> None
unreal.SoundSubmix.dry_level_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SoundSubmix.envelope_follower_attack_time(value: int) -> None
unreal.SoundSubmix.envelope_follower_release_time(value: int) -> None
unreal.SoundSubmix.mute_when_backgrounded() -> bool
unreal.SoundSubmix.on_submix_recorded_file_done(value: OnSubmixRecordedFileDone) -> None
unreal.SoundSubmix.output_volume_modulation(value: SoundModulationDestinationSettings) -> None
unreal.SoundSubmix.remove_envelope_follower_delegate(world_context_object: Object, on_submix_envelope_bp: OnSubmixEnvelopeBP) -> None
unreal.SoundSubmix.remove_spectral_analysis_delegate(world_context_object: Object, on_submix_spectral_analysis_bp: OnSubmixSpectralAnalysisBP) -> None
unreal.SoundSubmix.send_to_audio_link(value: bool) -> None
unreal.SoundSubmix.set_submix_dry_level(world_context_object: Object, dry_level: float) -> None
unreal.SoundSubmix.set_submix_output_volume(world_context_object: Object, output_volume: float) -> None
unreal.SoundSubmix.set_submix_wet_level(world_context_object: Object, wet_level: float) -> None
unreal.SoundSubmix.start_envelope_following(world_context_object: Object) -> None
unreal.SoundSubmix.start_recording_output(world_context_object: Object, expected_duration: float) -> None
unreal.SoundSubmix.start_spectral_analysis(world_context_object: Object, fft_size: FFTSize = FFTSize.DEFAULT_SIZE, interpolation_method: FFTPeakInterpolationMethod = FFTPeakInterpolationMethod.LINEAR, window_type: FFTWindowType = FFTWindowType.HANN, hop_size: float = 0.000000, spectrum_type: AudioSpectrumType = AudioSpectrumType.MAGNITUDE_SPECTRUM) -> None
unreal.SoundSubmix.stop_envelope_following(world_context_object: Object) -> None
unreal.SoundSubmix.stop_recording_output(world_context_object: Object, export_type: AudioRecordingExportType, name: str, path: str, existing_sound_wave_to_overwrite: SoundWave = None) -> None
unreal.SoundSubmix.stop_spectral_analysis(world_context_object: Object) -> None
unreal.SoundSubmix.submix_effect_chain() -> Array[SoundEffectSubmixPreset]
unreal.SoundSubmix.wet_level_modulation(value: SoundModulationDestinationSettings) -> None
```

## `unreal.SoundSubmixBase(Object)`

```python
unreal.SoundSubmixBase.auto_disable() -> bool
unreal.SoundSubmixBase.auto_disable_time(value: float) -> None
unreal.SoundSubmixBase.child_submixes() -> Array[SoundSubmixBase]
unreal.SoundSubmixBase.dynamic_connect(world_context_object: Object, parent: SoundSubmixBase) -> bool
unreal.SoundSubmixBase.dynamic_disconnect(world_context_object: Object) -> bool
unreal.SoundSubmixBase.find_dynamic_ancestor() -> SoundSubmixBase
```

## `unreal.SoundSubmixSendInfo(SoundSubmixSendInfoBase)`

```python
unreal.SoundSubmixSendInfo.__init__(send_level_control_method: SendLevelControlMethod = SendLevelControlMethod.LINEAR, sound_submix: SoundSubmixBase = None, send_level: float = 0.000000, disable_manual_send_clamp: bool = False, min_send_level: float = 0.000000, max_send_level: float = 0.000000, min_send_distance: float = 0.000000, max_send_distance: float = 0.000000, custom_send_level_curve: RuntimeFloatCurve = [], send_stage: SubmixSendStage = SubmixSendStage.POST_DISTANCE_ATTENUATION) -> None
unreal.SoundSubmixSendInfo.send_stage(value: SubmixSendStage) -> None
```

## `unreal.SoundSubmixSendInfoBase(StructBase)`

```python
unreal.SoundSubmixSendInfoBase.__init__(send_level_control_method: SendLevelControlMethod = SendLevelControlMethod.LINEAR, sound_submix: SoundSubmixBase = None, send_level: float = 0.000000, disable_manual_send_clamp: bool = False, min_send_level: float = 0.000000, max_send_level: float = 0.000000, min_send_distance: float = 0.000000, max_send_distance: float = 0.000000, custom_send_level_curve: RuntimeFloatCurve = []) -> None
unreal.SoundSubmixSendInfoBase.custom_send_level_curve(value: RuntimeFloatCurve) -> None
unreal.SoundSubmixSendInfoBase.disable_manual_send_clamp(value: bool) -> None
unreal.SoundSubmixSendInfoBase.max_send_distance(value: float) -> None
unreal.SoundSubmixSendInfoBase.max_send_level(value: float) -> None
unreal.SoundSubmixSendInfoBase.min_send_distance(value: float) -> None
unreal.SoundSubmixSendInfoBase.min_send_level(value: float) -> None
unreal.SoundSubmixSendInfoBase.send_level(value: float) -> None
unreal.SoundSubmixSendInfoBase.send_level_control_method(value: SendLevelControlMethod) -> None
unreal.SoundSubmixSendInfoBase.sound_submix(value: SoundSubmixBase) -> None
```

## `unreal.SoundSubmixSpectralAnalysisBandSettings(StructBase)`

```python
unreal.SoundSubmixSpectralAnalysisBandSettings.__init__(band_frequency: float = 0.000000, attack_time_msec: int = 0, release_time_msec: int = 0, q_factor: float = 0.000000) -> None
unreal.SoundSubmixSpectralAnalysisBandSettings.attack_time_msec(value: int) -> None
unreal.SoundSubmixSpectralAnalysisBandSettings.band_frequency(value: float) -> None
unreal.SoundSubmixSpectralAnalysisBandSettings.q_factor(value: float) -> None
unreal.SoundSubmixSpectralAnalysisBandSettings.release_time_msec(value: int) -> None
```

## `unreal.SoundSubmixWithParentBase(SoundSubmixBase)`

```python
unreal.SoundSubmixWithParentBase.is_dynamic() -> bool
unreal.SoundSubmixWithParentBase.parent_submix() -> SoundSubmixBase
```

## `unreal.SoundWave(SoundBase)`

```python
unreal.SoundWave.cue_points() -> Array[SoundWaveCuePoint]
unreal.SoundWave.get_cue_points() -> Array[SoundWaveCuePoint]
unreal.SoundWave.get_loop_regions() -> Array[SoundWaveCuePoint]
unreal.SoundWave.get_sound_asset_compression_type() -> SoundAssetCompressionType
unreal.SoundWave.initial_chunk_size(value: int) -> None
unreal.SoundWave.manual_word_wrap() -> bool
unreal.SoundWave.mature() -> bool
unreal.SoundWave.modulation_settings(value: SoundModulationDefaultRoutingSettings) -> None
unreal.SoundWave.seekable_streaming(value: bool) -> None
unreal.SoundWave.set_sound_asset_compression_type(sound_asset_compression_type: SoundAssetCompressionType, mark_dirty: bool = True) -> None
unreal.SoundWave.single_line() -> bool
unreal.SoundWave.spoken_text(value: str) -> None
unreal.SoundWave.streaming_priority(value: int) -> None
unreal.SoundWave.subtitle_priority() -> float
unreal.SoundWave.subtitles() -> Array[SubtitleCue]
unreal.SoundWave.use_bink_audio(value: bool) -> None
```

## `unreal.SoundWaveCloudStreamingPlatformSettings(StructBase)`

```python
unreal.SoundWaveCloudStreamingPlatformSettings.__init__() -> None
```

## `unreal.SoundWaveCuePoint(StructBase)`

```python
unreal.SoundWaveCuePoint.__init__(cue_point_id: int = 0, label: str = "", frame_position: int = 0, frame_length: int = 0) -> None
unreal.SoundWaveCuePoint.cue_point_id() -> int
unreal.SoundWaveCuePoint.frame_length() -> int
unreal.SoundWaveCuePoint.frame_position() -> int
unreal.SoundWaveCuePoint.label() -> str
```

## `unreal.SoundWaveEnvelopeDataPerSound(StructBase)`

```python
unreal.SoundWaveEnvelopeDataPerSound.__init__(envelope: float = 0.000000, playback_time: float = 0.000000, sound_wave: SoundWave = None) -> None
unreal.SoundWaveEnvelopeDataPerSound.envelope(value: float) -> None
unreal.SoundWaveEnvelopeDataPerSound.playback_time(value: float) -> None
unreal.SoundWaveEnvelopeDataPerSound.sound_wave(value: SoundWave) -> None
```

## `unreal.SoundWaveSpectralData(StructBase)`

```python
unreal.SoundWaveSpectralData.__init__(frequency_hz: float = 0.000000, magnitude: float = 0.000000, normalized_magnitude: float = 0.000000) -> None
unreal.SoundWaveSpectralData.frequency_hz(value: float) -> None
unreal.SoundWaveSpectralData.magnitude(value: float) -> None
unreal.SoundWaveSpectralData.normalized_magnitude(value: float) -> None
```

## `unreal.SoundWaveSpectralDataPerSound(StructBase)`

```python
unreal.SoundWaveSpectralDataPerSound.__init__(spectral_data: Array[SoundWaveSpectralData] = [], playback_time: float = 0.000000, sound_wave: SoundWave = None) -> None
unreal.SoundWaveSpectralDataPerSound.playback_time(value: float) -> None
unreal.SoundWaveSpectralDataPerSound.sound_wave(value: SoundWave) -> None
unreal.SoundWaveSpectralDataPerSound.spectral_data(value: Array[SoundWaveSpectralData]) -> None
```

## `unreal.SoundWaveTimecodeInfo(StructBase)`

```python
unreal.SoundWaveTimecodeInfo.__init__() -> None
```

## `unreal.SourceEffectFilterAudioBusModulationSettings(StructBase)`

```python
unreal.SourceEffectFilterAudioBusModulationSettings.__init__(audio_bus: AudioBus = None, envelope_follower_attack_time_msec: int = 0, envelope_follower_release_time_msec: int = 0, envelope_gain_multiplier: float = 0.000000, min_frequency_modulation: float = 0.000000, max_frequency_modulation: float = 0.000000, min_resonance_modulation: float = 0.000000, max_resonance_modulation: float = 0.000000) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.audio_bus(value: AudioBus) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_attack_time_msec(value: int) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.envelope_follower_release_time_msec(value: int) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.envelope_gain_multiplier(value: float) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.max_frequency_modulation(value: float) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.max_resonance_modulation(value: float) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.min_frequency_modulation(value: float) -> None
unreal.SourceEffectFilterAudioBusModulationSettings.min_resonance_modulation(value: float) -> None
```

## `unreal.SwapAudioOutputResult(StructBase)`

```python
unreal.SwapAudioOutputResult.__init__(current_device_id: str = "", requested_device_id: str = "", result: SwapAudioOutputDeviceResultState = SwapAudioOutputDeviceResultState.FAILURE) -> None
unreal.SwapAudioOutputResult.current_device_id() -> str
unreal.SwapAudioOutputResult.requested_device_id() -> str
unreal.SwapAudioOutputResult.result() -> SwapAudioOutputDeviceResultState
```

## `unreal.Synth1PatchCable(StructBase)`

```python
unreal.Synth1PatchCable.__init__(depth: float = 0.000000, destination: Synth1PatchDestination = Synth1PatchDestination.OSC1_GAIN) -> None
unreal.Synth1PatchCable.depth(value: float) -> None
unreal.Synth1PatchCable.destination(value: Synth1PatchDestination) -> None
```

## `unreal.Synth2DSlider(Widget)`

```python
unreal.Synth2DSlider.get_value() -> Vector2D
unreal.Synth2DSlider.indent_handle() -> bool
unreal.Synth2DSlider.is_focusable() -> bool
unreal.Synth2DSlider.locked() -> bool
unreal.Synth2DSlider.on_controller_capture_begin(value: OnControllerCaptureBeginEventSynth2D) -> None
unreal.Synth2DSlider.on_controller_capture_end(value: OnControllerCaptureEndEventSynth2D) -> None
unreal.Synth2DSlider.on_mouse_capture_begin(value: OnMouseCaptureBeginEventSynth2D) -> None
unreal.Synth2DSlider.on_mouse_capture_end(value: OnMouseCaptureEndEventSynth2D) -> None
unreal.Synth2DSlider.on_value_changed_x(value: OnFloatValueChangedEventSynth2D) -> None
unreal.Synth2DSlider.on_value_changed_y(value: OnFloatValueChangedEventSynth2D) -> None
unreal.Synth2DSlider.set_indent_handle(value: bool) -> None
unreal.Synth2DSlider.set_locked(value: bool) -> None
unreal.Synth2DSlider.set_slider_handle_color(value: LinearColor) -> None
unreal.Synth2DSlider.set_step_size(value: float) -> None
unreal.Synth2DSlider.set_value(value: Vector2D) -> None
unreal.Synth2DSlider.slider_handle_color() -> LinearColor
unreal.Synth2DSlider.step_size() -> float
unreal.Synth2DSlider.widget_style(value: Synth2DSliderStyle) -> None
```

## `unreal.Synth2DSliderStyle(SlateWidgetStyle)`

```python
unreal.Synth2DSliderStyle.__init__(normal_thumb_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], disabled_thumb_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], normal_bar_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], disabled_bar_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], background_image: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], bar_thickness: float = 0.000000) -> None
unreal.Synth2DSliderStyle.background_image(value: SlateBrush) -> None
unreal.Synth2DSliderStyle.bar_thickness(value: float) -> None
unreal.Synth2DSliderStyle.disabled_bar_image(value: SlateBrush) -> None
unreal.Synth2DSliderStyle.disabled_thumb_image(value: SlateBrush) -> None
unreal.Synth2DSliderStyle.normal_bar_image(value: SlateBrush) -> None
unreal.Synth2DSliderStyle.normal_thumb_image(value: SlateBrush) -> None
```

## `unreal.SynthComponent(SceneComponent)`

```python
unreal.SynthComponent.adjust_volume(adjust_volume_duration: float, adjust_volume_level: float, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.SynthComponent.allow_spatialization(value: bool) -> None
unreal.SynthComponent.attenuation_overrides(value: SoundAttenuationSettings) -> None
unreal.SynthComponent.attenuation_settings(value: SoundAttenuation) -> None
unreal.SynthComponent.bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
unreal.SynthComponent.concurrency_set(value: Set[SoundConcurrency]) -> None
unreal.SynthComponent.enable_bus_sends(value: bool) -> None
unreal.SynthComponent.envelope_follower_attack_time(value: int) -> None
unreal.SynthComponent.envelope_follower_release_time(value: int) -> None
unreal.SynthComponent.fade_in(fade_in_duration: float, fade_volume_level: float = 1.000000, start_time: float = 0.000000, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.SynthComponent.fade_out(fade_out_duration: float, fade_volume_level: float, fade_curve: AudioFaderCurve = AudioFaderCurve.LINEAR) -> None
unreal.SynthComponent.get_modulators(destination: ModulationDestination) -> Set[SoundModulatorBase]
unreal.SynthComponent.is_playing() -> bool
unreal.SynthComponent.is_ui_sound(value: bool) -> None
unreal.SynthComponent.modulation_routing(value: SoundModulationDefaultRoutingSettings) -> None
unreal.SynthComponent.on_audio_envelope_value(value: OnSynthEnvelopeValue) -> None
unreal.SynthComponent.override_attenuation(value: bool) -> None
unreal.SynthComponent.pre_effect_bus_sends(value: Array[SoundSourceBusSendInfo]) -> None
unreal.SynthComponent.set_audio_bus_send_post_effect(audio_bus: AudioBus, audio_bus_send_level: float) -> None
unreal.SynthComponent.set_audio_bus_send_pre_effect(audio_bus: AudioBus, audio_bus_send_level: float) -> None
unreal.SynthComponent.set_low_pass_filter_enabled(low_pass_filter_enabled: bool) -> None
unreal.SynthComponent.set_low_pass_filter_frequency(low_pass_filter_frequency: float) -> None
unreal.SynthComponent.set_modulation_routing(modulators: Set[SoundModulatorBase], destination: ModulationDestination, routing_method: ModulationRouting = ModulationRouting.INHERIT) -> None
unreal.SynthComponent.set_output_to_bus_only(output_to_bus_only: bool) -> None
unreal.SynthComponent.set_source_bus_send_post_effect(sound_source_bus: SoundSourceBus, source_bus_send_level: float) -> None
unreal.SynthComponent.set_source_bus_send_pre_effect(sound_source_bus: SoundSourceBus, source_bus_send_level: float) -> None
unreal.SynthComponent.set_submix_send(submix: SoundSubmixBase, send_level: float) -> None
unreal.SynthComponent.set_volume_multiplier(volume_multiplier: float) -> None
unreal.SynthComponent.sound_submix_sends(value: Array[SoundSubmixSendInfo]) -> None
unreal.SynthComponent.start() -> None
unreal.SynthComponent.stop() -> None
```

## `unreal.SynthComponentMonoWaveTable(SynthComponent)`

```python
unreal.SynthComponentMonoWaveTable.get_curve_tangent(table_index: int) -> float
unreal.SynthComponentMonoWaveTable.get_key_frame_values_for_table(table_index: float) -> Array[float]
unreal.SynthComponentMonoWaveTable.get_max_table_index() -> int
unreal.SynthComponentMonoWaveTable.get_num_table_entries() -> int
unreal.SynthComponentMonoWaveTable.note_off(midi_note: float) -> None
unreal.SynthComponentMonoWaveTable.note_on(midi_note: float, velocity: float) -> None
unreal.SynthComponentMonoWaveTable.on_num_tables_changed(value: NumTablesChanged) -> None
unreal.SynthComponentMonoWaveTable.on_table_altered(value: OnTableAltered) -> None
unreal.SynthComponentMonoWaveTable.refresh_all_wave_tables() -> None
unreal.SynthComponentMonoWaveTable.refresh_wave_table(index: int) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_attack_time(attack_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_bias_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_bias_invert(bias_invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_decay_time(decay_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_invert(invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_release_time(release_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_amp_envelope_sustain_gain(sustain_gain: float) -> None
unreal.SynthComponentMonoWaveTable.set_curve_interpolation_type(interpolation_type: CurveInterpolationType, table_index: int) -> bool
unreal.SynthComponentMonoWaveTable.set_curve_tangent(table_index: int, new_tangent: float) -> bool
unreal.SynthComponentMonoWaveTable.set_curve_value(table_index: int, keyframe_index: int, new_value: float) -> bool
unreal.SynthComponentMonoWaveTable.set_filter_envelope_attack_time(attack_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_bias_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_bias_invert(bias_invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_invert(invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_release_time(release_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelope_sustain_gain(sustain_gain: float) -> None
unreal.SynthComponentMonoWaveTable.set_filter_envelopen_decay_time(decay_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_frequency(frequency_hz: float) -> None
unreal.SynthComponentMonoWaveTable.set_frequency_pitch_bend(frequency_offset_cents: float) -> None
unreal.SynthComponentMonoWaveTable.set_frequency_with_midi_note(midi_note: float) -> None
unreal.SynthComponentMonoWaveTable.set_low_pass_filter_resonance(new_q: float) -> None
unreal.SynthComponentMonoWaveTable.set_pos_lfo_depth(lfo_depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_pos_lfo_frequency(lfo_frequency: float) -> None
unreal.SynthComponentMonoWaveTable.set_pos_lfo_type(lfo_type: SynthLFOType) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_attack_time(attack_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_bias_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_bias_invert(bias_invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_decay_time(decay_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_depth(depth: float) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_invert(invert: bool) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_release_time(release_time_msec: float) -> None
unreal.SynthComponentMonoWaveTable.set_position_envelope_sustain_gain(sustain_gain: float) -> None
unreal.SynthComponentMonoWaveTable.set_sustain_pedal_state(sustain_pedal_state: bool) -> None
unreal.SynthComponentMonoWaveTable.set_wave_table_position(position: float) -> None
```

## `unreal.SynthComponentToneGenerator(SynthComponent)`

```python
unreal.SynthComponentToneGenerator.attenuation_db_at_max_range(value: float) -> None
unreal.SynthComponentToneGenerator.distance_attenuation_curve(value: RuntimeFloatCurve) -> None
unreal.SynthComponentToneGenerator.distance_range(value: Vector2D) -> None
unreal.SynthComponentToneGenerator.frequency() -> float
unreal.SynthComponentToneGenerator.set_frequency(frequency: float) -> None
unreal.SynthComponentToneGenerator.set_volume(volume: float) -> None
unreal.SynthComponentToneGenerator.volume() -> float
```

## `unreal.SynthKnob(Widget)`

```python
unreal.SynthKnob.get_value() -> float
unreal.SynthKnob.is_focusable() -> bool
unreal.SynthKnob.locked() -> bool
unreal.SynthKnob.mouse_fine_tune_speed() -> float
unreal.SynthKnob.mouse_speed() -> float
unreal.SynthKnob.on_controller_capture_begin(value: OnControllerCaptureBeginEvent) -> None
unreal.SynthKnob.on_controller_capture_end(value: OnControllerCaptureEndEvent) -> None
unreal.SynthKnob.on_mouse_capture_begin(value: OnMouseCaptureBeginEvent) -> None
unreal.SynthKnob.on_mouse_capture_end(value: OnMouseCaptureEndEvent) -> None
unreal.SynthKnob.on_value_changed(value: OnFloatValueChangedEvent) -> None
unreal.SynthKnob.parameter_name() -> Text
unreal.SynthKnob.parameter_units() -> Text
unreal.SynthKnob.set_locked(value: bool) -> None
unreal.SynthKnob.set_step_size(value: float) -> None
unreal.SynthKnob.set_value(value: float) -> None
unreal.SynthKnob.show_tooltip_info() -> bool
unreal.SynthKnob.step_size() -> float
unreal.SynthKnob.widget_style(value: SynthKnobStyle) -> None
```

## `unreal.SynthKnobStyle(SlateWidgetStyle)`

```python
unreal.SynthKnobStyle.__init__(large_knob: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], large_knob_overlay: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], medium_knob: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], medium_knob_overlay: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], min_value_angle: float = 0.000000, max_value_angle: float = 0.000000, knob_size: SynthKnobSize = SynthKnobSize.MEDIUM) -> None
unreal.SynthKnobStyle.knob_size(value: SynthKnobSize) -> None
unreal.SynthKnobStyle.large_knob(value: SlateBrush) -> None
unreal.SynthKnobStyle.large_knob_overlay(value: SlateBrush) -> None
unreal.SynthKnobStyle.max_value_angle(value: float) -> None
unreal.SynthKnobStyle.medium_knob(value: SlateBrush) -> None
unreal.SynthKnobStyle.medium_knob_overlay(value: SlateBrush) -> None
unreal.SynthKnobStyle.min_value_angle(value: float) -> None
```

## `unreal.SynthSamplePlayer(SynthComponent)`

```python
unreal.SynthSamplePlayer.get_current_playback_progress_percent() -> float
unreal.SynthSamplePlayer.get_current_playback_progress_time() -> float
unreal.SynthSamplePlayer.get_sample_duration() -> float
unreal.SynthSamplePlayer.is_loaded() -> bool
unreal.SynthSamplePlayer.on_sample_loaded(value: OnSampleLoaded) -> None
unreal.SynthSamplePlayer.on_sample_playback_progress(value: OnSamplePlaybackProgress) -> None
unreal.SynthSamplePlayer.seek_to_time(time_sec: float, seek_type: SamplePlayerSeekType, wrap: bool = True) -> None
unreal.SynthSamplePlayer.set_pitch(pitch: float, time_sec: float) -> None
unreal.SynthSamplePlayer.set_scrub_mode(scrub_mode: bool) -> None
unreal.SynthSamplePlayer.set_scrub_time_width(scrub_time_width_sec: float) -> None
unreal.SynthSamplePlayer.set_sound_wave(sound_wave: SoundWave) -> None
unreal.SynthSamplePlayer.sound_wave(value: SoundWave) -> None
```

## `unreal.TakeRecorderMicrophoneAudioManager(TakeRecorderAudioInputSettings)`

```python
unreal.TakeRecorderMicrophoneAudioManager.audio_input_device(value: AudioInputDeviceProperty) -> None
```

## `unreal.TakeRecorderMicrophoneAudioSource(TakeRecorderMicrophoneAudioSourceSettings)`

```python
unreal.TakeRecorderMicrophoneAudioSource.audio_channel(value: AudioInputDeviceChannelProperty) -> None
unreal.TakeRecorderMicrophoneAudioSource.audio_gain(value: float) -> None
unreal.TakeRecorderMicrophoneAudioSource.replace_recorded_audio(value: bool) -> None
unreal.TakeRecorderMicrophoneAudioSource.split_audio_channels_into_separate_tracks(value: bool) -> None
```

## `unreal.TakeRecorderMicrophoneAudioSourceSettings(TakeRecorderSource)`

```python
unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_asset_name(value: str) -> None
unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_source_name(value: Text) -> None
unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_sub_directory(value: str) -> None
unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_track_name(value: Text) -> None
```

## `unreal.VoipListenerSynthComponent(SynthComponent)`

```python
unreal.VoipListenerSynthComponent.is_idling() -> bool
```

## `unreal.WdpGlobalSettingsSoundParams(ParamsBase)`

```python
unreal.WdpGlobalSettingsSoundParams.__init__(volume: float = 0.000000) -> None
unreal.WdpGlobalSettingsSoundParams.volume(value: float) -> None
```

## `unreal.glTFRuntimeAudioConfig(StructBase)`

```python
unreal.glTFRuntimeAudioConfig.__init__(loop: bool = False, volume: float = 0.000000) -> None
unreal.glTFRuntimeAudioConfig.loop(value: bool) -> None
unreal.glTFRuntimeAudioConfig.volume(value: float) -> None
```

## `unreal.glTFRuntimeAudioEmitter(StructBase)`

```python
unreal.glTFRuntimeAudioEmitter.__init__(name: str = "", volume: float = 0.000000, sound: SoundBase = None) -> None
unreal.glTFRuntimeAudioEmitter.name(value: str) -> None
unreal.glTFRuntimeAudioEmitter.sound(value: SoundBase) -> None
unreal.glTFRuntimeAudioEmitter.volume(value: float) -> None
```

