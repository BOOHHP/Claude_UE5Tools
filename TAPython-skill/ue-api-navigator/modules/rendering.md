# Unreal Python API — Rendering

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AbcMaterialSettings(StructBase)`

```python
unreal.AbcMaterialSettings.__init__(create_materials: bool = False, find_materials: bool = False) -> None
unreal.AbcMaterialSettings.create_materials(value: bool) -> None
unreal.AbcMaterialSettings.find_materials(value: bool) -> None
```

## `unreal.AbcStaticMeshSettings(StructBase)`

```python
unreal.AbcStaticMeshSettings.__init__(merge_meshes: bool = False, propagate_matrix_transformations: bool = False, generate_lightmap_u_vs: bool = False) -> None
unreal.AbcStaticMeshSettings.generate_lightmap_u_vs(value: bool) -> None
unreal.AbcStaticMeshSettings.merge_meshes(value: bool) -> None
unreal.AbcStaticMeshSettings.propagate_matrix_transformations(value: bool) -> None
```

## `unreal.AesFacadeMaterialInfo(StructBase)`

```python
unreal.AesFacadeMaterialInfo.__init__(material: SoftObjectPath = [""], texture_index: int = 0, random_texture_index: bool = False, max_texture_index: int = 0, unit_uv_size: Vector2f = [0.000000, 0.000000], uv_tile_precision: IntPoint = [0, 0]) -> None
unreal.AesFacadeMaterialInfo.material(value: SoftObjectPath) -> None
unreal.AesFacadeMaterialInfo.max_texture_index(value: int) -> None
unreal.AesFacadeMaterialInfo.random_texture_index(value: bool) -> None
unreal.AesFacadeMaterialInfo.texture_index(value: int) -> None
unreal.AesFacadeMaterialInfo.unit_uv_size(value: Vector2f) -> None
unreal.AesFacadeMaterialInfo.uv_tile_precision(value: IntPoint) -> None
```

## `unreal.AesInstancedStaticMeshComponent(InstancedStaticMeshComponent)`

```python
unreal.AesInstancedStaticMeshComponent.allow_create_physics_state(value: bool) -> None
unreal.AesInstancedStaticMeshComponent.local_bounds(value: BoxSphereBounds) -> None
unreal.AesInstancedStaticMeshComponent.set_bounds(bounds: BoxSphereBounds) -> None
```

## `unreal.AesMaterialData(StructBase)`

```python
unreal.AesMaterialData.__init__(asset_ref: SoftObjectPath = [""], texture_index: int = 0, unit_uv_size: float = 0.000000) -> None
unreal.AesMaterialData.asset_ref(value: SoftObjectPath) -> None
unreal.AesMaterialData.texture_index(value: int) -> None
unreal.AesMaterialData.unit_uv_size(value: float) -> None
```

## `unreal.AesRenderResourceSettings(DeveloperSettings)`

```python
unreal.AesRenderResourceSettings.component_mobility() -> ComponentMobility
```

## `unreal.AesStaticMeshComponent(StaticMeshComponent)`

```python
unreal.AesStaticMeshComponent.allow_create_physics_state(value: bool) -> None
```

## `unreal.AesTilesHighlightLayerParam(AesTilesHighlightParam)`

```python
unreal.AesTilesHighlightLayerParam.__init__(aes_tiles_eid: int = 0, highlight: bool = False, style_name: Name = "None", layers: Array[str] = []) -> None
unreal.AesTilesHighlightLayerParam.layers(value: Array[str]) -> None
```

## `unreal.AesTilesHighlightNodeIdParam(AesTilesHighlightParam)`

```python
unreal.AesTilesHighlightNodeIdParam.__init__(aes_tiles_eid: int = 0, highlight: bool = False, style_name: Name = "None", node_ids: Array[int] = []) -> None
unreal.AesTilesHighlightNodeIdParam.node_ids(value: Array[int]) -> None
```

## `unreal.AesTilesHighlightParam(AesTilesVisualApiParamBase)`

```python
unreal.AesTilesHighlightParam.__init__(aes_tiles_eid: int = 0, highlight: bool = False, style_name: Name = "None") -> None
unreal.AesTilesHighlightParam.highlight(value: bool) -> None
unreal.AesTilesHighlightParam.style_name(value: Name) -> None
```

## `unreal.AnimNotifyState_TimedNiagaraEffect(AnimNotifyState)`

```python
unreal.AnimNotifyState_TimedNiagaraEffect.apply_rate_scale_as_time_dilation() -> bool
unreal.AnimNotifyState_TimedNiagaraEffect.destroy_at_end() -> bool
unreal.AnimNotifyState_TimedNiagaraEffect.get_spawned_effect(mesh_comp: MeshComponent) -> FXSystemComponent
unreal.AnimNotifyState_TimedNiagaraEffect.location_offset() -> Vector
unreal.AnimNotifyState_TimedNiagaraEffect.rotation_offset() -> Rotator
unreal.AnimNotifyState_TimedNiagaraEffect.socket_name() -> Name
unreal.AnimNotifyState_TimedNiagaraEffect.template() -> NiagaraSystem
```

## `unreal.AnimNotifyState_TimedNiagaraEffectAdvanced(AnimNotifyState_TimedNiagaraEffect)`

```python
unreal.AnimNotifyState_TimedNiagaraEffectAdvanced.apply_rate_scale_to_progress() -> bool
unreal.AnimNotifyState_TimedNiagaraEffectAdvanced.get_notify_progress(mesh_comp: MeshComponent) -> float
```

## `unreal.AnimNotify_PlayNiagaraEffect(AnimNotify)`

```python
unreal.AnimNotify_PlayNiagaraEffect.attached() -> bool
unreal.AnimNotify_PlayNiagaraEffect.get_spawned_effect() -> FXSystemComponent
unreal.AnimNotify_PlayNiagaraEffect.location_offset() -> Vector
unreal.AnimNotify_PlayNiagaraEffect.rotation_offset() -> Rotator
unreal.AnimNotify_PlayNiagaraEffect.socket_name() -> Name
unreal.AnimNotify_PlayNiagaraEffect.template() -> NiagaraSystem
```

## `unreal.AnimatedSparseVolumeTextureController(Object)`

```python
unreal.AnimatedSparseVolumeTextureController.blocking_streaming_requests(value: bool) -> None
unreal.AnimatedSparseVolumeTextureController.frame_rate(value: float) -> None
unreal.AnimatedSparseVolumeTextureController.get_current_frame() -> SparseVolumeTextureFrame
unreal.AnimatedSparseVolumeTextureController.get_current_frames_for_interpolation() -> Tuple[SparseVolumeTextureFrame, SparseVolumeTextureFrame, float]
unreal.AnimatedSparseVolumeTextureController.get_duration() -> float
unreal.AnimatedSparseVolumeTextureController.get_fractional_frame_index() -> float
unreal.AnimatedSparseVolumeTextureController.get_frame_by_index(frame_index: int) -> SparseVolumeTextureFrame
unreal.AnimatedSparseVolumeTextureController.is_playing(value: bool) -> None
unreal.AnimatedSparseVolumeTextureController.mip_level(value: int) -> None
unreal.AnimatedSparseVolumeTextureController.pause() -> None
unreal.AnimatedSparseVolumeTextureController.play() -> None
unreal.AnimatedSparseVolumeTextureController.sparse_volume_texture(value: SparseVolumeTexture) -> None
unreal.AnimatedSparseVolumeTextureController.stop() -> None
unreal.AnimatedSparseVolumeTextureController.time(value: float) -> None
unreal.AnimatedSparseVolumeTextureController.update(delta_time: float) -> None
```

## `unreal.AnimatedTexture2D_Cov(Texture2DDynamic)`

```python
unreal.AnimatedTexture2D_Cov.address_x(value: TextureAddress) -> None
unreal.AnimatedTexture2D_Cov.address_y(value: TextureAddress) -> None
unreal.AnimatedTexture2D_Cov.default_frame_delay(value: float) -> None
unreal.AnimatedTexture2D_Cov.get_animation_length() -> float
unreal.AnimatedTexture2D_Cov.get_play_rate() -> float
unreal.AnimatedTexture2D_Cov.is_looping() -> bool
unreal.AnimatedTexture2D_Cov.is_playing() -> bool
unreal.AnimatedTexture2D_Cov.looping(value: bool) -> None
unreal.AnimatedTexture2D_Cov.play() -> None
unreal.AnimatedTexture2D_Cov.play_from_start() -> None
unreal.AnimatedTexture2D_Cov.play_rate(value: float) -> None
unreal.AnimatedTexture2D_Cov.set_looping(new_looping: bool) -> None
unreal.AnimatedTexture2D_Cov.set_play_rate(new_rate: float) -> None
unreal.AnimatedTexture2D_Cov.stop() -> None
unreal.AnimatedTexture2D_Cov.supports_transparency(value: bool) -> None
```

## `unreal.ApplyMaterialToEntityParams(ParamsBase)`

```python
unreal.ApplyMaterialToEntityParams.__init__(eid_to_new_material_info: Map[int, NewMaterialsInfoArray] = {}) -> None
unreal.ApplyMaterialToEntityParams.eid_to_new_material_info(value: Map[int, NewMaterialsInfoArray]) -> None
```

## `unreal.AsyncNiagaraCaptureSimCache(CancellableAsyncAction)`

```python
unreal.AsyncNiagaraCaptureSimCache.capture_complete(value: OnCaptureComplete) -> None
```

## `unreal.AsyncNiagaraCaptureSimCache_OnCaptureComplete(MulticastDelegateBase)`

```python
unreal.AsyncNiagaraCaptureSimCache_OnCaptureComplete.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioMaterialButton(Widget)`

```python
unreal.AudioMaterialButton.get_is_pressed() -> bool
unreal.AudioMaterialButton.is_pressed(value: bool) -> None
unreal.AudioMaterialButton.on_button_pressed_changed_event(value: OnButtonPressedChangedEvent) -> None
unreal.AudioMaterialButton.set_is_pressed(pressed: bool) -> None
unreal.AudioMaterialButton.widget_style(value: AudioMaterialButtonStyle) -> None
```

## `unreal.AudioMaterialButtonStyle(AudioMaterialWidgetStyle)`

```python
unreal.AudioMaterialButtonStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000], button_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_main_color_tint_1: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_main_color_tint_2: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_accent_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_shadow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_unpressed_outline_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], button_pressed_outline_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.AudioMaterialButtonStyle.button_accent_color(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_main_color(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_main_color_tint_1(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_main_color_tint_2(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_pressed_outline_color(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_shadow_color(value: LinearColor) -> None
unreal.AudioMaterialButtonStyle.button_unpressed_outline_color(value: LinearColor) -> None
```

## `unreal.AudioMaterialEnvelope(Widget)`

```python
unreal.AudioMaterialEnvelope.envelope_settings(value: AudioMaterialEnvelopeSettings) -> None
unreal.AudioMaterialEnvelope.widget_style(value: AudioMaterialEnvelopeStyle) -> None
```

## `unreal.AudioMaterialEnvelopeSettings(StructBase)`

```python
unreal.AudioMaterialEnvelopeSettings.__init__(attack_curve: float = 0.000000, attack_value: float = 0.000000, attack_time: float = 0.000000, decay_curve: float = 0.000000, decay_time: float = 0.000000, sustain_value: float = 0.000000, release_curve: float = 0.000000, release_time: float = 0.000000) -> None
unreal.AudioMaterialEnvelopeSettings.attack_curve(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.attack_time(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.attack_value(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.decay_curve(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.decay_time(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.release_curve(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.release_time(value: float) -> None
unreal.AudioMaterialEnvelopeSettings.sustain_value(value: float) -> None
```

## `unreal.AudioMaterialEnvelopeStyle(AudioMaterialWidgetStyle)`

```python
unreal.AudioMaterialEnvelopeStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000], curve_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], outline_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.AudioMaterialEnvelopeStyle.background_color(value: LinearColor) -> None
unreal.AudioMaterialEnvelopeStyle.curve_color(value: LinearColor) -> None
unreal.AudioMaterialEnvelopeStyle.outline_color(value: LinearColor) -> None
```

## `unreal.AudioMaterialKnob(Widget)`

```python
unreal.AudioMaterialKnob.fine_tune_speed(value: float) -> None
unreal.AudioMaterialKnob.get_fine_tune_speed() -> float
unreal.AudioMaterialKnob.get_is_locked() -> bool
unreal.AudioMaterialKnob.get_mouse_uses_step() -> bool
unreal.AudioMaterialKnob.get_step_size() -> float
unreal.AudioMaterialKnob.get_tune_speed() -> float
unreal.AudioMaterialKnob.get_value() -> float
unreal.AudioMaterialKnob.locked(value: bool) -> None
unreal.AudioMaterialKnob.mouse_uses_step(value: bool) -> None
unreal.AudioMaterialKnob.on_knob_value_changed(value: OnKnobValueChangedEvent) -> None
unreal.AudioMaterialKnob.set_fine_tune_speed(value: float) -> None
unreal.AudioMaterialKnob.set_locked(locked: bool) -> None
unreal.AudioMaterialKnob.set_mouse_uses_step(uses_step: bool) -> None
unreal.AudioMaterialKnob.set_step_size(value: float) -> None
unreal.AudioMaterialKnob.set_tune_speed(value: float) -> None
unreal.AudioMaterialKnob.set_value(value: float) -> None
unreal.AudioMaterialKnob.step_size(value: float) -> None
unreal.AudioMaterialKnob.tune_speed(value: float) -> None
unreal.AudioMaterialKnob.value(value: float) -> None
unreal.AudioMaterialKnob.widget_style(value: AudioMaterialKnobStyle) -> None
```

## `unreal.AudioMaterialKnobStyle(AudioMaterialWidgetStyle)`

```python
unreal.AudioMaterialKnobStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000], knob_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_accent_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_shadow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_smooth_bevel_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_indicator_dot_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_edge_fill_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_shadow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_fill_min_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_fill_mid_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_fill_max_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], knob_bar_fill_tint_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], text_box_style: AudioTextBoxStyle = [[[[0.000000, 0.000000, 0.000000, 0.000000], 0], SlateBrushDrawType.ROUNDED_BOX, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[4.000000, 4.000000, 4.000000, 4.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.FIXED_RADIUS, False]], [[0.000000, 0.000000, 0.000000, 0.000000], 0]]) -> None
unreal.AudioMaterialKnobStyle.knob_accent_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_fill_max_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_fill_mid_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_fill_min_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_fill_tint_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_bar_shadow_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_edge_fill_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_indicator_dot_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_main_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_shadow_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.knob_smooth_bevel_color(value: LinearColor) -> None
unreal.AudioMaterialKnobStyle.text_box_style(value: AudioTextBoxStyle) -> None
```

## `unreal.AudioMaterialMeter(Widget)`

```python
unreal.AudioMaterialMeter.get_meter_channel_info() -> Array[MeterChannelInfo]
unreal.AudioMaterialMeter.meter_channel_info(value: Array[MeterChannelInfo]) -> None
unreal.AudioMaterialMeter.orientation() -> Orientation
unreal.AudioMaterialMeter.set_meter_channel_info(meter_channel_info: Array[MeterChannelInfo]) -> None
unreal.AudioMaterialMeter.widget_style(value: AudioMaterialMeterStyle) -> None
```

## `unreal.AudioMaterialMeterStyle(AudioMaterialWidgetStyle)`

```python
unreal.AudioMaterialMeterStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000], meter_fill_min_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_fill_mid_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_fill_max_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_fill_background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], meter_padding: Vector2D = [0.000000, 0.000000], value_range_db: Vector2D = [0.000000, 0.000000], show_scale: bool = False, scale_side: bool = False, scale_hash_offset: float = 0.000000, scale_hash_width: float = 0.000000, scale_hash_height: float = 0.000000, decibels_per_hash: int = 0, font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000]) -> None
unreal.AudioMaterialMeterStyle.decibels_per_hash(value: int) -> None
unreal.AudioMaterialMeterStyle.font(value: SlateFontInfo) -> None
unreal.AudioMaterialMeterStyle.meter_fill_background_color(value: LinearColor) -> None
unreal.AudioMaterialMeterStyle.meter_fill_max_color(value: LinearColor) -> None
unreal.AudioMaterialMeterStyle.meter_fill_mid_color(value: LinearColor) -> None
unreal.AudioMaterialMeterStyle.meter_fill_min_color(value: LinearColor) -> None
unreal.AudioMaterialMeterStyle.meter_padding(value: Vector2D) -> None
unreal.AudioMaterialMeterStyle.scale_hash_height(value: float) -> None
unreal.AudioMaterialMeterStyle.scale_hash_offset(value: float) -> None
unreal.AudioMaterialMeterStyle.scale_hash_width(value: float) -> None
unreal.AudioMaterialMeterStyle.scale_side(value: bool) -> None
unreal.AudioMaterialMeterStyle.show_scale(value: bool) -> None
unreal.AudioMaterialMeterStyle.value_range_db(value: Vector2D) -> None
```

## `unreal.AudioMaterialMeter_GetMeterChannelInfo(DelegateBase)`

```python
unreal.AudioMaterialMeter_GetMeterChannelInfo.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AudioMaterialSlider(Widget)`

```python
unreal.AudioMaterialSlider.fine_tune_speed(value: float) -> None
unreal.AudioMaterialSlider.get_fine_tune_speed() -> float
unreal.AudioMaterialSlider.get_is_locked() -> bool
unreal.AudioMaterialSlider.get_mouse_uses_step() -> bool
unreal.AudioMaterialSlider.get_step_size() -> float
unreal.AudioMaterialSlider.get_tune_speed() -> float
unreal.AudioMaterialSlider.get_value() -> float
unreal.AudioMaterialSlider.locked(value: bool) -> None
unreal.AudioMaterialSlider.mouse_uses_step(value: bool) -> None
unreal.AudioMaterialSlider.on_value_changed(value: OnSliderFloatValueChangedEvent) -> None
unreal.AudioMaterialSlider.set_fine_tune_speed(value: float) -> None
unreal.AudioMaterialSlider.set_locked(locked: bool) -> None
unreal.AudioMaterialSlider.set_mouse_uses_step(uses_step: bool) -> None
unreal.AudioMaterialSlider.set_step_size(value: float) -> None
unreal.AudioMaterialSlider.set_tune_speed(value: float) -> None
unreal.AudioMaterialSlider.set_value(value: float) -> None
unreal.AudioMaterialSlider.step_size(value: float) -> None
unreal.AudioMaterialSlider.tune_speed(value: float) -> None
unreal.AudioMaterialSlider.value(value: float) -> None
unreal.AudioMaterialSlider.widget_style(value: AudioMaterialSliderStyle) -> None
```

## `unreal.AudioMaterialSliderStyle(AudioMaterialWidgetStyle)`

```python
unreal.AudioMaterialSliderStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000], slider_background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], slider_background_accent_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], slider_value_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], slider_handle_main_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], slider_handle_outline_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], text_box_style: AudioTextBoxStyle = [[[[0.000000, 0.000000, 0.000000, 0.000000], 0], SlateBrushDrawType.ROUNDED_BOX, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[4.000000, 4.000000, 4.000000, 4.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.FIXED_RADIUS, False]], [[0.000000, 0.000000, 0.000000, 0.000000], 0]]) -> None
unreal.AudioMaterialSliderStyle.slider_background_accent_color(value: LinearColor) -> None
unreal.AudioMaterialSliderStyle.slider_background_color(value: LinearColor) -> None
unreal.AudioMaterialSliderStyle.slider_handle_main_color(value: LinearColor) -> None
unreal.AudioMaterialSliderStyle.slider_handle_outline_color(value: LinearColor) -> None
unreal.AudioMaterialSliderStyle.slider_value_main_color(value: LinearColor) -> None
unreal.AudioMaterialSliderStyle.text_box_style(value: AudioTextBoxStyle) -> None
```

## `unreal.AudioMaterialWidgetStyle(SlateWidgetStyle)`

```python
unreal.AudioMaterialWidgetStyle.__init__(material: MaterialInterface = None, desired_size: Vector2f = [0.000000, 0.000000]) -> None
unreal.AudioMaterialWidgetStyle.desired_size(value: Vector2f) -> None
unreal.AudioMaterialWidgetStyle.material(value: MaterialInterface) -> None
```

## `unreal.BakeMultiTexture2DProperties(InteractiveToolPropertySet)`

```python
unreal.BakeMultiTexture2DProperties.all_source_textures() -> Array[Texture2D]
```

## `unreal.BatchStaticMeshEntityAtom(EntityAtomBase)`

```python
unreal.BatchStaticMeshEntityAtom.line_cells() -> Map[int, MeshCellsInfo]
unreal.BatchStaticMeshEntityAtom.region_cells() -> Map[int, MeshCellsInfo]
```

## `unreal.BlueprintMaterialTextureNodesBPLibrary(BlueprintFunctionLibrary)`

```python
unreal.BlueprintMaterialTextureNodesBPLibrary.create_mic_editor_only(material: MaterialInterface, name: str = "MIC_") -> MaterialInstanceConstant
unreal.BlueprintMaterialTextureNodesBPLibrary.render_target_sample_rectangle_editor_only(render_target: TextureRenderTarget2D, rect: LinearColor) -> Array[LinearColor]
unreal.BlueprintMaterialTextureNodesBPLibrary.render_target_sample_uv_editor_only(render_target: TextureRenderTarget2D, uv: Vector2D) -> LinearColor
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_blend_mode_editor_only(material: MaterialInstanceConstant, blend_mode: BlendMode = BlendMode.BLEND_OPAQUE) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_dithered_lod_transition_editor_only(material: MaterialInstanceConstant, dithered_lod_transition: bool = False) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_is_thin_surface_editor_only(material: MaterialInstanceConstant, is_thin_surface: bool = False) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_scalar_param_editor_only(material: MaterialInstanceConstant, param_name: str = "test", value: float = 0.000000) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_shading_model_editor_only(material: MaterialInstanceConstant, shading_model: MaterialShadingModel = MaterialShadingModel.MSM_DEFAULT_LIT) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_texture_param_editor_only(material: MaterialInstanceConstant, param_name: str, texture: Texture2D = None) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_two_sided_editor_only(material: MaterialInstanceConstant, two_sided: bool = False) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_vector_param_editor_only(material: MaterialInstanceConstant, param_name: str, value: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> bool
unreal.BlueprintMaterialTextureNodesBPLibrary.texture2d_sample_uv_editor_only(texture: Texture2D, uv: Vector2D) -> LinearColor
```

## `unreal.CanvasRenderTarget2D(TextureRenderTarget2D)`

```python
unreal.CanvasRenderTarget2D.create_canvas_render_target2d(world_context_object: Object, canvas_render_target2d_class: Class, width: int = 1024, height: int = 1024) -> CanvasRenderTarget2D
unreal.CanvasRenderTarget2D.get_size() -> Tuple[int, int]
unreal.CanvasRenderTarget2D.on_canvas_render_target_update(value: OnCanvasRenderTargetUpdate) -> None
unreal.CanvasRenderTarget2D.receive_update(canvas: Canvas, width: int, height: int) -> None
unreal.CanvasRenderTarget2D.sample_count(value: TextureRenderTargetSampleCount) -> None
unreal.CanvasRenderTarget2D.update_resource() -> None
```

## `unreal.CesiumFeatureIdTexture(StructBase)`

```python
unreal.CesiumFeatureIdTexture.__init__() -> None
```

## `unreal.CesiumFeatureIdTextureBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_texture_coordinates(feature_id_texture: CesiumFeatureIdTexture, u: float, v: float) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_uv(feature_id_texture: CesiumFeatureIdTexture, uv: Vector2D) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_for_vertex(feature_id_texture: CesiumFeatureIdTexture, vertex_index: int) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_from_hit(feature_id_texture: CesiumFeatureIdTexture, hit: HitResult) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_id_texture_status(feature_id_texture: CesiumFeatureIdTexture) -> CesiumFeatureIdTextureStatus
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_feature_table_name(feature_id_texture: CesiumFeatureIdTexture) -> str
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_gltf_texture_coordinate_set_index(feature_id_texture: CesiumFeatureIdTexture) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_texture_coordinate_index(component: PrimitiveComponent, feature_id_texture: CesiumFeatureIdTexture) -> int
unreal.CesiumFeatureIdTextureBlueprintLibrary.get_unreal_uv_channel(component: PrimitiveComponent, feature_id_texture: CesiumFeatureIdTexture) -> int
```

## `unreal.CesiumFeatureTexture(CesiumPropertyTexture)`

```python
unreal.CesiumFeatureTexture.__init__() -> None
```

## `unreal.CesiumFeatureTextureProperty(CesiumPropertyTextureProperty)`

```python
unreal.CesiumFeatureTextureProperty.__init__() -> None
```

## `unreal.CesiumFlightCompleted(MulticastDelegateBase)`

```python
unreal.CesiumFlightCompleted.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CesiumFlightInterrupted(MulticastDelegateBase)`

```python
unreal.CesiumFlightInterrupted.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CesiumPropertyTexture(StructBase)`

```python
unreal.CesiumPropertyTexture.__init__() -> None
```

## `unreal.CesiumPropertyTextureBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.CesiumPropertyTextureBlueprintLibrary.find_property(property_texture: CesiumPropertyTexture, property_name: str) -> CesiumPropertyTextureProperty
unreal.CesiumPropertyTextureBlueprintLibrary.get_metadata_values_for_uv(property_texture: CesiumPropertyTexture, uv: Vector2D) -> Map[str, CesiumMetadataValue]
unreal.CesiumPropertyTextureBlueprintLibrary.get_metadata_values_from_hit(property_texture: CesiumPropertyTexture, hit: HitResult) -> Map[str, CesiumMetadataValue]
unreal.CesiumPropertyTextureBlueprintLibrary.get_properties(property_texture: CesiumPropertyTexture) -> Map[str, CesiumPropertyTextureProperty]
unreal.CesiumPropertyTextureBlueprintLibrary.get_property_names(property_texture: CesiumPropertyTexture) -> Array[str]
unreal.CesiumPropertyTextureBlueprintLibrary.get_property_texture_name(property_texture: CesiumPropertyTexture) -> str
unreal.CesiumPropertyTextureBlueprintLibrary.get_property_texture_status(property_texture: CesiumPropertyTexture) -> CesiumPropertyTextureStatus
```

## `unreal.CesiumPropertyTextureDescription(StructBase)`

```python
unreal.CesiumPropertyTextureDescription.__init__() -> None
```

## `unreal.CesiumPropertyTextureProperty(StructBase)`

```python
unreal.CesiumPropertyTextureProperty.__init__() -> None
```

## `unreal.CesiumPropertyTexturePropertyBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array(property_: CesiumPropertyTextureProperty, uv: Vector2D) -> CesiumPropertyArray
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array_element_blueprint_type(property_: CesiumPropertyTextureProperty) -> CesiumMetadataBlueprintType
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_array_size(property_: CesiumPropertyTextureProperty) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_blueprint_type(property_: CesiumPropertyTextureProperty) -> CesiumMetadataBlueprintType
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_byte(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: int = 0) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_channels(property_: CesiumPropertyTextureProperty) -> Array[int]
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_component_count(property_: CesiumPropertyTextureProperty) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_default_value(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_float(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: float = 0.000000) -> float
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_float64(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: float = 0.000000) -> float
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_gltf_texture_coordinate_set_index(property_: CesiumPropertyTextureProperty) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_int_point(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: IntPoint) -> IntPoint
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_int_vector(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: IntVector) -> IntVector
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_integer(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: int = 0) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_maximum_value(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_minimum_value(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_no_data_value(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_offset(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_property_texture_property_status(property_: CesiumPropertyTextureProperty) -> CesiumPropertyTexturePropertyStatus
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_raw_value(property_: CesiumPropertyTextureProperty, uv: Vector2D) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_scale(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_swizzle(property_: CesiumPropertyTextureProperty) -> str
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_texture_coordinate_index(component: PrimitiveComponent, property_: CesiumPropertyTextureProperty) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_unreal_uv_channel(component: PrimitiveComponent, property_: CesiumPropertyTextureProperty) -> int
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_value(property_: CesiumPropertyTextureProperty, uv: Vector2D) -> CesiumMetadataValue
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_value_type(property_: CesiumPropertyTextureProperty) -> CesiumMetadataValueType
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: Vector) -> Vector
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector2d(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: Vector2D) -> Vector2D
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.get_vector4(property_: CesiumPropertyTextureProperty, uv: Vector2D, default_value: Vector4) -> Vector4
unreal.CesiumPropertyTexturePropertyBlueprintLibrary.is_normalized(property_: CesiumPropertyTextureProperty) -> bool
```

## `unreal.CesiumPropertyTexturePropertyDescription(StructBase)`

```python
unreal.CesiumPropertyTexturePropertyDescription.__init__() -> None
```

## `unreal.ChangedMaterialInfo(StructBase)`

```python
unreal.ChangedMaterialInfo.__init__() -> None
```

## `unreal.ChaosPhysicalMaterial(Object)`

```python
unreal.ChaosPhysicalMaterial.angular_ether_drag() -> float
unreal.ChaosPhysicalMaterial.friction() -> float
unreal.ChaosPhysicalMaterial.linear_ether_drag() -> float
unreal.ChaosPhysicalMaterial.restitution() -> float
unreal.ChaosPhysicalMaterial.sleeping_angular_velocity_threshold() -> float
unreal.ChaosPhysicalMaterial.sleeping_linear_velocity_threshold() -> float
unreal.ChaosPhysicalMaterial.static_friction() -> float
```

## `unreal.ChinaMapHighlightProvinceParams(ParamsBase)`

```python
unreal.ChinaMapHighlightProvinceParams.__init__(province_code: str = "", highlight: bool = False, color: str = "") -> None
unreal.ChinaMapHighlightProvinceParams.color(value: str) -> None
unreal.ChinaMapHighlightProvinceParams.highlight(value: bool) -> None
unreal.ChinaMapHighlightProvinceParams.province_code(value: str) -> None
```

## `unreal.CompletedFlight(MulticastDelegateBase)`

```python
unreal.CompletedFlight.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.ComponentMaterialInfo(StructBase)`

```python
unreal.ComponentMaterialInfo.__init__(material_slot_name: Name = "None", material_slot_index: int = 0, material_type: ComponentMaterialType = ComponentMaterialType.EMPTY) -> None
unreal.ComponentMaterialInfo.material_slot_index(value: int) -> None
unreal.ComponentMaterialInfo.material_slot_name(value: Name) -> None
unreal.ComponentMaterialInfo.material_type(value: ComponentMaterialType) -> None
```

## `unreal.ComponentSectionOriginalMaterial(StructBase)`

```python
unreal.ComponentSectionOriginalMaterial.__init__() -> None
```

## `unreal.CreateHighlightAreaParams(ParamsBase)`

```python
unreal.CreateHighlightAreaParams.__init__(polygon_entity_eid: str = "", highlight_area_style: HighlightAreaStyle = ["ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000]) -> None
unreal.CreateHighlightAreaParams.highlight_area_style(value: HighlightAreaStyle) -> None
unreal.CreateHighlightAreaParams.polygon_entity_eid(value: str) -> None
```

## `unreal.CreateMaterialObjectParams(StructBase)`

```python
unreal.CreateMaterialObjectParams.__init__() -> None
```

## `unreal.CreateMaterialObjectResult(StructBase)`

```python
unreal.CreateMaterialObjectResult.__init__() -> None
```

## `unreal.CreateTextureObjectParams(StructBase)`

```python
unreal.CreateTextureObjectParams.__init__() -> None
```

## `unreal.CreateTextureObjectResult(StructBase)`

```python
unreal.CreateTextureObjectResult.__init__() -> None
```

## `unreal.DCPMaterialEditorAssetNameResult(ResultBase)`

```python
unreal.DCPMaterialEditorAssetNameResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, mid: str = "", picture: str = "") -> None
unreal.DCPMaterialEditorAssetNameResult.mid(value: str) -> None
unreal.DCPMaterialEditorAssetNameResult.picture(value: str) -> None
```

## `unreal.DCPMaterialEditorAssetNamesResult(ResultBase)`

```python
unreal.DCPMaterialEditorAssetNamesResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, material_infos: Array[DCPMaterialEditorAssetNameResult] = []) -> None
unreal.DCPMaterialEditorAssetNamesResult.material_infos(value: Array[DCPMaterialEditorAssetNameResult]) -> None
```

## `unreal.DCPMaterialEditorNameResult(ResultBase)`

```python
unreal.DCPMaterialEditorNameResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, material_name: str = "", material_lable: str = "") -> None
unreal.DCPMaterialEditorNameResult.material_lable(value: str) -> None
unreal.DCPMaterialEditorNameResult.material_name(value: str) -> None
```

## `unreal.DCPMaterialEditorNamesResult(ResultBase)`

```python
unreal.DCPMaterialEditorNamesResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, material_infos: Array[DCPMaterialEditorNameResult] = []) -> None
unreal.DCPMaterialEditorNamesResult.material_infos(value: Array[DCPMaterialEditorNameResult]) -> None
```

## `unreal.DCPMaterialEditorResetParam(ParamsBase)`

```python
unreal.DCPMaterialEditorResetParam.__init__(material_name: str = "") -> None
unreal.DCPMaterialEditorResetParam.material_name(value: str) -> None
```

## `unreal.DCPMaterialEditorSetParam(ParamsBase)`

```python
unreal.DCPMaterialEditorSetParam.__init__(material_name: str = "", mid: str = "") -> None
unreal.DCPMaterialEditorSetParam.material_name(value: str) -> None
unreal.DCPMaterialEditorSetParam.mid(value: str) -> None
```

## `unreal.DCPMaterialEntityResult(ResultBase)`

```python
unreal.DCPMaterialEntityResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, material_sphere_eid: str = "") -> None
unreal.DCPMaterialEntityResult.material_sphere_eid(value: str) -> None
```

## `unreal.DCPMaterialNodeGetParam(StructBase)`

```python
unreal.DCPMaterialNodeGetParam.__init__(node_ids: Array[int] = [], mid: str = "", material_sphere_eid: str = "") -> None
unreal.DCPMaterialNodeGetParam.material_sphere_eid(value: str) -> None
unreal.DCPMaterialNodeGetParam.mid(value: str) -> None
unreal.DCPMaterialNodeGetParam.node_ids(value: Array[int]) -> None
```

## `unreal.DCPMaterialNodeGetParams(ResultBase)`

```python
unreal.DCPMaterialNodeGetParams.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, node_materials: Array[DCPMaterialNodeGetParam] = []) -> None
unreal.DCPMaterialNodeGetParams.node_materials(value: Array[DCPMaterialNodeGetParam]) -> None
```

## `unreal.DCPMaterialNodeResetParam(ParamsBase)`

```python
unreal.DCPMaterialNodeResetParam.__init__(model_eid: str = "", node_ids: Array[int] = []) -> None
unreal.DCPMaterialNodeResetParam.model_eid(value: str) -> None
unreal.DCPMaterialNodeResetParam.node_ids(value: Array[int]) -> None
```

## `unreal.DCPMaterialNodeSetParam(ParamsBase)`

```python
unreal.DCPMaterialNodeSetParam.__init__(node_ids: Array[int] = [], mid: str = "") -> None
unreal.DCPMaterialNodeSetParam.mid(value: str) -> None
unreal.DCPMaterialNodeSetParam.node_ids(value: Array[int]) -> None
```

## `unreal.DCPMaterialTransparencyDiagramNodeParam(ParamsBase)`

```python
unreal.DCPMaterialTransparencyDiagramNodeParam.__init__(node_ids: Array[int] = [], use_wire_frame: bool = False) -> None
unreal.DCPMaterialTransparencyDiagramNodeParam.node_ids(value: Array[int]) -> None
unreal.DCPMaterialTransparencyDiagramNodeParam.use_wire_frame(value: bool) -> None
```

## `unreal.DCPMaterialTransparencyDiagramPercentParam(ParamsBase)`

```python
unreal.DCPMaterialTransparencyDiagramPercentParam.__init__(transparency_percent: float = 0.000000) -> None
unreal.DCPMaterialTransparencyDiagramPercentParam.transparency_percent(value: float) -> None
```

## `unreal.DCPNodeHighLightStyleGetParam(ResultBase)`

```python
unreal.DCPNodeHighLightStyleGetParam.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, color: str = "", opacity: float = 0.000000, opacity_scale: float = 0.000000, can_be_occluded: bool = False) -> None
unreal.DCPNodeHighLightStyleGetParam.can_be_occluded(value: bool) -> None
unreal.DCPNodeHighLightStyleGetParam.color(value: str) -> None
unreal.DCPNodeHighLightStyleGetParam.opacity(value: float) -> None
unreal.DCPNodeHighLightStyleGetParam.opacity_scale(value: float) -> None
```

## `unreal.DCPNodeHighLightStyleParam(ParamsBase)`

```python
unreal.DCPNodeHighLightStyleParam.__init__(color: str = "", opacity: float = 0.000000, opacity_scale: float = 0.000000, can_be_occluded: bool = False, outline_style: NodeOutlineStyleParam = []) -> None
unreal.DCPNodeHighLightStyleParam.can_be_occluded(value: bool) -> None
unreal.DCPNodeHighLightStyleParam.color(value: str) -> None
unreal.DCPNodeHighLightStyleParam.opacity(value: float) -> None
unreal.DCPNodeHighLightStyleParam.opacity_scale(value: float) -> None
unreal.DCPNodeHighLightStyleParam.outline_style(value: NodeOutlineStyleParam) -> None
```

## `unreal.DCPNodeHightLightParam(DCPNodeBaseParam)`

```python
unreal.DCPNodeHightLightParam.__init__(node_id: int = 0, hightlight: bool = False, exclusion: bool = False, high_light_style: DCPNodeHighLightStyleParam = ["000000", 0.500000, 0.100000, False, []]) -> None
unreal.DCPNodeHightLightParam.exclusion(value: bool) -> None
unreal.DCPNodeHightLightParam.high_light_style(value: DCPNodeHighLightStyleParam) -> None
unreal.DCPNodeHightLightParam.hightlight(value: bool) -> None
```

## `unreal.DCPRoomHighLightParam(ParamsBase)`

```python
unreal.DCPRoomHighLightParam.__init__(room_ids: Array[int] = [], is_visible: bool = False, color: str = "", opacity: float = 0.000000, can_be_occluded: bool = False) -> None
unreal.DCPRoomHighLightParam.can_be_occluded(value: bool) -> None
unreal.DCPRoomHighLightParam.color(value: str) -> None
unreal.DCPRoomHighLightParam.is_visible(value: bool) -> None
unreal.DCPRoomHighLightParam.opacity(value: float) -> None
unreal.DCPRoomHighLightParam.room_ids(value: Array[int]) -> None
```

## `unreal.DataDrivenShaderPlatformInfoInput(StructBase)`

```python
unreal.DataDrivenShaderPlatformInfoInput.__init__() -> None
```

## `unreal.DatasmithStaticMeshImportOptions(StructBase)`

```python
unreal.DatasmithStaticMeshImportOptions.__init__(min_lightmap_resolution: DatasmithImportLightmapMin = DatasmithImportLightmapMin.LIGHTMAP_16, max_lightmap_resolution: DatasmithImportLightmapMax = DatasmithImportLightmapMax.LIGHTMAP_64, generate_lightmap_u_vs: bool = False, remove_degenerates: bool = False) -> None
unreal.DatasmithStaticMeshImportOptions.generate_lightmap_u_vs(value: bool) -> None
unreal.DatasmithStaticMeshImportOptions.max_lightmap_resolution(value: DatasmithImportLightmapMax) -> None
unreal.DatasmithStaticMeshImportOptions.min_lightmap_resolution(value: DatasmithImportLightmapMin) -> None
unreal.DatasmithStaticMeshImportOptions.remove_degenerates(value: bool) -> None
```

## `unreal.DirectionalLightComponent(LightComponent)`

```python
unreal.DirectionalLightComponent.atmosphere_sun_disk_color_scale() -> LinearColor
unreal.DirectionalLightComponent.atmosphere_sun_light() -> bool
unreal.DirectionalLightComponent.atmosphere_sun_light_index() -> int
unreal.DirectionalLightComponent.cascade_distribution_exponent() -> float
unreal.DirectionalLightComponent.cascade_transition_fraction() -> float
unreal.DirectionalLightComponent.cast_cloud_shadows() -> bool
unreal.DirectionalLightComponent.cast_modulated_shadows() -> bool
unreal.DirectionalLightComponent.cast_shadows_on_atmosphere() -> bool
unreal.DirectionalLightComponent.cast_shadows_on_clouds() -> bool
unreal.DirectionalLightComponent.cloud_scattered_luminance_scale() -> LinearColor
unreal.DirectionalLightComponent.cloud_shadow_depth_bias() -> float
unreal.DirectionalLightComponent.cloud_shadow_extent() -> float
unreal.DirectionalLightComponent.cloud_shadow_map_resolution_scale() -> float
unreal.DirectionalLightComponent.cloud_shadow_on_atmosphere_strength() -> float
unreal.DirectionalLightComponent.cloud_shadow_on_surface_strength() -> float
unreal.DirectionalLightComponent.cloud_shadow_ray_sample_count_scale() -> float
unreal.DirectionalLightComponent.cloud_shadow_strength() -> float
unreal.DirectionalLightComponent.distance_field_shadow_distance() -> float
unreal.DirectionalLightComponent.dynamic_shadow_cascades() -> int
unreal.DirectionalLightComponent.dynamic_shadow_distance_movable_light() -> float
unreal.DirectionalLightComponent.dynamic_shadow_distance_stationary_light() -> float
unreal.DirectionalLightComponent.enable_light_shaft_occlusion() -> bool
unreal.DirectionalLightComponent.far_shadow_cascade_count() -> int
unreal.DirectionalLightComponent.far_shadow_distance() -> float
unreal.DirectionalLightComponent.forward_shading_priority() -> int
unreal.DirectionalLightComponent.light_shaft_override_direction() -> Vector
unreal.DirectionalLightComponent.light_source_angle() -> float
unreal.DirectionalLightComponent.light_source_soft_angle() -> float
unreal.DirectionalLightComponent.modulated_shadow_color() -> Color
unreal.DirectionalLightComponent.movable_whole_scene_dynamic_shadow_radius() -> float
unreal.DirectionalLightComponent.occlusion_depth_range() -> float
unreal.DirectionalLightComponent.occlusion_mask_darkness() -> float
unreal.DirectionalLightComponent.per_pixel_atmosphere_transmittance() -> bool
unreal.DirectionalLightComponent.set_atmosphere_sun_disk_color_scale(new_value: LinearColor) -> None
unreal.DirectionalLightComponent.set_atmosphere_sun_light(new_value: bool) -> None
unreal.DirectionalLightComponent.set_atmosphere_sun_light_index(new_value: int) -> None
unreal.DirectionalLightComponent.set_cascade_distribution_exponent(new_value: float) -> None
unreal.DirectionalLightComponent.set_cascade_transition_fraction(new_value: float) -> None
unreal.DirectionalLightComponent.set_dynamic_shadow_cascades(new_value: int) -> None
unreal.DirectionalLightComponent.set_dynamic_shadow_distance_movable_light(new_value: float) -> None
unreal.DirectionalLightComponent.set_dynamic_shadow_distance_stationary_light(new_value: float) -> None
unreal.DirectionalLightComponent.set_enable_light_shaft_occlusion(new_value: bool) -> None
unreal.DirectionalLightComponent.set_forward_shading_priority(new_value: int) -> None
unreal.DirectionalLightComponent.set_light_shaft_override_direction(new_value: Vector) -> None
unreal.DirectionalLightComponent.set_light_source_angle(new_value: float) -> None
unreal.DirectionalLightComponent.set_light_source_soft_angle(new_value: float) -> None
unreal.DirectionalLightComponent.set_occlusion_depth_range(new_value: float) -> None
unreal.DirectionalLightComponent.set_occlusion_mask_darkness(new_value: float) -> None
unreal.DirectionalLightComponent.set_shadow_amount(new_value: float) -> None
unreal.DirectionalLightComponent.set_shadow_cascade_bias_distribution(new_value: float) -> None
unreal.DirectionalLightComponent.set_shadow_distance_fadeout_fraction(new_value: float) -> None
unreal.DirectionalLightComponent.set_shadow_source_angle_factor(new_value: float) -> None
unreal.DirectionalLightComponent.shadow_amount() -> float
unreal.DirectionalLightComponent.shadow_cascade_bias_distribution() -> float
unreal.DirectionalLightComponent.shadow_distance_fadeout_fraction() -> float
unreal.DirectionalLightComponent.shadow_source_angle_factor() -> float
unreal.DirectionalLightComponent.stationary_whole_scene_dynamic_shadow_radius() -> float
unreal.DirectionalLightComponent.trace_distance() -> float
unreal.DirectionalLightComponent.use_inset_shadows_for_movable_objects() -> bool
```

## `unreal.DistanceFieldToTextureSettings(StructBase)`

```python
unreal.DistanceFieldToTextureSettings.__init__(scale: float = 0.000000, offset: float = 0.000000) -> None
unreal.DistanceFieldToTextureSettings.offset(value: float) -> None
unreal.DistanceFieldToTextureSettings.scale(value: float) -> None
```

## `unreal.DrawToRenderTargetContext(StructBase)`

```python
unreal.DrawToRenderTargetContext.__init__() -> None
```

## `unreal.EarthAnimatedTexture2D(Texture)`

```python
unreal.EarthAnimatedTexture2D.address_x(value: TextureAddress) -> None
unreal.EarthAnimatedTexture2D.address_y(value: TextureAddress) -> None
unreal.EarthAnimatedTexture2D.default_frame_delay(value: float) -> None
unreal.EarthAnimatedTexture2D.get_animation_length() -> float
unreal.EarthAnimatedTexture2D.get_play_rate() -> float
unreal.EarthAnimatedTexture2D.is_looping() -> bool
unreal.EarthAnimatedTexture2D.is_playing() -> bool
unreal.EarthAnimatedTexture2D.looping(value: bool) -> None
unreal.EarthAnimatedTexture2D.play() -> None
unreal.EarthAnimatedTexture2D.play_from_start() -> None
unreal.EarthAnimatedTexture2D.play_rate(value: float) -> None
unreal.EarthAnimatedTexture2D.set_looping(new_looping: bool) -> None
unreal.EarthAnimatedTexture2D.set_play_rate(new_rate: float) -> None
unreal.EarthAnimatedTexture2D.stop() -> None
unreal.EarthAnimatedTexture2D.supports_transparency(value: bool) -> None
```

## `unreal.EarthHierarchicalInstancedStaticMeshComponent(HierarchicalInstancedStaticMeshComponent)`

```python
unreal.EarthHierarchicalInstancedStaticMeshComponent.allow_create_physics_state(value: bool) -> None
unreal.EarthHierarchicalInstancedStaticMeshComponent.local_bounds(value: BoxSphereBounds) -> None
unreal.EarthHierarchicalInstancedStaticMeshComponent.set_bounds(bounds: BoxSphereBounds) -> None
```

## `unreal.EarthInstancedStaticMeshFragment(EarthOutputFragment)`

```python
unreal.EarthInstancedStaticMeshFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, static_mesh: StaticMesh = None, mesh_bounds_fragment: EarthBoundsFragment = [False, [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], False, False], component_class: Class = None, instance_transforms: Array[Matrix] = [], custom_data_attributes: Map[Name, float] = {}, per_instance_sm_custom_data: Array[float] = [], material_fragment: EarthMaterialFragment = [[], None, [], False, False], primitive_data_fragment: EarthPrimitiveDataFragment = [{}, False, False], bounds_fragment: EarthBoundsFragment = [False, [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], False, False], tag_fragment: EarthTagFragment = [[], False, False]) -> None
unreal.EarthInstancedStaticMeshFragment.bounds_fragment(value: EarthBoundsFragment) -> None
unreal.EarthInstancedStaticMeshFragment.component_class(value: Class) -> None
unreal.EarthInstancedStaticMeshFragment.custom_data_attributes(value: Map[Name, float]) -> None
unreal.EarthInstancedStaticMeshFragment.instance_transforms(value: Array[Matrix]) -> None
unreal.EarthInstancedStaticMeshFragment.material_fragment(value: EarthMaterialFragment) -> None
unreal.EarthInstancedStaticMeshFragment.mesh_bounds_fragment(value: EarthBoundsFragment) -> None
unreal.EarthInstancedStaticMeshFragment.per_instance_sm_custom_data(value: Array[float]) -> None
unreal.EarthInstancedStaticMeshFragment.primitive_data_fragment(value: EarthPrimitiveDataFragment) -> None
unreal.EarthInstancedStaticMeshFragment.static_mesh(value: StaticMesh) -> None
unreal.EarthInstancedStaticMeshFragment.tag_fragment(value: EarthTagFragment) -> None
```

## `unreal.EarthInstancedStaticMeshPrefab(EarthStaticMeshPrefab)`

```python
unreal.EarthInstancedStaticMeshPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthMaterialFragment(EarthPropertyFragment)`

```python
unreal.EarthMaterialFragment.__init__(validated: bool = False, valid: bool = False, override_materials: Array[MaterialInterface] = [], overlay_material: MaterialInterface = None, runtime_virtual_textures: Array[RuntimeVirtualTexture] = []) -> None
unreal.EarthMaterialFragment.overlay_material(value: MaterialInterface) -> None
unreal.EarthMaterialFragment.override_materials(value: Array[MaterialInterface]) -> None
unreal.EarthMaterialFragment.runtime_virtual_textures(value: Array[RuntimeVirtualTexture]) -> None
```

## `unreal.EarthMaterialInfo(StructBase)`

```python
unreal.EarthMaterialInfo.__init__(symbol: Name = "None", material: MaterialInterface = None, texture_index: int = 0, random_texture_index: bool = False, max_texture_index: int = 0, unit_uv_size: Vector2f = [0.000000, 0.000000], uv_rotation: float = 0.000000, uv_tile_precision: IntPoint = [0, 0]) -> None
unreal.EarthMaterialInfo.material(value: MaterialInterface) -> None
unreal.EarthMaterialInfo.max_texture_index(value: int) -> None
unreal.EarthMaterialInfo.random_texture_index(value: bool) -> None
unreal.EarthMaterialInfo.symbol(value: Name) -> None
unreal.EarthMaterialInfo.texture_index(value: int) -> None
unreal.EarthMaterialInfo.unit_uv_size(value: Vector2f) -> None
unreal.EarthMaterialInfo.uv_rotation(value: float) -> None
unreal.EarthMaterialInfo.uv_tile_precision(value: IntPoint) -> None
```

## `unreal.EarthPropertyItem_TextureArray(EarthPropertyItemWidget)`

```python
unreal.EarthPropertyItem_TextureArray.get_texture_items() -> Array[EarthPropertyTextureItemInfo]
unreal.EarthPropertyItem_TextureArray.set_texture_items(texture_items: Array[EarthPropertyTextureItemInfo]) -> None
```

## `unreal.EarthPropertyTextureItemInfo(StructBase)`

```python
unreal.EarthPropertyTextureItemInfo.__init__(display_name: str = "", value: str = "", texture: Texture2D = None) -> None
unreal.EarthPropertyTextureItemInfo.display_name(value: str) -> None
unreal.EarthPropertyTextureItemInfo.texture(value: Texture2D) -> None
unreal.EarthPropertyTextureItemInfo.value(value: str) -> None
```

## `unreal.EarthRenderTarget2DFragment(EarthOutputFragment)`

```python
unreal.EarthRenderTarget2DFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, render_target2d: TextureRenderTarget2D = None, water_color_presets: Array[EarthWaterColorPreset] = []) -> None
unreal.EarthRenderTarget2DFragment.render_target2d(value: TextureRenderTarget2D) -> None
unreal.EarthRenderTarget2DFragment.water_color_presets(value: Array[EarthWaterColorPreset]) -> None
```

## `unreal.EarthStaticMeshAssetFragment(EarthPropertyFragment)`

```python
unreal.EarthStaticMeshAssetFragment.__init__(validated: bool = False, valid: bool = False, static_mesh: StaticMesh = None) -> None
unreal.EarthStaticMeshAssetFragment.static_mesh(value: StaticMesh) -> None
```

## `unreal.EarthStaticMeshFragment(EarthOutputFragment)`

```python
unreal.EarthStaticMeshFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, static_mesh: StaticMesh = None, component_class: Class = None, lod_feature_buffer: Array[EarthFeatureBuffer] = [], material_fragment: EarthMaterialFragment = [[], None, [], False, False], primitive_data_fragment: EarthPrimitiveDataFragment = [{}, False, False], bounds_fragment: EarthBoundsFragment = [False, [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], False, False], tag_fragment: EarthTagFragment = [[], False, False]) -> None
unreal.EarthStaticMeshFragment.bounds_fragment(value: EarthBoundsFragment) -> None
unreal.EarthStaticMeshFragment.component_class(value: Class) -> None
unreal.EarthStaticMeshFragment.lod_feature_buffer() -> Array[EarthFeatureBuffer]
unreal.EarthStaticMeshFragment.material_fragment(value: EarthMaterialFragment) -> None
unreal.EarthStaticMeshFragment.primitive_data_fragment(value: EarthPrimitiveDataFragment) -> None
unreal.EarthStaticMeshFragment.static_mesh(value: StaticMesh) -> None
unreal.EarthStaticMeshFragment.tag_fragment(value: EarthTagFragment) -> None
```

## `unreal.EarthStaticMeshPrefab(EarthPrefabBase)`

```python
unreal.EarthStaticMeshPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthTextureIndexFragment(EarthPropertyFragment)`

```python
unreal.EarthTextureIndexFragment.__init__(validated: bool = False, valid: bool = False, texture_index: int = 0) -> None
unreal.EarthTextureIndexFragment.texture_index(value: int) -> None
```

## `unreal.EarthTextureOverlayer(EarthPrefabActor)`

```python
unreal.EarthTextureOverlayer.box_component(value: EarthBoxComponent) -> None
```

## `unreal.EarthTextureOverlayerFragment(EarthOutputFragment)`

```python
unreal.EarthTextureOverlayerFragment.__init__(validated: bool = False, valid: bool = False, owned_object: Object = None, top_level: int = 0, texture: Texture = None, sampler_type: EarthOverlayerSamplerType = EarthOverlayerSamplerType.BILINEAR, blend_type: EarthOverlayerBlendType = EarthOverlayerBlendType.REPLACE, alpha_strength: float = 0.000000, use_alpha_channel: bool = False, alpha_texture: Texture = None, sort_order: int = 0, producer_name: Name = "None", invalidate_producer_names: Array[Name] = [], feature_id: EarthFeatureIDFragment = [0, 0, False, False], earth_actor: Actor = None, bottom_left: Vector2D = [0.000000, 0.000000], top_right: Vector2D = [0.000000, 0.000000], rotation: float = 0.000000, tiles: Set[str] = []) -> None
unreal.EarthTextureOverlayerFragment.alpha_strength(value: float) -> None
unreal.EarthTextureOverlayerFragment.alpha_texture(value: Texture) -> None
unreal.EarthTextureOverlayerFragment.blend_type(value: EarthOverlayerBlendType) -> None
unreal.EarthTextureOverlayerFragment.bottom_left(value: Vector2D) -> None
unreal.EarthTextureOverlayerFragment.earth_actor(value: Actor) -> None
unreal.EarthTextureOverlayerFragment.feature_id(value: EarthFeatureIDFragment) -> None
unreal.EarthTextureOverlayerFragment.invalidate_producer_names() -> Array[Name]
unreal.EarthTextureOverlayerFragment.producer_name() -> Name
unreal.EarthTextureOverlayerFragment.rotation(value: float) -> None
unreal.EarthTextureOverlayerFragment.sampler_type(value: EarthOverlayerSamplerType) -> None
unreal.EarthTextureOverlayerFragment.sort_order(value: int) -> None
unreal.EarthTextureOverlayerFragment.texture(value: Texture) -> None
unreal.EarthTextureOverlayerFragment.tiles(value: Set[str]) -> None
unreal.EarthTextureOverlayerFragment.top_level(value: int) -> None
unreal.EarthTextureOverlayerFragment.top_right(value: Vector2D) -> None
unreal.EarthTextureOverlayerFragment.use_alpha_channel(value: bool) -> None
```

## `unreal.EarthTextureOverlayerPrefab(EarthPrefabBase)`

```python
unreal.EarthTextureOverlayerPrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthTextureOverlayerSettings(StructBase)`

```python
unreal.EarthTextureOverlayerSettings.__init__() -> None
```

## `unreal.EditorSkeletalMeshLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorSkeletalMeshLibrary.create_physics_asset(skeletal_mesh: SkeletalMesh) -> PhysicsAsset
unreal.EditorSkeletalMeshLibrary.get_lod_build_settings(skeletal_mesh: SkeletalMesh, lod_index: int) -> SkeletalMeshBuildSettings
unreal.EditorSkeletalMeshLibrary.get_lod_count(skeletal_mesh: SkeletalMesh) -> int
unreal.EditorSkeletalMeshLibrary.get_num_verts(skeletal_mesh: SkeletalMesh, lod_index: int) -> int
unreal.EditorSkeletalMeshLibrary.import_lod(base_mesh: SkeletalMesh, lod_index: int, source_filename: str) -> int
unreal.EditorSkeletalMeshLibrary.regenerate_lod(skeletal_mesh: SkeletalMesh, new_lod_count: int = 0, regenerate_even_if_imported: bool = False, generate_base_lod: bool = False) -> bool
unreal.EditorSkeletalMeshLibrary.reimport_all_custom_lo_ds(skeletal_mesh: SkeletalMesh) -> bool
unreal.EditorSkeletalMeshLibrary.remove_lo_ds(skeletal_mesh: SkeletalMesh, to_remove_lo_ds: Array[int]) -> bool
unreal.EditorSkeletalMeshLibrary.rename_socket(skeletal_mesh: SkeletalMesh, old_name: Name, new_name: Name) -> bool
unreal.EditorSkeletalMeshLibrary.set_lod_build_settings(skeletal_mesh: SkeletalMesh, lod_index: int, build_options: SkeletalMeshBuildSettings) -> None
unreal.EditorSkeletalMeshLibrary.strip_lod_geometry(skeletal_mesh: SkeletalMesh, lod_index: int, texture_mask: Texture2D, threshold: float) -> bool
```

## `unreal.EditorStaticMeshLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorStaticMeshLibrary.add_simple_collisions(static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType) -> int
unreal.EditorStaticMeshLibrary.add_simple_collisions_with_notification(static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType, apply_changes: bool) -> int
unreal.EditorStaticMeshLibrary.add_uv_channel(static_mesh: StaticMesh, lod_index: int) -> bool
unreal.EditorStaticMeshLibrary.bulk_set_convex_decomposition_collisions(static_meshes: Array[StaticMesh], hull_count: int, max_hull_verts: int, hull_precision: int) -> bool
unreal.EditorStaticMeshLibrary.bulk_set_convex_decomposition_collisions_with_notification(static_meshes: Array[StaticMesh], hull_count: int, max_hull_verts: int, hull_precision: int, apply_changes: bool) -> bool
unreal.EditorStaticMeshLibrary.enable_section_cast_shadow(static_mesh: StaticMesh, cast_shadow: bool, lod_index: int, section_index: int) -> None
unreal.EditorStaticMeshLibrary.enable_section_collision(static_mesh: StaticMesh, collision_enabled: bool, lod_index: int, section_index: int) -> None
unreal.EditorStaticMeshLibrary.generate_box_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, size: Vector) -> bool
unreal.EditorStaticMeshLibrary.generate_cylindrical_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, tiling: Vector2D) -> bool
unreal.EditorStaticMeshLibrary.generate_planar_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int, position: Vector, orientation: Rotator, tiling: Vector2D) -> bool
unreal.EditorStaticMeshLibrary.get_collision_complexity(static_mesh: StaticMesh) -> CollisionTraceFlag
unreal.EditorStaticMeshLibrary.get_convex_collision_count(static_mesh: StaticMesh) -> int
unreal.EditorStaticMeshLibrary.get_lod_build_settings(static_mesh: StaticMesh, lod_index: int) -> MeshBuildSettings
unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh: StaticMesh) -> int
unreal.EditorStaticMeshLibrary.get_lod_reduction_settings(static_mesh: StaticMesh, lod_index: int) -> MeshReductionSettings
unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(static_mesh: StaticMesh) -> Array[float]
unreal.EditorStaticMeshLibrary.get_num_uv_channels(static_mesh: StaticMesh, lod_index: int) -> int
unreal.EditorStaticMeshLibrary.get_number_materials(static_mesh: StaticMesh) -> int
unreal.EditorStaticMeshLibrary.get_number_verts(static_mesh: StaticMesh, lod_index: int) -> int
unreal.EditorStaticMeshLibrary.get_simple_collision_count(static_mesh: StaticMesh) -> int
unreal.EditorStaticMeshLibrary.has_instance_vertex_colors(static_mesh_component: StaticMeshComponent) -> bool
unreal.EditorStaticMeshLibrary.has_vertex_colors(static_mesh: StaticMesh) -> bool
unreal.EditorStaticMeshLibrary.import_lod(base_static_mesh: StaticMesh, lod_index: int, source_filename: str) -> int
unreal.EditorStaticMeshLibrary.insert_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int) -> bool
unreal.EditorStaticMeshLibrary.is_section_collision_enabled(static_mesh: StaticMesh, lod_index: int, section_index: int) -> bool
unreal.EditorStaticMeshLibrary.reimport_all_custom_lo_ds(static_mesh: StaticMesh) -> bool
unreal.EditorStaticMeshLibrary.remove_collisions(static_mesh: StaticMesh) -> bool
unreal.EditorStaticMeshLibrary.remove_collisions_with_notification(static_mesh: StaticMesh, apply_changes: bool) -> bool
unreal.EditorStaticMeshLibrary.remove_lods(static_mesh: StaticMesh) -> bool
unreal.EditorStaticMeshLibrary.remove_uv_channel(static_mesh: StaticMesh, lod_index: int, uv_channel_index: int) -> bool
unreal.EditorStaticMeshLibrary.set_allow_cpu_access(static_mesh: StaticMesh, allow_cpu_access: bool) -> None
unreal.EditorStaticMeshLibrary.set_convex_decomposition_collisions(static_mesh: StaticMesh, hull_count: int, max_hull_verts: int, hull_precision: int) -> bool
unreal.EditorStaticMeshLibrary.set_convex_decomposition_collisions_with_notification(static_mesh: StaticMesh, hull_count: int, max_hull_verts: int, hull_precision: int, apply_changes: bool) -> bool
unreal.EditorStaticMeshLibrary.set_generate_lightmap_uv(static_mesh: StaticMesh, generate_lightmap_u_vs: bool) -> bool
unreal.EditorStaticMeshLibrary.set_lod_build_settings(static_mesh: StaticMesh, lod_index: int, build_options: MeshBuildSettings) -> None
unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(destination_static_mesh: StaticMesh, destination_lod_index: int, source_static_mesh: StaticMesh, source_lod_index: int, reuse_existing_material_slots: bool) -> int
unreal.EditorStaticMeshLibrary.set_lod_reduction_settings(static_mesh: StaticMesh, lod_index: int, reduction_options: MeshReductionSettings) -> None
unreal.EditorStaticMeshLibrary.set_lods(static_mesh: StaticMesh, reduction_options: StaticMeshReductionOptions) -> int
unreal.EditorStaticMeshLibrary.set_lods_with_notification(static_mesh: StaticMesh, reduction_options: StaticMeshReductionOptions, apply_changes: bool) -> int
```

## `unreal.EditorUserSceneTextureOverride(StructBase)`

```python
unreal.EditorUserSceneTextureOverride.__init__() -> None
```

## `unreal.EntityMaterialSlot(StructBase)`

```python
unreal.EntityMaterialSlot.__init__(mesh_name: Name = "None", material_index: Array[int] = []) -> None
unreal.EntityMaterialSlot.material_index(value: Array[int]) -> None
unreal.EntityMaterialSlot.mesh_name(value: Name) -> None
```

## `unreal.EntityMaterialSlots(StructBase)`

```python
unreal.EntityMaterialSlots.__init__(entity_material_slots: Array[EntityMaterialSlot] = []) -> None
unreal.EntityMaterialSlots.entity_material_slots(value: Array[EntityMaterialSlot]) -> None
```

## `unreal.FbxMaterialBakeSize(StructBase)`

```python
unreal.FbxMaterialBakeSize.__init__(size: IntPoint = [0, 0], auto_detect: bool = False) -> None
unreal.FbxMaterialBakeSize.auto_detect(value: bool) -> None
unreal.FbxMaterialBakeSize.size(value: IntPoint) -> None
```

## `unreal.FbxSkeletalMeshImportData(FbxMeshImportData)`

```python
unreal.FbxSkeletalMeshImportData.vertex_color_import_option(value: VertexColorImportOption) -> None
unreal.FbxSkeletalMeshImportData.vertex_override_color(value: Color) -> None
```

## `unreal.FbxStaticMeshImportData(FbxMeshImportData)`

```python
unreal.FbxStaticMeshImportData.auto_generate_collision(value: bool) -> None
unreal.FbxStaticMeshImportData.build_nanite(value: bool) -> None
unreal.FbxStaticMeshImportData.build_reversed_index_buffer(value: bool) -> None
unreal.FbxStaticMeshImportData.combine_meshes(value: bool) -> None
unreal.FbxStaticMeshImportData.distance_field_resolution_scale(value: float) -> None
unreal.FbxStaticMeshImportData.generate_lightmap_u_vs(value: bool) -> None
unreal.FbxStaticMeshImportData.one_convex_hull_per_ucx(value: bool) -> None
unreal.FbxStaticMeshImportData.remove_degenerates(value: bool) -> None
unreal.FbxStaticMeshImportData.static_mesh_lod_group(value: Name) -> None
unreal.FbxStaticMeshImportData.vertex_color_import_option(value: VertexColorImportOption) -> None
unreal.FbxStaticMeshImportData.vertex_override_color(value: Color) -> None
```

## `unreal.FbxTextureImportData(FbxAssetImportData)`

```python
unreal.FbxTextureImportData.base_color_name(value: str) -> None
unreal.FbxTextureImportData.base_diffuse_texture_name(value: str) -> None
unreal.FbxTextureImportData.base_emissive_color_name(value: str) -> None
unreal.FbxTextureImportData.base_emmisive_texture_name(value: str) -> None
unreal.FbxTextureImportData.base_material_name(value: SoftObjectPath) -> None
unreal.FbxTextureImportData.base_normal_texture_name(value: str) -> None
unreal.FbxTextureImportData.base_opacity_texture_name(value: str) -> None
unreal.FbxTextureImportData.base_specular_texture_name(value: str) -> None
unreal.FbxTextureImportData.invert_normal_maps(value: bool) -> None
unreal.FbxTextureImportData.material_search_location(value: MaterialSearchLocation) -> None
```

## `unreal.FeatureTextureDescription(StructBase)`

```python
unreal.FeatureTextureDescription.__init__() -> None
```

## `unreal.FeatureTexturePropertyDescription(StructBase)`

```python
unreal.FeatureTexturePropertyDescription.__init__() -> None
```

## `unreal.FoliageInstancedStaticMeshComponent(HierarchicalInstancedStaticMeshComponent)`

```python
unreal.FoliageInstancedStaticMeshComponent.on_instance_take_point_damage(value: InstancePointDamageSignature) -> None
unreal.FoliageInstancedStaticMeshComponent.on_instance_take_radial_damage(value: InstanceRadialDamageSignature) -> None
```

## `unreal.FoliageType_InstancedStaticMesh(FoliageType)`

```python
unreal.FoliageType_InstancedStaticMesh.mesh(value: StaticMesh) -> None
unreal.FoliageType_InstancedStaticMesh.nanite_override_materials(value: Array[MaterialInterface]) -> None
unreal.FoliageType_InstancedStaticMesh.override_materials(value: Array[MaterialInterface]) -> None
```

## `unreal.FontRenderInfo(StructBase)`

```python
unreal.FontRenderInfo.__init__(clip_text: bool = False, enable_shadow: bool = False, glow_info: DepthFieldGlowInfo = [False, [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000]]) -> None
unreal.FontRenderInfo.clip_text(value: bool) -> None
unreal.FontRenderInfo.enable_shadow(value: bool) -> None
unreal.FontRenderInfo.glow_info(value: DepthFieldGlowInfo) -> None
```

## `unreal.GLTFMaterialBakeSize(StructBase)`

```python
unreal.GLTFMaterialBakeSize.__init__(x: int = 0, y: int = 0, auto_detect: bool = False) -> None
unreal.GLTFMaterialBakeSize.auto_detect(value: bool) -> None
unreal.GLTFMaterialBakeSize.x(value: int) -> None
unreal.GLTFMaterialBakeSize.y(value: int) -> None
```

## `unreal.GLTFMaterialExportOptions(AssetUserData)`

```python
unreal.GLTFMaterialExportOptions.default(value: GLTFOverrideMaterialBakeSettings) -> None
unreal.GLTFMaterialExportOptions.inputs(value: Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]) -> None
unreal.GLTFMaterialExportOptions.proxy(value: MaterialInterface) -> None
```

## `unreal.GLTFOverrideMaterialBakeSettings(StructBase)`

```python
unreal.GLTFOverrideMaterialBakeSettings.__init__(override_size: bool = False, size: GLTFMaterialBakeSize = [1, 1, False], override_filter: bool = False, filter: TextureFilter = TextureFilter.TF_NEAREST, override_tiling: bool = False, tiling: TextureAddress = TextureAddress.TA_WRAP) -> None
unreal.GLTFOverrideMaterialBakeSettings.filter(value: TextureFilter) -> None
unreal.GLTFOverrideMaterialBakeSettings.override_filter(value: bool) -> None
unreal.GLTFOverrideMaterialBakeSettings.override_size(value: bool) -> None
unreal.GLTFOverrideMaterialBakeSettings.override_tiling(value: bool) -> None
unreal.GLTFOverrideMaterialBakeSettings.size(value: GLTFMaterialBakeSize) -> None
unreal.GLTFOverrideMaterialBakeSettings.tiling(value: TextureAddress) -> None
```

## `unreal.GenerateStaticMeshLODProcessSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcessSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_CollisionSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_CollisionSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_NormalsSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_NormalsSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_PreprocessSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_PreprocessSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_SimplifySettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_SimplifySettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_TextureSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_TextureSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_UVSettings(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_UVSettings.__init__() -> None
```

## `unreal.GenerateStaticMeshLODProcess_UVSettings_PatchBuilder(StructBase)`

```python
unreal.GenerateStaticMeshLODProcess_UVSettings_PatchBuilder.__init__() -> None
```

## `unreal.GeometryScriptBakeRenderCaptureOptions(StructBase)`

```python
unreal.GeometryScriptBakeRenderCaptureOptions.__init__(cameras: Array[GeometryScriptRenderCaptureCamera] = [], render_capture_resolution: GeometryScriptBakeResolution = GeometryScriptBakeResolution.RESOLUTION16, resolution: GeometryScriptBakeResolution = GeometryScriptBakeResolution.RESOLUTION16, samples_per_pixel: GeometryScriptBakeSamplesPerPixel = GeometryScriptBakeSamplesPerPixel.SAMPLE1, render_capture_anti_aliasing: bool = False, cleanup_tolerance: float = 0.000000, base_color_map: bool = False, normal_map: bool = False, packed_mrs_map: bool = False, metallic_map: bool = False, roughness_map: bool = False, specular_map: bool = False, emissive_map: bool = False, opacity_map: bool = False, subsurface_color_map: bool = False) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.base_color_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.cameras(value: Array[GeometryScriptRenderCaptureCamera]) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.cleanup_tolerance(value: float) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.emissive_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.metallic_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.normal_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.opacity_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.packed_mrs_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.render_capture_anti_aliasing(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.render_capture_resolution(value: GeometryScriptBakeResolution) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.resolution(value: GeometryScriptBakeResolution) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.roughness_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.samples_per_pixel(value: GeometryScriptBakeSamplesPerPixel) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.specular_map(value: bool) -> None
unreal.GeometryScriptBakeRenderCaptureOptions.subsurface_color_map(value: bool) -> None
```

## `unreal.GeometryScriptBakeTextureOptions(StructBase)`

```python
unreal.GeometryScriptBakeTextureOptions.__init__(resolution: GeometryScriptBakeResolution = GeometryScriptBakeResolution.RESOLUTION16, bit_depth: GeometryScriptBakeBitDepth = GeometryScriptBakeBitDepth.CHANNEL_BITS8, samples_per_pixel: GeometryScriptBakeSamplesPerPixel = GeometryScriptBakeSamplesPerPixel.SAMPLE1, sample_filter_mask: Texture2D = None, filtering_type: GeometryScriptBakeFilteringType = GeometryScriptBakeFilteringType.B_SPLINE, projection_distance: float = 0.000000, projection_in_world_space: bool = False) -> None
unreal.GeometryScriptBakeTextureOptions.bit_depth(value: GeometryScriptBakeBitDepth) -> None
unreal.GeometryScriptBakeTextureOptions.filtering_type(value: GeometryScriptBakeFilteringType) -> None
unreal.GeometryScriptBakeTextureOptions.projection_distance(value: float) -> None
unreal.GeometryScriptBakeTextureOptions.projection_in_world_space(value: bool) -> None
unreal.GeometryScriptBakeTextureOptions.resolution(value: GeometryScriptBakeResolution) -> None
unreal.GeometryScriptBakeTextureOptions.sample_filter_mask(value: Texture2D) -> None
unreal.GeometryScriptBakeTextureOptions.samples_per_pixel(value: GeometryScriptBakeSamplesPerPixel) -> None
```

## `unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions(StructBase)`

```python
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.__init__(enable_recompute_normals: bool = False, enable_recompute_tangents: bool = False, materials: Map[Name, MaterialInterface] = {}, use_mesh_bone_proportions: bool = False, use_original_vertex_order: bool = False) -> None
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_normals(value: bool) -> None
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.enable_recompute_tangents(value: bool) -> None
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.materials(value: Map[Name, MaterialInterface]) -> None
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_mesh_bone_proportions(value: bool) -> None
unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions.use_original_vertex_order(value: bool) -> None
```

## `unreal.GeometryScriptCreateNewStaticMeshAssetOptions(StructBase)`

```python
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.__init__(enable_recompute_normals: bool = False, enable_recompute_tangents: bool = False, enable_nanite: bool = False, nanite_settings: MeshNaniteSettings = [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0], nanite_proxy_triangle_percent: float = 0.000000, enable_collision: bool = False, collision_mode: CollisionTraceFlag = CollisionTraceFlag.CTF_USE_DEFAULT, use_original_vertex_order: bool = False) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.collision_mode(value: CollisionTraceFlag) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_collision(value: bool) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_nanite(value: bool) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_normals(value: bool) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_tangents(value: bool) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_proxy_triangle_percent(value: float) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_settings(value: MeshNaniteSettings) -> None
unreal.GeometryScriptCreateNewStaticMeshAssetOptions.use_original_vertex_order(value: bool) -> None
```

## `unreal.GeometryScriptCreateNewTexture2DAssetOptions(StructBase)`

```python
unreal.GeometryScriptCreateNewTexture2DAssetOptions.__init__(overwrite_if_exists: bool = False) -> None
unreal.GeometryScriptCreateNewTexture2DAssetOptions.overwrite_if_exists(value: bool) -> None
```

## `unreal.GeometryScriptDisplaceFromTextureOptions(StructBase)`

```python
unreal.GeometryScriptDisplaceFromTextureOptions.__init__(magnitude: float = 0.000000, uv_scale: Vector2D = [0.000000, 0.000000], uv_offset: Vector2D = [0.000000, 0.000000], center: float = 0.000000, image_channel: int = 0, empty_behavior: GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior.FULL_MESH_SELECTION) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.center(value: float) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.image_channel(value: int) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.magnitude(value: float) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.uv_offset(value: Vector2D) -> None
unreal.GeometryScriptDisplaceFromTextureOptions.uv_scale(value: Vector2D) -> None
```

## `unreal.GeometryScriptNaniteOptions(StructBase)`

```python
unreal.GeometryScriptNaniteOptions.__init__(enabled: bool = False, fallback_percent_triangles: float = 0.000000, fallback_relative_error: float = 0.000000) -> None
unreal.GeometryScriptNaniteOptions.enabled(value: bool) -> None
unreal.GeometryScriptNaniteOptions.fallback_percent_triangles(value: float) -> None
unreal.GeometryScriptNaniteOptions.fallback_relative_error(value: float) -> None
```

## `unreal.GeometryScriptRenderCaptureCamera(StructBase)`

```python
unreal.GeometryScriptRenderCaptureCamera.__init__(resolution: int = 0, field_of_view_degrees: float = 0.000000, view_position: Vector = [0.000000, 0.000000, 0.000000], view_direction: Vector = [0.000000, 0.000000, 0.000000], near_plane_dist: float = 0.000000) -> None
unreal.GeometryScriptRenderCaptureCamera.field_of_view_degrees(value: float) -> None
unreal.GeometryScriptRenderCaptureCamera.near_plane_dist(value: float) -> None
unreal.GeometryScriptRenderCaptureCamera.resolution(value: int) -> None
unreal.GeometryScriptRenderCaptureCamera.view_direction(value: Vector) -> None
unreal.GeometryScriptRenderCaptureCamera.view_position(value: Vector) -> None
```

## `unreal.GeometryScriptRenderCaptureCamerasForBoxOptions(StructBase)`

```python
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.__init__(resolution: int = 0, field_of_view_degrees: float = 0.000000, view_from_box_faces: bool = False, view_from_upper_corners: bool = False, view_from_lower_corners: bool = False, view_from_upper_edges: bool = False, view_from_lower_edges: bool = False, view_from_side_edges: bool = False, extra_view_from_positions: Array[Vector] = []) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.extra_view_from_positions(value: Array[Vector]) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.field_of_view_degrees(value: float) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.resolution(value: int) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_box_faces(value: bool) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_corners(value: bool) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_edges(value: bool) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_side_edges(value: bool) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_corners(value: bool) -> None
unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_edges(value: bool) -> None
```

## `unreal.GeometryScriptRenderCaptureTextures(StructBase)`

```python
unreal.GeometryScriptRenderCaptureTextures.__init__(base_color_map: Texture2D = None, has_base_color_map: bool = False, normal_map: Texture2D = None, has_normal_map: bool = False, packed_mrs_map: Texture2D = None, has_packed_mrs_map: bool = False, metallic_map: Texture2D = None, has_metallic_map: bool = False, roughness_map: Texture2D = None, has_roughness_map: bool = False, specular_map: Texture2D = None, has_specular_map: bool = False, emissive_map: Texture2D = None, has_emissive_map: bool = False, opacity_map: Texture2D = None, has_opacity_map: bool = False, subsurface_color_map: Texture2D = None, has_subsurface_color_map: bool = False) -> None
unreal.GeometryScriptRenderCaptureTextures.base_color_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.emissive_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.has_base_color_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_emissive_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_metallic_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_normal_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_opacity_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_packed_mrs_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_roughness_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_specular_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.has_subsurface_color_map(value: bool) -> None
unreal.GeometryScriptRenderCaptureTextures.metallic_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.normal_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.opacity_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.packed_mrs_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.roughness_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.specular_map(value: Texture2D) -> None
unreal.GeometryScriptRenderCaptureTextures.subsurface_color_map(value: Texture2D) -> None
```

## `unreal.GeometryScriptSampleTextureOptions(StructBase)`

```python
unreal.GeometryScriptSampleTextureOptions.__init__(sampling_method: GeometryScriptPixelSamplingMethod = GeometryScriptPixelSamplingMethod.BILINEAR, wrap: bool = False, uv_scale: Vector2D = [0.000000, 0.000000], uv_offset: Vector2D = [0.000000, 0.000000]) -> None
unreal.GeometryScriptSampleTextureOptions.sampling_method(value: GeometryScriptPixelSamplingMethod) -> None
unreal.GeometryScriptSampleTextureOptions.uv_offset(value: Vector2D) -> None
unreal.GeometryScriptSampleTextureOptions.uv_scale(value: Vector2D) -> None
unreal.GeometryScriptSampleTextureOptions.wrap(value: bool) -> None
```

## `unreal.GeometryScriptSetStaticMeshCollisionOptions(StructBase)`

```python
unreal.GeometryScriptSetStaticMeshCollisionOptions.__init__(mark_as_customized: bool = False) -> None
unreal.GeometryScriptSetStaticMeshCollisionOptions.mark_as_customized(value: bool) -> None
```

## `unreal.GeometryScript_EditorTextureUtils(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_EditorTextureUtils.channel_pack(r_channel_source: GeometryScriptChannelPackSource, g_channel_source: GeometryScriptChannelPackSource, b_channel_source: GeometryScriptChannelPackSource, a_channel_source: GeometryScriptChannelPackSource, output_srgb: bool, debug: GeometryScriptDebug = None) -> GeometryScriptChannelPackResult
```

## `unreal.GeometryScript_Materials(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Materials.clear_material_i_ds(target_mesh: DynamicMesh, clear_value: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.compact_material_i_ds(target_mesh: DynamicMesh, source_material_list: Array[MaterialInterface], remove_duplicate_materials: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[MaterialInterface]]
unreal.GeometryScript_Materials.delete_triangles_by_material_id(target_mesh: DynamicMesh, material_id: int, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_Materials.enable_material_i_ds(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.get_all_triangle_material_i_ds(target_mesh: DynamicMesh) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
unreal.GeometryScript_Materials.get_material_i_ds_of_triangles(target_mesh: DynamicMesh, triangle_id_list: GeometryScriptIndexList, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_Materials.get_max_material_id(target_mesh: DynamicMesh) -> Tuple[int, bool]
unreal.GeometryScript_Materials.get_triangle_material_id(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[int, bool]
unreal.GeometryScript_Materials.get_triangles_by_material_id(target_mesh: DynamicMesh, material_id: int, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_Materials.remap_and_combine_materials(target_mesh: DynamicMesh, target_mesh_materials: Array[MaterialInterface], required_materials: Array[MaterialInterface], remap_invalid_material_id: int = -1, compact_duplicate_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[MaterialInterface]]
unreal.GeometryScript_Materials.remap_material_i_ds(target_mesh: DynamicMesh, from_material_id: int, to_material_id: int, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.remap_to_new_material_i_ds_by_material(target_mesh: DynamicMesh, from_material_list: Array[MaterialInterface], to_material_list: Array[MaterialInterface], missing_material_id: int = -1, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.set_all_triangle_material_i_ds(target_mesh: DynamicMesh, triangle_material_id_list: GeometryScriptIndexList, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.set_material_id_for_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, material_id: int, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.set_material_id_on_triangles(target_mesh: DynamicMesh, triangle_id_list: GeometryScriptIndexList, material_id: int, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Materials.set_polygroup_material_id(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_id: int, material_id: int, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_Materials.set_triangle_material_id(target_mesh: DynamicMesh, triangle_id: int, material_id: int, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

## `unreal.GeometryScript_TextureUtils(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_TextureUtils.sample_texture2d_at_uv_positions(uv_list: GeometryScriptUVList, texture: Texture2D, sample_options: GeometryScriptSampleTextureOptions, debug: GeometryScriptDebug = None) -> GeometryScriptColorList
unreal.GeometryScript_TextureUtils.sample_texture_render_target2d_at_uv_positions(uv_list: GeometryScriptUVList, texture: TextureRenderTarget2D, sample_options: GeometryScriptSampleTextureOptions, debug: GeometryScriptDebug = None) -> GeometryScriptColorList
```

## `unreal.GetEntityMaterialSlotsResult(ResultBase)`

```python
unreal.GetEntityMaterialSlotsResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, eid_to_material_slots: Map[int, EntityMaterialSlots] = {}) -> None
unreal.GetEntityMaterialSlotsResult.eid_to_material_slots(value: Map[int, EntityMaterialSlots]) -> None
```

## `unreal.GetHighlightAreaParams(ResultBase)`

```python
unreal.GetHighlightAreaParams.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, polygon_entity_eid: str = "", highlight_area_style: HighlightAreaStyle = ["ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000]) -> None
unreal.GetHighlightAreaParams.highlight_area_style(value: HighlightAreaStyle) -> None
unreal.GetHighlightAreaParams.polygon_entity_eid(value: str) -> None
```

## `unreal.GetHighlightTextDelegate(DelegateBase)`

```python
unreal.GetHighlightTextDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.GroomCreateStrandsTexturesOptions(Object)`

```python
unreal.GroomCreateStrandsTexturesOptions.dilation(value: int) -> None
unreal.GroomCreateStrandsTexturesOptions.group_index(value: Array[int]) -> None
unreal.GroomCreateStrandsTexturesOptions.layout(value: HairTextureLayout) -> None
unreal.GroomCreateStrandsTexturesOptions.lod_index(value: int) -> None
unreal.GroomCreateStrandsTexturesOptions.mesh_type(value: StrandsTexturesMeshType) -> None
unreal.GroomCreateStrandsTexturesOptions.resolution(value: int) -> None
unreal.GroomCreateStrandsTexturesOptions.section_index(value: int) -> None
unreal.GroomCreateStrandsTexturesOptions.skeletal_mesh(value: SkeletalMesh) -> None
unreal.GroomCreateStrandsTexturesOptions.static_mesh(value: StaticMesh) -> None
unreal.GroomCreateStrandsTexturesOptions.trace_distance(value: float) -> None
unreal.GroomCreateStrandsTexturesOptions.trace_type(value: StrandsTexturesTraceType) -> None
unreal.GroomCreateStrandsTexturesOptions.uv_channel_index(value: int) -> None
```

## `unreal.HairAdvancedRenderingSettings(StructBase)`

```python
unreal.HairAdvancedRenderingSettings.__init__(use_stable_rasterization: bool = False, scatter_scene_lighting: bool = False) -> None
unreal.HairAdvancedRenderingSettings.scatter_scene_lighting() -> bool
unreal.HairAdvancedRenderingSettings.use_stable_rasterization() -> bool
```

## `unreal.HairGroupCardsTextures(StructBase)`

```python
unreal.HairGroupCardsTextures.__init__() -> None
```

## `unreal.HairGroupsMaterial(StructBase)`

```python
unreal.HairGroupsMaterial.__init__() -> None
```

## `unreal.HairGroupsRendering(StructBase)`

```python
unreal.HairGroupsRendering.__init__() -> None
```

## `unreal.HairMaterialConstraints(StructBase)`

```python
unreal.HairMaterialConstraints.__init__() -> None
```

## `unreal.HierarchyMeshHighlightStyle(StructBase)`

```python
unreal.HierarchyMeshHighlightStyle.__init__() -> None
```

## `unreal.HighlightAreaEntity(UniqueEntityBase)`

```python
unreal.HighlightAreaEntity.do_create_highlight_area(highlight_area_exterior_atom: HighlightAreaEntityAtom) -> bool
unreal.HighlightAreaEntity.set_coord_z(new_coord_z: float) -> bool
unreal.HighlightAreaEntity.set_exterior_brightness(new_value: float) -> bool
unreal.HighlightAreaEntity.set_exterior_color(new_color: str) -> bool
unreal.HighlightAreaEntity.set_exterior_contrast(new_value: float) -> bool
unreal.HighlightAreaEntity.set_exterior_outline_color(new_color: str) -> bool
unreal.HighlightAreaEntity.set_exterior_saturation(new_value: float) -> bool
unreal.HighlightAreaEntity.set_interior_color(new_colors: Array[str]) -> bool
unreal.HighlightAreaEntity.set_polygon(positions: Array[HighlightAreaPosition], new_colors: Array[str]) -> bool
```

## `unreal.HighlightAreaEntityAtom(EntityAtomBase)`

```python
unreal.HighlightAreaEntityAtom.custom_colors(value: Map[int, str]) -> None
unreal.HighlightAreaEntityAtom.exterior_brightness(value: float) -> None
unreal.HighlightAreaEntityAtom.exterior_color(value: str) -> None
unreal.HighlightAreaEntityAtom.exterior_contrast(value: float) -> None
unreal.HighlightAreaEntityAtom.exterior_outline_color(value: str) -> None
unreal.HighlightAreaEntityAtom.exterior_saturation(value: float) -> None
unreal.HighlightAreaEntityAtom.interior_color(value: str) -> None
```

## `unreal.HighlightAreaPosition(StructBase)`

```python
unreal.HighlightAreaPosition.__init__(points: Array[Vector] = []) -> None
unreal.HighlightAreaPosition.points(value: Array[Vector]) -> None
```

## `unreal.HighlightAreaStyle(StructBase)`

```python
unreal.HighlightAreaStyle.__init__(interior_color: str = "", exterior_color: str = "", exterior_outline_color: str = "", exterior_saturation: float = 0.000000, exterior_brightness: float = 0.000000, exterior_contrast: float = 0.000000) -> None
unreal.HighlightAreaStyle.exterior_brightness(value: float) -> None
unreal.HighlightAreaStyle.exterior_color(value: str) -> None
unreal.HighlightAreaStyle.exterior_contrast(value: float) -> None
unreal.HighlightAreaStyle.exterior_outline_color(value: str) -> None
unreal.HighlightAreaStyle.exterior_saturation(value: float) -> None
unreal.HighlightAreaStyle.interior_color(value: str) -> None
```

## `unreal.HighlightInfo(StructBase)`

```python
unreal.HighlightInfo.__init__(smc: StaticMeshComponent = None, default_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], mid: MaterialInstanceDynamic = None) -> None
unreal.HighlightInfo.default_color(value: LinearColor) -> None
unreal.HighlightInfo.mid(value: MaterialInstanceDynamic) -> None
unreal.HighlightInfo.smc(value: StaticMeshComponent) -> None
```

## `unreal.ImportanceTexture(StructBase)`

```python
unreal.ImportanceTexture.__init__(texture: Texture2D = None, weighting_func: ImportanceWeight = ImportanceWeight.LUMINANCE) -> None
```

## `unreal.InstancedStaticMeshComponent(StaticMeshComponent)`

```python
unreal.InstancedStaticMeshComponent.acquire_editor_element_handle(instance_index: int, allow_create: bool = True) -> ScriptTypedElementHandle
unreal.InstancedStaticMeshComponent.add_instance(instance_transform: Transform, world_space: bool = False) -> int
unreal.InstancedStaticMeshComponent.add_instance_world_space(world_transform: Transform) -> int
unreal.InstancedStaticMeshComponent.add_instances(instance_transforms: Array[Transform], should_return_indices: bool, world_space: bool = False, update_navigation: bool = True) -> Array[int]
unreal.InstancedStaticMeshComponent.batch_update_instances_transform(start_instance_index: int, num_instances: int, new_instances_transform: Transform, world_space: bool = False, mark_render_state_dirty: bool = False, teleport: bool = False) -> bool
unreal.InstancedStaticMeshComponent.batch_update_instances_transforms(start_instance_index: int, new_instances_transforms: Array[Transform], world_space: bool = False, mark_render_state_dirty: bool = False, teleport: bool = False) -> bool
unreal.InstancedStaticMeshComponent.clear_instances() -> None
unreal.InstancedStaticMeshComponent.get_cull_distances() -> Tuple[int, int]
unreal.InstancedStaticMeshComponent.get_instance_count() -> int
unreal.InstancedStaticMeshComponent.get_instance_transform(instance_index: int, world_space: bool = False) -> Optional[Transform]
unreal.InstancedStaticMeshComponent.get_instances_overlapping_box(box: Box, box_in_world_space: bool = True) -> Array[int]
unreal.InstancedStaticMeshComponent.get_instances_overlapping_sphere(center: Vector, radius: float, sphere_in_world_space: bool = True) -> Array[int]
unreal.InstancedStaticMeshComponent.get_lod_distance_scale() -> float
unreal.InstancedStaticMeshComponent.instance_end_cull_distance() -> int
unreal.InstancedStaticMeshComponent.instance_lod_distance_scale() -> float
unreal.InstancedStaticMeshComponent.instance_start_cull_distance() -> int
unreal.InstancedStaticMeshComponent.instancing_random_seed(value: int) -> None
unreal.InstancedStaticMeshComponent.is_valid_instance(instance_index: int) -> bool
unreal.InstancedStaticMeshComponent.remove_instance(instance_index: int) -> bool
unreal.InstancedStaticMeshComponent.remove_instances(instances_to_remove: Array[int]) -> bool
unreal.InstancedStaticMeshComponent.set_cull_distances(start_cull_distance: int, end_cull_distance: int) -> None
unreal.InstancedStaticMeshComponent.set_custom_data_value(instance_index: int, custom_data_index: int, custom_data_value: float, mark_render_state_dirty: bool = False) -> bool
unreal.InstancedStaticMeshComponent.set_lod_distance_scale(lod_distance_scale: float) -> None
unreal.InstancedStaticMeshComponent.set_num_custom_data_floats(num_custom_data_floats: int) -> None
unreal.InstancedStaticMeshComponent.update_instance_transform(instance_index: int, new_instance_transform: Transform, world_space: bool = False, mark_render_state_dirty: bool = False, teleport: bool = False) -> bool
unreal.InstancedStaticMeshComponent.use_gpu_lod_selection() -> bool
```

## `unreal.InstancedStaticMeshInstanceData(StructBase)`

```python
unreal.InstancedStaticMeshInstanceData.__init__() -> None
```

## `unreal.InterchangeBaseLightNode(InterchangeBaseNode)`

```python
unreal.InterchangeBaseLightNode.get_custom_intensity() -> Optional[float]
unreal.InterchangeBaseLightNode.get_custom_light_color() -> Optional[LinearColor]
unreal.InterchangeBaseLightNode.get_custom_temperature() -> Optional[float]
unreal.InterchangeBaseLightNode.get_custom_use_temperature() -> Optional[bool]
unreal.InterchangeBaseLightNode.set_custom_intensity(attribute_value: float) -> bool
unreal.InterchangeBaseLightNode.set_custom_light_color(attribute_value: LinearColor) -> bool
unreal.InterchangeBaseLightNode.set_custom_temperature(attribute_value: float) -> bool
unreal.InterchangeBaseLightNode.set_custom_use_temperature(attribute_value: bool) -> bool
```

## `unreal.InterchangeFunctionCallShaderNode(InterchangeShaderNode)`

```python
unreal.InterchangeFunctionCallShaderNode.get_custom_material_function() -> Optional[str]
unreal.InterchangeFunctionCallShaderNode.set_custom_material_function(attribute_value: str) -> bool
```

## `unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties(InterchangePipelineBase)`

```python
unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.convert_statics_with_morph_targets_to_skeletals(value: bool) -> None
unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_meshes_in_bone_hierarchy(value: bool) -> None
unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.import_only_animations(value: bool) -> None
unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.skeleton(value: Skeleton) -> None
unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties.use_t0_as_ref_pose(value: bool) -> None
```

## `unreal.InterchangeGenericMaterialPipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericMaterialPipeline.asset_name(value: str) -> None
unreal.InterchangeGenericMaterialPipeline.create_material_instance_for_parent(value: bool) -> None
unreal.InterchangeGenericMaterialPipeline.identify_duplicate_materials(value: bool) -> None
unreal.InterchangeGenericMaterialPipeline.import_materials(value: bool) -> None
unreal.InterchangeGenericMaterialPipeline.material_import(value: InterchangeMaterialImportOption) -> None
unreal.InterchangeGenericMaterialPipeline.parent_material(value: SoftObjectPath) -> None
unreal.InterchangeGenericMaterialPipeline.pipeline_display_name(value: str) -> None
unreal.InterchangeGenericMaterialPipeline.search_location(value: InterchangeMaterialSearchLocation) -> None
unreal.InterchangeGenericMaterialPipeline.texture_pipeline() -> InterchangeGenericTexturePipeline
```

## `unreal.InterchangeGenericTexturePipeline(InterchangePipelineBase)`

```python
unreal.InterchangeGenericTexturePipeline.allow_non_power_of_two(value: bool) -> None
unreal.InterchangeGenericTexturePipeline.asset_name(value: str) -> None
unreal.InterchangeGenericTexturePipeline.detect_normal_map_texture(value: bool) -> None
unreal.InterchangeGenericTexturePipeline.file_extensions_to_import_as_long_lat_cubemap(value: Set[str]) -> None
unreal.InterchangeGenericTexturePipeline.flip_normal_map_green_channel(value: bool) -> None
unreal.InterchangeGenericTexturePipeline.import_textures(value: bool) -> None
unreal.InterchangeGenericTexturePipeline.import_udi_ms(value: bool) -> None
unreal.InterchangeGenericTexturePipeline.pipeline_display_name(value: str) -> None
unreal.InterchangeGenericTexturePipeline.prefer_compressed_source_data(value: bool) -> None
```

## `unreal.InterchangeLightNode(InterchangeBaseLightNode)`

```python
unreal.InterchangeLightNode.get_custom_attenuation_radius() -> Optional[float]
unreal.InterchangeLightNode.get_custom_ies_brightness_scale() -> Optional[float]
unreal.InterchangeLightNode.get_custom_ies_texture() -> Optional[str]
unreal.InterchangeLightNode.get_custom_intensity_units() -> Optional[InterchangeLightUnits]
unreal.InterchangeLightNode.get_custom_rotation() -> Optional[Rotator]
unreal.InterchangeLightNode.get_custom_use_ies_brightness() -> Optional[bool]
unreal.InterchangeLightNode.set_custom_attenuation_radius(attribute_value: float) -> bool
unreal.InterchangeLightNode.set_custom_ies_brightness_scale(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightNode.set_custom_ies_texture(attribute_value: str) -> bool
unreal.InterchangeLightNode.set_custom_intensity_units(attribute_value: InterchangeLightUnits) -> bool
unreal.InterchangeLightNode.set_custom_rotation(attribute_value: Rotator, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightNode.set_custom_use_ies_brightness(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeMaterialInstanceNode(InterchangeBaseNode)`

```python
unreal.InterchangeMaterialInstanceNode.add_scalar_parameter_value(parameter_name: str, attribute_value: float) -> bool
unreal.InterchangeMaterialInstanceNode.add_static_switch_parameter_value(parameter_name: str, attribute_value: bool) -> bool
unreal.InterchangeMaterialInstanceNode.add_texture_parameter_value(parameter_name: str, attribute_value: str) -> bool
unreal.InterchangeMaterialInstanceNode.add_vector_parameter_value(parameter_name: str, attribute_value: LinearColor) -> bool
unreal.InterchangeMaterialInstanceNode.get_custom_parent() -> Optional[str]
unreal.InterchangeMaterialInstanceNode.get_scalar_parameter_value(parameter_name: str) -> Optional[float]
unreal.InterchangeMaterialInstanceNode.get_static_switch_parameter_value(parameter_name: str) -> Optional[bool]
unreal.InterchangeMaterialInstanceNode.get_texture_parameter_value(parameter_name: str) -> Optional[str]
unreal.InterchangeMaterialInstanceNode.get_vector_parameter_value(parameter_name: str) -> Optional[LinearColor]
unreal.InterchangeMaterialInstanceNode.set_custom_parent(attribute_value: str) -> bool
```

## `unreal.InterchangePointLightNode(InterchangeLightNode)`

```python
unreal.InterchangePointLightNode.get_custom_light_falloff_exponent() -> Optional[float]
unreal.InterchangePointLightNode.get_custom_use_inverse_squared_falloff() -> Optional[bool]
unreal.InterchangePointLightNode.set_custom_light_falloff_exponent(attribute_value: float) -> bool
unreal.InterchangePointLightNode.set_custom_use_inverse_squared_falloff(attribute_value: bool) -> bool
```

## `unreal.InterchangeRectLightNode(InterchangeLightNode)`

```python
unreal.InterchangeRectLightNode.get_custom_source_height() -> Optional[float]
unreal.InterchangeRectLightNode.get_custom_source_width() -> Optional[float]
unreal.InterchangeRectLightNode.set_custom_source_height(attribute_value: float) -> bool
unreal.InterchangeRectLightNode.set_custom_source_width(attribute_value: float) -> bool
```

## `unreal.InterchangeShaderGraphNode(InterchangeShaderNode)`

```python
unreal.InterchangeShaderGraphNode.get_custom_blend_mode() -> Optional[int]
unreal.InterchangeShaderGraphNode.get_custom_is_a_shader_function() -> Optional[bool]
unreal.InterchangeShaderGraphNode.get_custom_opacity_mask_clip_value() -> Optional[float]
unreal.InterchangeShaderGraphNode.get_custom_screen_space_reflections() -> Optional[bool]
unreal.InterchangeShaderGraphNode.get_custom_two_sided() -> Optional[bool]
unreal.InterchangeShaderGraphNode.get_custom_two_sided_transmission() -> Optional[bool]
unreal.InterchangeShaderGraphNode.set_custom_blend_mode(attribute_value: int) -> bool
unreal.InterchangeShaderGraphNode.set_custom_is_a_shader_function(attribute_value: bool) -> bool
unreal.InterchangeShaderGraphNode.set_custom_opacity_mask_clip_value(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeShaderGraphNode.set_custom_screen_space_reflections(attribute_value: bool) -> bool
unreal.InterchangeShaderGraphNode.set_custom_two_sided(attribute_value: bool) -> bool
unreal.InterchangeShaderGraphNode.set_custom_two_sided_transmission(attribute_value: bool) -> bool
```

## `unreal.InterchangeShaderNode(InterchangeBaseNode)`

```python
unreal.InterchangeShaderNode.add_float_input(input_name: str, attribute_value: float, is_a_parameter: bool = False) -> bool
unreal.InterchangeShaderNode.add_linear_color_input(input_name: str, attribute_value: LinearColor, is_a_parameter: bool = False) -> bool
unreal.InterchangeShaderNode.add_string_input(input_name: str, attribute_value: str, is_a_parameter: bool = False) -> bool
unreal.InterchangeShaderNode.get_custom_shader_type() -> Optional[str]
unreal.InterchangeShaderNode.set_custom_shader_type(attribute_value: str) -> bool
```

## `unreal.InterchangeShaderPortsAPI(Object)`

```python
unreal.InterchangeShaderPortsAPI.connect_default_ouput_to_input(interchange_node: InterchangeBaseNode, input_name: str, expression_uid: str) -> bool
unreal.InterchangeShaderPortsAPI.connect_ouput_to_input_by_index(interchange_node: InterchangeBaseNode, input_name: str, expression_uid: str, output_index: int) -> bool
unreal.InterchangeShaderPortsAPI.connect_ouput_to_input_by_name(interchange_node: InterchangeBaseNode, input_name: str, expression_uid: str, output_name: str) -> bool
unreal.InterchangeShaderPortsAPI.gather_inputs(interchange_node: InterchangeBaseNode) -> Array[str]
unreal.InterchangeShaderPortsAPI.get_input_connection(interchange_node: InterchangeBaseNode, input_name: str) -> Optional[Tuple[str, str]]
unreal.InterchangeShaderPortsAPI.has_input(interchange_node: InterchangeBaseNode, input_name: Name) -> bool
unreal.InterchangeShaderPortsAPI.has_parameter(interchange_node: InterchangeBaseNode, input_name: Name) -> bool
unreal.InterchangeShaderPortsAPI.is_a_parameter(attribute_key: str) -> bool
unreal.InterchangeShaderPortsAPI.is_an_input(attribute_key: str) -> bool
unreal.InterchangeShaderPortsAPI.make_input_connection_key(input_name: str) -> str
unreal.InterchangeShaderPortsAPI.make_input_name(input_key: str) -> str
unreal.InterchangeShaderPortsAPI.make_input_parameter_key(input_name: str) -> str
unreal.InterchangeShaderPortsAPI.make_input_value_key(input_name: str) -> str
```

## `unreal.InterchangeSkeletalMeshLodDataNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeSkeletalMeshLodDataNode.add_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeSkeletalMeshLodDataNode.get_custom_skeleton_uid() -> Optional[str]
unreal.InterchangeSkeletalMeshLodDataNode.get_mesh_uids() -> Array[str]
unreal.InterchangeSkeletalMeshLodDataNode.get_mesh_uids_count() -> int
unreal.InterchangeSkeletalMeshLodDataNode.remove_all_meshes() -> bool
unreal.InterchangeSkeletalMeshLodDataNode.remove_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeSkeletalMeshLodDataNode.set_custom_skeleton_uid(attribute_value: str) -> bool
```

## `unreal.InterchangeSpotLightNode(InterchangePointLightNode)`

```python
unreal.InterchangeSpotLightNode.get_custom_inner_cone_angle() -> Optional[float]
unreal.InterchangeSpotLightNode.get_custom_outer_cone_angle() -> Optional[float]
unreal.InterchangeSpotLightNode.set_custom_inner_cone_angle(attribute_value: float) -> bool
unreal.InterchangeSpotLightNode.set_custom_outer_cone_angle(attribute_value: float) -> bool
```

## `unreal.InterchangeStaticMeshLodDataNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeStaticMeshLodDataNode.add_box_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.add_capsule_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.add_convex_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.add_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.add_sphere_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.get_box_collision_mesh_uids() -> Array[str]
unreal.InterchangeStaticMeshLodDataNode.get_box_collision_mesh_uids_count() -> int
unreal.InterchangeStaticMeshLodDataNode.get_capsule_collision_mesh_uids() -> Array[str]
unreal.InterchangeStaticMeshLodDataNode.get_capsule_collision_mesh_uids_count() -> int
unreal.InterchangeStaticMeshLodDataNode.get_convex_collision_mesh_uids() -> Array[str]
unreal.InterchangeStaticMeshLodDataNode.get_convex_collision_mesh_uids_count() -> int
unreal.InterchangeStaticMeshLodDataNode.get_import_collision() -> Optional[bool]
unreal.InterchangeStaticMeshLodDataNode.get_import_collision_type() -> Optional[InterchangeMeshCollision]
unreal.InterchangeStaticMeshLodDataNode.get_mesh_uids() -> Array[str]
unreal.InterchangeStaticMeshLodDataNode.get_mesh_uids_count() -> int
unreal.InterchangeStaticMeshLodDataNode.get_one_convex_hull_per_ucx() -> Optional[bool]
unreal.InterchangeStaticMeshLodDataNode.get_sphere_collision_mesh_uids() -> Array[str]
unreal.InterchangeStaticMeshLodDataNode.get_sphere_collision_mesh_uids_count() -> int
unreal.InterchangeStaticMeshLodDataNode.remove_all_box_collision_meshes() -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_all_capsule_collision_meshes() -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_all_convex_collision_meshes() -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_all_meshes() -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_all_sphere_collision_meshes() -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_box_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_capsule_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_convex_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.remove_sphere_collision_mesh_uid(mesh_name: str) -> bool
unreal.InterchangeStaticMeshLodDataNode.set_import_collision(attribute_value: bool) -> bool
unreal.InterchangeStaticMeshLodDataNode.set_import_collision_type(attribute_value: InterchangeMeshCollision) -> bool
unreal.InterchangeStaticMeshLodDataNode.set_one_convex_hull_per_ucx(attribute_value: bool) -> bool
```

## `unreal.InterchangeTexture2DNode(InterchangeTextureNode)`

```python
unreal.InterchangeTexture2DNode.get_custom_wrap_u() -> Optional[InterchangeTextureWrapMode]
unreal.InterchangeTexture2DNode.get_custom_wrap_v() -> Optional[InterchangeTextureWrapMode]
unreal.InterchangeTexture2DNode.get_source_blocks() -> Map[int, str]
unreal.InterchangeTexture2DNode.set_custom_wrap_u(attribute_value: InterchangeTextureWrapMode) -> bool
unreal.InterchangeTexture2DNode.set_custom_wrap_v(attribute_value: InterchangeTextureWrapMode) -> bool
```

## `unreal.InterchangeTextureNode(InterchangeBaseNode)`

```python
unreal.InterchangeTextureNode.get_custom_color_space() -> Optional[InterchangeTextureColorSpace]
unreal.InterchangeTextureNode.get_custom_filter() -> Optional[InterchangeTextureFilterMode]
unreal.InterchangeTextureNode.get_custom_srgb() -> Optional[bool]
unreal.InterchangeTextureNode.get_customb_flip_green_channel() -> Optional[bool]
unreal.InterchangeTextureNode.set_custom_color_space(attribute_value: InterchangeTextureColorSpace) -> bool
unreal.InterchangeTextureNode.set_custom_filter(attribute_value: InterchangeTextureFilterMode) -> bool
unreal.InterchangeTextureNode.set_custom_srgb(attribute_value: bool) -> bool
unreal.InterchangeTextureNode.set_customb_flip_green_channel(attribute_value: bool) -> bool
unreal.InterchangeTextureNode.set_pay_load_key(payload_key: str) -> None
```

## `unreal.InterruptedFlight(MulticastDelegateBase)`

```python
unreal.InterruptedFlight.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.LandscapePerLODMaterialOverride(StructBase)`

```python
unreal.LandscapePerLODMaterialOverride.__init__() -> None
```

## `unreal.Light(Actor)`

```python
unreal.Light.get_brightness() -> float
unreal.Light.get_light_color() -> LinearColor
unreal.Light.is_enabled() -> bool
unreal.Light.light_component() -> LightComponent
unreal.Light.set_affect_translucent_lighting(new_value: bool) -> None
unreal.Light.set_brightness(new_brightness: float) -> None
unreal.Light.set_cast_shadows(new_value: bool) -> None
unreal.Light.set_enabled(set_enabled: bool) -> None
unreal.Light.set_light_color(new_light_color: LinearColor) -> None
unreal.Light.set_light_function_fade_distance(new_light_function_fade_distance: float) -> None
unreal.Light.set_light_function_material(new_light_function_material: MaterialInterface) -> None
unreal.Light.set_light_function_scale(new_light_function_scale: Vector) -> None
unreal.Light.toggle_enabled() -> None
```

## `unreal.LightArray(StructBase)`

```python
unreal.LightArray.__init__(light_actors: Array[Actor] = []) -> None
unreal.LightArray.light_actors(value: Array[Actor]) -> None
```

## `unreal.LightCollection(StructBase)`

```python
unreal.LightCollection.__init__(spot_light: Map[SpotLight, float] = {}, points_lights: Map[PointLight, float] = {}, rect_lights: Map[RectLight, float] = {}, light_actors: Array[Actor] = []) -> None
unreal.LightCollection.light_actors(value: Array[Actor]) -> None
unreal.LightCollection.points_lights(value: Map[PointLight, float]) -> None
unreal.LightCollection.rect_lights(value: Map[RectLight, float]) -> None
unreal.LightCollection.spot_light(value: Map[SpotLight, float]) -> None
```

## `unreal.LightCompIntensity(StructBase)`

```python
unreal.LightCompIntensity.__init__(light_comp_intensity: Map[LightComponent, float] = {}) -> None
unreal.LightCompIntensity.light_comp_intensity(value: Map[LightComponent, float]) -> None
```

## `unreal.LightComponent(LightComponentBase)`

```python
unreal.LightComponent.allow_mega_lights() -> bool
unreal.LightComponent.bloom_max_brightness() -> float
unreal.LightComponent.bloom_scale() -> float
unreal.LightComponent.bloom_threshold() -> float
unreal.LightComponent.bloom_tint() -> Color
unreal.LightComponent.cast_shadows_from_cinematic_objects_only() -> bool
unreal.LightComponent.cast_translucent_shadows() -> bool
unreal.LightComponent.contact_shadow_casting_intensity(value: float) -> None
unreal.LightComponent.contact_shadow_length(value: float) -> None
unreal.LightComponent.contact_shadow_length_in_ws(value: bool) -> None
unreal.LightComponent.contact_shadow_non_casting_intensity(value: float) -> None
unreal.LightComponent.diffuse_scale() -> float
unreal.LightComponent.disabled_brightness() -> float
unreal.LightComponent.enable_light_shaft_bloom() -> bool
unreal.LightComponent.force_cached_shadows_for_movable_primitives() -> bool
unreal.LightComponent.ies_brightness_scale() -> float
unreal.LightComponent.ies_texture() -> TextureLightProfile
unreal.LightComponent.light_function_fade_distance() -> float
unreal.LightComponent.light_function_material() -> MaterialInterface
unreal.LightComponent.light_function_scale() -> Vector
unreal.LightComponent.lighting_channels() -> LightingChannels
unreal.LightComponent.mega_lights_shadow_method() -> MegaLightsShadowMethod
unreal.LightComponent.ray_start_offset_depth_scale() -> float
unreal.LightComponent.set_affect_translucent_lighting(new_value: bool) -> None
unreal.LightComponent.set_bloom_max_brightness(new_value: float) -> None
unreal.LightComponent.set_bloom_scale(new_value: float) -> None
unreal.LightComponent.set_bloom_threshold(new_value: float) -> None
unreal.LightComponent.set_bloom_tint(new_value: Color) -> None
unreal.LightComponent.set_brightness(new_intensity: float) -> None
unreal.LightComponent.set_diffuse_scale(new_value: float) -> None
unreal.LightComponent.set_enable_light_shaft_bloom(new_value: bool) -> None
unreal.LightComponent.set_force_cached_shadows_for_movable_primitives(new_value: bool) -> None
unreal.LightComponent.set_ies_brightness_scale(new_value: float) -> None
unreal.LightComponent.set_ies_texture(new_value: TextureLightProfile) -> None
unreal.LightComponent.set_indirect_lighting_intensity(new_intensity: float) -> None
unreal.LightComponent.set_intensity(new_intensity: float) -> None
unreal.LightComponent.set_light_color(new_light_color: LinearColor, srgb: bool = True) -> None
unreal.LightComponent.set_light_function_disabled_brightness(new_value: float) -> None
unreal.LightComponent.set_light_function_fade_distance(new_light_function_fade_distance: float) -> None
unreal.LightComponent.set_light_function_material(new_light_function_material: MaterialInterface) -> None
unreal.LightComponent.set_light_function_scale(new_light_function_scale: Vector) -> None
unreal.LightComponent.set_lighting_channels(channel0: bool, channel1: bool, channel2: bool) -> None
unreal.LightComponent.set_shadow_bias(new_value: float) -> None
unreal.LightComponent.set_shadow_slope_bias(new_value: float) -> None
unreal.LightComponent.set_specular_scale(new_value: float) -> None
unreal.LightComponent.set_temperature(new_temperature: float) -> None
unreal.LightComponent.set_transmission(new_value: bool) -> None
unreal.LightComponent.set_use_ies_brightness(new_value: bool) -> None
unreal.LightComponent.set_use_ray_traced_distance_field_shadows(new_value: bool) -> None
unreal.LightComponent.set_use_temperature(new_value: bool) -> None
unreal.LightComponent.set_volumetric_scattering_intensity(new_intensity: float) -> None
unreal.LightComponent.shadow_bias() -> float
unreal.LightComponent.shadow_resolution_scale() -> float
unreal.LightComponent.shadow_sharpen() -> float
unreal.LightComponent.shadow_slope_bias() -> float
unreal.LightComponent.specular_scale() -> float
unreal.LightComponent.temperature() -> float
unreal.LightComponent.use_ies_brightness() -> bool
unreal.LightComponent.use_ray_traced_distance_field_shadows() -> bool
unreal.LightComponent.use_temperature() -> bool
```

## `unreal.LightComponentBase(SceneComponent)`

```python
unreal.LightComponentBase.affect_global_illumination() -> bool
unreal.LightComponentBase.affect_reflection() -> bool
unreal.LightComponentBase.affect_translucent_lighting() -> bool
unreal.LightComponentBase.affects_world() -> bool
unreal.LightComponentBase.brightness() -> float
unreal.LightComponentBase.cast_deep_shadow() -> bool
unreal.LightComponentBase.cast_dynamic_shadows() -> bool
unreal.LightComponentBase.cast_raytraced_shadow() -> CastRayTracedShadow
unreal.LightComponentBase.cast_shadows() -> bool
unreal.LightComponentBase.cast_static_shadows() -> bool
unreal.LightComponentBase.cast_volumetric_shadow() -> bool
unreal.LightComponentBase.deep_shadow_layer_distribution() -> float
unreal.LightComponentBase.get_light_color() -> LinearColor
unreal.LightComponentBase.indirect_lighting_intensity() -> float
unreal.LightComponentBase.intensity() -> float
unreal.LightComponentBase.light_color() -> Color
unreal.LightComponentBase.samples_per_pixel() -> int
unreal.LightComponentBase.set_affect_global_illumination(new_value: bool) -> None
unreal.LightComponentBase.set_affect_reflection(new_value: bool) -> None
unreal.LightComponentBase.set_cast_deep_shadow(new_value: bool) -> None
unreal.LightComponentBase.set_cast_raytraced_shadow(new_value: bool) -> None
unreal.LightComponentBase.set_cast_raytraced_shadows(new_value: CastRayTracedShadow) -> None
unreal.LightComponentBase.set_cast_shadows(new_value: bool) -> None
unreal.LightComponentBase.set_cast_volumetric_shadow(new_value: bool) -> None
unreal.LightComponentBase.set_samples_per_pixel(new_value: int) -> None
unreal.LightComponentBase.transmission() -> bool
unreal.LightComponentBase.volumetric_scattering_intensity() -> float
```

## `unreal.LightEntityAtom(EntityAtomBase)`

```python
unreal.LightEntityAtom.angle(value: int) -> None
unreal.LightEntityAtom.attenuation(value: int) -> None
unreal.LightEntityAtom.color(value: str) -> None
unreal.LightEntityAtom.haze(value: bool) -> None
unreal.LightEntityAtom.haze_intensity(value: int) -> None
unreal.LightEntityAtom.intensity(value: int) -> None
unreal.LightEntityAtom.shadows(value: bool) -> None
```

## `unreal.LightOC(StructBase)`

```python
unreal.LightOC.__init__(tag: Name = "None", close_light_interval: float = 0.000000, open_light_interval: float = 0.000000) -> None
unreal.LightOC.close_light_interval(value: float) -> None
unreal.LightOC.open_light_interval(value: float) -> None
unreal.LightOC.tag(value: Name) -> None
```

## `unreal.LightOC_MPC(StructBase)`

```python
unreal.LightOC_MPC.__init__(close_light_interval: float = 0.000000, open_light_interval: float = 0.000000, close_light_mpc: MatCollectionSetting_Array = [[]], open_light_mpc: MatCollectionSetting_Array = [[]]) -> None
unreal.LightOC_MPC.close_light_interval(value: float) -> None
unreal.LightOC_MPC.close_light_mpc(value: MatCollectionSetting_Array) -> None
unreal.LightOC_MPC.open_light_interval(value: float) -> None
unreal.LightOC_MPC.open_light_mpc(value: MatCollectionSetting_Array) -> None
```

## `unreal.LightWeightInstanceBlueprintFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.LightWeightInstanceBlueprintFunctionLibrary.convert_actor_to_light_weight_instance(actor: Actor) -> ActorInstanceHandle
unreal.LightWeightInstanceBlueprintFunctionLibrary.create_new_light_weight_instance(actor_class: Class, transform: Transform, layer: DataLayerInstance, world: World) -> ActorInstanceHandle
```

## `unreal.LightWeightInstanceStaticMeshManager(LightWeightInstanceManager)`

```python
unreal.LightWeightInstanceStaticMeshManager.ism_component() -> InstancedStaticMeshComponent
unreal.LightWeightInstanceStaticMeshManager.static_mesh() -> StaticMesh
```

## `unreal.LightingChannels(StructBase)`

```python
unreal.LightingChannels.__init__(channel0: bool = False, channel1: bool = False, channel2: bool = False) -> None
unreal.LightingChannels.channel0() -> bool
unreal.LightingChannels.channel1() -> bool
unreal.LightingChannels.channel2() -> bool
```

## `unreal.LightmassBooleanParameterValue(LightmassParameterValue)`

```python
unreal.LightmassBooleanParameterValue.__init__() -> None
```

## `unreal.LightmassDirectionalLightSettings(LightmassLightSettings)`

```python
unreal.LightmassDirectionalLightSettings.__init__() -> None
```

## `unreal.LightmassLightSettings(StructBase)`

```python
unreal.LightmassLightSettings.__init__() -> None
```

## `unreal.LightmassMaterialInterfaceSettings(StructBase)`

```python
unreal.LightmassMaterialInterfaceSettings.__init__() -> None
```

## `unreal.LightmassParameterValue(StructBase)`

```python
unreal.LightmassParameterValue.__init__() -> None
```

## `unreal.LightmassParameterizedMaterialSettings(StructBase)`

```python
unreal.LightmassParameterizedMaterialSettings.__init__() -> None
```

## `unreal.LightmassPointLightSettings(LightmassLightSettings)`

```python
unreal.LightmassPointLightSettings.__init__() -> None
```

## `unreal.LightmassPortal(Actor)`

```python
unreal.LightmassPortal.portal_component() -> LightmassPortalComponent
```

## `unreal.LightmassPrimitiveSettings(StructBase)`

```python
unreal.LightmassPrimitiveSettings.__init__() -> None
```

## `unreal.LightmassScalarParameterValue(LightmassParameterValue)`

```python
unreal.LightmassScalarParameterValue.__init__() -> None
```

## `unreal.LightningParameters(StructBase)`

```python
unreal.LightningParameters.__init__() -> None
```

## `unreal.LiveLinkLightBlueprintData(LiveLinkBaseBlueprintData)`

```python
unreal.LiveLinkLightBlueprintData.__init__(static_data: LiveLinkLightStaticData = [False, False, False, False, False, False, False, False, False, True, True, False, []], frame_data: LiveLinkLightFrameData = [6500.000000, 3.141593, [255, 255, 255, 255], 0.000000, 44.000000, 1000.000000, 0.000000, 0.000000, 0.000000, [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [{}, [[0], [24, 1], 0.000000]], []]) -> None
unreal.LiveLinkLightBlueprintData.frame_data(value: LiveLinkLightFrameData) -> None
unreal.LiveLinkLightBlueprintData.static_data(value: LiveLinkLightStaticData) -> None
```

## `unreal.LiveLinkLightFrameData(LiveLinkTransformFrameData)`

```python
unreal.LiveLinkLightFrameData.__init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]], property_values: Array[float] = [], transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], temperature: float = 0.000000, intensity: float = 0.000000, light_color: Color = [0, 0, 0, 0], inner_cone_angle: float = 0.000000, outer_cone_angle: float = 0.000000, attenuation_radius: float = 0.000000, source_radius: float = 0.000000, soft_source_radius: float = 0.000000, source_length: float = 0.000000) -> None
unreal.LiveLinkLightFrameData.attenuation_radius(value: float) -> None
unreal.LiveLinkLightFrameData.inner_cone_angle(value: float) -> None
unreal.LiveLinkLightFrameData.intensity(value: float) -> None
unreal.LiveLinkLightFrameData.light_color(value: Color) -> None
unreal.LiveLinkLightFrameData.outer_cone_angle(value: float) -> None
unreal.LiveLinkLightFrameData.soft_source_radius(value: float) -> None
unreal.LiveLinkLightFrameData.source_length(value: float) -> None
unreal.LiveLinkLightFrameData.source_radius(value: float) -> None
unreal.LiveLinkLightFrameData.temperature(value: float) -> None
```

## `unreal.LiveLinkLightStaticData(LiveLinkTransformStaticData)`

```python
unreal.LiveLinkLightStaticData.__init__(property_names: Array[Name] = [], is_location_supported: bool = False, is_rotation_supported: bool = False, is_scale_supported: bool = False, is_temperature_supported: bool = False, is_intensity_supported: bool = False, is_light_color_supported: bool = False, is_inner_cone_angle_supported: bool = False, is_outer_cone_angle_supported: bool = False, is_attenuation_radius_supported: bool = False, is_source_lenght_supported: bool = False, is_source_radius_supported: bool = False, is_soft_source_radius_supported: bool = False) -> None
unreal.LiveLinkLightStaticData.is_attenuation_radius_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_inner_cone_angle_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_intensity_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_light_color_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_outer_cone_angle_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_soft_source_radius_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_source_lenght_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_source_radius_supported(value: bool) -> None
unreal.LiveLinkLightStaticData.is_temperature_supported(value: bool) -> None
```

## `unreal.LocalLightComponent(LightComponent)`

```python
unreal.LocalLightComponent.attenuation_radius() -> float
unreal.LocalLightComponent.get_units_conversion_factor(src_units: LightUnits, target_units: LightUnits, cos_half_cone_angle: float = -1.000000) -> float
unreal.LocalLightComponent.intensity_units() -> LightUnits
unreal.LocalLightComponent.inverse_exposure_blend() -> float
unreal.LocalLightComponent.set_attenuation_radius(new_radius: float) -> None
unreal.LocalLightComponent.set_intensity_units(new_intensity_units: LightUnits) -> None
```

## `unreal.ML_Material_Channel_Control(StructBase)`

```python
unreal.ML_Material_Channel_Control.__init__(diffuse: str = "", diffuse_color: Color = [0, 0, 0, 0], diffuse_intensity: float = 0.000000, diffuse_desaturation: float = 0.000000, normal: str = "", normal_intensity: float = 0.000000, specular: str = "", specular_intensity: float = 0.000000, ao: str = "", ao_intensity: float = 0.000000, metallic: str = "", metallic_intensity: float = 0.000000, roughness: str = "", roughness_intensity: float = 0.000000, indoor_tex: str = "", alpha: str = "", inner_color: Color = [0, 0, 0, 0], morning_em_tex: str = "", morning_em_power: float = 0.000000, morning_em: float = 0.000000, window_interior_color: Color = [0, 0, 0, 0], opacity: float = 0.000000) -> None
unreal.ML_Material_Channel_Control.alpha(value: str) -> None
unreal.ML_Material_Channel_Control.ao(value: str) -> None
unreal.ML_Material_Channel_Control.ao_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.diffuse(value: str) -> None
unreal.ML_Material_Channel_Control.diffuse_color(value: Color) -> None
unreal.ML_Material_Channel_Control.diffuse_desaturation(value: float) -> None
unreal.ML_Material_Channel_Control.diffuse_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.indoor_tex(value: str) -> None
unreal.ML_Material_Channel_Control.inner_color(value: Color) -> None
unreal.ML_Material_Channel_Control.metallic(value: str) -> None
unreal.ML_Material_Channel_Control.metallic_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.morning_em(value: float) -> None
unreal.ML_Material_Channel_Control.morning_em_power(value: float) -> None
unreal.ML_Material_Channel_Control.morning_em_tex(value: str) -> None
unreal.ML_Material_Channel_Control.normal(value: str) -> None
unreal.ML_Material_Channel_Control.normal_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.opacity(value: float) -> None
unreal.ML_Material_Channel_Control.roughness(value: str) -> None
unreal.ML_Material_Channel_Control.roughness_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.specular(value: str) -> None
unreal.ML_Material_Channel_Control.specular_intensity(value: float) -> None
unreal.ML_Material_Channel_Control.window_interior_color(value: Color) -> None
```

## `unreal.MassStaticMeshInstanceVisualizationMeshDesc(StructBase)`

```python
unreal.MassStaticMeshInstanceVisualizationMeshDesc.__init__() -> None
```

## `unreal.Material(MaterialInterface)`

```python
unreal.Material.always_evaluate_world_position_offset(value: bool) -> None
unreal.Material.automatically_set_usage_in_editor() -> bool
unreal.Material.blend_mode() -> BlendMode
unreal.Material.blendable_location(value: BlendableLocation) -> None
unreal.Material.blendable_output_alpha(value: bool) -> None
unreal.Material.blendable_priority(value: int) -> None
unreal.Material.decal_blend_mode(value: DecalBlendMode) -> None
unreal.Material.displacement_fade_range(value: DisplacementFadeRange) -> None
unreal.Material.displacement_scaling(value: DisplacementScaling) -> None
unreal.Material.float_precision_mode() -> MaterialFloatPrecisionMode
unreal.Material.forward_blends_sky_light_cubemaps() -> bool
unreal.Material.forward_render_use_preintegrated_gf_for_simple_ibl() -> bool
unreal.Material.fully_rough() -> bool
unreal.Material.is_blendable(value: bool) -> None
unreal.Material.material_decal_response() -> MaterialDecalResponse
unreal.Material.material_domain() -> MaterialDomain
unreal.Material.max_world_position_offset_displacement(value: float) -> None
unreal.Material.max_world_position_offset_distance(value: float) -> None
unreal.Material.mobile_enable_high_quality_brdf() -> bool
unreal.Material.normal_curvature_to_roughness() -> bool
unreal.Material.parameter_group_data(value: Array[ParameterGroupData]) -> None
unreal.Material.resolution_relative_to_input(value: Name) -> None
unreal.Material.use_alpha_to_coverage() -> bool
unreal.Material.use_emissive_for_dynamic_area_lighting(value: bool) -> None
unreal.Material.use_hq_forward_reflections() -> bool
unreal.Material.use_lightmap_directionality() -> bool
unreal.Material.use_planar_forward_reflections() -> bool
unreal.Material.used_with_beam_trails() -> bool
unreal.Material.used_with_clothing() -> bool
unreal.Material.used_with_editor_compositing() -> bool
unreal.Material.used_with_geometry_cache() -> bool
unreal.Material.used_with_geometry_collections() -> bool
unreal.Material.used_with_hair_strands() -> bool
unreal.Material.used_with_heterogeneous_volumes() -> bool
unreal.Material.used_with_instanced_static_meshes() -> bool
unreal.Material.used_with_lidar_point_cloud() -> bool
unreal.Material.used_with_mesh_particles() -> bool
unreal.Material.used_with_morph_targets() -> bool
unreal.Material.used_with_nanite() -> bool
unreal.Material.used_with_niagara_mesh_particles() -> bool
unreal.Material.used_with_niagara_ribbons() -> bool
unreal.Material.used_with_niagara_sprites() -> bool
unreal.Material.used_with_particle_sprites() -> bool
unreal.Material.used_with_skeletal_mesh() -> bool
unreal.Material.used_with_spline_meshes() -> bool
unreal.Material.used_with_static_lighting() -> bool
unreal.Material.used_with_virtual_heightfield_mesh() -> bool
unreal.Material.used_with_volumetric_cloud() -> bool
unreal.Material.used_with_water() -> bool
unreal.Material.user_scene_texture(value: Name) -> None
unreal.Material.user_texture_divisor(value: IntPoint) -> None
```

## `unreal.MaterialAtom(EntityAtomBase)`

```python
unreal.MaterialAtom.apply_material_from_data() -> bool
unreal.MaterialAtom.apply_material_to_component(component: PrimitiveComponent, material_index: int, mi_eid: int) -> bool
unreal.MaterialAtom.changed_material_info() -> Array[ChangedMaterialInfo]
unreal.MaterialAtom.receives_decals() -> bool
```

## `unreal.MaterialBillboardComponent(PrimitiveComponent)`

```python
unreal.MaterialBillboardComponent.add_element(material: MaterialInterface, distance_to_opacity_curve: CurveFloat, size_is_in_screen_space: bool, base_size_x: float, base_size_y: float, distance_to_size_curve: CurveFloat) -> None
unreal.MaterialBillboardComponent.elements() -> Array[MaterialSpriteElement]
unreal.MaterialBillboardComponent.set_elements(new_elements: Array[MaterialSpriteElement]) -> None
```

## `unreal.MaterialEditingLibrary(BlueprintFunctionLibrary)`

```python
unreal.MaterialEditingLibrary.clear_all_material_instance_parameters(instance: MaterialInstanceConstant) -> None
unreal.MaterialEditingLibrary.connect_material_expressions(from_expression: MaterialExpression, from_output_name: str, to_expression: MaterialExpression, to_input_name: str) -> bool
unreal.MaterialEditingLibrary.connect_material_property(from_expression: MaterialExpression, from_output_name: str, property_: MaterialProperty) -> bool
unreal.MaterialEditingLibrary.create_material_expression(material: Material, expression_class: Class, node_pos_x: int = 0, node_pos_y: int = 0) -> MaterialExpression
unreal.MaterialEditingLibrary.create_material_expression_in_function(material_function: MaterialFunction, expression_class: Class, node_pos_x: int = 0, node_pos_y: int = 0) -> MaterialExpression
unreal.MaterialEditingLibrary.delete_all_material_expressions(material: Material) -> None
unreal.MaterialEditingLibrary.delete_all_material_expressions_in_function(material_function: MaterialFunction) -> None
unreal.MaterialEditingLibrary.delete_material_expression(material: Material, expression: MaterialExpression) -> None
unreal.MaterialEditingLibrary.delete_material_expression_in_function(material_function: MaterialFunction, expression: MaterialExpression) -> None
unreal.MaterialEditingLibrary.duplicate_material_expression(material: Material, material_function: MaterialFunction, expression: MaterialExpression) -> MaterialExpression
unreal.MaterialEditingLibrary.get_child_instances(parent: MaterialInterface) -> Array[AssetData]
unreal.MaterialEditingLibrary.get_input_node_output_name_for_material_expression(material_expression: MaterialExpression, input_node: MaterialExpression) -> Optional[str]
unreal.MaterialEditingLibrary.get_inputs_for_material_expression(material: Material, material_expression: MaterialExpression) -> Array[MaterialExpression]
unreal.MaterialEditingLibrary.get_material_default_scalar_parameter_value(material: Material, parameter_name: Name) -> float
unreal.MaterialEditingLibrary.get_material_default_static_switch_parameter_value(material: Material, parameter_name: Name) -> bool
unreal.MaterialEditingLibrary.get_material_default_texture_parameter_value(material: Material, parameter_name: Name) -> Texture
unreal.MaterialEditingLibrary.get_material_default_vector_parameter_value(material: Material, parameter_name: Name) -> LinearColor
unreal.MaterialEditingLibrary.get_material_expression_input_names(material_expression: MaterialExpression) -> Array[str]
unreal.MaterialEditingLibrary.get_material_expression_input_types(material_expression: MaterialExpression) -> Array[int]
unreal.MaterialEditingLibrary.get_material_expression_node_position(material_expression: MaterialExpression) -> Tuple[int, int]
unreal.MaterialEditingLibrary.get_material_instance_runtime_virtual_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> RuntimeVirtualTexture
unreal.MaterialEditingLibrary.get_material_instance_scalar_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> float
unreal.MaterialEditingLibrary.get_material_instance_sparse_volume_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> SparseVolumeTexture
unreal.MaterialEditingLibrary.get_material_instance_static_switch_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.get_material_instance_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> Texture
unreal.MaterialEditingLibrary.get_material_instance_vector_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> LinearColor
unreal.MaterialEditingLibrary.get_material_property_input_node(material: Material, property_: MaterialProperty) -> MaterialExpression
unreal.MaterialEditingLibrary.get_material_property_input_node_output_name(material: Material, property_: MaterialProperty) -> str
unreal.MaterialEditingLibrary.get_material_selected_nodes(material: Material) -> Set[Object]
unreal.MaterialEditingLibrary.get_nanite_override_material(material: MaterialInterface) -> MaterialInterface
unreal.MaterialEditingLibrary.get_num_material_expressions(material: Material) -> int
unreal.MaterialEditingLibrary.get_num_material_expressions_in_function(material_function: MaterialFunction) -> int
unreal.MaterialEditingLibrary.get_scalar_parameter_names(material: MaterialInterface) -> Array[Name]
unreal.MaterialEditingLibrary.get_scalar_parameter_source(material: MaterialInterface, parameter_name: Name) -> Optional[SoftObjectPath]
unreal.MaterialEditingLibrary.get_static_switch_parameter_names(material: MaterialInterface) -> Array[Name]
unreal.MaterialEditingLibrary.get_static_switch_parameter_source(material: MaterialInterface, parameter_name: Name) -> Optional[SoftObjectPath]
unreal.MaterialEditingLibrary.get_statistics(material: MaterialInterface) -> MaterialStatistics
unreal.MaterialEditingLibrary.get_texture_parameter_names(material: MaterialInterface) -> Array[Name]
unreal.MaterialEditingLibrary.get_texture_parameter_source(material: MaterialInterface, parameter_name: Name) -> Optional[SoftObjectPath]
unreal.MaterialEditingLibrary.get_used_textures(material: Material) -> Array[Texture]
unreal.MaterialEditingLibrary.get_vector_parameter_names(material: MaterialInterface) -> Array[Name]
unreal.MaterialEditingLibrary.get_vector_parameter_source(material: MaterialInterface, parameter_name: Name) -> Optional[SoftObjectPath]
unreal.MaterialEditingLibrary.has_material_usage(material: Material, usage: MaterialUsage) -> bool
unreal.MaterialEditingLibrary.layout_material_expressions(material: Material) -> None
unreal.MaterialEditingLibrary.layout_material_function_expressions(material_function: MaterialFunction) -> None
unreal.MaterialEditingLibrary.recompile_material(material: Material) -> None
unreal.MaterialEditingLibrary.set_material_instance_parent(instance: MaterialInstanceConstant, new_parent: MaterialInterface) -> None
unreal.MaterialEditingLibrary.set_material_instance_runtime_virtual_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: RuntimeVirtualTexture, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: float, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_instance_sparse_volume_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: SparseVolumeTexture, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: bool, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: Texture, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(instance: MaterialInstanceConstant, parameter_name: Name, value: LinearColor, association: MaterialParameterAssociation = MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
unreal.MaterialEditingLibrary.set_material_usage(material: Material, usage: MaterialUsage) -> Optional[bool]
unreal.MaterialEditingLibrary.update_material_function(material_function: MaterialFunctionInterface, preview_material: Material = None) -> None
unreal.MaterialEditingLibrary.update_material_instance(instance: MaterialInstanceConstant) -> None
```

## `unreal.MaterialEditorClickEventParam(EventArgsBase)`

```python
unreal.MaterialEditorClickEventParam.__init__(material_name: str = "", material_lable: str = "") -> None
unreal.MaterialEditorClickEventParam.material_lable(value: str) -> None
unreal.MaterialEditorClickEventParam.material_name(value: str) -> None
```

## `unreal.MaterialEditorInstanceConstant(MaterialEditorParameters)`

```python
unreal.MaterialEditorInstanceConstant.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialEditorPostProcessOverrides(StructBase)`

```python
unreal.MaterialEditorPostProcessOverrides.__init__() -> None
```

## `unreal.MaterialExpression(Object)`

```python
unreal.MaterialExpression.material_expression_editor_x(value: int) -> None
unreal.MaterialExpression.material_expression_editor_y(value: int) -> None
```

## `unreal.MaterialExpressionConstant(MaterialExpression)`

```python
unreal.MaterialExpressionConstant.r(value: float) -> None
```

## `unreal.MaterialExpressionConstant2Vector(MaterialExpression)`

```python
unreal.MaterialExpressionConstant2Vector.g(value: float) -> None
unreal.MaterialExpressionConstant2Vector.r(value: float) -> None
```

## `unreal.MaterialExpressionConstant3Vector(MaterialExpression)`

```python
unreal.MaterialExpressionConstant3Vector.constant(value: LinearColor) -> None
```

## `unreal.MaterialExpressionConstant4Vector(MaterialExpression)`

```python
unreal.MaterialExpressionConstant4Vector.constant(value: LinearColor) -> None
```

## `unreal.MaterialExpressionConstantDouble(MaterialExpressionGenericConstant)`

```python
unreal.MaterialExpressionConstantDouble.value(value: float) -> None
```

## `unreal.MaterialExpressionFunctionInput(MaterialExpression)`

```python
unreal.MaterialExpressionFunctionInput.input_name(value: Name) -> None
unreal.MaterialExpressionFunctionInput.input_type(value: FunctionInputType) -> None
unreal.MaterialExpressionFunctionInput.preview_value(value: Vector4f) -> None
unreal.MaterialExpressionFunctionInput.sort_priority(value: int) -> None
unreal.MaterialExpressionFunctionInput.use_preview_value_as_default(value: bool) -> None
```

## `unreal.MaterialExpressionFunctionOutput(MaterialExpression)`

```python
unreal.MaterialExpressionFunctionOutput.output_name(value: Name) -> None
```

## `unreal.MaterialExpressionMaterialFunctionCall(MaterialExpression)`

```python
unreal.MaterialExpressionMaterialFunctionCall.set_material_function(new_material_function: MaterialFunctionInterface) -> bool
```

## `unreal.MaterialExpressionSkyAtmosphereLightDirection(MaterialExpression)`

```python
unreal.MaterialExpressionSkyAtmosphereLightDirection.light_index(value: int) -> None
```

## `unreal.MaterialExpressionSkyAtmosphereLightDiskLuminance(MaterialExpression)`

```python
unreal.MaterialExpressionSkyAtmosphereLightDiskLuminance.light_index(value: int) -> None
```

## `unreal.MaterialExpressionSkyAtmosphereLightIlluminance(MaterialExpression)`

```python
unreal.MaterialExpressionSkyAtmosphereLightIlluminance.light_index(value: int) -> None
```

## `unreal.MaterialExpressionSkyAtmosphereLightIlluminanceOnGround(MaterialExpression)`

```python
unreal.MaterialExpressionSkyAtmosphereLightIlluminanceOnGround.light_index(value: int) -> None
```

## `unreal.MaterialExpressionSparseVolumeTextureBase(MaterialExpression)`

```python
unreal.MaterialExpressionSparseVolumeTextureBase.sparse_volume_texture(value: SparseVolumeTexture) -> None
```

## `unreal.MaterialExpressionSubstrateConvertMaterialAttributes(MaterialExpressionSubstrateBSDF)`

```python
unreal.MaterialExpressionSubstrateConvertMaterialAttributes.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialExpressionSubstrateEyeBSDF(MaterialExpressionSubstrateBSDF)`

```python
unreal.MaterialExpressionSubstrateEyeBSDF.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialExpressionSubstrateShadingModels(MaterialExpressionSubstrateBSDF)`

```python
unreal.MaterialExpressionSubstrateShadingModels.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialExpressionSubstrateSlabBSDF(MaterialExpressionSubstrateBSDF)`

```python
unreal.MaterialExpressionSubstrateSlabBSDF.specular_profile() -> SpecularProfile
unreal.MaterialExpressionSubstrateSlabBSDF.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialExpressionTextureBase(MaterialExpression)`

```python
unreal.MaterialExpressionTextureBase.sampler_type(value: MaterialSamplerType) -> None
unreal.MaterialExpressionTextureBase.texture(value: Texture) -> None
```

## `unreal.MaterialExpressionTextureCollection(MaterialExpression)`

```python
unreal.MaterialExpressionTextureCollection.texture_collection(value: TextureCollection) -> None
```

## `unreal.MaterialExpressionTextureCoordinate(MaterialExpression)`

```python
unreal.MaterialExpressionTextureCoordinate.coordinate_index(value: int) -> None
unreal.MaterialExpressionTextureCoordinate.u_tiling(value: float) -> None
unreal.MaterialExpressionTextureCoordinate.v_tiling(value: float) -> None
```

## `unreal.MaterialExpressionTextureObjectFromCollection(MaterialExpression)`

```python
unreal.MaterialExpressionTextureObjectFromCollection.const_collection_index(value: int) -> None
unreal.MaterialExpressionTextureObjectFromCollection.texture_collection_object(value: TextureCollection) -> None
unreal.MaterialExpressionTextureObjectFromCollection.texture_type(value: TextureCollectionMemberType) -> None
```

## `unreal.MaterialFunctionInstance(MaterialFunctionInterface)`

```python
unreal.MaterialFunctionInstance.parent() -> MaterialFunctionInterface
```

## `unreal.MaterialImportHelpers(Object)`

```python
unreal.MaterialImportHelpers.find_existing_material(base_path: str, material_full_name: str, recursive_paths: bool) -> Tuple[MaterialInterface, Text]
unreal.MaterialImportHelpers.find_existing_material_from_search_location(material_full_name: str, base_package_path: str, search_location: MaterialSearchLocation) -> Tuple[MaterialInterface, Text]
```

## `unreal.MaterialInstance(MaterialInterface)`

```python
unreal.MaterialInstance.blendable_location_override(value: BlendableLocation) -> None
unreal.MaterialInstance.blendable_priority_override(value: int) -> None
unreal.MaterialInstance.double_vector_parameter_values() -> Array[DoubleVectorParameterValue]
unreal.MaterialInstance.font_parameter_values() -> Array[FontParameterValue]
unreal.MaterialInstance.override_blendable_location(value: bool) -> None
unreal.MaterialInstance.override_blendable_priority(value: bool) -> None
unreal.MaterialInstance.override_subsurface_profile() -> bool
unreal.MaterialInstance.parent() -> MaterialInterface
unreal.MaterialInstance.phys_material(value: PhysicalMaterial) -> None
unreal.MaterialInstance.runtime_virtual_texture_parameter_values() -> Array[RuntimeVirtualTextureParameterValue]
unreal.MaterialInstance.scalar_parameter_values() -> Array[ScalarParameterValue]
unreal.MaterialInstance.sparse_volume_texture_parameter_values() -> Array[SparseVolumeTextureParameterValue]
unreal.MaterialInstance.texture_collection_parameter_values() -> Array[TextureCollectionParameterValue]
unreal.MaterialInstance.texture_parameter_values() -> Array[TextureParameterValue]
unreal.MaterialInstance.vector_parameter_values() -> Array[VectorParameterValue]
```

## `unreal.MaterialInstanceBasePropertyOverrides(StructBase)`

```python
unreal.MaterialInstanceBasePropertyOverrides.__init__() -> None
```

## `unreal.MaterialInstanceConstant(MaterialInstance)`

```python
unreal.MaterialInstanceConstant.get_scalar_parameter_value(parameter_name: Name) -> float
unreal.MaterialInstanceConstant.get_texture_parameter_value(parameter_name: Name) -> Texture
unreal.MaterialInstanceConstant.get_vector_parameter_value(parameter_name: Name) -> LinearColor
unreal.MaterialInstanceConstant.set_nanite_override_material(enable_override: bool, override_material: MaterialInterface) -> None
```

## `unreal.MaterialInstanceDynamic(MaterialInstance)`

```python
unreal.MaterialInstanceDynamic.copy_material_instance_parameters(source: MaterialInterface, quick_parameters_only: bool = False) -> None
unreal.MaterialInstanceDynamic.copy_parameter_overrides(material_instance: MaterialInstance) -> None
unreal.MaterialInstanceDynamic.get_scalar_parameter_value(parameter_name: Name) -> float
unreal.MaterialInstanceDynamic.get_scalar_parameter_value_by_info(parameter_info: MaterialParameterInfo) -> float
unreal.MaterialInstanceDynamic.get_texture_parameter_value(parameter_name: Name) -> Texture
unreal.MaterialInstanceDynamic.get_texture_parameter_value_by_info(parameter_info: MaterialParameterInfo) -> Texture
unreal.MaterialInstanceDynamic.get_vector_parameter_value(parameter_name: Name) -> LinearColor
unreal.MaterialInstanceDynamic.get_vector_parameter_value_by_info(parameter_info: MaterialParameterInfo) -> LinearColor
unreal.MaterialInstanceDynamic.initialize_scalar_parameter_and_get_index(parameter_name: Name, value: float) -> Optional[int]
unreal.MaterialInstanceDynamic.interpolate_material_instance_parameters(source_a: MaterialInstance, source_b: MaterialInstance, alpha: float) -> None
unreal.MaterialInstanceDynamic.set_double_vector_parameter_value(parameter_name: Name, value: Vector4) -> None
unreal.MaterialInstanceDynamic.set_runtime_virtual_texture_parameter_value(parameter_name: Name, value: RuntimeVirtualTexture) -> None
unreal.MaterialInstanceDynamic.set_runtime_virtual_texture_parameter_value_by_info(parameter_info: MaterialParameterInfo, value: RuntimeVirtualTexture) -> None
unreal.MaterialInstanceDynamic.set_scalar_parameter_by_index(parameter_index: int, value: float) -> bool
unreal.MaterialInstanceDynamic.set_scalar_parameter_value(parameter_name: Name, value: float) -> None
unreal.MaterialInstanceDynamic.set_scalar_parameter_value_by_info(parameter_info: MaterialParameterInfo, value: float) -> None
unreal.MaterialInstanceDynamic.set_sparse_volume_texture_parameter_value(parameter_name: Name, value: SparseVolumeTexture) -> None
unreal.MaterialInstanceDynamic.set_texture_parameter_value(parameter_name: Name, value: Texture) -> None
unreal.MaterialInstanceDynamic.set_texture_parameter_value_by_info(parameter_info: MaterialParameterInfo, value: Texture) -> None
unreal.MaterialInstanceDynamic.set_vector_parameter_value(parameter_name: Name, value: LinearColor) -> None
unreal.MaterialInstanceDynamic.set_vector_parameter_value_by_info(parameter_info: MaterialParameterInfo, value: LinearColor) -> None
```

## `unreal.MaterialInstanceParams(StructBase)`

```python
unreal.MaterialInstanceParams.__init__(uv_control: WdpJsonObjectWrapper = [], material_channel_control: WdpJsonObjectWrapper = []) -> None
unreal.MaterialInstanceParams.material_channel_control(value: WdpJsonObjectWrapper) -> None
unreal.MaterialInstanceParams.uv_control(value: WdpJsonObjectWrapper) -> None
```

## `unreal.MaterialInterface(Object)`

```python
unreal.MaterialInterface.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.MaterialInterface.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.MaterialInterface.get_base_material() -> Material
unreal.MaterialInterface.get_blend_mode() -> BlendMode
unreal.MaterialInterface.get_nanite_overide_material() -> MaterialInterface
unreal.MaterialInterface.get_parameter_info(association: MaterialParameterAssociation, parameter_name: Name, layer_function: MaterialFunctionInterface) -> MaterialParameterInfo
unreal.MaterialInterface.get_physical_material() -> PhysicalMaterial
unreal.MaterialInterface.get_physical_material_from_map(index: int) -> PhysicalMaterial
unreal.MaterialInterface.get_physical_material_mask() -> PhysicalMaterialMask
unreal.MaterialInterface.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.MaterialInterface.neural_profile() -> NeuralProfile
unreal.MaterialInterface.set_force_mip_levels_to_be_resident(override_force_miplevels_to_be_resident: bool, force_miplevels_to_be_resident_value: bool, force_duration: float, cinematic_texture_groups: int = 0, fast_response: bool = False) -> None
unreal.MaterialInterface.subsurface_profile() -> SubsurfaceProfile
```

## `unreal.MaterialLayersFunctions(MaterialLayersFunctionsRuntimeData)`

```python
unreal.MaterialLayersFunctions.__init__() -> None
```

## `unreal.MaterialLayersFunctionsEditorOnlyData(StructBase)`

```python
unreal.MaterialLayersFunctionsEditorOnlyData.__init__() -> None
```

## `unreal.MaterialLayersFunctionsRuntimeData(StructBase)`

```python
unreal.MaterialLayersFunctionsRuntimeData.__init__() -> None
```

## `unreal.MaterialLibrary(BlueprintFunctionLibrary)`

```python
unreal.MaterialLibrary.create_dynamic_material_instance(world_context_object: Object, parent: MaterialInterface, optional_name: Name = "None", creation_flags: MIDCreationFlags = MIDCreationFlags.NONE) -> MaterialInstanceDynamic
unreal.MaterialLibrary.create_material_instance_dynamic(world_context_object: Object, parent: MaterialInterface, optional_name: Name = "None", creation_flags: MIDCreationFlags = MIDCreationFlags.NONE) -> MaterialInstanceDynamic
unreal.MaterialLibrary.get_scalar_parameter_value(world_context_object: Object, collection: MaterialParameterCollection, parameter_name: Name) -> float
unreal.MaterialLibrary.get_vector_parameter_value(world_context_object: Object, collection: MaterialParameterCollection, parameter_name: Name) -> LinearColor
unreal.MaterialLibrary.set_scalar_parameter_value(world_context_object: Object, collection: MaterialParameterCollection, parameter_name: Name, parameter_value: float) -> None
unreal.MaterialLibrary.set_vector_parameter_value(world_context_object: Object, collection: MaterialParameterCollection, parameter_name: Name, parameter_value: LinearColor) -> None
```

## `unreal.MaterialMergeOptions(Object)`

```python
unreal.MaterialMergeOptions.blend_mode(value: BlendMode) -> None
```

## `unreal.MaterialOptions(Object)`

```python
unreal.MaterialOptions.lod_indices(value: Array[int]) -> None
unreal.MaterialOptions.properties(value: Array[PropertyEntry]) -> None
unreal.MaterialOptions.texture_coordinate_index(value: int) -> None
unreal.MaterialOptions.texture_size(value: IntPoint) -> None
unreal.MaterialOptions.use_mesh_data(value: bool) -> None
unreal.MaterialOptions.use_specific_uv_index(value: bool) -> None
```

## `unreal.MaterialOverrideNanite(StructBase)`

```python
unreal.MaterialOverrideNanite.__init__() -> None
```

## `unreal.MaterialPairData(StructBase)`

```python
unreal.MaterialPairData.__init__() -> None
```

## `unreal.MaterialParameterCollection(Object)`

```python
unreal.MaterialParameterCollection.get_scalar_parameter_default_value(parameter_name: Name) -> Tuple[float, bool]
unreal.MaterialParameterCollection.get_scalar_parameter_names() -> Array[Name]
unreal.MaterialParameterCollection.get_vector_parameter_default_value(parameter_name: Name) -> Tuple[LinearColor, bool]
unreal.MaterialParameterCollection.get_vector_parameter_names() -> Array[Name]
```

## `unreal.MaterialParameterInfo(StructBase)`

```python
unreal.MaterialParameterInfo.__init__(name: Name = "None", association: MaterialParameterAssociation = MaterialParameterAssociation.LAYER_PARAMETER, index: int = 0) -> None
unreal.MaterialParameterInfo.association(value: MaterialParameterAssociation) -> None
unreal.MaterialParameterInfo.index(value: int) -> None
unreal.MaterialParameterInfo.name(value: Name) -> None
```

## `unreal.MaterialProxySettings(StructBase)`

```python
unreal.MaterialProxySettings.__init__(texture_sizing_type: TextureSizingType = TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE, target_texel_density_per_meter: float = 0.000000, mesh_max_screen_size_percent: float = 0.000000, mesh_min_draw_distance: float = 0.000000, gutter_space: float = 0.000000, metallic_constant: float = 0.000000, roughness_constant: float = 0.000000, anisotropy_constant: float = 0.000000, specular_constant: float = 0.000000, opacity_constant: float = 0.000000, opacity_mask_constant: float = 0.000000, ambient_occlusion_constant: float = 0.000000, blend_mode: BlendMode = BlendMode.BLEND_OPAQUE, allow_two_sided_material: bool = False, normal_map: bool = False, tangent_map: bool = False, metallic_map: bool = False, roughness_map: bool = False, anisotropy_map: bool = False, specular_map: bool = False, emissive_map: bool = False, opacity_map: bool = False, opacity_mask_map: bool = False, ambient_occlusion_map: bool = False, diffuse_texture_size: IntPoint = [0, 0], normal_texture_size: IntPoint = [0, 0], tangent_texture_size: IntPoint = [0, 0], metallic_texture_size: IntPoint = [0, 0], roughness_texture_size: IntPoint = [0, 0], anisotropy_texture_size: IntPoint = [0, 0], specular_texture_size: IntPoint = [0, 0], emissive_texture_size: IntPoint = [0, 0], opacity_texture_size: IntPoint = [0, 0], opacity_mask_texture_size: IntPoint = [0, 0], ambient_occlusion_texture_size: IntPoint = [0, 0]) -> None
unreal.MaterialProxySettings.allow_two_sided_material(value: bool) -> None
unreal.MaterialProxySettings.ambient_occlusion_constant(value: float) -> None
unreal.MaterialProxySettings.ambient_occlusion_map(value: bool) -> None
unreal.MaterialProxySettings.ambient_occlusion_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.anisotropy_constant(value: float) -> None
unreal.MaterialProxySettings.anisotropy_map(value: bool) -> None
unreal.MaterialProxySettings.anisotropy_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.blend_mode(value: BlendMode) -> None
unreal.MaterialProxySettings.diffuse_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.emissive_map(value: bool) -> None
unreal.MaterialProxySettings.emissive_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.gutter_space(value: float) -> None
unreal.MaterialProxySettings.mesh_max_screen_size_percent(value: float) -> None
unreal.MaterialProxySettings.mesh_min_draw_distance(value: float) -> None
unreal.MaterialProxySettings.metallic_constant(value: float) -> None
unreal.MaterialProxySettings.metallic_map(value: bool) -> None
unreal.MaterialProxySettings.metallic_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.normal_map(value: bool) -> None
unreal.MaterialProxySettings.normal_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.opacity_constant(value: float) -> None
unreal.MaterialProxySettings.opacity_map(value: bool) -> None
unreal.MaterialProxySettings.opacity_mask_constant(value: float) -> None
unreal.MaterialProxySettings.opacity_mask_map(value: bool) -> None
unreal.MaterialProxySettings.opacity_mask_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.opacity_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.roughness_constant(value: float) -> None
unreal.MaterialProxySettings.roughness_map(value: bool) -> None
unreal.MaterialProxySettings.roughness_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.specular_constant(value: float) -> None
unreal.MaterialProxySettings.specular_map(value: bool) -> None
unreal.MaterialProxySettings.specular_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.tangent_map(value: bool) -> None
unreal.MaterialProxySettings.tangent_texture_size(value: IntPoint) -> None
unreal.MaterialProxySettings.target_texel_density_per_meter(value: float) -> None
unreal.MaterialProxySettings.texture_sizing_type(value: TextureSizingType) -> None
```

## `unreal.MaterialSpriteElement(StructBase)`

```python
unreal.MaterialSpriteElement.__init__(material: MaterialInterface = None, distance_to_opacity_curve: CurveFloat = None, size_is_in_screen_space: bool = False, base_size_x: float = 0.000000, base_size_y: float = 0.000000, distance_to_size_curve: CurveFloat = None) -> None
unreal.MaterialSpriteElement.base_size_x(value: float) -> None
unreal.MaterialSpriteElement.base_size_y(value: float) -> None
unreal.MaterialSpriteElement.distance_to_opacity_curve(value: CurveFloat) -> None
unreal.MaterialSpriteElement.distance_to_size_curve(value: CurveFloat) -> None
unreal.MaterialSpriteElement.material(value: MaterialInterface) -> None
unreal.MaterialSpriteElement.size_is_in_screen_space(value: bool) -> None
```

## `unreal.MaterialStatistics(StructBase)`

```python
unreal.MaterialStatistics.__init__(num_vertex_shader_instructions: int = 0, num_pixel_shader_instructions: int = 0, num_samplers: int = 0, num_vertex_texture_samples: int = 0, num_pixel_texture_samples: int = 0, num_virtual_texture_samples: int = 0, num_uv_scalars: int = 0, num_interpolator_scalars: int = 0) -> None
unreal.MaterialStatistics.num_interpolator_scalars(value: int) -> None
unreal.MaterialStatistics.num_pixel_shader_instructions(value: int) -> None
unreal.MaterialStatistics.num_pixel_texture_samples(value: int) -> None
unreal.MaterialStatistics.num_samplers(value: int) -> None
unreal.MaterialStatistics.num_uv_scalars(value: int) -> None
unreal.MaterialStatistics.num_vertex_shader_instructions(value: int) -> None
unreal.MaterialStatistics.num_vertex_texture_samples(value: int) -> None
unreal.MaterialStatistics.num_virtual_texture_samples(value: int) -> None
```

## `unreal.MaterialToolAPI(StandardApiClassBase)`

```python
unreal.MaterialToolAPI.apply_material_to_entity(params: ApplyMaterialToEntityParams) -> Optional[ResultBase]
unreal.MaterialToolAPI.get_entity_material_slots(params: EidArrayParams) -> Optional[GetEntityMaterialSlotsResult]
unreal.MaterialToolAPI.set_entity_slots_highlight(params: EntitySlotParamsArr) -> Optional[ResultBase]
```

## `unreal.MediaTexture(Texture)`

```python
unreal.MediaTexture.address_x(value: TextureAddress) -> None
unreal.MediaTexture.address_y(value: TextureAddress) -> None
unreal.MediaTexture.auto_clear(value: bool) -> None
unreal.MediaTexture.clear_color(value: LinearColor) -> None
unreal.MediaTexture.current_aspect_ratio() -> float
unreal.MediaTexture.current_orientation() -> MediaTextureOrientation
unreal.MediaTexture.enable_gen_mips() -> bool
unreal.MediaTexture.get_aspect_ratio() -> float
unreal.MediaTexture.get_height() -> int
unreal.MediaTexture.get_media_player() -> MediaPlayer
unreal.MediaTexture.get_texture_num_mips() -> int
unreal.MediaTexture.get_width() -> int
unreal.MediaTexture.new_style_output(value: bool) -> None
unreal.MediaTexture.num_mips(value: int) -> None
unreal.MediaTexture.output_format(value: MediaTextureOutputFormat) -> None
unreal.MediaTexture.set_media_player(new_media_player: MediaPlayer) -> None
unreal.MediaTexture.update_resource() -> None
```

## `unreal.MediaTextureResourceSettings(StructBase)`

```python
unreal.MediaTextureResourceSettings.__init__() -> None
```

## `unreal.MeshNaniteSettings(StructBase)`

```python
unreal.MeshNaniteSettings.__init__(enabled: bool = False, preserve_area: bool = False, explicit_tangents: bool = False, lerp_u_vs: bool = False, position_precision: int = 0, normal_precision: int = 0, tangent_precision: int = 0, keep_percent_triangles: float = 0.000000, trim_relative_error: float = 0.000000, fallback_target: NaniteFallbackTarget = NaniteFallbackTarget.AUTO, fallback_percent_triangles: float = 0.000000, fallback_relative_error: float = 0.000000, max_edge_length_factor: float = 0.000000, displacement_uv_channel: int = 0) -> None
unreal.MeshNaniteSettings.displacement_uv_channel(value: int) -> None
unreal.MeshNaniteSettings.enabled(value: bool) -> None
unreal.MeshNaniteSettings.explicit_tangents(value: bool) -> None
unreal.MeshNaniteSettings.fallback_percent_triangles(value: float) -> None
unreal.MeshNaniteSettings.fallback_relative_error(value: float) -> None
unreal.MeshNaniteSettings.fallback_target(value: NaniteFallbackTarget) -> None
unreal.MeshNaniteSettings.keep_percent_triangles(value: float) -> None
unreal.MeshNaniteSettings.lerp_u_vs(value: bool) -> None
unreal.MeshNaniteSettings.max_edge_length_factor(value: float) -> None
unreal.MeshNaniteSettings.normal_precision(value: int) -> None
unreal.MeshNaniteSettings.position_precision(value: int) -> None
unreal.MeshNaniteSettings.preserve_area(value: bool) -> None
unreal.MeshNaniteSettings.tangent_precision(value: int) -> None
unreal.MeshNaniteSettings.trim_relative_error(value: float) -> None
```

## `unreal.ModelerRenderInfo(StructBase)`

```python
unreal.ModelerRenderInfo.__init__(build_resource: UrbanSceneBuildResource = None, static_mesh_components: Array[StaticMeshComponent] = [], instanced_static_mesh_components: Array[InstancedStaticMeshComponent] = [], static_mesh_nodes: Array[UrbanSceneNode_StaticMesh] = [], resource_data_nodes: Array[UrbanSceneNode_ResourceData] = [], eid_data: str = "") -> None
unreal.ModelerRenderInfo.build_resource(value: UrbanSceneBuildResource) -> None
unreal.ModelerRenderInfo.eid_data(value: str) -> None
unreal.ModelerRenderInfo.instanced_static_mesh_components(value: Array[InstancedStaticMeshComponent]) -> None
unreal.ModelerRenderInfo.resource_data_nodes(value: Array[UrbanSceneNode_ResourceData]) -> None
unreal.ModelerRenderInfo.static_mesh_components(value: Array[StaticMeshComponent]) -> None
unreal.ModelerRenderInfo.static_mesh_nodes(value: Array[UrbanSceneNode_StaticMesh]) -> None
```

## `unreal.MovieSceneComponentMaterialParameterSection(MovieSceneSection)`

```python
unreal.MovieSceneComponentMaterialParameterSection.add_color_parameter_key(parameter_info: MaterialParameterInfo, time: FrameNumber, value: LinearColor, layer_name: str, asset_name: str, channel_names: ParameterChannelNames = []) -> None
unreal.MovieSceneComponentMaterialParameterSection.add_scalar_parameter_key(parameter_info: MaterialParameterInfo, time: FrameNumber, value: float, layer_name: str, asset_name: str) -> None
unreal.MovieSceneComponentMaterialParameterSection.remove_color_parameter(parameter_info: MaterialParameterInfo) -> bool
unreal.MovieSceneComponentMaterialParameterSection.remove_scalar_parameter(parameter_info: MaterialParameterInfo) -> bool
```

## `unreal.MovieSceneComponentMaterialTrack(MovieSceneMaterialTrack)`

```python
unreal.MovieSceneComponentMaterialTrack.get_material_index() -> int
unreal.MovieSceneComponentMaterialTrack.get_material_info() -> ComponentMaterialInfo
unreal.MovieSceneComponentMaterialTrack.material_index(value: int) -> None
unreal.MovieSceneComponentMaterialTrack.set_material_index(material_index: int) -> None
unreal.MovieSceneComponentMaterialTrack.set_material_info(material_info: ComponentMaterialInfo) -> None
```

## `unreal.MovieSceneMaterialTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieSceneMaterialTrackExtensions.get_material_index(track: MovieSceneComponentMaterialTrack) -> int
unreal.MovieSceneMaterialTrackExtensions.get_material_info(track: MovieSceneComponentMaterialTrack) -> ComponentMaterialInfo
unreal.MovieSceneMaterialTrackExtensions.set_material_index(track: MovieSceneComponentMaterialTrack, material_index: int) -> None
unreal.MovieSceneMaterialTrackExtensions.set_material_info(track: MovieSceneComponentMaterialTrack, material_info: ComponentMaterialInfo) -> None
```

## `unreal.MovieSceneNiagaraCacheParams(MovieSceneBaseCacheParams)`

```python
unreal.MovieSceneNiagaraCacheParams.__init__() -> None
```

## `unreal.MovieScenePrimitiveMaterialTrack(MovieScenePropertyTrack)`

```python
unreal.MovieScenePrimitiveMaterialTrack.get_material_index() -> int
unreal.MovieScenePrimitiveMaterialTrack.get_material_info() -> ComponentMaterialInfo
unreal.MovieScenePrimitiveMaterialTrack.set_material_index(material_index: int) -> None
unreal.MovieScenePrimitiveMaterialTrack.set_material_info(material_info: ComponentMaterialInfo) -> None
```

## `unreal.MovieScenePrimitiveMaterialTrackExtensions(BlueprintFunctionLibrary)`

```python
unreal.MovieScenePrimitiveMaterialTrackExtensions.get_material_index(track: MovieScenePrimitiveMaterialTrack) -> int
unreal.MovieScenePrimitiveMaterialTrackExtensions.get_material_info(track: MovieScenePrimitiveMaterialTrack) -> ComponentMaterialInfo
unreal.MovieScenePrimitiveMaterialTrackExtensions.set_material_index(track: MovieScenePrimitiveMaterialTrack, material_index: int) -> None
unreal.MovieScenePrimitiveMaterialTrackExtensions.set_material_info(track: MovieScenePrimitiveMaterialTrack, material_info: ComponentMaterialInfo) -> None
```

## `unreal.NDIStaticMeshSectionFilter(StructBase)`

```python
unreal.NDIStaticMeshSectionFilter.__init__() -> None
```

## `unreal.NamedEmitterMaterial(StructBase)`

```python
unreal.NamedEmitterMaterial.__init__() -> None
```

## `unreal.NaniteSettings(StructBase)`

```python
unreal.NaniteSettings.__init__() -> None
```

## `unreal.NewMaterialsInfo(StructBase)`

```python
unreal.NewMaterialsInfo.__init__() -> None
```

## `unreal.NewMaterialsInfoArray(ParamsBase)`

```python
unreal.NewMaterialsInfoArray.__init__(new_materials_info: Array[NewMaterialsInfo] = []) -> None
unreal.NewMaterialsInfoArray.new_materials_info(value: Array[NewMaterialsInfo]) -> None
```

## `unreal.NiagaraBaselineController(Object)`

```python
unreal.NiagaraBaselineController.effect_type() -> NiagaraEffectType
unreal.NiagaraBaselineController.get_system() -> NiagaraSystem
unreal.NiagaraBaselineController.on_begin_test() -> None
unreal.NiagaraBaselineController.on_end_test(stats: NiagaraPerfBaselineStats) -> None
unreal.NiagaraBaselineController.on_owner_tick(delta_time: float) -> None
unreal.NiagaraBaselineController.on_tick_test() -> bool
unreal.NiagaraBaselineController.owner() -> NiagaraPerfBaselineActor
unreal.NiagaraBaselineController.test_duration(value: float) -> None
```

## `unreal.NiagaraClipboardEditorScriptingUtilities(Object)`

```python
unreal.NiagaraClipboardEditorScriptingUtilities.create_bool_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, bool_value: bool) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_data_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, data_value: NiagaraDataInterface) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_dynamic_value_input(outer: Object, input_name: Name, input_type_name: Name, has_edit_condition: bool, edit_condition_value: bool, dynamic_value_name: str, dynamic_value: NiagaraScript) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_enum_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_codition_value: bool, enum_type: UserDefinedEnum, enum_value: int) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_expression_value_input(outer: Object, input_name: Name, input_type_name: Name, has_edit_condition: bool, edit_condition_value: bool, expression_value: str) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_float_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, local_value: float) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_int_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, local_value: int) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_linked_value_input(outer: Object, input_name: Name, input_type_name: Name, has_edit_condition: bool, edit_condition_value: bool, linked_value: Name) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_struct_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, struct_value: UserDefinedStruct) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_vec2_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, vec2_value: Vector2D) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.create_vec3_local_value_input(outer: Object, input_name: Name, has_edit_condition: bool, edit_condition_value: bool, vec3_value: Vector) -> NiagaraClipboardFunctionInput
unreal.NiagaraClipboardEditorScriptingUtilities.get_type_name(input: NiagaraClipboardFunctionInput) -> Name
unreal.NiagaraClipboardEditorScriptingUtilities.try_get_input_by_name(inputs: Array[NiagaraClipboardFunctionInput], input_name: Name) -> Tuple[bool, NiagaraClipboardFunctionInput]
unreal.NiagaraClipboardEditorScriptingUtilities.try_get_local_value_as_float(input: NiagaraClipboardFunctionInput) -> Tuple[bool, float]
unreal.NiagaraClipboardEditorScriptingUtilities.try_get_local_value_as_int(input: NiagaraClipboardFunctionInput) -> Tuple[bool, int]
unreal.NiagaraClipboardEditorScriptingUtilities.try_set_local_value_as_int(input: NiagaraClipboardFunctionInput, value: int, loose_typing: bool = True) -> bool
```

## `unreal.NiagaraClipboardFunction_OnPastedFunctionCallNode(DelegateBase)`

```python
unreal.NiagaraClipboardFunction_OnPastedFunctionCallNode.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.NiagaraComponent(FXSystemComponent)`

```python
unreal.NiagaraComponent.advance_simulation(tick_count: int, tick_delta_seconds: float) -> None
unreal.NiagaraComponent.advance_simulation_by_time(simulate_time: float, tick_delta_seconds: float) -> None
unreal.NiagaraComponent.allow_scalability(value: bool) -> None
unreal.NiagaraComponent.auto_attach_location_rule(value: AttachmentRule) -> None
unreal.NiagaraComponent.auto_attach_parent() -> SceneComponent
unreal.NiagaraComponent.auto_attach_rotation_rule(value: AttachmentRule) -> None
unreal.NiagaraComponent.auto_attach_scale_rule(value: AttachmentRule) -> None
unreal.NiagaraComponent.auto_attach_socket_name(value: Name) -> None
unreal.NiagaraComponent.auto_attach_weld_simulated_bodies(value: bool) -> None
unreal.NiagaraComponent.auto_manage_attachment() -> bool
unreal.NiagaraComponent.clear_emitter_fixed_bounds(emitter_name: Name) -> None
unreal.NiagaraComponent.clear_sim_cache(reset_system: bool = False) -> None
unreal.NiagaraComponent.clear_system_fixed_bounds() -> None
unreal.NiagaraComponent.get_age_update_mode() -> NiagaraAgeUpdateMode
unreal.NiagaraComponent.get_asset() -> NiagaraSystem
unreal.NiagaraComponent.get_custom_time_dilation() -> float
unreal.NiagaraComponent.get_data_interface(name: str) -> NiagaraDataInterface
unreal.NiagaraComponent.get_desired_age() -> float
unreal.NiagaraComponent.get_emitter_fixed_bounds(emitter_name: Name) -> Box
unreal.NiagaraComponent.get_force_solo() -> bool
unreal.NiagaraComponent.get_lock_desired_age_delta_time_to_seek_delta() -> bool
unreal.NiagaraComponent.get_max_sim_time() -> float
unreal.NiagaraComponent.get_occlusion_query_mode() -> NiagaraOcclusionQueryMode
unreal.NiagaraComponent.get_preview_lod_distance() -> float
unreal.NiagaraComponent.get_preview_lod_distance_enabled() -> bool
unreal.NiagaraComponent.get_random_seed_offset() -> int
unreal.NiagaraComponent.get_seek_delta() -> float
unreal.NiagaraComponent.get_sim_cache() -> NiagaraSimCache
unreal.NiagaraComponent.get_system_fixed_bounds() -> Box
unreal.NiagaraComponent.get_tick_behavior() -> NiagaraTickBehavior
unreal.NiagaraComponent.init_for_performance_baseline() -> None
unreal.NiagaraComponent.is_paused() -> bool
unreal.NiagaraComponent.occlusion_query_mode() -> NiagaraOcclusionQueryMode
unreal.NiagaraComponent.on_system_finished(value: OnNiagaraSystemFinished) -> None
unreal.NiagaraComponent.reinitialize_system() -> None
unreal.NiagaraComponent.reset_system() -> None
unreal.NiagaraComponent.seek_to_desired_age(desired_age: float) -> None
unreal.NiagaraComponent.set_age_update_mode(age_update_mode: NiagaraAgeUpdateMode) -> None
unreal.NiagaraComponent.set_asset(asset: NiagaraSystem, reset_existing_override_parameters: bool = True) -> None
unreal.NiagaraComponent.set_auto_destroy(auto_destroy: bool) -> None
unreal.NiagaraComponent.set_can_render_while_seeking(can_render_while_seeking: bool) -> None
unreal.NiagaraComponent.set_custom_time_dilation(dilation: float = 1.000000) -> None
unreal.NiagaraComponent.set_desired_age(desired_age: float) -> None
unreal.NiagaraComponent.set_emitter_fixed_bounds(emitter_name: Name, local_bounds: Box) -> None
unreal.NiagaraComponent.set_force_solo(force_solo: bool) -> None
unreal.NiagaraComponent.set_gpu_compute_debug(enable_debug: bool) -> None
unreal.NiagaraComponent.set_lock_desired_age_delta_time_to_seek_delta(lock: bool) -> None
unreal.NiagaraComponent.set_max_sim_time(max_time: float) -> None
unreal.NiagaraComponent.set_niagara_variable_actor(variable_name: str, actor: Actor) -> None
unreal.NiagaraComponent.set_niagara_variable_bool(variable_name: str, value: bool) -> None
unreal.NiagaraComponent.set_niagara_variable_float(variable_name: str, value: float) -> None
unreal.NiagaraComponent.set_niagara_variable_int(variable_name: str, value: int) -> None
unreal.NiagaraComponent.set_niagara_variable_linear_color(variable_name: str, value: LinearColor) -> None
unreal.NiagaraComponent.set_niagara_variable_matrix(variable_name: str, value: Matrix) -> None
unreal.NiagaraComponent.set_niagara_variable_object(variable_name: str, object: Object) -> None
unreal.NiagaraComponent.set_niagara_variable_position(variable_name: str, value: Vector) -> None
unreal.NiagaraComponent.set_niagara_variable_quat(variable_name: str, value: Quat) -> None
unreal.NiagaraComponent.set_niagara_variable_vec2(variable_name: str, value: Vector2D) -> None
unreal.NiagaraComponent.set_niagara_variable_vec3(variable_name: str, value: Vector) -> None
unreal.NiagaraComponent.set_niagara_variable_vec4(variable_name: str, value: Vector4) -> None
unreal.NiagaraComponent.set_occlusion_query_mode(mode: NiagaraOcclusionQueryMode) -> None
unreal.NiagaraComponent.set_paused(paused: bool) -> None
unreal.NiagaraComponent.set_preview_lod_distance(enable_preview_lod_distance: bool, preview_lod_distance: float, preview_max_distance: float) -> None
unreal.NiagaraComponent.set_random_seed_offset(new_random_seed_offset: int) -> None
unreal.NiagaraComponent.set_rendering_enabled(rendering_enabled: bool) -> None
unreal.NiagaraComponent.set_seek_delta(seek_delta: float) -> None
unreal.NiagaraComponent.set_sim_cache(sim_cache: NiagaraSimCache, reset_system: bool = False) -> None
unreal.NiagaraComponent.set_system_fixed_bounds(local_bounds: Box) -> None
unreal.NiagaraComponent.set_tick_behavior(new_tick_behavior: NiagaraTickBehavior) -> None
unreal.NiagaraComponent.set_variable_actor(variable_name: Name, actor: Actor) -> None
unreal.NiagaraComponent.set_variable_bool(variable_name: Name, value: bool) -> None
unreal.NiagaraComponent.set_variable_float(variable_name: Name, value: float) -> None
unreal.NiagaraComponent.set_variable_int(variable_name: Name, value: int) -> None
unreal.NiagaraComponent.set_variable_linear_color(variable_name: Name, value: LinearColor) -> None
unreal.NiagaraComponent.set_variable_material(variable_name: Name, object: MaterialInterface) -> None
unreal.NiagaraComponent.set_variable_matrix(variable_name: Name, value: Matrix) -> None
unreal.NiagaraComponent.set_variable_object(variable_name: Name, object: Object) -> None
unreal.NiagaraComponent.set_variable_position(variable_name: Name, value: Vector) -> None
unreal.NiagaraComponent.set_variable_quat(variable_name: Name, value: Quat) -> None
unreal.NiagaraComponent.set_variable_static_mesh(variable_name: Name, value: StaticMesh) -> None
unreal.NiagaraComponent.set_variable_texture(variable_name: Name, texture: Texture) -> None
unreal.NiagaraComponent.set_variable_texture_render_target(variable_name: Name, texture_render_target: TextureRenderTarget) -> None
unreal.NiagaraComponent.set_variable_vec2(variable_name: Name, value: Vector2D) -> None
unreal.NiagaraComponent.set_variable_vec3(variable_name: Name, value: Vector) -> None
unreal.NiagaraComponent.set_variable_vec4(variable_name: Name, value: Vector4) -> None
```

## `unreal.NiagaraCulledComponentInfo(StructBase)`

```python
unreal.NiagaraCulledComponentInfo.__init__() -> None
```

## `unreal.NiagaraDIRigidMeshCollisionFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraDIRigidMeshCollisionFunctionLibrary.set_source_actors(niagara_system: NiagaraComponent, override_name: Name, source_actors: Array[Actor]) -> None
```

## `unreal.NiagaraDataChannel(Object)`

```python
unreal.NiagaraDataChannel.variables(value: Array[NiagaraVariable]) -> None
```

## `unreal.NiagaraDataChannelHandler(Object)`

```python
unreal.NiagaraDataChannelHandler.get_data_channel_reader() -> NiagaraDataChannelReader
unreal.NiagaraDataChannelHandler.get_data_channel_writer() -> NiagaraDataChannelWriter
```

## `unreal.NiagaraDataChannelLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraDataChannelLibrary.get_data_channel_element_count(world_context_object: Object, channel: NiagaraDataChannelAsset, search_params: NiagaraDataChannelSearchParameters, read_previous_frame: bool = True) -> int
unreal.NiagaraDataChannelLibrary.read_from_niagara_data_channel(world_context_object: Object, channel: NiagaraDataChannelAsset, search_params: NiagaraDataChannelSearchParameters, read_previous_frame: bool) -> NiagaraDataChannelReader
unreal.NiagaraDataChannelLibrary.write_to_niagara_data_channel(world_context_object: Object, channel: NiagaraDataChannelAsset, search_params: NiagaraDataChannelSearchParameters, count: int, visible_to_game: bool, visible_to_cpu: bool, visible_to_gpu: bool, debug_source: str) -> NiagaraDataChannelWriter
```

## `unreal.NiagaraDataChannelReader(Object)`

```python
unreal.NiagaraDataChannelReader.init_access(search_params: NiagaraDataChannelSearchParameters, read_prev_frame_data: bool) -> bool
unreal.NiagaraDataChannelReader.num() -> int
unreal.NiagaraDataChannelReader.read_bool(var_name: Name, index: int) -> Optional[bool]
unreal.NiagaraDataChannelReader.read_enum(var_name: Name, index: int) -> Tuple[int, bool]
unreal.NiagaraDataChannelReader.read_float(var_name: Name, index: int) -> Tuple[float, bool]
unreal.NiagaraDataChannelReader.read_id(var_name: Name, index: int) -> Tuple[NiagaraID, bool]
unreal.NiagaraDataChannelReader.read_int(var_name: Name, index: int) -> Tuple[int, bool]
unreal.NiagaraDataChannelReader.read_linear_color(var_name: Name, index: int) -> Tuple[LinearColor, bool]
unreal.NiagaraDataChannelReader.read_position(var_name: Name, index: int) -> Tuple[Vector, bool]
unreal.NiagaraDataChannelReader.read_quat(var_name: Name, index: int) -> Tuple[Quat, bool]
unreal.NiagaraDataChannelReader.read_spawn_info(var_name: Name, index: int) -> Tuple[NiagaraSpawnInfo, bool]
unreal.NiagaraDataChannelReader.read_vector(var_name: Name, index: int) -> Tuple[Vector, bool]
unreal.NiagaraDataChannelReader.read_vector2d(var_name: Name, index: int) -> Tuple[Vector2D, bool]
unreal.NiagaraDataChannelReader.read_vector4(var_name: Name, index: int) -> Tuple[Vector4, bool]
```

## `unreal.NiagaraDataChannelSearchParameters(StructBase)`

```python
unreal.NiagaraDataChannelSearchParameters.__init__(owning_component: SceneComponent = None, location: Vector = [0.000000, 0.000000, 0.000000], override_location: bool = False) -> None
unreal.NiagaraDataChannelSearchParameters.location(value: Vector) -> None
unreal.NiagaraDataChannelSearchParameters.override_location(value: bool) -> None
unreal.NiagaraDataChannelSearchParameters.owning_component(value: SceneComponent) -> None
```

## `unreal.NiagaraDataChannelVariable(NiagaraVariableBase)`

```python
unreal.NiagaraDataChannelVariable.__init__() -> None
```

## `unreal.NiagaraDataChannelWriter(Object)`

```python
unreal.NiagaraDataChannelWriter.init_write(search_params: NiagaraDataChannelSearchParameters, count: int, visible_to_game: bool = True, visible_to_cpu: bool = True, visible_to_gpu: bool = True, debug_source: str = ...) -> bool
unreal.NiagaraDataChannelWriter.num() -> int
unreal.NiagaraDataChannelWriter.write_bool(var_name: Name, index: int, data: bool) -> None
unreal.NiagaraDataChannelWriter.write_enum(var_name: Name, index: int, data: int) -> None
unreal.NiagaraDataChannelWriter.write_float(var_name: Name, index: int, data: float) -> None
unreal.NiagaraDataChannelWriter.write_id(var_name: Name, index: int, data: NiagaraID) -> None
unreal.NiagaraDataChannelWriter.write_int(var_name: Name, index: int, data: int) -> None
unreal.NiagaraDataChannelWriter.write_linear_color(var_name: Name, index: int, data: LinearColor) -> None
unreal.NiagaraDataChannelWriter.write_position(var_name: Name, index: int, data: Vector) -> None
unreal.NiagaraDataChannelWriter.write_quat(var_name: Name, index: int, data: Quat) -> None
unreal.NiagaraDataChannelWriter.write_spawn_info(var_name: Name, index: int, data: NiagaraSpawnInfo) -> None
unreal.NiagaraDataChannelWriter.write_vector(var_name: Name, index: int, data: Vector) -> None
unreal.NiagaraDataChannelWriter.write_vector2d(var_name: Name, index: int, data: Vector2D) -> None
unreal.NiagaraDataChannelWriter.write_vector4(var_name: Name, index: int, data: Vector4) -> None
```

## `unreal.NiagaraDataInterfaceArray(NiagaraDataInterfaceRWBase)`

```python
unreal.NiagaraDataInterfaceArray.gpu_sync_mode() -> NiagaraGpuSyncMode
unreal.NiagaraDataInterfaceArray.max_elements() -> int
```

## `unreal.NiagaraDataInterfaceArrayBool(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayBool.bool_data(value: Array[bool]) -> None
```

## `unreal.NiagaraDataInterfaceArrayColor(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayColor.color_data(value: Array[LinearColor]) -> None
```

## `unreal.NiagaraDataInterfaceArrayFloat(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayFloat.float_data(value: Array[float]) -> None
```

## `unreal.NiagaraDataInterfaceArrayFloat2(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayFloat2.float_data(value: Array[Vector2D]) -> None
```

## `unreal.NiagaraDataInterfaceArrayFloat3(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayFloat3.float_data(value: Array[Vector]) -> None
```

## `unreal.NiagaraDataInterfaceArrayFloat4(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayFloat4.float_data(value: Array[Vector4]) -> None
```

## `unreal.NiagaraDataInterfaceArrayFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_bool(niagara_system: NiagaraComponent, override_name: Name) -> Array[bool]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_bool_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> bool
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_color(niagara_system: NiagaraComponent, override_name: Name) -> Array[LinearColor]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_color_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> LinearColor
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_float(niagara_system: NiagaraComponent, override_name: Name) -> Array[float]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_float_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> float
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_int32(niagara_system: NiagaraComponent, override_name: Name) -> Array[int]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_int32_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> int
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_matrix(niagara_system: NiagaraComponent, override_name: Name, apply_lwc_rebase: bool = True) -> Array[Matrix]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_matrix_value(niagara_system: NiagaraComponent, override_name: Name, index: int, apply_lwc_rebase: bool = True) -> Matrix
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_position(niagara_system: NiagaraComponent, override_name: Name) -> Array[Vector]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_position_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> Vector
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_quat(niagara_system: NiagaraComponent, override_name: Name) -> Array[Quat]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_quat_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> Quat
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_u_int8(niagara_system: NiagaraComponent, override_name: Name) -> Array[int]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_u_int8_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> int
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector(niagara_system: NiagaraComponent, override_name: Name) -> Array[Vector]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector2d(niagara_system: NiagaraComponent, override_name: Name) -> Array[Vector2D]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector2d_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> Vector2D
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector4(niagara_system: NiagaraComponent, override_name: Name) -> Array[Vector4]
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector4_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> Vector4
unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector_value(niagara_system: NiagaraComponent, override_name: Name, index: int) -> Vector
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_bool(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[bool]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_bool_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: bool, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_color(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[LinearColor]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_color_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: LinearColor, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_float(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[float]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_float_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: float, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_int32(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[int]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_int32_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: int, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_matrix(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Matrix], apply_lwc_rebase: bool = True) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_matrix_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Matrix, size_to_fit: bool, apply_lwc_rebase: bool = True) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_position(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Vector]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_position_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Vector, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_quat(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Quat]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_quat_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Quat, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_u_int8(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[int]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_u_int8_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: int, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Vector]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector2d(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Vector2D]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector2d_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Vector2D, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector4(niagara_system: NiagaraComponent, override_name: Name, array_data: Array[Vector4]) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector4_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Vector4, size_to_fit: bool) -> None
unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector_value(niagara_system: NiagaraComponent, override_name: Name, index: int, value: Vector, size_to_fit: bool) -> None
```

## `unreal.NiagaraDataInterfaceArrayInt32(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayInt32.int_data(value: Array[int]) -> None
```

## `unreal.NiagaraDataInterfaceArrayMatrix(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayMatrix.matrix_data(value: Array[Matrix]) -> None
```

## `unreal.NiagaraDataInterfaceArrayNiagaraID(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayNiagaraID.int_data(value: Array[NiagaraID]) -> None
```

## `unreal.NiagaraDataInterfaceArrayPosition(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayPosition.position_data(value: Array[NiagaraPosition]) -> None
```

## `unreal.NiagaraDataInterfaceArrayQuat(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayQuat.quat_data(value: Array[Quat]) -> None
```

## `unreal.NiagaraDataInterfaceArrayUInt8(NiagaraDataInterfaceArray)`

```python
unreal.NiagaraDataInterfaceArrayUInt8.int_data(value: Array[int]) -> None
```

## `unreal.NiagaraDataInterfaceAudioPlayerSettings(Object)`

```python
unreal.NiagaraDataInterfaceAudioPlayerSettings.attenuation_settings(value: SoundAttenuationSettings) -> None
unreal.NiagaraDataInterfaceAudioPlayerSettings.concurrency(value: SoundConcurrency) -> None
unreal.NiagaraDataInterfaceAudioPlayerSettings.override_attenuation_settings(value: bool) -> None
unreal.NiagaraDataInterfaceAudioPlayerSettings.override_concurrency(value: bool) -> None
```

## `unreal.NiagaraDataInterfaceEmitterBinding(StructBase)`

```python
unreal.NiagaraDataInterfaceEmitterBinding.__init__() -> None
```

## `unreal.NiagaraDataInterfaceGrid2DCollection(NiagaraDataInterfaceGrid2D)`

```python
unreal.NiagaraDataInterfaceGrid2DCollection.fill_raw_texture2d(component: NiagaraComponent, dest: TextureRenderTarget2D) -> Optional[Tuple[int, int]]
unreal.NiagaraDataInterfaceGrid2DCollection.fill_texture2d(component: NiagaraComponent, dest: TextureRenderTarget2D, attribute_index: int) -> bool
unreal.NiagaraDataInterfaceGrid2DCollection.get_raw_texture_size(component: NiagaraComponent) -> Tuple[int, int]
unreal.NiagaraDataInterfaceGrid2DCollection.get_texture_size(component: NiagaraComponent) -> Tuple[int, int]
```

## `unreal.NiagaraDataInterfaceGrid3DCollection(NiagaraDataInterfaceGrid3D)`

```python
unreal.NiagaraDataInterfaceGrid3DCollection.fill_raw_volume_texture(component: NiagaraComponent, dest: VolumeTexture) -> Optional[Tuple[int, int, int]]
unreal.NiagaraDataInterfaceGrid3DCollection.fill_volume_texture(component: NiagaraComponent, dest: VolumeTexture, attribute_index: int) -> bool
unreal.NiagaraDataInterfaceGrid3DCollection.get_raw_texture_size(component: NiagaraComponent) -> Tuple[int, int, int]
unreal.NiagaraDataInterfaceGrid3DCollection.get_texture_size(component: NiagaraComponent) -> Tuple[int, int, int]
```

## `unreal.NiagaraDataInterfaceSceneCapture2D(NiagaraDataInterface)`

```python
unreal.NiagaraDataInterfaceSceneCapture2D.set_scene_capture2d_managed_show_only_actors(niagara_system: NiagaraComponent, parameter_name: Name, show_only_actors: Array[Actor]) -> None
```

## `unreal.NiagaraDataInterfaceStaticMesh(NiagaraDataInterface)`

```python
unreal.NiagaraDataInterfaceStaticMesh.set_niagara_static_mesh_di_instance_index(niagara_system: NiagaraComponent, user_parameter_name: Name, new_instance_index: int) -> None
```

## `unreal.NiagaraDataInterfaceUObjectPropertyReader(NiagaraDataInterface)`

```python
unreal.NiagaraDataInterfaceUObjectPropertyReader.set_u_object_reader_property_remap(niagara_component: NiagaraComponent, user_parameter_name: Name, graph_name: Name, remap_name: Name) -> None
```

## `unreal.NiagaraDeviceProfileStateEntry(StructBase)`

```python
unreal.NiagaraDeviceProfileStateEntry.__init__() -> None
```

## `unreal.NiagaraEmitter(Object)`

```python
unreal.NiagaraEmitter.allocation_mode(value: ParticleAllocationMode) -> None
unreal.NiagaraEmitter.attributes_to_preserve(value: Array[str]) -> None
unreal.NiagaraEmitter.determinism(value: bool) -> None
unreal.NiagaraEmitter.editor_data(value: NiagaraEditorDataBase) -> None
unreal.NiagaraEmitter.editor_parameters(value: NiagaraEditorParametersAdapterBase) -> None
unreal.NiagaraEmitter.emitter_spawn_script_props(value: NiagaraEmitterScriptProperties) -> None
unreal.NiagaraEmitter.emitter_update_script_props(value: NiagaraEmitterScriptProperties) -> None
unreal.NiagaraEmitter.event_handler_script_props(value: Array[NiagaraEventScriptProperties]) -> None
unreal.NiagaraEmitter.gpu_compute_script(value: NiagaraScript) -> None
unreal.NiagaraEmitter.graph_source(value: NiagaraScriptSourceBase) -> None
unreal.NiagaraEmitter.interpolated_spawning(value: bool) -> None
unreal.NiagaraEmitter.local_space(value: bool) -> None
unreal.NiagaraEmitter.max_gpu_particles_spawn_per_frame(value: int) -> None
unreal.NiagaraEmitter.parent(value: NiagaraEmitter) -> None
unreal.NiagaraEmitter.parent_at_last_merge(value: NiagaraEmitter) -> None
unreal.NiagaraEmitter.parent_scratch_pad_scripts(value: Array[NiagaraScript]) -> None
unreal.NiagaraEmitter.platforms(value: NiagaraPlatformSet) -> None
unreal.NiagaraEmitter.pre_allocation_count(value: int) -> None
unreal.NiagaraEmitter.random_seed(value: int) -> None
unreal.NiagaraEmitter.renderer_bindings(value: NiagaraParameterStore) -> None
unreal.NiagaraEmitter.renderer_properties(value: Array[NiagaraRendererProperties]) -> None
unreal.NiagaraEmitter.requires_persistent_i_ds(value: bool) -> None
unreal.NiagaraEmitter.scalability_overrides(value: NiagaraEmitterScalabilityOverrides) -> None
unreal.NiagaraEmitter.scratch_pad_scripts(value: Array[NiagaraScript]) -> None
unreal.NiagaraEmitter.shared_event_generator_ids(value: Array[Name]) -> None
unreal.NiagaraEmitter.sim_target(value: NiagaraSimTarget) -> None
unreal.NiagaraEmitter.simulation_stages(value: Array[NiagaraSimulationStageBase]) -> None
unreal.NiagaraEmitter.spawn_script_props(value: NiagaraEmitterScriptProperties) -> None
unreal.NiagaraEmitter.template_specification(value: NiagaraScriptTemplateSpecification) -> None
unreal.NiagaraEmitter.update_script_props(value: NiagaraEmitterScriptProperties) -> None
```

## `unreal.NiagaraEmitterScalabilityOverride(NiagaraEmitterScalabilitySettings)`

```python
unreal.NiagaraEmitterScalabilityOverride.__init__() -> None
```

## `unreal.NiagaraEmitterScalabilityOverrides(StructBase)`

```python
unreal.NiagaraEmitterScalabilityOverrides.__init__() -> None
```

## `unreal.NiagaraEmitterScalabilitySettings(StructBase)`

```python
unreal.NiagaraEmitterScalabilitySettings.__init__() -> None
```

## `unreal.NiagaraEmitterScalabilitySettingsArray(StructBase)`

```python
unreal.NiagaraEmitterScalabilitySettingsArray.__init__() -> None
```

## `unreal.NiagaraEmitterScriptProperties(StructBase)`

```python
unreal.NiagaraEmitterScriptProperties.__init__() -> None
```

## `unreal.NiagaraEventScriptProperties(NiagaraEmitterScriptProperties)`

```python
unreal.NiagaraEventScriptProperties.__init__() -> None
```

## `unreal.NiagaraFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraFunctionLibrary.acquire_niagara_gpu_ray_traced_collision_group(world_context_object: Object) -> int
unreal.NiagaraFunctionLibrary.get_niagara_parameter_collection(world_context_object: Object, collection: NiagaraParameterCollection) -> NiagaraParameterCollectionInstance
unreal.NiagaraFunctionLibrary.override_system_user_variable_skeletal_mesh_component(niagara_system: NiagaraComponent, override_name: str, skeletal_mesh_component: SkeletalMeshComponent) -> None
unreal.NiagaraFunctionLibrary.override_system_user_variable_static_mesh(niagara_system: NiagaraComponent, override_name: str, static_mesh: StaticMesh) -> None
unreal.NiagaraFunctionLibrary.override_system_user_variable_static_mesh_component(niagara_system: NiagaraComponent, override_name: str, static_mesh_component: StaticMeshComponent) -> None
unreal.NiagaraFunctionLibrary.release_niagara_gpu_ray_traced_collision_group(world_context_object: Object, collision_group: int) -> None
unreal.NiagaraFunctionLibrary.set_actor_niagara_gpu_ray_traced_collision_group(world_context_object: Object, actor: Actor, collision_group: int) -> None
unreal.NiagaraFunctionLibrary.set_component_niagara_gpu_ray_traced_collision_group(world_context_object: Object, primitive: PrimitiveComponent, collision_group: int) -> None
unreal.NiagaraFunctionLibrary.set_scene_capture2d_data_interface_managed_mode(niagara_system: NiagaraComponent, di_name: Name, managed_capture_source: SceneCaptureSource, managed_texture_size: IntPoint, managed_texture_format: TextureRenderTargetFormat, managed_projection_type: CameraProjectionMode, managed_fov_angle: float, managed_ortho_width: float, managed_capture_every_frame: bool, managed_capture_on_movement: bool, show_only_actors: Array[Actor]) -> None
unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_filtered_bones(niagara_system: NiagaraComponent, override_name: str, filtered_bones: Array[Name]) -> None
unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_filtered_sockets(niagara_system: NiagaraComponent, override_name: str, filtered_sockets: Array[Name]) -> None
unreal.NiagaraFunctionLibrary.set_skeletal_mesh_data_interface_sampling_regions(niagara_system: NiagaraComponent, override_name: str, sampling_regions: Array[Name]) -> None
unreal.NiagaraFunctionLibrary.set_texture2d_array_object(niagara_system: NiagaraComponent, override_name: str, texture: Texture2DArray) -> None
unreal.NiagaraFunctionLibrary.set_texture_object(niagara_system: NiagaraComponent, override_name: str, texture: Texture) -> None
unreal.NiagaraFunctionLibrary.set_volume_texture_object(niagara_system: NiagaraComponent, override_name: str, texture: VolumeTexture) -> None
unreal.NiagaraFunctionLibrary.spawn_system_at_location(world_context_object: Object, system_template: NiagaraSystem, location: Vector, rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [1.000000, 1.000000, 1.000000], auto_destroy: bool = True, auto_activate: bool = True, pooling_method: NCPoolMethod = NCPoolMethod.NONE, pre_cull_check: bool = True) -> NiagaraComponent
unreal.NiagaraFunctionLibrary.spawn_system_at_location_with_params(spawn_params: FXSystemSpawnParameters) -> NiagaraComponent
unreal.NiagaraFunctionLibrary.spawn_system_attached(system_template: NiagaraSystem, attach_to_component: SceneComponent, attach_point_name: Name, location: Vector, rotation: Rotator, location_type: AttachLocation, auto_destroy: bool, auto_activate: bool = True, pooling_method: NCPoolMethod = NCPoolMethod.NONE, pre_cull_check: bool = True) -> NiagaraComponent
unreal.NiagaraFunctionLibrary.spawn_system_attached_with_params(spawn_params: FXSystemSpawnParameters) -> NiagaraComponent
```

## `unreal.NiagaraGlobalBudgetScaling(StructBase)`

```python
unreal.NiagaraGlobalBudgetScaling.__init__() -> None
```

## `unreal.NiagaraID(StructBase)`

```python
unreal.NiagaraID.__init__(index: int = 0, acquire_tag: int = 0) -> None
unreal.NiagaraID.acquire_tag(value: int) -> None
unreal.NiagaraID.index(value: int) -> None
```

## `unreal.NiagaraLensEffectBase(NiagaraActor)`

```python
unreal.NiagaraLensEffectBase.get_particle_components() -> Array[FXSystemComponent]
unreal.NiagaraLensEffectBase.get_primary_particle_component() -> FXSystemComponent
```

## `unreal.NiagaraLightRendererProperties(NiagaraRendererProperties)`

```python
unreal.NiagaraLightRendererProperties.inverse_exposure_blend() -> float
```

## `unreal.NiagaraLinearRamp(StructBase)`

```python
unreal.NiagaraLinearRamp.__init__() -> None
```

## `unreal.NiagaraMaterialAttributeBinding(StructBase)`

```python
unreal.NiagaraMaterialAttributeBinding.__init__() -> None
```

## `unreal.NiagaraModuleDependency(StructBase)`

```python
unreal.NiagaraModuleDependency.__init__() -> None
```

## `unreal.NiagaraParameterCollectionInstance(Object)`

```python
unreal.NiagaraParameterCollectionInstance.get_bool_parameter(variable_name: str) -> bool
unreal.NiagaraParameterCollectionInstance.get_color_parameter(variable_name: str) -> LinearColor
unreal.NiagaraParameterCollectionInstance.get_float_parameter(variable_name: str) -> float
unreal.NiagaraParameterCollectionInstance.get_int_parameter(variable_name: str) -> int
unreal.NiagaraParameterCollectionInstance.get_quat_parameter(variable_name: str) -> Quat
unreal.NiagaraParameterCollectionInstance.get_vector2d_parameter(variable_name: str) -> Vector2D
unreal.NiagaraParameterCollectionInstance.get_vector4_parameter(variable_name: str) -> Vector4
unreal.NiagaraParameterCollectionInstance.get_vector_parameter(variable_name: str) -> Vector
unreal.NiagaraParameterCollectionInstance.set_bool_parameter(variable_name: str, value: bool) -> None
unreal.NiagaraParameterCollectionInstance.set_color_parameter(variable_name: str, value: LinearColor) -> None
unreal.NiagaraParameterCollectionInstance.set_float_parameter(variable_name: str, value: float) -> None
unreal.NiagaraParameterCollectionInstance.set_int_parameter(variable_name: str, value: int) -> None
unreal.NiagaraParameterCollectionInstance.set_quat_parameter(variable_name: str, value: Quat) -> None
unreal.NiagaraParameterCollectionInstance.set_vector2d_parameter(variable_name: str, value: Vector2D) -> None
unreal.NiagaraParameterCollectionInstance.set_vector4_parameter(variable_name: str, value: Vector4) -> None
unreal.NiagaraParameterCollectionInstance.set_vector_parameter(variable_name: str, value: Vector) -> None
```

## `unreal.NiagaraParameterStore(StructBase)`

```python
unreal.NiagaraParameterStore.__init__() -> None
unreal.NiagaraParameterStore.parameter_offsets(value: Map[NiagaraVariable, int]) -> None
```

## `unreal.NiagaraParticleCallbackHandler(Interface)`

```python
unreal.NiagaraParticleCallbackHandler.receive_particle_data(data: Array[BasicParticleData], niagara_system: NiagaraSystem, simulation_position_offset: Vector) -> None
```

## `unreal.NiagaraPerfBaselineStats(StructBase)`

```python
unreal.NiagaraPerfBaselineStats.__init__(per_instance_avg_gt: float = 0.000000, per_instance_avg_rt: float = 0.000000, per_instance_max_gt: float = 0.000000, per_instance_max_rt: float = 0.000000) -> None
unreal.NiagaraPerfBaselineStats.per_instance_avg_gt(value: float) -> None
unreal.NiagaraPerfBaselineStats.per_instance_avg_rt(value: float) -> None
unreal.NiagaraPerfBaselineStats.per_instance_max_gt(value: float) -> None
unreal.NiagaraPerfBaselineStats.per_instance_max_rt(value: float) -> None
```

## `unreal.NiagaraPlatformSet(StructBase)`

```python
unreal.NiagaraPlatformSet.__init__() -> None
```

## `unreal.NiagaraPlatformSetCVarCondition(StructBase)`

```python
unreal.NiagaraPlatformSetCVarCondition.__init__() -> None
```

## `unreal.NiagaraPlatformSetRedirect(StructBase)`

```python
unreal.NiagaraPlatformSetRedirect.__init__() -> None
```

## `unreal.NiagaraPosition(Vector3f)`

```python
unreal.NiagaraPosition.__init__() -> None
```

## `unreal.NiagaraPreviewAxis(Object)`

```python
unreal.NiagaraPreviewAxis.apply_to_preview(preview_component: NiagaraComponent, preview_index: int, is_x_axis: bool) -> str
unreal.NiagaraPreviewAxis.num() -> int
```

## `unreal.NiagaraPreviewBase(Actor)`

```python
unreal.NiagaraPreviewBase.set_label_text(x_axis_text: Text, y_axis_text: Text) -> None
unreal.NiagaraPreviewBase.set_system(system: NiagaraSystem) -> None
```

## `unreal.NiagaraPreviewGrid(Actor)`

```python
unreal.NiagaraPreviewGrid.activate_previews(reset: bool) -> None
unreal.NiagaraPreviewGrid.deactivate_previews() -> None
unreal.NiagaraPreviewGrid.get_previews() -> Array[NiagaraComponent]
unreal.NiagaraPreviewGrid.set_paused(paused: bool) -> None
```

## `unreal.NiagaraPythonEmitter(Object)`

```python
unreal.NiagaraPythonEmitter.get_module(module_name: str) -> NiagaraPythonModule
unreal.NiagaraPythonEmitter.get_modules() -> Array[NiagaraPythonModule]
unreal.NiagaraPythonEmitter.get_object() -> NiagaraEmitter
unreal.NiagaraPythonEmitter.get_properties() -> VersionedNiagaraEmitterData
unreal.NiagaraPythonEmitter.has_module(module_name: str) -> bool
unreal.NiagaraPythonEmitter.set_properties(data: VersionedNiagaraEmitterData) -> None
```

## `unreal.NiagaraPythonModule(Object)`

```python
unreal.NiagaraPythonModule.get_object() -> NiagaraStackModuleItem
```

## `unreal.NiagaraPythonScriptModuleInput(Object)`

```python
unreal.NiagaraPythonScriptModuleInput.as_bool() -> bool
unreal.NiagaraPythonScriptModuleInput.as_color() -> LinearColor
unreal.NiagaraPythonScriptModuleInput.as_enum() -> str
unreal.NiagaraPythonScriptModuleInput.as_float() -> float
unreal.NiagaraPythonScriptModuleInput.as_int() -> int
unreal.NiagaraPythonScriptModuleInput.as_linked_value() -> str
unreal.NiagaraPythonScriptModuleInput.as_quat() -> Quat
unreal.NiagaraPythonScriptModuleInput.as_vec2() -> Vector2D
unreal.NiagaraPythonScriptModuleInput.as_vec3() -> Vector
unreal.NiagaraPythonScriptModuleInput.as_vec4() -> Vector4
unreal.NiagaraPythonScriptModuleInput.is_linked_value() -> bool
unreal.NiagaraPythonScriptModuleInput.is_local_value() -> bool
unreal.NiagaraPythonScriptModuleInput.is_set() -> bool
```

## `unreal.NiagaraRendererMaterialParameters(StructBase)`

```python
unreal.NiagaraRendererMaterialParameters.__init__() -> None
```

## `unreal.NiagaraRendererMaterialScalarParameter(StructBase)`

```python
unreal.NiagaraRendererMaterialScalarParameter.__init__() -> None
```

## `unreal.NiagaraRendererMaterialStaticBoolParameter(StructBase)`

```python
unreal.NiagaraRendererMaterialStaticBoolParameter.__init__() -> None
```

## `unreal.NiagaraRendererMaterialTextureParameter(StructBase)`

```python
unreal.NiagaraRendererMaterialTextureParameter.__init__() -> None
```

## `unreal.NiagaraRendererMaterialVectorParameter(StructBase)`

```python
unreal.NiagaraRendererMaterialVectorParameter.__init__() -> None
```

## `unreal.NiagaraScalabilityOverrides(NiagaraSystemScalabilityOverride)`

```python
unreal.NiagaraScalabilityOverrides.__init__() -> None
```

## `unreal.NiagaraScalabilitySettings(NiagaraSystemScalabilitySettings)`

```python
unreal.NiagaraScalabilitySettings.__init__() -> None
```

## `unreal.NiagaraScript(NiagaraScriptBase)`

```python
unreal.NiagaraScript.category(value: Text) -> None
unreal.NiagaraScript.collapsed_view_format(value: Text) -> None
unreal.NiagaraScript.conversion_utility(value: Class) -> None
unreal.NiagaraScript.deprecated(value: bool) -> None
unreal.NiagaraScript.deprecation_message(value: Text) -> None
unreal.NiagaraScript.deprecation_recommendation(value: NiagaraScript) -> None
unreal.NiagaraScript.description(value: Text) -> None
unreal.NiagaraScript.experimental(value: bool) -> None
unreal.NiagaraScript.experimental_message(value: Text) -> None
unreal.NiagaraScript.expose_to_library(value: bool) -> None
unreal.NiagaraScript.keywords(value: Text) -> None
unreal.NiagaraScript.library_visibility(value: NiagaraScriptLibraryVisibility) -> None
unreal.NiagaraScript.module_usage_bitmask(value: int) -> None
unreal.NiagaraScript.note_message(value: Text) -> None
unreal.NiagaraScript.numeric_output_type_selection_mode(value: NiagaraNumericOutputTypeSelectionMode) -> None
unreal.NiagaraScript.provided_dependencies(value: Array[Name]) -> None
unreal.NiagaraScript.required_dependencies(value: Array[NiagaraModuleDependency]) -> None
unreal.NiagaraScript.script_meta_data(value: Map[Name, str]) -> None
unreal.NiagaraScript.source(value: NiagaraScriptSourceBase) -> None
```

## `unreal.NiagaraSettings(DeveloperSettings)`

```python
unreal.NiagaraSettings.limit_delta_time(value: bool) -> None
unreal.NiagaraSettings.max_delta_time_per_tick(value: float) -> None
```

## `unreal.NiagaraSimCache(Object)`

```python
unreal.NiagaraSimCache.get_attribute_capture_mode() -> NiagaraSimCacheAttributeCaptureMode
unreal.NiagaraSimCache.get_emitter_name(emitter_index: int) -> Name
unreal.NiagaraSimCache.get_emitter_names() -> Array[Name]
unreal.NiagaraSimCache.get_num_emitters() -> int
unreal.NiagaraSimCache.get_num_frames() -> int
unreal.NiagaraSimCache.get_start_seconds() -> float
unreal.NiagaraSimCache.is_cache_valid() -> bool
unreal.NiagaraSimCache.is_empty() -> bool
unreal.NiagaraSimCache.read_color_attribute(attribute_name: Name = "Color", emitter_name: Name = "None", frame_index: int = 0) -> Array[LinearColor]
unreal.NiagaraSimCache.read_data_interface_as(requested_type: Class, attribute_name: Name, frame_index: int = 0) -> Object
unreal.NiagaraSimCache.read_float_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[float]
unreal.NiagaraSimCache.read_id_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[NiagaraID]
unreal.NiagaraSimCache.read_int_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[int]
unreal.NiagaraSimCache.read_position_attribute(attribute_name: Name = "Position", emitter_name: Name = "None", local_space_to_world: bool = True, frame_index: int = 0) -> Array[Vector]
unreal.NiagaraSimCache.read_position_attribute_with_rebase(transform: Transform, attribute_name: Name = "Position", emitter_name: Name = "None", frame_index: int = 0) -> Array[Vector]
unreal.NiagaraSimCache.read_quat_attribute(attribute_name: Name = "MeshOrientation", emitter_name: Name = "None", local_space_to_world: bool = True, frame_index: int = 0) -> Array[Quat]
unreal.NiagaraSimCache.read_quat_attribute_with_rebase(quat: Quat, attribute_name: Name = "MeshOrientation", emitter_name: Name = "None", frame_index: int = 0) -> Array[Quat]
unreal.NiagaraSimCache.read_vector2_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[Vector2D]
unreal.NiagaraSimCache.read_vector4_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[Vector4]
unreal.NiagaraSimCache.read_vector_attribute(attribute_name: Name, emitter_name: Name, frame_index: int = 0) -> Array[Vector]
```

## `unreal.NiagaraSimCacheCaptureParameters(StructBase)`

```python
unreal.NiagaraSimCacheCaptureParameters.__init__(append_to_sim_cache: bool = False, capture_fixed_number_of_frames: bool = False, num_frames: int = 0, capture_rate: int = 0, use_timeout: bool = False, timeout_frame_count: int = 0, capture_all_frames_immediatly: bool = False, immediate_capture_delta_time: float = 0.000000) -> None
unreal.NiagaraSimCacheCaptureParameters.append_to_sim_cache(value: bool) -> None
unreal.NiagaraSimCacheCaptureParameters.capture_all_frames_immediatly(value: bool) -> None
unreal.NiagaraSimCacheCaptureParameters.capture_fixed_number_of_frames(value: bool) -> None
unreal.NiagaraSimCacheCaptureParameters.capture_rate(value: int) -> None
unreal.NiagaraSimCacheCaptureParameters.immediate_capture_delta_time(value: float) -> None
unreal.NiagaraSimCacheCaptureParameters.num_frames(value: int) -> None
unreal.NiagaraSimCacheCaptureParameters.timeout_frame_count(value: int) -> None
unreal.NiagaraSimCacheCaptureParameters.use_timeout(value: bool) -> None
```

## `unreal.NiagaraSimCacheCreateParameters(StructBase)`

```python
unreal.NiagaraSimCacheCreateParameters.__init__(attribute_capture_mode: NiagaraSimCacheAttributeCaptureMode = NiagaraSimCacheAttributeCaptureMode.ALL, allow_rebasing: bool = False, allow_data_interface_caching: bool = False, allow_interpolation: bool = False, allow_velocity_extrapolation: bool = False, allow_serialize_large_cache: bool = False, include_debug_data: bool = False, rebase_include_attributes: Array[Name] = [], rebase_exclude_attributes: Array[Name] = [], interpolation_include_attributes: Array[Name] = [], interpolation_exclude_attributes: Array[Name] = [], explicit_capture_attributes: Array[Name] = []) -> None
unreal.NiagaraSimCacheCreateParameters.allow_data_interface_caching(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.allow_interpolation(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.allow_rebasing(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.allow_serialize_large_cache(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.allow_velocity_extrapolation(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.attribute_capture_mode(value: NiagaraSimCacheAttributeCaptureMode) -> None
unreal.NiagaraSimCacheCreateParameters.explicit_capture_attributes(value: Array[Name]) -> None
unreal.NiagaraSimCacheCreateParameters.include_debug_data(value: bool) -> None
unreal.NiagaraSimCacheCreateParameters.interpolation_exclude_attributes(value: Array[Name]) -> None
unreal.NiagaraSimCacheCreateParameters.interpolation_include_attributes(value: Array[Name]) -> None
unreal.NiagaraSimCacheCreateParameters.rebase_exclude_attributes(value: Array[Name]) -> None
unreal.NiagaraSimCacheCreateParameters.rebase_include_attributes(value: Array[Name]) -> None
```

## `unreal.NiagaraSimCacheFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraSimCacheFunctionLibrary.capture_niagara_sim_cache_immediate(sim_cache: NiagaraSimCache, create_parameters: NiagaraSimCacheCreateParameters, niagara_component: NiagaraComponent, advance_simulation: bool = False, advance_delta_time: float = 0.016660) -> Optional[NiagaraSimCache]
unreal.NiagaraSimCacheFunctionLibrary.create_niagara_sim_cache(world_context_object: Object) -> NiagaraSimCache
```

## `unreal.NiagaraSimStageExecutionLoopEditorData(StructBase)`

```python
unreal.NiagaraSimStageExecutionLoopEditorData.__init__() -> None
```

## `unreal.NiagaraSpawnInfo(StructBase)`

```python
unreal.NiagaraSpawnInfo.__init__(count: int = 0, interp_start_dt: float = 0.000000, interval_dt: float = 0.000000, spawn_group: int = 0) -> None
unreal.NiagaraSpawnInfo.count(value: int) -> None
unreal.NiagaraSpawnInfo.interp_start_dt(value: float) -> None
unreal.NiagaraSpawnInfo.interval_dt(value: float) -> None
unreal.NiagaraSpawnInfo.spawn_group(value: int) -> None
```

## `unreal.NiagaraSpriteRendererProperties(NiagaraRendererProperties)`

```python
unreal.NiagaraSpriteRendererProperties.use_material_cutout_texture() -> bool
```

## `unreal.NiagaraSystem(FXSystemAsset)`

```python
unreal.NiagaraSystem.cast_shadow() -> bool
unreal.NiagaraSystem.custom_depth_stencil_value() -> int
unreal.NiagaraSystem.custom_depth_stencil_write_mask() -> RendererStencilMask
unreal.NiagaraSystem.receives_decals() -> bool
unreal.NiagaraSystem.render_custom_depth() -> bool
unreal.NiagaraSystem.translucency_sort_distance_offset() -> float
unreal.NiagaraSystem.translucency_sort_priority() -> int
```

## `unreal.NiagaraSystemScalabilityOverride(NiagaraSystemScalabilitySettings)`

```python
unreal.NiagaraSystemScalabilityOverride.__init__() -> None
```

## `unreal.NiagaraSystemScalabilityOverrides(StructBase)`

```python
unreal.NiagaraSystemScalabilityOverrides.__init__() -> None
```

## `unreal.NiagaraSystemScalabilitySettings(StructBase)`

```python
unreal.NiagaraSystemScalabilitySettings.__init__() -> None
```

## `unreal.NiagaraSystemScalabilitySettingsArray(StructBase)`

```python
unreal.NiagaraSystemScalabilitySettingsArray.__init__() -> None
```

## `unreal.NiagaraSystemVisibilityCullingSettings(StructBase)`

```python
unreal.NiagaraSystemVisibilityCullingSettings.__init__() -> None
```

## `unreal.NiagaraTypeDefinition(StructBase)`

```python
unreal.NiagaraTypeDefinition.__init__() -> None
```

## `unreal.NiagaraTypeDefinitionHandle(StructBase)`

```python
unreal.NiagaraTypeDefinitionHandle.__init__() -> None
```

## `unreal.NiagaraUObjectPropertyReaderRemap(StructBase)`

```python
unreal.NiagaraUObjectPropertyReaderRemap.__init__() -> None
```

## `unreal.NiagaraUserParameterBinding(StructBase)`

```python
unreal.NiagaraUserParameterBinding.__init__() -> None
```

## `unreal.NiagaraVariable(NiagaraVariableBase)`

```python
unreal.NiagaraVariable.__init__() -> None
```

## `unreal.NiagaraVariableAttributeBinding(StructBase)`

```python
unreal.NiagaraVariableAttributeBinding.__init__() -> None
```

## `unreal.NiagaraVariableBase(StructBase)`

```python
unreal.NiagaraVariableBase.__init__() -> None
unreal.NiagaraVariableBase.type_def(value: NiagaraTypeDefinition) -> None
```

## `unreal.NiagaraVariant(StructBase)`

```python
unreal.NiagaraVariant.__init__() -> None
```

## `unreal.NiagaraWaterFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.NiagaraWaterFunctionLibrary.set_water_body(niagara_system: NiagaraComponent, override_name: str, water_body: WaterBody) -> None
unreal.NiagaraWaterFunctionLibrary.set_water_body_component(niagara_system: NiagaraComponent, override_name: str, water_body_component: WaterBodyComponent) -> None
```

## `unreal.OnCanvasRenderTargetUpdate(MulticastDelegateBase)`

```python
unreal.OnCanvasRenderTargetUpdate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnLightningStrike(MulticastDelegateBase)`

```python
unreal.OnLightningStrike.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnNiagaraScriptCompilationComplete(MulticastDelegateBase)`

```python
unreal.OnNiagaraScriptCompilationComplete.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnNiagaraSystemFinished(MulticastDelegateBase)`

```python
unreal.OnNiagaraSystemFinished.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnRenderMovieStopped(DelegateBase)`

```python
unreal.OnRenderMovieStopped.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnWaterInfoTextureArrayCreated(MulticastDelegateBase)`

```python
unreal.OnWaterInfoTextureArrayCreated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnWaterInfoTextureCreated(MulticastDelegateBase)`

```python
unreal.OnWaterInfoTextureCreated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnWdpMaterialHitEventArgs(EventArgsBase)`

```python
unreal.OnWdpMaterialHitEventArgs.__init__(eid: int = 0, mesh_name: Name = "None", material_index: int = 0) -> None
unreal.OnWdpMaterialHitEventArgs.eid(value: int) -> None
unreal.OnWdpMaterialHitEventArgs.material_index(value: int) -> None
unreal.OnWdpMaterialHitEventArgs.mesh_name(value: Name) -> None
```

## `unreal.OptimusShaderText(StructBase)`

```python
unreal.OptimusShaderText.__init__() -> None
```

## `unreal.Optimus_ShaderBinding(StructBase)`

```python
unreal.Optimus_ShaderBinding.__init__() -> None
```

## `unreal.PCGBaseTextureData(PCGSurfaceData)`

```python
unreal.PCGBaseTextureData.bounds() -> Box
unreal.PCGBaseTextureData.center_offset(value: Vector2D) -> None
unreal.PCGBaseTextureData.color_channel(value: PCGTextureColorChannel) -> None
unreal.PCGBaseTextureData.density_function(value: PCGTextureDensityFunction) -> None
unreal.PCGBaseTextureData.filter(value: PCGTextureFilter) -> None
unreal.PCGBaseTextureData.height() -> int
unreal.PCGBaseTextureData.rotation(value: float) -> None
unreal.PCGBaseTextureData.texel_size(value: float) -> None
unreal.PCGBaseTextureData.tile_bounds(value: Box2D) -> None
unreal.PCGBaseTextureData.tiling(value: Vector2D) -> None
unreal.PCGBaseTextureData.use_advanced_tiling(value: bool) -> None
unreal.PCGBaseTextureData.use_density_source_channel(value: bool) -> None
unreal.PCGBaseTextureData.use_tile_bounds(value: bool) -> None
unreal.PCGBaseTextureData.width() -> int
```

## `unreal.PCGRenderTargetData(PCGBaseTextureData)`

```python
unreal.PCGRenderTargetData.initialize(render_target: TextureRenderTarget2D, transform: Transform) -> None
unreal.PCGRenderTargetData.render_target() -> TextureRenderTarget2D
```

## `unreal.PCGSampleTextureSettings(PCGSettings)`

```python
unreal.PCGSampleTextureSettings.clamp_output_density(value: bool) -> None
unreal.PCGSampleTextureSettings.density_merge_function(value: PCGDensityMergeOperation) -> None
unreal.PCGSampleTextureSettings.texture_mapping_method(value: PCGTextureMappingMethod) -> None
unreal.PCGSampleTextureSettings.tiling_mode(value: PCGTextureAddressMode) -> None
unreal.PCGSampleTextureSettings.uv_coordinates_attribute(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGStaticMeshSpawnerContext(PCGContext)`

```python
unreal.PCGStaticMeshSpawnerContext.__init__() -> None
```

## `unreal.PCGStaticMeshSpawnerSettings(PCGSettings)`

```python
unreal.PCGStaticMeshSpawnerSettings.allow_descriptor_changes() -> bool
unreal.PCGStaticMeshSpawnerSettings.apply_mesh_bounds_to_points(value: bool) -> None
unreal.PCGStaticMeshSpawnerSettings.instance_data_packer_parameters() -> PCGInstanceDataPackerBase
unreal.PCGStaticMeshSpawnerSettings.instance_data_packer_type() -> Class
unreal.PCGStaticMeshSpawnerSettings.instance_packer_instance() -> PCGInstanceDataPackerBase
unreal.PCGStaticMeshSpawnerSettings.instance_packer_type() -> Class
unreal.PCGStaticMeshSpawnerSettings.mesh_selector_instance() -> PCGMeshSelectorBase
unreal.PCGStaticMeshSpawnerSettings.mesh_selector_parameters() -> PCGMeshSelectorBase
unreal.PCGStaticMeshSpawnerSettings.mesh_selector_type() -> Class
unreal.PCGStaticMeshSpawnerSettings.out_attribute_name(value: Name) -> None
unreal.PCGStaticMeshSpawnerSettings.post_process_function_names(value: Array[Name]) -> None
unreal.PCGStaticMeshSpawnerSettings.set_instance_packer_type(instance_packer_type: Class) -> None
unreal.PCGStaticMeshSpawnerSettings.set_mesh_selector_type(mesh_selector_type: Class) -> None
unreal.PCGStaticMeshSpawnerSettings.silence_override_attribute_not_found_errors(value: bool) -> None
unreal.PCGStaticMeshSpawnerSettings.static_mesh_component_property_overrides(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGStaticMeshSpawnerSettings.synchronous_load(value: bool) -> None
unreal.PCGStaticMeshSpawnerSettings.target_actor(value: Actor) -> None
unreal.PCGStaticMeshSpawnerSettings.warn_on_identical_spawn(value: bool) -> None
```

## `unreal.PCGStaticMeshToDynamicMeshSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGStaticMeshToDynamicMeshSettings.extract_materials(value: bool) -> None
unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_index(value: int) -> None
unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_type(value: GeometryScriptLODType) -> None
unreal.PCGStaticMeshToDynamicMeshSettings.static_mesh(value: StaticMesh) -> None
unreal.PCGStaticMeshToDynamicMeshSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGTextureData(PCGBaseTextureData)`

```python
unreal.PCGTextureData.readback_from_gpu_initiated() -> bool
unreal.PCGTextureData.successfully_initialized() -> bool
unreal.PCGTextureData.texture() -> Texture
unreal.PCGTextureData.texture_index() -> int
```

## `unreal.PCGTextureSamplerSettings(PCGSettings)`

```python
unreal.PCGTextureSamplerSettings.center_offset(value: Vector2D) -> None
unreal.PCGTextureSamplerSettings.color_channel(value: PCGTextureColorChannel) -> None
unreal.PCGTextureSamplerSettings.density_function(value: PCGTextureDensityFunction) -> None
unreal.PCGTextureSamplerSettings.filter(value: PCGTextureFilter) -> None
unreal.PCGTextureSamplerSettings.force_editor_only_cpu_sampling(value: bool) -> None
unreal.PCGTextureSamplerSettings.rotation(value: float) -> None
unreal.PCGTextureSamplerSettings.synchronous_load(value: bool) -> None
unreal.PCGTextureSamplerSettings.texel_size(value: float) -> None
unreal.PCGTextureSamplerSettings.texture(value: Texture) -> None
unreal.PCGTextureSamplerSettings.texture_array_index(value: int) -> None
unreal.PCGTextureSamplerSettings.tile_bounds_max(value: Vector2D) -> None
unreal.PCGTextureSamplerSettings.tile_bounds_min(value: Vector2D) -> None
unreal.PCGTextureSamplerSettings.tiling(value: Vector2D) -> None
unreal.PCGTextureSamplerSettings.transform(value: Transform) -> None
unreal.PCGTextureSamplerSettings.use_absolute_transform(value: bool) -> None
unreal.PCGTextureSamplerSettings.use_advanced_tiling(value: bool) -> None
unreal.PCGTextureSamplerSettings.use_density_source_channel(value: bool) -> None
unreal.PCGTextureSamplerSettings.use_tile_bounds(value: bool) -> None
```

## `unreal.PaperTerrainMaterialRule(StructBase)`

```python
unreal.PaperTerrainMaterialRule.__init__() -> None
```

## `unreal.ParticleModuleLight(ParticleModuleLightBase)`

```python
unreal.ParticleModuleLight.inverse_exposure_blend() -> float
unreal.ParticleModuleLight.lighting_channels() -> LightingChannels
unreal.ParticleModuleLight.volumetric_scattering_intensity() -> float
```

## `unreal.PhysicalMaterial(Object)`

```python
unreal.PhysicalMaterial.damage_modifier() -> PhysicalMaterialDamageModifier
unreal.PhysicalMaterial.density() -> float
unreal.PhysicalMaterial.friction() -> float
unreal.PhysicalMaterial.friction_combine_mode() -> FrictionCombineMode
unreal.PhysicalMaterial.override_friction_combine_mode(value: bool) -> None
unreal.PhysicalMaterial.override_restitution_combine_mode(value: bool) -> None
unreal.PhysicalMaterial.raise_mass_to_power() -> float
unreal.PhysicalMaterial.restitution() -> float
unreal.PhysicalMaterial.restitution_combine_mode() -> FrictionCombineMode
unreal.PhysicalMaterial.sleep_angular_velocity_threshold() -> float
unreal.PhysicalMaterial.sleep_counter_threshold() -> int
unreal.PhysicalMaterial.sleep_linear_velocity_threshold() -> float
unreal.PhysicalMaterial.static_friction() -> float
unreal.PhysicalMaterial.strength() -> PhysicalMaterialStrength
unreal.PhysicalMaterial.surface_type() -> PhysicalSurface
```

## `unreal.PhysicalMaterialDamageModifier(StructBase)`

```python
unreal.PhysicalMaterialDamageModifier.__init__(damage_threshold_multiplier: float = 0.000000) -> None
unreal.PhysicalMaterialDamageModifier.damage_threshold_multiplier() -> float
```

## `unreal.PhysicalMaterialInput(StructBase)`

```python
unreal.PhysicalMaterialInput.__init__() -> None
```

## `unreal.PhysicalMaterialMask(Object)`

```python
unreal.PhysicalMaterialMask.address_x(value: TextureAddress) -> None
unreal.PhysicalMaterialMask.address_y(value: TextureAddress) -> None
unreal.PhysicalMaterialMask.mask_texture() -> Texture
unreal.PhysicalMaterialMask.uv_channel_index(value: int) -> None
```

## `unreal.PhysicalMaterialStrength(StructBase)`

```python
unreal.PhysicalMaterialStrength.__init__(tensile_strength: float = 0.000000, compression_strength: float = 0.000000, shear_strength: float = 0.000000) -> None
unreal.PhysicalMaterialStrength.compression_strength() -> float
unreal.PhysicalMaterialStrength.shear_strength() -> float
unreal.PhysicalMaterialStrength.tensile_strength() -> float
```

## `unreal.PickMaterialApiResult(ResultBase)`

```python
unreal.PickMaterialApiResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, eid: int = 0, component_id: str = "", position: Vector = [0.000000, 0.000000, 0.000000], material_name: str = "", material_index: int = 0) -> None
unreal.PickMaterialApiResult.component_id(value: str) -> None
unreal.PickMaterialApiResult.eid(value: int) -> None
unreal.PickMaterialApiResult.material_index(value: int) -> None
unreal.PickMaterialApiResult.material_name(value: str) -> None
unreal.PickMaterialApiResult.position(value: Vector) -> None
```

## `unreal.PointLight(Light)`

```python
unreal.PointLight.point_light_component() -> PointLightComponent
unreal.PointLight.set_light_falloff_exponent(new_light_falloff_exponent: float) -> None
unreal.PointLight.set_radius(new_radius: float) -> None
```

## `unreal.PointLightComponent(LocalLightComponent)`

```python
unreal.PointLightComponent.light_falloff_exponent() -> float
unreal.PointLightComponent.set_inverse_exposure_blend(new_inverse_exposure_blend: float) -> None
unreal.PointLightComponent.set_light_falloff_exponent(new_light_falloff_exponent: float) -> None
unreal.PointLightComponent.set_soft_source_radius(new_value: float) -> None
unreal.PointLightComponent.set_source_length(new_value: float) -> None
unreal.PointLightComponent.set_source_radius(new_value: float) -> None
unreal.PointLightComponent.set_use_inverse_squared_falloff(new_value: bool) -> None
unreal.PointLightComponent.soft_source_radius() -> float
unreal.PointLightComponent.source_length() -> float
unreal.PointLightComponent.source_radius() -> float
unreal.PointLightComponent.use_inverse_squared_falloff() -> bool
```

## `unreal.PostProcessComponent(SceneComponent)`

```python
unreal.PostProcessComponent.add_or_update_blendable(blendable_object: BlendableInterface, weight: float = 1.000000) -> None
unreal.PostProcessComponent.blend_radius(value: float) -> None
unreal.PostProcessComponent.blend_weight(value: float) -> None
unreal.PostProcessComponent.enabled(value: bool) -> None
unreal.PostProcessComponent.priority(value: float) -> None
unreal.PostProcessComponent.settings(value: PostProcessSettings) -> None
unreal.PostProcessComponent.unbound(value: bool) -> None
```

## `unreal.PostProcessSettings(StructBase)`

```python
unreal.PostProcessSettings.__init__(*args: Any, **kwargs: Any) -> None
unreal.PostProcessSettings.ambient_cubemap(value: TextureCube) -> None
unreal.PostProcessSettings.ambient_cubemap_intensity(value: float) -> None
unreal.PostProcessSettings.ambient_cubemap_tint(value: LinearColor) -> None
unreal.PostProcessSettings.ambient_occlusion_bias(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_fade_distance(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_fade_radius(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_intensity(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_mip_blend(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_mip_scale(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_mip_threshold(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_power(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_quality(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_radius(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_radius_in_ws(value: bool) -> None
unreal.PostProcessSettings.ambient_occlusion_static_fraction(value: float) -> None
unreal.PostProcessSettings.ambient_occlusion_temporal_blend_weight(value: float) -> None
unreal.PostProcessSettings.auto_exposure_apply_physical_camera_exposure(value: bool) -> None
unreal.PostProcessSettings.auto_exposure_bias(value: float) -> None
unreal.PostProcessSettings.auto_exposure_bias_curve(value: CurveFloat) -> None
unreal.PostProcessSettings.auto_exposure_high_percent(value: float) -> None
unreal.PostProcessSettings.auto_exposure_low_percent(value: float) -> None
unreal.PostProcessSettings.auto_exposure_max_brightness(value: float) -> None
unreal.PostProcessSettings.auto_exposure_meter_mask(value: Texture) -> None
unreal.PostProcessSettings.auto_exposure_method(value: AutoExposureMethod) -> None
unreal.PostProcessSettings.auto_exposure_min_brightness(value: float) -> None
unreal.PostProcessSettings.auto_exposure_speed_down(value: float) -> None
unreal.PostProcessSettings.auto_exposure_speed_up(value: float) -> None
unreal.PostProcessSettings.b_override_exposure_offset(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaptation_high_percent(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaptation_low_percent(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaptation_max_brightness(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaptation_min_brightness(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaption_speed_down(value: bool) -> None
unreal.PostProcessSettings.b_override_eye_adaption_speed_up(value: bool) -> None
unreal.PostProcessSettings.bloom1_size(value: float) -> None
unreal.PostProcessSettings.bloom1_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom2_size(value: float) -> None
unreal.PostProcessSettings.bloom2_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom3_size(value: float) -> None
unreal.PostProcessSettings.bloom3_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom4_size(value: float) -> None
unreal.PostProcessSettings.bloom4_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom5_size(value: float) -> None
unreal.PostProcessSettings.bloom5_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom6_size(value: float) -> None
unreal.PostProcessSettings.bloom6_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom_convolution_buffer_scale(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_center_uv(value: Vector2D) -> None
unreal.PostProcessSettings.bloom_convolution_pre_filter_max(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_pre_filter_min(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_pre_filter_mult(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_scatter_dispersion(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_size(value: float) -> None
unreal.PostProcessSettings.bloom_convolution_texture(value: Texture2D) -> None
unreal.PostProcessSettings.bloom_dirt_mask(value: Texture) -> None
unreal.PostProcessSettings.bloom_dirt_mask_intensity(value: float) -> None
unreal.PostProcessSettings.bloom_dirt_mask_tint(value: LinearColor) -> None
unreal.PostProcessSettings.bloom_intensity(value: float) -> None
unreal.PostProcessSettings.bloom_method(value: BloomMethod) -> None
unreal.PostProcessSettings.bloom_size_scale(value: float) -> None
unreal.PostProcessSettings.bloom_threshold(value: float) -> None
unreal.PostProcessSettings.blue_correction(value: float) -> None
unreal.PostProcessSettings.camera_iso(value: float) -> None
unreal.PostProcessSettings.camera_shutter_speed(value: float) -> None
unreal.PostProcessSettings.chromatic_aberration_start_offset(value: float) -> None
unreal.PostProcessSettings.color_contrast(value: Vector4) -> None
unreal.PostProcessSettings.color_contrast_highlights(value: Vector4) -> None
unreal.PostProcessSettings.color_contrast_midtones(value: Vector4) -> None
unreal.PostProcessSettings.color_contrast_shadows(value: Vector4) -> None
unreal.PostProcessSettings.color_correction_highlights_max(value: float) -> None
unreal.PostProcessSettings.color_correction_highlights_min(value: float) -> None
unreal.PostProcessSettings.color_correction_shadows_max(value: float) -> None
unreal.PostProcessSettings.color_gain(value: Vector4) -> None
unreal.PostProcessSettings.color_gain_highlights(value: Vector4) -> None
unreal.PostProcessSettings.color_gain_midtones(value: Vector4) -> None
unreal.PostProcessSettings.color_gain_shadows(value: Vector4) -> None
unreal.PostProcessSettings.color_gamma(value: Vector4) -> None
unreal.PostProcessSettings.color_gamma_highlights(value: Vector4) -> None
unreal.PostProcessSettings.color_gamma_midtones(value: Vector4) -> None
unreal.PostProcessSettings.color_gamma_shadows(value: Vector4) -> None
unreal.PostProcessSettings.color_grading_intensity(value: float) -> None
unreal.PostProcessSettings.color_grading_lut(value: Texture) -> None
unreal.PostProcessSettings.color_offset(value: Vector4) -> None
unreal.PostProcessSettings.color_offset_highlights(value: Vector4) -> None
unreal.PostProcessSettings.color_offset_midtones(value: Vector4) -> None
unreal.PostProcessSettings.color_offset_shadows(value: Vector4) -> None
unreal.PostProcessSettings.color_saturation(value: Vector4) -> None
unreal.PostProcessSettings.color_saturation_highlights(value: Vector4) -> None
unreal.PostProcessSettings.color_saturation_midtones(value: Vector4) -> None
unreal.PostProcessSettings.color_saturation_shadows(value: Vector4) -> None
unreal.PostProcessSettings.depth_of_field_blade_count(value: int) -> None
unreal.PostProcessSettings.depth_of_field_depth_blur_amount(value: float) -> None
unreal.PostProcessSettings.depth_of_field_depth_blur_radius(value: float) -> None
unreal.PostProcessSettings.depth_of_field_far_blur_size(value: float) -> None
unreal.PostProcessSettings.depth_of_field_far_transition_region(value: float) -> None
unreal.PostProcessSettings.depth_of_field_focal_distance(value: float) -> None
unreal.PostProcessSettings.depth_of_field_focal_region(value: float) -> None
unreal.PostProcessSettings.depth_of_field_fstop(value: float) -> None
unreal.PostProcessSettings.depth_of_field_min_fstop(value: float) -> None
unreal.PostProcessSettings.depth_of_field_near_blur_size(value: float) -> None
unreal.PostProcessSettings.depth_of_field_near_transition_region(value: float) -> None
unreal.PostProcessSettings.depth_of_field_occlusion(value: float) -> None
unreal.PostProcessSettings.depth_of_field_scale(value: float) -> None
unreal.PostProcessSettings.depth_of_field_sensor_width(value: float) -> None
unreal.PostProcessSettings.depth_of_field_sky_focus_distance(value: float) -> None
unreal.PostProcessSettings.depth_of_field_squeeze_factor(value: float) -> None
unreal.PostProcessSettings.depth_of_field_use_hair_depth(value: bool) -> None
unreal.PostProcessSettings.depth_of_field_vignette_size(value: float) -> None
unreal.PostProcessSettings.dynamic_global_illumination_method(value: DynamicGlobalIlluminationMethod) -> None
unreal.PostProcessSettings.expand_gamut(value: float) -> None
unreal.PostProcessSettings.exposure_offset(value: float) -> None
unreal.PostProcessSettings.eye_adaptation_high_percent(value: float) -> None
unreal.PostProcessSettings.eye_adaptation_low_percent(value: float) -> None
unreal.PostProcessSettings.eye_adaptation_max_brightness(value: float) -> None
unreal.PostProcessSettings.eye_adaptation_min_brightness(value: float) -> None
unreal.PostProcessSettings.eye_adaption_speed_down(value: float) -> None
unreal.PostProcessSettings.eye_adaption_speed_up(value: float) -> None
unreal.PostProcessSettings.film_black_clip(value: float) -> None
unreal.PostProcessSettings.film_grain_highlights_max(value: float) -> None
unreal.PostProcessSettings.film_grain_highlights_min(value: float) -> None
unreal.PostProcessSettings.film_grain_intensity(value: float) -> None
unreal.PostProcessSettings.film_grain_intensity_highlights(value: float) -> None
unreal.PostProcessSettings.film_grain_intensity_midtones(value: float) -> None
unreal.PostProcessSettings.film_grain_intensity_shadows(value: float) -> None
unreal.PostProcessSettings.film_grain_shadows_max(value: float) -> None
unreal.PostProcessSettings.film_grain_texel_size(value: float) -> None
unreal.PostProcessSettings.film_grain_texture(value: Texture2D) -> None
unreal.PostProcessSettings.film_shoulder(value: float) -> None
unreal.PostProcessSettings.film_slope(value: float) -> None
unreal.PostProcessSettings.film_toe(value: float) -> None
unreal.PostProcessSettings.film_white_clip(value: float) -> None
unreal.PostProcessSettings.histogram_log_max(value: float) -> None
unreal.PostProcessSettings.histogram_log_min(value: float) -> None
unreal.PostProcessSettings.indirect_lighting_color(value: LinearColor) -> None
unreal.PostProcessSettings.indirect_lighting_intensity(value: float) -> None
unreal.PostProcessSettings.lens_flare_bokeh_shape(value: Texture) -> None
unreal.PostProcessSettings.lens_flare_bokeh_size(value: float) -> None
unreal.PostProcessSettings.lens_flare_intensity(value: float) -> None
unreal.PostProcessSettings.lens_flare_threshold(value: float) -> None
unreal.PostProcessSettings.lens_flare_tint(value: LinearColor) -> None
unreal.PostProcessSettings.local_exposure_blurred_luminance_blend(value: float) -> None
unreal.PostProcessSettings.local_exposure_blurred_luminance_kernel_size_percent(value: float) -> None
unreal.PostProcessSettings.local_exposure_detail_strength(value: float) -> None
unreal.PostProcessSettings.local_exposure_highlight_contrast_curve(value: CurveFloat) -> None
unreal.PostProcessSettings.local_exposure_highlight_contrast_scale(value: float) -> None
unreal.PostProcessSettings.local_exposure_highlight_threshold(value: float) -> None
unreal.PostProcessSettings.local_exposure_method(value: LocalExposureMethod) -> None
unreal.PostProcessSettings.local_exposure_middle_grey_bias(value: float) -> None
unreal.PostProcessSettings.local_exposure_shadow_contrast_curve(value: CurveFloat) -> None
unreal.PostProcessSettings.local_exposure_shadow_contrast_scale(value: float) -> None
unreal.PostProcessSettings.local_exposure_shadow_threshold(value: float) -> None
unreal.PostProcessSettings.lumen_diffuse_color_boost(value: float) -> None
unreal.PostProcessSettings.lumen_final_gather_lighting_update_speed(value: float) -> None
unreal.PostProcessSettings.lumen_final_gather_quality(value: float) -> None
unreal.PostProcessSettings.lumen_final_gather_screen_traces(value: bool) -> None
unreal.PostProcessSettings.lumen_front_layer_translucency_reflections(value: bool) -> None
unreal.PostProcessSettings.lumen_full_skylight_leaking_distance(value: float) -> None
unreal.PostProcessSettings.lumen_max_reflection_bounces(value: int) -> None
unreal.PostProcessSettings.lumen_max_refraction_bounces(value: int) -> None
unreal.PostProcessSettings.lumen_max_roughness_to_trace_reflections(value: float) -> None
unreal.PostProcessSettings.lumen_max_trace_distance(value: float) -> None
unreal.PostProcessSettings.lumen_ray_lighting_mode(value: LumenRayLightingModeOverride) -> None
unreal.PostProcessSettings.lumen_reflection_quality(value: float) -> None
unreal.PostProcessSettings.lumen_reflections_screen_traces(value: bool) -> None
unreal.PostProcessSettings.lumen_scene_detail(value: float) -> None
unreal.PostProcessSettings.lumen_scene_lighting_quality(value: float) -> None
unreal.PostProcessSettings.lumen_scene_lighting_update_speed(value: float) -> None
unreal.PostProcessSettings.lumen_scene_view_distance(value: float) -> None
unreal.PostProcessSettings.lumen_skylight_leaking(value: float) -> None
unreal.PostProcessSettings.lumen_surface_cache_resolution(value: float) -> None
unreal.PostProcessSettings.mega_lights(value: bool) -> None
unreal.PostProcessSettings.mobile_hq_gaussian(value: bool) -> None
unreal.PostProcessSettings.motion_blur_amount(value: float) -> None
unreal.PostProcessSettings.motion_blur_max(value: float) -> None
unreal.PostProcessSettings.motion_blur_per_object_size(value: float) -> None
unreal.PostProcessSettings.motion_blur_target_fps(value: int) -> None
unreal.PostProcessSettings.override_ambient_cubemap_intensity(value: bool) -> None
unreal.PostProcessSettings.override_ambient_cubemap_tint(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_bias(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_fade_distance(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_fade_radius(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_intensity(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_mip_blend(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_mip_scale(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_mip_threshold(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_power(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_quality(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_radius(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_radius_in_ws(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_static_fraction(value: bool) -> None
unreal.PostProcessSettings.override_ambient_occlusion_temporal_blend_weight(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_apply_physical_camera_exposure(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_bias(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_bias_curve(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_high_percent(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_low_percent(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_max_brightness(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_meter_mask(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_method(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_min_brightness(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_speed_down(value: bool) -> None
unreal.PostProcessSettings.override_auto_exposure_speed_up(value: bool) -> None
unreal.PostProcessSettings.override_b_mega_lights(value: bool) -> None
unreal.PostProcessSettings.override_bloom1_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom1_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom2_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom2_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom3_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom3_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom4_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom4_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom5_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom5_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom6_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom6_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_buffer_scale(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_center_uv(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_pre_filter_max(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_pre_filter_min(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_pre_filter_mult(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_scatter_dispersion(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_size(value: bool) -> None
unreal.PostProcessSettings.override_bloom_convolution_texture(value: bool) -> None
unreal.PostProcessSettings.override_bloom_dirt_mask(value: bool) -> None
unreal.PostProcessSettings.override_bloom_dirt_mask_intensity(value: bool) -> None
unreal.PostProcessSettings.override_bloom_dirt_mask_tint(value: bool) -> None
unreal.PostProcessSettings.override_bloom_intensity(value: bool) -> None
unreal.PostProcessSettings.override_bloom_method(value: bool) -> None
unreal.PostProcessSettings.override_bloom_size_scale(value: bool) -> None
unreal.PostProcessSettings.override_bloom_threshold(value: bool) -> None
unreal.PostProcessSettings.override_blue_correction(value: bool) -> None
unreal.PostProcessSettings.override_camera_iso(value: bool) -> None
unreal.PostProcessSettings.override_camera_shutter_speed(value: bool) -> None
unreal.PostProcessSettings.override_chromatic_aberration_start_offset(value: bool) -> None
unreal.PostProcessSettings.override_color_contrast(value: bool) -> None
unreal.PostProcessSettings.override_color_contrast_highlights(value: bool) -> None
unreal.PostProcessSettings.override_color_contrast_midtones(value: bool) -> None
unreal.PostProcessSettings.override_color_contrast_shadows(value: bool) -> None
unreal.PostProcessSettings.override_color_correction_highlights_max(value: bool) -> None
unreal.PostProcessSettings.override_color_correction_highlights_min(value: bool) -> None
unreal.PostProcessSettings.override_color_correction_shadows_max(value: bool) -> None
unreal.PostProcessSettings.override_color_gain(value: bool) -> None
unreal.PostProcessSettings.override_color_gain_highlights(value: bool) -> None
unreal.PostProcessSettings.override_color_gain_midtones(value: bool) -> None
unreal.PostProcessSettings.override_color_gain_shadows(value: bool) -> None
unreal.PostProcessSettings.override_color_gamma(value: bool) -> None
unreal.PostProcessSettings.override_color_gamma_highlights(value: bool) -> None
unreal.PostProcessSettings.override_color_gamma_midtones(value: bool) -> None
unreal.PostProcessSettings.override_color_gamma_shadows(value: bool) -> None
unreal.PostProcessSettings.override_color_grading_intensity(value: bool) -> None
unreal.PostProcessSettings.override_color_grading_lut(value: bool) -> None
unreal.PostProcessSettings.override_color_offset(value: bool) -> None
unreal.PostProcessSettings.override_color_offset_highlights(value: bool) -> None
unreal.PostProcessSettings.override_color_offset_midtones(value: bool) -> None
unreal.PostProcessSettings.override_color_offset_shadows(value: bool) -> None
unreal.PostProcessSettings.override_color_saturation(value: bool) -> None
unreal.PostProcessSettings.override_color_saturation_highlights(value: bool) -> None
unreal.PostProcessSettings.override_color_saturation_midtones(value: bool) -> None
unreal.PostProcessSettings.override_color_saturation_shadows(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_blade_count(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_depth_blur_amount(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_depth_blur_radius(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_far_blur_size(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_far_transition_region(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_focal_distance(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_focal_region(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_fstop(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_min_fstop(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_near_blur_size(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_near_transition_region(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_occlusion(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_scale(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_sensor_width(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_sky_focus_distance(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_squeeze_factor(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_use_hair_depth(value: bool) -> None
unreal.PostProcessSettings.override_depth_of_field_vignette_size(value: bool) -> None
unreal.PostProcessSettings.override_dynamic_global_illumination_method(value: bool) -> None
unreal.PostProcessSettings.override_expand_gamut(value: bool) -> None
unreal.PostProcessSettings.override_film_black_clip(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_highlights_max(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_highlights_min(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_intensity(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_intensity_highlights(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_intensity_midtones(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_intensity_shadows(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_shadows_max(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_texel_size(value: bool) -> None
unreal.PostProcessSettings.override_film_grain_texture(value: bool) -> None
unreal.PostProcessSettings.override_film_shoulder(value: bool) -> None
unreal.PostProcessSettings.override_film_slope(value: bool) -> None
unreal.PostProcessSettings.override_film_toe(value: bool) -> None
unreal.PostProcessSettings.override_film_white_clip(value: bool) -> None
unreal.PostProcessSettings.override_histogram_log_max(value: bool) -> None
unreal.PostProcessSettings.override_histogram_log_min(value: bool) -> None
unreal.PostProcessSettings.override_indirect_lighting_color(value: bool) -> None
unreal.PostProcessSettings.override_indirect_lighting_intensity(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_bokeh_shape(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_bokeh_size(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_intensity(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_threshold(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_tint(value: bool) -> None
unreal.PostProcessSettings.override_lens_flare_tints(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_blurred_luminance_blend(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_blurred_luminance_kernel_size_percent(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_detail_strength(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_highlight_contrast_curve(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_highlight_contrast_scale(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_highlight_threshold(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_method(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_middle_grey_bias(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_shadow_contrast_curve(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_shadow_contrast_scale(value: bool) -> None
unreal.PostProcessSettings.override_local_exposure_shadow_threshold(value: bool) -> None
unreal.PostProcessSettings.override_lumen_diffuse_color_boost(value: bool) -> None
unreal.PostProcessSettings.override_lumen_final_gather_lighting_update_speed(value: bool) -> None
unreal.PostProcessSettings.override_lumen_final_gather_quality(value: bool) -> None
unreal.PostProcessSettings.override_lumen_final_gather_screen_traces(value: bool) -> None
unreal.PostProcessSettings.override_lumen_front_layer_translucency_reflections(value: bool) -> None
unreal.PostProcessSettings.override_lumen_full_skylight_leaking_distance(value: bool) -> None
unreal.PostProcessSettings.override_lumen_max_reflection_bounces(value: bool) -> None
unreal.PostProcessSettings.override_lumen_max_refraction_bounces(value: bool) -> None
unreal.PostProcessSettings.override_lumen_max_roughness_to_trace_reflections(value: bool) -> None
unreal.PostProcessSettings.override_lumen_max_trace_distance(value: bool) -> None
unreal.PostProcessSettings.override_lumen_ray_lighting_mode(value: bool) -> None
unreal.PostProcessSettings.override_lumen_reflection_quality(value: bool) -> None
unreal.PostProcessSettings.override_lumen_reflections_screen_traces(value: bool) -> None
unreal.PostProcessSettings.override_lumen_scene_detail(value: bool) -> None
unreal.PostProcessSettings.override_lumen_scene_lighting_quality(value: bool) -> None
unreal.PostProcessSettings.override_lumen_scene_lighting_update_speed(value: bool) -> None
unreal.PostProcessSettings.override_lumen_scene_view_distance(value: bool) -> None
unreal.PostProcessSettings.override_lumen_skylight_leaking(value: bool) -> None
unreal.PostProcessSettings.override_lumen_surface_cache_resolution(value: bool) -> None
unreal.PostProcessSettings.override_mobile_hq_gaussian(value: bool) -> None
unreal.PostProcessSettings.override_motion_blur_amount(value: bool) -> None
unreal.PostProcessSettings.override_motion_blur_max(value: bool) -> None
unreal.PostProcessSettings.override_motion_blur_per_object_size(value: bool) -> None
unreal.PostProcessSettings.override_motion_blur_target_fps(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_enable_denoiser(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_enable_emissive_materials(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_enable_reference_atmosphere(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_enable_reference_dof(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_diffuse(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_emissive(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_indirect_diffuse(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_indirect_specular(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_indirect_volume(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_specular(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_include_volume(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_max_bounces(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_max_path_intensity(value: bool) -> None
unreal.PostProcessSettings.override_path_tracing_samples_per_pixel(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_ao(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_ao_intensity(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_ao_radius(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_ao_samples_per_pixel(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_gi(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_gi_max_bounces(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_gi_samples_per_pixel(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_reflections_max_bounces(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_reflections_max_roughness(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_reflections_samples_per_pixel(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_reflections_shadows(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_reflections_translucency(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_translucency_max_roughness(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_translucency_refraction(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_translucency_refraction_rays(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_translucency_samples_per_pixel(value: bool) -> None
unreal.PostProcessSettings.override_ray_tracing_translucency_shadows(value: bool) -> None
unreal.PostProcessSettings.override_reflection_method(value: bool) -> None
unreal.PostProcessSettings.override_scene_color_tint(value: bool) -> None
unreal.PostProcessSettings.override_scene_fringe_intensity(value: bool) -> None
unreal.PostProcessSettings.override_screen_space_reflection_intensity(value: bool) -> None
unreal.PostProcessSettings.override_screen_space_reflection_max_roughness(value: bool) -> None
unreal.PostProcessSettings.override_screen_space_reflection_quality(value: bool) -> None
unreal.PostProcessSettings.override_screen_space_reflection_roughness_scale(value: bool) -> None
unreal.PostProcessSettings.override_sharpen(value: bool) -> None
unreal.PostProcessSettings.override_temperature_type(value: bool) -> None
unreal.PostProcessSettings.override_tone_curve_amount(value: bool) -> None
unreal.PostProcessSettings.override_translucency_type(value: bool) -> None
unreal.PostProcessSettings.override_user_flags(value: bool) -> None
unreal.PostProcessSettings.override_vignette_intensity(value: bool) -> None
unreal.PostProcessSettings.override_white_temp(value: bool) -> None
unreal.PostProcessSettings.override_white_tint(value: bool) -> None
unreal.PostProcessSettings.path_tracing_enable_denoiser(value: bool) -> None
unreal.PostProcessSettings.path_tracing_enable_emissive_materials(value: bool) -> None
unreal.PostProcessSettings.path_tracing_enable_reference_atmosphere(value: bool) -> None
unreal.PostProcessSettings.path_tracing_enable_reference_dof(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_diffuse(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_emissive(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_indirect_diffuse(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_indirect_specular(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_indirect_volume(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_specular(value: bool) -> None
unreal.PostProcessSettings.path_tracing_include_volume(value: bool) -> None
unreal.PostProcessSettings.path_tracing_max_bounces(value: int) -> None
unreal.PostProcessSettings.path_tracing_max_path_intensity(value: float) -> None
unreal.PostProcessSettings.path_tracing_samples_per_pixel(value: int) -> None
unreal.PostProcessSettings.ray_tracing_ao(value: bool) -> None
unreal.PostProcessSettings.ray_tracing_ao_intensity(value: float) -> None
unreal.PostProcessSettings.ray_tracing_ao_radius(value: float) -> None
unreal.PostProcessSettings.ray_tracing_ao_samples_per_pixel(value: int) -> None
unreal.PostProcessSettings.ray_tracing_translucency_max_roughness(value: float) -> None
unreal.PostProcessSettings.ray_tracing_translucency_refraction(value: bool) -> None
unreal.PostProcessSettings.ray_tracing_translucency_refraction_rays(value: int) -> None
unreal.PostProcessSettings.ray_tracing_translucency_samples_per_pixel(value: int) -> None
unreal.PostProcessSettings.ray_tracing_translucency_shadows(value: ReflectedAndRefractedRayTracedShadows) -> None
unreal.PostProcessSettings.reflection_method(value: ReflectionMethod) -> None
unreal.PostProcessSettings.scene_color_tint(value: LinearColor) -> None
unreal.PostProcessSettings.scene_fringe_intensity(value: float) -> None
unreal.PostProcessSettings.screen_space_reflection_intensity(value: float) -> None
unreal.PostProcessSettings.screen_space_reflection_max_roughness(value: float) -> None
unreal.PostProcessSettings.screen_space_reflection_quality(value: float) -> None
unreal.PostProcessSettings.sharpen(value: float) -> None
unreal.PostProcessSettings.temperature_type(value: TemperatureMethod) -> None
unreal.PostProcessSettings.tone_curve_amount(value: float) -> None
unreal.PostProcessSettings.translucency_type(value: TranslucencyType) -> None
unreal.PostProcessSettings.user_flags(value: int) -> None
unreal.PostProcessSettings.vignette_intensity(value: float) -> None
unreal.PostProcessSettings.weighted_blendables(value: WeightedBlendables) -> None
unreal.PostProcessSettings.white_temp(value: float) -> None
unreal.PostProcessSettings.white_tint(value: float) -> None
```

## `unreal.PostProcessVolume(Volume)`

```python
unreal.PostProcessVolume.add_or_update_blendable(blendable_object: BlendableInterface, weight: float = 1.000000) -> None
unreal.PostProcessVolume.blend_radius(value: float) -> None
unreal.PostProcessVolume.blend_weight(value: float) -> None
unreal.PostProcessVolume.enabled(value: bool) -> None
unreal.PostProcessVolume.priority(value: float) -> None
unreal.PostProcessVolume.settings(value: PostProcessSettings) -> None
unreal.PostProcessVolume.unbound(value: bool) -> None
```

## `unreal.PythonMaterialInfosDelegate(DelegateBase)`

```python
unreal.PythonMaterialInfosDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PythonMaterialLib(BlueprintFunctionLibrary)`

```python
unreal.PythonMaterialLib.add_input_at_expression_set_material_attributes(expression_set_material_attributes: MaterialExpressionSetMaterialAttributes, property_str: str) -> None
unreal.PythonMaterialLib.add_output_at_expression_get_material_attributes(expression_get_material_attributes: MaterialExpressionGetMaterialAttributes, property_str: str) -> None
unreal.PythonMaterialLib.connect_material_expressions(from_expression: MaterialExpression, from_output_name: str, to_expression: MaterialExpression, to_input_name: str) -> bool
unreal.PythonMaterialLib.connect_material_property(from_expression: MaterialExpression, from_output_name: str, material_property_str: str) -> bool
unreal.PythonMaterialLib.disconnect_expression(expression: MaterialExpression, input_name: str) -> bool
unreal.PythonMaterialLib.disconnect_material_property(material: Material, material_property_str: str) -> bool
unreal.PythonMaterialLib.gen_guid_from_material_property_str(property_str: str) -> Guid
unreal.PythonMaterialLib.get_all_referenced_expressions(material_interface: MaterialInterface, feature_level: int = 3) -> Array[MaterialExpression]
unreal.PythonMaterialLib.get_editing_materials_from_mat(object: Object) -> Array[Material]
unreal.PythonMaterialLib.get_hlsl_code(material_interface: MaterialInterface) -> Optional[str]
unreal.PythonMaterialLib.get_material_connections(material_interface: MaterialInterface) -> Array[TAPythonMaterialConnection]
unreal.PythonMaterialLib.get_material_content(material: Material, only_editable: bool = True, include_comments: bool = False) -> str
unreal.PythonMaterialLib.get_material_expression_captions(expression: MaterialExpression) -> Array[str]
unreal.PythonMaterialLib.get_material_expression_id(expression: MaterialExpression) -> Guid
unreal.PythonMaterialLib.get_material_expression_input_names(expression: MaterialExpression, raw_name: bool = False) -> Array[str]
unreal.PythonMaterialLib.get_material_expression_output_names(expression: MaterialExpression) -> Array[str]
unreal.PythonMaterialLib.get_material_expressions(material_interface: MaterialInterface) -> Array[MaterialExpression]
unreal.PythonMaterialLib.get_material_function_connections(material_function: MaterialFunction) -> Array[TAPythonMaterialConnection]
unreal.PythonMaterialLib.get_material_function_content(material_function: MaterialFunction, only_editable: bool = True, include_comments: bool = False) -> str
unreal.PythonMaterialLib.get_material_function_expressions(material_function: MaterialFunction, recursive: bool = False) -> Array[MaterialExpression]
unreal.PythonMaterialLib.get_material_function_output_expressions(material_function: MaterialFunction) -> Array[MaterialExpressionFunctionOutput]
unreal.PythonMaterialLib.get_material_proper_str_from_guid(guid: Guid) -> str
unreal.PythonMaterialLib.get_mf_static_switch_parameter(material_function: MaterialFunction) -> Array[StaticSwitchInfo]
unreal.PythonMaterialLib.get_selected_material_nodes(material: Material) -> Array[MaterialExpression]
unreal.PythonMaterialLib.get_selected_nodes_in_material_editor(material_or_mf: Object) -> Array[MaterialExpression]
unreal.PythonMaterialLib.get_shader_map_info(material: Material, platform_str: str, detail: bool = False) -> str
unreal.PythonMaterialLib.get_static_parameters_summary(material_instance: MaterialInstance) -> Tuple[Array[int], Array[str]]
unreal.PythonMaterialLib.get_static_switch_parameter_values(material_interface: MaterialInterface) -> Array[StaticSwitchInfo]
unreal.PythonMaterialLib.log_editing_nodes(material_or_mf: Object) -> None
unreal.PythonMaterialLib.log_mat(material_interface: MaterialInterface) -> None
unreal.PythonMaterialLib.log_mat_deep_first(material_interface: MaterialInterface) -> None
unreal.PythonMaterialLib.log_mat_parameters(material_interface: MaterialInterface) -> Array[str]
unreal.PythonMaterialLib.log_material_expression(material_expression: MaterialExpression) -> None
unreal.PythonMaterialLib.log_mf(material_function: MaterialFunction) -> None
unreal.PythonMaterialLib.set_shading_model(material: Material, shading_model_value: int) -> None
unreal.PythonMaterialLib.set_static_switch_parameter_value(material_instance: MaterialInstanceConstant, switch_name: str, enabled: bool, update_static_permutation: bool = True) -> None
unreal.PythonMaterialLib.set_static_switch_parameters_values(material_instance: MaterialInstanceConstant, switch_names: Array[str], values: Array[bool], overrides: Array[bool]) -> None
```

## `unreal.PythonTextureLib(BlueprintFunctionLibrary)`

```python
unreal.PythonTextureLib.compress_image_array(image_width: int, image_height: int, src_data: Array[Color]) -> Array[int]
unreal.PythonTextureLib.create_texture2d(width: int, height: int, use_srgb: bool = False, texture_filter_value: int = -1, texture_source_format: int = 2) -> Texture2D
unreal.PythonTextureLib.create_texture2d_from_raw(raw_data: Array[int], width: int, height: int, channel_num: int, use_srgb: bool = False, texture_filter_value: int = -1, bgr: bool = False, flip_y: bool = False) -> Texture2D
unreal.PythonTextureLib.finish_compilation_texture(texture: Texture2D) -> Texture2D
unreal.PythonTextureLib.get_pixel_at_texture2d_array(texture_array: Texture2DArray, slice_index: int, x: int, y: int) -> Optional[Array[int]]
unreal.PythonTextureLib.get_render_target_raw_data(render_target_texture: TextureRenderTarget2D) -> Array[int]
unreal.PythonTextureLib.get_textexture2d_array_size(texture_array: Texture2DArray) -> Array[int]
unreal.PythonTextureLib.get_texture2d_array_content(texture_array: Texture2DArray, index: int) -> Optional[Array[int]]
unreal.PythonTextureLib.get_texture2d_content(texture: Texture2D, mip_level: int) -> Optional[Array[int]]
unreal.PythonTextureLib.png_compress_image_array(image_width: int, image_height: int, src_data: Array[Color]) -> Array[int]
unreal.PythonTextureLib.set_image_data_from_memory(texture_array: Texture2DArray, slice_index: int, address: int, length: int, width: int, height: int, channel_num: int = 4, bgr: bool = True) -> bool
unreal.PythonTextureLib.set_render_target_data(render_target_texture: TextureRenderTarget2D, raw_data: Array[int], raw_data_width: int, raw_data_height: int, raw_data_channel_num: int, use_srgb: bool = False, texture_filter_value: int = -1, bgr: bool = False, flip_y: bool = False) -> None
unreal.PythonTextureLib.set_texture2d_array_data_at(texture_array: Texture2DArray, slice_index: int, pos_x: int, pos_y: int, address: int, length: int, width: int, height: int, bgr: bool = True) -> bool
unreal.PythonTextureLib.set_texture2d_array_data_from_memory(texture_array: Texture2DArray, each_layer_addresses: Array[int], length: int, width: int, height: int, channel_num: int = 4, bgr: bool = True) -> bool
unreal.PythonTextureLib.set_texture2d_array_rhi_slice(texture2d_array: Texture2DArray, slice_index: int, address: int, length: int, bgr: bool = False) -> bool
unreal.PythonTextureLib.set_texture2d_array_rhi_slices(texture2d_array: Texture2DArray, each_layer_addresses: Array[int], length: int, bgr: bool = False) -> bool
unreal.PythonTextureLib.set_texture2d_array_slice(texture_array: Texture2DArray, slice_index: int, texture: Texture2D) -> bool
unreal.PythonTextureLib.set_texture_array_render_target2d(render_target: TextureRenderTarget2DArray, slice: int) -> bool
unreal.PythonTextureLib.set_texture_render_target2d_array_format(texture_array: TextureRenderTarget2DArray, format: PixelFormat) -> bool
```

## `unreal.RasterOverlayRendererOptions(StructBase)`

```python
unreal.RasterOverlayRendererOptions.__init__(filter: TextureFilter = TextureFilter.TF_NEAREST, group: TextureGroup = TextureGroup.TEXTUREGROUP_WORLD, use_mipmaps: bool = False) -> None
unreal.RasterOverlayRendererOptions.filter(value: TextureFilter) -> None
unreal.RasterOverlayRendererOptions.group(value: TextureGroup) -> None
unreal.RasterOverlayRendererOptions.use_mipmaps(value: bool) -> None
```

## `unreal.RectLight(Light)`

```python
unreal.RectLight.rect_light_component() -> RectLightComponent
```

## `unreal.RectLightComponent(LocalLightComponent)`

```python
unreal.RectLightComponent.barn_door_angle() -> float
unreal.RectLightComponent.barn_door_length() -> float
unreal.RectLightComponent.light_function_cone_angle() -> float
unreal.RectLightComponent.set_barn_door_angle(new_value: float) -> None
unreal.RectLightComponent.set_barn_door_length(new_value: float) -> None
unreal.RectLightComponent.set_source_height(new_value: float) -> None
unreal.RectLightComponent.set_source_texture(new_value: Texture) -> None
unreal.RectLightComponent.set_source_width(new_value: float) -> None
unreal.RectLightComponent.source_height() -> float
unreal.RectLightComponent.source_texture() -> Texture
unreal.RectLightComponent.source_width() -> float
```

## `unreal.RenderingLibrary(BlueprintFunctionLibrary)`

```python
unreal.RenderingLibrary.begin_draw_canvas_to_render_target(world_context_object: Object, texture_render_target: TextureRenderTarget2D) -> Tuple[Canvas, Vector2D, DrawToRenderTargetContext]
unreal.RenderingLibrary.calculate_projection_matrix(minimal_view_info: MinimalViewInfo) -> Matrix
unreal.RenderingLibrary.clear_render_target2d(world_context_object: Object, texture_render_target: TextureRenderTarget2D, clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
unreal.RenderingLibrary.convert_render_target_to_texture2d_array_editor_only(world_context_object: Object, render_target: TextureRenderTarget2DArray, texture: Texture2DArray) -> None
unreal.RenderingLibrary.convert_render_target_to_texture2d_editor_only(world_context_object: Object, render_target: TextureRenderTarget2D, texture: Texture2D) -> None
unreal.RenderingLibrary.convert_render_target_to_texture_cube_editor_only(world_context_object: Object, render_target: TextureRenderTargetCube, texture: TextureCube) -> None
unreal.RenderingLibrary.convert_render_target_to_texture_volume_editor_only(world_context_object: Object, render_target: TextureRenderTargetVolume, texture: VolumeTexture) -> None
unreal.RenderingLibrary.create_render_target2d(world_context_object: Object, width: int = 256, height: int = 256, format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_RGBA16F, clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps: bool = False, support_ua_vs: bool = False) -> TextureRenderTarget2D
unreal.RenderingLibrary.create_render_target2d_array(world_context_object: Object, width: int = 256, height: int = 256, slices: int = 1, format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_RGBA16F, clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps: bool = False, support_ua_vs: bool = False) -> TextureRenderTarget2DArray
unreal.RenderingLibrary.create_render_target_volume(world_context_object: Object, width: int = 16, height: int = 16, depth: int = 16, format: TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_RGBA16F, clear_color: LinearColor = [0.000000, 0.000000, 0.000000, 1.000000], auto_generate_mip_maps: bool = False, support_ua_vs: bool = False) -> TextureRenderTargetVolume
unreal.RenderingLibrary.draw_material_to_render_target(world_context_object: Object, texture_render_target: TextureRenderTarget2D, material: MaterialInterface) -> None
unreal.RenderingLibrary.enable_path_tracing(enable_path_tracer: bool) -> None
unreal.RenderingLibrary.end_draw_canvas_to_render_target(world_context_object: Object, context: DrawToRenderTargetContext) -> None
unreal.RenderingLibrary.export_render_target(world_context_object: Object, texture_render_target: TextureRenderTarget2D, file_path: str, file_name: str) -> None
unreal.RenderingLibrary.export_texture2d(world_context_object: Object, texture: Texture2D, file_path: str, file_name: str) -> None
unreal.RenderingLibrary.import_buffer_as_texture2d(world_context_object: Object, buffer: Array[int]) -> Texture2D
unreal.RenderingLibrary.import_file_as_texture2d(world_context_object: Object, filename: str) -> Texture2D
unreal.RenderingLibrary.read_render_target(world_context_object: Object, texture_render_target: TextureRenderTarget2D, normalize: bool = True) -> Optional[Array[Color]]
unreal.RenderingLibrary.read_render_target_pixel(world_context_object: Object, texture_render_target: TextureRenderTarget2D, x: int, y: int) -> Color
unreal.RenderingLibrary.read_render_target_raw(world_context_object: Object, texture_render_target: TextureRenderTarget2D, normalize: bool = True) -> Optional[Array[LinearColor]]
unreal.RenderingLibrary.read_render_target_raw_pixel(world_context_object: Object, texture_render_target: TextureRenderTarget2D, x: int, y: int, normalize: bool = True) -> LinearColor
unreal.RenderingLibrary.read_render_target_raw_pixel_area(world_context_object: Object, texture_render_target: TextureRenderTarget2D, min_x: int, min_y: int, max_x: int, max_y: int, normalize: bool = True) -> Array[LinearColor]
unreal.RenderingLibrary.read_render_target_raw_uv(world_context_object: Object, texture_render_target: TextureRenderTarget2D, u: float, v: float, normalize: bool = True) -> LinearColor
unreal.RenderingLibrary.read_render_target_raw_uv_area(world_context_object: Object, texture_render_target: TextureRenderTarget2D, area: Box2D, normalize: bool = True) -> Array[LinearColor]
unreal.RenderingLibrary.read_render_target_uv(world_context_object: Object, texture_render_target: TextureRenderTarget2D, u: float, v: float) -> Color
unreal.RenderingLibrary.refresh_path_tracing_output() -> None
unreal.RenderingLibrary.release_render_target2d(texture_render_target: TextureRenderTarget2D) -> None
unreal.RenderingLibrary.render_target_create_static_texture2d_array_editor_only(render_target: TextureRenderTarget2DArray, name: str = "Texture", compression_settings: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, mip_settings: TextureMipGenSettings = TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> Texture2DArray
unreal.RenderingLibrary.render_target_create_static_texture2d_editor_only(render_target: TextureRenderTarget2D, name: str = "Texture", compression_settings: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, mip_settings: TextureMipGenSettings = TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> Texture2D
unreal.RenderingLibrary.render_target_create_static_texture_cube_editor_only(render_target: TextureRenderTargetCube, name: str = "Texture", compression_settings: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, mip_settings: TextureMipGenSettings = TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> TextureCube
unreal.RenderingLibrary.render_target_create_static_volume_texture_editor_only(render_target: TextureRenderTargetVolume, name: str = "Texture", compression_settings: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, mip_settings: TextureMipGenSettings = TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP) -> VolumeTexture
unreal.RenderingLibrary.resize_render_target2d(texture_render_target: TextureRenderTarget2D, width: int = 256, height: int = 256) -> None
unreal.RenderingLibrary.set_cast_inset_shadow_for_all_attachments(primitive_component: PrimitiveComponent, cast_inset_shadow: bool, light_attachments_as_group: bool) -> None
```

## `unreal.RigUnit_Control_StaticMesh(RigUnit_Control)`

```python
unreal.RigUnit_Control_StaticMesh.__init__(transform: EulerTransform = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], base: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], init_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], result: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], filter: TransformFilter = [[True, True, True], [True, True, True], [True, True, True]], mesh_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_Control_StaticMesh.mesh_transform(value: Transform) -> None
```

## `unreal.RuntimeVirtualTexture(Object)`

```python
unreal.RuntimeVirtualTexture.compress_textures() -> bool
unreal.RuntimeVirtualTexture.get_page_table_size() -> int
unreal.RuntimeVirtualTexture.get_size() -> int
unreal.RuntimeVirtualTexture.lod_group(value: TextureGroup) -> None
unreal.RuntimeVirtualTexture.material_type() -> RuntimeVirtualTextureMaterialType
unreal.RuntimeVirtualTexture.tile_border_size() -> int
unreal.RuntimeVirtualTexture.tile_count() -> int
unreal.RuntimeVirtualTexture.tile_size() -> int
unreal.RuntimeVirtualTexture.use_low_quality_compression() -> bool
```

## `unreal.RuntimeVirtualTextureComponent(SceneComponent)`

```python
unreal.RuntimeVirtualTextureComponent.invalidate(world_bounds: BoxSphereBounds) -> None
unreal.RuntimeVirtualTextureComponent.lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
unreal.RuntimeVirtualTextureComponent.streaming_mips_fixed_color() -> LinearColor
unreal.RuntimeVirtualTextureComponent.streaming_texture() -> VirtualTextureBuilder
unreal.RuntimeVirtualTextureComponent.use_streaming_mips_fixed_color() -> bool
unreal.RuntimeVirtualTextureComponent.virtual_texture() -> RuntimeVirtualTexture
```

## `unreal.RuntimeVirtualTextureParameterValue(StructBase)`

```python
unreal.RuntimeVirtualTextureParameterValue.__init__(parameter_info: MaterialParameterInfo = ["None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1], parameter_value: RuntimeVirtualTexture = None) -> None
unreal.RuntimeVirtualTextureParameterValue.parameter_info(value: MaterialParameterInfo) -> None
unreal.RuntimeVirtualTextureParameterValue.parameter_value(value: RuntimeVirtualTexture) -> None
```

## `unreal.RuntimeVirtualTextureVolume(Actor)`

```python
unreal.RuntimeVirtualTextureVolume.virtual_texture_component() -> RuntimeVirtualTextureComponent
```

## `unreal.SetGeoLayerHighlightParams(ParamsBase)`

```python
unreal.SetGeoLayerHighlightParams.__init__(eids: Array[str] = [], style_name: str = "", highlight: bool = False) -> None
unreal.SetGeoLayerHighlightParams.eids(value: Array[str]) -> None
unreal.SetGeoLayerHighlightParams.highlight(value: bool) -> None
unreal.SetGeoLayerHighlightParams.style_name(value: str) -> None
```

## `unreal.ShaderFunctionDefinition(StructBase)`

```python
unreal.ShaderFunctionDefinition.__init__() -> None
```

## `unreal.ShaderParamTypeDefinition(StructBase)`

```python
unreal.ShaderParamTypeDefinition.__init__() -> None
```

## `unreal.SkeletalMaterial(StructBase)`

```python
unreal.SkeletalMaterial.__init__(material_interface: MaterialInterface = None, material_slot_name: Name = "None", uv_channel_data: MeshUVChannelInfo = []) -> None
unreal.SkeletalMaterial.material_interface(value: MaterialInterface) -> None
unreal.SkeletalMaterial.material_slot_name(value: Name) -> None
unreal.SkeletalMaterial.uv_channel_data() -> MeshUVChannelInfo
```

## `unreal.SkeletalMesh(SkinnedAsset)`

```python
unreal.SkeletalMesh.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.SkeletalMesh.add_socket(socket: SkeletalMeshSocket, add_to_skeleton: bool = False) -> None
unreal.SkeletalMesh.default_animating_rig(value: Object) -> None
unreal.SkeletalMesh.default_mesh_deformer() -> MeshDeformer
unreal.SkeletalMesh.find_socket_and_index(socket_name: Name) -> Tuple[SkeletalMeshSocket, int]
unreal.SkeletalMesh.get_all_morph_target_names() -> Array[str]
unreal.SkeletalMesh.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.SkeletalMesh.get_bounds() -> BoxSphereBounds
unreal.SkeletalMesh.get_default_mesh_deformer() -> MeshDeformer
unreal.SkeletalMesh.get_imported_bounds() -> BoxSphereBounds
unreal.SkeletalMesh.get_min_lod_for_quality_levels() -> Tuple[Map[PerQualityLevels, int], int]
unreal.SkeletalMesh.get_node_mapping_container(source_asset: Blueprint) -> NodeMappingContainer
unreal.SkeletalMesh.get_overlay_material() -> MaterialInterface
unreal.SkeletalMesh.get_overlay_material_max_draw_distance() -> float
unreal.SkeletalMesh.get_socket_by_index(index: int) -> SkeletalMeshSocket
unreal.SkeletalMesh.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.SkeletalMesh.has_vertex_colors() -> bool
unreal.SkeletalMesh.is_section_using_cloth(section_index: int, check_corresponding_sections: bool = True) -> bool
unreal.SkeletalMesh.lod_settings(value: SkeletalMeshLODSettings) -> None
unreal.SkeletalMesh.materials(value: Array[SkeletalMaterial]) -> None
unreal.SkeletalMesh.mesh_clothing_assets(value: Array[ClothingAssetBase]) -> None
unreal.SkeletalMesh.morph_targets(value: Array[MorphTarget]) -> None
unreal.SkeletalMesh.negative_bounds_extension() -> Vector
unreal.SkeletalMesh.node_mapping_data() -> Array[NodeMappingContainer]
unreal.SkeletalMesh.num_sockets() -> int
unreal.SkeletalMesh.overlay_material() -> MaterialInterface
unreal.SkeletalMesh.overlay_material_max_draw_distance() -> float
unreal.SkeletalMesh.physics_asset() -> PhysicsAsset
unreal.SkeletalMesh.positive_bounds_extension() -> Vector
unreal.SkeletalMesh.post_process_anim_blueprint() -> Class
unreal.SkeletalMesh.regenerate_lod(new_lod_count: int = 0, regenerate_even_if_imported: bool = False, generate_base_lod: bool = False) -> bool
unreal.SkeletalMesh.remove_lo_ds(to_remove_lo_ds: Array[int]) -> bool
unreal.SkeletalMesh.rename_socket(old_name: Name, new_name: Name) -> bool
unreal.SkeletalMesh.set_min_lod_for_quality_levels(quality_level_minimum_lo_ds: Map[PerQualityLevels, int], default: int = -1) -> None
unreal.SkeletalMesh.set_overlay_material(new_overlay_material: MaterialInterface) -> None
unreal.SkeletalMesh.set_overlay_material_max_draw_distance(max_draw_distance: float) -> None
unreal.SkeletalMesh.shadow_physics_asset() -> PhysicsAsset
unreal.SkeletalMesh.skeleton() -> Skeleton
unreal.SkeletalMesh.strip_lod_geometry(lod_index: int, texture_mask: Texture2D, threshold: float) -> bool
```

## `unreal.SkeletalMeshBuildSettings(StructBase)`

```python
unreal.SkeletalMeshBuildSettings.__init__(recompute_normals: bool = False, recompute_tangents: bool = False, use_mikk_t_space: bool = False, compute_weighted_normals: bool = False, remove_degenerates: bool = False, use_high_precision_tangent_basis: bool = False, use_high_precision_skin_weights: bool = False, use_full_precision_u_vs: bool = False, use_backwards_compatible_f16_trunc_u_vs: bool = False, threshold_position: float = 0.000000, threshold_tangent_normal: float = 0.000000, threshold_uv: float = 0.000000, morph_threshold_position: float = 0.000000, bone_influence_limit: int = 0) -> None
unreal.SkeletalMeshBuildSettings.bone_influence_limit(value: int) -> None
unreal.SkeletalMeshBuildSettings.compute_weighted_normals(value: bool) -> None
unreal.SkeletalMeshBuildSettings.morph_threshold_position(value: float) -> None
unreal.SkeletalMeshBuildSettings.recompute_normals(value: bool) -> None
unreal.SkeletalMeshBuildSettings.recompute_tangents(value: bool) -> None
unreal.SkeletalMeshBuildSettings.remove_degenerates(value: bool) -> None
unreal.SkeletalMeshBuildSettings.threshold_position(value: float) -> None
unreal.SkeletalMeshBuildSettings.threshold_tangent_normal(value: float) -> None
unreal.SkeletalMeshBuildSettings.threshold_uv(value: float) -> None
unreal.SkeletalMeshBuildSettings.use_backwards_compatible_f16_trunc_u_vs(value: bool) -> None
unreal.SkeletalMeshBuildSettings.use_full_precision_u_vs(value: bool) -> None
unreal.SkeletalMeshBuildSettings.use_high_precision_skin_weights(value: bool) -> None
unreal.SkeletalMeshBuildSettings.use_high_precision_tangent_basis(value: bool) -> None
unreal.SkeletalMeshBuildSettings.use_mikk_t_space(value: bool) -> None
```

## `unreal.SkeletalMeshComponent(SkinnedMeshComponent)`

```python
unreal.SkeletalMeshComponent.accumulate_all_bodies_below_physics_blend_weight(bone_name: Name, add_physics_blend_weight: float, skip_custom_physics_type: bool = False) -> None
unreal.SkeletalMeshComponent.add_cloth_collision_source(source_component: SkeletalMeshComponent, source_physics_asset: PhysicsAsset) -> None
unreal.SkeletalMeshComponent.add_force_to_all_bodies_below(force: Vector, bone_name: Name = "None", accel_change: bool = False, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.add_impulse_to_all_bodies_below(impulse: Vector, bone_name: Name = "None", vel_change: bool = False, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.allow_anim_curve_evaluation(name_of_curve: Name, allow: bool) -> None
unreal.SkeletalMeshComponent.allow_cloth_actors(value: bool) -> None
unreal.SkeletalMeshComponent.anim_blueprint_generated_class() -> AnimBlueprintGeneratedClass
unreal.SkeletalMeshComponent.anim_class() -> Class
unreal.SkeletalMeshComponent.animation_blueprint() -> AnimBlueprintGeneratedClass
unreal.SkeletalMeshComponent.animation_data(value: SingleAnimationPlayData) -> None
unreal.SkeletalMeshComponent.animation_mode() -> AnimationMode
unreal.SkeletalMeshComponent.b_propagate_curves_to_slaves(value: bool) -> None
unreal.SkeletalMeshComponent.bind_cloth_to_leader_pose_component() -> None
unreal.SkeletalMeshComponent.bind_cloth_to_master_pose_component() -> None
unreal.SkeletalMeshComponent.break_constraint(impulse: Vector, hit_location: Vector, bone_name: Name) -> None
unreal.SkeletalMeshComponent.clear_layer_overlay(class_: Class) -> None
unreal.SkeletalMeshComponent.clear_morph_targets() -> None
unreal.SkeletalMeshComponent.cloth_blend_weight(value: float) -> None
unreal.SkeletalMeshComponent.cloth_geometry_scale(value: float) -> None
unreal.SkeletalMeshComponent.cloth_max_distance_scale(value: float) -> None
unreal.SkeletalMeshComponent.cloth_teleport_mode() -> ClothingTeleportMode
unreal.SkeletalMeshComponent.cloth_velocity_scale(value: float) -> None
unreal.SkeletalMeshComponent.collide_with_attached_children(value: bool) -> None
unreal.SkeletalMeshComponent.collide_with_environment(value: bool) -> None
unreal.SkeletalMeshComponent.default_animating_rig_override(value: Object) -> None
unreal.SkeletalMeshComponent.defer_kinematic_bone_update() -> bool
unreal.SkeletalMeshComponent.disable_cloth_simulation(value: bool) -> None
unreal.SkeletalMeshComponent.disable_post_process_blueprint(value: bool) -> None
unreal.SkeletalMeshComponent.enable_animation() -> bool
unreal.SkeletalMeshComponent.enable_per_poly_collision() -> bool
unreal.SkeletalMeshComponent.enable_physics_on_dedicated_server(value: bool) -> None
unreal.SkeletalMeshComponent.find_constraint_bone_name(constraint_index: int) -> Name
unreal.SkeletalMeshComponent.force_cloth_next_update_teleport() -> None
unreal.SkeletalMeshComponent.force_cloth_next_update_teleport_and_reset() -> None
unreal.SkeletalMeshComponent.force_collision_update(value: bool) -> None
unreal.SkeletalMeshComponent.get_allow_cloth_actors() -> bool
unreal.SkeletalMeshComponent.get_allow_rigid_body_anim_node() -> bool
unreal.SkeletalMeshComponent.get_allowed_anim_curve_evaluate() -> bool
unreal.SkeletalMeshComponent.get_anim_instance() -> AnimInstance
unreal.SkeletalMeshComponent.get_animation_mode() -> AnimationMode
unreal.SkeletalMeshComponent.get_bone_linear_velocity(bone_name: Name) -> Vector
unreal.SkeletalMeshComponent.get_bone_mass(bone_name: Name = "None", scale_mass: bool = True) -> float
unreal.SkeletalMeshComponent.get_closest_point_on_physics_asset(world_position: Vector) -> Optional[Tuple[Vector, Vector, Name, float]]
unreal.SkeletalMeshComponent.get_cloth_max_distance_scale() -> float
unreal.SkeletalMeshComponent.get_clothing_simulation_interactor() -> ClothingSimulationInteractor
unreal.SkeletalMeshComponent.get_constraint_by_name(constraint_name: Name, includes_terminated: bool) -> ConstraintInstanceAccessor
unreal.SkeletalMeshComponent.get_constraints(includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
unreal.SkeletalMeshComponent.get_constraints_from_body(body_name: Name, parent_constraints: bool, child_constraints: bool, includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
unreal.SkeletalMeshComponent.get_current_joint_angles(bone_name: Name) -> Tuple[float, float, float]
unreal.SkeletalMeshComponent.get_default_animating_rig() -> Object
unreal.SkeletalMeshComponent.get_disable_anim_curves() -> bool
unreal.SkeletalMeshComponent.get_float_attribute(bone_name: Name, attribute_name: Name, default_value: float, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[float]
unreal.SkeletalMeshComponent.get_float_attribute_ref(bone_name: Name, attribute_name: Name, out_value: float, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[float]
unreal.SkeletalMeshComponent.get_integer_attribute(bone_name: Name, attribute_name: Name, default_value: int, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[int]
unreal.SkeletalMeshComponent.get_integer_attribute_ref(bone_name: Name, attribute_name: Name, out_value: int, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[int]
unreal.SkeletalMeshComponent.get_layer_sub_instance_by_class(class_: Class) -> AnimInstance
unreal.SkeletalMeshComponent.get_layer_sub_instance_by_group(group: Name) -> AnimInstance
unreal.SkeletalMeshComponent.get_linked_anim_graph_instance_by_tag(tag: Name) -> AnimInstance
unreal.SkeletalMeshComponent.get_linked_anim_graph_instances_by_tag(tag: Name) -> Array[AnimInstance]
unreal.SkeletalMeshComponent.get_linked_anim_layer_instance_by_class(class_: Class) -> AnimInstance
unreal.SkeletalMeshComponent.get_linked_anim_layer_instance_by_group(group: Name) -> AnimInstance
unreal.SkeletalMeshComponent.get_morph_target(morph_target_name: Name) -> float
unreal.SkeletalMeshComponent.get_play_rate() -> float
unreal.SkeletalMeshComponent.get_position() -> float
unreal.SkeletalMeshComponent.get_post_process_instance() -> AnimInstance
unreal.SkeletalMeshComponent.get_skeletal_center_of_mass() -> Vector
unreal.SkeletalMeshComponent.get_skeletal_mesh_asset() -> SkeletalMesh
unreal.SkeletalMeshComponent.get_string_attribute(bone_name: Name, attribute_name: Name, default_value: str, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[str]
unreal.SkeletalMeshComponent.get_string_attribute_ref(bone_name: Name, attribute_name: Name, out_value: str, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[str]
unreal.SkeletalMeshComponent.get_sub_instance_by_tag(tag: Name) -> AnimInstance
unreal.SkeletalMeshComponent.get_sub_instances_by_tag(tag: Name) -> Array[AnimInstance]
unreal.SkeletalMeshComponent.get_transform_attribute(bone_name: Name, attribute_name: Name, default_value: Transform, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[Transform]
unreal.SkeletalMeshComponent.get_transform_attribute_ref(bone_name: Name, attribute_name: Name, out_value: Transform, lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.BONE_ONLY) -> Optional[Transform]
unreal.SkeletalMeshComponent.global_anim_rate_scale(value: float) -> None
unreal.SkeletalMeshComponent.has_valid_animation_instance() -> bool
unreal.SkeletalMeshComponent.is_body_gravity_enabled(bone_name: Name) -> bool
unreal.SkeletalMeshComponent.is_clothing_simulation_suspended() -> bool
unreal.SkeletalMeshComponent.is_playing() -> bool
unreal.SkeletalMeshComponent.k2_set_anim_instance_class(new_class: Class) -> None
unreal.SkeletalMeshComponent.kinematic_bones_update_type(value: KinematicBonesUpdateToPhysics) -> None
unreal.SkeletalMeshComponent.link_anim_class_layers(class_: Class) -> None
unreal.SkeletalMeshComponent.link_anim_graph_by_tag(tag: Name, class_: Class) -> None
unreal.SkeletalMeshComponent.no_skeleton_update(value: bool) -> None
unreal.SkeletalMeshComponent.on_anim_initialized(value: OnAnimInitialized) -> None
unreal.SkeletalMeshComponent.on_constraint_broken(value: ConstraintBrokenSignature) -> None
unreal.SkeletalMeshComponent.on_plastic_deformation(value: PlasticDeformationEventSignature) -> None
unreal.SkeletalMeshComponent.override_animation_data(anim_to_play: AnimationAsset, is_looping: bool = True, is_playing: bool = True, position: float = 0.000000, play_rate: float = 1.000000) -> None
unreal.SkeletalMeshComponent.pause_anims(value: bool) -> None
unreal.SkeletalMeshComponent.physics_transform_update_mode(value: PhysicsTransformUpdateMode) -> None
unreal.SkeletalMeshComponent.play(looping: bool) -> None
unreal.SkeletalMeshComponent.play_animation(new_anim_to_play: AnimationAsset, looping: bool) -> None
unreal.SkeletalMeshComponent.post_process_anim_bplod_threshold(value: int) -> None
unreal.SkeletalMeshComponent.propagate_curves_to_followers(value: bool) -> None
unreal.SkeletalMeshComponent.recreate_clothing_actors() -> None
unreal.SkeletalMeshComponent.remove_cloth_collision_source(source_component: SkeletalMeshComponent, source_physics_asset: PhysicsAsset) -> None
unreal.SkeletalMeshComponent.remove_cloth_collision_sources(source_component: SkeletalMeshComponent) -> None
unreal.SkeletalMeshComponent.reset_after_teleport(value: bool) -> None
unreal.SkeletalMeshComponent.reset_all_bodies_simulate_physics() -> None
unreal.SkeletalMeshComponent.reset_allowed_anim_curve_evaluation() -> None
unreal.SkeletalMeshComponent.reset_anim_instance_dynamics(teleport_type: TeleportType = TeleportType.RESET_PHYSICS) -> None
unreal.SkeletalMeshComponent.reset_cloth_collision_sources() -> None
unreal.SkeletalMeshComponent.reset_cloth_teleport_mode() -> None
unreal.SkeletalMeshComponent.resume_clothing_simulation() -> None
unreal.SkeletalMeshComponent.set_all_bodies_below_linear_velocity(bone_name: Name, linear_velocity: Vector, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_all_bodies_below_physics_blend_weight(bone_name: Name, physics_blend_weight: float, skip_custom_physics_type: bool = False, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_all_bodies_below_physics_disabled(bone_name: Name, disabled: bool, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_all_bodies_below_simulate_physics(bone_name: Name, new_simulate: bool, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_all_bodies_physics_blend_weight(physics_blend_weight: float, skip_custom_physics_type: bool = False) -> None
unreal.SkeletalMeshComponent.set_all_bodies_simulate_physics(new_simulate: bool) -> None
unreal.SkeletalMeshComponent.set_all_motors_angular_drive_params(spring: float, damping: float, force_limit: float, skip_custom_physics_type: bool = False) -> None
unreal.SkeletalMeshComponent.set_all_motors_angular_position_drive(enable_swing_drive: bool, enable_twist_drive: bool, skip_custom_physics_type: bool = False) -> None
unreal.SkeletalMeshComponent.set_all_motors_angular_velocity_drive(enable_swing_drive: bool, enable_twist_drive: bool, skip_custom_physics_type: bool = False) -> None
unreal.SkeletalMeshComponent.set_allow_anim_curve_evaluation(allow: bool) -> None
unreal.SkeletalMeshComponent.set_allow_cloth_actors(allow: bool) -> None
unreal.SkeletalMeshComponent.set_allow_rigid_body_anim_node(allow: bool, reinit_anim: bool = True) -> None
unreal.SkeletalMeshComponent.set_allowed_anim_curves_evaluation(list: Array[Name], allow: bool) -> None
unreal.SkeletalMeshComponent.set_angular_limits(bone_name: Name, swing1_limit_angle: float, twist_limit_angle: float, swing2_limit_angle: float) -> None
unreal.SkeletalMeshComponent.set_anim_blueprint(new_class: Class) -> None
unreal.SkeletalMeshComponent.set_anim_class(new_class: Class) -> None
unreal.SkeletalMeshComponent.set_anim_instance_class(new_class: Class) -> None
unreal.SkeletalMeshComponent.set_animation(new_anim_to_play: AnimationAsset) -> None
unreal.SkeletalMeshComponent.set_animation_mode(animation_mode: AnimationMode, force_init_anim_script_instance: bool = True) -> None
unreal.SkeletalMeshComponent.set_body_notify_rigid_body_collision(new_notify_rigid_body_collision: bool, bone_name: Name = "None") -> None
unreal.SkeletalMeshComponent.set_body_simulate_physics(bone_name: Name, simulate: bool) -> None
unreal.SkeletalMeshComponent.set_cloth_max_distance_scale(scale: float) -> None
unreal.SkeletalMeshComponent.set_constraint_profile(joint_name: Name, profile_name: Name, default_if_not_found: bool = False) -> None
unreal.SkeletalMeshComponent.set_constraint_profile_for_all(profile_name: Name, default_if_not_found: bool = False) -> None
unreal.SkeletalMeshComponent.set_disable_anim_curves(disable_anim_curves: bool) -> None
unreal.SkeletalMeshComponent.set_enable_body_gravity(enable_gravity: bool, bone_name: Name) -> None
unreal.SkeletalMeshComponent.set_enable_gravity_on_all_bodies_below(enable_gravity: bool, bone_name: Name, include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_enable_physics_blending(new_blend_physics: bool) -> None
unreal.SkeletalMeshComponent.set_layer_overlay(class_: Class) -> None
unreal.SkeletalMeshComponent.set_morph_target(morph_target_name: Name, value: float, remove_zero_weight: bool = True) -> None
unreal.SkeletalMeshComponent.set_notify_rigid_body_collision_below(new_notify_rigid_body_collision: bool, bone_name: Name = "None", include_self: bool = True) -> None
unreal.SkeletalMeshComponent.set_override_post_process_anim_bp(post_process_anim_blueprint: Class, reinit_anim_instances: bool = True) -> None
unreal.SkeletalMeshComponent.set_physics_blend_weight(physics_blend_weight: float) -> None
unreal.SkeletalMeshComponent.set_play_rate(rate: float) -> None
unreal.SkeletalMeshComponent.set_position(pos: float, fire_notifies: bool = True) -> None
unreal.SkeletalMeshComponent.set_skeletal_mesh_asset(new_mesh: SkeletalMesh) -> None
unreal.SkeletalMeshComponent.set_sub_instance_class_by_tag(tag: Name, class_: Class) -> None
unreal.SkeletalMeshComponent.set_update_animation_in_editor(new_update_state: bool) -> None
unreal.SkeletalMeshComponent.set_update_cloth_in_editor(new_update_state: bool) -> None
unreal.SkeletalMeshComponent.skeletal_mesh_asset(value: SkeletalMesh) -> None
unreal.SkeletalMeshComponent.skip_bounds_update_when_interpolating(value: bool) -> None
unreal.SkeletalMeshComponent.skip_kinematic_update_when_interpolating(value: bool) -> None
unreal.SkeletalMeshComponent.snapshot_pose(snapshot: PoseSnapshot) -> PoseSnapshot
unreal.SkeletalMeshComponent.stop() -> None
unreal.SkeletalMeshComponent.suspend_clothing_simulation() -> None
unreal.SkeletalMeshComponent.teleport_distance_threshold(value: float) -> None
unreal.SkeletalMeshComponent.teleport_rotation_threshold(value: float) -> None
unreal.SkeletalMeshComponent.term_bodies_below(parent_bone_name: Name) -> None
unreal.SkeletalMeshComponent.toggle_disable_post_process_blueprint() -> None
unreal.SkeletalMeshComponent.unbind_cloth_from_leader_pose_component(restore_simulation_space: bool = True) -> None
unreal.SkeletalMeshComponent.unbind_cloth_from_master_pose_component(restore_simulation_space: bool = True) -> None
unreal.SkeletalMeshComponent.unlink_anim_class_layers(class_: Class) -> None
unreal.SkeletalMeshComponent.update_joints_from_animation(value: bool) -> None
unreal.SkeletalMeshComponent.update_mesh_when_kinematic(value: bool) -> None
unreal.SkeletalMeshComponent.wait_for_parallel_cloth_task(value: bool) -> None
```

## `unreal.SkeletalMeshLODGroupSettings(StructBase)`

```python
unreal.SkeletalMeshLODGroupSettings.__init__() -> None
```

## `unreal.SkeletalMeshLODInfo(StructBase)`

```python
unreal.SkeletalMeshLODInfo.__init__() -> None
```

## `unreal.SkeletalMeshOptimizationSettings(StructBase)`

```python
unreal.SkeletalMeshOptimizationSettings.__init__() -> None
```

## `unreal.SkeletalMeshSamplingInfo(StructBase)`

```python
unreal.SkeletalMeshSamplingInfo.__init__() -> None
```

## `unreal.SkeletalMeshSamplingRegion(StructBase)`

```python
unreal.SkeletalMeshSamplingRegion.__init__() -> None
```

## `unreal.SkeletalMeshSamplingRegionBoneFilter(StructBase)`

```python
unreal.SkeletalMeshSamplingRegionBoneFilter.__init__() -> None
```

## `unreal.SkeletalMeshSamplingRegionMaterialFilter(StructBase)`

```python
unreal.SkeletalMeshSamplingRegionMaterialFilter.__init__() -> None
```

## `unreal.SkeletalMeshSocket(Object)`

```python
unreal.SkeletalMeshSocket.bone_name() -> Name
unreal.SkeletalMeshSocket.force_always_animated() -> bool
unreal.SkeletalMeshSocket.get_socket_location(skel_comp: SkeletalMeshComponent) -> Vector
unreal.SkeletalMeshSocket.initialize_socket_from_location(skel_comp: SkeletalMeshComponent, world_location: Vector, world_normal: Vector) -> None
unreal.SkeletalMeshSocket.relative_location() -> Vector
unreal.SkeletalMeshSocket.relative_rotation() -> Rotator
unreal.SkeletalMeshSocket.relative_scale() -> Vector
unreal.SkeletalMeshSocket.socket_name() -> Name
```

## `unreal.SkeletalMeshVertexAttributeInfo(StructBase)`

```python
unreal.SkeletalMeshVertexAttributeInfo.__init__() -> None
```

## `unreal.SkyCreatorLightningParameters(StructBase)`

```python
unreal.SkyCreatorLightningParameters.__init__(position: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.SkyCreatorLightningParameters.color(value: LinearColor) -> None
unreal.SkyCreatorLightningParameters.position(value: LinearColor) -> None
```

## `unreal.SkyCreatorMoonLightSettings(StructBase)`

```python
unreal.SkyCreatorMoonLightSettings.__init__(intensity: float = 0.000000, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], temperature: float = 0.000000, volumetric_scattering_intensity: float = 0.000000, atmosphere_disk_color_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_scattered_luminance_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_shadow_strength: float = 0.000000, cloud_shadow_on_atmosphere_strength: float = 0.000000, cloud_shadow_on_surface_strength: float = 0.000000) -> None
unreal.SkyCreatorMoonLightSettings.atmosphere_disk_color_scale(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings.cloud_scattered_luminance_scale(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings.cloud_shadow_on_atmosphere_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings.cloud_shadow_on_surface_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings.cloud_shadow_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings.intensity(value: float) -> None
unreal.SkyCreatorMoonLightSettings.light_color(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings.temperature(value: float) -> None
unreal.SkyCreatorMoonLightSettings.volumetric_scattering_intensity(value: float) -> None
```

## `unreal.SkyCreatorMoonLightSettings_51(StructBase)`

```python
unreal.SkyCreatorMoonLightSettings_51.__init__(use_intensity: bool = False, intensity: float = 0.000000, intensity_curve: CurveFloat = None, use_light_color: bool = False, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], light_color_curve: CurveLinearColor = None, use_temperature: bool = False, temperature: float = 0.000000, temperature_curve: CurveFloat = None, use_volumetric_scattering_intensity: bool = False, volumetric_scattering_intensity: float = 0.000000, volumetric_scattering_intensity_curve: CurveFloat = None, use_atmosphere_disk_color_scale: bool = False, atmosphere_disk_color_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], atmosphere_disk_color_scale_curve: CurveLinearColor = None, use_cloud_scattered_luminance_scale: bool = False, cloud_scattered_luminance_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_scattered_luminance_scale_curve: CurveLinearColor = None, use_cloud_shadow_strength: bool = False, cloud_shadow_strength: float = 0.000000, cloud_shadow_strength_curve: CurveFloat = None, use_cloud_shadow_on_atmosphere_strength: bool = False, cloud_shadow_on_atmosphere_strength: float = 0.000000, cloud_shadow_on_atmosphere_strength_curve: CurveFloat = None, use_cloud_shadow_on_surface_strength: bool = False, cloud_shadow_on_surface_strength: float = 0.000000, cloud_shadow_on_surface_strength_curve: CurveFloat = None) -> None
unreal.SkyCreatorMoonLightSettings_51.atmosphere_disk_color_scale(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.atmosphere_disk_color_scale_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_scattered_luminance_scale(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_scattered_luminance_scale_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_on_atmosphere_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_on_atmosphere_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_on_surface_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_on_surface_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_strength(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.cloud_shadow_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorMoonLightSettings_51.intensity(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorMoonLightSettings_51.light_color(value: LinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.light_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorMoonLightSettings_51.temperature(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.temperature_curve(value: CurveFloat) -> None
unreal.SkyCreatorMoonLightSettings_51.use_atmosphere_disk_color_scale(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_cloud_scattered_luminance_scale(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_cloud_shadow_on_atmosphere_strength(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_cloud_shadow_on_surface_strength(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_cloud_shadow_strength(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_intensity(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_light_color(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_temperature(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.use_volumetric_scattering_intensity(value: bool) -> None
unreal.SkyCreatorMoonLightSettings_51.volumetric_scattering_intensity(value: float) -> None
unreal.SkyCreatorMoonLightSettings_51.volumetric_scattering_intensity_curve(value: CurveFloat) -> None
```

## `unreal.SkyCreatorNiagaraParameters(StructBase)`

```python
unreal.SkyCreatorNiagaraParameters.__init__() -> None
```

## `unreal.SkyCreatorPostProcessSettings(StructBase)`

```python
unreal.SkyCreatorPostProcessSettings.__init__(bloom_intensity: float = 0.000000, bloom_threshold: float = 0.000000, exposure_compensation: float = 0.000000) -> None
unreal.SkyCreatorPostProcessSettings.bloom_intensity(value: float) -> None
unreal.SkyCreatorPostProcessSettings.bloom_threshold(value: float) -> None
unreal.SkyCreatorPostProcessSettings.exposure_compensation(value: float) -> None
```

## `unreal.SkyCreatorSkyLightSettings(StructBase)`

```python
unreal.SkyCreatorSkyLightSettings.__init__(intensity: float = 0.000000, night_intensity: float = 0.000000, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lower_hemisphere_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_ambient_occlusion_strength: float = 0.000000) -> None
unreal.SkyCreatorSkyLightSettings.cloud_ambient_occlusion_strength(value: float) -> None
unreal.SkyCreatorSkyLightSettings.intensity(value: float) -> None
unreal.SkyCreatorSkyLightSettings.light_color(value: LinearColor) -> None
unreal.SkyCreatorSkyLightSettings.lower_hemisphere_color(value: LinearColor) -> None
unreal.SkyCreatorSkyLightSettings.night_intensity(value: float) -> None
```

## `unreal.SkyCreatorSkyLightSettings_51(StructBase)`

```python
unreal.SkyCreatorSkyLightSettings_51.__init__(use_intensity: bool = False, intensity: float = 0.000000, intensity_curve: CurveFloat = None, use_night_intensity: bool = False, night_intensity: float = 0.000000, night_intensity_curve: CurveFloat = None, use_light_color: bool = False, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], light_color_curve: CurveLinearColor = None, use_lower_hemisphere_color: bool = False, lower_hemisphere_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], lower_hemisphere_color_curve: CurveLinearColor = None, use_cloud_ambient_occlusion_strength: bool = False, cloud_ambient_occlusion_strength: float = 0.000000, cloud_ambient_occlusion_strength_curve: CurveFloat = None) -> None
unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength(value: float) -> None
unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyLightSettings_51.intensity(value: float) -> None
unreal.SkyCreatorSkyLightSettings_51.intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyLightSettings_51.light_color(value: LinearColor) -> None
unreal.SkyCreatorSkyLightSettings_51.light_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color(value: LinearColor) -> None
unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSkyLightSettings_51.night_intensity(value: float) -> None
unreal.SkyCreatorSkyLightSettings_51.night_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorSkyLightSettings_51.use_cloud_ambient_occlusion_strength(value: bool) -> None
unreal.SkyCreatorSkyLightSettings_51.use_intensity(value: bool) -> None
unreal.SkyCreatorSkyLightSettings_51.use_light_color(value: bool) -> None
unreal.SkyCreatorSkyLightSettings_51.use_lower_hemisphere_color(value: bool) -> None
unreal.SkyCreatorSkyLightSettings_51.use_night_intensity(value: bool) -> None
```

## `unreal.SkyCreatorSunLightSettings(StructBase)`

```python
unreal.SkyCreatorSunLightSettings.__init__(intensity: float = 0.000000, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], temperature: float = 0.000000, volumetric_scattering_intensity: float = 0.000000, atmosphere_disk_color_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_scattered_luminance_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_shadow_strength: float = 0.000000, cloud_shadow_on_atmosphere_strength: float = 0.000000, cloud_shadow_on_surface_strength: float = 0.000000) -> None
unreal.SkyCreatorSunLightSettings.atmosphere_disk_color_scale(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings.cloud_scattered_luminance_scale(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings.cloud_shadow_on_atmosphere_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings.cloud_shadow_on_surface_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings.cloud_shadow_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings.intensity(value: float) -> None
unreal.SkyCreatorSunLightSettings.light_color(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings.temperature(value: float) -> None
unreal.SkyCreatorSunLightSettings.volumetric_scattering_intensity(value: float) -> None
```

## `unreal.SkyCreatorSunLightSettings_51(StructBase)`

```python
unreal.SkyCreatorSunLightSettings_51.__init__(use_intensity: bool = False, intensity: float = 0.000000, intensity_curve: CurveFloat = None, use_light_color: bool = False, light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], light_color_curve: CurveLinearColor = None, use_temperature: bool = False, temperature: float = 0.000000, temperature_curve: CurveFloat = None, use_volumetric_scattering_intensity: bool = False, volumetric_scattering_intensity: float = 0.000000, volumetric_scattering_intensity_curve: CurveFloat = None, use_atmosphere_disk_color_scale: bool = False, atmosphere_disk_color_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], atmosphere_disk_color_scale_curve: CurveLinearColor = None, use_cloud_scattered_luminance_scale: bool = False, cloud_scattered_luminance_scale: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], cloud_scattered_luminance_scale_curve: CurveLinearColor = None, use_cloud_shadow_strength: bool = False, cloud_shadow_strength: float = 0.000000, cloud_shadow_strength_curve: CurveFloat = None, use_cloud_shadow_on_atmosphere_strength: bool = False, cloud_shadow_on_atmosphere_strength: float = 0.000000, cloud_shadow_on_atmosphere_strength_curve: CurveFloat = None, use_cloud_shadow_on_surface_strength: bool = False, cloud_shadow_on_surface_strength: float = 0.000000, cloud_shadow_on_surface_strength_curve: CurveFloat = None) -> None
unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength_curve(value: CurveFloat) -> None
unreal.SkyCreatorSunLightSettings_51.intensity(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorSunLightSettings_51.light_color(value: LinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.light_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorSunLightSettings_51.temperature(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.temperature_curve(value: CurveFloat) -> None
unreal.SkyCreatorSunLightSettings_51.use_atmosphere_disk_color_scale(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_cloud_scattered_luminance_scale(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_atmosphere_strength(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_surface_strength(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_strength(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_intensity(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_light_color(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_temperature(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.use_volumetric_scattering_intensity(value: bool) -> None
unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity(value: float) -> None
unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity_curve(value: CurveFloat) -> None
```

## `unreal.SkyCreatorWeatherMaterialFXSettings(StructBase)`

```python
unreal.SkyCreatorWeatherMaterialFXSettings.__init__(wetness_amount: float = 0.000000, wetness_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], puddles_amount: float = 0.000000, puddles_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], rain_ripples_amount: float = 0.000000, rain_ripples_intensity: float = 0.000000, rain_ripples_force_min_radius: float = 0.000000, rain_ripples_force_max_radius: float = 0.000000, rain_ripples_rings_number: float = 0.000000, rain_ripples_rings_delay: float = 0.000000, rain_ripples_damping: float = 0.000000, wind_ripples_intensity: float = 0.000000, wind_ripples_speed: float = 0.000000, snow_amount: float = 0.000000, snow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], snow_intensity: float = 0.000000, snow_sparkles_threshold: float = 0.000000) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.puddles_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.puddles_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_damping(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_max_radius(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_min_radius(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_delay(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_number(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.snow_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.snow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.snow_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.snow_sparkles_threshold(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.wetness_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.wetness_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_speed(value: float) -> None
```

## `unreal.SkyCreatorWeatherMaterialFXSettings_51(StructBase)`

```python
unreal.SkyCreatorWeatherMaterialFXSettings_51.__init__(use_wetness_amount: bool = False, wetness_amount: float = 0.000000, wetness_amount_curve: CurveFloat = None, use_wetness_color: bool = False, wetness_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], wetness_color_curve: CurveLinearColor = None, use_puddles_amount: bool = False, puddles_amount: float = 0.000000, puddles_amount_curve: CurveFloat = None, use_puddles_color: bool = False, puddles_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], puddles_color_curve: CurveLinearColor = None, use_rain_ripples_amount: bool = False, rain_ripples_amount: float = 0.000000, rain_ripples_amount_curve: CurveFloat = None, use_rain_ripples_intensity: bool = False, rain_ripples_intensity: float = 0.000000, rain_ripples_intensity_curve: CurveFloat = None, use_rain_ripples_force_min_radius: bool = False, rain_ripples_force_min_radius: float = 0.000000, rain_ripples_force_min_radius_curve: CurveFloat = None, use_rain_ripples_force_max_radius: bool = False, rain_ripples_force_max_radius: float = 0.000000, rain_ripples_force_max_radius_curve: CurveFloat = None, use_rain_ripples_rings_number: bool = False, rain_ripples_rings_number: float = 0.000000, rain_ripples_rings_number_curve: CurveFloat = None, use_rain_ripples_rings_delay: bool = False, rain_ripples_rings_delay: float = 0.000000, rain_ripples_rings_delay_curve: CurveFloat = None, use_rain_ripples_damping: bool = False, rain_ripples_damping: float = 0.000000, rain_ripples_damping_curve: CurveFloat = None, use_wind_ripples_intensity: bool = False, wind_ripples_intensity: float = 0.000000, wind_ripples_intensity_curve: CurveFloat = None, use_wind_ripples_speed: bool = False, wind_ripples_speed: float = 0.000000, wind_ripples_speed_curve: CurveFloat = None, use_snow_amount: bool = False, snow_amount: float = 0.000000, snow_amount_curve: CurveFloat = None, use_snow_color: bool = False, snow_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], snow_color_curve: CurveLinearColor = None, use_snow_intensity: bool = False, snow_intensity: float = 0.000000, snow_intensity_curve: CurveFloat = None, use_snow_sparkles_threshold: bool = False, snow_sparkles_threshold: float = 0.000000, snow_sparkles_threshold_curve: CurveFloat = None) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_amount(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_color(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_amount(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_damping(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_max_radius(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_min_radius(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_intensity(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_delay(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_number(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_amount(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_color(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_intensity(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_sparkles_threshold(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_amount(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_color(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_intensity(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_speed(value: bool) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color(value: LinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color_curve(value: CurveLinearColor) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity_curve(value: CurveFloat) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed(value: float) -> None
unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed_curve(value: CurveFloat) -> None
```

## `unreal.SkyLight(Info)`

```python
unreal.SkyLight.light_component() -> SkyLightComponent
```

## `unreal.SkyLightComponent(LightComponentBase)`

```python
unreal.SkyLightComponent.capture_emissive_only() -> bool
unreal.SkyLightComponent.cloud_ambient_occlusion() -> bool
unreal.SkyLightComponent.cloud_ambient_occlusion_aperture_scale() -> float
unreal.SkyLightComponent.cloud_ambient_occlusion_extent() -> float
unreal.SkyLightComponent.cloud_ambient_occlusion_map_resolution_scale() -> float
unreal.SkyLightComponent.cloud_ambient_occlusion_strength() -> float
unreal.SkyLightComponent.contrast() -> float
unreal.SkyLightComponent.cubemap() -> TextureCube
unreal.SkyLightComponent.cubemap_resolution() -> int
unreal.SkyLightComponent.lower_hemisphere_color() -> LinearColor
unreal.SkyLightComponent.lower_hemisphere_is_black() -> bool
unreal.SkyLightComponent.min_occlusion() -> float
unreal.SkyLightComponent.occlusion_combine_mode() -> OcclusionCombineMode
unreal.SkyLightComponent.occlusion_exponent() -> float
unreal.SkyLightComponent.occlusion_max_distance() -> float
unreal.SkyLightComponent.occlusion_tint() -> Color
unreal.SkyLightComponent.real_time_capture() -> bool
unreal.SkyLightComponent.recapture_sky() -> None
unreal.SkyLightComponent.set_brightness(new_intensity: float) -> None
unreal.SkyLightComponent.set_cubemap(new_cubemap: TextureCube) -> None
unreal.SkyLightComponent.set_cubemap_blend(source_cubemap: TextureCube, destination_cubemap: TextureCube, blend_fraction: float) -> None
unreal.SkyLightComponent.set_indirect_lighting_intensity(new_intensity: float) -> None
unreal.SkyLightComponent.set_intensity(new_intensity: float) -> None
unreal.SkyLightComponent.set_light_color(new_light_color: LinearColor) -> None
unreal.SkyLightComponent.set_lower_hemisphere_color(lower_hemisphere_color: LinearColor) -> None
unreal.SkyLightComponent.set_min_occlusion(min_occlusion: float) -> None
unreal.SkyLightComponent.set_occlusion_contrast(occlusion_contrast: float) -> None
unreal.SkyLightComponent.set_occlusion_exponent(occlusion_exponent: float) -> None
unreal.SkyLightComponent.set_occlusion_tint(tint: Color) -> None
unreal.SkyLightComponent.set_real_time_capture(real_time_capture: bool) -> None
unreal.SkyLightComponent.set_source_cubemap_angle(new_value: float) -> None
unreal.SkyLightComponent.set_volumetric_scattering_intensity(new_intensity: float) -> None
unreal.SkyLightComponent.sky_distance_threshold() -> float
unreal.SkyLightComponent.source_cubemap_angle() -> float
unreal.SkyLightComponent.source_type() -> SkyLightSourceType
```

## `unreal.SkylightTime(ParamsBase)`

```python
unreal.SkylightTime.__init__(skylight_time: str = "", duration_seconds: float = 0.000000, realtime: bool = False) -> None
unreal.SkylightTime.duration_seconds(value: float) -> None
unreal.SkylightTime.realtime(value: bool) -> None
unreal.SkylightTime.skylight_time(value: str) -> None
```

## `unreal.SkylightTimeResult(ResultBase)`

```python
unreal.SkylightTimeResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, skylight_time: str = "", realtime: bool = False) -> None
unreal.SkylightTimeResult.realtime(value: bool) -> None
unreal.SkylightTimeResult.skylight_time(value: str) -> None
```

## `unreal.SlateRHIRendererSettings(DeveloperSettings)`

```python
unreal.SlateRHIRendererSettings.get_mutable_slate_post_setting(post_buffer_bit: SlatePostRT) -> SlatePostSettings
unreal.SlateRHIRendererSettings.get_slate_post_setting(post_buffer_bit: SlatePostRT) -> SlatePostSettings
```

## `unreal.SparseVolumeTexture(Object)`

```python
unreal.SparseVolumeTexture.get_frame_transform() -> Transform
unreal.SparseVolumeTexture.get_num_frames() -> int
unreal.SparseVolumeTexture.get_num_mip_levels() -> int
unreal.SparseVolumeTexture.get_size_x() -> int
unreal.SparseVolumeTexture.get_size_y() -> int
unreal.SparseVolumeTexture.get_size_z() -> int
```

## `unreal.SparseVolumeTextureParameterValue(StructBase)`

```python
unreal.SparseVolumeTextureParameterValue.__init__(parameter_info: MaterialParameterInfo = ["None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1], parameter_value: SparseVolumeTexture = None) -> None
unreal.SparseVolumeTextureParameterValue.parameter_info(value: MaterialParameterInfo) -> None
unreal.SparseVolumeTextureParameterValue.parameter_value(value: SparseVolumeTexture) -> None
```

## `unreal.SparseVolumeTextureViewer(Info)`

```python
unreal.SparseVolumeTextureViewer.sparse_volume_texture_viewer_component() -> SparseVolumeTextureViewerComponent
```

## `unreal.SparseVolumeTextureViewerComponent(PrimitiveComponent)`

```python
unreal.SparseVolumeTextureViewerComponent.apply_per_frame_transforms() -> bool
unreal.SparseVolumeTextureViewerComponent.blocking_streaming_requests() -> bool
unreal.SparseVolumeTextureViewerComponent.extinction(value: float) -> None
unreal.SparseVolumeTextureViewerComponent.frame(value: float) -> None
unreal.SparseVolumeTextureViewerComponent.frame_rate(value: float) -> None
unreal.SparseVolumeTextureViewerComponent.looping(value: bool) -> None
unreal.SparseVolumeTextureViewerComponent.mip_level(value: int) -> None
unreal.SparseVolumeTextureViewerComponent.pivot_at_centroid() -> bool
unreal.SparseVolumeTextureViewerComponent.playing(value: bool) -> None
unreal.SparseVolumeTextureViewerComponent.preview_attribute(value: SparseVolumeTexturePreviewAttribute) -> None
unreal.SparseVolumeTextureViewerComponent.reverse_playback() -> bool
unreal.SparseVolumeTextureViewerComponent.sparse_volume_texture_preview(value: SparseVolumeTexture) -> None
unreal.SparseVolumeTextureViewerComponent.voxel_size(value: float) -> None
```

## `unreal.SpotLight(Light)`

```python
unreal.SpotLight.set_inner_cone_angle(new_inner_cone_angle: float) -> None
unreal.SpotLight.set_outer_cone_angle(new_outer_cone_angle: float) -> None
unreal.SpotLight.spot_light_component() -> SpotLightComponent
```

## `unreal.SpotLightComponent(PointLightComponent)`

```python
unreal.SpotLightComponent.inner_cone_angle() -> float
unreal.SpotLightComponent.outer_cone_angle() -> float
unreal.SpotLightComponent.set_inner_cone_angle(new_inner_cone_angle: float) -> None
unreal.SpotLightComponent.set_outer_cone_angle(new_outer_cone_angle: float) -> None
```

## `unreal.StaticMaterial(StructBase)`

```python
unreal.StaticMaterial.__init__(material_interface: MaterialInterface = None, material_slot_name: Name = "None", uv_channel_data: MeshUVChannelInfo = []) -> None
unreal.StaticMaterial.material_interface(value: MaterialInterface) -> None
unreal.StaticMaterial.material_slot_name(value: Name) -> None
unreal.StaticMaterial.uv_channel_data() -> MeshUVChannelInfo
```

## `unreal.StaticMesh(StreamableRenderAsset)`

```python
unreal.StaticMesh.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.StaticMesh.add_material(material: MaterialInterface) -> Name
unreal.StaticMesh.add_socket(socket: StaticMeshSocket) -> None
unreal.StaticMesh.build_from_static_mesh_descriptions(static_mesh_descriptions: Array[StaticMeshDescription], build_simple_collision: bool = False, fast_build: bool = True) -> None
unreal.StaticMesh.create_static_mesh_description(outer: Object = None) -> StaticMeshDescription
unreal.StaticMesh.find_socket(socket_name: Name) -> StaticMeshSocket
unreal.StaticMesh.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.StaticMesh.get_bounding_box() -> Box
unreal.StaticMesh.get_bounds() -> BoxSphereBounds
unreal.StaticMesh.get_material(material_index: int) -> MaterialInterface
unreal.StaticMesh.get_material_index(material_slot_name: Name) -> int
unreal.StaticMesh.get_min_lod_for_quality_levels() -> Tuple[Map[PerQualityLevels, int], int]
unreal.StaticMesh.get_minimum_lod_for_platform(platform_name: Name) -> int
unreal.StaticMesh.get_minimum_lod_for_platforms() -> Map[Name, int]
unreal.StaticMesh.get_minimum_lod_for_quality_level(quality_level: Name) -> int
unreal.StaticMesh.get_minimum_lod_for_quality_levels() -> Map[Name, int]
unreal.StaticMesh.get_num_lods() -> int
unreal.StaticMesh.get_num_sections(lod: int) -> int
unreal.StaticMesh.get_num_triangles(lod_index: int) -> int
unreal.StaticMesh.get_sockets_by_tag(socket_tag: str) -> Array[StaticMeshSocket]
unreal.StaticMesh.get_static_mesh_description(lod_index: int) -> StaticMeshDescription
unreal.StaticMesh.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.StaticMesh.is_lod_screen_size_auto_computed() -> bool
unreal.StaticMesh.lod_for_collision(value: int) -> None
unreal.StaticMesh.remove_socket(socket: StaticMeshSocket) -> None
unreal.StaticMesh.set_material(material_index: int, new_material: MaterialInterface) -> None
unreal.StaticMesh.set_min_lod_for_quality_levels(quality_level_minimum_lo_ds: Map[PerQualityLevels, int], default: int = -1) -> None
unreal.StaticMesh.set_minimum_lod_for_platform(platform_name: Name, min_lod: int) -> None
unreal.StaticMesh.set_minimum_lod_for_platforms(platform_minimum_lo_ds: Map[Name, int]) -> None
unreal.StaticMesh.set_num_source_models(num: int) -> None
unreal.StaticMesh.static_materials(value: Array[StaticMaterial]) -> None
unreal.StaticMesh.static_mesh_paint_support(value: StaticMeshPaintSupport) -> None
```

## `unreal.StaticMeshComponent(MeshComponent)`

```python
unreal.StaticMeshComponent.cast_distance_field_indirect_shadow() -> bool
unreal.StaticMeshComponent.disallow_nanite(value: bool) -> None
unreal.StaticMeshComponent.distance_field_indirect_shadow_min_visibility() -> float
unreal.StaticMeshComponent.distance_field_self_shadow_bias() -> float
unreal.StaticMeshComponent.enable_texture_color_mesh_painting(value: bool) -> None
unreal.StaticMeshComponent.enable_vertex_color_mesh_painting(value: bool) -> None
unreal.StaticMeshComponent.evaluate_world_position_offset(value: bool) -> None
unreal.StaticMeshComponent.evaluate_world_position_offset_in_ray_tracing(value: bool) -> None
unreal.StaticMeshComponent.force_nanite_for_masked(value: bool) -> None
unreal.StaticMeshComponent.forced_lod_model() -> int
unreal.StaticMeshComponent.get_initial_evaluate_world_position_offset() -> bool
unreal.StaticMeshComponent.get_local_bounds() -> Tuple[Vector, Vector]
unreal.StaticMeshComponent.ignore_instance_for_texture_streaming(value: bool) -> None
unreal.StaticMeshComponent.min_lod() -> int
unreal.StaticMeshComponent.nanite_pixel_programmable_distance() -> float
unreal.StaticMeshComponent.overridden_light_map_res() -> int
unreal.StaticMeshComponent.override_distance_field_self_shadow_bias() -> bool
unreal.StaticMeshComponent.override_light_map_res() -> bool
unreal.StaticMeshComponent.override_min_lod() -> bool
unreal.StaticMeshComponent.override_wireframe_color() -> bool
unreal.StaticMeshComponent.reverse_culling() -> bool
unreal.StaticMeshComponent.set_distance_field_self_shadow_bias(new_value: float) -> None
unreal.StaticMeshComponent.set_evaluate_world_position_offset(new_value: bool) -> None
unreal.StaticMeshComponent.set_evaluate_world_position_offset_in_ray_tracing(new_value: bool) -> None
unreal.StaticMeshComponent.set_force_disable_nanite(force_disable_nanite: bool) -> None
unreal.StaticMeshComponent.set_forced_lod_model(new_forced_lod_model: int) -> None
unreal.StaticMeshComponent.set_reverse_culling(reverse_culling: bool) -> None
unreal.StaticMeshComponent.set_static_mesh(new_mesh: StaticMesh) -> bool
unreal.StaticMeshComponent.set_world_position_offset_disable_distance(new_value: int) -> None
unreal.StaticMeshComponent.sort_triangles() -> bool
unreal.StaticMeshComponent.static_mesh() -> StaticMesh
unreal.StaticMeshComponent.streaming_distance_multiplier(value: float) -> None
unreal.StaticMeshComponent.update_initial_evaluate_world_position_offset() -> None
unreal.StaticMeshComponent.wireframe_color_override() -> Color
unreal.StaticMeshComponent.world_position_offset_disable_distance() -> int
unreal.StaticMeshComponent.world_position_offset_writes_velocity(value: bool) -> None
```

## `unreal.StaticMeshDescription(MeshDescriptionBase)`

```python
unreal.StaticMeshDescription.create_cube(center: Vector, half_extents: Vector, polygon_group: PolygonGroupID) -> Tuple[PolygonID, PolygonID, PolygonID, PolygonID, PolygonID, PolygonID]
unreal.StaticMeshDescription.get_vertex_instance_uv(vertex_instance_id: VertexInstanceID, uv_index: int = 0) -> Vector2D
unreal.StaticMeshDescription.set_polygon_group_material_slot_name(polygon_group_id: PolygonGroupID, slot_name: Name) -> None
unreal.StaticMeshDescription.set_vertex_instance_uv(vertex_instance_id: VertexInstanceID, uv: Vector2D, uv_index: int = 0) -> None
```

## `unreal.StaticMeshInstanceVisualizationDesc(TableRowBase)`

```python
unreal.StaticMeshInstanceVisualizationDesc.__init__() -> None
```

## `unreal.StaticMeshInstanceVisualizationMeshDesc(MassStaticMeshInstanceVisualizationMeshDesc)`

```python
unreal.StaticMeshInstanceVisualizationMeshDesc.__init__() -> None
```

## `unreal.StaticMeshReductionOptions(StructBase)`

```python
unreal.StaticMeshReductionOptions.__init__(auto_compute_lod_screen_size: bool = False, reduction_settings: Array[StaticMeshReductionSettings] = []) -> None
unreal.StaticMeshReductionOptions.auto_compute_lod_screen_size(value: bool) -> None
unreal.StaticMeshReductionOptions.reduction_settings(value: Array[StaticMeshReductionSettings]) -> None
```

## `unreal.StaticMeshReductionSettings(StructBase)`

```python
unreal.StaticMeshReductionSettings.__init__(percent_triangles: float = 0.000000, screen_size: float = 0.000000) -> None
unreal.StaticMeshReductionSettings.percent_triangles(value: float) -> None
unreal.StaticMeshReductionSettings.screen_size(value: float) -> None
```

## `unreal.StaticMeshSocket(Object)`

```python
unreal.StaticMeshSocket.relative_location(value: Vector) -> None
unreal.StaticMeshSocket.relative_rotation(value: Rotator) -> None
unreal.StaticMeshSocket.relative_scale(value: Vector) -> None
unreal.StaticMeshSocket.socket_name() -> Name
unreal.StaticMeshSocket.tag(value: str) -> None
```

## `unreal.StreamableRenderAsset(Object)`

```python
unreal.StreamableRenderAsset.global_force_mip_levels_to_be_resident() -> bool
unreal.StreamableRenderAsset.never_stream(value: bool) -> None
unreal.StreamableRenderAsset.num_cinematic_mip_levels(value: int) -> None
unreal.StreamableRenderAsset.set_force_mip_levels_to_be_resident(seconds: float, cinematic_lod_group_mask: int = 0) -> None
```

## `unreal.StreamableSparseVolumeTexture(SparseVolumeTexture)`

```python
unreal.StreamableSparseVolumeTexture.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.StreamableSparseVolumeTexture.address_x(value: TextureAddress) -> None
unreal.StreamableSparseVolumeTexture.address_y(value: TextureAddress) -> None
unreal.StreamableSparseVolumeTexture.address_z(value: TextureAddress) -> None
unreal.StreamableSparseVolumeTexture.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.StreamableSparseVolumeTexture.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.StreamableSparseVolumeTexture.local_ddc_only(value: bool) -> None
```

## `unreal.TAPythonMaterialConnection(StructBase)`

```python
unreal.TAPythonMaterialConnection.__init__(left_expression_index: int = 0, left_output_index: int = 0, left_output_name: str = "", right_expression_index: int = 0, right_expression_input_index: int = 0, right_expression_input_name: str = "") -> None
unreal.TAPythonMaterialConnection.left_expression_index(value: int) -> None
unreal.TAPythonMaterialConnection.left_output_index(value: int) -> None
unreal.TAPythonMaterialConnection.left_output_name(value: str) -> None
unreal.TAPythonMaterialConnection.right_expression_index(value: int) -> None
unreal.TAPythonMaterialConnection.right_expression_input_index(value: int) -> None
unreal.TAPythonMaterialConnection.right_expression_input_name(value: str) -> None
```

## `unreal.TextRenderComponent(PrimitiveComponent)`

```python
unreal.TextRenderComponent.always_render_as_text() -> bool
unreal.TextRenderComponent.font() -> Font
unreal.TextRenderComponent.get_text_local_size() -> Vector
unreal.TextRenderComponent.get_text_world_size() -> Vector
unreal.TextRenderComponent.horiz_spacing_adjust() -> float
unreal.TextRenderComponent.horizontal_alignment() -> HorizTextAligment
unreal.TextRenderComponent.set_font(value: Font) -> None
unreal.TextRenderComponent.set_horiz_spacing_adjust(value: float) -> None
unreal.TextRenderComponent.set_horizontal_alignment(value: HorizTextAligment) -> None
unreal.TextRenderComponent.set_text(value: Text) -> None
unreal.TextRenderComponent.set_text_material(material: MaterialInterface) -> None
unreal.TextRenderComponent.set_text_render_color(value: Color) -> None
unreal.TextRenderComponent.set_vert_spacing_adjust(value: float) -> None
unreal.TextRenderComponent.set_vertical_alignment(value: VerticalTextAligment) -> None
unreal.TextRenderComponent.set_world_size(value: float) -> None
unreal.TextRenderComponent.set_x_scale(value: float) -> None
unreal.TextRenderComponent.set_y_scale(value: float) -> None
unreal.TextRenderComponent.text() -> Text
unreal.TextRenderComponent.text_material() -> MaterialInterface
unreal.TextRenderComponent.text_render_color() -> Color
unreal.TextRenderComponent.vert_spacing_adjust() -> float
unreal.TextRenderComponent.vertical_alignment() -> VerticalTextAligment
unreal.TextRenderComponent.world_size() -> float
unreal.TextRenderComponent.x_scale() -> float
unreal.TextRenderComponent.y_scale() -> float
```

## `unreal.Texture(StreamableRenderAsset)`

```python
unreal.Texture.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.Texture.adjust_brightness(value: float) -> None
unreal.Texture.adjust_brightness_curve(value: float) -> None
unreal.Texture.adjust_hue(value: float) -> None
unreal.Texture.adjust_max_alpha(value: float) -> None
unreal.Texture.adjust_min_alpha(value: float) -> None
unreal.Texture.adjust_rgb_curve(value: float) -> None
unreal.Texture.adjust_saturation(value: float) -> None
unreal.Texture.adjust_vibrance(value: float) -> None
unreal.Texture.alpha_coverage_thresholds(value: Vector4) -> None
unreal.Texture.availability(value: TextureAvailability) -> None
unreal.Texture.blueprint_get_memory_size() -> int
unreal.Texture.blueprint_get_texture_source_disk_and_memory_size() -> Tuple[int, int]
unreal.Texture.blueprint_get_texture_source_id_string() -> Optional[str]
unreal.Texture.chroma_key_color(value: Color) -> None
unreal.Texture.chroma_key_texture(value: bool) -> None
unreal.Texture.chroma_key_threshold(value: float) -> None
unreal.Texture.composite_power(value: float) -> None
unreal.Texture.composite_texture(value: Texture) -> None
unreal.Texture.composite_texture_mode(value: CompositeTextureMode) -> None
unreal.Texture.compress_final(value: bool) -> None
unreal.Texture.compression_no_alpha(value: bool) -> None
unreal.Texture.compression_quality(value: TextureCompressionQuality) -> None
unreal.Texture.compression_settings(value: TextureCompressionSettings) -> None
unreal.Texture.compute_texture_source_channel_min_max() -> Optional[Tuple[LinearColor, LinearColor]]
unreal.Texture.cook_platform_tiling_settings(value: TextureCookPlatformTilingSettings) -> None
unreal.Texture.defer_compression(value: bool) -> None
unreal.Texture.do_scale_mips_for_alpha_coverage(value: bool) -> None
unreal.Texture.export_to_disk(filename: str, options: ImageWriteOptions) -> None
unreal.Texture.filter(value: TextureFilter) -> None
unreal.Texture.flip_green_channel(value: bool) -> None
unreal.Texture.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.Texture.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.Texture.lod_bias(value: int) -> None
unreal.Texture.lod_group(value: TextureGroup) -> None
unreal.Texture.lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
unreal.Texture.max_texture_size(value: int) -> None
unreal.Texture.mip_gen_settings(value: TextureMipGenSettings) -> None
unreal.Texture.mip_load_options(value: TextureMipLoadOptions) -> None
unreal.Texture.normalize_normals(value: bool) -> None
unreal.Texture.oodle_preserve_extremes(value: bool) -> None
unreal.Texture.oodle_texture_sdk_version(value: Name) -> None
unreal.Texture.pad_with_border_color(value: bool) -> None
unreal.Texture.padding_color(value: Color) -> None
unreal.Texture.power_of_two_mode(value: TexturePowerOfTwoSetting) -> None
unreal.Texture.preserve_border(value: bool) -> None
unreal.Texture.resize_during_build_x(value: int) -> None
unreal.Texture.resize_during_build_y(value: int) -> None
unreal.Texture.source_color_settings(value: TextureSourceColorSettings) -> None
unreal.Texture.srgb(value: bool) -> None
unreal.Texture.use_legacy_gamma(value: bool) -> None
unreal.Texture.use_new_mip_filter(value: bool) -> None
unreal.Texture.virtual_texture_streaming() -> bool
```

## `unreal.Texture2D(Texture)`

```python
unreal.Texture2D.address_x(value: TextureAddress) -> None
unreal.Texture2D.address_y(value: TextureAddress) -> None
unreal.Texture2D.blueprint_get_cpu_copy() -> SharedImageConstRefBlueprint
unreal.Texture2D.blueprint_get_size_x() -> int
unreal.Texture2D.blueprint_get_size_y() -> int
```

## `unreal.Texture2DArrayAsset(StructBase)`

```python
unreal.Texture2DArrayAsset.__init__() -> None
```

## `unreal.TextureArea(StructBase)`

```python
unreal.TextureArea.__init__(center: Vector = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000], rotator: Rotator = [0.000000, 0.000000, 0.000000]) -> None
unreal.TextureArea.center() -> Vector
unreal.TextureArea.rotator() -> Rotator
unreal.TextureArea.scale() -> Vector
```

## `unreal.TextureBound(StructBase)`

```python
unreal.TextureBound.__init__(left_bottom_lon: str = "", left_bottom_lat: str = "", right_top_lon: str = "", right_top_lat: str = "") -> None
unreal.TextureBound.left_bottom_lat() -> str
unreal.TextureBound.left_bottom_lon() -> str
unreal.TextureBound.right_top_lat() -> str
unreal.TextureBound.right_top_lon() -> str
```

## `unreal.TextureCollectionParameterValue(StructBase)`

```python
unreal.TextureCollectionParameterValue.__init__(parameter_info: MaterialParameterInfo = ["None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1], parameter_value: TextureCollection = None) -> None
unreal.TextureCollectionParameterValue.parameter_info(value: MaterialParameterInfo) -> None
unreal.TextureCollectionParameterValue.parameter_value(value: TextureCollection) -> None
```

## `unreal.TextureParameterValue(StructBase)`

```python
unreal.TextureParameterValue.__init__(parameter_info: MaterialParameterInfo = ["None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1], parameter_value: Texture = None) -> None
unreal.TextureParameterValue.parameter_info(value: MaterialParameterInfo) -> None
unreal.TextureParameterValue.parameter_value(value: Texture) -> None
```

## `unreal.TextureRenderTarget(Texture)`

```python
unreal.TextureRenderTarget.target_gamma(value: float) -> None
```

## `unreal.TextureRenderTarget2D(TextureRenderTarget)`

```python
unreal.TextureRenderTarget2D.address_x(value: TextureAddress) -> None
unreal.TextureRenderTarget2D.address_y(value: TextureAddress) -> None
unreal.TextureRenderTarget2D.auto_generate_mips() -> bool
unreal.TextureRenderTarget2D.clear_color() -> LinearColor
unreal.TextureRenderTarget2D.gpu_shared_flag() -> bool
unreal.TextureRenderTarget2D.mips_address_u() -> TextureAddress
unreal.TextureRenderTarget2D.mips_address_v() -> TextureAddress
unreal.TextureRenderTarget2D.mips_sampler_filter() -> TextureFilter
unreal.TextureRenderTarget2D.render_target_format() -> TextureRenderTargetFormat
unreal.TextureRenderTarget2D.size_x() -> int
unreal.TextureRenderTarget2D.size_y() -> int
unreal.TextureRenderTarget2D.supports_uav() -> bool
```

## `unreal.TextureRenderTarget2DArray(TextureRenderTarget)`

```python
unreal.TextureRenderTarget2DArray.hdr() -> bool
unreal.TextureRenderTarget2DArray.size_x(value: int) -> None
unreal.TextureRenderTarget2DArray.size_y(value: int) -> None
unreal.TextureRenderTarget2DArray.slices(value: int) -> None
unreal.TextureRenderTarget2DArray.supports_uav() -> bool
```

## `unreal.TextureRenderTargetCube(TextureRenderTarget)`

```python
unreal.TextureRenderTargetCube.auto_generate_mips() -> bool
unreal.TextureRenderTargetCube.hdr() -> bool
unreal.TextureRenderTargetCube.mips_sampler_filter() -> TextureFilter
unreal.TextureRenderTargetCube.size_x(value: int) -> None
unreal.TextureRenderTargetCube.supports_uav() -> bool
```

## `unreal.TextureRenderTargetVolume(TextureRenderTarget)`

```python
unreal.TextureRenderTargetVolume.hdr() -> bool
unreal.TextureRenderTargetVolume.size_x(value: int) -> None
unreal.TextureRenderTargetVolume.size_y(value: int) -> None
unreal.TextureRenderTargetVolume.size_z(value: int) -> None
unreal.TextureRenderTargetVolume.supports_uav() -> bool
```

## `unreal.TextureSourceColorSettings(StructBase)`

```python
unreal.TextureSourceColorSettings.__init__(encoding_override: TextureSourceEncoding = TextureSourceEncoding.TSE_NONE, color_space: TextureColorSpace = TextureColorSpace.TCS_NONE, red_chromaticity_coordinate: Vector2D = [0.000000, 0.000000], green_chromaticity_coordinate: Vector2D = [0.000000, 0.000000], blue_chromaticity_coordinate: Vector2D = [0.000000, 0.000000], white_chromaticity_coordinate: Vector2D = [0.000000, 0.000000], chromatic_adaptation_method: TextureChromaticAdaptationMethod = TextureChromaticAdaptationMethod.TCAM_NONE) -> None
unreal.TextureSourceColorSettings.blue_chromaticity_coordinate(value: Vector2D) -> None
unreal.TextureSourceColorSettings.chromatic_adaptation_method(value: TextureChromaticAdaptationMethod) -> None
unreal.TextureSourceColorSettings.color_space(value: TextureColorSpace) -> None
unreal.TextureSourceColorSettings.encoding_override(value: TextureSourceEncoding) -> None
unreal.TextureSourceColorSettings.green_chromaticity_coordinate(value: Vector2D) -> None
unreal.TextureSourceColorSettings.red_chromaticity_coordinate(value: Vector2D) -> None
unreal.TextureSourceColorSettings.white_chromaticity_coordinate(value: Vector2D) -> None
```

## `unreal.UDIMTextureFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.UDIMTextureFunctionLibrary.make_udim_virtual_texture_from_texture2_ds(output_path_name: str, source_textures: Array[Texture2D], block_coords: Array[IntPoint], keep_existing_settings: bool = False, check_out_and_save: bool = False) -> Texture2D
```

## `unreal.UnderwaterPostProcessSettings(StructBase)`

```python
unreal.UnderwaterPostProcessSettings.__init__(enabled: bool = False, priority: float = 0.000000, blend_radius: float = 0.000000, blend_weight: float = 0.000000, post_process_settings: PostProcessSettings = []) -> None
unreal.UnderwaterPostProcessSettings.blend_radius(value: float) -> None
unreal.UnderwaterPostProcessSettings.blend_weight(value: float) -> None
unreal.UnderwaterPostProcessSettings.enabled(value: bool) -> None
unreal.UnderwaterPostProcessSettings.post_process_settings(value: PostProcessSettings) -> None
unreal.UnderwaterPostProcessSettings.priority(value: float) -> None
```

## `unreal.UpdateHighlightAreaParams(ParamsBase)`

```python
unreal.UpdateHighlightAreaParams.__init__(eid: str = "", polygon_entity_eid: str = "", highlight_area_style: HighlightAreaStyle = ["ffffffaa", "595959aa", "000000ff", 0.000000, 0.000000, 0.000000]) -> None
unreal.UpdateHighlightAreaParams.eid(value: str) -> None
unreal.UpdateHighlightAreaParams.highlight_area_style(value: HighlightAreaStyle) -> None
unreal.UpdateHighlightAreaParams.polygon_entity_eid(value: str) -> None
```

## `unreal.UpgradeNiagaraEmitterContext(Object)`

```python
unreal.UpgradeNiagaraEmitterContext.cancelled_by_python_error(value: bool) -> None
unreal.UpgradeNiagaraEmitterContext.new_emitter(value: NiagaraPythonEmitter) -> None
unreal.UpgradeNiagaraEmitterContext.old_emitter(value: NiagaraPythonEmitter) -> None
```

## `unreal.UpgradeNiagaraScriptResults(Object)`

```python
unreal.UpgradeNiagaraScriptResults.cancelled_by_python_error(value: bool) -> None
unreal.UpgradeNiagaraScriptResults.get_old_input(input_name: str) -> NiagaraPythonScriptModuleInput
unreal.UpgradeNiagaraScriptResults.new_inputs(value: Array[NiagaraPythonScriptModuleInput]) -> None
unreal.UpgradeNiagaraScriptResults.old_inputs(value: Array[NiagaraPythonScriptModuleInput]) -> None
unreal.UpgradeNiagaraScriptResults.reset_to_default(input_name: str) -> None
unreal.UpgradeNiagaraScriptResults.set_bool_input(input_name: str, value: bool) -> None
unreal.UpgradeNiagaraScriptResults.set_color_input(input_name: str, value: LinearColor) -> None
unreal.UpgradeNiagaraScriptResults.set_enum_input(input_name: str, value: str) -> None
unreal.UpgradeNiagaraScriptResults.set_float_input(input_name: str, value: float) -> None
unreal.UpgradeNiagaraScriptResults.set_int_input(input_name: str, value: int) -> None
unreal.UpgradeNiagaraScriptResults.set_linked_input(input_name: str, value: str) -> None
unreal.UpgradeNiagaraScriptResults.set_new_input(input_name: str, value: NiagaraPythonScriptModuleInput) -> None
unreal.UpgradeNiagaraScriptResults.set_quat_input(input_name: str, value: Quat) -> None
unreal.UpgradeNiagaraScriptResults.set_vec2_input(input_name: str, value: Vector2D) -> None
unreal.UpgradeNiagaraScriptResults.set_vec3_input(input_name: str, value: Vector) -> None
unreal.UpgradeNiagaraScriptResults.set_vec4_input(input_name: str, value: Vector4) -> None
```

## `unreal.UrbanBuildTemplateTexture(StructBase)`

```python
unreal.UrbanBuildTemplateTexture.__init__(power_of_two_mode: TexturePowerOfTwoSetting = TexturePowerOfTwoSetting.NONE, srgb: bool = False, padding_color: Color = [0, 0, 0, 0], use_legacy_gamma: bool = False, address_x: TextureAddress = TextureAddress.TA_WRAP, address_y: TextureAddress = TextureAddress.TA_WRAP, filter: TextureFilter = TextureFilter.TF_NEAREST, mip_load_options: TextureMipLoadOptions = TextureMipLoadOptions.DEFAULT, virtual_texture_streaming: bool = False, alpha_coverage_thresholds: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], dither_mip_map_alpha: bool = False, flip_green_channel: bool = False, compression_no_alpha: bool = False, defer_compression: bool = False, compression_settings: TextureCompressionSettings = TextureCompressionSettings.TC_DEFAULT, max_texture_size: int = 0, compression_quality: TextureCompressionQuality = TextureCompressionQuality.TCQ_DEFAULT, lossy_compression_amount: TextureLossyCompressionAmount = TextureLossyCompressionAmount.TLCA_DEFAULT, adjust_brightness: float = 0.000000, adjust_brightness_curve: float = 0.000000, adjust_vibrance: float = 0.000000, adjust_saturation: float = 0.000000, adjust_rgb_curve: float = 0.000000, adjust_hue: float = 0.000000, adjust_min_alpha: float = 0.000000, adjust_max_alpha: float = 0.000000, chroma_key_texture: bool = False, chroma_key_threshold: float = 0.000000, chroma_key_color: Color = [0, 0, 0, 0], mip_gen_settings: TextureMipGenSettings = TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP, lod_bias: int = 0, lod_group: TextureGroup = TextureGroup.TEXTUREGROUP_WORLD, preserve_border: bool = False, never_stream: bool = False, global_force_mip_levels_to_be_resident: bool = False, num_cinematic_mip_levels: int = 0, composite_texture: Texture = None, composite_texture_mode: CompositeTextureMode = CompositeTextureMode.CTM_DISABLED, composite_power: float = 0.000000) -> None
unreal.UrbanBuildTemplateTexture.address_x(value: TextureAddress) -> None
unreal.UrbanBuildTemplateTexture.address_y(value: TextureAddress) -> None
unreal.UrbanBuildTemplateTexture.adjust_brightness(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_brightness_curve(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_hue(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_max_alpha(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_min_alpha(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_rgb_curve(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_saturation(value: float) -> None
unreal.UrbanBuildTemplateTexture.adjust_vibrance(value: float) -> None
unreal.UrbanBuildTemplateTexture.alpha_coverage_thresholds(value: Vector4) -> None
unreal.UrbanBuildTemplateTexture.chroma_key_color(value: Color) -> None
unreal.UrbanBuildTemplateTexture.chroma_key_texture(value: bool) -> None
unreal.UrbanBuildTemplateTexture.chroma_key_threshold(value: float) -> None
unreal.UrbanBuildTemplateTexture.composite_power(value: float) -> None
unreal.UrbanBuildTemplateTexture.composite_texture(value: Texture) -> None
unreal.UrbanBuildTemplateTexture.composite_texture_mode(value: CompositeTextureMode) -> None
unreal.UrbanBuildTemplateTexture.compression_no_alpha(value: bool) -> None
unreal.UrbanBuildTemplateTexture.compression_quality(value: TextureCompressionQuality) -> None
unreal.UrbanBuildTemplateTexture.compression_settings(value: TextureCompressionSettings) -> None
unreal.UrbanBuildTemplateTexture.defer_compression(value: bool) -> None
unreal.UrbanBuildTemplateTexture.dither_mip_map_alpha(value: bool) -> None
unreal.UrbanBuildTemplateTexture.filter(value: TextureFilter) -> None
unreal.UrbanBuildTemplateTexture.flip_green_channel(value: bool) -> None
unreal.UrbanBuildTemplateTexture.global_force_mip_levels_to_be_resident() -> bool
unreal.UrbanBuildTemplateTexture.lod_bias(value: int) -> None
unreal.UrbanBuildTemplateTexture.lod_group(value: TextureGroup) -> None
unreal.UrbanBuildTemplateTexture.lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
unreal.UrbanBuildTemplateTexture.max_texture_size() -> int
unreal.UrbanBuildTemplateTexture.mip_gen_settings(value: TextureMipGenSettings) -> None
unreal.UrbanBuildTemplateTexture.mip_load_options(value: TextureMipLoadOptions) -> None
unreal.UrbanBuildTemplateTexture.never_stream(value: bool) -> None
unreal.UrbanBuildTemplateTexture.num_cinematic_mip_levels(value: int) -> None
unreal.UrbanBuildTemplateTexture.padding_color(value: Color) -> None
unreal.UrbanBuildTemplateTexture.power_of_two_mode(value: TexturePowerOfTwoSetting) -> None
unreal.UrbanBuildTemplateTexture.preserve_border(value: bool) -> None
unreal.UrbanBuildTemplateTexture.srgb(value: bool) -> None
unreal.UrbanBuildTemplateTexture.use_legacy_gamma(value: bool) -> None
unreal.UrbanBuildTemplateTexture.virtual_texture_streaming() -> bool
```

## `unreal.UrbanBuildTemplateTextureComponent(Object)`

```python
unreal.UrbanBuildTemplateTextureComponent.address_x(value: TextureAddress) -> None
unreal.UrbanBuildTemplateTextureComponent.address_y(value: TextureAddress) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_brightness(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_brightness_curve(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_hue(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_max_alpha(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_min_alpha(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_rgb_curve(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_saturation(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.adjust_vibrance(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.alpha_coverage_thresholds(value: Vector4) -> None
unreal.UrbanBuildTemplateTextureComponent.chroma_key_color(value: Color) -> None
unreal.UrbanBuildTemplateTextureComponent.chroma_key_texture(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.chroma_key_threshold(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.composite_power(value: float) -> None
unreal.UrbanBuildTemplateTextureComponent.composite_texture(value: Texture) -> None
unreal.UrbanBuildTemplateTextureComponent.composite_texture_mode(value: CompositeTextureMode) -> None
unreal.UrbanBuildTemplateTextureComponent.compression_no_alpha(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.compression_quality(value: TextureCompressionQuality) -> None
unreal.UrbanBuildTemplateTextureComponent.compression_settings(value: TextureCompressionSettings) -> None
unreal.UrbanBuildTemplateTextureComponent.defer_compression(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.dither_mip_map_alpha(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.filter(value: TextureFilter) -> None
unreal.UrbanBuildTemplateTextureComponent.flip_green_channel(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.global_force_mip_levels_to_be_resident() -> bool
unreal.UrbanBuildTemplateTextureComponent.lod_bias(value: int) -> None
unreal.UrbanBuildTemplateTextureComponent.lod_group(value: TextureGroup) -> None
unreal.UrbanBuildTemplateTextureComponent.lossy_compression_amount(value: TextureLossyCompressionAmount) -> None
unreal.UrbanBuildTemplateTextureComponent.max_texture_size() -> int
unreal.UrbanBuildTemplateTextureComponent.mip_gen_settings(value: TextureMipGenSettings) -> None
unreal.UrbanBuildTemplateTextureComponent.mip_load_options(value: TextureMipLoadOptions) -> None
unreal.UrbanBuildTemplateTextureComponent.never_stream(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.num_cinematic_mip_levels(value: int) -> None
unreal.UrbanBuildTemplateTextureComponent.padding_color(value: Color) -> None
unreal.UrbanBuildTemplateTextureComponent.power_of_two_mode(value: TexturePowerOfTwoSetting) -> None
unreal.UrbanBuildTemplateTextureComponent.preserve_border(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.srgb(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.use_legacy_gamma(value: bool) -> None
unreal.UrbanBuildTemplateTextureComponent.virtual_texture_streaming() -> bool
```

## `unreal.UrbanModelerRender(Actor)`

```python
unreal.UrbanModelerRender.clear_render_components() -> Tuple[Array[StaticMeshComponent], Array[InstancedStaticMeshComponent]]
unreal.UrbanModelerRender.clear_render_info(render_info: ModelerRenderInfo) -> ModelerRenderInfo
unreal.UrbanModelerRender.clear_resource() -> None
unreal.UrbanModelerRender.empty_modeler_render() -> None
unreal.UrbanModelerRender.load_resource() -> None
unreal.UrbanModelerRender.load_urban_scene_node(static_mesh_nodes: Array[UrbanSceneNode_StaticMesh], resource_data_nodes: Array[UrbanSceneNode_ResourceData]) -> Optional[Tuple[Array[UrbanSceneNode_StaticMesh], Array[UrbanSceneNode_ResourceData], Array[StaticMeshComponent], Array[InstancedStaticMeshComponent]]]
unreal.UrbanModelerRender.on_modeler_render_destroyed(actor_deleted: Actor) -> None
unreal.UrbanModelerRender.receive_render_info(render_info: ModelerRenderInfo) -> ModelerRenderInfo
unreal.UrbanModelerRender.render_infos(value: Array[ModelerRenderInfo]) -> None
unreal.UrbanModelerRender.render_transform(value: Transform) -> None
```

## `unreal.UrbanSceneNode_StaticMesh(UrbanSceneNode_Base)`

```python
unreal.UrbanSceneNode_StaticMesh.load_mesh_and_fi_ds(actor: Actor) -> Array[StaticMeshComponent]
```

## `unreal.UrbanStaticMeshAssetUserData(AssetUserData)`

```python
unreal.UrbanStaticMeshAssetUserData.material_color() -> Map[SoftObjectPath, LinearColor]
unreal.UrbanStaticMeshAssetUserData.material_simplification() -> Map[SoftObjectPath, str]
```

## `unreal.UrbanStaticMeshBlueprintLibrary(BlueprintFunctionLibrary)`

```python
unreal.UrbanStaticMeshBlueprintLibrary.get_all_static_mesh_user_data(object_class: Class) -> Array[UrbanStaticMeshAssetUserData]
unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data(object: Object) -> UrbanStaticMeshAssetUserData
unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_keys_and_values_for_value(object: Object, color_to_match: LinearColor) -> Tuple[Array[SoftObjectPath], Array[LinearColor]]
unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_material_color_for_key(object: Object, key: SoftObjectPath) -> LinearColor
unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_material_simplification_for_key(object: Object, key: SoftObjectPath) -> str
unreal.UrbanStaticMeshBlueprintLibrary.set_static_mesh_asset_user_data_material_color_for_key(object: Object, key: SoftObjectPath, value: LinearColor) -> bool
unreal.UrbanStaticMeshBlueprintLibrary.set_static_mesh_asset_user_data_material_simplification_for_key(object: Object, key: SoftObjectPath, value: str) -> bool
```

## `unreal.UsdMaterialAssetUserData(UsdAssetUserData)`

```python
unreal.UsdMaterialAssetUserData.parameter_to_primvar(value: Map[str, str]) -> None
unreal.UsdMaterialAssetUserData.primvar_to_uv_index(value: Map[str, int]) -> None
```

## `unreal.UsdSparseVolumeTextureAssetUserData(UsdAssetUserData)`

```python
unreal.UsdSparseVolumeTextureAssetUserData.source_open_vdb_asset_prim_paths(value: Array[str]) -> None
unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_indices(value: Array[int]) -> None
unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_time_codes(value: Array[float]) -> None
unreal.UsdSparseVolumeTextureAssetUserData.time_sample_paths(value: Array[str]) -> None
```

## `unreal.UserSceneTextureOverride(StructBase)`

```python
unreal.UserSceneTextureOverride.__init__(key: Name = "None", value: Name = "None") -> None
unreal.UserSceneTextureOverride.key(value: Name) -> None
unreal.UserSceneTextureOverride.value(value: Name) -> None
```

## `unreal.VegetationRenderControl(StructBase)`

```python
unreal.VegetationRenderControl.__init__() -> None
```

## `unreal.VersionedNiagaraEmitterData(StructBase)`

```python
unreal.VersionedNiagaraEmitterData.__init__(local_space: bool = False, determinism: bool = False, random_seed: int = 0, interpolated_spawning: bool = False, sim_target: NiagaraSimTarget = NiagaraSimTarget.CPU_SIM, fixed_bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], requires_persistent_i_ds: bool = False, max_gpu_particles_spawn_per_frame: int = 0, allocation_mode: ParticleAllocationMode = ParticleAllocationMode.AUTOMATIC_ESTIMATE) -> None
unreal.VersionedNiagaraEmitterData.allocation_mode(value: ParticleAllocationMode) -> None
unreal.VersionedNiagaraEmitterData.determinism(value: bool) -> None
unreal.VersionedNiagaraEmitterData.fixed_bounds(value: Box) -> None
unreal.VersionedNiagaraEmitterData.interpolated_spawning(value: bool) -> None
unreal.VersionedNiagaraEmitterData.local_space(value: bool) -> None
unreal.VersionedNiagaraEmitterData.max_gpu_particles_spawn_per_frame(value: int) -> None
unreal.VersionedNiagaraEmitterData.random_seed(value: int) -> None
unreal.VersionedNiagaraEmitterData.requires_persistent_i_ds(value: bool) -> None
unreal.VersionedNiagaraEmitterData.sim_target(value: NiagaraSimTarget) -> None
```

## `unreal.VirtualTextureBuilder(Object)`

```python
unreal.VirtualTextureBuilder.texture() -> VirtualTexture2D
unreal.VirtualTextureBuilder.texture_mobile() -> VirtualTexture2D
```

## `unreal.VisualHighlightParams(WdpVisualParamBase)`

```python
unreal.VisualHighlightParams.__init__(eids: Array[int] = [], style_name: Name = "None", highlight: bool = False) -> None
unreal.VisualHighlightParams.highlight(value: bool) -> None
```

## `unreal.VolumeTexture(Texture)`

```python
unreal.VolumeTexture.address_mode(value: TextureAddress) -> None
```

## `unreal.WaterBodyStaticMeshSettings(StructBase)`

```python
unreal.WaterBodyStaticMeshSettings.__init__() -> None
```

## `unreal.WdpMaterialInstanceObject(StructBase)`

```python
unreal.WdpMaterialInstanceObject.__init__(id: str = "", name: str = "", friendly_name: str = "", category: str = "", parent_material: str = "", parameters: MaterialInstanceParams = [[], []]) -> None
unreal.WdpMaterialInstanceObject.category(value: str) -> None
unreal.WdpMaterialInstanceObject.friendly_name(value: str) -> None
unreal.WdpMaterialInstanceObject.id(value: str) -> None
unreal.WdpMaterialInstanceObject.name(value: str) -> None
unreal.WdpMaterialInstanceObject.parameters(value: MaterialInstanceParams) -> None
unreal.WdpMaterialInstanceObject.parent_material(value: str) -> None
```

## `unreal.WdpMaterialLibrary(WorldSubsystem)`

```python
unreal.WdpMaterialLibrary.create_material_instance_entity_by_id(mi_id: str) -> WdpMaterialInstance
```

## `unreal.WdpMaterialLibraryJson(StructBase)`

```python
unreal.WdpMaterialLibraryJson.__init__() -> None
```

## `unreal.WdpMaterialObject(StructBase)`

```python
unreal.WdpMaterialObject.__init__(id: str = "", name: str = "", parameters: WdpMaterialParams = [[1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000], ["", [0, 0, 0, 0], 1.000000, 1.000000, "", 1.000000, "", 0.500000, "", 0.000000, "", 1.000000, "", 1.000000, "", "", [0, 0, 0, 0], "", 1.000000, 0.100000, [0, 0, 0, 0], 1.000000]]) -> None
unreal.WdpMaterialObject.id(value: str) -> None
unreal.WdpMaterialObject.name(value: str) -> None
unreal.WdpMaterialObject.parameters(value: WdpMaterialParams) -> None
```

## `unreal.WdpMaterialParams(StructBase)`

```python
unreal.WdpMaterialParams.__init__(uv_control: ML_UV_Control = [1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000], material_channel_control: ML_Material_Channel_Control = ["", [0, 0, 0, 0], 1.000000, 1.000000, "", 1.000000, "", 0.500000, "", 0.000000, "", 1.000000, "", 1.000000, "", "", [0, 0, 0, 0], "", 1.000000, 0.100000, [0, 0, 0, 0], 1.000000]) -> None
unreal.WdpMaterialParams.material_channel_control(value: ML_Material_Channel_Control) -> None
unreal.WdpMaterialParams.uv_control(value: ML_UV_Control) -> None
```

## `unreal.WdpPickMaterialActionResult(StructBase)`

```python
unreal.WdpPickMaterialActionResult.__init__() -> None
```

## `unreal.WdpPickMaterialResult(StructBase)`

```python
unreal.WdpPickMaterialResult.__init__(entity_result: IWdpEntity = None, component_result: PrimitiveComponent = None, material_name: str = "", material_index: int = 0, hit_result: HitResult = [False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0, 0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], multi_trace_results: Array[HitResult] = []) -> None
unreal.WdpPickMaterialResult.component_result() -> PrimitiveComponent
unreal.WdpPickMaterialResult.entity_result() -> IWdpEntity
unreal.WdpPickMaterialResult.hit_result() -> HitResult
unreal.WdpPickMaterialResult.material_index() -> int
unreal.WdpPickMaterialResult.material_name() -> str
unreal.WdpPickMaterialResult.multi_trace_results() -> Array[HitResult]
```

## `unreal.glTFRuntimeLightConfig(StructBase)`

```python
unreal.glTFRuntimeLightConfig.__init__(default_attenuation_multiplier: float = 0.000000) -> None
unreal.glTFRuntimeLightConfig.default_attenuation_multiplier(value: float) -> None
```

## `unreal.glTFRuntimeMaterialsConfig(StructBase)`

```python
unreal.glTFRuntimeMaterialsConfig.__init__(cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE, uber_materials_override_map: Map[EglTFRuntimeMaterialType, MaterialInterface] = {}, materials_override_map: Map[int, MaterialInterface] = {}, materials_override_by_name_map: Map[str, MaterialInterface] = {}, textures_override_map: Map[int, Texture2D] = {}, images_override_map: Map[int, Texture2D] = {}, disable_vertex_colors: bool = False, generates_mip_maps: bool = False, merge_sections_by_material: bool = False, specular_factor: float = 0.000000, materials_override_map_inject_params: bool = False, params_multiplier: Map[str, float] = {}, images_config: glTFRuntimeImagesConfig = [TextureCompressionSettings.TC_DEFAULT, TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False, False, 0], variant: str = "", skip_load: bool = False, vertex_color_only_material: MaterialInterface = None, scalar_params_overrides: Map[str, float] = {}, load_mip_maps: bool = False, force_material: MaterialInterface = None, skip_points: bool = False, points_triangulation_mode: EglTFRuntimePointsTriangulationMode = EglTFRuntimePointsTriangulationMode.TRIANGLE, points_base_material: MaterialInterface = None, points_scale_factor: float = 0.000000, skip_lines: bool = False, lines_triangulation_mode: EglTFRuntimeLinesTriangulationMode = EglTFRuntimeLinesTriangulationMode.RECTANGLE, lines_base_material: MaterialInterface = None, lines_scale_factor: float = 0.000000, custom_scalar_params: Map[str, float] = {}, custom_vector_params: Map[str, LinearColor] = {}, custom_texture_params: Map[str, Texture] = {}) -> None
unreal.glTFRuntimeMaterialsConfig.cache_mode(value: EglTFRuntimeCacheMode) -> None
unreal.glTFRuntimeMaterialsConfig.custom_scalar_params(value: Map[str, float]) -> None
unreal.glTFRuntimeMaterialsConfig.custom_texture_params(value: Map[str, Texture]) -> None
unreal.glTFRuntimeMaterialsConfig.custom_vector_params(value: Map[str, LinearColor]) -> None
unreal.glTFRuntimeMaterialsConfig.disable_vertex_colors(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.force_material(value: MaterialInterface) -> None
unreal.glTFRuntimeMaterialsConfig.generates_mip_maps(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.images_config(value: glTFRuntimeImagesConfig) -> None
unreal.glTFRuntimeMaterialsConfig.images_override_map(value: Map[int, Texture2D]) -> None
unreal.glTFRuntimeMaterialsConfig.lines_base_material(value: MaterialInterface) -> None
unreal.glTFRuntimeMaterialsConfig.lines_scale_factor(value: float) -> None
unreal.glTFRuntimeMaterialsConfig.lines_triangulation_mode(value: EglTFRuntimeLinesTriangulationMode) -> None
unreal.glTFRuntimeMaterialsConfig.load_mip_maps(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.materials_override_by_name_map(value: Map[str, MaterialInterface]) -> None
unreal.glTFRuntimeMaterialsConfig.materials_override_map(value: Map[int, MaterialInterface]) -> None
unreal.glTFRuntimeMaterialsConfig.materials_override_map_inject_params(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.merge_sections_by_material(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.params_multiplier(value: Map[str, float]) -> None
unreal.glTFRuntimeMaterialsConfig.points_base_material(value: MaterialInterface) -> None
unreal.glTFRuntimeMaterialsConfig.points_scale_factor(value: float) -> None
unreal.glTFRuntimeMaterialsConfig.points_triangulation_mode(value: EglTFRuntimePointsTriangulationMode) -> None
unreal.glTFRuntimeMaterialsConfig.scalar_params_overrides(value: Map[str, float]) -> None
unreal.glTFRuntimeMaterialsConfig.skip_lines(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.skip_load(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.skip_points(value: bool) -> None
unreal.glTFRuntimeMaterialsConfig.specular_factor(value: float) -> None
unreal.glTFRuntimeMaterialsConfig.textures_override_map(value: Map[int, Texture2D]) -> None
unreal.glTFRuntimeMaterialsConfig.uber_materials_override_map(value: Map[EglTFRuntimeMaterialType, MaterialInterface]) -> None
unreal.glTFRuntimeMaterialsConfig.variant(value: str) -> None
unreal.glTFRuntimeMaterialsConfig.vertex_color_only_material(value: MaterialInterface) -> None
```

## `unreal.glTFRuntimeOnSkeletalMeshCreated(MulticastDelegateBase)`

```python
unreal.glTFRuntimeOnSkeletalMeshCreated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeOnStaticMeshCreated(MulticastDelegateBase)`

```python
unreal.glTFRuntimeOnStaticMeshCreated.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeSkeletalMeshAsync(DelegateBase)`

```python
unreal.glTFRuntimeSkeletalMeshAsync.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeSkeletalMeshConfig(StructBase)`

```python
unreal.glTFRuntimeSkeletalMeshConfig.__init__(cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE, skeleton: Skeleton = None, overwrite_ref_skeleton: bool = False, merge_all_bones_to_bone_tree: bool = False, custom_skeleton: Array[glTFRuntimeBone] = [], ignore_skin: bool = False, override_skin_index: int = 0, skeleton_config: glTFRuntimeSkeletonConfig = [EglTFRuntimeCacheMode.READ_WRITE, False, "", {}, False, {}, False, -1, {}, False, None, False, "", {}, [glTFRuntimeBoneRemapper(), None], False, False, False, -1, False, {}, False], materials_config: glTFRuntimeMaterialsConfig = [EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False, False, 0.000000, False, {}, [TextureCompressionSettings.TC_DEFAULT, TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False, False, 0], "", False, None, {}, False, None, True, EglTFRuntimePointsTriangulationMode.OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True, EglTFRuntimeLinesTriangulationMode.OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, {}, {}, {}], lod_screen_size: Map[int, float] = {}, bounds_scale: Vector = [0.000000, 0.000000, 0.000000], shift_bounds_by_root_bone: bool = False, ignore_missing_bones: bool = False, physics_bodies: Map[str, glTFRuntimePhysicsBody] = {}, outer: Object = None, save_to_package: str = "", per_poly_collision: bool = False, disable_morph_targets: bool = False, ignore_empty_morph_targets: bool = False, morph_targets_duplicate_strategy: EglTFRuntimeMorphTargetsDuplicateStrategy = EglTFRuntimeMorphTargetsDuplicateStrategy.IGNORE, shift_bounds: Vector = [0.000000, 0.000000, 0.000000], use_high_precision_u_vs: bool = False, physics_asset_template: PhysicsAsset = None, add_virtual_bones: bool = False, normals_generation_strategy: EglTFRuntimeNormalsGenerationStrategy = EglTFRuntimeNormalsGenerationStrategy.IF_MISSING, tangents_generation_strategy: EglTFRuntimeTangentsGenerationStrategy = EglTFRuntimeTangentsGenerationStrategy.IF_MISSING, reverse_tangents: bool = False, auto_generate_physics_asset_bodies: bool = False, physics_asset_auto_body_config: glTFRuntimePhysicsAssetAutoBodyConfig = [EglTFRuntimePhysicsAssetAutoBodyCollisionType.CAPSULE, 20.000000, True, False, CollisionTraceFlag.CTF_USE_DEFAULT, PhysicsType.PHYS_TYPE_DEFAULT, True, 1.010000], auto_generate_physics_asset_constraints: bool = False, physics_constraints: Array[glTFRuntimePhysicsConstraint] = [], bone_bounds_filter: glTFRuntimeBoneBoundsFilterHook = [glTFRuntimeBoneBoundsFilter(), None]) -> None
unreal.glTFRuntimeSkeletalMeshConfig.add_virtual_bones(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_bodies(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_constraints(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.bone_bounds_filter(value: glTFRuntimeBoneBoundsFilterHook) -> None
unreal.glTFRuntimeSkeletalMeshConfig.bounds_scale(value: Vector) -> None
unreal.glTFRuntimeSkeletalMeshConfig.cache_mode(value: EglTFRuntimeCacheMode) -> None
unreal.glTFRuntimeSkeletalMeshConfig.custom_skeleton(value: Array[glTFRuntimeBone]) -> None
unreal.glTFRuntimeSkeletalMeshConfig.disable_morph_targets(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.ignore_empty_morph_targets(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.ignore_missing_bones(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.ignore_skin(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.lod_screen_size(value: Map[int, float]) -> None
unreal.glTFRuntimeSkeletalMeshConfig.materials_config(value: glTFRuntimeMaterialsConfig) -> None
unreal.glTFRuntimeSkeletalMeshConfig.merge_all_bones_to_bone_tree(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.morph_targets_duplicate_strategy(value: EglTFRuntimeMorphTargetsDuplicateStrategy) -> None
unreal.glTFRuntimeSkeletalMeshConfig.normals_generation_strategy(value: EglTFRuntimeNormalsGenerationStrategy) -> None
unreal.glTFRuntimeSkeletalMeshConfig.outer(value: Object) -> None
unreal.glTFRuntimeSkeletalMeshConfig.override_skin_index(value: int) -> None
unreal.glTFRuntimeSkeletalMeshConfig.overwrite_ref_skeleton(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.per_poly_collision(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_auto_body_config(value: glTFRuntimePhysicsAssetAutoBodyConfig) -> None
unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_template(value: PhysicsAsset) -> None
unreal.glTFRuntimeSkeletalMeshConfig.physics_bodies(value: Map[str, glTFRuntimePhysicsBody]) -> None
unreal.glTFRuntimeSkeletalMeshConfig.physics_constraints(value: Array[glTFRuntimePhysicsConstraint]) -> None
unreal.glTFRuntimeSkeletalMeshConfig.reverse_tangents(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.save_to_package(value: str) -> None
unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds(value: Vector) -> None
unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds_by_root_bone(value: bool) -> None
unreal.glTFRuntimeSkeletalMeshConfig.skeleton(value: Skeleton) -> None
unreal.glTFRuntimeSkeletalMeshConfig.skeleton_config(value: glTFRuntimeSkeletonConfig) -> None
unreal.glTFRuntimeSkeletalMeshConfig.tangents_generation_strategy(value: EglTFRuntimeTangentsGenerationStrategy) -> None
unreal.glTFRuntimeSkeletalMeshConfig.use_high_precision_u_vs(value: bool) -> None
```

## `unreal.glTFRuntimeStaticMeshAsync(DelegateBase)`

```python
unreal.glTFRuntimeStaticMeshAsync.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeStaticMeshConfig(StructBase)`

```python
unreal.glTFRuntimeStaticMeshConfig.__init__(cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE, reverse_winding: bool = False, build_simple_collision: bool = False, build_complex_collision: bool = False, box_collisions: Array[Box] = [], sphere_collisions: Array[Vector4] = [], collision_complexity: CollisionTraceFlag = CollisionTraceFlag.CTF_USE_DEFAULT, allow_cpu_access: bool = False, pivot_position: EglTFRuntimePivotPosition = EglTFRuntimePivotPosition.ASSET, outer: Object = None, materials_config: glTFRuntimeMaterialsConfig = [EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False, False, 0.000000, False, {}, [TextureCompressionSettings.TC_DEFAULT, TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False, False, 0], "", False, None, {}, False, None, True, EglTFRuntimePointsTriangulationMode.OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True, EglTFRuntimeLinesTriangulationMode.OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, {}, {}, {}], sockets: Map[str, Transform] = {}, export_original_pivot_to_socket: str = "", lod_screen_size: Map[int, float] = {}, normals_generation_strategy: EglTFRuntimeNormalsGenerationStrategy = EglTFRuntimeNormalsGenerationStrategy.IF_MISSING, tangents_generation_strategy: EglTFRuntimeTangentsGenerationStrategy = EglTFRuntimeTangentsGenerationStrategy.IF_MISSING, reverse_tangents: bool = False, use_high_precision_u_vs: bool = False, generate_static_mesh_description: bool = False, build_nav_collision: bool = False, custom_config_map: Map[str, str] = {}, custom_config_objects: Array[DataAsset] = [], lod_screen_size_multiplier: float = 0.000000, build_lumen_cards: bool = False) -> None
unreal.glTFRuntimeStaticMeshConfig.allow_cpu_access(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.box_collisions(value: Array[Box]) -> None
unreal.glTFRuntimeStaticMeshConfig.build_complex_collision(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.build_lumen_cards(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.build_nav_collision(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.build_simple_collision(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.cache_mode(value: EglTFRuntimeCacheMode) -> None
unreal.glTFRuntimeStaticMeshConfig.collision_complexity(value: CollisionTraceFlag) -> None
unreal.glTFRuntimeStaticMeshConfig.custom_config_map(value: Map[str, str]) -> None
unreal.glTFRuntimeStaticMeshConfig.custom_config_objects(value: Array[DataAsset]) -> None
unreal.glTFRuntimeStaticMeshConfig.export_original_pivot_to_socket(value: str) -> None
unreal.glTFRuntimeStaticMeshConfig.generate_static_mesh_description(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.lod_screen_size(value: Map[int, float]) -> None
unreal.glTFRuntimeStaticMeshConfig.lod_screen_size_multiplier(value: float) -> None
unreal.glTFRuntimeStaticMeshConfig.materials_config(value: glTFRuntimeMaterialsConfig) -> None
unreal.glTFRuntimeStaticMeshConfig.normals_generation_strategy(value: EglTFRuntimeNormalsGenerationStrategy) -> None
unreal.glTFRuntimeStaticMeshConfig.outer(value: Object) -> None
unreal.glTFRuntimeStaticMeshConfig.pivot_position(value: EglTFRuntimePivotPosition) -> None
unreal.glTFRuntimeStaticMeshConfig.reverse_tangents(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.reverse_winding(value: bool) -> None
unreal.glTFRuntimeStaticMeshConfig.sockets(value: Map[str, Transform]) -> None
unreal.glTFRuntimeStaticMeshConfig.sphere_collisions(value: Array[Vector4]) -> None
unreal.glTFRuntimeStaticMeshConfig.tangents_generation_strategy(value: EglTFRuntimeTangentsGenerationStrategy) -> None
unreal.glTFRuntimeStaticMeshConfig.use_high_precision_u_vs(value: bool) -> None
```

## `unreal.glTFRuntimeTexture2DArrayAsync(DelegateBase)`

```python
unreal.glTFRuntimeTexture2DArrayAsync.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeTexture2DAsync(DelegateBase)`

```python
unreal.glTFRuntimeTexture2DAsync.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeTextureCubeAsync(DelegateBase)`

```python
unreal.glTFRuntimeTextureCubeAsync.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.glTFRuntimeTextureSampler(StructBase)`

```python
unreal.glTFRuntimeTextureSampler.__init__(tile_x: TextureAddress = TextureAddress.TA_WRAP, tile_y: TextureAddress = TextureAddress.TA_WRAP, tile_z: TextureAddress = TextureAddress.TA_WRAP, min_filter: TextureFilter = TextureFilter.TF_NEAREST, mag_filter: TextureFilter = TextureFilter.TF_NEAREST) -> None
unreal.glTFRuntimeTextureSampler.mag_filter(value: TextureFilter) -> None
unreal.glTFRuntimeTextureSampler.min_filter(value: TextureFilter) -> None
unreal.glTFRuntimeTextureSampler.tile_x(value: TextureAddress) -> None
unreal.glTFRuntimeTextureSampler.tile_y(value: TextureAddress) -> None
unreal.glTFRuntimeTextureSampler.tile_z(value: TextureAddress) -> None
```

