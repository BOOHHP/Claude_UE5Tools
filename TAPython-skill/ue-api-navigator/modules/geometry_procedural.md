# Unreal Python API — Geometry Procedural

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AbcGeometryCacheSettings(StructBase)`

```python
unreal.AbcGeometryCacheSettings.__init__(flatten_tracks: bool = False, store_imported_vertex_numbers: bool = False, apply_constant_topology_optimizations: bool = False, motion_vectors: AbcGeometryCacheMotionVectorsImport = AbcGeometryCacheMotionVectorsImport.NO_MOTION_VECTORS, optimize_index_buffers: bool = False, compressed_position_precision: float = 0.000000, compressed_texture_coordinates_number_of_bits: int = 0) -> None
unreal.AbcGeometryCacheSettings.apply_constant_topology_optimizations(value: bool) -> None
unreal.AbcGeometryCacheSettings.compressed_position_precision(value: float) -> None
unreal.AbcGeometryCacheSettings.compressed_texture_coordinates_number_of_bits(value: int) -> None
unreal.AbcGeometryCacheSettings.flatten_tracks(value: bool) -> None
unreal.AbcGeometryCacheSettings.motion_vectors(value: AbcGeometryCacheMotionVectorsImport) -> None
unreal.AbcGeometryCacheSettings.optimize_index_buffers(value: bool) -> None
unreal.AbcGeometryCacheSettings.store_imported_vertex_numbers(value: bool) -> None
```

## `unreal.AesEditorWaterSplitMessage(StructBase)`

```python
unreal.AesEditorWaterSplitMessage.__init__(original_entity_id: int = 0, new_entity_id1: int = 0, new_entity_id2: int = 0) -> None
unreal.AesEditorWaterSplitMessage.new_entity_id1(value: int) -> None
unreal.AesEditorWaterSplitMessage.new_entity_id2(value: int) -> None
unreal.AesEditorWaterSplitMessage.original_entity_id(value: int) -> None
```

## `unreal.AesInstanceSplineAssetTagData(StructBase)`

```python
unreal.AesInstanceSplineAssetTagData.__init__(closed_loop: bool = False, reverse: bool = False, spline_point_type: SplinePointType = SplinePointType.LINEAR, start_extension: float = 0.000000, end_extension: float = 0.000000, start_mesh: AesMeshData = [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [], []], mid_meshes: Array[AesMeshData] = [], end_mesh: AesMeshData = [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [], []], flip_start_mesh: bool = False, flip_end_mesh: bool = False, spline_deform_type: SplineDeformType = SplineDeformType.LINEAR, forward_axis: SplineMeshAxis = SplineMeshAxis.X, spline_up_dir: Vector3f = [0.000000, 0.000000, 0.000000], world_smooth_interp_roll_scale: bool = False, local_smooth_interp_roll_scale: bool = False, control_type: AesSplineSizeControlType = AesSplineSizeControlType.SCALE, start_scale: Vector2f = [0.000000, 0.000000], start_offset: Vector2f = [0.000000, 0.000000], start_width: Vector2f = [0.000000, 0.000000], start_height: Vector2f = [0.000000, 0.000000], start_roll: float = 0.000000, end_scale: Vector2f = [0.000000, 0.000000], end_offset: Vector2f = [0.000000, 0.000000], end_width: Vector2f = [0.000000, 0.000000], end_height: Vector2f = [0.000000, 0.000000], end_roll: float = 0.000000, resample_type: SplineResampleType = SplineResampleType.INTERPOLATING, resample_by_edge: bool = False, placement_type: SplinePlacementType = SplinePlacementType.CONTINUOUS, section_length: float = 0.000000, gap_between_bounds: float = 0.000000, alignment_type: SplineAlignmentType = SplineAlignmentType.NORMAL, start_scale_x: float = 0.000000, end_scale_x: float = 0.000000, keep_tan_value: bool = False, start_tan: Vector = [0.000000, 0.000000, 0.000000], end_tan: Vector = [0.000000, 0.000000, 0.000000], build_start_mesh: bool = False, build_end_mesh: bool = False, chamfer_corner: bool = False, chamfer_length: float = 0.000000, custom_data: Map[Name, float] = {}) -> None
unreal.AesInstanceSplineAssetTagData.alignment_type(value: SplineAlignmentType) -> None
unreal.AesInstanceSplineAssetTagData.build_end_mesh(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.build_start_mesh(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.chamfer_corner(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.chamfer_length(value: float) -> None
unreal.AesInstanceSplineAssetTagData.closed_loop(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.control_type(value: AesSplineSizeControlType) -> None
unreal.AesInstanceSplineAssetTagData.custom_data(value: Map[Name, float]) -> None
unreal.AesInstanceSplineAssetTagData.end_extension(value: float) -> None
unreal.AesInstanceSplineAssetTagData.end_height(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.end_mesh(value: AesMeshData) -> None
unreal.AesInstanceSplineAssetTagData.end_offset(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.end_roll(value: float) -> None
unreal.AesInstanceSplineAssetTagData.end_scale(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.end_scale_x(value: float) -> None
unreal.AesInstanceSplineAssetTagData.end_tan(value: Vector) -> None
unreal.AesInstanceSplineAssetTagData.end_width(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.flip_end_mesh(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.flip_start_mesh(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.forward_axis(value: SplineMeshAxis) -> None
unreal.AesInstanceSplineAssetTagData.gap_between_bounds(value: float) -> None
unreal.AesInstanceSplineAssetTagData.keep_tan_value(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.local_smooth_interp_roll_scale(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.mid_meshes(value: Array[AesMeshData]) -> None
unreal.AesInstanceSplineAssetTagData.placement_type(value: SplinePlacementType) -> None
unreal.AesInstanceSplineAssetTagData.resample_by_edge(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.resample_type(value: SplineResampleType) -> None
unreal.AesInstanceSplineAssetTagData.reverse(value: bool) -> None
unreal.AesInstanceSplineAssetTagData.section_length(value: float) -> None
unreal.AesInstanceSplineAssetTagData.spline_deform_type(value: SplineDeformType) -> None
unreal.AesInstanceSplineAssetTagData.spline_point_type(value: SplinePointType) -> None
unreal.AesInstanceSplineAssetTagData.spline_up_dir(value: Vector3f) -> None
unreal.AesInstanceSplineAssetTagData.start_extension(value: float) -> None
unreal.AesInstanceSplineAssetTagData.start_height(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.start_mesh(value: AesMeshData) -> None
unreal.AesInstanceSplineAssetTagData.start_offset(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.start_roll(value: float) -> None
unreal.AesInstanceSplineAssetTagData.start_scale(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.start_scale_x(value: float) -> None
unreal.AesInstanceSplineAssetTagData.start_tan(value: Vector) -> None
unreal.AesInstanceSplineAssetTagData.start_width(value: Vector2f) -> None
unreal.AesInstanceSplineAssetTagData.world_smooth_interp_roll_scale(value: bool) -> None
```

## `unreal.AesSplineCurves(StructBase)`

```python
unreal.AesSplineCurves.__init__() -> None
```

## `unreal.AesSplineCurvesMetadata(StructBase)`

```python
unreal.AesSplineCurvesMetadata.__init__() -> None
```

## `unreal.AesSplineHandleGizmoBeginHover(MulticastDelegateBase)`

```python
unreal.AesSplineHandleGizmoBeginHover.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AesSplineHandleGizmoEndHover(MulticastDelegateBase)`

```python
unreal.AesSplineHandleGizmoEndHover.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AesWaterEditorActionParams_SplitContour(AesEditorSimpleActionParams)`

```python
unreal.AesWaterEditorActionParams_SplitContour.snap_distance(value: float) -> None
```

## `unreal.AttributeCurve(IndexedCurve)`

```python
unreal.AttributeCurve.__init__() -> None
```

## `unreal.AudioCurveSourceComponent(AudioComponent)`

```python
unreal.AudioCurveSourceComponent.curve_source_binding_name(value: Name) -> None
unreal.AudioCurveSourceComponent.curve_sync_offset(value: float) -> None
unreal.AudioCurveSourceComponent.get_binding_name() -> Name
unreal.AudioCurveSourceComponent.get_curve_value(curve_name: Name) -> float
unreal.AudioCurveSourceComponent.get_curves() -> Array[NamedCurveValue]
```

## `unreal.BrushEffectCurves(StructBase)`

```python
unreal.BrushEffectCurves.__init__(use_curve_channel: bool = False, elevation_curve_asset: CurveFloat = None, channel_edge_offset: float = 0.000000, channel_depth: float = 0.000000, curve_ramp_width: float = 0.000000) -> None
unreal.BrushEffectCurves.channel_depth(value: float) -> None
unreal.BrushEffectCurves.channel_edge_offset(value: float) -> None
unreal.BrushEffectCurves.curve_ramp_width(value: float) -> None
unreal.BrushEffectCurves.elevation_curve_asset(value: CurveFloat) -> None
unreal.BrushEffectCurves.use_curve_channel(value: bool) -> None
```

## `unreal.CachedFloatCurve(StructBase)`

```python
unreal.CachedFloatCurve.__init__(curve_name: Name = "None") -> None
unreal.CachedFloatCurve.curve_name(value: Name) -> None
```

## `unreal.ColorInputDeviceCurveProperty(InputDeviceProperty)`

```python
unreal.ColorInputDeviceCurveProperty.color_data(value: DeviceColorCurveData) -> None
unreal.ColorInputDeviceCurveProperty.device_override_data(value: Map[Name, DeviceColorCurveData]) -> None
```

## `unreal.CreateGeometryEntitiesParams(ParamsBase)`

```python
unreal.CreateGeometryEntitiesParams.__init__(url: str = "") -> None
unreal.CreateGeometryEntitiesParams.url(value: str) -> None
```

## `unreal.CreateGeometryEntitiesResult(ResultBase)`

```python
unreal.CreateGeometryEntitiesResult.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, point_eids: Array[str] = [], polyline_eids: Array[str] = [], polygon2d_eids: Array[str] = []) -> None
unreal.CreateGeometryEntitiesResult.point_eids(value: Array[str]) -> None
unreal.CreateGeometryEntitiesResult.polygon2d_eids(value: Array[str]) -> None
unreal.CreateGeometryEntitiesResult.polyline_eids(value: Array[str]) -> None
```

## `unreal.CurveBase(Object)`

```python
unreal.CurveBase.get_time_range() -> Tuple[float, float]
unreal.CurveBase.get_value_range() -> Tuple[float, float]
```

## `unreal.CurveEditorBakeFilter(CurveEditorFilterBase)`

```python
unreal.CurveEditorBakeFilter.bake_interval(value: FrameNumber) -> None
unreal.CurveEditorBakeFilter.bake_interval_in_seconds(value: float) -> None
unreal.CurveEditorBakeFilter.custom_range(value: CurveEditorBakeFilterRange) -> None
unreal.CurveEditorBakeFilter.custom_range_max_in_seconds(value: float) -> None
unreal.CurveEditorBakeFilter.custom_range_min_in_seconds(value: float) -> None
unreal.CurveEditorBakeFilter.custom_range_override(value: bool) -> None
```

## `unreal.CurveEditorBakeFilterRange(StructBase)`

```python
unreal.CurveEditorBakeFilterRange.__init__(min: FrameNumber = [0], max: FrameNumber = [0]) -> None
unreal.CurveEditorBakeFilterRange.max(value: FrameNumber) -> None
unreal.CurveEditorBakeFilterRange.min(value: FrameNumber) -> None
```

## `unreal.CurveEditorFFTFilter(CurveEditorFilterBase)`

```python
unreal.CurveEditorFFTFilter.cutoff_frequency(value: float) -> None
unreal.CurveEditorFFTFilter.order(value: int) -> None
unreal.CurveEditorFFTFilter.response(value: CurveEditorFFTFilterClass) -> None
unreal.CurveEditorFFTFilter.type(value: CurveEditorFFTFilterType) -> None
```

## `unreal.CurveEditorGaussianFilter(CurveEditorFilterBase)`

```python
unreal.CurveEditorGaussianFilter.gaussian_params(value: GaussianParams) -> None
```

## `unreal.CurveEditorReduceFilter(CurveEditorFilterBase)`

```python
unreal.CurveEditorReduceFilter.sample_rate(value: FrameRate) -> None
unreal.CurveEditorReduceFilter.tolerance(value: float) -> None
unreal.CurveEditorReduceFilter.try_remove_user_set_tangent_keys(value: bool) -> None
```

## `unreal.CurveEditorSmartReduceFilter(CurveEditorFilterBase)`

```python
unreal.CurveEditorSmartReduceFilter.smart_reduce_params(value: SmartReduceParams) -> None
```

## `unreal.CurveFlagsChangedPayload(CurvePayload)`

```python
unreal.CurveFlagsChangedPayload.__init__(identifier: AnimationCurveIdentifier = [], old_flags: int = 0) -> None
unreal.CurveFlagsChangedPayload.old_flags() -> int
```

## `unreal.CurveFloat(CurveBase)`

```python
unreal.CurveFloat.get_float_value(time: float) -> float
```

## `unreal.CurveLinearColor(CurveBase)`

```python
unreal.CurveLinearColor.get_clamped_linear_color_value(time: float) -> LinearColor
unreal.CurveLinearColor.get_linear_color_value(time: float) -> LinearColor
unreal.CurveLinearColor.get_unadjusted_linear_color_value(time: float) -> LinearColor
```

## `unreal.CurveLinearColorAtlas(Texture2D)`

```python
unreal.CurveLinearColorAtlas.get_curve_position(curve: CurveLinearColor) -> Optional[float]
```

## `unreal.CurveParameterPair(StructBase)`

```python
unreal.CurveParameterPair.__init__(anim_curve_name: Name = "None", user_variable_name: Name = "None") -> None
unreal.CurveParameterPair.anim_curve_name() -> Name
unreal.CurveParameterPair.user_variable_name() -> Name
```

## `unreal.CurvePayload(EmptyPayload)`

```python
unreal.CurvePayload.__init__(identifier: AnimationCurveIdentifier = []) -> None
unreal.CurvePayload.identifier() -> AnimationCurveIdentifier
```

## `unreal.CurveRemapPair(StructBase)`

```python
unreal.CurveRemapPair.__init__() -> None
```

## `unreal.CurveRenamedPayload(CurvePayload)`

```python
unreal.CurveRenamedPayload.__init__(identifier: AnimationCurveIdentifier = [], new_identifier: AnimationCurveIdentifier = []) -> None
unreal.CurveRenamedPayload.new_identifier() -> AnimationCurveIdentifier
```

## `unreal.CurveScaledPayload(CurvePayload)`

```python
unreal.CurveScaledPayload.__init__(identifier: AnimationCurveIdentifier = [], factor: float = 0.000000, origin: float = 0.000000) -> None
unreal.CurveScaledPayload.factor() -> float
unreal.CurveScaledPayload.origin() -> float
```

## `unreal.CurveSourceInterface(Interface)`

```python
unreal.CurveSourceInterface.get_binding_name() -> Name
unreal.CurveSourceInterface.get_curve_value(curve_name: Name) -> float
unreal.CurveSourceInterface.get_curves() -> Array[NamedCurveValue]
```

## `unreal.CurveVector(CurveBase)`

```python
unreal.CurveVector.get_vector_value(time: float) -> Vector
```

## `unreal.DeviceColorCurveData(StructBase)`

```python
unreal.DeviceColorCurveData.__init__(enable: bool = False, reset_after_completion: bool = False, device_color_curve: CurveLinearColor = None) -> None
unreal.DeviceColorCurveData.device_color_curve(value: CurveLinearColor) -> None
unreal.DeviceColorCurveData.enable(value: bool) -> None
unreal.DeviceColorCurveData.reset_after_completion(value: bool) -> None
```

## `unreal.DrawGeometryParams(ParamsBase)`

```python
unreal.DrawGeometryParams.__init__(draw: bool = False, default_z: float = 0.000000, eids: Array[str] = []) -> None
unreal.DrawGeometryParams.default_z(value: float) -> None
unreal.DrawGeometryParams.draw(value: bool) -> None
unreal.DrawGeometryParams.eids(value: Array[str]) -> None
```

## `unreal.EarthInstanceSplineFragment(EarthEntityFragment)`

```python
unreal.EarthInstanceSplineFragment.__init__(validated: bool = False, valid: bool = False, points_order: EarthPointsOrder = EarthPointsOrder.KEEP, start_extension: float = 0.000000, end_extension: float = 0.000000, spline_deform_type: EarthSplineDeformType = EarthSplineDeformType.CURVE, forward_axis: SplineMeshAxis = SplineMeshAxis.X, spline_up_dir: Vector3f = [0.000000, 0.000000, 0.000000], world_smooth_interp_roll_scale: bool = False, local_smooth_interp_roll_scale: bool = False, control_type: EarthSplineSizeControlType = EarthSplineSizeControlType.SCALE, start_scale: Vector2f = [0.000000, 0.000000], start_offset: Vector2f = [0.000000, 0.000000], start_width: Vector2f = [0.000000, 0.000000], start_height: Vector2f = [0.000000, 0.000000], start_roll: float = 0.000000, end_scale: Vector2f = [0.000000, 0.000000], end_offset: Vector2f = [0.000000, 0.000000], end_width: Vector2f = [0.000000, 0.000000], end_height: Vector2f = [0.000000, 0.000000], end_roll: float = 0.000000, resample_by_edge: bool = False, placement_type: EarthSplinePlacementType = EarthSplinePlacementType.CONTINUOUS, gap_between_bounds: float = 0.000000, alignment_type: EarthSplineAlignmentType = EarthSplineAlignmentType.NORMAL, use_random_parameter: bool = False, rotation_range: Vector2f = [0.000000, 0.000000], scale_range: Vector2f = [0.000000, 0.000000], start_scale_x: float = 0.000000, end_scale_x: float = 0.000000, chamfer_corner: bool = False, chamfer_length: float = 0.000000, instance_mesh_list: EarthRoadInstanceShapeGrammar = [{}, "", "", ""], multi_width_params: Array[WidthParam] = [], remove_ratios: ModifyRanges = [[]]) -> None
unreal.EarthInstanceSplineFragment.alignment_type(value: EarthSplineAlignmentType) -> None
unreal.EarthInstanceSplineFragment.chamfer_corner(value: bool) -> None
unreal.EarthInstanceSplineFragment.chamfer_length(value: float) -> None
unreal.EarthInstanceSplineFragment.control_type(value: EarthSplineSizeControlType) -> None
unreal.EarthInstanceSplineFragment.end_extension(value: float) -> None
unreal.EarthInstanceSplineFragment.end_height(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.end_offset(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.end_roll(value: float) -> None
unreal.EarthInstanceSplineFragment.end_scale(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.end_scale_x(value: float) -> None
unreal.EarthInstanceSplineFragment.end_width(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.forward_axis(value: SplineMeshAxis) -> None
unreal.EarthInstanceSplineFragment.gap_between_bounds(value: float) -> None
unreal.EarthInstanceSplineFragment.instance_mesh_list(value: EarthRoadInstanceShapeGrammar) -> None
unreal.EarthInstanceSplineFragment.local_smooth_interp_roll_scale(value: bool) -> None
unreal.EarthInstanceSplineFragment.multi_width_params(value: Array[WidthParam]) -> None
unreal.EarthInstanceSplineFragment.placement_type(value: EarthSplinePlacementType) -> None
unreal.EarthInstanceSplineFragment.points_order(value: EarthPointsOrder) -> None
unreal.EarthInstanceSplineFragment.remove_ratios(value: ModifyRanges) -> None
unreal.EarthInstanceSplineFragment.resample_by_edge(value: bool) -> None
unreal.EarthInstanceSplineFragment.rotation_range(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.scale_range(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.spline_deform_type(value: EarthSplineDeformType) -> None
unreal.EarthInstanceSplineFragment.spline_up_dir(value: Vector3f) -> None
unreal.EarthInstanceSplineFragment.start_extension(value: float) -> None
unreal.EarthInstanceSplineFragment.start_height(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.start_offset(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.start_roll(value: float) -> None
unreal.EarthInstanceSplineFragment.start_scale(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.start_scale_x(value: float) -> None
unreal.EarthInstanceSplineFragment.start_width(value: Vector2f) -> None
unreal.EarthInstanceSplineFragment.use_random_parameter(value: bool) -> None
unreal.EarthInstanceSplineFragment.world_smooth_interp_roll_scale(value: bool) -> None
```

## `unreal.EarthInstanceSplinePrefab(EarthPrefabBase)`

```python
unreal.EarthInstanceSplinePrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthInstancedSplineMeshOverrideFragment(EarthInstanceSplineFragment)`

```python
unreal.EarthInstancedSplineMeshOverrideFragment.__init__(validated: bool = False, valid: bool = False, points_order: EarthPointsOrder = EarthPointsOrder.KEEP, start_extension: float = 0.000000, end_extension: float = 0.000000, spline_deform_type: EarthSplineDeformType = EarthSplineDeformType.CURVE, forward_axis: SplineMeshAxis = SplineMeshAxis.X, spline_up_dir: Vector3f = [0.000000, 0.000000, 0.000000], world_smooth_interp_roll_scale: bool = False, local_smooth_interp_roll_scale: bool = False, control_type: EarthSplineSizeControlType = EarthSplineSizeControlType.SCALE, start_scale: Vector2f = [0.000000, 0.000000], start_offset: Vector2f = [0.000000, 0.000000], start_width: Vector2f = [0.000000, 0.000000], start_height: Vector2f = [0.000000, 0.000000], start_roll: float = 0.000000, end_scale: Vector2f = [0.000000, 0.000000], end_offset: Vector2f = [0.000000, 0.000000], end_width: Vector2f = [0.000000, 0.000000], end_height: Vector2f = [0.000000, 0.000000], end_roll: float = 0.000000, resample_by_edge: bool = False, placement_type: EarthSplinePlacementType = EarthSplinePlacementType.CONTINUOUS, gap_between_bounds: float = 0.000000, alignment_type: EarthSplineAlignmentType = EarthSplineAlignmentType.NORMAL, use_random_parameter: bool = False, rotation_range: Vector2f = [0.000000, 0.000000], scale_range: Vector2f = [0.000000, 0.000000], start_scale_x: float = 0.000000, end_scale_x: float = 0.000000, chamfer_corner: bool = False, chamfer_length: float = 0.000000, instance_mesh_list: EarthRoadInstanceShapeGrammar = [{}, "", "", ""], multi_width_params: Array[WidthParam] = [], remove_ratios: ModifyRanges = [[]]) -> None
```

## `unreal.EarthPcgPointFragment(EarthSpatialFragment)`

```python
unreal.EarthPcgPointFragment.__init__(validated: bool = False, valid: bool = False, owned_component: ActorComponent = None, with_: int = 0, height: int = 0, positions: Array[Vector] = [], normals: Array[Vector] = [], colors: Array[Vector4] = [], vgm: Array[float] = [], lcg: Array[float] = [], bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False]) -> None
unreal.EarthPcgPointFragment.bounds(value: Box) -> None
unreal.EarthPcgPointFragment.colors(value: Array[Vector4]) -> None
unreal.EarthPcgPointFragment.height(value: int) -> None
unreal.EarthPcgPointFragment.lcg(value: Array[float]) -> None
unreal.EarthPcgPointFragment.normals(value: Array[Vector]) -> None
unreal.EarthPcgPointFragment.positions(value: Array[Vector]) -> None
unreal.EarthPcgPointFragment.vgm(value: Array[float]) -> None
unreal.EarthPcgPointFragment.with_(value: int) -> None
```

## `unreal.EarthSplineComponent(SplineComponent)`

```python
unreal.EarthSplineComponent.feature_id(value: int) -> None
unreal.EarthSplineComponent.get_spatial_data() -> InstancedStruct
unreal.EarthSplineComponent.get_spatial_data_type() -> EarthSpatialDataType
unreal.EarthSplineComponent.prefab_asset(value: EarthPrefabAsset) -> None
unreal.EarthSplineComponent.set_spatial_data(spatial_data: InstancedStruct) -> None
unreal.EarthSplineComponent.set_spatial_data_type(spatial_data_type: EarthSpatialDataType) -> None
unreal.EarthSplineComponent.spatial_data(value: InstancedStruct) -> None
unreal.EarthSplineComponent.spatial_data_type(value: EarthSpatialDataType) -> None
unreal.EarthSplineComponent.update_spatial_data() -> None
```

## `unreal.EarthSplineCurveFragment(EarthPrimitiveFragment)`

```python
unreal.EarthSplineCurveFragment.__init__(validated: bool = False, valid: bool = False, owned_component: ActorComponent = None, vertices: Array[Vector] = [], area: float = 0.000000, closed_loop: bool = False, clockwise: bool = False, min_area_bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], bounds_rotation: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

## `unreal.EarthSplineCurvePrefab(EarthSpatialPrefab)`

```python
unreal.EarthSplineCurvePrefab.__init__(fragments: Array[InstancedStruct] = []) -> None
```

## `unreal.EarthSplineCurves(StructBase)`

```python
unreal.EarthSplineCurves.__init__() -> None
```

## `unreal.EarthSplineCurvesMetadata(StructBase)`

```python
unreal.EarthSplineCurvesMetadata.__init__() -> None
```

## `unreal.EarthTerraformingSplineFragment(EarthEntityFragment)`

```python
unreal.EarthTerraformingSplineFragment.__init__(validated: bool = False, valid: bool = False, spline_width: float = 0.000000, offset_z: float = 0.000000, edge_width: float = 0.000000, edge_offset_z: float = 0.000000, mask_width: float = 0.000000, depth: float = 0.000000, surface_widths: Array[float] = [], edge_widths: Array[float] = [], use_uniform_width: bool = False, min_width: float = 0.000000) -> None
unreal.EarthTerraformingSplineFragment.depth(value: float) -> None
unreal.EarthTerraformingSplineFragment.edge_offset_z(value: float) -> None
unreal.EarthTerraformingSplineFragment.edge_width(value: float) -> None
unreal.EarthTerraformingSplineFragment.edge_widths(value: Array[float]) -> None
unreal.EarthTerraformingSplineFragment.mask_width(value: float) -> None
unreal.EarthTerraformingSplineFragment.min_width(value: float) -> None
unreal.EarthTerraformingSplineFragment.offset_z(value: float) -> None
unreal.EarthTerraformingSplineFragment.spline_width(value: float) -> None
unreal.EarthTerraformingSplineFragment.surface_widths(value: Array[float]) -> None
unreal.EarthTerraformingSplineFragment.use_uniform_width(value: bool) -> None
```

## `unreal.EarthTerraformingSplineMeshGenerator(StructBase)`

```python
unreal.EarthTerraformingSplineMeshGenerator.__init__() -> None
```

## `unreal.EarthWaterColorPreset(StructBase)`

```python
unreal.EarthWaterColorPreset.__init__(scattering_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], absorption_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], behind_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], overlay_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], clarity: float = 0.000000, phase_g: float = 0.000000) -> None
unreal.EarthWaterColorPreset.absorption_color(value: LinearColor) -> None
unreal.EarthWaterColorPreset.behind_color(value: LinearColor) -> None
unreal.EarthWaterColorPreset.clarity(value: float) -> None
unreal.EarthWaterColorPreset.overlay_color(value: LinearColor) -> None
unreal.EarthWaterColorPreset.phase_g(value: float) -> None
unreal.EarthWaterColorPreset.scattering_color(value: LinearColor) -> None
```

## `unreal.EarthWaterSettings(EarthLayerSettingsBase)`

```python
unreal.EarthWaterSettings.__init__(use_bake_board: bool = False) -> None
```

## `unreal.FloatCurve(AnimCurveBase)`

```python
unreal.FloatCurve.__init__() -> None
```

## `unreal.FoliageDensityFalloff(StructBase)`

```python
unreal.FoliageDensityFalloff.__init__() -> None
```

## `unreal.FoliageStatistics(BlueprintFunctionLibrary)`

```python
unreal.FoliageStatistics.foliage_overlapping_box_count(world_context_object: Object, static_mesh: StaticMesh, box: Box) -> int
unreal.FoliageStatistics.foliage_overlapping_box_transforms(world_context_object: Object, static_mesh: StaticMesh, box: Box) -> Array[Transform]
unreal.FoliageStatistics.foliage_overlapping_sphere_count(world_context_object: Object, static_mesh: StaticMesh, center_position: Vector, radius: float) -> int
```

## `unreal.FoliageType(Object)`

```python
unreal.FoliageType.affect_distance_field_lighting() -> bool
unreal.FoliageType.affect_dynamic_indirect_lighting() -> bool
unreal.FoliageType.align_max_angle(value: float) -> None
unreal.FoliageType.align_to_normal(value: bool) -> None
unreal.FoliageType.average_normal(value: bool) -> None
unreal.FoliageType.average_normal_sample_count(value: int) -> None
unreal.FoliageType.average_normal_single_component(value: bool) -> None
unreal.FoliageType.cast_contact_shadow() -> bool
unreal.FoliageType.cast_dynamic_shadow() -> bool
unreal.FoliageType.cast_shadow() -> bool
unreal.FoliageType.cast_shadow_as_two_sided() -> bool
unreal.FoliageType.cast_static_shadow() -> bool
unreal.FoliageType.collision_scale(value: Vector) -> None
unreal.FoliageType.collision_with_world(value: bool) -> None
unreal.FoliageType.custom_depth_stencil_value() -> int
unreal.FoliageType.custom_depth_stencil_write_mask() -> RendererStencilMask
unreal.FoliageType.evaluate_world_position_offset() -> bool
unreal.FoliageType.exclusion_landscape_layers(value: Array[Name]) -> None
unreal.FoliageType.ground_slope_angle(value: FloatInterval) -> None
unreal.FoliageType.height(value: FloatInterval) -> None
unreal.FoliageType.include_in_hlod(value: bool) -> None
unreal.FoliageType.landscape_layers(value: Array[Name]) -> None
unreal.FoliageType.lighting_channels() -> LightingChannels
unreal.FoliageType.lightmap_type() -> LightmapType
unreal.FoliageType.minimum_exclusion_layer_weight(value: float) -> None
unreal.FoliageType.minimum_layer_weight(value: float) -> None
unreal.FoliageType.mobility() -> ComponentMobility
unreal.FoliageType.overridden_light_map_res() -> int
unreal.FoliageType.override_light_map_res() -> bool
unreal.FoliageType.random_pitch_angle(value: float) -> None
unreal.FoliageType.random_yaw(value: bool) -> None
unreal.FoliageType.receives_decals() -> bool
unreal.FoliageType.render_custom_depth() -> bool
unreal.FoliageType.runtime_virtual_textures(value: Array[RuntimeVirtualTexture]) -> None
unreal.FoliageType.shadow_cache_invalidation_behavior() -> ShadowCacheInvalidationBehavior
unreal.FoliageType.translucency_sort_priority() -> int
unreal.FoliageType.use_as_occluder() -> bool
unreal.FoliageType.virtual_texture_cull_mips() -> int
unreal.FoliageType.virtual_texture_render_pass_type() -> RuntimeVirtualTextureMainPassType
unreal.FoliageType.visible_in_ray_tracing() -> bool
unreal.FoliageType.world_position_offset_disable_distance() -> int
unreal.FoliageType.z_offset(value: FloatInterval) -> None
```

## `unreal.FoliageTypeObject(StructBase)`

```python
unreal.FoliageTypeObject.__init__() -> None
```

## `unreal.FoliageVertexColorChannelMask(StructBase)`

```python
unreal.FoliageVertexColorChannelMask.__init__() -> None
```

## `unreal.Geometry(StructBase)`

```python
unreal.Geometry.__init__() -> None
```

## `unreal.GeometryCache(Object)`

```python
unreal.GeometryCache.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GeometryCache.end_frame() -> int
unreal.GeometryCache.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.GeometryCache.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GeometryCache.material_slot_names(value: Array[Name]) -> None
unreal.GeometryCache.materials(value: Array[MaterialInterface]) -> None
unreal.GeometryCache.start_frame() -> int
```

## `unreal.GeometryCacheComponent(MeshComponent)`

```python
unreal.GeometryCacheComponent.duration() -> float
unreal.GeometryCacheComponent.geometry_cache() -> GeometryCache
unreal.GeometryCacheComponent.get_animation_time() -> float
unreal.GeometryCacheComponent.get_duration() -> float
unreal.GeometryCacheComponent.get_elapsed_time() -> float
unreal.GeometryCacheComponent.get_motion_vector_scale() -> float
unreal.GeometryCacheComponent.get_number_of_frames() -> int
unreal.GeometryCacheComponent.get_number_of_tracks() -> int
unreal.GeometryCacheComponent.get_override_wireframe_color() -> bool
unreal.GeometryCacheComponent.get_playback_direction() -> float
unreal.GeometryCacheComponent.get_playback_speed() -> float
unreal.GeometryCacheComponent.get_start_time_offset() -> float
unreal.GeometryCacheComponent.get_wireframe_override_color() -> LinearColor
unreal.GeometryCacheComponent.is_extrapolating_frames() -> bool
unreal.GeometryCacheComponent.is_looping() -> bool
unreal.GeometryCacheComponent.is_playing() -> bool
unreal.GeometryCacheComponent.is_playing_reversed() -> bool
unreal.GeometryCacheComponent.looping(value: bool) -> None
unreal.GeometryCacheComponent.motion_vector_scale(value: float) -> None
unreal.GeometryCacheComponent.pause() -> None
unreal.GeometryCacheComponent.play() -> None
unreal.GeometryCacheComponent.play_from_start() -> None
unreal.GeometryCacheComponent.play_reversed() -> None
unreal.GeometryCacheComponent.play_reversed_from_end() -> None
unreal.GeometryCacheComponent.playback_speed(value: float) -> None
unreal.GeometryCacheComponent.running(value: bool) -> None
unreal.GeometryCacheComponent.set_extrapolate_frames(new_extrapolating: bool) -> None
unreal.GeometryCacheComponent.set_geometry_cache(new_geom_cache: GeometryCache) -> bool
unreal.GeometryCacheComponent.set_looping(new_looping: bool) -> None
unreal.GeometryCacheComponent.set_motion_vector_scale(new_motion_vector_scale: float) -> None
unreal.GeometryCacheComponent.set_override_wireframe_color(override: bool) -> None
unreal.GeometryCacheComponent.set_playback_speed(new_playback_speed: float) -> None
unreal.GeometryCacheComponent.set_start_time_offset(new_start_time_offset: float) -> None
unreal.GeometryCacheComponent.set_wireframe_override_color(color: LinearColor) -> None
unreal.GeometryCacheComponent.start_time_offset(value: float) -> None
unreal.GeometryCacheComponent.stop() -> None
unreal.GeometryCacheComponent.tick_at_this_time(time: float, is_running: bool, backwards: bool, is_looping: bool) -> None
```

## `unreal.GeometryCacheStreamerSettings(DeveloperSettings)`

```python
unreal.GeometryCacheStreamerSettings.look_ahead_buffer(value: float) -> None
unreal.GeometryCacheStreamerSettings.max_memory_allowed(value: float) -> None
```

## `unreal.GeometryCollection(Object)`

```python
unreal.GeometryCollection.add_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GeometryCollection.asset_import_data(value: AssetImportData) -> None
unreal.GeometryCollection.collision_object_reduction_percentage(value: float) -> None
unreal.GeometryCollection.collision_particles_fraction(value: float) -> None
unreal.GeometryCollection.collision_type(value: CollisionTypeEnum) -> None
unreal.GeometryCollection.convert_vertex_colors_to_srgb(value: bool) -> None
unreal.GeometryCollection.custom_renderer_type(value: Class) -> None
unreal.GeometryCollection.damage_model(value: DamageModelTypeEnum) -> None
unreal.GeometryCollection.dataflow_asset(value: Dataflow) -> None
unreal.GeometryCollection.density_from_physics_material(value: bool) -> None
unreal.GeometryCollection.enable_nanite(value: bool) -> None
unreal.GeometryCollection.enable_remove_pieces_on_fracture(value: bool) -> None
unreal.GeometryCollection.geometry_source(value: Array[GeometryCollectionSource]) -> None
unreal.GeometryCollection.get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
unreal.GeometryCollection.has_asset_user_data_of_class(user_data_class: Class) -> bool
unreal.GeometryCollection.implicit_type(value: ImplicitTypeEnum) -> None
unreal.GeometryCollection.import_collision_from_source(value: bool) -> None
unreal.GeometryCollection.mass(value: float) -> None
unreal.GeometryCollection.mass_as_density(value: bool) -> None
unreal.GeometryCollection.max_cluster_level_set_resolution(value: int) -> None
unreal.GeometryCollection.max_level_set_resolution(value: int) -> None
unreal.GeometryCollection.maximum_collision_particles(value: int) -> None
unreal.GeometryCollection.maximum_sleep_time() -> Vector2D
unreal.GeometryCollection.min_cluster_level_set_resolution(value: int) -> None
unreal.GeometryCollection.min_level_set_resolution(value: int) -> None
unreal.GeometryCollection.minimum_mass_clamp() -> float
unreal.GeometryCollection.optimize_convexes(value: bool) -> None
unreal.GeometryCollection.overrides(value: Map[str, str]) -> None
unreal.GeometryCollection.physics_material() -> PhysicalMaterial
unreal.GeometryCollection.removal_duration() -> Vector2D
unreal.GeometryCollection.remove_on_fracture_materials(value: Array[MaterialInterface]) -> None
unreal.GeometryCollection.remove_on_max_sleep() -> bool
unreal.GeometryCollection.root_proxy(value: SoftObjectPath) -> None
unreal.GeometryCollection.root_proxy_data(value: GeometryCollectionProxyMeshData) -> None
unreal.GeometryCollection.scale_on_removal(value: bool) -> None
unreal.GeometryCollection.set_convert_vertex_colors_to_srgb(value: bool) -> None
unreal.GeometryCollection.set_enable_nanite(value: bool) -> None
unreal.GeometryCollection.slow_moving_as_sleeping() -> bool
unreal.GeometryCollection.slow_moving_velocity_threshold() -> float
unreal.GeometryCollection.strip_on_cook(value: bool) -> None
unreal.GeometryCollection.strip_render_data_on_cook(value: bool) -> None
unreal.GeometryCollection.use_material_damage_modifiers(value: bool) -> None
```

## `unreal.GeometryCollectionAutoInstanceMesh(StructBase)`

```python
unreal.GeometryCollectionAutoInstanceMesh.__init__(mesh: StaticMesh = None, materials: Array[MaterialInterface] = []) -> None
unreal.GeometryCollectionAutoInstanceMesh.materials(value: Array[MaterialInterface]) -> None
unreal.GeometryCollectionAutoInstanceMesh.mesh(value: StaticMesh) -> None
unreal.GeometryCollectionAutoInstanceMesh.static_mesh(value: SoftObjectPath) -> None
```

## `unreal.GeometryCollectionComponent(MeshComponent)`

```python
unreal.GeometryCollectionComponent.abandoned_collision_profile_name(value: Name) -> None
unreal.GeometryCollectionComponent.allow_removal_on_break(value: bool) -> None
unreal.GeometryCollectionComponent.allow_removal_on_sleep(value: bool) -> None
unreal.GeometryCollectionComponent.angular_ether_drag(value: float) -> None
unreal.GeometryCollectionComponent.apply_angular_velocity(item_index: int, angular_velocity: Vector) -> None
unreal.GeometryCollectionComponent.apply_asset_defaults() -> None
unreal.GeometryCollectionComponent.apply_breaking_angular_velocity(item_index: int, angular_velocity: Vector) -> None
unreal.GeometryCollectionComponent.apply_breaking_linear_velocity(item_index: int, linear_velocity: Vector) -> None
unreal.GeometryCollectionComponent.apply_external_strain(item_index: int, location: Vector, radius: float = 0.000000, propagation_depth: int = 0, propagation_factor: float = 1.000000, strain: float = 0.000000) -> None
unreal.GeometryCollectionComponent.apply_internal_strain(item_index: int, location: Vector, radius: float = 0.000000, propagation_depth: int = 0, propagation_factor: float = 1.000000, strain: float = 0.000000) -> None
unreal.GeometryCollectionComponent.apply_kinematic_field(radius: float, position: Vector) -> None
unreal.GeometryCollectionComponent.apply_linear_velocity(item_index: int, linear_velocity: Vector) -> None
unreal.GeometryCollectionComponent.apply_physics_field(enabled: bool, target: GeometryCollectionPhysicsTypeEnum, meta_data: FieldSystemMetaData, field: FieldNodeBase) -> None
unreal.GeometryCollectionComponent.cache_playback() -> bool
unreal.GeometryCollectionComponent.chaos_solver_actor(value: ChaosSolverActor) -> None
unreal.GeometryCollectionComponent.cluster_connection_type(value: ClusterConnectionTypeEnum) -> None
unreal.GeometryCollectionComponent.cluster_group_index(value: int) -> None
unreal.GeometryCollectionComponent.collision_group(value: int) -> None
unreal.GeometryCollectionComponent.collision_profile_per_level(value: Array[Name]) -> None
unreal.GeometryCollectionComponent.collision_sample_fraction(value: float) -> None
unreal.GeometryCollectionComponent.crumble_active_clusters() -> None
unreal.GeometryCollectionComponent.crumble_cluster(item_index: int) -> None
unreal.GeometryCollectionComponent.crumbling_event_includes_children() -> bool
unreal.GeometryCollectionComponent.custom_renderer_type(value: Class) -> None
unreal.GeometryCollectionComponent.damage_model(value: DamageModelTypeEnum) -> None
unreal.GeometryCollectionComponent.damage_propagation_data(value: GeometryCollectionDamagePropagationData) -> None
unreal.GeometryCollectionComponent.damage_threshold(value: Array[float]) -> None
unreal.GeometryCollectionComponent.density_from_physics_material(value: bool) -> None
unreal.GeometryCollectionComponent.desired_cache_time() -> float
unreal.GeometryCollectionComponent.enable_abandon_after_level(value: bool) -> None
unreal.GeometryCollectionComponent.enable_clustering(value: bool) -> None
unreal.GeometryCollectionComponent.enable_damage_from_collision(value: bool) -> None
unreal.GeometryCollectionComponent.enable_replication(value: bool) -> None
unreal.GeometryCollectionComponent.enable_root_proxy_for_custom_renderer(enable: bool) -> None
unreal.GeometryCollectionComponent.force_broken_for_custom_renderer(force_broken: bool) -> None
unreal.GeometryCollectionComponent.force_motion_blur(value: bool) -> None
unreal.GeometryCollectionComponent.force_update_active_transforms(value: bool) -> None
unreal.GeometryCollectionComponent.get_debug_info() -> str
unreal.GeometryCollectionComponent.get_initial_level(item_index: int) -> int
unreal.GeometryCollectionComponent.get_initial_local_rest_transforms() -> Array[Transform]
unreal.GeometryCollectionComponent.get_local_bounds() -> Box
unreal.GeometryCollectionComponent.get_local_rest_transforms(initial_transforms: bool = False) -> Array[Transform]
unreal.GeometryCollectionComponent.get_mass_and_extents(item_index: int) -> Tuple[float, Box]
unreal.GeometryCollectionComponent.get_root_current_transform() -> Transform
unreal.GeometryCollectionComponent.get_root_index() -> int
unreal.GeometryCollectionComponent.get_root_initial_transform() -> Transform
unreal.GeometryCollectionComponent.global_crumbling_event_includes_children() -> bool
unreal.GeometryCollectionComponent.gravity_group_index(value: int) -> None
unreal.GeometryCollectionComponent.initial_angular_velocity(value: Vector) -> None
unreal.GeometryCollectionComponent.initial_linear_velocity(value: Vector) -> None
unreal.GeometryCollectionComponent.initial_velocity_type(value: InitialVelocityTypeEnum) -> None
unreal.GeometryCollectionComponent.initialization_fields() -> Array[FieldSystemActor]
unreal.GeometryCollectionComponent.is_root_broken() -> bool
unreal.GeometryCollectionComponent.linear_ether_drag(value: float) -> None
unreal.GeometryCollectionComponent.max_cluster_level(value: int) -> None
unreal.GeometryCollectionComponent.max_simulated_level(value: int) -> None
unreal.GeometryCollectionComponent.notify_breaks() -> bool
unreal.GeometryCollectionComponent.notify_collisions() -> bool
unreal.GeometryCollectionComponent.notify_crumblings() -> bool
unreal.GeometryCollectionComponent.notify_geometry_collection_physics_loading_state_change(value: NotifyGeometryCollectionPhysicsLoadingStateChange) -> None
unreal.GeometryCollectionComponent.notify_geometry_collection_physics_state_change(value: NotifyGeometryCollectionPhysicsStateChange) -> None
unreal.GeometryCollectionComponent.notify_global_breaks() -> bool
unreal.GeometryCollectionComponent.notify_global_collisions() -> bool
unreal.GeometryCollectionComponent.notify_global_crumblings() -> bool
unreal.GeometryCollectionComponent.notify_global_removals() -> bool
unreal.GeometryCollectionComponent.notify_removals() -> bool
unreal.GeometryCollectionComponent.notify_trailing() -> bool
unreal.GeometryCollectionComponent.object_type(value: ObjectStateTypeEnum) -> None
unreal.GeometryCollectionComponent.on_chaos_break_event(value: OnChaosBreakEvent) -> None
unreal.GeometryCollectionComponent.on_chaos_crumbling_event(value: OnChaosCrumblingEvent) -> None
unreal.GeometryCollectionComponent.on_chaos_physics_collision(value: OnChaosPhysicsCollision) -> None
unreal.GeometryCollectionComponent.on_chaos_removal_event(value: OnChaosRemovalEvent) -> None
unreal.GeometryCollectionComponent.one_way_interaction_level(value: int) -> None
unreal.GeometryCollectionComponent.override_custom_renderer(value: bool) -> None
unreal.GeometryCollectionComponent.physical_material(value: ChaosPhysicalMaterial) -> None
unreal.GeometryCollectionComponent.physical_material_override(value: PhysicalMaterial) -> None
unreal.GeometryCollectionComponent.receive_physics_collision(collision_info: ChaosPhysicsCollisionInfo) -> None
unreal.GeometryCollectionComponent.remove_all_anchors() -> None
unreal.GeometryCollectionComponent.replication_abandon_after_level(value: int) -> None
unreal.GeometryCollectionComponent.replication_abandon_cluster_level(value: int) -> None
unreal.GeometryCollectionComponent.replication_max_position_and_velocity_correction_level(value: int) -> None
unreal.GeometryCollectionComponent.rest_collection() -> GeometryCollection
unreal.GeometryCollectionComponent.run_time_data_collection_guid() -> Guid
unreal.GeometryCollectionComponent.set_abandoned_particle_collision_profile_name(collision_profile: Name) -> None
unreal.GeometryCollectionComponent.set_anchored_by_box(world_space_box: Box, anchored: bool, max_level: int = -1) -> None
unreal.GeometryCollectionComponent.set_anchored_by_index(index: int, anchored: bool) -> None
unreal.GeometryCollectionComponent.set_anchored_by_transformed_box(box: Box, transform: Transform, anchored: bool, max_level: int = -1) -> None
unreal.GeometryCollectionComponent.set_enable_damage_from_collision(value: bool) -> None
unreal.GeometryCollectionComponent.set_local_rest_transforms(transforms: Array[Transform], only_leaves: bool) -> None
unreal.GeometryCollectionComponent.set_notify_breaks(new_notify_breaks: bool) -> None
unreal.GeometryCollectionComponent.set_notify_crumblings(new_notify_crumblings: bool, new_crumbling_event_includes_children: bool = False) -> None
unreal.GeometryCollectionComponent.set_notify_global_breaks(new_notify_global_breaks: bool) -> None
unreal.GeometryCollectionComponent.set_notify_global_collision(new_notify_global_collisions: bool) -> None
unreal.GeometryCollectionComponent.set_notify_global_crumblings(new_notify_global_crumblings: bool, global_new_crumbling_event_includes_children: bool) -> None
unreal.GeometryCollectionComponent.set_notify_global_removals(new_notify_global_removals: bool) -> None
unreal.GeometryCollectionComponent.set_notify_removals(new_notify_removals: bool) -> None
unreal.GeometryCollectionComponent.set_per_level_collision_profile_names(profile_names: Array[Name]) -> None
unreal.GeometryCollectionComponent.set_per_particle_collision_profile_name(bone_ids: Array[int], profile_name: Name) -> None
unreal.GeometryCollectionComponent.set_rest_collection(rest_collection_in: GeometryCollection, apply_asset_defaults: bool = True) -> None
unreal.GeometryCollectionComponent.set_root_proxy_component_space_transform(index: int, root_proxy_transform: Transform) -> None
unreal.GeometryCollectionComponent.show_bone_colors(value: bool) -> None
unreal.GeometryCollectionComponent.simulating(value: bool) -> None
unreal.GeometryCollectionComponent.store_velocities() -> bool
unreal.GeometryCollectionComponent.update_component_transform_to_root_bone(value: bool) -> None
unreal.GeometryCollectionComponent.update_navigation_in_tick(value: bool) -> None
unreal.GeometryCollectionComponent.use_material_damage_modifiers(value: bool) -> None
unreal.GeometryCollectionComponent.use_root_proxy_for_navigation(value: bool) -> None
unreal.GeometryCollectionComponent.use_size_specific_damage_threshold(value: bool) -> None
unreal.GeometryCollectionComponent.use_static_mesh_collision_for_traces(value: bool) -> None
```

## `unreal.GeometryCollectionEmbeddedExemplar(StructBase)`

```python
unreal.GeometryCollectionEmbeddedExemplar.__init__() -> None
```

## `unreal.GeometryCollectionLibrary(BlueprintFunctionLibrary)`

```python
unreal.GeometryCollectionLibrary.set_custom_instance_data_by_index(geometry_collection_component: GeometryCollectionComponent, custom_data_index: int, custom_data_value: float) -> None
unreal.GeometryCollectionLibrary.set_custom_instance_data_by_name(geometry_collection_component: GeometryCollectionComponent, custom_data_name: Name, custom_data_value: float) -> None
unreal.GeometryCollectionLibrary.set_ism_pool_custom_instance_data(geometry_collection_component: GeometryCollectionComponent, custom_data_index: int, custom_data_value: float) -> None
```

## `unreal.GeometryCollectionProxyMeshData(StructBase)`

```python
unreal.GeometryCollectionProxyMeshData.__init__(proxy_meshes: Array[StaticMesh] = []) -> None
unreal.GeometryCollectionProxyMeshData.proxy_meshes(value: Array[StaticMesh]) -> None
```

## `unreal.GeometryCollectionSizeSpecificData(StructBase)`

```python
unreal.GeometryCollectionSizeSpecificData.__init__() -> None
unreal.GeometryCollectionSizeSpecificData.collision_object_reduction_percentage(value: int) -> None
unreal.GeometryCollectionSizeSpecificData.collision_particles_fraction(value: float) -> None
unreal.GeometryCollectionSizeSpecificData.collision_type(value: CollisionTypeEnum) -> None
unreal.GeometryCollectionSizeSpecificData.implicit_type(value: ImplicitTypeEnum) -> None
unreal.GeometryCollectionSizeSpecificData.max_cluster_level_set_resolution(value: int) -> None
unreal.GeometryCollectionSizeSpecificData.max_level_set_resolution(value: int) -> None
unreal.GeometryCollectionSizeSpecificData.maximum_collision_particles(value: int) -> None
unreal.GeometryCollectionSizeSpecificData.min_cluster_level_set_resolution(value: int) -> None
unreal.GeometryCollectionSizeSpecificData.min_level_set_resolution(value: int) -> None
```

## `unreal.GeometryCollectionSource(StructBase)`

```python
unreal.GeometryCollectionSource.__init__(source_geometry_object: SoftObjectPath = [""], local_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], source_material: Array[MaterialInterface] = [], instance_custom_data: Array[float] = [], add_internal_materials: bool = False, split_components: bool = False, set_internal_from_material_index: bool = False) -> None
unreal.GeometryCollectionSource.add_internal_materials(value: bool) -> None
unreal.GeometryCollectionSource.instance_custom_data(value: Array[float]) -> None
unreal.GeometryCollectionSource.local_transform(value: Transform) -> None
unreal.GeometryCollectionSource.set_internal_from_material_index(value: bool) -> None
unreal.GeometryCollectionSource.source_geometry_object(value: SoftObjectPath) -> None
unreal.GeometryCollectionSource.source_material(value: Array[MaterialInterface]) -> None
unreal.GeometryCollectionSource.split_components(value: bool) -> None
```

## `unreal.GeometryScript3DGridParameters(StructBase)`

```python
unreal.GeometryScript3DGridParameters.__init__(size_method: GeometryScriptGridSizingMethod = GeometryScriptGridSizingMethod.GRID_CELL_SIZE, grid_cell_size: float = 0.000000, grid_resolution: int = 0) -> None
unreal.GeometryScript3DGridParameters.grid_cell_size(value: float) -> None
unreal.GeometryScript3DGridParameters.grid_resolution(value: int) -> None
unreal.GeometryScript3DGridParameters.size_method(value: GeometryScriptGridSizingMethod) -> None
```

## `unreal.GeometryScriptAppendMeshOptions(StructBase)`

```python
unreal.GeometryScriptAppendMeshOptions.__init__(combine_mode: GeometryScriptCombineAttributesMode = GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING) -> None
unreal.GeometryScriptAppendMeshOptions.combine_mode(value: GeometryScriptCombineAttributesMode) -> None
```

## `unreal.GeometryScriptBakeOutputType(StructBase)`

```python
unreal.GeometryScriptBakeOutputType.__init__(output_mode: GeometryScriptBakeOutputMode = GeometryScriptBakeOutputMode.RGBA, rgba: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE], r: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE], g: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE], b: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE], a: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE]) -> None
unreal.GeometryScriptBakeOutputType.a(value: GeometryScriptBakeTypeOptions) -> None
unreal.GeometryScriptBakeOutputType.b(value: GeometryScriptBakeTypeOptions) -> None
unreal.GeometryScriptBakeOutputType.g(value: GeometryScriptBakeTypeOptions) -> None
unreal.GeometryScriptBakeOutputType.output_mode(value: GeometryScriptBakeOutputMode) -> None
unreal.GeometryScriptBakeOutputType.r(value: GeometryScriptBakeTypeOptions) -> None
unreal.GeometryScriptBakeOutputType.rgba(value: GeometryScriptBakeTypeOptions) -> None
```

## `unreal.GeometryScriptBakeSourceMeshOptions(StructBase)`

```python
unreal.GeometryScriptBakeSourceMeshOptions.__init__(source_normal_map: Texture2D = None, source_normal_uv_layer: int = 0, source_normal_space: GeometryScriptBakeNormalSpace = GeometryScriptBakeNormalSpace.TANGENT) -> None
unreal.GeometryScriptBakeSourceMeshOptions.source_normal_map(value: Texture2D) -> None
unreal.GeometryScriptBakeSourceMeshOptions.source_normal_space(value: GeometryScriptBakeNormalSpace) -> None
unreal.GeometryScriptBakeSourceMeshOptions.source_normal_uv_layer(value: int) -> None
```

## `unreal.GeometryScriptBakeTargetMeshOptions(StructBase)`

```python
unreal.GeometryScriptBakeTargetMeshOptions.__init__(target_uv_layer: int = 0) -> None
unreal.GeometryScriptBakeTargetMeshOptions.target_uv_layer(value: int) -> None
```

## `unreal.GeometryScriptBakeTypeOptions(StructBase)`

```python
unreal.GeometryScriptBakeTypeOptions.__init__(bake_type: GeometryScriptBakeTypes = GeometryScriptBakeTypes.NONE) -> None
unreal.GeometryScriptBakeTypeOptions.bake_type() -> GeometryScriptBakeTypes
```

## `unreal.GeometryScriptBakeVertexOptions(StructBase)`

```python
unreal.GeometryScriptBakeVertexOptions.__init__(split_at_normal_seams: bool = False, split_at_uv_seams: bool = False, projection_distance: float = 0.000000, projection_in_world_space: bool = False) -> None
unreal.GeometryScriptBakeVertexOptions.projection_distance(value: float) -> None
unreal.GeometryScriptBakeVertexOptions.projection_in_world_space(value: bool) -> None
unreal.GeometryScriptBakeVertexOptions.split_at_normal_seams(value: bool) -> None
unreal.GeometryScriptBakeVertexOptions.split_at_uv_seams(value: bool) -> None
```

## `unreal.GeometryScriptBendWarpOptions(StructBase)`

```python
unreal.GeometryScriptBendWarpOptions.__init__(symmetric_extents: bool = False, lower_extent: float = 0.000000, bidirectional: bool = False) -> None
unreal.GeometryScriptBendWarpOptions.bidirectional(value: bool) -> None
unreal.GeometryScriptBendWarpOptions.lower_extent(value: float) -> None
unreal.GeometryScriptBendWarpOptions.symmetric_extents(value: bool) -> None
```

## `unreal.GeometryScriptBlurMeshVertexColorsOptions(StructBase)`

```python
unreal.GeometryScriptBlurMeshVertexColorsOptions.__init__(red: bool = False, green: bool = False, blue: bool = False, alpha: bool = False) -> None
unreal.GeometryScriptBlurMeshVertexColorsOptions.alpha(value: bool) -> None
unreal.GeometryScriptBlurMeshVertexColorsOptions.blue(value: bool) -> None
unreal.GeometryScriptBlurMeshVertexColorsOptions.green(value: bool) -> None
unreal.GeometryScriptBlurMeshVertexColorsOptions.red(value: bool) -> None
```

## `unreal.GeometryScriptCalculateNormalsOptions(StructBase)`

```python
unreal.GeometryScriptCalculateNormalsOptions.__init__(angle_weighted: bool = False, area_weighted: bool = False) -> None
unreal.GeometryScriptCalculateNormalsOptions.angle_weighted(value: bool) -> None
unreal.GeometryScriptCalculateNormalsOptions.area_weighted(value: bool) -> None
```

## `unreal.GeometryScriptChannelPackResult(StructBase)`

```python
unreal.GeometryScriptChannelPackResult.__init__(output: Texture2D = None) -> None
unreal.GeometryScriptChannelPackResult.output(value: Texture2D) -> None
```

## `unreal.GeometryScriptChannelPackSource(StructBase)`

```python
unreal.GeometryScriptChannelPackSource.__init__(texture: Texture2D = None, read_gamma_space: GeometryScriptReadGammaSpace = GeometryScriptReadGammaSpace.FROM_TEXTURE_SETTINGS, channel: GeometryScriptRGBAChannel = GeometryScriptRGBAChannel.R, default_value: float = 0.000000) -> None
unreal.GeometryScriptChannelPackSource.channel(value: GeometryScriptRGBAChannel) -> None
unreal.GeometryScriptChannelPackSource.default_value(value: float) -> None
unreal.GeometryScriptChannelPackSource.read_gamma_space(value: GeometryScriptReadGammaSpace) -> None
unreal.GeometryScriptChannelPackSource.texture(value: Texture2D) -> None
```

## `unreal.GeometryScriptColorFlags(StructBase)`

```python
unreal.GeometryScriptColorFlags.__init__(red: bool = False, green: bool = False, blue: bool = False, alpha: bool = False) -> None
unreal.GeometryScriptColorFlags.alpha(value: bool) -> None
unreal.GeometryScriptColorFlags.blue(value: bool) -> None
unreal.GeometryScriptColorFlags.green(value: bool) -> None
unreal.GeometryScriptColorFlags.red(value: bool) -> None
```

## `unreal.GeometryScriptColorList(StructBase)`

```python
unreal.GeometryScriptColorList.__init__() -> None
unreal.GeometryScriptColorList.clear_color_list(clear_color: LinearColor) -> None
unreal.GeometryScriptColorList.convert_color_list_to_array() -> Array[LinearColor]
unreal.GeometryScriptColorList.duplicate_color_list() -> GeometryScriptColorList
unreal.GeometryScriptColorList.extract_color_list_channel(channel_index: int = 0) -> GeometryScriptScalarList
unreal.GeometryScriptColorList.extract_color_list_channels(x_channel_index: int = 0, y_channel_index: int = 1, z_channel_index: int = 2) -> GeometryScriptVectorList
unreal.GeometryScriptColorList.get_color_list_item(index: int) -> Tuple[LinearColor, bool]
unreal.GeometryScriptColorList.get_color_list_last_index() -> int
unreal.GeometryScriptColorList.get_color_list_length() -> int
unreal.GeometryScriptColorList.set_color_list_item(index: int, new_color: LinearColor) -> bool
```

## `unreal.GeometryScriptConstrainedDelaunayTriangulationOptions(StructBase)`

```python
unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.__init__(constrained_edges_fill_mode: GeometryScriptPolygonFillMode = GeometryScriptPolygonFillMode.ALL, validate_edges_in_result: bool = False, remove_duplicate_vertices: bool = False) -> None
unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.constrained_edges_fill_mode(value: GeometryScriptPolygonFillMode) -> None
unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.remove_duplicate_vertices(value: bool) -> None
unreal.GeometryScriptConstrainedDelaunayTriangulationOptions.validate_edges_in_result(value: bool) -> None
```

## `unreal.GeometryScriptConvexDecompositionOptions(StructBase)`

```python
unreal.GeometryScriptConvexDecompositionOptions.__init__(num_hulls: int = 0, search_factor: float = 0.000000, error_tolerance: float = 0.000000, min_part_thickness: float = 0.000000, simplify_to_face_count: int = 0) -> None
unreal.GeometryScriptConvexDecompositionOptions.error_tolerance(value: float) -> None
unreal.GeometryScriptConvexDecompositionOptions.min_part_thickness(value: float) -> None
unreal.GeometryScriptConvexDecompositionOptions.num_hulls(value: int) -> None
unreal.GeometryScriptConvexDecompositionOptions.search_factor(value: float) -> None
unreal.GeometryScriptConvexDecompositionOptions.simplify_to_face_count(value: int) -> None
```

## `unreal.GeometryScriptConvexHullApproximationOptions(StructBase)`

```python
unreal.GeometryScriptConvexHullApproximationOptions.__init__(fit_spheres: bool = False, fit_boxes: bool = False, distance_threshold: float = 0.000000, volume_diff_threshold_fraction: float = 0.000000) -> None
unreal.GeometryScriptConvexHullApproximationOptions.distance_threshold(value: float) -> None
unreal.GeometryScriptConvexHullApproximationOptions.fit_boxes(value: bool) -> None
unreal.GeometryScriptConvexHullApproximationOptions.fit_spheres(value: bool) -> None
unreal.GeometryScriptConvexHullApproximationOptions.volume_diff_threshold_fraction(value: float) -> None
```

## `unreal.GeometryScriptConvexHullOptions(StructBase)`

```python
unreal.GeometryScriptConvexHullOptions.__init__(prefilter_vertices: bool = False, prefilter_grid_resolution: int = 0, simplify_to_face_count: int = 0) -> None
unreal.GeometryScriptConvexHullOptions.prefilter_grid_resolution(value: int) -> None
unreal.GeometryScriptConvexHullOptions.prefilter_vertices(value: bool) -> None
unreal.GeometryScriptConvexHullOptions.simplify_to_face_count(value: int) -> None
```

## `unreal.GeometryScriptConvexHullSimplificationOptions(StructBase)`

```python
unreal.GeometryScriptConvexHullSimplificationOptions.__init__(simplification_method: GeometryScriptConvexHullSimplifyMethod = GeometryScriptConvexHullSimplifyMethod.MESH_Q_SLIM, simplification_distance_threshold: float = 0.000000, simplification_angle_threshold: float = 0.000000, min_target_face_count: int = 0) -> None
unreal.GeometryScriptConvexHullSimplificationOptions.min_target_face_count(value: int) -> None
unreal.GeometryScriptConvexHullSimplificationOptions.simplification_angle_threshold(value: float) -> None
unreal.GeometryScriptConvexHullSimplificationOptions.simplification_distance_threshold(value: float) -> None
unreal.GeometryScriptConvexHullSimplificationOptions.simplification_method(value: GeometryScriptConvexHullSimplifyMethod) -> None
```

## `unreal.GeometryScriptCopyMeshFromAssetOptions(StructBase)`

```python
unreal.GeometryScriptCopyMeshFromAssetOptions.__init__(apply_build_settings: bool = False, request_tangents: bool = False, ignore_remove_degenerates: bool = False, use_build_scale: bool = False) -> None
unreal.GeometryScriptCopyMeshFromAssetOptions.apply_build_settings(value: bool) -> None
unreal.GeometryScriptCopyMeshFromAssetOptions.ignore_remove_degenerates(value: bool) -> None
unreal.GeometryScriptCopyMeshFromAssetOptions.request_tangents(value: bool) -> None
unreal.GeometryScriptCopyMeshFromAssetOptions.use_build_scale(value: bool) -> None
```

## `unreal.GeometryScriptCopyMeshFromComponentOptions(StructBase)`

```python
unreal.GeometryScriptCopyMeshFromComponentOptions.__init__(want_normals: bool = False, want_tangents: bool = False, want_instance_colors: bool = False, requested_lod: GeometryScriptMeshReadLOD = [GeometryScriptLODType.MAX_AVAILABLE, 0]) -> None
unreal.GeometryScriptCopyMeshFromComponentOptions.requested_lod(value: GeometryScriptMeshReadLOD) -> None
unreal.GeometryScriptCopyMeshFromComponentOptions.want_instance_colors(value: bool) -> None
unreal.GeometryScriptCopyMeshFromComponentOptions.want_normals(value: bool) -> None
unreal.GeometryScriptCopyMeshFromComponentOptions.want_tangents(value: bool) -> None
```

## `unreal.GeometryScriptCopyMeshToAssetOptions(StructBase)`

```python
unreal.GeometryScriptCopyMeshToAssetOptions.__init__(enable_recompute_normals: bool = False, enable_recompute_tangents: bool = False, enable_remove_degenerates: bool = False, remap_bone_indices_to_match_asset: bool = False, use_original_vertex_order: bool = False, use_build_scale: bool = False, replace_materials: bool = False, new_materials: Array[MaterialInterface] = [], new_material_slot_names: Array[Name] = [], apply_nanite_settings: bool = False, nanite_settings: GeometryScriptNaniteOptions = [True, 100.000000, 0.000000], new_nanite_settings: MeshNaniteSettings = [False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0], emit_transaction: bool = False, defer_mesh_post_edit_change: bool = False) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.apply_nanite_settings(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.defer_mesh_post_edit_change(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.emit_transaction(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_normals(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_tangents(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.enable_remove_degenerates(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.nanite_settings(value: GeometryScriptNaniteOptions) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.new_material_slot_names(value: Array[Name]) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.new_materials(value: Array[MaterialInterface]) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.new_nanite_settings(value: MeshNaniteSettings) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.remap_bone_indices_to_match_asset(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.replace_materials(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.use_build_scale(value: bool) -> None
unreal.GeometryScriptCopyMeshToAssetOptions.use_original_vertex_order(value: bool) -> None
```

## `unreal.GeometryScriptCopyMorphTargetToAssetOptions(StructBase)`

```python
unreal.GeometryScriptCopyMorphTargetToAssetOptions.__init__(overwrite_existing_target: bool = False, emit_transaction: bool = False, defer_mesh_post_edit_change: bool = False) -> None
unreal.GeometryScriptCopyMorphTargetToAssetOptions.defer_mesh_post_edit_change(value: bool) -> None
unreal.GeometryScriptCopyMorphTargetToAssetOptions.emit_transaction(value: bool) -> None
unreal.GeometryScriptCopyMorphTargetToAssetOptions.overwrite_existing_target(value: bool) -> None
```

## `unreal.GeometryScriptCopySkinWeightProfileToAssetOptions(StructBase)`

```python
unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.__init__(overwrite_existing_profile: bool = False, emit_transaction: bool = False, defer_mesh_post_edit_change: bool = False) -> None
unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.defer_mesh_post_edit_change(value: bool) -> None
unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.emit_transaction(value: bool) -> None
unreal.GeometryScriptCopySkinWeightProfileToAssetOptions.overwrite_existing_profile(value: bool) -> None
```

## `unreal.GeometryScriptCreateNewVolumeFromMeshOptions(StructBase)`

```python
unreal.GeometryScriptCreateNewVolumeFromMeshOptions.__init__(volume_type: Class = None, auto_simplify: bool = False, max_triangles: int = 0) -> None
unreal.GeometryScriptCreateNewVolumeFromMeshOptions.auto_simplify(value: bool) -> None
unreal.GeometryScriptCreateNewVolumeFromMeshOptions.max_triangles(value: int) -> None
unreal.GeometryScriptCreateNewVolumeFromMeshOptions.volume_type(value: Class) -> None
```

## `unreal.GeometryScriptDebug(Object)`

```python
unreal.GeometryScriptDebug.messages(value: Array[GeometryScriptDebugMessage]) -> None
```

## `unreal.GeometryScriptDebugMessage(StructBase)`

```python
unreal.GeometryScriptDebugMessage.__init__(message_type: GeometryScriptDebugMessageType = GeometryScriptDebugMessageType.ERROR_MESSAGE, error_type: GeometryScriptErrorType = GeometryScriptErrorType.NO_ERROR, message: Text = "") -> None
unreal.GeometryScriptDebugMessage.error_type(value: GeometryScriptErrorType) -> None
unreal.GeometryScriptDebugMessage.message(value: Text) -> None
unreal.GeometryScriptDebugMessage.message_type(value: GeometryScriptDebugMessageType) -> None
```

## `unreal.GeometryScriptDegenerateTriangleOptions(StructBase)`

```python
unreal.GeometryScriptDegenerateTriangleOptions.__init__(mode: GeometryScriptRepairMeshMode = GeometryScriptRepairMeshMode.DELETE_ONLY, min_triangle_area: float = 0.000000, min_edge_length: float = 0.000000, compact_on_completion: bool = False) -> None
unreal.GeometryScriptDegenerateTriangleOptions.compact_on_completion(value: bool) -> None
unreal.GeometryScriptDegenerateTriangleOptions.min_edge_length(value: float) -> None
unreal.GeometryScriptDegenerateTriangleOptions.min_triangle_area(value: float) -> None
unreal.GeometryScriptDegenerateTriangleOptions.mode(value: GeometryScriptRepairMeshMode) -> None
```

## `unreal.GeometryScriptDetermineMeshOcclusionOptions(StructBase)`

```python
unreal.GeometryScriptDetermineMeshOcclusionOptions.__init__(sampling_density: float = 0.000000, double_sided: bool = False, num_search_directions: int = 0) -> None
unreal.GeometryScriptDetermineMeshOcclusionOptions.double_sided(value: bool) -> None
unreal.GeometryScriptDetermineMeshOcclusionOptions.num_search_directions(value: int) -> None
unreal.GeometryScriptDetermineMeshOcclusionOptions.sampling_density(value: float) -> None
```

## `unreal.GeometryScriptDynamicMeshBVH(StructBase)`

```python
unreal.GeometryScriptDynamicMeshBVH.__init__() -> None
unreal.GeometryScriptDynamicMeshBVH.reset_bvh() -> None
```

## `unreal.GeometryScriptExpMapUVOptions(StructBase)`

```python
unreal.GeometryScriptExpMapUVOptions.__init__(normal_smoothing_rounds: int = 0, normal_smoothing_alpha: float = 0.000000) -> None
unreal.GeometryScriptExpMapUVOptions.normal_smoothing_alpha(value: float) -> None
unreal.GeometryScriptExpMapUVOptions.normal_smoothing_rounds(value: int) -> None
```

## `unreal.GeometryScriptFillHolesOptions(StructBase)`

```python
unreal.GeometryScriptFillHolesOptions.__init__(fill_method: GeometryScriptFillHolesMethod = GeometryScriptFillHolesMethod.AUTOMATIC, delete_isolated_triangles: bool = False) -> None
unreal.GeometryScriptFillHolesOptions.delete_isolated_triangles(value: bool) -> None
unreal.GeometryScriptFillHolesOptions.fill_method(value: GeometryScriptFillHolesMethod) -> None
```

## `unreal.GeometryScriptFlareWarpOptions(StructBase)`

```python
unreal.GeometryScriptFlareWarpOptions.__init__(symmetric_extents: bool = False, lower_extent: float = 0.000000, flare_type: GeometryScriptFlareType = GeometryScriptFlareType.SIN_MODE) -> None
unreal.GeometryScriptFlareWarpOptions.flare_type(value: GeometryScriptFlareType) -> None
unreal.GeometryScriptFlareWarpOptions.lower_extent(value: float) -> None
unreal.GeometryScriptFlareWarpOptions.symmetric_extents(value: bool) -> None
```

## `unreal.GeometryScriptGeneralPolygonList(StructBase)`

```python
unreal.GeometryScriptGeneralPolygonList.__init__() -> None
unreal.GeometryScriptGeneralPolygonList.add_polygon_to_list(outer_polygon: GeometryScriptSimplePolygon, hole_polygons: Array[GeometryScriptSimplePolygon], fix_hole_orientations: bool = True) -> int
unreal.GeometryScriptGeneralPolygonList.append_polygon_list(polygons_to_append: GeometryScriptGeneralPolygonList) -> None
unreal.GeometryScriptGeneralPolygonList.get_polygon_area(polygon_index: int) -> Tuple[float, bool]
unreal.GeometryScriptGeneralPolygonList.get_polygon_bounds(polygon_index: int) -> Tuple[Box2D, bool]
unreal.GeometryScriptGeneralPolygonList.get_polygon_count() -> int
unreal.GeometryScriptGeneralPolygonList.get_polygon_hole_count(polygon_index: int) -> Tuple[int, bool]
unreal.GeometryScriptGeneralPolygonList.get_polygon_list_area() -> float
unreal.GeometryScriptGeneralPolygonList.get_polygon_list_bounds() -> Box2D
unreal.GeometryScriptGeneralPolygonList.get_polygon_vertex(vertex_index: int, polygon_index: int, hole_index: int = -1) -> Tuple[Vector2D, bool]
unreal.GeometryScriptGeneralPolygonList.get_polygon_vertex_count(polygon_index: int, hole_index: int = -1) -> Tuple[int, bool]
unreal.GeometryScriptGeneralPolygonList.get_polygon_vertices(polygon_index: int, hole_index: int = -1) -> Tuple[Array[Vector2D], bool]
unreal.GeometryScriptGeneralPolygonList.get_simple_polygon(polygon_index: int, hole_index: int = -1) -> Tuple[GeometryScriptSimplePolygon, bool]
unreal.GeometryScriptGeneralPolygonList.polygons_difference(polygons_to_subtract: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScriptGeneralPolygonList.polygons_exclusive_or(polygons_to_exclusive_or: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScriptGeneralPolygonList.polygons_intersection(polygons_to_intersect: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScriptGeneralPolygonList.polygons_morphology_close(offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScriptGeneralPolygonList.polygons_morphology_open(offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScriptGeneralPolygonList.polygons_offset(offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScriptGeneralPolygonList.polygons_offsets(offset_options: GeometryScriptPolygonOffsetOptions, first_offset: float, second_offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScriptGeneralPolygonList.polygons_union(copy_input_on_failure: bool = True) -> GeometryScriptGeneralPolygonList
```

## `unreal.GeometryScriptGroupLayer(StructBase)`

```python
unreal.GeometryScriptGroupLayer.__init__(default_layer: bool = False, extended_layer_index: int = 0) -> None
unreal.GeometryScriptGroupLayer.default_layer(value: bool) -> None
unreal.GeometryScriptGroupLayer.extended_layer_index(value: int) -> None
```

## `unreal.GeometryScriptIndexList(StructBase)`

```python
unreal.GeometryScriptIndexList.__init__(index_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY) -> None
unreal.GeometryScriptIndexList.clear_index_list(clear_value: int = 0) -> None
unreal.GeometryScriptIndexList.convert_index_list_to_array() -> Array[int]
unreal.GeometryScriptIndexList.duplicate_index_list() -> GeometryScriptIndexList
unreal.GeometryScriptIndexList.get_index_list_item(index: int) -> Tuple[int, bool]
unreal.GeometryScriptIndexList.get_index_list_last_index() -> int
unreal.GeometryScriptIndexList.get_index_list_length() -> int
unreal.GeometryScriptIndexList.index_type(value: GeometryScriptIndexType) -> None
unreal.GeometryScriptIndexList.set_index_list_item(index: int, new_value: int) -> bool
```

## `unreal.GeometryScriptIsSameMeshOptions(StructBase)`

```python
unreal.GeometryScriptIsSameMeshOptions.__init__(check_connectivity: bool = False, check_edge_i_ds: bool = False, check_normals: bool = False, check_colors: bool = False, check_u_vs: bool = False, check_groups: bool = False, check_attributes: bool = False, epsilon: float = 0.000000) -> None
unreal.GeometryScriptIsSameMeshOptions.check_attributes(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_colors(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_connectivity(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_edge_i_ds(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_groups(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_normals(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.check_u_vs(value: bool) -> None
unreal.GeometryScriptIsSameMeshOptions.epsilon(value: float) -> None
```

## `unreal.GeometryScriptIterativeMeshSmoothingOptions(StructBase)`

```python
unreal.GeometryScriptIterativeMeshSmoothingOptions.__init__(num_iterations: int = 0, alpha: float = 0.000000, empty_behavior: GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior.FULL_MESH_SELECTION) -> None
unreal.GeometryScriptIterativeMeshSmoothingOptions.alpha(value: float) -> None
unreal.GeometryScriptIterativeMeshSmoothingOptions.empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
unreal.GeometryScriptIterativeMeshSmoothingOptions.num_iterations(value: int) -> None
```

## `unreal.GeometryScriptLayoutUVsOptions(StructBase)`

```python
unreal.GeometryScriptLayoutUVsOptions.__init__(layout_type: GeometryScriptUVLayoutType = GeometryScriptUVLayoutType.TRANSFORM, texture_resolution: int = 0, scale: float = 0.000000, translation: Vector2D = [0.000000, 0.000000], preserve_scale: bool = False, preserve_rotation: bool = False, allow_flips: bool = False, enable_udim_layout: bool = False, udim_resolutions: Map[int, int] = {}) -> None
unreal.GeometryScriptLayoutUVsOptions.allow_flips(value: bool) -> None
unreal.GeometryScriptLayoutUVsOptions.enable_udim_layout(value: bool) -> None
unreal.GeometryScriptLayoutUVsOptions.layout_type(value: GeometryScriptUVLayoutType) -> None
unreal.GeometryScriptLayoutUVsOptions.preserve_rotation(value: bool) -> None
unreal.GeometryScriptLayoutUVsOptions.preserve_scale(value: bool) -> None
unreal.GeometryScriptLayoutUVsOptions.scale(value: float) -> None
unreal.GeometryScriptLayoutUVsOptions.texture_resolution(value: int) -> None
unreal.GeometryScriptLayoutUVsOptions.translation(value: Vector2D) -> None
unreal.GeometryScriptLayoutUVsOptions.udim_resolutions(value: Map[int, int]) -> None
```

## `unreal.GeometryScriptMathWarpOptions(StructBase)`

```python
unreal.GeometryScriptMathWarpOptions.__init__(magnitude: float = 0.000000, frequency: float = 0.000000, frequency_shift: float = 0.000000) -> None
unreal.GeometryScriptMathWarpOptions.frequency(value: float) -> None
unreal.GeometryScriptMathWarpOptions.frequency_shift(value: float) -> None
unreal.GeometryScriptMathWarpOptions.magnitude(value: float) -> None
```

## `unreal.GeometryScriptMeasureMeshDistanceOptions(StructBase)`

```python
unreal.GeometryScriptMeasureMeshDistanceOptions.__init__(symmetric: bool = False) -> None
unreal.GeometryScriptMeasureMeshDistanceOptions.symmetric(value: bool) -> None
```

## `unreal.GeometryScriptMeshBevelOptions(StructBase)`

```python
unreal.GeometryScriptMeshBevelOptions.__init__(bevel_distance: float = 0.000000, infer_material_id: bool = False, set_material_id: int = 0, subdivisions: int = 0, round_weight: float = 0.000000, apply_filter_box: bool = False, filter_box: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], filter_box_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], fully_contained: bool = False) -> None
unreal.GeometryScriptMeshBevelOptions.apply_filter_box(value: bool) -> None
unreal.GeometryScriptMeshBevelOptions.bevel_distance(value: float) -> None
unreal.GeometryScriptMeshBevelOptions.filter_box(value: Box) -> None
unreal.GeometryScriptMeshBevelOptions.filter_box_transform(value: Transform) -> None
unreal.GeometryScriptMeshBevelOptions.fully_contained(value: bool) -> None
unreal.GeometryScriptMeshBevelOptions.infer_material_id(value: bool) -> None
unreal.GeometryScriptMeshBevelOptions.round_weight(value: float) -> None
unreal.GeometryScriptMeshBevelOptions.set_material_id(value: int) -> None
unreal.GeometryScriptMeshBevelOptions.subdivisions(value: int) -> None
```

## `unreal.GeometryScriptMeshBevelSelectionOptions(StructBase)`

```python
unreal.GeometryScriptMeshBevelSelectionOptions.__init__(bevel_distance: float = 0.000000, infer_material_id: bool = False, set_material_id: int = 0, subdivisions: int = 0, round_weight: float = 0.000000) -> None
unreal.GeometryScriptMeshBevelSelectionOptions.bevel_distance(value: float) -> None
unreal.GeometryScriptMeshBevelSelectionOptions.infer_material_id(value: bool) -> None
unreal.GeometryScriptMeshBevelSelectionOptions.round_weight(value: float) -> None
unreal.GeometryScriptMeshBevelSelectionOptions.set_material_id(value: int) -> None
unreal.GeometryScriptMeshBevelSelectionOptions.subdivisions(value: int) -> None
```

## `unreal.GeometryScriptMeshBooleanOptions(StructBase)`

```python
unreal.GeometryScriptMeshBooleanOptions.__init__(fill_holes: bool = False, simplify_output: bool = False, simplify_planar_tolerance: float = 0.000000, allow_empty_result: bool = False) -> None
unreal.GeometryScriptMeshBooleanOptions.allow_empty_result(value: bool) -> None
unreal.GeometryScriptMeshBooleanOptions.fill_holes(value: bool) -> None
unreal.GeometryScriptMeshBooleanOptions.simplify_output(value: bool) -> None
unreal.GeometryScriptMeshBooleanOptions.simplify_planar_tolerance(value: float) -> None
```

## `unreal.GeometryScriptMeshDifferenceInfo(StructBase)`

```python
unreal.GeometryScriptMeshDifferenceInfo.__init__(reason: GeometryScriptMeshDifferenceReason = GeometryScriptMeshDifferenceReason.UNKNOWN, detail: str = "", target_mesh_element_id: int = 0, other_mesh_element_id: int = 0, element_id_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY) -> None
unreal.GeometryScriptMeshDifferenceInfo.detail(value: str) -> None
unreal.GeometryScriptMeshDifferenceInfo.element_id_type(value: GeometryScriptIndexType) -> None
unreal.GeometryScriptMeshDifferenceInfo.other_mesh_element_id(value: int) -> None
unreal.GeometryScriptMeshDifferenceInfo.reason(value: GeometryScriptMeshDifferenceReason) -> None
unreal.GeometryScriptMeshDifferenceInfo.target_mesh_element_id(value: int) -> None
```

## `unreal.GeometryScriptMeshEditPolygroupOptions(StructBase)`

```python
unreal.GeometryScriptMeshEditPolygroupOptions.__init__(group_mode: GeometryScriptMeshEditPolygroupMode = GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, constant_group: int = 0) -> None
unreal.GeometryScriptMeshEditPolygroupOptions.constant_group(value: int) -> None
unreal.GeometryScriptMeshEditPolygroupOptions.group_mode(value: GeometryScriptMeshEditPolygroupMode) -> None
```

## `unreal.GeometryScriptMeshExtrudeOptions(StructBase)`

```python
unreal.GeometryScriptMeshExtrudeOptions.__init__(extrude_distance: float = 0.000000, extrude_direction: Vector = [0.000000, 0.000000, 0.000000], uv_scale: float = 0.000000, solids_to_shells: bool = False) -> None
unreal.GeometryScriptMeshExtrudeOptions.extrude_direction(value: Vector) -> None
unreal.GeometryScriptMeshExtrudeOptions.extrude_distance(value: float) -> None
unreal.GeometryScriptMeshExtrudeOptions.solids_to_shells(value: bool) -> None
unreal.GeometryScriptMeshExtrudeOptions.uv_scale(value: float) -> None
```

## `unreal.GeometryScriptMeshInsetOutsetFacesOptions(StructBase)`

```python
unreal.GeometryScriptMeshInsetOutsetFacesOptions.__init__(distance: float = 0.000000, reproject: bool = False, boundary_only: bool = False, softness: float = 0.000000, area_scale: float = 0.000000, area_mode: GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.ENTIRE_SELECTION, group_options: GeometryScriptMeshEditPolygroupOptions = [GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], uv_scale: float = 0.000000) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_mode(value: GeometryScriptPolyOperationArea) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_scale(value: float) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.boundary_only(value: bool) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.distance(value: float) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.reproject(value: bool) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.softness(value: float) -> None
unreal.GeometryScriptMeshInsetOutsetFacesOptions.uv_scale(value: float) -> None
```

## `unreal.GeometryScriptMeshLinearExtrudeOptions(StructBase)`

```python
unreal.GeometryScriptMeshLinearExtrudeOptions.__init__(distance: float = 0.000000, direction_mode: GeometryScriptLinearExtrudeDirection = GeometryScriptLinearExtrudeDirection.FIXED_DIRECTION, direction: Vector = [0.000000, 0.000000, 0.000000], area_mode: GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.ENTIRE_SELECTION, group_options: GeometryScriptMeshEditPolygroupOptions = [GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], uv_scale: float = 0.000000, solids_to_shells: bool = False) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.area_mode(value: GeometryScriptPolyOperationArea) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.direction(value: Vector) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.direction_mode(value: GeometryScriptLinearExtrudeDirection) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.distance(value: float) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.solids_to_shells(value: bool) -> None
unreal.GeometryScriptMeshLinearExtrudeOptions.uv_scale(value: float) -> None
```

## `unreal.GeometryScriptMeshMirrorOptions(StructBase)`

```python
unreal.GeometryScriptMeshMirrorOptions.__init__(apply_plane_cut: bool = False, flip_cut_side: bool = False, weld_along_plane: bool = False) -> None
unreal.GeometryScriptMeshMirrorOptions.apply_plane_cut(value: bool) -> None
unreal.GeometryScriptMeshMirrorOptions.flip_cut_side(value: bool) -> None
unreal.GeometryScriptMeshMirrorOptions.weld_along_plane(value: bool) -> None
```

## `unreal.GeometryScriptMeshOffsetFacesOptions(StructBase)`

```python
unreal.GeometryScriptMeshOffsetFacesOptions.__init__(distance: float = 0.000000, offset_type: GeometryScriptOffsetFacesType = GeometryScriptOffsetFacesType.VERTEX_NORMAL, area_mode: GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.ENTIRE_SELECTION, group_options: GeometryScriptMeshEditPolygroupOptions = [GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], uv_scale: float = 0.000000, solids_to_shells: bool = False) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.area_mode(value: GeometryScriptPolyOperationArea) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.distance(value: float) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.offset_type(value: GeometryScriptOffsetFacesType) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.solids_to_shells(value: bool) -> None
unreal.GeometryScriptMeshOffsetFacesOptions.uv_scale(value: float) -> None
```

## `unreal.GeometryScriptMeshOffsetOptions(StructBase)`

```python
unreal.GeometryScriptMeshOffsetOptions.__init__(offset_distance: float = 0.000000, fixed_boundary: bool = False, solve_steps: int = 0, smooth_alpha: float = 0.000000, reproject_during_smoothing: bool = False, boundary_alpha: float = 0.000000) -> None
unreal.GeometryScriptMeshOffsetOptions.boundary_alpha(value: float) -> None
unreal.GeometryScriptMeshOffsetOptions.fixed_boundary(value: bool) -> None
unreal.GeometryScriptMeshOffsetOptions.offset_distance(value: float) -> None
unreal.GeometryScriptMeshOffsetOptions.reproject_during_smoothing(value: bool) -> None
unreal.GeometryScriptMeshOffsetOptions.smooth_alpha(value: float) -> None
unreal.GeometryScriptMeshOffsetOptions.solve_steps(value: int) -> None
```

## `unreal.GeometryScriptMeshPlaneCutOptions(StructBase)`

```python
unreal.GeometryScriptMeshPlaneCutOptions.__init__(fill_holes: bool = False, hole_fill_material_id: int = 0, fill_spans: bool = False, flip_cut_side: bool = False, uv_world_dimension: float = 0.000000) -> None
unreal.GeometryScriptMeshPlaneCutOptions.fill_holes(value: bool) -> None
unreal.GeometryScriptMeshPlaneCutOptions.fill_spans(value: bool) -> None
unreal.GeometryScriptMeshPlaneCutOptions.flip_cut_side(value: bool) -> None
unreal.GeometryScriptMeshPlaneCutOptions.hole_fill_material_id(value: int) -> None
unreal.GeometryScriptMeshPlaneCutOptions.uv_world_dimension(value: float) -> None
```

## `unreal.GeometryScriptMeshPlaneSliceOptions(StructBase)`

```python
unreal.GeometryScriptMeshPlaneSliceOptions.__init__(fill_holes: bool = False, hole_fill_material_id: int = 0, fill_spans: bool = False, gap_width: float = 0.000000, uv_world_dimension: float = 0.000000) -> None
unreal.GeometryScriptMeshPlaneSliceOptions.fill_holes(value: bool) -> None
unreal.GeometryScriptMeshPlaneSliceOptions.fill_spans(value: bool) -> None
unreal.GeometryScriptMeshPlaneSliceOptions.gap_width(value: float) -> None
unreal.GeometryScriptMeshPlaneSliceOptions.hole_fill_material_id(value: int) -> None
unreal.GeometryScriptMeshPlaneSliceOptions.uv_world_dimension(value: float) -> None
```

## `unreal.GeometryScriptMeshPointSamplingOptions(StructBase)`

```python
unreal.GeometryScriptMeshPointSamplingOptions.__init__(sampling_radius: float = 0.000000, max_num_samples: int = 0, random_seed: int = 0, sub_sample_density: float = 0.000000) -> None
unreal.GeometryScriptMeshPointSamplingOptions.max_num_samples(value: int) -> None
unreal.GeometryScriptMeshPointSamplingOptions.random_seed(value: int) -> None
unreal.GeometryScriptMeshPointSamplingOptions.sampling_radius(value: float) -> None
unreal.GeometryScriptMeshPointSamplingOptions.sub_sample_density(value: float) -> None
```

## `unreal.GeometryScriptMeshReadLOD(StructBase)`

```python
unreal.GeometryScriptMeshReadLOD.__init__(lod_type: GeometryScriptLODType = GeometryScriptLODType.MAX_AVAILABLE, lod_index: int = 0) -> None
unreal.GeometryScriptMeshReadLOD.lod_index(value: int) -> None
unreal.GeometryScriptMeshReadLOD.lod_type(value: GeometryScriptLODType) -> None
```

## `unreal.GeometryScriptMeshSelection(StructBase)`

```python
unreal.GeometryScriptMeshSelection.__init__() -> None
unreal.GeometryScriptMeshSelection.combine_mesh_selections(selection_b: GeometryScriptMeshSelection, combine_mode: GeometryScriptCombineSelectionMode = GeometryScriptCombineSelectionMode.ADD) -> GeometryScriptMeshSelection
unreal.GeometryScriptMeshSelection.debug_print_mesh_selection(disable: bool = False) -> None
unreal.GeometryScriptMeshSelection.get_mesh_selection_info() -> Tuple[GeometryScriptMeshSelectionType, int]
```

## `unreal.GeometryScriptMeshSelfUnionOptions(StructBase)`

```python
unreal.GeometryScriptMeshSelfUnionOptions.__init__(fill_holes: bool = False, trim_flaps: bool = False, simplify_output: bool = False, simplify_planar_tolerance: float = 0.000000, winding_threshold: float = 0.000000) -> None
unreal.GeometryScriptMeshSelfUnionOptions.fill_holes(value: bool) -> None
unreal.GeometryScriptMeshSelfUnionOptions.simplify_output(value: bool) -> None
unreal.GeometryScriptMeshSelfUnionOptions.simplify_planar_tolerance(value: float) -> None
unreal.GeometryScriptMeshSelfUnionOptions.trim_flaps(value: bool) -> None
unreal.GeometryScriptMeshSelfUnionOptions.winding_threshold(value: float) -> None
```

## `unreal.GeometryScriptMeshWriteLOD(StructBase)`

```python
unreal.GeometryScriptMeshWriteLOD.__init__(write_hi_res_source: bool = False, lod_index: int = 0) -> None
unreal.GeometryScriptMeshWriteLOD.lod_index(value: int) -> None
unreal.GeometryScriptMeshWriteLOD.write_hi_res_source(value: bool) -> None
```

## `unreal.GeometryScriptMorphologyOptions(StructBase)`

```python
unreal.GeometryScriptMorphologyOptions.__init__(sdf_grid_parameters: GeometryScript3DGridParameters = [GeometryScriptGridSizingMethod.GRID_RESOLUTION, 0.500000, 64], use_separate_mesh_grid: bool = False, mesh_grid_parameters: GeometryScript3DGridParameters = [GeometryScriptGridSizingMethod.GRID_RESOLUTION, 0.500000, 64], operation: GeometryScriptMorphologicalOpType = GeometryScriptMorphologicalOpType.DILATE, distance: float = 0.000000) -> None
unreal.GeometryScriptMorphologyOptions.distance(value: float) -> None
unreal.GeometryScriptMorphologyOptions.mesh_grid_parameters(value: GeometryScript3DGridParameters) -> None
unreal.GeometryScriptMorphologyOptions.operation(value: GeometryScriptMorphologicalOpType) -> None
unreal.GeometryScriptMorphologyOptions.sdf_grid_parameters(value: GeometryScript3DGridParameters) -> None
unreal.GeometryScriptMorphologyOptions.use_separate_mesh_grid(value: bool) -> None
```

## `unreal.GeometryScriptNonUniformPointSamplingOptions(StructBase)`

```python
unreal.GeometryScriptNonUniformPointSamplingOptions.__init__(max_sampling_radius: float = 0.000000, size_distribution: GeometryScriptSamplingDistributionMode = GeometryScriptSamplingDistributionMode.UNIFORM, size_distribution_power: float = 0.000000, weight_mode: GeometryScriptSamplingWeightMode = GeometryScriptSamplingWeightMode.WEIGHT_TO_RADIUS, invert_weights: bool = False) -> None
unreal.GeometryScriptNonUniformPointSamplingOptions.invert_weights(value: bool) -> None
unreal.GeometryScriptNonUniformPointSamplingOptions.max_sampling_radius(value: float) -> None
unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution(value: GeometryScriptSamplingDistributionMode) -> None
unreal.GeometryScriptNonUniformPointSamplingOptions.size_distribution_power(value: float) -> None
unreal.GeometryScriptNonUniformPointSamplingOptions.weight_mode(value: GeometryScriptSamplingWeightMode) -> None
```

## `unreal.GeometryScriptOpenPathOffsetOptions(StructBase)`

```python
unreal.GeometryScriptOpenPathOffsetOptions.__init__(join_type: GeometryScriptPolyOffsetJoinType = GeometryScriptPolyOffsetJoinType.SQUARE, miter_limit: float = 0.000000, end_type: GeometryScriptPathOffsetEndType = GeometryScriptPathOffsetEndType.BUTT, steps_per_radian_scale: float = 0.000000, maximum_steps_per_radian: float = 0.000000) -> None
unreal.GeometryScriptOpenPathOffsetOptions.end_type(value: GeometryScriptPathOffsetEndType) -> None
unreal.GeometryScriptOpenPathOffsetOptions.join_type(value: GeometryScriptPolyOffsetJoinType) -> None
unreal.GeometryScriptOpenPathOffsetOptions.maximum_steps_per_radian(value: float) -> None
unreal.GeometryScriptOpenPathOffsetOptions.miter_limit(value: float) -> None
unreal.GeometryScriptOpenPathOffsetOptions.steps_per_radian_scale(value: float) -> None
```

## `unreal.GeometryScriptPNTessellateOptions(StructBase)`

```python
unreal.GeometryScriptPNTessellateOptions.__init__(recompute_normals: bool = False) -> None
unreal.GeometryScriptPNTessellateOptions.recompute_normals(value: bool) -> None
```

## `unreal.GeometryScriptPatchBuilderOptions(StructBase)`

```python
unreal.GeometryScriptPatchBuilderOptions.__init__(initial_patch_count: int = 0, min_patch_size: int = 0, patch_curvature_alignment_weight: float = 0.000000, patch_merging_metric_thresh: float = 0.000000, patch_merging_angle_thresh: float = 0.000000, exp_map_options: GeometryScriptExpMapUVOptions = [0, 0.250000], respect_input_groups: bool = False, group_layer: GeometryScriptGroupLayer = [True, 0], auto_pack: bool = False, packing_options: GeometryScriptRepackUVsOptions = [512, True]) -> None
unreal.GeometryScriptPatchBuilderOptions.auto_pack(value: bool) -> None
unreal.GeometryScriptPatchBuilderOptions.exp_map_options(value: GeometryScriptExpMapUVOptions) -> None
unreal.GeometryScriptPatchBuilderOptions.group_layer(value: GeometryScriptGroupLayer) -> None
unreal.GeometryScriptPatchBuilderOptions.initial_patch_count(value: int) -> None
unreal.GeometryScriptPatchBuilderOptions.min_patch_size(value: int) -> None
unreal.GeometryScriptPatchBuilderOptions.packing_options(value: GeometryScriptRepackUVsOptions) -> None
unreal.GeometryScriptPatchBuilderOptions.patch_curvature_alignment_weight(value: float) -> None
unreal.GeometryScriptPatchBuilderOptions.patch_merging_angle_thresh(value: float) -> None
unreal.GeometryScriptPatchBuilderOptions.patch_merging_metric_thresh(value: float) -> None
unreal.GeometryScriptPatchBuilderOptions.respect_input_groups(value: bool) -> None
```

## `unreal.GeometryScriptPerlinNoiseLayerOptions(StructBase)`

```python
unreal.GeometryScriptPerlinNoiseLayerOptions.__init__(magnitude: float = 0.000000, frequency: float = 0.000000, frequency_shift: Vector = [0.000000, 0.000000, 0.000000], random_seed: int = 0) -> None
unreal.GeometryScriptPerlinNoiseLayerOptions.frequency(value: float) -> None
unreal.GeometryScriptPerlinNoiseLayerOptions.frequency_shift(value: Vector) -> None
unreal.GeometryScriptPerlinNoiseLayerOptions.magnitude(value: float) -> None
unreal.GeometryScriptPerlinNoiseLayerOptions.random_seed(value: int) -> None
```

## `unreal.GeometryScriptPerlinNoiseOptions(StructBase)`

```python
unreal.GeometryScriptPerlinNoiseOptions.__init__(base_layer: GeometryScriptPerlinNoiseLayerOptions = [5.000000, 0.250000, [0.000000, 0.000000, 0.000000], 0], apply_along_normal: bool = False, empty_behavior: GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior.FULL_MESH_SELECTION) -> None
unreal.GeometryScriptPerlinNoiseOptions.apply_along_normal(value: bool) -> None
unreal.GeometryScriptPerlinNoiseOptions.base_layer(value: GeometryScriptPerlinNoiseLayerOptions) -> None
unreal.GeometryScriptPerlinNoiseOptions.empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
```

## `unreal.GeometryScriptPlanarSimplifyOptions(StructBase)`

```python
unreal.GeometryScriptPlanarSimplifyOptions.__init__(angle_threshold: float = 0.000000, auto_compact: bool = False) -> None
unreal.GeometryScriptPlanarSimplifyOptions.angle_threshold(value: float) -> None
unreal.GeometryScriptPlanarSimplifyOptions.auto_compact(value: bool) -> None
```

## `unreal.GeometryScriptPointClusteringOptions(StructBase)`

```python
unreal.GeometryScriptPointClusteringOptions.__init__(initial_cluster_centers: Array[Vector] = [], target_num_clusters: int = 0, initialize_method: GeometryScriptInitKMeansMethod = GeometryScriptInitKMeansMethod.RANDOM, random_seed: int = 0, max_iterations: int = 0) -> None
unreal.GeometryScriptPointClusteringOptions.initial_cluster_centers(value: Array[Vector]) -> None
unreal.GeometryScriptPointClusteringOptions.initialize_method(value: GeometryScriptInitKMeansMethod) -> None
unreal.GeometryScriptPointClusteringOptions.max_iterations(value: int) -> None
unreal.GeometryScriptPointClusteringOptions.random_seed(value: int) -> None
unreal.GeometryScriptPointClusteringOptions.target_num_clusters(value: int) -> None
```

## `unreal.GeometryScriptPointFlatteningOptions(StructBase)`

```python
unreal.GeometryScriptPointFlatteningOptions.__init__(frame: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], drop_axis: GeometryScriptAxis = GeometryScriptAxis.X) -> None
unreal.GeometryScriptPointFlatteningOptions.drop_axis(value: GeometryScriptAxis) -> None
unreal.GeometryScriptPointFlatteningOptions.frame(value: Transform) -> None
```

## `unreal.GeometryScriptPointPriorityOptions(StructBase)`

```python
unreal.GeometryScriptPointPriorityOptions.__init__(optional_priority_weights: Array[float] = [], uniform_spacing: bool = False) -> None
unreal.GeometryScriptPointPriorityOptions.optional_priority_weights(value: Array[float]) -> None
unreal.GeometryScriptPointPriorityOptions.uniform_spacing(value: bool) -> None
```

## `unreal.GeometryScriptPolyPath(StructBase)`

```python
unreal.GeometryScriptPolyPath.__init__() -> None
unreal.GeometryScriptPolyPath.convert_poly_path_to_array() -> Array[Vector]
unreal.GeometryScriptPolyPath.convert_poly_path_to_array_of_vector2d() -> Array[Vector2D]
unreal.GeometryScriptPolyPath.flatten_to2d_on_axis(drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z) -> GeometryScriptPolyPath
unreal.GeometryScriptPolyPath.get_nearest_vertex_index(point: Vector) -> int
unreal.GeometryScriptPolyPath.get_poly_path_arc_length() -> float
unreal.GeometryScriptPolyPath.get_poly_path_last_index() -> int
unreal.GeometryScriptPolyPath.get_poly_path_num_vertices() -> int
unreal.GeometryScriptPolyPath.get_poly_path_tangent(index: int) -> Tuple[Vector, bool]
unreal.GeometryScriptPolyPath.get_poly_path_vertex(index: int) -> Tuple[Vector, bool]
```

## `unreal.GeometryScriptPolygonOffsetOptions(StructBase)`

```python
unreal.GeometryScriptPolygonOffsetOptions.__init__(join_type: GeometryScriptPolyOffsetJoinType = GeometryScriptPolyOffsetJoinType.SQUARE, miter_limit: float = 0.000000, offset_both_sides: bool = False, steps_per_radian_scale: float = 0.000000, maximum_steps_per_radian: float = 0.000000) -> None
unreal.GeometryScriptPolygonOffsetOptions.join_type(value: GeometryScriptPolyOffsetJoinType) -> None
unreal.GeometryScriptPolygonOffsetOptions.maximum_steps_per_radian(value: float) -> None
unreal.GeometryScriptPolygonOffsetOptions.miter_limit(value: float) -> None
unreal.GeometryScriptPolygonOffsetOptions.offset_both_sides(value: bool) -> None
unreal.GeometryScriptPolygonOffsetOptions.steps_per_radian_scale(value: float) -> None
```

## `unreal.GeometryScriptPolygonsTriangulationOptions(StructBase)`

```python
unreal.GeometryScriptPolygonsTriangulationOptions.__init__(still_append_on_triangulation_error: bool = False) -> None
unreal.GeometryScriptPolygonsTriangulationOptions.still_append_on_triangulation_error(value: bool) -> None
```

## `unreal.GeometryScriptPolygroupSimplifyOptions(StructBase)`

```python
unreal.GeometryScriptPolygroupSimplifyOptions.__init__(angle_threshold: float = 0.000000, auto_compact: bool = False) -> None
unreal.GeometryScriptPolygroupSimplifyOptions.angle_threshold(value: float) -> None
unreal.GeometryScriptPolygroupSimplifyOptions.auto_compact(value: bool) -> None
```

## `unreal.GeometryScriptPrimitiveOptions(StructBase)`

```python
unreal.GeometryScriptPrimitiveOptions.__init__(polygroup_mode: GeometryScriptPrimitivePolygroupMode = GeometryScriptPrimitivePolygroupMode.SINGLE_GROUP, flip_orientation: bool = False, uv_mode: GeometryScriptPrimitiveUVMode = GeometryScriptPrimitiveUVMode.UNIFORM, material_id: int = 0) -> None
unreal.GeometryScriptPrimitiveOptions.flip_orientation(value: bool) -> None
unreal.GeometryScriptPrimitiveOptions.material_id(value: int) -> None
unreal.GeometryScriptPrimitiveOptions.polygroup_mode(value: GeometryScriptPrimitivePolygroupMode) -> None
unreal.GeometryScriptPrimitiveOptions.uv_mode(value: GeometryScriptPrimitiveUVMode) -> None
```

## `unreal.GeometryScriptRayHitResult(StructBase)`

```python
unreal.GeometryScriptRayHitResult.__init__(hit: bool = False, ray_parameter: float = 0.000000, hit_triangle_id: int = 0, hit_position: Vector = [0.000000, 0.000000, 0.000000], hit_bary_coords: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptRayHitResult.hit(value: bool) -> None
unreal.GeometryScriptRayHitResult.hit_bary_coords(value: Vector) -> None
unreal.GeometryScriptRayHitResult.hit_position(value: Vector) -> None
unreal.GeometryScriptRayHitResult.hit_triangle_id(value: int) -> None
unreal.GeometryScriptRayHitResult.ray_parameter(value: float) -> None
```

## `unreal.GeometryScriptRecomputeUVsOptions(StructBase)`

```python
unreal.GeometryScriptRecomputeUVsOptions.__init__(method: GeometryScriptUVFlattenMethod = GeometryScriptUVFlattenMethod.EXP_MAP, island_source: GeometryScriptUVIslandSource = GeometryScriptUVIslandSource.POLY_GROUPS, exp_map_options: GeometryScriptExpMapUVOptions = [0, 0.250000], spectral_conformal_options: GeometryScriptSpectralConformalUVOptions = [True], group_layer: GeometryScriptGroupLayer = [True, 0], auto_align_islands_with_axes: bool = False) -> None
unreal.GeometryScriptRecomputeUVsOptions.auto_align_islands_with_axes(value: bool) -> None
unreal.GeometryScriptRecomputeUVsOptions.exp_map_options(value: GeometryScriptExpMapUVOptions) -> None
unreal.GeometryScriptRecomputeUVsOptions.group_layer(value: GeometryScriptGroupLayer) -> None
unreal.GeometryScriptRecomputeUVsOptions.island_source(value: GeometryScriptUVIslandSource) -> None
unreal.GeometryScriptRecomputeUVsOptions.method(value: GeometryScriptUVFlattenMethod) -> None
unreal.GeometryScriptRecomputeUVsOptions.spectral_conformal_options(value: GeometryScriptSpectralConformalUVOptions) -> None
```

## `unreal.GeometryScriptRemeshOptions(StructBase)`

```python
unreal.GeometryScriptRemeshOptions.__init__(discard_attributes: bool = False, reproject_to_input_mesh: bool = False, smoothing_type: GeometryScriptRemeshSmoothingType = GeometryScriptRemeshSmoothingType.UNIFORM, smoothing_rate: float = 0.000000, mesh_boundary_constraint: GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType.FIXED, group_boundary_constraint: GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType.FIXED, material_boundary_constraint: GeometryScriptRemeshEdgeConstraintType = GeometryScriptRemeshEdgeConstraintType.FIXED, allow_flips: bool = False, allow_splits: bool = False, allow_collapses: bool = False, prevent_normal_flips: bool = False, prevent_tiny_triangles: bool = False, use_full_remesh_passes: bool = False, remesh_iterations: int = 0, auto_compact: bool = False) -> None
unreal.GeometryScriptRemeshOptions.allow_collapses(value: bool) -> None
unreal.GeometryScriptRemeshOptions.allow_flips(value: bool) -> None
unreal.GeometryScriptRemeshOptions.allow_splits(value: bool) -> None
unreal.GeometryScriptRemeshOptions.auto_compact(value: bool) -> None
unreal.GeometryScriptRemeshOptions.discard_attributes(value: bool) -> None
unreal.GeometryScriptRemeshOptions.group_boundary_constraint(value: GeometryScriptRemeshEdgeConstraintType) -> None
unreal.GeometryScriptRemeshOptions.material_boundary_constraint(value: GeometryScriptRemeshEdgeConstraintType) -> None
unreal.GeometryScriptRemeshOptions.mesh_boundary_constraint(value: GeometryScriptRemeshEdgeConstraintType) -> None
unreal.GeometryScriptRemeshOptions.prevent_normal_flips(value: bool) -> None
unreal.GeometryScriptRemeshOptions.prevent_tiny_triangles(value: bool) -> None
unreal.GeometryScriptRemeshOptions.remesh_iterations(value: int) -> None
unreal.GeometryScriptRemeshOptions.reproject_to_input_mesh(value: bool) -> None
unreal.GeometryScriptRemeshOptions.smoothing_rate(value: float) -> None
unreal.GeometryScriptRemeshOptions.smoothing_type(value: GeometryScriptRemeshSmoothingType) -> None
unreal.GeometryScriptRemeshOptions.use_full_remesh_passes(value: bool) -> None
```

## `unreal.GeometryScriptRemoveHiddenTrianglesOptions(StructBase)`

```python
unreal.GeometryScriptRemoveHiddenTrianglesOptions.__init__(method: GeometryScriptRemoveHiddenTrianglesMethod = GeometryScriptRemoveHiddenTrianglesMethod.FAST_WINDING_NUMBER, samples_per_triangle: int = 0, shrink_selection: int = 0, winding_iso_value: float = 0.000000, rays_per_sample: int = 0, normal_offset: float = 0.000000, compact_result: bool = False) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.compact_result(value: bool) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.method(value: GeometryScriptRemoveHiddenTrianglesMethod) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.normal_offset(value: float) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.rays_per_sample(value: int) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.samples_per_triangle(value: int) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.shrink_selection(value: int) -> None
unreal.GeometryScriptRemoveHiddenTrianglesOptions.winding_iso_value(value: float) -> None
```

## `unreal.GeometryScriptRemoveSmallComponentOptions(StructBase)`

```python
unreal.GeometryScriptRemoveSmallComponentOptions.__init__(min_volume: float = 0.000000, min_area: float = 0.000000, min_triangle_count: int = 0) -> None
unreal.GeometryScriptRemoveSmallComponentOptions.min_area(value: float) -> None
unreal.GeometryScriptRemoveSmallComponentOptions.min_triangle_count(value: int) -> None
unreal.GeometryScriptRemoveSmallComponentOptions.min_volume(value: float) -> None
```

## `unreal.GeometryScriptRepackUVsOptions(StructBase)`

```python
unreal.GeometryScriptRepackUVsOptions.__init__(target_image_width: int = 0, optimize_island_rotation: bool = False) -> None
unreal.GeometryScriptRepackUVsOptions.optimize_island_rotation(value: bool) -> None
unreal.GeometryScriptRepackUVsOptions.target_image_width(value: int) -> None
```

## `unreal.GeometryScriptResolveTJunctionOptions(StructBase)`

```python
unreal.GeometryScriptResolveTJunctionOptions.__init__(tolerance: float = 0.000000) -> None
unreal.GeometryScriptResolveTJunctionOptions.tolerance(value: float) -> None
```

## `unreal.GeometryScriptRevolveOptions(StructBase)`

```python
unreal.GeometryScriptRevolveOptions.__init__(revolve_degrees: float = 0.000000, degree_offset: float = 0.000000, reverse_direction: bool = False, hard_normals: bool = False, hard_normal_angle: float = 0.000000, profile_at_midpoint: bool = False, fill_partial_revolve_endcaps: bool = False) -> None
unreal.GeometryScriptRevolveOptions.degree_offset(value: float) -> None
unreal.GeometryScriptRevolveOptions.fill_partial_revolve_endcaps(value: bool) -> None
unreal.GeometryScriptRevolveOptions.hard_normal_angle(value: float) -> None
unreal.GeometryScriptRevolveOptions.hard_normals(value: bool) -> None
unreal.GeometryScriptRevolveOptions.profile_at_midpoint(value: bool) -> None
unreal.GeometryScriptRevolveOptions.reverse_direction(value: bool) -> None
unreal.GeometryScriptRevolveOptions.revolve_degrees(value: float) -> None
```

## `unreal.GeometryScriptScalarList(StructBase)`

```python
unreal.GeometryScriptScalarList.__init__() -> None
unreal.GeometryScriptScalarList.clear_scalar_list(clear_value: float = 0.000000) -> None
unreal.GeometryScriptScalarList.convert_scalar_list_to_array() -> Array[float]
unreal.GeometryScriptScalarList.duplicate_scalar_list() -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.get_scalar_list_item(index: int) -> Tuple[float, bool]
unreal.GeometryScriptScalarList.get_scalar_list_last_index() -> int
unreal.GeometryScriptScalarList.get_scalar_list_length() -> int
unreal.GeometryScriptScalarList.scalar_blend(scalar_list_b: GeometryScriptScalarList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.scalar_blend_in_place(scalar_list_b: GeometryScriptScalarList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.scalar_invert(numerator: float = 1.000000, set_on_failure: float = 0.000000, epsilon: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.scalar_invert_in_place(numerator: float = 1.000000, set_on_failure: float = 0.000000, epsilon: float = 0.000000) -> None
unreal.GeometryScriptScalarList.scalar_multiply(scalar_list_b: GeometryScriptScalarList, constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.scalar_multiply_in_place(scalar_list_b: GeometryScriptScalarList, constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScriptScalarList.scalar_vector_multiply(vector_list: GeometryScriptVectorList, scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScriptScalarList.scalar_vector_multiply_in_place(vector_list: GeometryScriptVectorList, scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScriptScalarList.set_scalar_list_item(index: int, new_value: float) -> bool
```

## `unreal.GeometryScriptSelectiveTessellateOptions(StructBase)`

```python
unreal.GeometryScriptSelectiveTessellateOptions.__init__(enable_multithreading: bool = False, empty_behavior: GeometryScriptEmptySelectionBehavior = GeometryScriptEmptySelectionBehavior.FULL_MESH_SELECTION) -> None
unreal.GeometryScriptSelectiveTessellateOptions.empty_behavior(value: GeometryScriptEmptySelectionBehavior) -> None
unreal.GeometryScriptSelectiveTessellateOptions.enable_multithreading(value: bool) -> None
```

## `unreal.GeometryScriptSimpleMeshBuffers(StructBase)`

```python
unreal.GeometryScriptSimpleMeshBuffers.__init__(vertices: Array[Vector] = [], normals: Array[Vector] = [], uv0: Array[Vector2D] = [], uv1: Array[Vector2D] = [], uv2: Array[Vector2D] = [], uv3: Array[Vector2D] = [], uv4: Array[Vector2D] = [], uv5: Array[Vector2D] = [], uv6: Array[Vector2D] = [], uv7: Array[Vector2D] = [], vertex_colors: Array[LinearColor] = [], triangles: Array[IntVector] = [], tri_group_i_ds: Array[int] = []) -> None
unreal.GeometryScriptSimpleMeshBuffers.normals(value: Array[Vector]) -> None
unreal.GeometryScriptSimpleMeshBuffers.tri_group_i_ds(value: Array[int]) -> None
unreal.GeometryScriptSimpleMeshBuffers.triangles(value: Array[IntVector]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv0(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv1(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv2(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv3(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv4(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv5(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv6(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.uv7(value: Array[Vector2D]) -> None
unreal.GeometryScriptSimpleMeshBuffers.vertex_colors(value: Array[LinearColor]) -> None
unreal.GeometryScriptSimpleMeshBuffers.vertices(value: Array[Vector]) -> None
```

## `unreal.GeometryScriptSimplePolygon(StructBase)`

```python
unreal.GeometryScriptSimplePolygon.__init__() -> None
unreal.GeometryScriptSimplePolygon.add_polygon_vertex(position: Vector2D) -> int
unreal.GeometryScriptSimplePolygon.create_polygon_list_from_single_polygon(hole_polygons: Array[GeometryScriptSimplePolygon], fix_hole_orientations: bool = True) -> GeometryScriptGeneralPolygonList
unreal.GeometryScriptSimplePolygon.get_polygon_arc_length() -> float
unreal.GeometryScriptSimplePolygon.get_polygon_area() -> float
unreal.GeometryScriptSimplePolygon.get_polygon_bounds() -> Box2D
unreal.GeometryScriptSimplePolygon.get_polygon_tangent(vertex_index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScriptSimplePolygon.get_polygon_vertex(vertex_index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScriptSimplePolygon.get_polygon_vertex_count() -> int
unreal.GeometryScriptSimplePolygon.set_polygon_vertex(vertex_index: int, position: Vector2D) -> bool
```

## `unreal.GeometryScriptSimplifyMeshOptions(StructBase)`

```python
unreal.GeometryScriptSimplifyMeshOptions.__init__(method: GeometryScriptRemoveMeshSimplificationType = GeometryScriptRemoveMeshSimplificationType.STANDARD_QEM, allow_seam_collapse: bool = False, allow_seam_smoothing: bool = False, allow_seam_splits: bool = False, preserve_vertex_positions: bool = False, retain_quadric_memory: bool = False, auto_compact: bool = False) -> None
unreal.GeometryScriptSimplifyMeshOptions.allow_seam_collapse(value: bool) -> None
unreal.GeometryScriptSimplifyMeshOptions.allow_seam_smoothing(value: bool) -> None
unreal.GeometryScriptSimplifyMeshOptions.allow_seam_splits(value: bool) -> None
unreal.GeometryScriptSimplifyMeshOptions.auto_compact(value: bool) -> None
unreal.GeometryScriptSimplifyMeshOptions.method(value: GeometryScriptRemoveMeshSimplificationType) -> None
unreal.GeometryScriptSimplifyMeshOptions.preserve_vertex_positions(value: bool) -> None
unreal.GeometryScriptSimplifyMeshOptions.retain_quadric_memory(value: bool) -> None
```

## `unreal.GeometryScriptSnapBoundariesOptions(StructBase)`

```python
unreal.GeometryScriptSnapBoundariesOptions.__init__(tolerance: float = 0.000000, snap_to_edges: bool = False, max_iterations: int = 0) -> None
unreal.GeometryScriptSnapBoundariesOptions.max_iterations(value: int) -> None
unreal.GeometryScriptSnapBoundariesOptions.snap_to_edges(value: bool) -> None
unreal.GeometryScriptSnapBoundariesOptions.tolerance(value: float) -> None
```

## `unreal.GeometryScriptSolidifyOptions(StructBase)`

```python
unreal.GeometryScriptSolidifyOptions.__init__(grid_parameters: GeometryScript3DGridParameters = [GeometryScriptGridSizingMethod.GRID_RESOLUTION, 0.500000, 64], winding_threshold: float = 0.000000, solid_at_boundaries: bool = False, extend_bounds: float = 0.000000, surface_search_steps: int = 0, thicken_shells: bool = False, shell_thickness: float = 0.000000) -> None
unreal.GeometryScriptSolidifyOptions.extend_bounds(value: float) -> None
unreal.GeometryScriptSolidifyOptions.grid_parameters(value: GeometryScript3DGridParameters) -> None
unreal.GeometryScriptSolidifyOptions.shell_thickness(value: float) -> None
unreal.GeometryScriptSolidifyOptions.solid_at_boundaries(value: bool) -> None
unreal.GeometryScriptSolidifyOptions.surface_search_steps(value: int) -> None
unreal.GeometryScriptSolidifyOptions.thicken_shells(value: bool) -> None
unreal.GeometryScriptSolidifyOptions.winding_threshold(value: float) -> None
```

## `unreal.GeometryScriptSpatialQueryOptions(StructBase)`

```python
unreal.GeometryScriptSpatialQueryOptions.__init__(max_distance: float = 0.000000, allow_unsafe_modified_queries: bool = False, winding_iso_threshold: float = 0.000000) -> None
unreal.GeometryScriptSpatialQueryOptions.allow_unsafe_modified_queries(value: bool) -> None
unreal.GeometryScriptSpatialQueryOptions.max_distance(value: float) -> None
unreal.GeometryScriptSpatialQueryOptions.winding_iso_threshold(value: float) -> None
```

## `unreal.GeometryScriptSpectralConformalUVOptions(StructBase)`

```python
unreal.GeometryScriptSpectralConformalUVOptions.__init__(preserve_irregularity: bool = False) -> None
unreal.GeometryScriptSpectralConformalUVOptions.preserve_irregularity(value: bool) -> None
```

## `unreal.GeometryScriptSphereCovering(StructBase)`

```python
unreal.GeometryScriptSphereCovering.__init__() -> None
```

## `unreal.GeometryScriptSplineSamplingOptions(StructBase)`

```python
unreal.GeometryScriptSplineSamplingOptions.__init__(num_samples: int = 0, error_tolerance: float = 0.000000, sample_spacing: GeometryScriptSampleSpacing = GeometryScriptSampleSpacing.UNIFORM_DISTANCE, coordinate_space: SplineCoordinateSpace = SplineCoordinateSpace.LOCAL, range_method: GeometryScriptEvaluateSplineRange = GeometryScriptEvaluateSplineRange.FULL_SPLINE, range_start: float = 0.000000, range_end: float = 0.000000) -> None
unreal.GeometryScriptSplineSamplingOptions.coordinate_space(value: SplineCoordinateSpace) -> None
unreal.GeometryScriptSplineSamplingOptions.error_tolerance(value: float) -> None
unreal.GeometryScriptSplineSamplingOptions.num_samples(value: int) -> None
unreal.GeometryScriptSplineSamplingOptions.range_end(value: float) -> None
unreal.GeometryScriptSplineSamplingOptions.range_method(value: GeometryScriptEvaluateSplineRange) -> None
unreal.GeometryScriptSplineSamplingOptions.range_start(value: float) -> None
unreal.GeometryScriptSplineSamplingOptions.sample_spacing(value: GeometryScriptSampleSpacing) -> None
```

## `unreal.GeometryScriptSplitNormalsOptions(StructBase)`

```python
unreal.GeometryScriptSplitNormalsOptions.__init__(split_by_opening_angle: bool = False, opening_angle_deg: float = 0.000000, split_by_face_group: bool = False, group_layer: GeometryScriptGroupLayer = [True, 0]) -> None
unreal.GeometryScriptSplitNormalsOptions.group_layer(value: GeometryScriptGroupLayer) -> None
unreal.GeometryScriptSplitNormalsOptions.opening_angle_deg(value: float) -> None
unreal.GeometryScriptSplitNormalsOptions.split_by_face_group(value: bool) -> None
unreal.GeometryScriptSplitNormalsOptions.split_by_opening_angle(value: bool) -> None
```

## `unreal.GeometryScriptSweptHullOptions(StructBase)`

```python
unreal.GeometryScriptSweptHullOptions.__init__(prefilter_vertices: bool = False, prefilter_grid_resolution: int = 0, min_thickness: float = 0.000000, simplify: bool = False, min_edge_length: float = 0.000000, simplify_tolerance: float = 0.000000) -> None
unreal.GeometryScriptSweptHullOptions.min_edge_length(value: float) -> None
unreal.GeometryScriptSweptHullOptions.min_thickness(value: float) -> None
unreal.GeometryScriptSweptHullOptions.prefilter_grid_resolution(value: int) -> None
unreal.GeometryScriptSweptHullOptions.prefilter_vertices(value: bool) -> None
unreal.GeometryScriptSweptHullOptions.simplify(value: bool) -> None
unreal.GeometryScriptSweptHullOptions.simplify_tolerance(value: float) -> None
```

## `unreal.GeometryScriptTangentsOptions(StructBase)`

```python
unreal.GeometryScriptTangentsOptions.__init__(type: GeometryScriptTangentTypes = GeometryScriptTangentTypes.FAST_MIKK_T, uv_layer: int = 0) -> None
unreal.GeometryScriptTangentsOptions.type(value: GeometryScriptTangentTypes) -> None
unreal.GeometryScriptTangentsOptions.uv_layer(value: int) -> None
```

## `unreal.GeometryScriptTriangle(StructBase)`

```python
unreal.GeometryScriptTriangle.__init__(vector0: Vector = [0.000000, 0.000000, 0.000000], vector1: Vector = [0.000000, 0.000000, 0.000000], vector2: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptTriangle.vector0(value: Vector) -> None
unreal.GeometryScriptTriangle.vector1(value: Vector) -> None
unreal.GeometryScriptTriangle.vector2(value: Vector) -> None
```

## `unreal.GeometryScriptTriangleList(StructBase)`

```python
unreal.GeometryScriptTriangleList.__init__() -> None
unreal.GeometryScriptTriangleList.convert_triangle_list_to_array() -> Array[IntVector]
unreal.GeometryScriptTriangleList.get_triangle_list_item(triangle: int) -> Tuple[IntVector, bool]
unreal.GeometryScriptTriangleList.get_triangle_list_last_triangle() -> int
unreal.GeometryScriptTriangleList.get_triangle_list_length() -> int
```

## `unreal.GeometryScriptTrianglePoint(StructBase)`

```python
unreal.GeometryScriptTrianglePoint.__init__(valid: bool = False, triangle_id: int = 0, position: Vector = [0.000000, 0.000000, 0.000000], bary_coords: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptTrianglePoint.bary_coords(value: Vector) -> None
unreal.GeometryScriptTrianglePoint.position(value: Vector) -> None
unreal.GeometryScriptTrianglePoint.triangle_id(value: int) -> None
unreal.GeometryScriptTrianglePoint.valid(value: bool) -> None
```

## `unreal.GeometryScriptTwistWarpOptions(StructBase)`

```python
unreal.GeometryScriptTwistWarpOptions.__init__(symmetric_extents: bool = False, lower_extent: float = 0.000000, bidirectional: bool = False) -> None
unreal.GeometryScriptTwistWarpOptions.bidirectional(value: bool) -> None
unreal.GeometryScriptTwistWarpOptions.lower_extent(value: float) -> None
unreal.GeometryScriptTwistWarpOptions.symmetric_extents(value: bool) -> None
```

## `unreal.GeometryScriptUVList(StructBase)`

```python
unreal.GeometryScriptUVList.__init__() -> None
unreal.GeometryScriptUVList.clear_uv_list(clear_uv: Vector2D) -> None
unreal.GeometryScriptUVList.convert_uv_list_to_array() -> Array[Vector2D]
unreal.GeometryScriptUVList.duplicate_uv_list() -> GeometryScriptUVList
unreal.GeometryScriptUVList.get_uv_list_item(index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScriptUVList.get_uv_list_last_index() -> int
unreal.GeometryScriptUVList.get_uv_list_length() -> int
unreal.GeometryScriptUVList.set_uv_list_item(index: int, new_uv: Vector2D) -> bool
```

## `unreal.GeometryScriptUVTexelDensityOptions(StructBase)`

```python
unreal.GeometryScriptUVTexelDensityOptions.__init__(texel_density_mode: GeometryScriptTexelDensityMode = GeometryScriptTexelDensityMode.APPLY_TO_ISLANDS, target_world_units: float = 0.000000, target_pixel_count: float = 0.000000, texture_resolution: float = 0.000000, enable_udim_layout: bool = False, udim_resolutions: Map[int, int] = {}) -> None
unreal.GeometryScriptUVTexelDensityOptions.enable_udim_layout(value: bool) -> None
unreal.GeometryScriptUVTexelDensityOptions.target_pixel_count(value: float) -> None
unreal.GeometryScriptUVTexelDensityOptions.target_world_units(value: float) -> None
unreal.GeometryScriptUVTexelDensityOptions.texel_density_mode(value: GeometryScriptTexelDensityMode) -> None
unreal.GeometryScriptUVTexelDensityOptions.texture_resolution(value: float) -> None
unreal.GeometryScriptUVTexelDensityOptions.udim_resolutions(value: Map[int, int]) -> None
```

## `unreal.GeometryScriptUVTriangle(StructBase)`

```python
unreal.GeometryScriptUVTriangle.__init__(uv0: Vector2D = [0.000000, 0.000000], uv1: Vector2D = [0.000000, 0.000000], uv2: Vector2D = [0.000000, 0.000000]) -> None
unreal.GeometryScriptUVTriangle.uv0(value: Vector2D) -> None
unreal.GeometryScriptUVTriangle.uv1(value: Vector2D) -> None
unreal.GeometryScriptUVTriangle.uv2(value: Vector2D) -> None
```

## `unreal.GeometryScriptUniformRemeshOptions(StructBase)`

```python
unreal.GeometryScriptUniformRemeshOptions.__init__(target_type: GeometryScriptUniformRemeshTargetType = GeometryScriptUniformRemeshTargetType.TRIANGLE_COUNT, target_triangle_count: int = 0, target_edge_length: float = 0.000000) -> None
unreal.GeometryScriptUniformRemeshOptions.target_edge_length(value: float) -> None
unreal.GeometryScriptUniformRemeshOptions.target_triangle_count(value: int) -> None
unreal.GeometryScriptUniformRemeshOptions.target_type(value: GeometryScriptUniformRemeshTargetType) -> None
```

## `unreal.GeometryScriptUniqueAssetNameOptions(StructBase)`

```python
unreal.GeometryScriptUniqueAssetNameOptions.__init__(unique_id_digits: int = 0) -> None
unreal.GeometryScriptUniqueAssetNameOptions.unique_id_digits(value: int) -> None
```

## `unreal.GeometryScriptVectorList(StructBase)`

```python
unreal.GeometryScriptVectorList.__init__() -> None
unreal.GeometryScriptVectorList.clear_vector_list(clear_value: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptVectorList.convert_vector_list_to_array() -> Array[Vector]
unreal.GeometryScriptVectorList.duplicate_vector_list() -> GeometryScriptVectorList
unreal.GeometryScriptVectorList.get_vector_list_item(index: int) -> Tuple[Vector, bool]
unreal.GeometryScriptVectorList.get_vector_list_last_index() -> int
unreal.GeometryScriptVectorList.get_vector_list_length() -> int
unreal.GeometryScriptVectorList.set_vector_list_item(index: int, new_value: Vector) -> bool
unreal.GeometryScriptVectorList.vector_blend(vector_list_b: GeometryScriptVectorList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScriptVectorList.vector_blend_in_place(vector_list_b: GeometryScriptVectorList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScriptVectorList.vector_cross(vector_list_b: GeometryScriptVectorList) -> GeometryScriptVectorList
unreal.GeometryScriptVectorList.vector_dot(vector_list_b: GeometryScriptVectorList) -> GeometryScriptScalarList
unreal.GeometryScriptVectorList.vector_inverse_transform_in_place(transform: Transform, as_position: bool = True) -> None
unreal.GeometryScriptVectorList.vector_length() -> GeometryScriptScalarList
unreal.GeometryScriptVectorList.vector_normalize_in_place(set_on_failure: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.GeometryScriptVectorList.vector_plane_project_in_place(plane: Plane) -> None
unreal.GeometryScriptVectorList.vector_to_scalar(constant_x: float = 1.000000, constant_y: float = 0.000000, constant_z: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScriptVectorList.vector_transform_in_place(transform: Transform, as_position: bool = True) -> None
```

## `unreal.GeometryScriptVoronoiOptions(StructBase)`

```python
unreal.GeometryScriptVoronoiOptions.__init__(bounds_expand: float = 0.000000, bounds: Box = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], False], create_cells: Array[int] = [], include_boundary: bool = False) -> None
unreal.GeometryScriptVoronoiOptions.bounds(value: Box) -> None
unreal.GeometryScriptVoronoiOptions.bounds_expand(value: float) -> None
unreal.GeometryScriptVoronoiOptions.create_cells(value: Array[int]) -> None
unreal.GeometryScriptVoronoiOptions.include_boundary(value: bool) -> None
```

## `unreal.GeometryScriptWeldEdgesOptions(StructBase)`

```python
unreal.GeometryScriptWeldEdgesOptions.__init__(tolerance: float = 0.000000, only_unique_pairs: bool = False) -> None
unreal.GeometryScriptWeldEdgesOptions.only_unique_pairs(value: bool) -> None
unreal.GeometryScriptWeldEdgesOptions.tolerance(value: float) -> None
```

## `unreal.GeometryScriptXAtlasOptions(StructBase)`

```python
unreal.GeometryScriptXAtlasOptions.__init__(max_iterations: int = 0) -> None
unreal.GeometryScriptXAtlasOptions.max_iterations(value: int) -> None
```

## `unreal.GeometryScript_AssetUtils(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_AssetUtils.check_static_mesh_has_available_lod(static_mesh_asset: StaticMesh, requested_lod: GeometryScriptMeshReadLOD, debug: GeometryScriptDebug = None) -> Optional[GeometryScriptSearchOutcomePins]
unreal.GeometryScript_AssetUtils.convert_material_list_to_material_map(material_list: Array[MaterialInterface], material_slot_names: Array[Name]) -> Map[Name, MaterialInterface]
unreal.GeometryScript_AssetUtils.convert_material_map_to_material_list(material_map: Map[Name, MaterialInterface]) -> Tuple[Array[MaterialInterface], Array[Name]]
unreal.GeometryScript_AssetUtils.copy_mesh_from_skeletal_mesh(from_skeletal_mesh_asset: SkeletalMesh, to_dynamic_mesh: DynamicMesh, asset_options: GeometryScriptCopyMeshFromAssetOptions, requested_lod: GeometryScriptMeshReadLOD, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_mesh_from_static_mesh(from_static_mesh_asset: StaticMesh, to_dynamic_mesh: DynamicMesh, asset_options: GeometryScriptCopyMeshFromAssetOptions, requested_lod: GeometryScriptMeshReadLOD, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_mesh_from_static_mesh_v2(from_static_mesh_asset: StaticMesh, to_dynamic_mesh: DynamicMesh, asset_options: GeometryScriptCopyMeshFromAssetOptions, requested_lod: GeometryScriptMeshReadLOD, use_section_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_mesh_to_skeletal_mesh(from_dynamic_mesh: DynamicMesh, to_skeletal_mesh_asset: SkeletalMesh, options: GeometryScriptCopyMeshToAssetOptions, target_lod: GeometryScriptMeshWriteLOD, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_mesh_to_static_mesh(from_dynamic_mesh: DynamicMesh, to_static_mesh_asset: StaticMesh, options: GeometryScriptCopyMeshToAssetOptions, target_lod: GeometryScriptMeshWriteLOD, use_section_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_morph_target_to_skeletal_mesh(from_morph_target: DynamicMesh, to_skeletal_mesh_asset: SkeletalMesh, morph_target_name: Name, options: GeometryScriptCopyMorphTargetToAssetOptions, target_lod: GeometryScriptMeshWriteLOD, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.copy_skin_weight_profile_to_skeletal_mesh(from_dynamic_mesh: DynamicMesh, to_skeletal_mesh_asset: SkeletalMesh, target_profile_name: Name, source_profile_name: Name, options: GeometryScriptCopySkinWeightProfileToAssetOptions, target_lod: GeometryScriptMeshWriteLOD, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.get_lod_material_list_from_skeletal_mesh(from_skeletal_mesh_asset: SkeletalMesh, requested_lod: GeometryScriptMeshReadLOD, debug: GeometryScriptDebug = None) -> Tuple[Array[MaterialInterface], Array[int], Array[Name], GeometryScriptOutcomePins]
unreal.GeometryScript_AssetUtils.get_material_list_from_skeletal_mesh(from_skeletal_mesh_asset: SkeletalMesh, debug: GeometryScriptDebug = None) -> Tuple[Array[MaterialInterface], Array[Name]]
unreal.GeometryScript_AssetUtils.get_material_list_from_static_mesh(from_static_mesh_asset: StaticMesh, debug: GeometryScriptDebug = None) -> Tuple[Array[MaterialInterface], Array[Name]]
unreal.GeometryScript_AssetUtils.get_num_static_mesh_lo_ds_of_type(static_mesh_asset: StaticMesh, lod_type: GeometryScriptLODType = GeometryScriptLODType.SOURCE_MODEL) -> int
unreal.GeometryScript_AssetUtils.get_section_material_list_from_static_mesh(from_static_mesh_asset: StaticMesh, requested_lod: GeometryScriptMeshReadLOD, debug: GeometryScriptDebug = None) -> Tuple[Array[MaterialInterface], Array[int], Array[Name], GeometryScriptOutcomePins]
```

## `unreal.GeometryScript_Bake(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Bake.bake_texture(target_mesh: DynamicMesh, target_transform: Transform, target_options: GeometryScriptBakeTargetMeshOptions, source_mesh: DynamicMesh, source_transform: Transform, source_options: GeometryScriptBakeSourceMeshOptions, bake_types: Array[GeometryScriptBakeTypeOptions], bake_options: GeometryScriptBakeTextureOptions, debug: GeometryScriptDebug = None) -> Array[Texture2D]
unreal.GeometryScript_Bake.bake_texture_from_render_captures(target_mesh: DynamicMesh, target_local_to_world: Transform, target_options: GeometryScriptBakeTargetMeshOptions, source_actors: Array[Actor], bake_options: GeometryScriptBakeRenderCaptureOptions, debug: GeometryScriptDebug = None) -> GeometryScriptRenderCaptureTextures
unreal.GeometryScript_Bake.bake_vertex(target_mesh: DynamicMesh, target_transform: Transform, target_options: GeometryScriptBakeTargetMeshOptions, source_mesh: DynamicMesh, source_transform: Transform, source_options: GeometryScriptBakeSourceMeshOptions, bake_types: GeometryScriptBakeOutputType, bake_options: GeometryScriptBakeVertexOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Bake.convert_bake_resolution_to_int(bake_resolution: GeometryScriptBakeResolution) -> int
unreal.GeometryScript_Bake.make_bake_type_ambient_occlusion(occlusion_rays: int = 16, max_distance: float = 0.000000, spread_angle: float = 180.000000, bias_angle: float = 15.000000) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_bent_normal(occlusion_rays: int = 16, max_distance: float = 0.000000, spread_angle: float = 180.000000, normal_space: GeometryScriptBakeNormalSpace = GeometryScriptBakeNormalSpace.TANGENT) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_constant(value: float = 0.000000) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_curvature(curvature_type: GeometryScriptBakeCurvatureTypeMode = GeometryScriptBakeCurvatureTypeMode.MEAN, color_mapping: GeometryScriptBakeCurvatureColorMode = GeometryScriptBakeCurvatureColorMode.GRAYSCALE, color_range_multiplier: float = 1.000000, min_range_multiplier: float = 0.000000, clamping: GeometryScriptBakeCurvatureClampMode = GeometryScriptBakeCurvatureClampMode.NONE) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_face_normal() -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_material_id() -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_multi_texture(material_id_source_textures: Array[Texture2D], source_uv_layer: int = 0) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_object_normal() -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_position() -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_tangent_normal() -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_texture(source_texture: Texture2D = None, source_uv_layer: int = 0) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_uv_shell(source_uv_layer: int = 0, wireframe_thickness: float = 1.000000, wireframe_color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000], shell_color: LinearColor = [0.500000, 0.500000, 0.500000, 1.000000], background_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> GeometryScriptBakeTypeOptions
unreal.GeometryScript_Bake.make_bake_type_vertex_color() -> GeometryScriptBakeTypeOptions
```

## `unreal.GeometryScript_Box(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Box.find_box_box_intersection(box1: Box, box2: Box) -> Tuple[Box, bool]
unreal.GeometryScript_Box.find_closest_point_on_box(box: Box, point: Vector) -> Tuple[Vector, bool]
unreal.GeometryScript_Box.get_box_box_distance(box1: Box, box2: Box) -> float
unreal.GeometryScript_Box.get_box_center_size(box: Box) -> Tuple[Vector, Vector]
unreal.GeometryScript_Box.get_box_corner(box: Box, corner_index: int) -> Vector
unreal.GeometryScript_Box.get_box_face_center(box: Box, face_index: int) -> Tuple[Vector, Vector]
unreal.GeometryScript_Box.get_box_point_distance(box: Box, point: Vector) -> float
unreal.GeometryScript_Box.get_box_volume_area(box: Box) -> Tuple[float, float]
unreal.GeometryScript_Box.get_expanded_box(box: Box, expand_by: Vector) -> Box
unreal.GeometryScript_Box.get_transformed_box(box: Box, transform: Transform) -> Box
unreal.GeometryScript_Box.make_box_from_center_extents(center: Vector, extents: Vector) -> Box
unreal.GeometryScript_Box.make_box_from_center_size(center: Vector, dimensions: Vector) -> Box
unreal.GeometryScript_Box.test_box_box_intersection(box1: Box, box2: Box) -> bool
unreal.GeometryScript_Box.test_box_sphere_intersection(box: Box, sphere_center: Vector, sphere_radius: float) -> bool
unreal.GeometryScript_Box.test_point_inside_box(box: Box, point: Vector, consider_on_box_as_inside: bool = True) -> bool
```

## `unreal.GeometryScript_Containment(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Containment.compute_mesh_convex_decomposition(target_mesh: DynamicMesh, copy_to_mesh: DynamicMesh, options: GeometryScriptConvexDecompositionOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
unreal.GeometryScript_Containment.compute_mesh_convex_hull(target_mesh: DynamicMesh, copy_to_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, options: GeometryScriptConvexHullOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
unreal.GeometryScript_Containment.compute_mesh_swept_hull(target_mesh: DynamicMesh, copy_to_mesh: DynamicMesh, projection_frame: Transform, options: GeometryScriptSweptHullOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
```

## `unreal.GeometryScript_EditorDynamicMeshUtil(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_EditorDynamicMeshUtil.begin_tracked_mesh_change(target_mesh: DynamicMesh) -> Tuple[DynamicMesh, DynamicMeshChangeContainer]
unreal.GeometryScript_EditorDynamicMeshUtil.emit_tracked_mesh_change(target_mesh: DynamicMesh, change_tracker: DynamicMeshChangeContainer) -> Tuple[DynamicMesh, DynamicMeshChangeContainer]
unreal.GeometryScript_EditorDynamicMeshUtil.fetch_debug_mesh(debug_mesh_name: str, to_target_mesh: DynamicMesh, clear_debug_mesh: bool) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_EditorDynamicMeshUtil.stash_debug_mesh(target_mesh: DynamicMesh, debug_mesh_name: str) -> DynamicMesh
```

## `unreal.GeometryScript_List(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_List.clear_color_list(color_list: GeometryScriptColorList, clear_color: LinearColor) -> GeometryScriptColorList
unreal.GeometryScript_List.clear_index_list(index_list: GeometryScriptIndexList, clear_value: int = 0) -> GeometryScriptIndexList
unreal.GeometryScript_List.clear_scalar_list(scalar_list: GeometryScriptScalarList, clear_value: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScript_List.clear_uv_list(uv_list: GeometryScriptUVList, clear_uv: Vector2D) -> GeometryScriptUVList
unreal.GeometryScript_List.clear_vector_list(vector_list: GeometryScriptVectorList, clear_value: Vector = [0.000000, 0.000000, 0.000000]) -> GeometryScriptVectorList
unreal.GeometryScript_List.convert_array_to_color_list(color_array: Array[LinearColor]) -> GeometryScriptColorList
unreal.GeometryScript_List.convert_array_to_index_list(index_array: Array[int], index_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY) -> GeometryScriptIndexList
unreal.GeometryScript_List.convert_array_to_scalar_list(vector_array: Array[float]) -> GeometryScriptScalarList
unreal.GeometryScript_List.convert_array_to_triangle_list(triangle_array: Array[IntVector]) -> GeometryScriptTriangleList
unreal.GeometryScript_List.convert_array_to_uv_list(uv_array: Array[Vector2D]) -> GeometryScriptUVList
unreal.GeometryScript_List.convert_array_to_vector_list(vector_array: Array[Vector]) -> GeometryScriptVectorList
unreal.GeometryScript_List.convert_color_list_to_array(color_list: GeometryScriptColorList) -> Array[LinearColor]
unreal.GeometryScript_List.convert_index_list_to_array(index_list: GeometryScriptIndexList) -> Array[int]
unreal.GeometryScript_List.convert_scalar_list_to_array(scalar_list: GeometryScriptScalarList) -> Array[float]
unreal.GeometryScript_List.convert_triangle_list_to_array(triangle_list: GeometryScriptTriangleList) -> Array[IntVector]
unreal.GeometryScript_List.convert_uv_list_to_array(uv_list: GeometryScriptUVList) -> Array[Vector2D]
unreal.GeometryScript_List.convert_vector_list_to_array(vector_list: GeometryScriptVectorList) -> Array[Vector]
unreal.GeometryScript_List.duplicate_color_list(color_list: GeometryScriptColorList) -> GeometryScriptColorList
unreal.GeometryScript_List.duplicate_index_list(index_list: GeometryScriptIndexList) -> GeometryScriptIndexList
unreal.GeometryScript_List.duplicate_scalar_list(scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
unreal.GeometryScript_List.duplicate_uv_list(uv_list: GeometryScriptUVList) -> GeometryScriptUVList
unreal.GeometryScript_List.duplicate_vector_list(vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
unreal.GeometryScript_List.extract_color_list_channel(color_list: GeometryScriptColorList, channel_index: int = 0) -> GeometryScriptScalarList
unreal.GeometryScript_List.extract_color_list_channels(color_list: GeometryScriptColorList, x_channel_index: int = 0, y_channel_index: int = 1, z_channel_index: int = 2) -> GeometryScriptVectorList
unreal.GeometryScript_List.get_color_list_item(color_list: GeometryScriptColorList, index: int) -> Tuple[LinearColor, bool]
unreal.GeometryScript_List.get_color_list_last_index(color_list: GeometryScriptColorList) -> int
unreal.GeometryScript_List.get_color_list_length(color_list: GeometryScriptColorList) -> int
unreal.GeometryScript_List.get_index_list_item(index_list: GeometryScriptIndexList, index: int) -> Tuple[int, bool]
unreal.GeometryScript_List.get_index_list_last_index(index_list: GeometryScriptIndexList) -> int
unreal.GeometryScript_List.get_index_list_length(index_list: GeometryScriptIndexList) -> int
unreal.GeometryScript_List.get_scalar_list_item(scalar_list: GeometryScriptScalarList, index: int) -> Tuple[float, bool]
unreal.GeometryScript_List.get_scalar_list_last_index(scalar_list: GeometryScriptScalarList) -> int
unreal.GeometryScript_List.get_scalar_list_length(scalar_list: GeometryScriptScalarList) -> int
unreal.GeometryScript_List.get_triangle_list_item(triangle_list: GeometryScriptTriangleList, triangle: int) -> Tuple[IntVector, bool]
unreal.GeometryScript_List.get_triangle_list_last_triangle(triangle_list: GeometryScriptTriangleList) -> int
unreal.GeometryScript_List.get_triangle_list_length(triangle_list: GeometryScriptTriangleList) -> int
unreal.GeometryScript_List.get_uv_list_item(uv_list: GeometryScriptUVList, index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScript_List.get_uv_list_last_index(uv_list: GeometryScriptUVList) -> int
unreal.GeometryScript_List.get_uv_list_length(uv_list: GeometryScriptUVList) -> int
unreal.GeometryScript_List.get_vector_list_item(vector_list: GeometryScriptVectorList, index: int) -> Tuple[Vector, bool]
unreal.GeometryScript_List.get_vector_list_last_index(vector_list: GeometryScriptVectorList) -> int
unreal.GeometryScript_List.get_vector_list_length(vector_list: GeometryScriptVectorList) -> int
unreal.GeometryScript_List.set_color_list_item(color_list: GeometryScriptColorList, index: int, new_color: LinearColor) -> Tuple[GeometryScriptColorList, bool]
unreal.GeometryScript_List.set_index_list_item(index_list: GeometryScriptIndexList, index: int, new_value: int) -> Tuple[GeometryScriptIndexList, bool]
unreal.GeometryScript_List.set_scalar_list_item(scalar_list: GeometryScriptScalarList, index: int, new_value: float) -> Tuple[GeometryScriptScalarList, bool]
unreal.GeometryScript_List.set_uv_list_item(uv_list: GeometryScriptUVList, index: int, new_uv: Vector2D) -> Tuple[GeometryScriptUVList, bool]
unreal.GeometryScript_List.set_vector_list_item(vector_list: GeometryScriptVectorList, index: int, new_value: Vector) -> Tuple[GeometryScriptVectorList, bool]
```

## `unreal.GeometryScript_MeshBooleans(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshBooleans.apply_mesh_boolean(target_mesh: DynamicMesh, target_transform: Transform, tool_mesh: DynamicMesh, tool_transform: Transform, operation: GeometryScriptBooleanOperation, options: GeometryScriptMeshBooleanOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshBooleans.apply_mesh_mirror(target_mesh: DynamicMesh, mirror_frame: Transform, options: GeometryScriptMeshMirrorOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshBooleans.apply_mesh_plane_cut(target_mesh: DynamicMesh, cut_frame: Transform, options: GeometryScriptMeshPlaneCutOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshBooleans.apply_mesh_plane_slice(target_mesh: DynamicMesh, cut_frame: Transform, options: GeometryScriptMeshPlaneSliceOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshBooleans.apply_mesh_self_union(target_mesh: DynamicMesh, options: GeometryScriptMeshSelfUnionOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshComparison(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshComparison.is_intersecting_mesh(target_mesh: DynamicMesh, target_transform: Transform, other_mesh: DynamicMesh, other_transform: Transform, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_MeshComparison.is_same_mesh_as(target_mesh: DynamicMesh, other_mesh: DynamicMesh, options: GeometryScriptIsSameMeshOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, GeometryScriptMeshDifferenceInfo]
unreal.GeometryScript_MeshComparison.measure_distances_between_meshes(target_mesh: DynamicMesh, other_mesh: DynamicMesh, options: GeometryScriptMeasureMeshDistanceOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, float, float, float, float]
```

## `unreal.GeometryScript_MeshDecomposition(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshDecomposition.copy_mesh_selection_to_mesh(target_mesh: DynamicMesh, store_to_submesh: DynamicMesh, selection: GeometryScriptMeshSelection, append_to_existing: bool = False, preserve_group_i_ds: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
unreal.GeometryScript_MeshDecomposition.copy_mesh_to_mesh(copy_from_mesh: DynamicMesh, copy_to_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
unreal.GeometryScript_MeshDecomposition.get_sub_mesh_from_mesh(target_mesh: DynamicMesh, store_to_submesh: DynamicMesh, triangle_list: GeometryScriptIndexList, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh]
unreal.GeometryScript_MeshDecomposition.split_mesh_by_components(target_mesh: DynamicMesh, mesh_pool: DynamicMeshPool, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[DynamicMesh]]
unreal.GeometryScript_MeshDecomposition.split_mesh_by_material_i_ds(target_mesh: DynamicMesh, mesh_pool: DynamicMeshPool, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
unreal.GeometryScript_MeshDecomposition.split_mesh_by_polygroups(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, mesh_pool: DynamicMeshPool, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[DynamicMesh], Array[int]]
```

## `unreal.GeometryScript_MeshDeformers(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshDeformers.apply_bend_warp_to_mesh(target_mesh: DynamicMesh, options: GeometryScriptBendWarpOptions, bend_orientation: Transform, bend_angle: float = 45.000000, bend_extent: float = 50.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_displace_from_per_vertex_vectors(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, vector_list: GeometryScriptVectorList, magnitude: float = 5.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_displace_from_texture_map(target_mesh: DynamicMesh, texture: Texture2D, selection: GeometryScriptMeshSelection, options: GeometryScriptDisplaceFromTextureOptions, uv_layer: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_flare_warp_to_mesh(target_mesh: DynamicMesh, options: GeometryScriptFlareWarpOptions, flare_orientation: Transform, flare_percent_x: float = 0.000000, flare_percent_y: float = 0.000000, flare_extent: float = 50.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_iterative_smoothing_to_mesh(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, options: GeometryScriptIterativeMeshSmoothingOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_math_warp_to_mesh(target_mesh: DynamicMesh, warp_orientation: Transform, warp_type: GeometryScriptMathWarpType, options: GeometryScriptMathWarpOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_perlin_noise_to_mesh(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, options: GeometryScriptPerlinNoiseOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshDeformers.apply_twist_warp_to_mesh(target_mesh: DynamicMesh, options: GeometryScriptTwistWarpOptions, twist_orientation: Transform, twist_angle: float = 45.000000, twist_extent: float = 50.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshEdits(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshEdits.add_triangle_to_mesh(target_mesh: DynamicMesh, new_triangle: IntVector, new_triangle_group_id: int = 0, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_MeshEdits.add_triangles_to_mesh(target_mesh: DynamicMesh, new_triangles_list: GeometryScriptTriangleList, new_triangle_group_id: int = 0, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_MeshEdits.add_vertex_to_mesh(target_mesh: DynamicMesh, new_position: Vector, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_MeshEdits.add_vertices_to_mesh(target_mesh: DynamicMesh, new_positions_list: GeometryScriptVectorList, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_MeshEdits.append_buffers_to_mesh(target_mesh: DynamicMesh, buffers: GeometryScriptSimpleMeshBuffers, material_id: int = 0, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_MeshEdits.append_mesh(target_mesh: DynamicMesh, append_mesh: DynamicMesh, append_transform: Transform, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshEdits.append_mesh_repeated(target_mesh: DynamicMesh, append_mesh: DynamicMesh, append_transform: Transform, repeat_count: int = 1, apply_transform_to_first_instance: bool = True, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshEdits.append_mesh_repeated_with_materials(target_mesh: DynamicMesh, target_mesh_material_list: Array[MaterialInterface], append_mesh: DynamicMesh, append_mesh_material_list: Array[MaterialInterface], append_transform: Transform, repeat_count: int = 1, apply_transform_to_first_instance: bool = True, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[MaterialInterface]]
unreal.GeometryScript_MeshEdits.append_mesh_transformed(target_mesh: DynamicMesh, append_mesh: DynamicMesh, append_transforms: Array[Transform], constant_transform: Transform, constant_transform_is_relative: bool = True, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshEdits.append_mesh_transformed_with_materials(target_mesh: DynamicMesh, target_mesh_material_list: Array[MaterialInterface], append_mesh: DynamicMesh, append_mesh_material_list: Array[MaterialInterface], append_transforms: Array[Transform], constant_transform: Transform, constant_transform_is_relative: bool = True, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[MaterialInterface]]
unreal.GeometryScript_MeshEdits.append_mesh_with_materials(target_mesh: DynamicMesh, target_mesh_material_list: Array[MaterialInterface], append_mesh: DynamicMesh, append_mesh_material_list: Array[MaterialInterface], append_transform: Transform, defer_change_notifications: bool = False, append_options: GeometryScriptAppendMeshOptions = [GeometryScriptCombineAttributesMode.ENABLE_ALL_MATCHING], compact_appended_materials: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[MaterialInterface]]
unreal.GeometryScript_MeshEdits.delete_selected_triangles_from_mesh(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_MeshEdits.delete_triangle_from_mesh(target_mesh: DynamicMesh, triangle_id: int, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_MeshEdits.delete_triangles_from_mesh(target_mesh: DynamicMesh, triangle_list: GeometryScriptIndexList, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_MeshEdits.delete_vertex_from_mesh(target_mesh: DynamicMesh, vertex_id: int, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_MeshEdits.delete_vertices_from_mesh(target_mesh: DynamicMesh, vertex_list: GeometryScriptIndexList, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_MeshEdits.discard_mesh_attributes(target_mesh: DynamicMesh, defer_change_notifications: bool = False) -> DynamicMesh
unreal.GeometryScript_MeshEdits.set_all_mesh_vertex_positions(target_mesh: DynamicMesh, position_list: GeometryScriptVectorList, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshEdits.set_vertex_position(target_mesh: DynamicMesh, vertex_id: int, new_position: Vector, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

## `unreal.GeometryScript_MeshGeodesic(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshGeodesic.create_surface_path(target_mesh: DynamicMesh, direction: Vector, start_triangle_id: int, start_bary_coords: Vector, max_path_length: float, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
unreal.GeometryScript_MeshGeodesic.get_shortest_surface_path(target_mesh: DynamicMesh, start_triangle_id: int, start_bary_coords: Vector, end_triangle_id: int, end_bary_coords: Vector, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptPolyPath, bool]
unreal.GeometryScript_MeshGeodesic.get_shortest_vertex_path(target_mesh: DynamicMesh, start_vertex_id: int, end_vertex_id: int, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

## `unreal.GeometryScript_MeshModeling(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshModeling.apply_mesh_bevel_edge_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, bevel_options: GeometryScriptMeshBevelSelectionOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_bevel_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, bevel_mode: GeometryScriptMeshBevelSelectionMode, bevel_options: GeometryScriptMeshBevelSelectionOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_disconnect_faces(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, allow_bowties_in_output: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_disconnect_faces_along_edges(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_duplicate_faces(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, group_options: GeometryScriptMeshEditPolygroupOptions = [GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0], debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshModeling.apply_mesh_extrude(target_mesh: DynamicMesh, options: GeometryScriptMeshExtrudeOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_extrude_compatibility_5p0(target_mesh: DynamicMesh, options: GeometryScriptMeshExtrudeOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_inset_outset_faces(target_mesh: DynamicMesh, options: GeometryScriptMeshInsetOutsetFacesOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_linear_extrude_faces(target_mesh: DynamicMesh, options: GeometryScriptMeshLinearExtrudeOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_offset(target_mesh: DynamicMesh, options: GeometryScriptMeshOffsetOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_offset_faces(target_mesh: DynamicMesh, options: GeometryScriptMeshOffsetFacesOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_polygroup_bevel(target_mesh: DynamicMesh, options: GeometryScriptMeshBevelOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshModeling.apply_mesh_shell(target_mesh: DynamicMesh, options: GeometryScriptMeshOffsetOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshPoolUtility(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshPoolUtility.discard_global_mesh_pool() -> None
unreal.GeometryScript_MeshPoolUtility.get_global_mesh_pool() -> DynamicMeshPool
```

## `unreal.GeometryScript_MeshQueries(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshQueries.compute_triangle_barycentric_coords(target_mesh: DynamicMesh, triangle_id: int, point: Vector) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector, Vector]
unreal.GeometryScript_MeshQueries.get_all_split_u_vs_at_vertex(target_mesh: DynamicMesh, uv_set_index: int, vertex_id: int) -> Tuple[DynamicMesh, Array[int], Array[Vector2D], bool]
unreal.GeometryScript_MeshQueries.get_all_triangle_i_ds(target_mesh: DynamicMesh) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
unreal.GeometryScript_MeshQueries.get_all_triangle_indices(target_mesh: DynamicMesh, skip_gaps: bool) -> Tuple[DynamicMesh, GeometryScriptTriangleList, bool]
unreal.GeometryScript_MeshQueries.get_all_uv_seam_edges(target_mesh: DynamicMesh, uv_set_index: int) -> Tuple[DynamicMesh, bool, GeometryScriptIndexList]
unreal.GeometryScript_MeshQueries.get_all_vertex_i_ds(target_mesh: DynamicMesh) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
unreal.GeometryScript_MeshQueries.get_all_vertex_positions(target_mesh: DynamicMesh, skip_gaps: bool) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool]
unreal.GeometryScript_MeshQueries.get_all_vertex_positions_at_edges(target_mesh: DynamicMesh, edge_i_ds: GeometryScriptIndexList) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList]
unreal.GeometryScript_MeshQueries.get_has_material_i_ds(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_has_polygroups(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_has_triangle_id_gaps(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_has_triangle_normals(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_has_vertex_colors(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_has_vertex_id_gaps(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_interpolated_triangle_normal(target_mesh: DynamicMesh, triangle_id: int, barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
unreal.GeometryScript_MeshQueries.get_interpolated_triangle_normal_tangents(target_mesh: DynamicMesh, triangle_id: int, barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector, Vector, Vector]
unreal.GeometryScript_MeshQueries.get_interpolated_triangle_position(target_mesh: DynamicMesh, triangle_id: int, barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector]
unreal.GeometryScript_MeshQueries.get_interpolated_triangle_uv(target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int, barycentric_coords: Vector) -> Tuple[DynamicMesh, bool, Vector2D]
unreal.GeometryScript_MeshQueries.get_interpolated_triangle_vertex_color(target_mesh: DynamicMesh, triangle_id: int, barycentric_coords: Vector, default_color: LinearColor) -> Tuple[DynamicMesh, bool, LinearColor]
unreal.GeometryScript_MeshQueries.get_is_closed_mesh(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_is_dense_mesh(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_mesh_bounding_box(target_mesh: DynamicMesh) -> Box
unreal.GeometryScript_MeshQueries.get_mesh_has_attribute_set(target_mesh: DynamicMesh) -> bool
unreal.GeometryScript_MeshQueries.get_mesh_info_string(target_mesh: DynamicMesh) -> str
unreal.GeometryScript_MeshQueries.get_mesh_uv_area(target_mesh: DynamicMesh, uv_channel: int) -> Tuple[float, bool]
unreal.GeometryScript_MeshQueries.get_mesh_volume_area(target_mesh: DynamicMesh) -> Tuple[float, float]
unreal.GeometryScript_MeshQueries.get_mesh_volume_area_center(target_mesh: DynamicMesh) -> Tuple[float, float, Vector]
unreal.GeometryScript_MeshQueries.get_num_connected_components(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_num_extended_polygroup_layers(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_num_open_border_edges(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_num_open_border_loops(target_mesh: DynamicMesh) -> Tuple[int, bool]
unreal.GeometryScript_MeshQueries.get_num_triangle_i_ds(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_num_uv_islands(target_mesh: DynamicMesh, uv_channel: int) -> Tuple[int, bool]
unreal.GeometryScript_MeshQueries.get_num_uv_sets(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_num_vertex_i_ds(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_triangle_face_normal(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[Vector, bool]
unreal.GeometryScript_MeshQueries.get_triangle_indices(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[IntVector, bool]
unreal.GeometryScript_MeshQueries.get_triangle_normal_tangents(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[DynamicMesh, bool, GeometryScriptTriangle, GeometryScriptTriangle, GeometryScriptTriangle]
unreal.GeometryScript_MeshQueries.get_triangle_normals(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[DynamicMesh, Vector, Vector, Vector, bool]
unreal.GeometryScript_MeshQueries.get_triangle_positions(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[bool, Vector, Vector, Vector]
unreal.GeometryScript_MeshQueries.get_triangle_u_vs(target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int) -> Tuple[Vector2D, Vector2D, Vector2D, bool]
unreal.GeometryScript_MeshQueries.get_triangle_vertex_colors(target_mesh: DynamicMesh, triangle_id: int) -> Tuple[DynamicMesh, LinearColor, LinearColor, LinearColor, bool]
unreal.GeometryScript_MeshQueries.get_uv_set_bounding_box(target_mesh: DynamicMesh, uv_set_index: int) -> Tuple[Box2D, bool, bool]
unreal.GeometryScript_MeshQueries.get_vertex_connected_triangles(target_mesh: DynamicMesh, vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
unreal.GeometryScript_MeshQueries.get_vertex_connected_vertices(target_mesh: DynamicMesh, vertex_id: int) -> Tuple[DynamicMesh, Array[int]]
unreal.GeometryScript_MeshQueries.get_vertex_count(target_mesh: DynamicMesh) -> int
unreal.GeometryScript_MeshQueries.get_vertex_position(target_mesh: DynamicMesh, vertex_id: int) -> Tuple[Vector, bool]
unreal.GeometryScript_MeshQueries.is_valid_triangle_id(target_mesh: DynamicMesh, triangle_id: int) -> bool
unreal.GeometryScript_MeshQueries.is_valid_vertex_id(target_mesh: DynamicMesh, vertex_id: int) -> bool
```

## `unreal.GeometryScript_MeshRepair(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshRepair.compact_mesh(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.fill_all_mesh_holes(target_mesh: DynamicMesh, fill_options: GeometryScriptFillHolesOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int, int]
unreal.GeometryScript_MeshRepair.remove_hidden_triangles(target_mesh: DynamicMesh, options: GeometryScriptRemoveHiddenTrianglesOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.remove_small_components(target_mesh: DynamicMesh, options: GeometryScriptRemoveSmallComponentOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.remove_unused_vertices(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.repair_mesh_degenerate_geometry(target_mesh: DynamicMesh, options: GeometryScriptDegenerateTriangleOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.resolve_mesh_t_junctions(target_mesh: DynamicMesh, resolve_options: GeometryScriptResolveTJunctionOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.snap_mesh_open_boundaries(target_mesh: DynamicMesh, snap_options: GeometryScriptSnapBoundariesOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.split_mesh_bowties(target_mesh: DynamicMesh, mesh_bowties: bool = True, attribute_bowties: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshRepair.weld_mesh_edges(target_mesh: DynamicMesh, weld_options: GeometryScriptWeldEdgesOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshSampling(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSampling.compute_non_uniform_point_sampling(target_mesh: DynamicMesh, options: GeometryScriptMeshPointSamplingOptions, non_uniform_options: GeometryScriptNonUniformPointSamplingOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[Transform], Array[float], GeometryScriptIndexList]
unreal.GeometryScript_MeshSampling.compute_point_sampling(target_mesh: DynamicMesh, options: GeometryScriptMeshPointSamplingOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[Transform], GeometryScriptIndexList]
unreal.GeometryScript_MeshSampling.compute_render_capture_cameras_for_box(box: Box, options: GeometryScriptRenderCaptureCamerasForBoxOptions, debug: GeometryScriptDebug = None) -> Array[GeometryScriptRenderCaptureCamera]
unreal.GeometryScript_MeshSampling.compute_render_capture_point_sampling(actors: Array[Actor], cameras: Array[GeometryScriptRenderCaptureCamera], debug: GeometryScriptDebug = None) -> Array[Transform]
unreal.GeometryScript_MeshSampling.compute_vertex_weighted_point_sampling(target_mesh: DynamicMesh, options: GeometryScriptMeshPointSamplingOptions, non_uniform_options: GeometryScriptNonUniformPointSamplingOptions, vertex_weights: GeometryScriptScalarList, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[Transform], Array[float], GeometryScriptIndexList]
```

## `unreal.GeometryScript_MeshSelection(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSelection.combine_mesh_selections(selection_a: GeometryScriptMeshSelection, selection_b: GeometryScriptMeshSelection, combine_mode: GeometryScriptCombineSelectionMode = GeometryScriptCombineSelectionMode.ADD) -> GeometryScriptMeshSelection
unreal.GeometryScript_MeshSelection.convert_index_array_to_mesh_selection(target_mesh: DynamicMesh, index_array: Array[int], selection_type: GeometryScriptMeshSelectionType) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.convert_index_list_to_mesh_selection(target_mesh: DynamicMesh, index_list: GeometryScriptIndexList, selection_type: GeometryScriptMeshSelectionType) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.convert_index_set_to_mesh_selection(target_mesh: DynamicMesh, index_set: Set[int], selection_type: GeometryScriptMeshSelectionType) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.convert_mesh_selection(target_mesh: DynamicMesh, from_selection: GeometryScriptMeshSelection, new_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, allow_partial_inclusion: bool = True) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.convert_mesh_selection_to_index_array(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection) -> Tuple[DynamicMesh, Array[int], GeometryScriptMeshSelectionType]
unreal.GeometryScript_MeshSelection.convert_mesh_selection_to_index_list(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, convert_to_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY) -> Tuple[DynamicMesh, GeometryScriptIndexList, GeometryScriptIndexType]
unreal.GeometryScript_MeshSelection.create_select_all_mesh_selection(target_mesh: DynamicMesh, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.debug_print_mesh_selection(selection: GeometryScriptMeshSelection, disable: bool = False) -> None
unreal.GeometryScript_MeshSelection.expand_contract_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, iterations: int = 1, contract: bool = False, only_expand_to_face_neighbours: bool = False) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.expand_mesh_selection_to_connected(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, connection_type: GeometryScriptTopologyConnectionType = GeometryScriptTopologyConnectionType.GEOMETRIC) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.get_mesh_selection_info(selection: GeometryScriptMeshSelection) -> Tuple[GeometryScriptMeshSelectionType, int]
unreal.GeometryScript_MeshSelection.get_mesh_unique_selection_info(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection) -> Tuple[GeometryScriptMeshSelectionType, int]
unreal.GeometryScript_MeshSelection.invert_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, only_to_connected: bool = False) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_boundary_edges(target_mesh: DynamicMesh) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_by_material_id(target_mesh: DynamicMesh, material_id: int, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_by_normal_angle(target_mesh: DynamicMesh, normal: Vector = [0.000000, 0.000000, 1.000000], max_angle_deg: float = 1.000000, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, invert: bool = False, min_num_triangle_points: int = 3) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_by_polygroup(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_id: int, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_in_box(target_mesh: DynamicMesh, box: Box, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, invert: bool = False, min_num_triangle_points: int = 3) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_in_sphere(target_mesh: DynamicMesh, sphere_origin: Vector = [0.000000, 0.000000, 0.000000], sphere_radius: float = 100.000000, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, invert: bool = False, min_num_triangle_points: int = 3) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_inside_mesh(target_mesh: DynamicMesh, selection_mesh: DynamicMesh, selection_mesh_transform: Transform, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, invert: bool = False, shell_distance: float = 0.000000, winding_threshold: float = 0.500000, min_num_triangle_points: int = 3) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_elements_with_plane(target_mesh: DynamicMesh, plane_origin: Vector = [0.000000, 0.000000, 0.000000], plane_normal: Vector = [0.000000, 0.000000, 1.000000], selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES, invert: bool = False, min_num_triangle_points: int = 3) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_mesh_sharp_edges(target_mesh: DynamicMesh, min_angle_deg: float = 20.000000) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
unreal.GeometryScript_MeshSelection.select_selection_boundary_edges(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, exclude_mesh_boundary_edges: bool = False) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

## `unreal.GeometryScript_MeshSelectionQueries(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSelectionQueries.get_mesh_selection_boundary_loops(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[GeometryScriptIndexList], Array[GeometryScriptPolyPath], int, bool]
unreal.GeometryScript_MeshSelectionQueries.get_mesh_selection_bounding_box(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Box, bool]
```

## `unreal.GeometryScript_MeshSimplification(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSimplification.apply_simplify_to_planar(target_mesh: DynamicMesh, options: GeometryScriptPlanarSimplifyOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSimplification.apply_simplify_to_polygroup_topology(target_mesh: DynamicMesh, options: GeometryScriptPolygroupSimplifyOptions, group_layer: GeometryScriptGroupLayer, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSimplification.apply_simplify_to_tolerance(target_mesh: DynamicMesh, tolerance: float, options: GeometryScriptSimplifyMeshOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSimplification.apply_simplify_to_triangle_count(target_mesh: DynamicMesh, triangle_count: int, options: GeometryScriptSimplifyMeshOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSimplification.apply_simplify_to_vertex_count(target_mesh: DynamicMesh, vertex_count: int, options: GeometryScriptSimplifyMeshOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshSpatial(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSpatial.build_bvh_for_mesh(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
unreal.GeometryScript_MeshSpatial.find_nearest_point_on_mesh(target_mesh: DynamicMesh, query_bvh: GeometryScriptDynamicMeshBVH, query_point: Vector, options: GeometryScriptSpatialQueryOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptTrianglePoint, GeometryScriptSearchOutcomePins]
unreal.GeometryScript_MeshSpatial.find_nearest_ray_intersection_with_mesh(target_mesh: DynamicMesh, query_bvh: GeometryScriptDynamicMeshBVH, ray_origin: Vector, ray_direction: Vector, options: GeometryScriptSpatialQueryOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptRayHitResult, GeometryScriptSearchOutcomePins]
unreal.GeometryScript_MeshSpatial.is_bvh_valid_for_mesh(target_mesh: DynamicMesh, test_bvh: GeometryScriptDynamicMeshBVH, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_MeshSpatial.is_point_inside_mesh(target_mesh: DynamicMesh, query_bvh: GeometryScriptDynamicMeshBVH, query_point: Vector, options: GeometryScriptSpatialQueryOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, GeometryScriptContainmentOutcomePins]
unreal.GeometryScript_MeshSpatial.rebuild_bvh_for_mesh(target_mesh: DynamicMesh, update_bvh: GeometryScriptDynamicMeshBVH, only_if_invalid: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptDynamicMeshBVH]
unreal.GeometryScript_MeshSpatial.reset_bvh(reset_bvh: GeometryScriptDynamicMeshBVH) -> GeometryScriptDynamicMeshBVH
unreal.GeometryScript_MeshSpatial.select_mesh_elements_in_box_with_bvh(target_mesh: DynamicMesh, query_bvh: GeometryScriptDynamicMeshBVH, query_box: Box, options: GeometryScriptSpatialQueryOptions, selection_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.VERTICES, min_num_triangle_points: int = 3, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

## `unreal.GeometryScript_MeshSubdivide(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshSubdivide.apply_pn_tessellation(target_mesh: DynamicMesh, options: GeometryScriptPNTessellateOptions, tessellation_level: int = 3, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSubdivide.apply_selective_tessellation(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, options: GeometryScriptSelectiveTessellateOptions, tessellation_level: int = 1, pattern_type: SelectiveTessellatePatternType = SelectiveTessellatePatternType.CONCENTRIC_RINGS, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshSubdivide.apply_uniform_tessellation(target_mesh: DynamicMesh, tessellation_level: int = 3, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_MeshVoxelProcessing(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_MeshVoxelProcessing.apply_mesh_morphology(target_mesh: DynamicMesh, options: GeometryScriptMorphologyOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_MeshVoxelProcessing.apply_mesh_solidify(target_mesh: DynamicMesh, options: GeometryScriptSolidifyOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_NewAssetUtils(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_NewAssetUtils.create_new_skeletal_mesh_asset_from_mesh(from_dynamic_mesh: DynamicMesh, skeleton: Skeleton, asset_path_and_name: str, options: GeometryScriptCreateNewSkeletalMeshAssetOptions, debug: GeometryScriptDebug = None) -> Tuple[SkeletalMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_new_skeletal_mesh_asset_from_mesh_lo_ds(from_dynamic_mesh_lo_ds: Array[DynamicMesh], skeleton: Skeleton, asset_path_and_name: str, options: GeometryScriptCreateNewSkeletalMeshAssetOptions, debug: GeometryScriptDebug = None) -> Tuple[SkeletalMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh(from_dynamic_mesh: DynamicMesh, asset_path_and_name: str, options: GeometryScriptCreateNewStaticMeshAssetOptions, debug: GeometryScriptDebug = None) -> Tuple[StaticMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh_lo_ds(from_dynamic_mesh: Array[DynamicMesh], asset_path_and_name: str, options: GeometryScriptCreateNewStaticMeshAssetOptions, debug: GeometryScriptDebug = None) -> Tuple[StaticMesh, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_new_texture2d_asset(from_texture: Texture2D, asset_path_and_name: str, options: GeometryScriptCreateNewTexture2DAssetOptions, debug: GeometryScriptDebug = None) -> Tuple[Texture2D, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_new_volume_from_mesh(from_dynamic_mesh: DynamicMesh, create_in_world: World, actor_transform: Transform, base_actor_name: str, options: GeometryScriptCreateNewVolumeFromMeshOptions, debug: GeometryScriptDebug = None) -> Tuple[Volume, World, GeometryScriptOutcomePins]
unreal.GeometryScript_NewAssetUtils.create_unique_new_asset_path_name(asset_folder_path: str, base_asset_name: str, options: GeometryScriptUniqueAssetNameOptions, debug: GeometryScriptDebug = None) -> Tuple[str, str, GeometryScriptOutcomePins]
```

## `unreal.GeometryScript_Normals(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Normals.auto_repair_normals(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.compute_split_normals(target_mesh: DynamicMesh, split_options: GeometryScriptSplitNormalsOptions, calculate_options: GeometryScriptCalculateNormalsOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.compute_tangents(target_mesh: DynamicMesh, options: GeometryScriptTangentsOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.discard_tangents(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.flip_normals(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.get_mesh_has_tangents(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_Normals.get_mesh_per_vertex_normals(target_mesh: DynamicMesh, average_split_vertex_values: bool = True) -> Tuple[DynamicMesh, GeometryScriptVectorList, bool, bool]
unreal.GeometryScript_Normals.get_mesh_per_vertex_tangents(target_mesh: DynamicMesh, average_split_vertex_values: bool = True) -> Tuple[DynamicMesh, GeometryScriptVectorList, GeometryScriptVectorList, bool, bool]
unreal.GeometryScript_Normals.recompute_normals(target_mesh: DynamicMesh, calculate_options: GeometryScriptCalculateNormalsOptions, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.recompute_normals_for_mesh_selection(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, calculate_options: GeometryScriptCalculateNormalsOptions, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.set_mesh_per_vertex_normals(target_mesh: DynamicMesh, vertex_normal_list: GeometryScriptVectorList, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.set_mesh_per_vertex_tangents(target_mesh: DynamicMesh, tangent_x_list: GeometryScriptVectorList, tangent_y_list: GeometryScriptVectorList, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.set_mesh_triangle_normals(target_mesh: DynamicMesh, triangle_id: int, normals: GeometryScriptTriangle, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_Normals.set_per_face_normals(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.set_per_vertex_normals(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.set_split_normals_along_selected_edges(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, split: bool = True, recalculate_normals: bool = True, calculate_options: GeometryScriptCalculateNormalsOptions = [True, True], defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Normals.update_vertex_normal(target_mesh: DynamicMesh, vertex_id: int, update_normal: bool = True, new_normal: Vector = ..., update_tangents: bool = ..., new_tangent_x: Vector = ..., new_tangent_y: Vector = ..., merge_split_values: bool = ..., defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

## `unreal.GeometryScript_OpenSubdiv(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_OpenSubdiv.apply_polygroup_catmull_clark_sub_d(from_dynamic_mesh: DynamicMesh, subdivisions: int, group_layer: GeometryScriptGroupLayer, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_OpenSubdiv.apply_triangle_loop_sub_d(from_dynamic_mesh: DynamicMesh, subdivisions: int, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_PointSetSampling(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_PointSetSampling.downsample_points(points: Array[Vector], options: GeometryScriptPointPriorityOptions, keep_num_points: int = 100, debug: GeometryScriptDebug = None) -> GeometryScriptIndexList
unreal.GeometryScript_PointSetSampling.flatten_points(points_in3d: Array[Vector], options: GeometryScriptPointFlatteningOptions) -> Array[Vector2D]
unreal.GeometryScript_PointSetSampling.get_points_from_index_list(all_points: Array[Vector], indices: GeometryScriptIndexList) -> Array[Vector]
unreal.GeometryScript_PointSetSampling.k_means_cluster_to_arrays(points: Array[Vector], options: GeometryScriptPointClusteringOptions) -> Array[GeometryScriptIndexList]
unreal.GeometryScript_PointSetSampling.k_means_cluster_to_i_ds(points: Array[Vector], options: GeometryScriptPointClusteringOptions) -> Array[int]
unreal.GeometryScript_PointSetSampling.make_bounding_box_from_points(points: Array[Vector], expand_by: float = 0.000000) -> Box
unreal.GeometryScript_PointSetSampling.offset_transforms(transforms: Array[Transform], offset: float, direction: Vector = [0.000000, 0.000000, 1.000000], space: GeometryScriptCoordinateSpace = GeometryScriptCoordinateSpace.LOCAL) -> Array[Transform]
unreal.GeometryScript_PointSetSampling.transforms_to_points(transforms: Array[Transform]) -> Array[Vector]
unreal.GeometryScript_PointSetSampling.unflatten_points(points_in2d: Array[Vector2D], options: GeometryScriptPointFlatteningOptions, height: float = 0.000000) -> Array[Vector]
```

## `unreal.GeometryScript_PolyGroups(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_PolyGroups.clear_polygroups(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, clear_value: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.compute_polygroups_from_angle_threshold(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, crease_angle: float = 15.000000, min_group_size: int = 2, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.compute_polygroups_from_polygon_detection(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, respect_uv_seams: bool = True, respect_hard_normals: bool = False, quad_adjacency_weight: float = 1.000000, quad_metric_clamp: float = 1.000000, max_search_rounds: int = 1, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.convert_components_to_polygroups(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.convert_uv_islands_to_polygroups(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, uv_layer: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.copy_polygroups_layer(target_mesh: DynamicMesh, from_group_layer: GeometryScriptGroupLayer, to_group_layer: GeometryScriptGroupLayer, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.delete_triangles_in_polygroup(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_id: int, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
unreal.GeometryScript_PolyGroups.enable_polygroups(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.get_all_triangle_polygroup_i_ds(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_i_ds_out: GeometryScriptIndexList) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_PolyGroups.get_polygroup_i_ds_in_mesh(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_i_ds_out: GeometryScriptIndexList) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_PolyGroups.get_triangle_polygroup_id(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, triangle_id: int) -> Tuple[int, bool]
unreal.GeometryScript_PolyGroups.get_triangles_in_polygroup(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, polygroup_id: int, triangle_i_ds_out: GeometryScriptIndexList) -> Tuple[DynamicMesh, GeometryScriptIndexList]
unreal.GeometryScript_PolyGroups.set_num_extended_polygroup_layers(target_mesh: DynamicMesh, num_layers: int, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_PolyGroups.set_polygroup_for_mesh_selection(target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer, selection: GeometryScriptMeshSelection, set_polygroup_id: int = 0, generate_new_polygroup: bool = False, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

## `unreal.GeometryScript_PolyPath(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_PolyPath.conv_array_of_vector2d_to_geometry_script_poly_path(path_vertices: Array[Vector2D]) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.conv_array_to_geometry_script_poly_path(path_vertices: Array[Vector]) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.conv_geometry_script_poly_path_to_array(poly_path: GeometryScriptPolyPath) -> Array[Vector]
unreal.GeometryScript_PolyPath.conv_geometry_script_poly_path_to_array_of_vector2d(poly_path: GeometryScriptPolyPath) -> Array[Vector2D]
unreal.GeometryScript_PolyPath.convert_array_of_vector2d_to_poly_path(vertex_array: Array[Vector2D]) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.convert_array_to_poly_path(vertex_array: Array[Vector]) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.convert_poly_path_to_array(poly_path: GeometryScriptPolyPath) -> Array[Vector]
unreal.GeometryScript_PolyPath.convert_poly_path_to_array_of_vector2d(poly_path: GeometryScriptPolyPath) -> Array[Vector2D]
unreal.GeometryScript_PolyPath.convert_spline_to_poly_path(spline: SplineComponent, sampling_options: GeometryScriptSplineSamplingOptions) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.create_arc_path2d(center: Vector2D = [0.000000, 0.000000], radius: float = 10.000000, num_points: int = 10, start_angle: float = 0.000000, end_angle: float = 90.000000) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.create_arc_path3d(transform: Transform, radius: float = 10.000000, num_points: int = 10, start_angle: float = 0.000000, end_angle: float = 90.000000) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.create_circle_path2d(center: Vector2D = [0.000000, 0.000000], radius: float = 10.000000, num_points: int = 10) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.create_circle_path3d(transform: Transform, radius: float = 10.000000, num_points: int = 10) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.flatten_to2d_on_axis(poly_path: GeometryScriptPolyPath, drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z) -> GeometryScriptPolyPath
unreal.GeometryScript_PolyPath.get_nearest_vertex_index(poly_path: GeometryScriptPolyPath, point: Vector) -> int
unreal.GeometryScript_PolyPath.get_poly_path_arc_length(poly_path: GeometryScriptPolyPath) -> float
unreal.GeometryScript_PolyPath.get_poly_path_last_index(poly_path: GeometryScriptPolyPath) -> int
unreal.GeometryScript_PolyPath.get_poly_path_num_vertices(poly_path: GeometryScriptPolyPath) -> int
unreal.GeometryScript_PolyPath.get_poly_path_tangent(poly_path: GeometryScriptPolyPath, index: int) -> Tuple[Vector, bool]
unreal.GeometryScript_PolyPath.get_poly_path_vertex(poly_path: GeometryScriptPolyPath, index: int) -> Tuple[Vector, bool]
unreal.GeometryScript_PolyPath.sample_spline_to_transforms(spline: SplineComponent, sampling_options: GeometryScriptSplineSamplingOptions, relative_transform: Transform, include_scale: bool = True) -> Optional[Tuple[Array[Transform], Array[float]]]
```

## `unreal.GeometryScript_PolygonList(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_PolygonList.add_polygon_to_list(polygon_list: GeometryScriptGeneralPolygonList, outer_polygon: GeometryScriptSimplePolygon, hole_polygons: Array[GeometryScriptSimplePolygon], fix_hole_orientations: bool = True) -> Tuple[int, GeometryScriptGeneralPolygonList]
unreal.GeometryScript_PolygonList.append_polygon_list(polygon_list: GeometryScriptGeneralPolygonList, polygons_to_append: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.create_polygon_list_from_simple_polygons(outer_polygons: Array[GeometryScriptSimplePolygon]) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.create_polygon_list_from_single_polygon(outer_polygon: GeometryScriptSimplePolygon, hole_polygons: Array[GeometryScriptSimplePolygon], fix_hole_orientations: bool = True) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.create_polygons_from_open_poly_paths_offset(poly_paths: Array[GeometryScriptPolyPath], offset_options: GeometryScriptOpenPathOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.create_polygons_from_path_offset(path: Array[Vector2D], offset_options: GeometryScriptOpenPathOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.get_polygon_area(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int) -> Tuple[float, bool]
unreal.GeometryScript_PolygonList.get_polygon_bounds(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int) -> Tuple[Box2D, bool]
unreal.GeometryScript_PolygonList.get_polygon_count(polygon_list: GeometryScriptGeneralPolygonList) -> int
unreal.GeometryScript_PolygonList.get_polygon_hole_count(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int) -> Tuple[int, bool]
unreal.GeometryScript_PolygonList.get_polygon_list_area(polygon_list: GeometryScriptGeneralPolygonList) -> float
unreal.GeometryScript_PolygonList.get_polygon_list_bounds(polygon_list: GeometryScriptGeneralPolygonList) -> Box2D
unreal.GeometryScript_PolygonList.get_polygon_vertex(polygon_list: GeometryScriptGeneralPolygonList, vertex_index: int, polygon_index: int, hole_index: int = -1) -> Tuple[Vector2D, bool]
unreal.GeometryScript_PolygonList.get_polygon_vertex_count(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int, hole_index: int = -1) -> Tuple[int, bool]
unreal.GeometryScript_PolygonList.get_polygon_vertices(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int, hole_index: int = -1) -> Tuple[Array[Vector2D], bool]
unreal.GeometryScript_PolygonList.get_simple_polygon(polygon_list: GeometryScriptGeneralPolygonList, polygon_index: int, hole_index: int = -1) -> Tuple[GeometryScriptSimplePolygon, bool]
unreal.GeometryScript_PolygonList.polygons_difference(polygon_list: GeometryScriptGeneralPolygonList, polygons_to_subtract: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.polygons_exclusive_or(polygon_list: GeometryScriptGeneralPolygonList, polygons_to_exclusive_or: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.polygons_intersection(polygon_list: GeometryScriptGeneralPolygonList, polygons_to_intersect: GeometryScriptGeneralPolygonList) -> GeometryScriptGeneralPolygonList
unreal.GeometryScript_PolygonList.polygons_morphology_close(polygon_list: GeometryScriptGeneralPolygonList, offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.polygons_morphology_open(polygon_list: GeometryScriptGeneralPolygonList, offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.polygons_offset(polygon_list: GeometryScriptGeneralPolygonList, offset_options: GeometryScriptPolygonOffsetOptions, offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.polygons_offsets(polygon_list: GeometryScriptGeneralPolygonList, offset_options: GeometryScriptPolygonOffsetOptions, first_offset: float, second_offset: float, copy_input_on_failure: bool = True) -> Tuple[GeometryScriptGeneralPolygonList, bool]
unreal.GeometryScript_PolygonList.polygons_union(polygon_list: GeometryScriptGeneralPolygonList, copy_input_on_failure: bool = True) -> GeometryScriptGeneralPolygonList
```

## `unreal.GeometryScript_Primitives(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Primitives.append_bounding_box(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, box: Box, steps_x: int = 0, steps_y: int = 0, steps_z: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_bounding_box_with_collision(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, box: Box, steps_x: int = 0, steps_y: int = 0, steps_z: int = 0, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
unreal.GeometryScript_Primitives.append_box(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, dimension_z: float = 100.000000, steps_x: int = 0, steps_y: int = 0, steps_z: int = 0, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_box_with_collision(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, dimension_z: float = 100.000000, steps_x: int = 0, steps_y: int = 0, steps_z: int = 0, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
unreal.GeometryScript_Primitives.append_capsule(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 30.000000, line_length: float = 75.000000, hemisphere_steps: int = 5, circle_steps: int = 8, segment_steps: int = 0, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_capsule_with_collision(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 30.000000, line_length: float = 75.000000, hemisphere_steps: int = 5, circle_steps: int = 8, segment_steps: int = 0, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
unreal.GeometryScript_Primitives.append_cone(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, base_radius: float = 50.000000, top_radius: float = 5.000000, height: float = 100.000000, radial_steps: int = 12, height_steps: int = 4, capped: bool = True, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_curved_stairs(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, step_width: float = 100.000000, step_height: float = 20.000000, inner_radius: float = 150.000000, curve_angle: float = 90.000000, num_steps: int = 8, floating: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_cylinder(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, height: float = 100.000000, radial_steps: int = 12, height_steps: int = 0, capped: bool = True, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_delaunay_triangulation2d(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, vertex_positions: Array[Vector2D], constrained_edges: Array[IntPoint], triangulation_options: GeometryScriptConstrainedDelaunayTriangulationOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[int], bool]
unreal.GeometryScript_Primitives.append_disc(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, angle_steps: int = 16, spoke_steps: int = 0, start_angle: float = 0.000000, end_angle: float = 360.000000, hole_radius: float = 0.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_linear_stairs(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, step_width: float = 100.000000, step_height: float = 20.000000, step_depth: float = 30.000000, num_steps: int = 8, floating: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_polygon_list_triangulation(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_list: GeometryScriptGeneralPolygonList, triangulation_options: GeometryScriptPolygonsTriangulationOptions, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_Primitives.append_rectangle(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, steps_width: int = 0, steps_height: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_rectangle_compatibility_5_0(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, steps_width: int = 0, steps_height: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_rectangle_xy(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, steps_width: int = 0, steps_height: int = 0, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_revolve_path(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, path_vertices: Array[Vector2D], revolve_options: GeometryScriptRevolveOptions, steps: int = 8, capped: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_revolve_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], revolve_options: GeometryScriptRevolveOptions, radius: float = 100.000000, steps: int = 8, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_round_rectangle(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, corner_radius: float = 5.000000, steps_width: int = 0, steps_height: int = 0, steps_round: int = 4, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_round_rectangle_compatibility_5_0(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, corner_radius: float = 5.000000, steps_width: int = 0, steps_height: int = 0, steps_round: int = 4, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_round_rectangle_xy(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, dimension_x: float = 100.000000, dimension_y: float = 100.000000, corner_radius: float = 5.000000, steps_width: int = 0, steps_height: int = 0, steps_round: int = 4, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_simple_collision_shapes(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, simple_collision: GeometryScriptSimpleCollision, triangulation_options: GeometryScriptSimpleCollisionTriangulationOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_simple_extrude_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], height: float = 100.000000, height_steps: int = 0, capped: bool = True, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_simple_swept_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], sweep_path: Array[Vector], loop: bool = False, capped: bool = True, start_scale: float = 1.000000, end_scale: float = 1.000000, rotation_angle_deg: float = 0.000000, miter_limit: float = 1.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sphere_box(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, steps_x: int = 6, steps_y: int = 6, steps_z: int = 6, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.CENTER, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sphere_box_with_collision(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, steps_x: int = 6, steps_y: int = 6, steps_z: int = 6, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.CENTER, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
unreal.GeometryScript_Primitives.append_sphere_covering(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, sphere_covering: GeometryScriptSphereCovering, steps_x: int = 6, steps_y: int = 6, steps_z: int = 6, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sphere_lat_long(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, steps_phi: int = 10, steps_theta: int = 16, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.CENTER, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sphere_lat_long_with_collision(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, radius: float = 50.000000, steps_phi: int = 10, steps_theta: int = 16, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.CENTER, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
unreal.GeometryScript_Primitives.append_spiral_revolve_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], revolve_options: GeometryScriptRevolveOptions, radius: float = 100.000000, steps: int = 18, rise_per_revolution: float = 50.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sweep_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], sweep_path: Array[Transform], loop: bool = False, capped: bool = True, start_scale: float = 1.000000, end_scale: float = 1.000000, rotation_angle_deg: float = 0.000000, miter_limit: float = 1.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_sweep_polyline(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polyline_vertices: Array[Vector2D], sweep_path: Array[Transform], polyline_tex_param_u: Array[float], sweep_path_tex_param_v: Array[float], loop: bool = False, start_scale: float = 1.000000, end_scale: float = 1.000000, rotation_angle_deg: float = 0.000000, miter_limit: float = 1.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_torus(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, revolve_options: GeometryScriptRevolveOptions, major_radius: float = 50.000000, minor_radius: float = 25.000000, major_steps: int = 16, minor_steps: int = 8, origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_triangulated_polygon(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices: Array[Vector2D], allow_self_intersections: bool = True, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_triangulated_polygon3d(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, polygon_vertices3d: Array[Vector], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.append_voronoi_diagram2d(target_mesh: DynamicMesh, primitive_options: GeometryScriptPrimitiveOptions, transform: Transform, voronoi_sites: Array[Vector2D], voronoi_options: GeometryScriptVoronoiOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_Primitives.create_constrained_edges_chain(num_vertices: int, start: int = 0) -> Array[IntPoint]
unreal.GeometryScript_Primitives.create_constrained_edges_loop(num_vertices: int, start: int = 0) -> Array[IntPoint]
```

## `unreal.GeometryScript_Ray(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Ray.get_ray_box_intersection(ray: Ray, box: Box) -> Optional[float]
unreal.GeometryScript_Ray.get_ray_closest_point(ray: Ray, point: Vector) -> Vector
unreal.GeometryScript_Ray.get_ray_line_closest_point(ray: Ray, line_origin: Vector, line_direction: Vector) -> Tuple[float, float, Vector, float, Vector]
unreal.GeometryScript_Ray.get_ray_parameter(ray: Ray, point: Vector) -> float
unreal.GeometryScript_Ray.get_ray_plane_intersection(ray: Ray, plane: Plane) -> Optional[float]
unreal.GeometryScript_Ray.get_ray_point(ray: Ray, distance: float) -> Vector
unreal.GeometryScript_Ray.get_ray_point_distance(ray: Ray, point: Vector) -> float
unreal.GeometryScript_Ray.get_ray_segment_closest_point(ray: Ray, seg_start_point: Vector, seg_end_point: Vector) -> Tuple[float, float, Vector, Vector]
unreal.GeometryScript_Ray.get_ray_sphere_intersection(ray: Ray, sphere_center: Vector, sphere_radius: float) -> Optional[Tuple[float, float]]
unreal.GeometryScript_Ray.get_ray_start_end(ray: Ray, start_distance: float = 0.000000, end_distance: float = 0.000000) -> Tuple[Vector, Vector]
unreal.GeometryScript_Ray.get_transformed_ray(ray: Ray, transform: Transform, invert: bool = False) -> Ray
unreal.GeometryScript_Ray.make_ray_from_point_direction(origin: Vector, direction: Vector, direction_is_normalized: bool = True) -> Ray
unreal.GeometryScript_Ray.make_ray_from_points(a: Vector, b: Vector) -> Ray
```

## `unreal.GeometryScript_Remeshing(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_Remeshing.apply_uniform_remesh(target_mesh: DynamicMesh, remesh_options: GeometryScriptRemeshOptions, uniform_options: GeometryScriptUniformRemeshOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_SceneUtils(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_SceneUtils.copy_collision_meshes_from_object(from_object: Object, to_dynamic_mesh: DynamicMesh, transform_to_world: bool, use_complex_collision: bool = False, sphere_resolution: int = 16, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Transform, GeometryScriptOutcomePins]
unreal.GeometryScript_SceneUtils.copy_mesh_from_component(component: SceneComponent, to_dynamic_mesh: DynamicMesh, options: GeometryScriptCopyMeshFromComponentOptions, transform_to_world: bool, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Transform, GeometryScriptOutcomePins]
unreal.GeometryScript_SceneUtils.create_dynamic_mesh_pool() -> DynamicMeshPool
unreal.GeometryScript_SceneUtils.determine_mesh_occlusion(source_meshes: Array[DynamicMesh], source_mesh_transforms: Array[Transform], transparent_meshes: Array[DynamicMesh], transparent_mesh_transforms: Array[Transform], occlude_meshes: Array[DynamicMesh], occlude_mesh_transforms: Array[Transform], occlusion_options: GeometryScriptDetermineMeshOcclusionOptions, debug: GeometryScriptDebug = None) -> Tuple[Array[bool], Array[bool]]
unreal.GeometryScript_SceneUtils.set_component_material_list(component: PrimitiveComponent, material_list: Array[MaterialInterface], debug: GeometryScriptDebug = None) -> None
```

## `unreal.GeometryScript_SimplePolygon(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_SimplePolygon.add_polygon_vertex(polygon: GeometryScriptSimplePolygon, position: Vector2D) -> Tuple[int, GeometryScriptSimplePolygon]
unreal.GeometryScript_SimplePolygon.conv_array_of_vector2d_to_geometry_script_simple_polygon(path_vertices: Array[Vector2D]) -> GeometryScriptSimplePolygon
unreal.GeometryScript_SimplePolygon.conv_array_to_geometry_script_simple_polygon(path_vertices: Array[Vector]) -> GeometryScriptSimplePolygon
unreal.GeometryScript_SimplePolygon.conv_geometry_script_simple_polygon_to_array(polygon: GeometryScriptSimplePolygon) -> Array[Vector]
unreal.GeometryScript_SimplePolygon.conv_geometry_script_simple_polygon_to_array_of_vector2d(polygon: GeometryScriptSimplePolygon) -> Array[Vector2D]
unreal.GeometryScript_SimplePolygon.convert_spline_to_polygon(spline: SplineComponent, sampling_options: GeometryScriptSplineSamplingOptions, drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z) -> GeometryScriptSimplePolygon
unreal.GeometryScript_SimplePolygon.get_polygon_arc_length(polygon: GeometryScriptSimplePolygon) -> float
unreal.GeometryScript_SimplePolygon.get_polygon_area(polygon: GeometryScriptSimplePolygon) -> float
unreal.GeometryScript_SimplePolygon.get_polygon_bounds(polygon: GeometryScriptSimplePolygon) -> Box2D
unreal.GeometryScript_SimplePolygon.get_polygon_tangent(polygon: GeometryScriptSimplePolygon, vertex_index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScript_SimplePolygon.get_polygon_vertex(polygon: GeometryScriptSimplePolygon, vertex_index: int) -> Tuple[Vector2D, bool]
unreal.GeometryScript_SimplePolygon.get_polygon_vertex_count(polygon: GeometryScriptSimplePolygon) -> int
unreal.GeometryScript_SimplePolygon.set_polygon_vertex(polygon: GeometryScriptSimplePolygon, vertex_index: int, position: Vector2D) -> Tuple[GeometryScriptSimplePolygon, bool]
```

## `unreal.GeometryScript_UVs(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_UVs.add_uv_element_to_mesh(target_mesh: DynamicMesh, uv_set_index: int, new_uv_position: Vector2D, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int, bool]
unreal.GeometryScript_UVs.apply_texel_density_uv_scaling(target_mesh: DynamicMesh, uv_set_index: int, options: GeometryScriptUVTexelDensityOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.auto_generate_patch_builder_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, options: GeometryScriptPatchBuilderOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.auto_generate_x_atlas_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, options: GeometryScriptXAtlasOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.compute_mesh_local_uv_param(target_mesh: DynamicMesh, center_point: Vector, center_point_triangle_id: int, radius: float = 1.000000, use_interpolated_normal: bool = False, tangent_y_direction: Vector = [0.000000, 0.000000, 0.000000], uv_rotation_deg: float = 0.000000, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Array[int], Array[Vector2D]]
unreal.GeometryScript_UVs.copy_mesh_to_mesh_uv_layer(copy_from_uv_mesh: DynamicMesh, to_uv_set_index: int, copy_to_mesh: DynamicMesh, only_uv_positions: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
unreal.GeometryScript_UVs.copy_mesh_uv_layer_to_mesh(copy_from_mesh: DynamicMesh, uv_set_index: int, copy_to_uv_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, DynamicMesh, DynamicMesh, bool, bool]
unreal.GeometryScript_UVs.copy_uv_set(target_mesh: DynamicMesh, from_uv_set: int, to_uv_set: int, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.get_mesh_per_vertex_u_vs(target_mesh: DynamicMesh, uv_set_index: int, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, GeometryScriptUVList, bool, bool, bool]
unreal.GeometryScript_UVs.get_mesh_triangle_uv_element_i_ds(target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int) -> Tuple[DynamicMesh, IntVector, bool]
unreal.GeometryScript_UVs.get_mesh_uv_element_position(target_mesh: DynamicMesh, uv_set_index: int, element_id: int) -> Tuple[DynamicMesh, Vector2D, bool]
unreal.GeometryScript_UVs.get_mesh_uv_size_info(target_mesh: DynamicMesh, uv_set_index: int, selection: GeometryScriptMeshSelection, only_include_valid_uv_tris: bool = True, debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, float, float, Box, Box2D, bool, bool]
unreal.GeometryScript_UVs.layout_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, layout_options: GeometryScriptLayoutUVsOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.recompute_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, options: GeometryScriptRecomputeUVsOptions, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.repack_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, repack_options: GeometryScriptRepackUVsOptions, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.rotate_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, rotation_angle: float, rotation_origin: Vector2D, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.scale_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, scale: Vector2D, scale_origin: Vector2D, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.set_mesh_triangle_u_vs(target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int, u_vs: GeometryScriptUVTriangle, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_UVs.set_mesh_triangle_uv_element_i_ds(target_mesh: DynamicMesh, uv_set_index: int, triangle_id: int, triangle_uv_elements: IntVector, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_UVs.set_mesh_u_vs_from_box_projection(target_mesh: DynamicMesh, uv_set_index: int, box_transform: Transform, selection: GeometryScriptMeshSelection, min_island_tri_count: int = 2, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.set_mesh_u_vs_from_cylinder_projection(target_mesh: DynamicMesh, uv_set_index: int, cylinder_transform: Transform, selection: GeometryScriptMeshSelection, split_angle: float = 45.000000, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.set_mesh_u_vs_from_planar_projection(target_mesh: DynamicMesh, uv_set_index: int, plane_transform: Transform, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.set_mesh_uv_element_position(target_mesh: DynamicMesh, uv_set_index: int, element_id: int, new_uv_position: Vector2D, defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
unreal.GeometryScript_UVs.set_num_uv_sets(target_mesh: DynamicMesh, num_uv_sets: int, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.set_uv_seams_along_selected_edges(target_mesh: DynamicMesh, uv_channel: int, selection: GeometryScriptMeshSelection, insert_seams: bool = True, defer_change_notifications: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_UVs.translate_mesh_u_vs(target_mesh: DynamicMesh, uv_set_index: int, translation: Vector2D, selection: GeometryScriptMeshSelection, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_VectorMath(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_VectorMath.constant_scalar_multiply(constant: float, scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.constant_scalar_multiply_in_place(constant: float, scalar_list: GeometryScriptScalarList) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.constant_vector_multiply(constant: float, vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.constant_vector_multiply_in_place(constant: float, vector_list: GeometryScriptVectorList) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.scalar_blend(scalar_list_a: GeometryScriptScalarList, scalar_list_b: GeometryScriptScalarList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_blend_in_place(scalar_list_a: GeometryScriptScalarList, scalar_list_b: GeometryScriptScalarList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_invert(scalar_list: GeometryScriptScalarList, numerator: float = 1.000000, set_on_failure: float = 0.000000, epsilon: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_invert_in_place(scalar_list: GeometryScriptScalarList, numerator: float = 1.000000, set_on_failure: float = 0.000000, epsilon: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_multiply(scalar_list_a: GeometryScriptScalarList, scalar_list_b: GeometryScriptScalarList, constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_multiply_in_place(scalar_list_a: GeometryScriptScalarList, scalar_list_b: GeometryScriptScalarList, constant_multiplier: float = 1.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.scalar_vector_multiply(scalar_list: GeometryScriptScalarList, vector_list: GeometryScriptVectorList, scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.scalar_vector_multiply_in_place(scalar_list: GeometryScriptScalarList, vector_list: GeometryScriptVectorList, scalar_multiplier: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_blend(vector_list_a: GeometryScriptVectorList, vector_list_b: GeometryScriptVectorList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_blend_in_place(vector_list_a: GeometryScriptVectorList, vector_list_b: GeometryScriptVectorList, constant_a: float = 1.000000, constant_b: float = 1.000000) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_cross(vector_list_a: GeometryScriptVectorList, vector_list_b: GeometryScriptVectorList) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_dot(vector_list_a: GeometryScriptVectorList, vector_list_b: GeometryScriptVectorList) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.vector_inverse_transform_in_place(vector_list: GeometryScriptVectorList, transform: Transform, as_position: bool = True) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_length(vector_list: GeometryScriptVectorList) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.vector_normalize_in_place(vector_list: GeometryScriptVectorList, set_on_failure: Vector = [0.000000, 0.000000, 0.000000]) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_plane_project_in_place(vector_list: GeometryScriptVectorList, plane: Plane) -> GeometryScriptVectorList
unreal.GeometryScript_VectorMath.vector_to_scalar(vector_list: GeometryScriptVectorList, constant_x: float = 1.000000, constant_y: float = 0.000000, constant_z: float = 0.000000) -> GeometryScriptScalarList
unreal.GeometryScript_VectorMath.vector_transform_in_place(vector_list: GeometryScriptVectorList, transform: Transform, as_position: bool = True) -> GeometryScriptVectorList
```

## `unreal.GeometryScript_VertexColors(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_VertexColors.blur_mesh_vertex_colors(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, num_iterations: int = 1, strength: float = 0.500000, blur_mode: GeometryScriptBlurColorMode = GeometryScriptBlurColorMode.UNIFORM, options: GeometryScriptBlurMeshVertexColorsOptions = [True, True, True, True], debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_VertexColors.convert_mesh_vertex_colors_linear_to_srgb(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_VertexColors.convert_mesh_vertex_colors_srgb_to_linear(target_mesh: DynamicMesh, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_VertexColors.get_mesh_per_vertex_colors(target_mesh: DynamicMesh, blend_split_vertex_values: bool = True) -> Tuple[DynamicMesh, GeometryScriptColorList, bool, bool]
unreal.GeometryScript_VertexColors.set_mesh_constant_vertex_color(target_mesh: DynamicMesh, color: LinearColor, flags: GeometryScriptColorFlags, clear_existing: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_VertexColors.set_mesh_per_vertex_colors(target_mesh: DynamicMesh, vertex_color_list: GeometryScriptColorList, debug: GeometryScriptDebug = None) -> DynamicMesh
unreal.GeometryScript_VertexColors.set_mesh_selection_vertex_color(target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection, color: LinearColor, flags: GeometryScriptColorFlags, create_color_seam: bool = False, debug: GeometryScriptDebug = None) -> DynamicMesh
```

## `unreal.GeometryScript_VolumeBake(BlueprintFunctionLibrary)`

```python
unreal.GeometryScript_VolumeBake.bake_signed_distance_to_volume_texture(target_mesh: DynamicMesh, volume_texture: VolumeTexture, distance_settings: ComputeDistanceFieldSettings, texture_settings: DistanceFieldToTextureSettings) -> bool
```

## `unreal.GerstnerWaterWaveGeneratorBase(Object)`

```python
unreal.GerstnerWaterWaveGeneratorBase.generate_gerstner_waves() -> Array[GerstnerWave]
```

## `unreal.GerstnerWaterWaveGeneratorSimple(GerstnerWaterWaveGeneratorBase)`

```python
unreal.GerstnerWaterWaveGeneratorSimple.amplitude_falloff(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.direction_angular_spread_deg(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.large_wave_steepness(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.max_amplitude(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.max_wavelength(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.min_amplitude(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.min_wavelength(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.num_waves(value: int) -> None
unreal.GerstnerWaterWaveGeneratorSimple.randomness(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.seed(value: int) -> None
unreal.GerstnerWaterWaveGeneratorSimple.small_wave_steepness(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.steepness_falloff(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.wavelength_falloff(value: float) -> None
unreal.GerstnerWaterWaveGeneratorSimple.wind_angle_deg(value: float) -> None
```

## `unreal.GerstnerWaterWaves(WaterWaves)`

```python
unreal.GerstnerWaterWaves.gerstner_wave_generator() -> GerstnerWaterWaveGeneratorBase
unreal.GerstnerWaterWaves.gerstner_waves() -> Array[GerstnerWave]
unreal.GerstnerWaterWaves.max_wave_height() -> float
```

## `unreal.HairGeometrySettings(StructBase)`

```python
unreal.HairGeometrySettings.__init__(hair_width: float = 0.000000, hair_width_override: bool = False, hair_root_scale: float = 0.000000, hair_tip_scale: float = 0.000000) -> None
unreal.HairGeometrySettings.hair_root_scale(value: float) -> None
unreal.HairGeometrySettings.hair_tip_scale(value: float) -> None
unreal.HairGeometrySettings.hair_width(value: float) -> None
unreal.HairGeometrySettings.hair_width_override(value: bool) -> None
```

## `unreal.HapticFeedbackDetails_Curve(StructBase)`

```python
unreal.HapticFeedbackDetails_Curve.__init__() -> None
```

## `unreal.IndexedCurve(StructBase)`

```python
unreal.IndexedCurve.__init__() -> None
```

## `unreal.InputModifierResponseCurveExponential(InputModifier)`

```python
unreal.InputModifierResponseCurveExponential.curve_exponent(value: Vector) -> None
```

## `unreal.InputModifierResponseCurveUser(InputModifier)`

```python
unreal.InputModifierResponseCurveUser.response_x(value: CurveFloat) -> None
unreal.InputModifierResponseCurveUser.response_y(value: CurveFloat) -> None
unreal.InputModifierResponseCurveUser.response_z(value: CurveFloat) -> None
```

## `unreal.InterchangeMeshGeometry(StructBase)`

```python
unreal.InterchangeMeshGeometry.__init__() -> None
```

## `unreal.InterpCurveFloat(StructBase)`

```python
unreal.InterpCurveFloat.__init__(points: Array[InterpCurvePointFloat] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveFloat.is_looped(value: bool) -> None
unreal.InterpCurveFloat.loop_key_offset(value: float) -> None
unreal.InterpCurveFloat.points(value: Array[InterpCurvePointFloat]) -> None
```

## `unreal.InterpCurveLinearColor(StructBase)`

```python
unreal.InterpCurveLinearColor.__init__(points: Array[InterpCurvePointLinearColor] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveLinearColor.is_looped(value: bool) -> None
unreal.InterpCurveLinearColor.loop_key_offset(value: float) -> None
unreal.InterpCurveLinearColor.points(value: Array[InterpCurvePointLinearColor]) -> None
```

## `unreal.InterpCurvePointFloat(StructBase)`

```python
unreal.InterpCurvePointFloat.__init__(val: float = 0.000000, out_val: float = 0.000000, arrive_tangent: float = 0.000000, leave_tangent: float = 0.000000, interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointFloat.arrive_tangent(value: float) -> None
unreal.InterpCurvePointFloat.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointFloat.leave_tangent(value: float) -> None
unreal.InterpCurvePointFloat.out_val(value: float) -> None
unreal.InterpCurvePointFloat.val(value: float) -> None
```

## `unreal.InterpCurvePointLinearColor(StructBase)`

```python
unreal.InterpCurvePointLinearColor.__init__(val: float = 0.000000, out_val: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], arrive_tangent: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], leave_tangent: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointLinearColor.arrive_tangent(value: LinearColor) -> None
unreal.InterpCurvePointLinearColor.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointLinearColor.leave_tangent(value: LinearColor) -> None
unreal.InterpCurvePointLinearColor.out_val(value: LinearColor) -> None
unreal.InterpCurvePointLinearColor.val(value: float) -> None
```

## `unreal.InterpCurvePointQuat(StructBase)`

```python
unreal.InterpCurvePointQuat.__init__(val: float = 0.000000, out_val: Quat = [0.000000, 0.000000, 0.000000, 1.000000], arrive_tangent: Quat = [0.000000, 0.000000, 0.000000, 1.000000], leave_tangent: Quat = [0.000000, 0.000000, 0.000000, 1.000000], interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointQuat.arrive_tangent(value: Quat) -> None
unreal.InterpCurvePointQuat.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointQuat.leave_tangent(value: Quat) -> None
unreal.InterpCurvePointQuat.out_val(value: Quat) -> None
unreal.InterpCurvePointQuat.val(value: float) -> None
```

## `unreal.InterpCurvePointTwoVectors(StructBase)`

```python
unreal.InterpCurvePointTwoVectors.__init__(val: float = 0.000000, out_val: TwoVectors = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], arrive_tangent: TwoVectors = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], leave_tangent: TwoVectors = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]], interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointTwoVectors.arrive_tangent(value: TwoVectors) -> None
unreal.InterpCurvePointTwoVectors.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointTwoVectors.leave_tangent(value: TwoVectors) -> None
unreal.InterpCurvePointTwoVectors.out_val(value: TwoVectors) -> None
unreal.InterpCurvePointTwoVectors.val(value: float) -> None
```

## `unreal.InterpCurvePointVector(StructBase)`

```python
unreal.InterpCurvePointVector.__init__(val: float = 0.000000, out_val: Vector = [0.000000, 0.000000, 0.000000], arrive_tangent: Vector = [0.000000, 0.000000, 0.000000], leave_tangent: Vector = [0.000000, 0.000000, 0.000000], interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointVector.arrive_tangent(value: Vector) -> None
unreal.InterpCurvePointVector.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointVector.leave_tangent(value: Vector) -> None
unreal.InterpCurvePointVector.out_val(value: Vector) -> None
unreal.InterpCurvePointVector.val(value: float) -> None
```

## `unreal.InterpCurvePointVector2D(StructBase)`

```python
unreal.InterpCurvePointVector2D.__init__(val: float = 0.000000, out_val: Vector2D = [0.000000, 0.000000], arrive_tangent: Vector2D = [0.000000, 0.000000], leave_tangent: Vector2D = [0.000000, 0.000000], interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
unreal.InterpCurvePointVector2D.arrive_tangent(value: Vector2D) -> None
unreal.InterpCurvePointVector2D.interp_mode(value: InterpCurveMode) -> None
unreal.InterpCurvePointVector2D.leave_tangent(value: Vector2D) -> None
unreal.InterpCurvePointVector2D.out_val(value: Vector2D) -> None
unreal.InterpCurvePointVector2D.val(value: float) -> None
```

## `unreal.InterpCurveQuat(StructBase)`

```python
unreal.InterpCurveQuat.__init__(points: Array[InterpCurvePointQuat] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveQuat.is_looped(value: bool) -> None
unreal.InterpCurveQuat.loop_key_offset(value: float) -> None
unreal.InterpCurveQuat.points(value: Array[InterpCurvePointQuat]) -> None
```

## `unreal.InterpCurveTwoVectors(StructBase)`

```python
unreal.InterpCurveTwoVectors.__init__(points: Array[InterpCurvePointTwoVectors] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveTwoVectors.is_looped(value: bool) -> None
unreal.InterpCurveTwoVectors.loop_key_offset(value: float) -> None
unreal.InterpCurveTwoVectors.points(value: Array[InterpCurvePointTwoVectors]) -> None
```

## `unreal.InterpCurveVector(StructBase)`

```python
unreal.InterpCurveVector.__init__(points: Array[InterpCurvePointVector] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveVector.is_looped(value: bool) -> None
unreal.InterpCurveVector.loop_key_offset(value: float) -> None
unreal.InterpCurveVector.points(value: Array[InterpCurvePointVector]) -> None
```

## `unreal.InterpCurveVector2D(StructBase)`

```python
unreal.InterpCurveVector2D.__init__(points: Array[InterpCurvePointVector2D] = [], is_looped: bool = False, loop_key_offset: float = 0.000000) -> None
unreal.InterpCurveVector2D.is_looped(value: bool) -> None
unreal.InterpCurveVector2D.loop_key_offset(value: float) -> None
unreal.InterpCurveVector2D.points(value: Array[InterpCurvePointVector2D]) -> None
```

## `unreal.LandmassLandscapeInfo(StructBase)`

```python
unreal.LandmassLandscapeInfo.__init__(landscape_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], landscape_quads: IntPoint = [0, 0], render_target_resolution: IntPoint = [0, 0]) -> None
unreal.LandmassLandscapeInfo.landscape_quads(value: IntPoint) -> None
unreal.LandmassLandscapeInfo.landscape_transform(value: Transform) -> None
unreal.LandmassLandscapeInfo.render_target_resolution(value: IntPoint) -> None
```

## `unreal.Landscape(LandscapeProxy)`

```python
unreal.Landscape.force_layers_full_update() -> None
unreal.Landscape.get_target_layer_names(include_visibility_layer: bool = False) -> Array[Name]
unreal.Landscape.render_heightmap(world_transform: Transform, extents: Box2D, out_render_target: TextureRenderTarget2D) -> bool
unreal.Landscape.render_weightmap(world_transform: Transform, extents: Box2D, weightmap_layer_name: Name, out_render_target: TextureRenderTarget2D) -> bool
unreal.Landscape.render_weightmaps(world_transform: Transform, extents: Box2D, weightmap_layer_names: Array[Name], out_render_target: TextureRenderTarget) -> bool
```

## `unreal.LandscapeBrushParameters(StructBase)`

```python
unreal.LandscapeBrushParameters.__init__(render_area_world_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], render_area_size: IntPoint = [0, 0], combined_result: TextureRenderTarget2D = None, layer_type: LandscapeToolTargetType = LandscapeToolTargetType.HEIGHTMAP, weightmap_layer_name: Name = "None") -> None
unreal.LandscapeBrushParameters.combined_result(value: TextureRenderTarget2D) -> None
unreal.LandscapeBrushParameters.layer_type(value: LandscapeToolTargetType) -> None
unreal.LandscapeBrushParameters.render_area_size(value: IntPoint) -> None
unreal.LandscapeBrushParameters.render_area_world_transform(value: Transform) -> None
unreal.LandscapeBrushParameters.weightmap_layer_name(value: Name) -> None
```

## `unreal.LandscapeComponent(PrimitiveComponent)`

```python
unreal.LandscapeComponent.editor_get_paint_layer_weight_at_location(location: Vector, paint_layer: LandscapeLayerInfoObject) -> float
unreal.LandscapeComponent.editor_get_paint_layer_weight_by_name_at_location(location: Vector, paint_layer_name: Name) -> float
unreal.LandscapeComponent.forced_lod() -> int
unreal.LandscapeComponent.get_material_instance_dynamic(index: int) -> MaterialInstanceDynamic
unreal.LandscapeComponent.lod_bias() -> int
unreal.LandscapeComponent.override_hole_material(value: MaterialInterface) -> None
unreal.LandscapeComponent.override_material(value: MaterialInterface) -> None
unreal.LandscapeComponent.section_base_x() -> int
unreal.LandscapeComponent.section_base_y() -> int
unreal.LandscapeComponent.set_forced_lod(forced_lod: int) -> None
unreal.LandscapeComponent.set_lod_bias(lod_bias: int) -> None
```

## `unreal.LandscapeGrassType(Object)`

```python
unreal.LandscapeGrassType.enable_density_scaling() -> bool
unreal.LandscapeGrassType.grass_varieties() -> Array[GrassVariety]
```

## `unreal.LandscapeProxy(PartitionActor)`

```python
unreal.LandscapeProxy.affect_distance_field_lighting() -> bool
unreal.LandscapeProxy.affect_dynamic_indirect_lighting() -> bool
unreal.LandscapeProxy.affect_indirect_lighting_while_hidden() -> bool
unreal.LandscapeProxy.body_instance() -> BodyInstance
unreal.LandscapeProxy.cast_contact_shadow() -> bool
unreal.LandscapeProxy.cast_dynamic_shadow() -> bool
unreal.LandscapeProxy.cast_far_shadow() -> bool
unreal.LandscapeProxy.cast_hidden_shadow() -> bool
unreal.LandscapeProxy.cast_shadow() -> bool
unreal.LandscapeProxy.cast_shadow_as_two_sided() -> bool
unreal.LandscapeProxy.cast_static_shadow() -> bool
unreal.LandscapeProxy.change_component_screen_size_to_use_sub_sections(component_screen_size_to_use_sub_sections: float) -> None
unreal.LandscapeProxy.change_lod_distance_factor(lod_distance_factor: float) -> None
unreal.LandscapeProxy.custom_depth_stencil_value() -> int
unreal.LandscapeProxy.custom_depth_stencil_write_mask() -> RendererStencilMask
unreal.LandscapeProxy.delete_unused_layers() -> None
unreal.LandscapeProxy.editor_apply_spline(spline_component: SplineComponent, start_width: float = 200.000000, end_width: float = 200.000000, start_side_falloff: float = 200.000000, end_side_falloff: float = 200.000000, start_roll: float = 0.000000, end_roll: float = 0.000000, num_subdivisions: int = 20, raise_heights: bool = True, lower_heights: bool = True, paint_layer: LandscapeLayerInfoObject = None, edit_layer_name: Name = "None") -> None
unreal.LandscapeProxy.enable_nanite() -> bool
unreal.LandscapeProxy.generate_overlap_events() -> bool
unreal.LandscapeProxy.get_landscape_actor() -> Landscape
unreal.LandscapeProxy.holdout(value: bool) -> None
unreal.LandscapeProxy.landscape_export_heightmap_to_render_target(render_target: TextureRenderTarget2D, export_height_into_rg_channel: bool = False, export_landscape_proxies: bool = True) -> bool
unreal.LandscapeProxy.landscape_export_weightmap_to_render_target(render_target: TextureRenderTarget2D, layer_name: Name) -> bool
unreal.LandscapeProxy.landscape_import_heightmap_from_render_target(render_target: TextureRenderTarget2D, import_height_from_rg_channel: bool = False) -> bool
unreal.LandscapeProxy.landscape_import_weightmap_from_render_target(render_target: TextureRenderTarget2D, layer_name: Name) -> bool
unreal.LandscapeProxy.landscape_material(value: MaterialInterface) -> None
unreal.LandscapeProxy.ld_max_draw_distance() -> float
unreal.LandscapeProxy.lighting_channels() -> LightingChannels
unreal.LandscapeProxy.render_custom_depth() -> bool
unreal.LandscapeProxy.runtime_virtual_textures(value: Array[RuntimeVirtualTexture]) -> None
unreal.LandscapeProxy.set_landscape_material_scalar_parameter_value(parameter_name: Name, value: float) -> None
unreal.LandscapeProxy.set_landscape_material_texture_parameter_value(parameter_name: Name, value: Texture) -> None
unreal.LandscapeProxy.set_landscape_material_vector_parameter_value(parameter_name: Name, value: LinearColor) -> None
unreal.LandscapeProxy.shadow_cache_invalidation_behavior() -> ShadowCacheInvalidationBehavior
unreal.LandscapeProxy.virtual_texture_lod_bias() -> int
unreal.LandscapeProxy.virtual_texture_num_lods() -> int
unreal.LandscapeProxy.virtual_texture_render_pass_type(value: RuntimeVirtualTextureMainPassType) -> None
unreal.LandscapeProxy.virtual_texture_render_with_quad() -> bool
unreal.LandscapeProxy.virtual_texture_render_with_quad_hq() -> bool
```

## `unreal.LandscapeSplineControlPoint(Object)`

```python
unreal.LandscapeSplineControlPoint.body_instance() -> BodyInstance
```

## `unreal.LandscapeSplineMeshEntry(StructBase)`

```python
unreal.LandscapeSplineMeshEntry.__init__() -> None
```

## `unreal.LandscapeSplineSegment(Object)`

```python
unreal.LandscapeSplineSegment.body_instance() -> BodyInstance
```

## `unreal.LandscapeSplineSegmentConnection(StructBase)`

```python
unreal.LandscapeSplineSegmentConnection.__init__() -> None
```

## `unreal.LandscapeSplinesComponent(PrimitiveComponent)`

```python
unreal.LandscapeSplinesComponent.get_spline_mesh_components() -> Array[SplineMeshComponent]
```

## `unreal.LandscapeTargetLayerSettings(StructBase)`

```python
unreal.LandscapeTargetLayerSettings.__init__() -> None
```

## `unreal.LiveLinkCurveConversionSettings(StructBase)`

```python
unreal.LiveLinkCurveConversionSettings.__init__() -> None
```

## `unreal.ModelerWaterAtom(EntityAtomBase)`

```python
unreal.ModelerWaterAtom.align_z() -> bool
unreal.ModelerWaterAtom.corner_radius() -> float
unreal.ModelerWaterAtom.corner_split_num() -> int
unreal.ModelerWaterAtom.inverse_normal() -> bool
unreal.ModelerWaterAtom.ripple_scale() -> float
unreal.ModelerWaterAtom.use_vertex_corner() -> bool
unreal.ModelerWaterAtom.water_color() -> str
unreal.ModelerWaterAtom.water_height() -> float
unreal.ModelerWaterAtom.water_transparency() -> float
unreal.ModelerWaterAtom.water_transparent_depth() -> float
unreal.ModelerWaterAtom.water_type() -> WdpModelerWaterType
unreal.ModelerWaterAtom.wave_height() -> float
unreal.ModelerWaterAtom.wave_intensity() -> float
unreal.ModelerWaterAtom.wave_rotate() -> float
unreal.ModelerWaterAtom.wave_scale() -> float
unreal.ModelerWaterAtom.wave_speed() -> float
```

## `unreal.MovieSceneGeometryCacheParams(StructBase)`

```python
unreal.MovieSceneGeometryCacheParams.__init__(geometry_cache_asset: GeometryCache = None, first_loop_start_frame_offset: FrameNumber = [0], start_frame_offset: FrameNumber = [0], end_frame_offset: FrameNumber = [0], play_rate: float = 0.000000, reverse: bool = False) -> None
unreal.MovieSceneGeometryCacheParams.end_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneGeometryCacheParams.first_loop_start_frame_offset(value: FrameNumber) -> None
unreal.MovieSceneGeometryCacheParams.geometry_cache_asset(value: GeometryCache) -> None
unreal.MovieSceneGeometryCacheParams.play_rate(value: float) -> None
unreal.MovieSceneGeometryCacheParams.reverse(value: bool) -> None
unreal.MovieSceneGeometryCacheParams.start_frame_offset(value: FrameNumber) -> None
```

## `unreal.MovieSceneGeometryCacheSection(MovieSceneSection)`

```python
unreal.MovieSceneGeometryCacheSection.params(value: MovieSceneGeometryCacheParams) -> None
```

## `unreal.MovieSceneGeometryCacheSectionTemplateParameters(MovieSceneGeometryCacheParams)`

```python
unreal.MovieSceneGeometryCacheSectionTemplateParameters.__init__(geometry_cache_asset: GeometryCache = None, first_loop_start_frame_offset: FrameNumber = [0], start_frame_offset: FrameNumber = [0], end_frame_offset: FrameNumber = [0], play_rate: float = 0.000000, reverse: bool = False) -> None
```

## `unreal.MovieSceneGeometryCollectionParams(StructBase)`

```python
unreal.MovieSceneGeometryCollectionParams.__init__() -> None
```

## `unreal.NamedCurveValue(StructBase)`

```python
unreal.NamedCurveValue.__init__(name: Name = "None", value: float = 0.000000) -> None
unreal.NamedCurveValue.name(value: Name) -> None
unreal.NamedCurveValue.value(value: float) -> None
```

## `unreal.OnCameraUnderwaterStateChanged(MulticastDelegateBase)`

```python
unreal.OnCameraUnderwaterStateChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnGeometryCollectionFullyDecayedEvent(MulticastDelegateBase)`

```python
unreal.OnGeometryCollectionFullyDecayedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnGeometryCollectionRootMovedEvent(MulticastDelegateBase)`

```python
unreal.OnGeometryCollectionRootMovedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnPontoonEnteredWater(MulticastDelegateBase)`

```python
unreal.OnPontoonEnteredWater.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnPontoonExitedWater(MulticastDelegateBase)`

```python
unreal.OnPontoonExitedWater.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQueryWaterEntityIdCompleted(MulticastDelegateBase)`

```python
unreal.OnQueryWaterEntityIdCompleted.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnQueryWaterEntityTileIdCompleted(MulticastDelegateBase)`

```python
unreal.OnQueryWaterEntityTileIdCompleted.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnWaterScalabilityChanged(MulticastDelegateBase)`

```python
unreal.OnWaterScalabilityChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PCGAddAttributeSettings(PCGSettings)`

```python
unreal.PCGAddAttributeSettings.attribute_types(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGAddAttributeSettings.copy_all_attributes(value: bool) -> None
unreal.PCGAddAttributeSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAddAttributeSettings.output_target(value: PCGAttributePropertyOutputSelector) -> None
```

## `unreal.PCGAddComponentSettings(PCGSettings)`

```python
unreal.PCGAddComponentSettings.actor_reference_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAddComponentSettings.allow_template_component_editing(value: bool) -> None
unreal.PCGAddComponentSettings.class_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAddComponentSettings.component_reference_attribute(value: PCGAttributePropertyOutputNoSourceSelector) -> None
unreal.PCGAddComponentSettings.template_component(value: ActorComponent) -> None
unreal.PCGAddComponentSettings.template_component_class() -> Class
unreal.PCGAddComponentSettings.use_class_attribute(value: bool) -> None
```

## `unreal.PCGAddTagSettings(PCGSettings)`

```python
unreal.PCGAddTagSettings.ignore_tag_value_parsing(value: bool) -> None
unreal.PCGAddTagSettings.prefix(value: str) -> None
unreal.PCGAddTagSettings.suffix(value: str) -> None
unreal.PCGAddTagSettings.tags_to_add(value: str) -> None
```

## `unreal.PCGAppendMeshesFromPointsSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGAppendMeshesFromPointsSettings.extract_materials(value: bool) -> None
unreal.PCGAppendMeshesFromPointsSettings.mesh_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAppendMeshesFromPointsSettings.mode(value: PCGAppendMeshesFromPointsMode) -> None
unreal.PCGAppendMeshesFromPointsSettings.requested_lod_index(value: int) -> None
unreal.PCGAppendMeshesFromPointsSettings.requested_lod_type(value: GeometryScriptLODType) -> None
unreal.PCGAppendMeshesFromPointsSettings.static_mesh(value: StaticMesh) -> None
unreal.PCGAppendMeshesFromPointsSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGAssetExporter(Object)`

```python
unreal.PCGAssetExporter.bp_export_to_asset(asset: PCGDataAsset) -> bool
unreal.PCGAssetExporter.bp_get_asset_type() -> Class
```

## `unreal.PCGAssetExporterParameters(StructBase)`

```python
unreal.PCGAssetExporterParameters.__init__(open_save_dialog: bool = False, asset_name: str = "", asset_path: str = "", save_on_export_ended: bool = False) -> None
unreal.PCGAssetExporterParameters.asset_name(value: str) -> None
unreal.PCGAssetExporterParameters.asset_path(value: str) -> None
unreal.PCGAssetExporterParameters.open_save_dialog(value: bool) -> None
unreal.PCGAssetExporterParameters.save_on_export_ended(value: bool) -> None
```

## `unreal.PCGAssetExporterUtils(BlueprintFunctionLibrary)`

```python
unreal.PCGAssetExporterUtils.create_asset(exporter: PCGAssetExporter, parameters: PCGAssetExporterParameters = [True, "", "", True]) -> Package
unreal.PCGAssetExporterUtils.update_assets(pcg_assets: Array[AssetData], parameters: PCGAssetExporterParameters = [True, "", "", True]) -> None
```

## `unreal.PCGAttractSettings(PCGSettings)`

```python
unreal.PCGAttractSettings.attractor_index_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttractSettings.distance(value: float) -> None
unreal.PCGAttractSettings.mode(value: PCGAttractMode) -> None
unreal.PCGAttractSettings.output_attract_index(value: bool) -> None
unreal.PCGAttractSettings.output_attract_index_attribute(value: PCGAttributePropertyOutputNoSourceSelector) -> None
unreal.PCGAttractSettings.remove_unattracted_points(value: bool) -> None
unreal.PCGAttractSettings.source_and_target_attribute_mapping(value: Map[PCGAttributePropertyInputSelector, PCGAttributePropertyInputSelector]) -> None
unreal.PCGAttractSettings.source_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttractSettings.target_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttractSettings.target_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttractSettings.use_source_weight(value: bool) -> None
unreal.PCGAttractSettings.use_target_weight(value: bool) -> None
unreal.PCGAttractSettings.weight(value: float) -> None
```

## `unreal.PCGAttributeCastSettings(PCGSettings)`

```python
unreal.PCGAttributeCastSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeCastSettings.output_target(value: PCGAttributePropertyOutputSelector) -> None
unreal.PCGAttributeCastSettings.output_type(value: PCGMetadataTypes) -> None
```

## `unreal.PCGAttributeFilterThresholdSettings(StructBase)`

```python
unreal.PCGAttributeFilterThresholdSettings.__init__(inclusive: bool = False, use_constant_threshold: bool = False, threshold_attribute: PCGAttributePropertyInputSelector = [], use_spatial_query: bool = False, attribute_types: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]]) -> None
unreal.PCGAttributeFilterThresholdSettings.attribute_types(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGAttributeFilterThresholdSettings.inclusive(value: bool) -> None
unreal.PCGAttributeFilterThresholdSettings.threshold_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeFilterThresholdSettings.use_constant_threshold(value: bool) -> None
unreal.PCGAttributeFilterThresholdSettings.use_spatial_query(value: bool) -> None
```

## `unreal.PCGAttributeFilteringRangeSettings(PCGSettings)`

```python
unreal.PCGAttributeFilteringRangeSettings.max_threshold(value: PCGAttributeFilterThresholdSettings) -> None
unreal.PCGAttributeFilteringRangeSettings.min_threshold(value: PCGAttributeFilterThresholdSettings) -> None
unreal.PCGAttributeFilteringRangeSettings.target_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeFilteringRangeSettings.warn_on_data_missing_attribute(value: bool) -> None
```

## `unreal.PCGAttributeFilteringSettings(PCGSettings)`

```python
unreal.PCGAttributeFilteringSettings.attribute_types(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGAttributeFilteringSettings.operator(value: PCGAttributeFilterOperator) -> None
unreal.PCGAttributeFilteringSettings.target_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeFilteringSettings.threshold_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeFilteringSettings.use_constant_threshold(value: bool) -> None
unreal.PCGAttributeFilteringSettings.use_spatial_query(value: bool) -> None
unreal.PCGAttributeFilteringSettings.warn_on_data_missing_attribute(value: bool) -> None
```

## `unreal.PCGAttributeGetFromIndexSettings(PCGSettings)`

```python
unreal.PCGAttributeGetFromIndexSettings.index(value: int) -> None
```

## `unreal.PCGAttributeGetFromPointIndexSettings(PCGSettings)`

```python
unreal.PCGAttributeGetFromPointIndexSettings.index(value: int) -> None
unreal.PCGAttributeGetFromPointIndexSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeGetFromPointIndexSettings.output_attribute_name(value: Name) -> None
```

## `unreal.PCGAttributeNoiseSettings(PCGSettings)`

```python
unreal.PCGAttributeNoiseSettings.clamp_result(value: bool) -> None
unreal.PCGAttributeNoiseSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeNoiseSettings.invert_source(value: bool) -> None
unreal.PCGAttributeNoiseSettings.mode(value: PCGAttributeNoiseMode) -> None
unreal.PCGAttributeNoiseSettings.noise_max(value: float) -> None
unreal.PCGAttributeNoiseSettings.noise_min(value: float) -> None
unreal.PCGAttributeNoiseSettings.output_target(value: PCGAttributePropertyOutputSelector) -> None
```

## `unreal.PCGAttributePropertyInputSelector(PCGAttributePropertySelector)`

```python
unreal.PCGAttributePropertyInputSelector.__init__() -> None
unreal.PCGAttributePropertyInputSelector.copy_and_fix_last(data: PCGData) -> PCGAttributePropertyInputSelector
```

## `unreal.PCGAttributePropertyOutputNoSourceSelector(PCGAttributePropertySelector)`

```python
unreal.PCGAttributePropertyOutputNoSourceSelector.__init__() -> None
```

## `unreal.PCGAttributePropertyOutputSelector(PCGAttributePropertySelector)`

```python
unreal.PCGAttributePropertyOutputSelector.__init__() -> None
unreal.PCGAttributePropertyOutputSelector.copy_and_fix_source(input_selector: PCGAttributePropertyInputSelector) -> PCGAttributePropertyOutputSelector
```

## `unreal.PCGAttributePropertySelector(StructBase)`

```python
unreal.PCGAttributePropertySelector.__init__() -> None
unreal.PCGAttributePropertySelector.get_attribute_name() -> Name
unreal.PCGAttributePropertySelector.get_extra_names() -> Array[str]
unreal.PCGAttributePropertySelector.get_extra_property() -> PCGExtraProperties
unreal.PCGAttributePropertySelector.get_name() -> Name
unreal.PCGAttributePropertySelector.get_point_property() -> PCGPointProperties
unreal.PCGAttributePropertySelector.get_selection() -> PCGAttributePropertySelection
unreal.PCGAttributePropertySelector.set_attribute_name(attribute_name: Name) -> bool
unreal.PCGAttributePropertySelector.set_extra_property(extra_property: PCGExtraProperties) -> bool
unreal.PCGAttributePropertySelector.set_point_property(point_property: PCGPointProperties) -> bool
```

## `unreal.PCGAttributeReduceSettings(PCGSettings)`

```python
unreal.PCGAttributeReduceSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeReduceSettings.join_delimiter(value: str) -> None
unreal.PCGAttributeReduceSettings.merge_output_attributes(value: bool) -> None
unreal.PCGAttributeReduceSettings.operation(value: PCGAttributeReduceOperation) -> None
unreal.PCGAttributeReduceSettings.output_attribute_name(value: Name) -> None
```

## `unreal.PCGAttributeRemapSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGAttributeRemapSettings.allow_inverse_range(value: bool) -> None
unreal.PCGAttributeRemapSettings.clamp_to_unit_range(value: bool) -> None
unreal.PCGAttributeRemapSettings.ignore_values_outside_input_range(value: bool) -> None
unreal.PCGAttributeRemapSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeRemapSettings.out_range_max(value: float) -> None
unreal.PCGAttributeRemapSettings.out_range_min(value: float) -> None
unreal.PCGAttributeRemapSettings.range_max(value: float) -> None
unreal.PCGAttributeRemapSettings.range_min(value: float) -> None
```

## `unreal.PCGAttributeRemoveDuplicatesSettings(PCGSettings)`

```python
unreal.PCGAttributeRemoveDuplicatesSettings.attribute_selectors(value: Array[PCGAttributePropertyInputSelector]) -> None
```

## `unreal.PCGAttributeSelectSettings(PCGSettings)`

```python
unreal.PCGAttributeSelectSettings.axis(value: PCGAttributeSelectAxis) -> None
unreal.PCGAttributeSelectSettings.custom_axis(value: Vector4) -> None
unreal.PCGAttributeSelectSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGAttributeSelectSettings.operation(value: PCGAttributeSelectOperation) -> None
unreal.PCGAttributeSelectSettings.output_attribute_name(value: Name) -> None
```

## `unreal.PCGBlurSettings(PCGSettings)`

```python
unreal.PCGBlurSettings.blur_mode(value: PCGBlurElementMode) -> None
unreal.PCGBlurSettings.custom_standard_deviation(value: float) -> None
unreal.PCGBlurSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGBlurSettings.num_iterations(value: int) -> None
unreal.PCGBlurSettings.output_target(value: PCGAttributePropertyOutputSelector) -> None
unreal.PCGBlurSettings.search_distance(value: float) -> None
unreal.PCGBlurSettings.use_custom_standard_deviation(value: bool) -> None
```

## `unreal.PCGBooleanOperationSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGBooleanOperationSettings.boolean_operation(value: GeometryScriptBooleanOperation) -> None
unreal.PCGBooleanOperationSettings.boolean_operation_options(value: GeometryScriptMeshBooleanOptions) -> None
unreal.PCGBooleanOperationSettings.mode(value: PCGBooleanOperationMode) -> None
unreal.PCGBooleanOperationSettings.tag_inheritance_mode(value: PCGBooleanOperationTagInheritanceMode) -> None
```

## `unreal.PCGBooleanSelectSettings(PCGSettings)`

```python
unreal.PCGBooleanSelectSettings.use_input_b(value: bool) -> None
```

## `unreal.PCGBoundsFromMeshSettings(PCGSettings)`

```python
unreal.PCGBoundsFromMeshSettings.mesh_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGBoundsFromMeshSettings.silence_attribute_not_found_errors(value: bool) -> None
unreal.PCGBoundsFromMeshSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGBoundsModifierSettings(PCGSettings)`

```python
unreal.PCGBoundsModifierSettings.affect_steepness(value: bool) -> None
unreal.PCGBoundsModifierSettings.bounds_max(value: Vector) -> None
unreal.PCGBoundsModifierSettings.bounds_min(value: Vector) -> None
unreal.PCGBoundsModifierSettings.mode(value: PCGBoundsModifierMode) -> None
unreal.PCGBoundsModifierSettings.steepness(value: float) -> None
```

## `unreal.PCGBranchSettings(PCGSettings)`

```python
unreal.PCGBranchSettings.output_to_b(value: bool) -> None
```

## `unreal.PCGCleanSplineSettings(PCGSettings)`

```python
unreal.PCGCleanSplineSettings.collinear_angle_threshold(value: float) -> None
unreal.PCGCleanSplineSettings.colocation_distance_threshold(value: float) -> None
unreal.PCGCleanSplineSettings.fuse_colocated_control_points(value: bool) -> None
unreal.PCGCleanSplineSettings.fuse_mode(value: PCGControlPointFuseMode) -> None
unreal.PCGCleanSplineSettings.remove_collinear_control_points(value: bool) -> None
unreal.PCGCleanSplineSettings.use_radians(value: bool) -> None
unreal.PCGCleanSplineSettings.use_spline_local_space(value: bool) -> None
```

## `unreal.PCGClusterSettings(PCGSettings)`

```python
unreal.PCGClusterSettings.algorithm(value: PCGClusterAlgorithm) -> None
unreal.PCGClusterSettings.cluster_attribute(value: Name) -> None
unreal.PCGClusterSettings.max_iterations(value: int) -> None
unreal.PCGClusterSettings.num_clusters(value: int) -> None
unreal.PCGClusterSettings.output_final_centroids(value: bool) -> None
unreal.PCGClusterSettings.tolerance(value: float) -> None
```

## `unreal.PCGCollapsePointsSettings(PCGSettings)`

```python
unreal.PCGCollapsePointsSettings.attributes_to_merge(value: Array[PCGAttributePropertyOutputNoSourceSelector]) -> None
unreal.PCGCollapsePointsSettings.comparison_mode(value: PCGCollapseComparisonMode) -> None
unreal.PCGCollapsePointsSettings.distance_threshold(value: float) -> None
unreal.PCGCollapsePointsSettings.merge_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGCollapsePointsSettings.mode(value: PCGCollapseMode) -> None
unreal.PCGCollapsePointsSettings.use_merge_weight_attribute(value: bool) -> None
unreal.PCGCollapsePointsSettings.visit_order(value: PCGCollapseVisitOrder) -> None
unreal.PCGCollapsePointsSettings.visit_order_attribute(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGCombinePointsSettings(PCGSettings)`

```python
unreal.PCGCombinePointsSettings.center_pivot(value: bool) -> None
unreal.PCGCombinePointsSettings.point_transform(value: Transform) -> None
unreal.PCGCombinePointsSettings.use_first_point_transform(value: bool) -> None
```

## `unreal.PCGComponent(ActorComponent)`

```python
unreal.PCGComponent.activated(value: bool) -> None
unreal.PCGComponent.add_actors_to_managed_resources(actors: Array[Actor]) -> None
unreal.PCGComponent.add_components_to_managed_resources(components: Array[ActorComponent]) -> None
unreal.PCGComponent.add_to_managed_resources(resource: PCGManagedResource) -> None
unreal.PCGComponent.cleanup(remove_components: bool, save: bool = False) -> None
unreal.PCGComponent.cleanup_local(remove_components: bool, save: bool = False) -> None
unreal.PCGComponent.clear_pcg_link(template_actor: Class = None) -> Actor
unreal.PCGComponent.dirty_generated() -> bool
unreal.PCGComponent.generate(force: bool) -> None
unreal.PCGComponent.generate_local(force: bool) -> None
unreal.PCGComponent.generate_on_drop_when_trigger_on_demand() -> bool
unreal.PCGComponent.generated() -> bool
unreal.PCGComponent.generation_radii(value: PCGRuntimeGenerationRadii) -> None
unreal.PCGComponent.generation_trigger() -> PCGComponentGenerationTrigger
unreal.PCGComponent.get_editing_mode() -> PCGEditorDirtyMode
unreal.PCGComponent.get_generated_graph_output() -> PCGDataCollection
unreal.PCGComponent.get_serialized_editing_mode() -> PCGEditorDirtyMode
unreal.PCGComponent.graph_instance() -> PCGGraphInstance
unreal.PCGComponent.ignore_landscape_tracking(value: bool) -> None
unreal.PCGComponent.input_type(value: PCGComponentInput) -> None
unreal.PCGComponent.is_component_partitioned(value: bool) -> None
unreal.PCGComponent.notify_properties_changed_from_blueprint() -> None
unreal.PCGComponent.on_pcg_graph_cancelled_external(value: OnPCGGraphCancelledExternal) -> None
unreal.PCGComponent.on_pcg_graph_cleaned_external(value: OnPCGGraphCleanedExternal) -> None
unreal.PCGComponent.on_pcg_graph_generated_external(value: OnPCGGraphGeneratedExternal) -> None
unreal.PCGComponent.on_pcg_graph_start_generating_external(value: OnPCGGraphStartGeneratingExternal) -> None
unreal.PCGComponent.only_track_itself(value: bool) -> None
unreal.PCGComponent.override_generation_radii(value: bool) -> None
unreal.PCGComponent.parse_actor_components(value: bool) -> None
unreal.PCGComponent.post_generate_function_names(value: Array[Name]) -> None
unreal.PCGComponent.refresh_pcg_runtime_component(flush_cache: bool = False) -> None
unreal.PCGComponent.regenerate_in_editor(value: bool) -> None
unreal.PCGComponent.scheduling_policy() -> PCGSchedulingPolicyBase
unreal.PCGComponent.scheduling_policy_class() -> Class
unreal.PCGComponent.seed(value: int) -> None
unreal.PCGComponent.set_editing_mode(editing_mode: PCGEditorDirtyMode, serialized_editing_mode: PCGEditorDirtyMode) -> None
unreal.PCGComponent.set_graph(graph: PCGGraphInterface) -> None
```

## `unreal.PCGComponentSelectorSettings(StructBase)`

```python
unreal.PCGComponentSelectorSettings.__init__(component_selection: PCGComponentSelection = PCGComponentSelection.BY_TAG, component_selection_tag: Name = "None", component_selection_class: Class = None) -> None
unreal.PCGComponentSelectorSettings.component_selection(value: PCGComponentSelection) -> None
unreal.PCGComponentSelectorSettings.component_selection_class(value: Class) -> None
unreal.PCGComponentSelectorSettings.component_selection_tag(value: Name) -> None
```

## `unreal.PCGContext(StructBase)`

```python
unreal.PCGContext.__init__() -> None
unreal.PCGContext.get_actor_data() -> PCGData
unreal.PCGContext.get_component() -> PCGComponent
unreal.PCGContext.get_input_data() -> PCGData
unreal.PCGContext.get_original_component() -> PCGComponent
unreal.PCGContext.get_settings() -> PCGSettings
unreal.PCGContext.get_target_actor(spatial_data: PCGSpatialData) -> Actor
unreal.PCGContext.get_task_id() -> int
```

## `unreal.PCGCopyAttributesSettings(PCGSettings)`

```python
unreal.PCGCopyAttributesSettings.copy_all_attributes(value: bool) -> None
unreal.PCGCopyAttributesSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGCopyAttributesSettings.operation(value: PCGCopyAttributesOperation) -> None
unreal.PCGCopyAttributesSettings.output_target(value: PCGAttributePropertyOutputSelector) -> None
```

## `unreal.PCGCopyPointsSettings(PCGSettings)`

```python
unreal.PCGCopyPointsSettings.attribute_inheritance(value: PCGCopyPointsMetadataInheritanceMode) -> None
unreal.PCGCopyPointsSettings.color_inheritance(value: PCGCopyPointsInheritanceMode) -> None
unreal.PCGCopyPointsSettings.copy_each_source_on_every_target(value: bool) -> None
unreal.PCGCopyPointsSettings.rotation_inheritance(value: PCGCopyPointsInheritanceMode) -> None
unreal.PCGCopyPointsSettings.scale_inheritance(value: PCGCopyPointsInheritanceMode) -> None
unreal.PCGCopyPointsSettings.seed_inheritance(value: PCGCopyPointsInheritanceMode) -> None
unreal.PCGCopyPointsSettings.tag_inheritance(value: PCGCopyPointsTagInheritanceMode) -> None
```

## `unreal.PCGCrc(StructBase)`

```python
unreal.PCGCrc.__init__() -> None
```

## `unreal.PCGCreateAttributeSetSettings(PCGSettings)`

```python
unreal.PCGCreateAttributeSetSettings.attribute_types(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGCreateAttributeSetSettings.output_target(value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

## `unreal.PCGCreatePointsGridSettings(PCGSettings)`

```python
unreal.PCGCreatePointsGridSettings.cell_size(value: Vector) -> None
unreal.PCGCreatePointsGridSettings.coordinate_space(value: PCGCoordinateSpace) -> None
unreal.PCGCreatePointsGridSettings.cull_points_outside_volume(value: bool) -> None
unreal.PCGCreatePointsGridSettings.grid_extents(value: Vector) -> None
unreal.PCGCreatePointsGridSettings.point_position(value: PCGPointPosition) -> None
unreal.PCGCreatePointsGridSettings.point_steepness(value: float) -> None
unreal.PCGCreatePointsGridSettings.set_points_bounds(value: bool) -> None
```

## `unreal.PCGCreatePointsSettings(PCGSettings)`

```python
unreal.PCGCreatePointsSettings.coordinate_space(value: PCGCoordinateSpace) -> None
unreal.PCGCreatePointsSettings.cull_points_outside_volume(value: bool) -> None
unreal.PCGCreatePointsSettings.points_to_create(value: Array[PCGPoint]) -> None
```

## `unreal.PCGCreatePointsSphereSettings(PCGSettings)`

```python
unreal.PCGCreatePointsSphereSettings.coordinate_space(value: PCGCoordinateSpace) -> None
unreal.PCGCreatePointsSphereSettings.cull_points_outside_volume(value: bool) -> None
unreal.PCGCreatePointsSphereSettings.geodesic_subdivisions(value: int) -> None
unreal.PCGCreatePointsSphereSettings.jitter(value: float) -> None
unreal.PCGCreatePointsSphereSettings.latitudinal_end_angle(value: float) -> None
unreal.PCGCreatePointsSphereSettings.latitudinal_segments(value: int) -> None
unreal.PCGCreatePointsSphereSettings.latitudinal_start_angle(value: float) -> None
unreal.PCGCreatePointsSphereSettings.longitudinal_end_angle(value: float) -> None
unreal.PCGCreatePointsSphereSettings.longitudinal_segments(value: int) -> None
unreal.PCGCreatePointsSphereSettings.longitudinal_start_angle(value: float) -> None
unreal.PCGCreatePointsSphereSettings.origin(value: Vector) -> None
unreal.PCGCreatePointsSphereSettings.phi(value: float) -> None
unreal.PCGCreatePointsSphereSettings.point_orientation(value: PCGSpherePointOrientation) -> None
unreal.PCGCreatePointsSphereSettings.point_steepness(value: float) -> None
unreal.PCGCreatePointsSphereSettings.poisson_distance(value: float) -> None
unreal.PCGCreatePointsSphereSettings.poisson_max_attempts(value: int) -> None
unreal.PCGCreatePointsSphereSettings.radius(value: float) -> None
unreal.PCGCreatePointsSphereSettings.sample_count(value: int) -> None
unreal.PCGCreatePointsSphereSettings.sphere_generation(value: PCGSphereGeneration) -> None
unreal.PCGCreatePointsSphereSettings.theta(value: float) -> None
```

## `unreal.PCGCreateSplineSettings(PCGSettings)`

```python
unreal.PCGCreateSplineSettings.apply_custom_tangents(value: bool) -> None
unreal.PCGCreateSplineSettings.arrive_tangent_attribute(value: Name) -> None
unreal.PCGCreateSplineSettings.closed_loop(value: bool) -> None
unreal.PCGCreateSplineSettings.leave_tangent_attribute(value: Name) -> None
unreal.PCGCreateSplineSettings.linear(value: bool) -> None
unreal.PCGCreateSplineSettings.mode(value: PCGCreateSplineMode) -> None
unreal.PCGCreateSplineSettings.post_process_function_names(value: Array[Name]) -> None
```

## `unreal.PCGData(Object)`

```python
unreal.PCGData.duplicate_data(context: PCGContext, initialize_metadata: bool = True) -> Tuple[PCGData, PCGContext]
```

## `unreal.PCGDataAsset(Object)`

```python
unreal.PCGDataAsset.category(value: Text) -> None
unreal.PCGDataAsset.color(value: LinearColor) -> None
unreal.PCGDataAsset.data() -> PCGDataCollection
unreal.PCGDataAsset.description(value: Text) -> None
unreal.PCGDataAsset.exporter_class() -> Class
unreal.PCGDataAsset.expose_to_library(value: bool) -> None
unreal.PCGDataAsset.name(value: str) -> None
unreal.PCGDataAsset.object_path() -> SoftObjectPath
unreal.PCGDataAsset.settings_class() -> Class
```

## `unreal.PCGDataCollection(StructBase)`

```python
unreal.PCGDataCollection.__init__(tagged_data: Array[PCGTaggedData] = [], cancel_execution_on_empty: bool = False) -> None
unreal.PCGDataCollection.add_to_collection(data: PCGData, pin_label: Name, tags: Array[str]) -> None
unreal.PCGDataCollection.cancel_execution_on_empty(value: bool) -> None
unreal.PCGDataCollection.get_typed_inputs(data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataCollection.get_typed_inputs_by_pin(pin: PCGPinProperties, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataCollection.get_typed_inputs_by_pin_label(pin_label: Name, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataCollection.get_typed_inputs_by_tag(tag: str, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataCollection.tagged_data(value: Array[PCGTaggedData]) -> None
```

## `unreal.PCGDataCollectionExporter(PCGAssetExporter)`

```python
unreal.PCGDataCollectionExporter.asset_color() -> LinearColor
unreal.PCGDataCollectionExporter.asset_description() -> str
unreal.PCGDataCollectionExporter.data() -> PCGDataCollection
```

## `unreal.PCGDataFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.PCGDataFunctionLibrary.add_to_collection(collection: PCGDataCollection, data: PCGData, pin_label: Name, tags: Array[str]) -> PCGDataCollection
unreal.PCGDataFunctionLibrary.get_all_settings(collection: PCGDataCollection) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_inputs(collection: PCGDataCollection) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_inputs_by_pin(collection: PCGDataCollection, pin_label: Name) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_inputs_by_pin_label(collection: PCGDataCollection, pin_label: Name) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_inputs_by_tag(collection: PCGDataCollection, tag: str) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_params(collection: PCGDataCollection) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_params_by_pin(collection: PCGDataCollection, pin_label: Name) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_params_by_pin_label(collection: PCGDataCollection, pin_label: Name) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_params_by_tag(collection: PCGDataCollection, tag: str) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_tagged_inputs(collection: PCGDataCollection, tag: str) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_tagged_params(collection: PCGDataCollection, tag: str) -> Array[PCGTaggedData]
unreal.PCGDataFunctionLibrary.get_typed_inputs(collection: PCGDataCollection, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataFunctionLibrary.get_typed_inputs_by_pin(collection: PCGDataCollection, pin: PCGPinProperties, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataFunctionLibrary.get_typed_inputs_by_pin_label(collection: PCGDataCollection, pin_label: Name, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
unreal.PCGDataFunctionLibrary.get_typed_inputs_by_tag(collection: PCGDataCollection, tag: str, data_type_class: Class = None) -> Tuple[Array[PCGData], Array[PCGTaggedData]]
```

## `unreal.PCGDataNumSettings(PCGSettings)`

```python
unreal.PCGDataNumSettings.output_attribute_name(value: Name) -> None
```

## `unreal.PCGDebugSettings(PCGSettings)`

```python
unreal.PCGDebugSettings.target_actor(value: Actor) -> None
```

## `unreal.PCGDebugVisualizationSettings(StructBase)`

```python
unreal.PCGDebugVisualizationSettings.__init__(point_scale: float = 0.000000, scale_method: PCGDebugVisScaleMethod = PCGDebugVisScaleMethod.RELATIVE, point_mesh: StaticMesh = None, material_override: MaterialInterface = None) -> None
unreal.PCGDebugVisualizationSettings.material_override(value: MaterialInterface) -> None
unreal.PCGDebugVisualizationSettings.point_mesh(value: StaticMesh) -> None
unreal.PCGDebugVisualizationSettings.point_scale(value: float) -> None
unreal.PCGDebugVisualizationSettings.scale_method(value: PCGDebugVisScaleMethod) -> None
```

## `unreal.PCGDeleteAttributesSettings(PCGSettings)`

```python
unreal.PCGDeleteAttributesSettings.operation(value: PCGAttributeFilterOperation) -> None
unreal.PCGDeleteAttributesSettings.operator(value: PCGStringMatchingOperator) -> None
unreal.PCGDeleteAttributesSettings.selected_attributes(value: str) -> None
```

## `unreal.PCGDeleteTagsSettings(PCGSettings)`

```python
unreal.PCGDeleteTagsSettings.operation(value: PCGTagFilterOperation) -> None
unreal.PCGDeleteTagsSettings.operator(value: PCGStringMatchingOperator) -> None
unreal.PCGDeleteTagsSettings.selected_tags(value: str) -> None
```

## `unreal.PCGDensityFilterSettings(PCGSettings)`

```python
unreal.PCGDensityFilterSettings.invert_filter(value: bool) -> None
unreal.PCGDensityFilterSettings.keep_zero_density_points(value: bool) -> None
unreal.PCGDensityFilterSettings.lower_bound(value: float) -> None
unreal.PCGDensityFilterSettings.upper_bound(value: float) -> None
```

## `unreal.PCGDensityRemapSettings(PCGSettings)`

```python
unreal.PCGDensityRemapSettings.exclude_values_outside_input_range(value: bool) -> None
unreal.PCGDensityRemapSettings.out_range_max(value: float) -> None
unreal.PCGDensityRemapSettings.out_range_min(value: float) -> None
unreal.PCGDensityRemapSettings.range_max(value: float) -> None
unreal.PCGDensityRemapSettings.range_min(value: float) -> None
```

## `unreal.PCGDeterminismSettings(StructBase)`

```python
unreal.PCGDeterminismSettings.__init__(native_tests: bool = False, use_blueprint_determinism_test: bool = False, determinism_test_blueprint: Class = None) -> None
unreal.PCGDeterminismSettings.determinism_test_blueprint() -> Class
unreal.PCGDeterminismSettings.native_tests(value: bool) -> None
unreal.PCGDeterminismSettings.use_blueprint_determinism_test(value: bool) -> None
```

## `unreal.PCGDifferenceData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGDifferenceData.add_difference(difference: PCGSpatialData) -> None
unreal.PCGDifferenceData.density_function(value: PCGDifferenceDensityFunction) -> None
unreal.PCGDifferenceData.diff_metadata() -> bool
unreal.PCGDifferenceData.difference() -> PCGSpatialData
unreal.PCGDifferenceData.initialize(data: PCGSpatialData) -> None
unreal.PCGDifferenceData.k2_add_difference(difference: PCGSpatialData) -> None
unreal.PCGDifferenceData.set_density_function(density_function: PCGDifferenceDensityFunction) -> None
unreal.PCGDifferenceData.source() -> PCGSpatialData
```

## `unreal.PCGDifferenceSettings(PCGSettings)`

```python
unreal.PCGDifferenceSettings.density_function(value: PCGDifferenceDensityFunction) -> None
unreal.PCGDifferenceSettings.diff_metadata(value: bool) -> None
unreal.PCGDifferenceSettings.keep_zero_density_points(value: bool) -> None
unreal.PCGDifferenceSettings.mode(value: PCGDifferenceMode) -> None
```

## `unreal.PCGDistanceSettings(PCGSettings)`

```python
unreal.PCGDistanceSettings.attribute_name(value: Name) -> None
unreal.PCGDistanceSettings.check_source_against_respective_target(value: bool) -> None
unreal.PCGDistanceSettings.maximum_distance(value: float) -> None
unreal.PCGDistanceSettings.output_attribute(value: PCGAttributePropertySelector) -> None
unreal.PCGDistanceSettings.output_distance_vector(value: bool) -> None
unreal.PCGDistanceSettings.output_to_attribute(value: bool) -> None
unreal.PCGDistanceSettings.set_density(value: bool) -> None
unreal.PCGDistanceSettings.source_shape(value: PCGDistanceShape) -> None
unreal.PCGDistanceSettings.target_shape(value: PCGDistanceShape) -> None
```

## `unreal.PCGDummyGetPropertyStruct(StructBase)`

```python
unreal.PCGDummyGetPropertyStruct.__init__(int_array_property: Array[int] = [], float_property: float = 0.000000, level2_struct: PCGDummyGetPropertyLevel2Struct = [[]]) -> None
unreal.PCGDummyGetPropertyStruct.float_property() -> float
unreal.PCGDummyGetPropertyStruct.int_array_property() -> Array[int]
unreal.PCGDummyGetPropertyStruct.level2_struct() -> PCGDummyGetPropertyLevel2Struct
```

## `unreal.PCGDummyGetPropertyTest(Object)`

```python
unreal.PCGDummyGetPropertyTest.double_property() -> float
unreal.PCGDummyGetPropertyTest.int64_property() -> int
```

## `unreal.PCGDuplicateCrossSectionsSettings(PCGSubdivisionBaseSettings)`

```python
unreal.PCGDuplicateCrossSectionsSettings.extrude_vector(value: Vector) -> None
unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_as_attribute(value: bool) -> None
unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGDuplicateCrossSectionsSettings.output_spline_index_attribute(value: bool) -> None
unreal.PCGDuplicateCrossSectionsSettings.spline_index_attribute_name(value: Name) -> None
```

## `unreal.PCGDuplicatePointSettings(PCGSettings)`

```python
unreal.PCGDuplicatePointSettings.direction(value: Vector) -> None
unreal.PCGDuplicatePointSettings.direction_applied_in_relative_space(value: bool) -> None
unreal.PCGDuplicatePointSettings.iterations(value: int) -> None
unreal.PCGDuplicatePointSettings.output_source_point(value: bool) -> None
unreal.PCGDuplicatePointSettings.point_transform(value: Transform) -> None
```

## `unreal.PCGDynamicMeshData(PCGSpatialData)`

```python
unreal.PCGDynamicMeshData.dynamic_mesh() -> DynamicMesh
unreal.PCGDynamicMeshData.k2_initialize(mesh: DynamicMesh, materials: Array[MaterialInterface], can_take_ownership: bool = False) -> None
unreal.PCGDynamicMeshData.materials() -> Array[MaterialInterface]
unreal.PCGDynamicMeshData.set_materials(materials: Array[MaterialInterface]) -> None
```

## `unreal.PCGElevationIsolinesSettings(PCGSettings)`

```python
unreal.PCGElevationIsolinesSettings.add_tag_on_output_for_same_elevation(value: bool) -> None
unreal.PCGElevationIsolinesSettings.elevation_end(value: float) -> None
unreal.PCGElevationIsolinesSettings.elevation_increment(value: float) -> None
unreal.PCGElevationIsolinesSettings.elevation_start(value: float) -> None
unreal.PCGElevationIsolinesSettings.linear_spline(value: bool) -> None
unreal.PCGElevationIsolinesSettings.output_as_spline(value: bool) -> None
unreal.PCGElevationIsolinesSettings.project_surface_normal(value: bool) -> None
unreal.PCGElevationIsolinesSettings.resolution(value: float) -> None
```

## `unreal.PCGExternalDataSettings(PCGSettings)`

```python
unreal.PCGExternalDataSettings.attribute_mapping(value: Map[str, PCGAttributePropertyInputSelector]) -> None
```

## `unreal.PCGFilterByAttributeSettings(PCGFilterDataBaseSettings)`

```python
unreal.PCGFilterByAttributeSettings.attribute(value: Name) -> None
unreal.PCGFilterByAttributeSettings.ignore_properties(value: bool) -> None
unreal.PCGFilterByAttributeSettings.operator(value: PCGStringMatchingOperator) -> None
```

## `unreal.PCGFilterByIndexSettings(PCGFilterDataBaseSettings)`

```python
unreal.PCGFilterByIndexSettings.invert_filter(value: bool) -> None
unreal.PCGFilterByIndexSettings.selected_indices(value: str) -> None
```

## `unreal.PCGFilterByTagSettings(PCGFilterDataBaseSettings)`

```python
unreal.PCGFilterByTagSettings.operation(value: PCGFilterByTagOperation) -> None
unreal.PCGFilterByTagSettings.operator(value: PCGStringMatchingOperator) -> None
unreal.PCGFilterByTagSettings.selected_tags(value: str) -> None
```

## `unreal.PCGFilterByTypeSettings(PCGFilterDataBaseSettings)`

```python
unreal.PCGFilterByTypeSettings.show_outside_filter(value: bool) -> None
unreal.PCGFilterByTypeSettings.target_type(value: PCGDataType) -> None
```

## `unreal.PCGFilterElementsByIndexSettings(PCGSettings)`

```python
unreal.PCGFilterElementsByIndexSettings.index_selection_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGFilterElementsByIndexSettings.invert_filter(value: bool) -> None
unreal.PCGFilterElementsByIndexSettings.output_discarded_elements(value: bool) -> None
unreal.PCGFilterElementsByIndexSettings.select_indices_by_input(value: bool) -> None
unreal.PCGFilterElementsByIndexSettings.selected_indices(value: str) -> None
```

## `unreal.PCGGenericUserParameterGetSettings(PCGSettings)`

```python
unreal.PCGGenericUserParameterGetSettings.force_object_and_struct_extraction(value: bool) -> None
unreal.PCGGenericUserParameterGetSettings.output_attribute_name(value: Name) -> None
unreal.PCGGenericUserParameterGetSettings.property_path(value: str) -> None
unreal.PCGGenericUserParameterGetSettings.quiet(value: bool) -> None
unreal.PCGGenericUserParameterGetSettings.source(value: PCGUserParameterSource) -> None
```

## `unreal.PCGGetAttributesSettings(PCGSettings)`

```python
unreal.PCGGetAttributesSettings.get_default_value(value: bool) -> None
unreal.PCGGetAttributesSettings.get_type(value: bool) -> None
```

## `unreal.PCGGetDynamicMeshDataSettings(PCGDataFromActorSettings)`

```python
unreal.PCGGetDynamicMeshDataSettings.options(value: GeometryScriptCopyMeshFromComponentOptions) -> None
```

## `unreal.PCGGetLandscapeSettings(PCGDataFromActorSettings)`

```python
unreal.PCGGetLandscapeSettings.sampling_properties(value: PCGLandscapeDataProps) -> None
```

## `unreal.PCGGetPropertyFromObjectPathSettings(PCGSettings)`

```python
unreal.PCGGetPropertyFromObjectPathSettings.force_object_and_struct_extraction(value: bool) -> None
unreal.PCGGetPropertyFromObjectPathSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGGetPropertyFromObjectPathSettings.object_paths_to_extract(value: Array[SoftObjectPath]) -> None
unreal.PCGGetPropertyFromObjectPathSettings.output_attribute_name(value: Name) -> None
unreal.PCGGetPropertyFromObjectPathSettings.persist_all_data(value: bool) -> None
unreal.PCGGetPropertyFromObjectPathSettings.property_name(value: Name) -> None
unreal.PCGGetPropertyFromObjectPathSettings.silence_error_on_empty_object_path(value: bool) -> None
unreal.PCGGetPropertyFromObjectPathSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGGetTagsSettings(PCGSettings)`

```python
unreal.PCGGetTagsSettings.extract_tag_values(value: bool) -> None
```

## `unreal.PCGGrammarSelection(StructBase)`

```python
unreal.PCGGrammarSelection.__init__(grammar_as_attribute: bool = False, grammar_string: str = "", grammar_attribute: PCGAttributePropertyInputSelector = []) -> None
unreal.PCGGrammarSelection.grammar_as_attribute(value: bool) -> None
unreal.PCGGrammarSelection.grammar_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGGrammarSelection.grammar_string(value: str) -> None
```

## `unreal.PCGHiGenGridSizeSettings(PCGSettings)`

```python
unreal.PCGHiGenGridSizeSettings.hi_gen_grid_size(value: PCGHiGenGrid) -> None
```

## `unreal.PCGIndirectionSettings(PCGSettings)`

```python
unreal.PCGIndirectionSettings.proxy_interface_mode(value: PCGProxyInterfaceMode) -> None
unreal.PCGIndirectionSettings.settings(value: PCGSettings) -> None
unreal.PCGIndirectionSettings.tag_outputs_based_on_output_pins(value: bool) -> None
```

## `unreal.PCGInnerIntersectionSettings(PCGSettings)`

```python
unreal.PCGInnerIntersectionSettings.density_function(value: PCGIntersectionDensityFunction) -> None
unreal.PCGInnerIntersectionSettings.keep_zero_density_points(value: bool) -> None
```

## `unreal.PCGInstanceDataPackerBase(Object)`

```python
unreal.PCGInstanceDataPackerBase.add_type_to_packing(type_id: int) -> Optional[PCGPackedCustomData]
unreal.PCGInstanceDataPackerBase.pack_custom_data_from_attributes(instance_list: PCGMeshInstanceList, metadata: PCGMetadata, attribute_names: Array[Name]) -> PCGPackedCustomData
unreal.PCGInstanceDataPackerBase.pack_instances(spatial_data: PCGSpatialData, instance_list: PCGMeshInstanceList) -> Tuple[PCGContext, PCGPackedCustomData]
```

## `unreal.PCGInstanceDataPackerByAttribute(PCGInstanceDataPackerBase)`

```python
unreal.PCGInstanceDataPackerByAttribute.attribute_names(value: Array[Name]) -> None
unreal.PCGInstanceDataPackerByAttribute.attribute_selectors(value: Array[PCGAttributePropertyInputSelector]) -> None
```

## `unreal.PCGInstanceDataPackerByRegex(PCGInstanceDataPackerBase)`

```python
unreal.PCGInstanceDataPackerByRegex.regex_patterns(value: Array[str]) -> None
```

## `unreal.PCGIntersectionData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGIntersectionData.a() -> PCGSpatialData
unreal.PCGIntersectionData.b() -> PCGSpatialData
unreal.PCGIntersectionData.density_function(value: PCGIntersectionDensityFunction) -> None
unreal.PCGIntersectionData.initialize(a: PCGSpatialData, b: PCGSpatialData) -> None
```

## `unreal.PCGKernelAttributeKey(StructBase)`

```python
unreal.PCGKernelAttributeKey.__init__() -> None
```

## `unreal.PCGLandscapeCache(Object)`

```python
unreal.PCGLandscapeCache.cache_entry_count() -> int
unreal.PCGLandscapeCache.cooked_serialized_contents(value: PCGLandscapeCacheSerializationContents) -> None
unreal.PCGLandscapeCache.serialization_mode(value: PCGLandscapeCacheSerializationMode) -> None
```

## `unreal.PCGLandscapeData(PCGSurfaceData)`

```python
unreal.PCGLandscapeData.landscapes(value: Array[LandscapeProxy]) -> None
```

## `unreal.PCGLandscapeDataProps(StructBase)`

```python
unreal.PCGLandscapeDataProps.__init__(get_height_only: bool = False, get_layer_weights: bool = False, get_actor_reference: bool = False, get_physical_material: bool = False, get_component_coordinates: bool = False) -> None
unreal.PCGLandscapeDataProps.get_actor_reference(value: bool) -> None
unreal.PCGLandscapeDataProps.get_component_coordinates(value: bool) -> None
unreal.PCGLandscapeDataProps.get_height_only(value: bool) -> None
unreal.PCGLandscapeDataProps.get_layer_weights(value: bool) -> None
unreal.PCGLandscapeDataProps.get_physical_material(value: bool) -> None
```

## `unreal.PCGLandscapeLayerWeight(StructBase)`

```python
unreal.PCGLandscapeLayerWeight.__init__(name: Name = "None", weight: float = 0.000000) -> None
unreal.PCGLandscapeLayerWeight.name(value: Name) -> None
unreal.PCGLandscapeLayerWeight.weight(value: float) -> None
```

## `unreal.PCGLandscapeSplineData(PCGPolyLineData)`

```python
unreal.PCGLandscapeSplineData.spline(value: LandscapeSplinesComponent) -> None
```

## `unreal.PCGLoadAlembicBPData(StructBase)`

```python
unreal.PCGLoadAlembicBPData.__init__(conversion_settings: AbcConversionSettings = [AbcConversionPreset.MAYA, False, True, [1.000000, -1.000000, 1.000000], [90.000000, 0.000000, 0.000000]], conversion_flip_handedness: bool = False, attribute_mapping: Map[str, PCGAttributePropertyInputSelector] = {}) -> None
unreal.PCGLoadAlembicBPData.attribute_mapping(value: Map[str, PCGAttributePropertyInputSelector]) -> None
unreal.PCGLoadAlembicBPData.conversion_flip_handedness(value: bool) -> None
unreal.PCGLoadAlembicBPData.conversion_settings(value: AbcConversionSettings) -> None
unreal.PCGLoadAlembicBPData.setup_from_standard(setup: PCGLoadAlembicStandardSetup) -> None
```

## `unreal.PCGLoadAlembicFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.PCGLoadAlembicFunctionLibrary.export_alembic_file_to_pcg(settings: PCGLoadAlembicBPData, parameters: PCGAssetExporterParameters = [True, "", "", True]) -> None
unreal.PCGLoadAlembicFunctionLibrary.load_alembic_file_to_pcg(settings: PCGLoadAlembicBPData, target_outer: Object) -> PCGDataCollection
unreal.PCGLoadAlembicFunctionLibrary.setup_from_standard(data: PCGLoadAlembicBPData, setup: PCGLoadAlembicStandardSetup) -> PCGLoadAlembicBPData
```

## `unreal.PCGLoadAlembicSettings(PCGExternalDataSettings)`

```python
unreal.PCGLoadAlembicSettings.alembic_file_path(value: FilePath) -> None
unreal.PCGLoadAlembicSettings.conversion_flip_handedness(value: bool) -> None
unreal.PCGLoadAlembicSettings.conversion_rotation(value: Vector) -> None
unreal.PCGLoadAlembicSettings.conversion_scale(value: Vector) -> None
unreal.PCGLoadAlembicSettings.setup_from_standard(setup: PCGLoadAlembicStandardSetup) -> None
```

## `unreal.PCGLoadDataAssetSettings(PCGSettings)`

```python
unreal.PCGLoadDataAssetSettings.asset(value: PCGDataAsset) -> None
unreal.PCGLoadDataAssetSettings.asset_color() -> LinearColor
unreal.PCGLoadDataAssetSettings.asset_description() -> Text
unreal.PCGLoadDataAssetSettings.asset_name() -> str
unreal.PCGLoadDataAssetSettings.asset_reference_selector(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGLoadDataAssetSettings.data_index_tag(value: Name) -> None
unreal.PCGLoadDataAssetSettings.input_index_tag(value: Name) -> None
unreal.PCGLoadDataAssetSettings.load_from_input(value: bool) -> None
unreal.PCGLoadDataAssetSettings.pins() -> Array[PCGPinProperties]
unreal.PCGLoadDataAssetSettings.synchronous_load(value: bool) -> None
unreal.PCGLoadDataAssetSettings.tag_outputs_based_on_output_pins() -> bool
unreal.PCGLoadDataAssetSettings.warn_if_no_asset(value: bool) -> None
```

## `unreal.PCGLoopSettings(PCGSubgraphSettings)`

```python
unreal.PCGLoopSettings.feedback_pins(value: str) -> None
unreal.PCGLoopSettings.loop_pins(value: str) -> None
unreal.PCGLoopSettings.use_graph_default_pin_usage(value: bool) -> None
```

## `unreal.PCGManagedComponent(PCGManagedComponentBase)`

```python
unreal.PCGManagedComponent.generated_component(value: ActorComponent) -> None
```

## `unreal.PCGManagedComponentList(PCGManagedComponentBase)`

```python
unreal.PCGManagedComponentList.generated_components(value: Array[ActorComponent]) -> None
```

## `unreal.PCGMatchAndSetAttributesSettings(PCGSettings)`

```python
unreal.PCGMatchAndSetAttributesSettings.find_nearest(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.input_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMatchAndSetAttributesSettings.input_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMatchAndSetAttributesSettings.keep_unmatched(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.match_attribute(value: Name) -> None
unreal.PCGMatchAndSetAttributesSettings.match_attributes(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.max_distance_for_nearest_match(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGMatchAndSetAttributesSettings.max_distance_input_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMatchAndSetAttributesSettings.max_distance_mode(value: PCGMatchMaxDistanceMode) -> None
unreal.PCGMatchAndSetAttributesSettings.use_input_weight_attribute(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.use_weight_attribute(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.warn_if_no_match_data(value: bool) -> None
unreal.PCGMatchAndSetAttributesSettings.weight_attribute(value: Name) -> None
```

## `unreal.PCGMatchAndSetBase(Object)`

```python
unreal.PCGMatchAndSetBase.match_and_set(context: PCGContext, settings: PCGPointMatchAndSetSettings, point_data: PCGPointData, out_point_data: PCGPointData) -> PCGContext
unreal.PCGMatchAndSetBase.validate_preconditions(point_data: PCGPointData) -> bool
```

## `unreal.PCGMatchAndSetByAttribute(PCGMatchAndSetBase)`

```python
unreal.PCGMatchAndSetByAttribute.entries(value: Array[PCGMatchAndSetByAttributeEntry]) -> None
unreal.PCGMatchAndSetByAttribute.match_source_attribute(value: Name) -> None
unreal.PCGMatchAndSetByAttribute.match_source_type(value: PCGMetadataTypes) -> None
```

## `unreal.PCGMatchAndSetByAttributeEntry(StructBase)`

```python
unreal.PCGMatchAndSetByAttributeEntry.__init__(value_to_match: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]], value: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]]) -> None
unreal.PCGMatchAndSetByAttributeEntry.value(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGMatchAndSetByAttributeEntry.value_to_match(value: PCGMetadataTypesConstantStruct) -> None
```

## `unreal.PCGMatchAndSetWeighted(PCGMatchAndSetBase)`

```python
unreal.PCGMatchAndSetWeighted.entries(value: Array[PCGMatchAndSetWeightedEntry]) -> None
unreal.PCGMatchAndSetWeighted.should_mutate_seed(value: bool) -> None
```

## `unreal.PCGMatchAndSetWeightedByCategory(PCGMatchAndSetBase)`

```python
unreal.PCGMatchAndSetWeightedByCategory.categories(value: Array[PCGMatchAndSetWeightedByCategoryEntryList]) -> None
unreal.PCGMatchAndSetWeightedByCategory.category_attribute(value: Name) -> None
unreal.PCGMatchAndSetWeightedByCategory.category_type(value: PCGMetadataTypes) -> None
unreal.PCGMatchAndSetWeightedByCategory.should_mutate_seed(value: bool) -> None
```

## `unreal.PCGMatchAndSetWeightedByCategoryEntryList(StructBase)`

```python
unreal.PCGMatchAndSetWeightedByCategoryEntryList.__init__(category_value: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]], is_default: bool = False, weighted_entries: Array[PCGMatchAndSetWeightedEntry] = []) -> None
unreal.PCGMatchAndSetWeightedByCategoryEntryList.category_value(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGMatchAndSetWeightedByCategoryEntryList.is_default(value: bool) -> None
unreal.PCGMatchAndSetWeightedByCategoryEntryList.weighted_entries(value: Array[PCGMatchAndSetWeightedEntry]) -> None
```

## `unreal.PCGMatchAndSetWeightedEntry(StructBase)`

```python
unreal.PCGMatchAndSetWeightedEntry.__init__(value: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]], weight: int = 0) -> None
unreal.PCGMatchAndSetWeightedEntry.value(value: PCGMetadataTypesConstantStruct) -> None
unreal.PCGMatchAndSetWeightedEntry.weight(value: int) -> None
```

## `unreal.PCGMergeSettings(PCGSettings)`

```python
unreal.PCGMergeSettings.merge_metadata(value: bool) -> None
```

## `unreal.PCGMeshInstanceList(StructBase)`

```python
unreal.PCGMeshInstanceList.__init__(instances: Array[Transform] = [], point_data: PCGPointData = None, instances_indices: Array[int] = []) -> None
unreal.PCGMeshInstanceList.instances(value: Array[Transform]) -> None
unreal.PCGMeshInstanceList.instances_indices(value: Array[int]) -> None
unreal.PCGMeshInstanceList.instances_metadata_entry(value: Array[int]) -> None
unreal.PCGMeshInstanceList.point_data(value: PCGPointData) -> None
```

## `unreal.PCGMeshSamplerSettings(PCGSettings)`

```python
unreal.PCGMeshSamplerSettings.color_channel_as_density(value: PCGColorChannel) -> None
unreal.PCGMeshSamplerSettings.extract_mesh_from_input(value: bool) -> None
unreal.PCGMeshSamplerSettings.extract_uv_as_attribute(value: bool) -> None
unreal.PCGMeshSamplerSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMeshSamplerSettings.material_attribute_name(value: Name) -> None
unreal.PCGMeshSamplerSettings.material_id_attribute_name(value: Name) -> None
unreal.PCGMeshSamplerSettings.non_uniform_sampling_options(value: GeometryScriptNonUniformPointSamplingOptions) -> None
unreal.PCGMeshSamplerSettings.output_material_info(value: bool) -> None
unreal.PCGMeshSamplerSettings.output_triangle_ids(value: bool) -> None
unreal.PCGMeshSamplerSettings.point_steepness(value: float) -> None
unreal.PCGMeshSamplerSettings.remove_hidden_triangles(value: bool) -> None
unreal.PCGMeshSamplerSettings.requested_lod_index(value: int) -> None
unreal.PCGMeshSamplerSettings.requested_lod_type(value: GeometryScriptLODType) -> None
unreal.PCGMeshSamplerSettings.sampling_method(value: PCGMeshSamplingMethod) -> None
unreal.PCGMeshSamplerSettings.sampling_options(value: GeometryScriptMeshPointSamplingOptions) -> None
unreal.PCGMeshSamplerSettings.static_mesh(value: StaticMesh) -> None
unreal.PCGMeshSamplerSettings.synchronous_load(value: bool) -> None
unreal.PCGMeshSamplerSettings.triangle_id_attribute_name(value: Name) -> None
unreal.PCGMeshSamplerSettings.use_color_channel_as_density(value: bool) -> None
unreal.PCGMeshSamplerSettings.uv_attribute_name(value: Name) -> None
unreal.PCGMeshSamplerSettings.uv_channel(value: int) -> None
unreal.PCGMeshSamplerSettings.voxel_size(value: float) -> None
unreal.PCGMeshSamplerSettings.voxelize(value: bool) -> None
```

## `unreal.PCGMeshSelectorByAttribute(PCGMeshSelectorBase)`

```python
unreal.PCGMeshSelectorByAttribute.attribute_name(value: Name) -> None
unreal.PCGMeshSelectorByAttribute.material_override_attributes(value: Array[Name]) -> None
unreal.PCGMeshSelectorByAttribute.use_attribute_material_overrides(value: bool) -> None
```

## `unreal.PCGMeshSelectorWeighted(PCGMeshSelectorBase)`

```python
unreal.PCGMeshSelectorWeighted.material_override_attributes(value: Array[Name]) -> None
unreal.PCGMeshSelectorWeighted.mesh_entries(value: Array[PCGMeshSelectorWeightedEntry]) -> None
unreal.PCGMeshSelectorWeighted.use_attribute_material_overrides(value: bool) -> None
```

## `unreal.PCGMeshSelectorWeightedByCategory(PCGMeshSelectorBase)`

```python
unreal.PCGMeshSelectorWeightedByCategory.category_attribute(value: Name) -> None
unreal.PCGMeshSelectorWeightedByCategory.entries(value: Array[PCGWeightedByCategoryEntryList]) -> None
unreal.PCGMeshSelectorWeightedByCategory.material_override_attributes(value: Array[Name]) -> None
unreal.PCGMeshSelectorWeightedByCategory.use_attribute_material_overrides(value: bool) -> None
```

## `unreal.PCGMeshSelectorWeightedEntry(StructBase)`

```python
unreal.PCGMeshSelectorWeightedEntry.__init__(weight: int = 0) -> None
unreal.PCGMeshSelectorWeightedEntry.weight(value: int) -> None
```

## `unreal.PCGMetadata(Object)`

```python
unreal.PCGMetadata.accumulate_point_weighted_attributes(point: PCGPoint, metadata: PCGMetadata, weight: float, set_non_interpolable_attributes: bool, out_point: PCGPoint) -> PCGPoint
unreal.PCGMetadata.accumulate_weighted_attributes_by_key(key: int, metadata: PCGMetadata, weight: float, set_non_interpolable_attributes: bool, target_key: int) -> int
unreal.PCGMetadata.add_attribute(other: PCGMetadata, attribute_name: Name) -> None
unreal.PCGMetadata.add_attributes(other: PCGMetadata) -> None
unreal.PCGMetadata.add_attributes_filtered(other: PCGMetadata, filtered_attributes: Set[Name], filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, match_operator: PCGStringMatchingOperator = PCGStringMatchingOperator.EQUAL) -> None
unreal.PCGMetadata.add_entry(parent_entry_key: int = -1) -> int
unreal.PCGMetadata.clear_attribute(attribute_to_clear: Name) -> None
unreal.PCGMetadata.copy_attribute(other: PCGMetadata, attribute_to_copy: Name, new_attribute_name: Name) -> None
unreal.PCGMetadata.copy_attributes(other: PCGMetadata) -> None
unreal.PCGMetadata.copy_existing_attribute(attribute_to_copy: Name, new_attribute_name: Name, keep_parent: bool = True) -> bool
unreal.PCGMetadata.create_bool_attribute(attribute_name: Name, default_value: bool, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_double_attribute(attribute_name: Name, default_value: float, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_float_attribute(attribute_name: Name, default_value: float, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_integer32_attribute(attribute_name: Name, default_value: int, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_integer64_attribute(attribute_name: Name, default_value: int, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_name_attribute(attribute_name: Name, default_value: Name, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_quat_attribute(attribute_name: Name, default_value: Quat, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_rotator_attribute(attribute_name: Name, default_value: Rotator, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_soft_class_path_attribute(attribute_name: Name, default_value: SoftClassPath, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_soft_object_path_attribute(attribute_name: Name, default_value: SoftObjectPath, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_string_attribute(attribute_name: Name, default_value: str, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_transform_attribute(attribute_name: Name, default_value: Transform, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_vector2_attribute(attribute_name: Name, default_value: Vector2D, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_vector4_attribute(attribute_name: Name, default_value: Vector4, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.create_vector_attribute(attribute_name: Name, default_value: Vector, allows_interpolation: bool, override_parent: bool = True) -> PCGMetadata
unreal.PCGMetadata.delete_attribute(attribute_name: Name) -> None
unreal.PCGMetadata.flatten() -> None
unreal.PCGMetadata.get_attribute_count() -> int
unreal.PCGMetadata.get_attributes() -> Tuple[Array[Name], Array[PCGMetadataTypes]]
unreal.PCGMetadata.get_item_count_for_child() -> int
unreal.PCGMetadata.has_attribute(attribute_name: Name) -> bool
unreal.PCGMetadata.has_common_attributes(metadata: PCGMetadata) -> bool
unreal.PCGMetadata.initialize(parent: PCGMetadata) -> None
unreal.PCGMetadata.initialize_as_copy(metadata_to_copy: PCGMetadata, optional_entries_to_copy: Array[int]) -> None
unreal.PCGMetadata.initialize_as_copy_with_attribute_filter(metadata_to_copy: PCGMetadata, filtered_attributes: Set[Name], optional_entries_to_copy: Array[int], filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES) -> None
unreal.PCGMetadata.initialize_with_attribute_filter(parent: PCGMetadata, filtered_attributes: Set[Name], filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, match_operator: PCGStringMatchingOperator = PCGStringMatchingOperator.EQUAL) -> None
unreal.PCGMetadata.k2_initialize_as_copy(metadata_to_copy: PCGMetadata, optional_entries_to_copy: Array[int]) -> None
unreal.PCGMetadata.k2_initialize_as_copy_with_attribute_filter(metadata_to_copy: PCGMetadata, filtered_attributes: Set[Name], optional_entries_to_copy: Array[int], filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES) -> None
unreal.PCGMetadata.merge_attributes_by_key(key_a: int, metadata_a: PCGMetadata, key_b: int, metadata_b: PCGMetadata, target_key: int, op: PCGMetadataOp) -> int
unreal.PCGMetadata.merge_point_attributes(point_a: PCGPoint, metadata_a: PCGMetadata, point_b: PCGPoint, metadata_b: PCGMetadata, target_point: PCGPoint, op: PCGMetadataOp) -> PCGPoint
unreal.PCGMetadata.rename_attribute(attribute_to_rename: Name, new_attribute_name: Name) -> bool
unreal.PCGMetadata.reset_point_weighted_attributes() -> PCGPoint
unreal.PCGMetadata.reset_weighted_attributes_by_key(target_key: int) -> int
unreal.PCGMetadata.set_attributes_by_key(key: int, metadata: PCGMetadata, target_key: int) -> int
unreal.PCGMetadata.set_point_attributes(point: PCGPoint, metadata: PCGMetadata, out_point: PCGPoint) -> PCGPoint
```

## `unreal.PCGMetadataAccessorHelpers(BlueprintFunctionLibrary)`

```python
unreal.PCGMetadataAccessorHelpers.copy_point(point: PCGPoint, copy_metadata: bool = True, metadata: PCGMetadata = None, out_metadata: PCGMetadata = None) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.get_bool_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGMetadataAccessorHelpers.get_bool_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGMetadataAccessorHelpers.get_double_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGMetadataAccessorHelpers.get_double_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGMetadataAccessorHelpers.get_float_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGMetadataAccessorHelpers.get_float_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGMetadataAccessorHelpers.get_integer32_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGMetadataAccessorHelpers.get_integer32_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGMetadataAccessorHelpers.get_integer64_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGMetadataAccessorHelpers.get_integer64_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGMetadataAccessorHelpers.get_name_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Name
unreal.PCGMetadataAccessorHelpers.get_quat_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Quat
unreal.PCGMetadataAccessorHelpers.get_quat_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Quat
unreal.PCGMetadataAccessorHelpers.get_rotator_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Rotator
unreal.PCGMetadataAccessorHelpers.get_rotator_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Rotator
unreal.PCGMetadataAccessorHelpers.get_soft_class_path_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> SoftClassPath
unreal.PCGMetadataAccessorHelpers.get_soft_class_path_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> SoftClassPath
unreal.PCGMetadataAccessorHelpers.get_soft_object_path_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> SoftObjectPath
unreal.PCGMetadataAccessorHelpers.get_soft_object_path_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> SoftObjectPath
unreal.PCGMetadataAccessorHelpers.get_string_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> str
unreal.PCGMetadataAccessorHelpers.get_string_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> str
unreal.PCGMetadataAccessorHelpers.get_transform_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Transform
unreal.PCGMetadataAccessorHelpers.get_transform_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Transform
unreal.PCGMetadataAccessorHelpers.get_vector2_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Vector2D
unreal.PCGMetadataAccessorHelpers.get_vector2_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Vector2D
unreal.PCGMetadataAccessorHelpers.get_vector4_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Vector4
unreal.PCGMetadataAccessorHelpers.get_vector4_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Vector4
unreal.PCGMetadataAccessorHelpers.get_vector_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> Vector
unreal.PCGMetadataAccessorHelpers.get_vector_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> Vector
unreal.PCGMetadataAccessorHelpers.has_attribute_set(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGMetadataAccessorHelpers.has_attribute_set_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGMetadataAccessorHelpers.initialize_metadata(point: PCGPoint, metadata: PCGMetadata, parent_point: PCGPoint, parent_metadata: PCGMetadata = None) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_attribute_from_property_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, object: Object, property_name: Name) -> Optional[int]
unreal.PCGMetadataAccessorHelpers.set_bool_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: bool) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_bool_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: bool) -> int
unreal.PCGMetadataAccessorHelpers.set_double_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: float) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_double_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: float) -> int
unreal.PCGMetadataAccessorHelpers.set_float_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: float) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_float_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: float) -> int
unreal.PCGMetadataAccessorHelpers.set_integer32_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: int) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_integer32_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: int) -> int
unreal.PCGMetadataAccessorHelpers.set_integer64_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: int) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_integer64_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: int) -> int
unreal.PCGMetadataAccessorHelpers.set_name_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Name) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_quat_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Quat) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_quat_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Quat) -> int
unreal.PCGMetadataAccessorHelpers.set_rotator_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Rotator) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_rotator_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Rotator) -> int
unreal.PCGMetadataAccessorHelpers.set_soft_class_path_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: SoftClassPath) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_soft_class_path_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: SoftClassPath) -> int
unreal.PCGMetadataAccessorHelpers.set_soft_object_path_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: SoftObjectPath) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_soft_object_path_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: SoftObjectPath) -> int
unreal.PCGMetadataAccessorHelpers.set_string_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: str) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_string_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: str) -> int
unreal.PCGMetadataAccessorHelpers.set_transform_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Transform) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_transform_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Transform) -> int
unreal.PCGMetadataAccessorHelpers.set_vector2_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Vector2D) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_vector2_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Vector2D) -> int
unreal.PCGMetadataAccessorHelpers.set_vector4_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Vector4) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_vector4_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Vector4) -> int
unreal.PCGMetadataAccessorHelpers.set_vector_attribute(point: PCGPoint, metadata: PCGMetadata, attribute_name: Name, value: Vector) -> PCGPoint
unreal.PCGMetadataAccessorHelpers.set_vector_attribute_by_metadata_key(key: int, metadata: PCGMetadata, attribute_name: Name, value: Vector) -> int
```

## `unreal.PCGMetadataBitwiseSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataBitwiseSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataBitwiseSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataBitwiseSettings.operation(value: PCGMetadataBitwiseOperation) -> None
```

## `unreal.PCGMetadataBooleanSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataBooleanSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataBooleanSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataBooleanSettings.operation(value: PCGMetadataBooleanOperation) -> None
```

## `unreal.PCGMetadataBreakVectorSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataBreakVectorSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGMetadataCompareSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataCompareSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataCompareSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataCompareSettings.operation(value: PCGMetadataCompareOperation) -> None
unreal.PCGMetadataCompareSettings.tolerance(value: float) -> None
```

## `unreal.PCGMetadataMakeRotatorSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataMakeRotatorSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeRotatorSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeRotatorSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeRotatorSettings.operation(value: PCGMetadataMakeRotatorOp) -> None
```

## `unreal.PCGMetadataMakeVectorSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataMakeVectorSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeVectorSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeVectorSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeVectorSettings.input_source4(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMakeVectorSettings.make_vector3_op(value: PCGMetadataMakeVector3) -> None
unreal.PCGMetadataMakeVectorSettings.make_vector4_op(value: PCGMetadataMakeVector4) -> None
unreal.PCGMetadataMakeVectorSettings.output_type(value: PCGMetadataTypes) -> None
```

## `unreal.PCGMetadataMathsSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataMathsSettings.force_op_to_double(value: bool) -> None
unreal.PCGMetadataMathsSettings.force_rounding_op_to_int(value: bool) -> None
unreal.PCGMetadataMathsSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMathsSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMathsSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataMathsSettings.operation(value: PCGMetadataMathsOperation) -> None
```

## `unreal.PCGMetadataPartitionSettings(PCGSettings)`

```python
unreal.PCGMetadataPartitionSettings.partition_attribute(value: Name) -> None
unreal.PCGMetadataPartitionSettings.partition_attribute_selectors(value: Array[PCGAttributePropertyInputSelector]) -> None
unreal.PCGMetadataPartitionSettings.partition_attribute_source(value: PCGAttributePropertyInputSelector) -> None
```

## `unreal.PCGMetadataRenameSettings(PCGSettings)`

```python
unreal.PCGMetadataRenameSettings.attribute_to_rename(value: Name) -> None
unreal.PCGMetadataRenameSettings.new_attribute_name(value: Name) -> None
```

## `unreal.PCGMetadataRotatorSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataRotatorSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataRotatorSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataRotatorSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataRotatorSettings.operation(value: PCGMetadataRotatorOperation) -> None
```

## `unreal.PCGMetadataSettingsBase(PCGSettings)`

```python
unreal.PCGMetadataSettingsBase.output_data_from_pin(value: Name) -> None
unreal.PCGMetadataSettingsBase.output_target(value: PCGAttributePropertyOutputSelector) -> None
```

## `unreal.PCGMetadataStringOpSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataStringOpSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataStringOpSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataStringOpSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataStringOpSettings.operation(value: PCGMetadataStringOperation) -> None
```

## `unreal.PCGMetadataTrigSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataTrigSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataTrigSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataTrigSettings.operation(value: PCGMetadataTrigOperation) -> None
```

## `unreal.PCGMetadataTypesConstantStruct(StructBase)`

```python
unreal.PCGMetadataTypesConstantStruct.__init__(type: PCGMetadataTypes = PCGMetadataTypes.FLOAT, float_value: float = 0.000000, int32_value: int = 0, double_value: float = 0.000000, int_value: int = 0, vector2_value: Vector2D = [0.000000, 0.000000], vector_value: Vector = [0.000000, 0.000000, 0.000000], vector4_value: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], quat_value: Quat = [0.000000, 0.000000, 0.000000, 1.000000], transform_value: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], string_value: str = "", bool_value: bool = False, rotator_value: Rotator = [0.000000, 0.000000, 0.000000], name_value: Name = "None", soft_class_path_value: SoftClassPath = [""], soft_object_path_value: SoftObjectPath = [""]) -> None
unreal.PCGMetadataTypesConstantStruct.bool_value(value: bool) -> None
unreal.PCGMetadataTypesConstantStruct.double_value(value: float) -> None
unreal.PCGMetadataTypesConstantStruct.float_value(value: float) -> None
unreal.PCGMetadataTypesConstantStruct.int32_value(value: int) -> None
unreal.PCGMetadataTypesConstantStruct.int_value(value: int) -> None
unreal.PCGMetadataTypesConstantStruct.name_value(value: Name) -> None
unreal.PCGMetadataTypesConstantStruct.quat_value(value: Quat) -> None
unreal.PCGMetadataTypesConstantStruct.rotator_value(value: Rotator) -> None
unreal.PCGMetadataTypesConstantStruct.soft_class_path_value(value: SoftClassPath) -> None
unreal.PCGMetadataTypesConstantStruct.soft_object_path_value(value: SoftObjectPath) -> None
unreal.PCGMetadataTypesConstantStruct.string_value(value: str) -> None
unreal.PCGMetadataTypesConstantStruct.transform_value(value: Transform) -> None
unreal.PCGMetadataTypesConstantStruct.type(value: PCGMetadataTypes) -> None
unreal.PCGMetadataTypesConstantStruct.vector2_value(value: Vector2D) -> None
unreal.PCGMetadataTypesConstantStruct.vector4_value(value: Vector4) -> None
unreal.PCGMetadataTypesConstantStruct.vector_value(value: Vector) -> None
```

## `unreal.PCGMetadataVectorSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGMetadataVectorSettings.input_source1(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataVectorSettings.input_source2(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataVectorSettings.input_source3(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGMetadataVectorSettings.operation(value: PCGMetadataVectorOperation) -> None
```

## `unreal.PCGMultiSelectSettings(PCGSettings)`

```python
unreal.PCGMultiSelectSettings.enum_selection(value: EnumSelector) -> None
unreal.PCGMultiSelectSettings.int_options(value: Array[int]) -> None
unreal.PCGMultiSelectSettings.integer_selection(value: int) -> None
unreal.PCGMultiSelectSettings.selection_mode(value: PCGControlFlowSelectionMode) -> None
unreal.PCGMultiSelectSettings.string_options(value: Array[str]) -> None
unreal.PCGMultiSelectSettings.string_selection(value: str) -> None
```

## `unreal.PCGNamedRerouteUsageSettings(PCGNamedRerouteBaseSettings)`

```python
unreal.PCGNamedRerouteUsageSettings.declaration(value: PCGNamedRerouteDeclarationSettings) -> None
```

## `unreal.PCGNormalToDensitySettings(PCGSettings)`

```python
unreal.PCGNormalToDensitySettings.density_mode(value: PCGNormalToDensityMode) -> None
unreal.PCGNormalToDensitySettings.normal(value: Vector) -> None
unreal.PCGNormalToDensitySettings.offset(value: float) -> None
unreal.PCGNormalToDensitySettings.strength(value: float) -> None
```

## `unreal.PCGNumberOfElementsBaseSettings(PCGSettings)`

```python
unreal.PCGNumberOfElementsBaseSettings.output_attribute_name(value: Name) -> None
```

## `unreal.PCGObjectPropertyOverrideDescription(StructBase)`

```python
unreal.PCGObjectPropertyOverrideDescription.__init__() -> None
```

## `unreal.PCGOctreeQueries(BlueprintFunctionLibrary)`

```python
unreal.PCGOctreeQueries.get_closest_point(point_data: PCGPointData, center: Vector, discard_center: bool, search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
unreal.PCGOctreeQueries.get_closest_point_from_other_point(point_data: PCGPointData, point_index: int, search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
unreal.PCGOctreeQueries.get_farthest_point(point_data: PCGPointData, center: Vector, search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
unreal.PCGOctreeQueries.get_farthest_point_from_other_point(point_data: PCGPointData, point_index: int, search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
unreal.PCGOctreeQueries.get_points_inside_bounds(point_data: PCGPointData, bounds: Box) -> Array[PCGPoint]
unreal.PCGOctreeQueries.get_points_inside_sphere(point_data: PCGPointData, center: Vector, radius: float) -> Array[PCGPoint]
```

## `unreal.PCGOuterIntersectionSettings(PCGSettingsWithDynamicInputs)`

```python
unreal.PCGOuterIntersectionSettings.density_function(value: PCGIntersectionDensityFunction) -> None
unreal.PCGOuterIntersectionSettings.ignore_pins_with_no_input(value: bool) -> None
unreal.PCGOuterIntersectionSettings.keep_zero_density_points(value: bool) -> None
```

## `unreal.PCGOverrideInstancedPropertyBag(StructBase)`

```python
unreal.PCGOverrideInstancedPropertyBag.__init__() -> None
```

## `unreal.PCGPackedCustomData(StructBase)`

```python
unreal.PCGPackedCustomData.__init__(num_custom_data_floats: int = 0, custom_data: Array[float] = []) -> None
unreal.PCGPackedCustomData.custom_data(value: Array[float]) -> None
unreal.PCGPackedCustomData.num_custom_data_floats(value: int) -> None
```

## `unreal.PCGParamData(PCGData)`

```python
unreal.PCGParamData.const_metadata() -> PCGMetadata
unreal.PCGParamData.filter_params_by_key(key: int) -> PCGParamData
unreal.PCGParamData.filter_params_by_name(name: Name) -> PCGParamData
unreal.PCGParamData.find_metadata_key(name: Name) -> int
unreal.PCGParamData.find_or_add_metadata_key(name: Name) -> int
unreal.PCGParamData.k2_filter_params_by_key(key: int) -> PCGParamData
unreal.PCGParamData.k2_filter_params_by_name(name: Name) -> PCGParamData
unreal.PCGParamData.mutable_metadata() -> PCGMetadata
```

## `unreal.PCGParseStringSettings(PCGMetadataSettingsBase)`

```python
unreal.PCGParseStringSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGParseStringSettings.target_type(value: PCGMetadataTypes) -> None
```

## `unreal.PCGPathfindingSettings(PCGSettings)`

```python
unreal.PCGPathfindingSettings.accept_partial_path(value: bool) -> None
unreal.PCGPathfindingSettings.copy_originating_points(value: bool) -> None
unreal.PCGPathfindingSettings.cost_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGPathfindingSettings.cost_function_mode(value: PCGPathfindingCostFunctionMode) -> None
unreal.PCGPathfindingSettings.goal(value: Vector) -> None
unreal.PCGPathfindingSettings.goal_location_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGPathfindingSettings.goal_locations_as_input(value: bool) -> None
unreal.PCGPathfindingSettings.heuristic_weight(value: float) -> None
unreal.PCGPathfindingSettings.maximum_fitness_penalty_factor(value: float) -> None
unreal.PCGPathfindingSettings.output_as_spline(value: bool) -> None
unreal.PCGPathfindingSettings.path_trace_params(value: PCGWorldRaycastQueryParams) -> None
unreal.PCGPathfindingSettings.search_distance(value: float) -> None
unreal.PCGPathfindingSettings.spline_mode(value: PCGPathfindingSplineMode) -> None
unreal.PCGPathfindingSettings.start(value: Vector) -> None
unreal.PCGPathfindingSettings.start_location_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGPathfindingSettings.start_locations_as_input(value: bool) -> None
unreal.PCGPathfindingSettings.use_path_traces(value: bool) -> None
```

## `unreal.PCGPoint(StructBase)`

```python
unreal.PCGPoint.__init__(transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], density: float = 0.000000, bounds_min: Vector = [0.000000, 0.000000, 0.000000], bounds_max: Vector = [0.000000, 0.000000, 0.000000], color: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], steepness: float = 0.000000, seed: int = 0, metadata_entry: int = 0) -> None
unreal.PCGPoint.bounds_max(value: Vector) -> None
unreal.PCGPoint.bounds_min(value: Vector) -> None
unreal.PCGPoint.color(value: Vector4) -> None
unreal.PCGPoint.copy_point(copy_metadata: bool = True, metadata: PCGMetadata = None, out_metadata: PCGMetadata = None) -> PCGPoint
unreal.PCGPoint.density(value: float) -> None
unreal.PCGPoint.get_bool_attribute(metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGPoint.get_double_attribute(metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGPoint.get_extents() -> Vector
unreal.PCGPoint.get_float_attribute(metadata: PCGMetadata, attribute_name: Name) -> float
unreal.PCGPoint.get_integer32_attribute(metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGPoint.get_integer64_attribute(metadata: PCGMetadata, attribute_name: Name) -> int
unreal.PCGPoint.get_local_center() -> Vector
unreal.PCGPoint.get_name_attribute(metadata: PCGMetadata, attribute_name: Name) -> Name
unreal.PCGPoint.get_quat_attribute(metadata: PCGMetadata, attribute_name: Name) -> Quat
unreal.PCGPoint.get_random_stream(optional_settings: PCGSettings = None, optional_component: PCGComponent = None) -> RandomStream
unreal.PCGPoint.get_random_stream_from_point(optional_settings: PCGSettings = None, optional_component: PCGComponent = None) -> RandomStream
unreal.PCGPoint.get_random_stream_from_two_points(point_b: PCGPoint, optional_settings: PCGSettings = None, optional_component: PCGComponent = None) -> RandomStream
unreal.PCGPoint.get_rotator_attribute(metadata: PCGMetadata, attribute_name: Name) -> Rotator
unreal.PCGPoint.get_soft_class_path_attribute(metadata: PCGMetadata, attribute_name: Name) -> SoftClassPath
unreal.PCGPoint.get_soft_object_path_attribute(metadata: PCGMetadata, attribute_name: Name) -> SoftObjectPath
unreal.PCGPoint.get_string_attribute(metadata: PCGMetadata, attribute_name: Name) -> str
unreal.PCGPoint.get_transform_attribute(metadata: PCGMetadata, attribute_name: Name) -> Transform
unreal.PCGPoint.get_transformed_bounds() -> Box
unreal.PCGPoint.get_vector2_attribute(metadata: PCGMetadata, attribute_name: Name) -> Vector2D
unreal.PCGPoint.get_vector4_attribute(metadata: PCGMetadata, attribute_name: Name) -> Vector4
unreal.PCGPoint.get_vector_attribute(metadata: PCGMetadata, attribute_name: Name) -> Vector
unreal.PCGPoint.has_attribute_set(metadata: PCGMetadata, attribute_name: Name) -> bool
unreal.PCGPoint.initialize_metadata(metadata: PCGMetadata, parent_point: PCGPoint, parent_metadata: PCGMetadata = None) -> None
unreal.PCGPoint.metadata_entry() -> int
unreal.PCGPoint.seed(value: int) -> None
unreal.PCGPoint.set_bool_attribute(metadata: PCGMetadata, attribute_name: Name, value: bool) -> None
unreal.PCGPoint.set_double_attribute(metadata: PCGMetadata, attribute_name: Name, value: float) -> None
unreal.PCGPoint.set_extents(extents: Vector) -> None
unreal.PCGPoint.set_float_attribute(metadata: PCGMetadata, attribute_name: Name, value: float) -> None
unreal.PCGPoint.set_integer32_attribute(metadata: PCGMetadata, attribute_name: Name, value: int) -> None
unreal.PCGPoint.set_integer64_attribute(metadata: PCGMetadata, attribute_name: Name, value: int) -> None
unreal.PCGPoint.set_local_center(local_center: Vector) -> None
unreal.PCGPoint.set_name_attribute(metadata: PCGMetadata, attribute_name: Name, value: Name) -> None
unreal.PCGPoint.set_quat_attribute(metadata: PCGMetadata, attribute_name: Name, value: Quat) -> None
unreal.PCGPoint.set_rotator_attribute(metadata: PCGMetadata, attribute_name: Name, value: Rotator) -> None
unreal.PCGPoint.set_soft_class_path_attribute(metadata: PCGMetadata, attribute_name: Name, value: SoftClassPath) -> None
unreal.PCGPoint.set_soft_object_path_attribute(metadata: PCGMetadata, attribute_name: Name, value: SoftObjectPath) -> None
unreal.PCGPoint.set_string_attribute(metadata: PCGMetadata, attribute_name: Name, value: str) -> None
unreal.PCGPoint.set_transform_attribute(metadata: PCGMetadata, attribute_name: Name, value: Transform) -> None
unreal.PCGPoint.set_vector2_attribute(metadata: PCGMetadata, attribute_name: Name, value: Vector2D) -> None
unreal.PCGPoint.set_vector4_attribute(metadata: PCGMetadata, attribute_name: Name, value: Vector4) -> None
unreal.PCGPoint.set_vector_attribute(metadata: PCGMetadata, attribute_name: Name, value: Vector) -> None
unreal.PCGPoint.steepness(value: float) -> None
unreal.PCGPoint.transform(value: Transform) -> None
```

## `unreal.PCGPointData(PCGSpatialData)`

```python
unreal.PCGPointData.copy_points_from(data: PCGPointData, data_indices: Array[int]) -> None
unreal.PCGPointData.get_num_points() -> int
unreal.PCGPointData.get_point(index: int) -> PCGPoint
unreal.PCGPointData.get_points() -> Array[PCGPoint]
unreal.PCGPointData.get_points_copy() -> Array[PCGPoint]
unreal.PCGPointData.is_empty() -> bool
unreal.PCGPointData.set_points(points: Array[PCGPoint]) -> None
```

## `unreal.PCGPointExtentsModifierSettings(PCGSettings)`

```python
unreal.PCGPointExtentsModifierSettings.extents(value: Vector) -> None
unreal.PCGPointExtentsModifierSettings.mode(value: PCGPointExtentsModifierMode) -> None
```

## `unreal.PCGPointFilterThresholdSettings(PCGAttributeFilterThresholdSettings)`

```python
unreal.PCGPointFilterThresholdSettings.__init__(inclusive: bool = False, use_constant_threshold: bool = False, threshold_attribute: PCGAttributePropertyInputSelector = [], use_spatial_query: bool = False, attribute_types: PCGMetadataTypesConstantStruct = [PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], "", False, [0.000000, 0.000000, 0.000000], "None", [""], [""]]) -> None
```

## `unreal.PCGPointFromMeshSettings(PCGSettings)`

```python
unreal.PCGPointFromMeshSettings.mesh_path_attribute_name(value: Name) -> None
unreal.PCGPointFromMeshSettings.static_mesh(value: StaticMesh) -> None
unreal.PCGPointFromMeshSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGPointMatchAndSetSettings(PCGSettings)`

```python
unreal.PCGPointMatchAndSetSettings.match_and_set_instance() -> PCGMatchAndSetBase
unreal.PCGPointMatchAndSetSettings.match_and_set_type() -> Class
unreal.PCGPointMatchAndSetSettings.set_match_and_set_type(match_and_set_type: Class) -> None
unreal.PCGPointMatchAndSetSettings.set_target(value: PCGAttributePropertyOutputSelector) -> None
unreal.PCGPointMatchAndSetSettings.set_target_type(value: PCGMetadataTypes) -> None
```

## `unreal.PCGPointNeighborhoodSettings(PCGSettings)`

```python
unreal.PCGPointNeighborhoodSettings.average_position_attribute(value: Name) -> None
unreal.PCGPointNeighborhoodSettings.distance_attribute(value: Name) -> None
unreal.PCGPointNeighborhoodSettings.search_distance(value: float) -> None
unreal.PCGPointNeighborhoodSettings.set_average_color(value: bool) -> None
unreal.PCGPointNeighborhoodSettings.set_average_position(value: bool) -> None
unreal.PCGPointNeighborhoodSettings.set_average_position_to_attribute(value: bool) -> None
unreal.PCGPointNeighborhoodSettings.set_density(value: PCGPointNeighborhoodDensityMode) -> None
unreal.PCGPointNeighborhoodSettings.set_distance_to_attribute(value: bool) -> None
unreal.PCGPointNeighborhoodSettings.weighted_average(value: bool) -> None
```

## `unreal.PCGPreConfiguredSettingsInfo(StructBase)`

```python
unreal.PCGPreConfiguredSettingsInfo.__init__(preconfigured_index: int = 0, label: Text = "") -> None
unreal.PCGPreConfiguredSettingsInfo.label(value: Text) -> None
unreal.PCGPreConfiguredSettingsInfo.preconfigured_index(value: int) -> None
```

## `unreal.PCGPrimitiveCrossSectionSettings(PCGSettings)`

```python
unreal.PCGPrimitiveCrossSectionSettings.enable_min_area_culling(value: bool) -> None
unreal.PCGPrimitiveCrossSectionSettings.enable_tier_merging(value: bool) -> None
unreal.PCGPrimitiveCrossSectionSettings.extrusion_vector_attribute(value: PCGAttributePropertyOutputSelector) -> None
unreal.PCGPrimitiveCrossSectionSettings.max_mesh_vertex_count(value: int) -> None
unreal.PCGPrimitiveCrossSectionSettings.min_area_culling_threshold(value: float) -> None
unreal.PCGPrimitiveCrossSectionSettings.minimum_coplanar_vertices(value: int) -> None
unreal.PCGPrimitiveCrossSectionSettings.remove_redundant_sections(value: bool) -> None
unreal.PCGPrimitiveCrossSectionSettings.slice_direction(value: Vector) -> None
unreal.PCGPrimitiveCrossSectionSettings.tier_merging_threshold(value: float) -> None
```

## `unreal.PCGPrimitiveData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGPrimitiveData.primitive() -> PrimitiveComponent
unreal.PCGPrimitiveData.voxel_size(value: Vector) -> None
```

## `unreal.PCGPrintElementSettings(PCGSettings)`

```python
unreal.PCGPrintElementSettings.custom_prefix(value: str) -> None
unreal.PCGPrintElementSettings.display_on_node(value: bool) -> None
unreal.PCGPrintElementSettings.enable_print(value: bool) -> None
unreal.PCGPrintElementSettings.prefix_with_component(value: bool) -> None
unreal.PCGPrintElementSettings.prefix_with_graph(value: bool) -> None
unreal.PCGPrintElementSettings.prefix_with_node(value: bool) -> None
unreal.PCGPrintElementSettings.prefix_with_owner(value: bool) -> None
unreal.PCGPrintElementSettings.print_per_component(value: bool) -> None
unreal.PCGPrintElementSettings.print_string(value: str) -> None
unreal.PCGPrintElementSettings.print_to_screen(value: bool) -> None
unreal.PCGPrintElementSettings.print_to_screen_color(value: Color) -> None
unreal.PCGPrintElementSettings.print_to_screen_duration(value: float) -> None
unreal.PCGPrintElementSettings.verbosity(value: PCGPrintVerbosity) -> None
```

## `unreal.PCGPrintGrammarSettings(PCGSettings)`

```python
unreal.PCGPrintGrammarSettings.grammar(value: str) -> None
```

## `unreal.PCGProceduralISMComponent(StaticMeshComponent)`

```python
unreal.PCGProceduralISMComponent.clear_instances() -> None
unreal.PCGProceduralISMComponent.get_cull_distances() -> Tuple[int, int]
unreal.PCGProceduralISMComponent.get_num_custom_data_floats() -> int
unreal.PCGProceduralISMComponent.get_num_instances() -> int
unreal.PCGProceduralISMComponent.instance_end_cull_distance() -> int
unreal.PCGProceduralISMComponent.instance_start_cull_distance() -> int
unreal.PCGProceduralISMComponent.set_cull_distances(start_cull_distance: int, end_cull_distance: int) -> None
unreal.PCGProceduralISMComponent.set_local_bounds(local_bounds: Box) -> None
unreal.PCGProceduralISMComponent.set_num_custom_data_floats(num_custom_data_floats: int) -> None
unreal.PCGProceduralISMComponent.set_num_instances(num_instances: int) -> None
```

## `unreal.PCGProjectionData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGProjectionData.projection_params() -> PCGProjectionParams
unreal.PCGProjectionData.source() -> PCGSpatialData
unreal.PCGProjectionData.target() -> PCGSpatialData
```

## `unreal.PCGProjectionParams(StructBase)`

```python
unreal.PCGProjectionParams.__init__(project_positions: bool = False, project_rotations: bool = False, project_scales: bool = False, color_blend_mode: PCGProjectionColorBlendMode = PCGProjectionColorBlendMode.SOURCE_VALUE, attribute_list: str = "", attribute_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, attribute_merge_operation: PCGMetadataOp = PCGMetadataOp.MIN, tag_merge_operation: PCGProjectionTagMergeMode = PCGProjectionTagMergeMode.SOURCE) -> None
unreal.PCGProjectionParams.attribute_list(value: str) -> None
unreal.PCGProjectionParams.attribute_merge_operation(value: PCGMetadataOp) -> None
unreal.PCGProjectionParams.attribute_mode(value: PCGMetadataFilterMode) -> None
unreal.PCGProjectionParams.color_blend_mode(value: PCGProjectionColorBlendMode) -> None
unreal.PCGProjectionParams.project_colors(value: bool) -> None
unreal.PCGProjectionParams.project_positions(value: bool) -> None
unreal.PCGProjectionParams.project_rotations(value: bool) -> None
unreal.PCGProjectionParams.project_scales(value: bool) -> None
unreal.PCGProjectionParams.tag_merge_operation(value: PCGProjectionTagMergeMode) -> None
```

## `unreal.PCGProjectionSettings(PCGSettings)`

```python
unreal.PCGProjectionSettings.force_collapse_to_point(value: bool) -> None
unreal.PCGProjectionSettings.keep_zero_density_points(value: bool) -> None
unreal.PCGProjectionSettings.params(value: PCGProjectionParams) -> None
unreal.PCGProjectionSettings.projection_params(value: PCGProjectionParams) -> None
```

## `unreal.PCGQualityBranchSettings(PCGSettings)`

```python
unreal.PCGQualityBranchSettings.use_cinematic_pin(value: bool) -> None
unreal.PCGQualityBranchSettings.use_epic_pin(value: bool) -> None
unreal.PCGQualityBranchSettings.use_high_pin(value: bool) -> None
unreal.PCGQualityBranchSettings.use_low_pin(value: bool) -> None
unreal.PCGQualityBranchSettings.use_medium_pin(value: bool) -> None
```

## `unreal.PCGQualitySelectSettings(PCGSettings)`

```python
unreal.PCGQualitySelectSettings.use_cinematic_pin(value: bool) -> None
unreal.PCGQualitySelectSettings.use_epic_pin(value: bool) -> None
unreal.PCGQualitySelectSettings.use_high_pin(value: bool) -> None
unreal.PCGQualitySelectSettings.use_low_pin(value: bool) -> None
unreal.PCGQualitySelectSettings.use_medium_pin(value: bool) -> None
```

## `unreal.PCGRandomChoiceSettings(PCGSettings)`

```python
unreal.PCGRandomChoiceSettings.b_output_discarded_points(value: bool) -> None
unreal.PCGRandomChoiceSettings.fixed_mode(value: bool) -> None
unreal.PCGRandomChoiceSettings.fixed_number(value: int) -> None
unreal.PCGRandomChoiceSettings.output_discarded_entries(value: bool) -> None
unreal.PCGRandomChoiceSettings.ratio(value: float) -> None
```

## `unreal.PCGReplaceTagsSettings(PCGSettings)`

```python
unreal.PCGReplaceTagsSettings.replaced_tags(value: str) -> None
unreal.PCGReplaceTagsSettings.selected_tags(value: str) -> None
```

## `unreal.PCGResetPointCenterSettings(PCGSettings)`

```python
unreal.PCGResetPointCenterSettings.point_center_location(value: Vector) -> None
```

## `unreal.PCGReverseSplineSettings(PCGSettings)`

```python
unreal.PCGReverseSplineSettings.operation(value: PCGReverseSplineOperation) -> None
```

## `unreal.PCGRuntimeGenerationRadii(StructBase)`

```python
unreal.PCGRuntimeGenerationRadii.__init__(generation_radius: float = 0.000000, generation_radius400: float = 0.000000, generation_radius800: float = 0.000000, generation_radius1600: float = 0.000000, generation_radius3200: float = 0.000000, generation_radius6400: float = 0.000000, generation_radius12800: float = 0.000000, generation_radius25600: float = 0.000000, generation_radius51200: float = 0.000000, generation_radius102400: float = 0.000000, generation_radius204800: float = 0.000000, cleanup_radius_multiplier: float = 0.000000) -> None
unreal.PCGRuntimeGenerationRadii.cleanup_radius_multiplier(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius102400(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius12800(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius1600(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius204800(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius25600(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius3200(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius400(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius51200(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius6400(value: float) -> None
unreal.PCGRuntimeGenerationRadii.generation_radius800(value: float) -> None
```

## `unreal.PCGSanityCheckPointDataSettings(PCGSettings)`

```python
unreal.PCGSanityCheckPointDataSettings.max_point_count(value: int) -> None
unreal.PCGSanityCheckPointDataSettings.min_point_count(value: int) -> None
```

## `unreal.PCGSaveDataAssetSettings(PCGSettings)`

```python
unreal.PCGSaveDataAssetSettings.asset_color(value: LinearColor) -> None
unreal.PCGSaveDataAssetSettings.asset_description(value: str) -> None
unreal.PCGSaveDataAssetSettings.custom_data_collection_exporter_class(value: Class) -> None
unreal.PCGSaveDataAssetSettings.params(value: PCGAssetExporterParameters) -> None
unreal.PCGSaveDataAssetSettings.pins(value: Array[PCGPinProperties]) -> None
```

## `unreal.PCGSaveDynamicMeshToAssetSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGSaveDynamicMeshToAssetSettings.copy_mesh_to_asset_options(value: GeometryScriptCopyMeshToAssetOptions) -> None
unreal.PCGSaveDynamicMeshToAssetSettings.export_materials_from_dynamic_mesh(value: bool) -> None
unreal.PCGSaveDynamicMeshToAssetSettings.export_params(value: PCGAssetExporterParameters) -> None
unreal.PCGSaveDynamicMeshToAssetSettings.mesh_write_lod(value: GeometryScriptMeshWriteLOD) -> None
```

## `unreal.PCGSchedulingPolicyDistanceAndDirection(PCGSchedulingPolicyBase)`

```python
unreal.PCGSchedulingPolicyDistanceAndDirection.direction_weight(value: float) -> None
unreal.PCGSchedulingPolicyDistanceAndDirection.distance_weight(value: float) -> None
unreal.PCGSchedulingPolicyDistanceAndDirection.use_direction(value: bool) -> None
unreal.PCGSchedulingPolicyDistanceAndDirection.use_distance(value: bool) -> None
```

## `unreal.PCGSelectGrammarCriteriaAttributeNames(StructBase)`

```python
unreal.PCGSelectGrammarCriteriaAttributeNames.__init__(key_attribute_name: Name = "None", comparator_attribute_name: Name = "None", first_value_attribute_name: Name = "None", second_value_attribute_name: Name = "None", grammar_attribute_name: Name = "None") -> None
unreal.PCGSelectGrammarCriteriaAttributeNames.comparator_attribute_name(value: Name) -> None
unreal.PCGSelectGrammarCriteriaAttributeNames.first_value_attribute_name(value: Name) -> None
unreal.PCGSelectGrammarCriteriaAttributeNames.grammar_attribute_name(value: Name) -> None
unreal.PCGSelectGrammarCriteriaAttributeNames.key_attribute_name(value: Name) -> None
unreal.PCGSelectGrammarCriteriaAttributeNames.second_value_attribute_name(value: Name) -> None
```

## `unreal.PCGSelectGrammarCriterion(StructBase)`

```python
unreal.PCGSelectGrammarCriterion.__init__(key: Name = "None", comparator: PCGSelectGrammarComparator = 0, first_value: float = 0.000000, second_value: float = 0.000000, grammar: str = "") -> None
unreal.PCGSelectGrammarCriterion.comparator(value: PCGSelectGrammarComparator) -> None
unreal.PCGSelectGrammarCriterion.first_value(value: float) -> None
unreal.PCGSelectGrammarCriterion.grammar(value: str) -> None
unreal.PCGSelectGrammarCriterion.key(value: Name) -> None
unreal.PCGSelectGrammarCriterion.second_value(value: float) -> None
```

## `unreal.PCGSelectGrammarSettings(PCGSettings)`

```python
unreal.PCGSelectGrammarSettings.compared_value_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSelectGrammarSettings.copy_key_for_unselected_grammar(value: bool) -> None
unreal.PCGSelectGrammarSettings.criteria(value: Array[PCGSelectGrammarCriterion]) -> None
unreal.PCGSelectGrammarSettings.criteria_as_input(value: bool) -> None
unreal.PCGSelectGrammarSettings.criteria_attribute_names(value: PCGSelectGrammarCriteriaAttributeNames) -> None
unreal.PCGSelectGrammarSettings.key(value: Name) -> None
unreal.PCGSelectGrammarSettings.key_as_attribute(value: bool) -> None
unreal.PCGSelectGrammarSettings.key_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSelectGrammarSettings.output_grammar_attribute(value: PCGAttributePropertyOutputSelector) -> None
unreal.PCGSelectGrammarSettings.remap_criteria_attribute_names(value: bool) -> None
```

## `unreal.PCGSelectPointsSettings(PCGSettings)`

```python
unreal.PCGSelectPointsSettings.keep_zero_density_points(value: bool) -> None
unreal.PCGSelectPointsSettings.ratio(value: float) -> None
```

## `unreal.PCGSelfPruningParameters(StructBase)`

```python
unreal.PCGSelfPruningParameters.__init__(pruning_type: PCGSelfPruningType = PCGSelfPruningType.LARGE_TO_SMALL, comparison_source: PCGAttributePropertyInputSelector = [], radius_similarity_factor: float = 0.000000, randomized_pruning: bool = False, use_collision_attribute: bool = False, collision_attribute: PCGAttributePropertyInputSelector = [], collision_query_flag: PCGCollisionQueryFlag = PCGCollisionQueryFlag.SIMPLE) -> None
unreal.PCGSelfPruningParameters.collision_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSelfPruningParameters.collision_query_flag(value: PCGCollisionQueryFlag) -> None
unreal.PCGSelfPruningParameters.comparison_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSelfPruningParameters.pruning_type(value: PCGSelfPruningType) -> None
unreal.PCGSelfPruningParameters.radius_similarity_factor(value: float) -> None
unreal.PCGSelfPruningParameters.randomized_pruning(value: bool) -> None
unreal.PCGSelfPruningParameters.use_collision_attribute(value: bool) -> None
```

## `unreal.PCGSelfPruningSettings(PCGSettings)`

```python
unreal.PCGSelfPruningSettings.parameters(value: PCGSelfPruningParameters) -> None
```

## `unreal.PCGSettings(PCGSettingsInterface)`

```python
unreal.PCGSettings.bp_get_type_union_of_incident_edges(pin_label: Name) -> int
unreal.PCGSettings.category(value: Text) -> None
unreal.PCGSettings.description(value: Text) -> None
unreal.PCGSettings.determinism_settings(value: PCGDeterminismSettings) -> None
unreal.PCGSettings.expose_to_library(value: bool) -> None
unreal.PCGSettings.seed(value: int) -> None
unreal.PCGSettings.use_seed(value: bool) -> None
```

## `unreal.PCGSettingsInstance(PCGSettingsInterface)`

```python
unreal.PCGSettingsInstance.settings() -> PCGSettings
```

## `unreal.PCGSettingsInterface(PCGData)`

```python
unreal.PCGSettingsInterface.break_debugger(value: bool) -> None
unreal.PCGSettingsInterface.debug(value: bool) -> None
unreal.PCGSettingsInterface.debug_settings(value: PCGDebugVisualizationSettings) -> None
unreal.PCGSettingsInterface.enabled(value: bool) -> None
```

## `unreal.PCGSoftISMComponentDescriptor(SoftISMComponentDescriptor)`

```python
unreal.PCGSoftISMComponentDescriptor.__init__() -> None
```

## `unreal.PCGSortAttributesSettings(PCGSettings)`

```python
unreal.PCGSortAttributesSettings.input_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSortAttributesSettings.sort_method(value: PCGSortMethod) -> None
```

## `unreal.PCGSortTagsSettings(PCGSettings)`

```python
unreal.PCGSortTagsSettings.sort_method(value: PCGSortMethod) -> None
unreal.PCGSortTagsSettings.tag(value: Name) -> None
```

## `unreal.PCGSpatialData(PCGData)`

```python
unreal.PCGSpatialData.const_metadata() -> PCGMetadata
unreal.PCGSpatialData.create_empty_metadata() -> PCGMetadata
unreal.PCGSpatialData.get_bounds() -> Box
unreal.PCGSpatialData.get_density_at_position(position: Vector) -> float
unreal.PCGSpatialData.get_dimension() -> int
unreal.PCGSpatialData.get_normal() -> Vector
unreal.PCGSpatialData.get_strict_bounds() -> Box
unreal.PCGSpatialData.has_non_trivial_transform() -> bool
unreal.PCGSpatialData.initialize_from_data(source: PCGSpatialData, metadata_parent_override: PCGMetadata = None, inherit_metadata: bool = True, inherit_attributes: bool = True) -> None
unreal.PCGSpatialData.intersect_with(other: PCGSpatialData) -> PCGIntersectionData
unreal.PCGSpatialData.k2_intersect_with(other: PCGSpatialData) -> PCGIntersectionData
unreal.PCGSpatialData.k2_project_on(other: PCGSpatialData, params: PCGProjectionParams = [True, True, False, PCGProjectionColorBlendMode.SOURCE_VALUE, "", PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, PCGMetadataOp.TARGET_VALUE, PCGProjectionTagMergeMode.SOURCE]) -> PCGSpatialData
unreal.PCGSpatialData.k2_project_point(transform: Transform, bounds: Box, params: PCGProjectionParams, out_metadata: PCGMetadata) -> Optional[PCGPoint]
unreal.PCGSpatialData.k2_sample_point(transform: Transform, bounds: Box, out_metadata: PCGMetadata) -> Optional[PCGPoint]
unreal.PCGSpatialData.k2_subtract(other: PCGSpatialData) -> PCGDifferenceData
unreal.PCGSpatialData.k2_union_with(other: PCGSpatialData) -> PCGUnionData
unreal.PCGSpatialData.keep_zero_density_points(value: bool) -> None
unreal.PCGSpatialData.mutable_metadata() -> PCGMetadata
unreal.PCGSpatialData.project_on(other: PCGSpatialData, params: PCGProjectionParams = [True, True, False, PCGProjectionColorBlendMode.SOURCE_VALUE, "", PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, PCGMetadataOp.TARGET_VALUE, PCGProjectionTagMergeMode.SOURCE]) -> PCGSpatialData
unreal.PCGSpatialData.project_point(transform: Transform, bounds: Box, params: PCGProjectionParams, out_metadata: PCGMetadata) -> Optional[PCGPoint]
unreal.PCGSpatialData.sample_point(transform: Transform, bounds: Box, out_metadata: PCGMetadata) -> Optional[PCGPoint]
unreal.PCGSpatialData.subtract(other: PCGSpatialData) -> PCGDifferenceData
unreal.PCGSpatialData.target_actor(value: Actor) -> None
unreal.PCGSpatialData.to_point_data() -> PCGPointData
unreal.PCGSpatialData.to_point_data_with_context(context: PCGContext) -> Tuple[PCGPointData, PCGContext]
unreal.PCGSpatialData.union_with(other: PCGSpatialData) -> PCGUnionData
```

## `unreal.PCGSpatialNoiseSettings(PCGSettings)`

```python
unreal.PCGSpatialNoiseSettings.brightness(value: float) -> None
unreal.PCGSpatialNoiseSettings.contrast(value: float) -> None
unreal.PCGSpatialNoiseSettings.edge_blend_curve_intensity(value: float) -> None
unreal.PCGSpatialNoiseSettings.edge_blend_curve_offset(value: float) -> None
unreal.PCGSpatialNoiseSettings.edge_blend_distance(value: float) -> None
unreal.PCGSpatialNoiseSettings.edge_mask2d_mode(value: PCGSpatialNoiseMask2DMode) -> None
unreal.PCGSpatialNoiseSettings.iterations(value: int) -> None
unreal.PCGSpatialNoiseSettings.mode(value: PCGSpatialNoiseMode) -> None
unreal.PCGSpatialNoiseSettings.random_offset(value: Vector) -> None
unreal.PCGSpatialNoiseSettings.tiled_voronoi_edge_blend_cell_count(value: int) -> None
unreal.PCGSpatialNoiseSettings.tiled_voronoi_resolution(value: int) -> None
unreal.PCGSpatialNoiseSettings.tiling(value: bool) -> None
unreal.PCGSpatialNoiseSettings.transform(value: Transform) -> None
unreal.PCGSpatialNoiseSettings.value_target(value: PCGAttributePropertyOutputNoSourceSelector) -> None
unreal.PCGSpatialNoiseSettings.voronoi_cell_id_target(value: PCGAttributePropertyOutputNoSourceSelector) -> None
unreal.PCGSpatialNoiseSettings.voronoi_cell_randomness(value: float) -> None
unreal.PCGSpatialNoiseSettings.voronoi_orient_samples_to_cell_edge(value: bool) -> None
```

## `unreal.PCGSpawnDynamicMeshSettings(PCGDynamicMeshBaseSettings)`

```python
unreal.PCGSpawnDynamicMeshSettings.post_process_function_names(value: Array[Name]) -> None
unreal.PCGSpawnDynamicMeshSettings.target_actor(value: Actor) -> None
```

## `unreal.PCGSpawnSplineMeshSettings(PCGSettings)`

```python
unreal.PCGSpawnSplineMeshSettings.post_process_function_names(value: Array[Name]) -> None
unreal.PCGSpawnSplineMeshSettings.spline_mesh_override_descriptions(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGSpawnSplineMeshSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGSpawnSplineSettings(PCGSettings)`

```python
unreal.PCGSpawnSplineSettings.component_reference_attribute_name(value: Name) -> None
unreal.PCGSpawnSplineSettings.output_spline_component_reference(value: bool) -> None
unreal.PCGSpawnSplineSettings.post_process_function_names(value: Array[Name]) -> None
unreal.PCGSpawnSplineSettings.property_override_descriptions(value: Array[PCGObjectPropertyOverrideDescription]) -> None
unreal.PCGSpawnSplineSettings.spawn_component_from_attribute(value: bool) -> None
unreal.PCGSpawnSplineSettings.spawn_component_from_attribute_name(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSpawnSplineSettings.spline_component(value: Class) -> None
```

## `unreal.PCGSplineMeshParams(StructBase)`

```python
unreal.PCGSplineMeshParams.__init__(forward_axis: PCGSplineMeshForwardAxis = PCGSplineMeshForwardAxis.X, scale_mesh_to_bounds: bool = False, scale_mesh_to_landscape_spline_full_width: bool = False, spline_up_dir: Vector = [0.000000, 0.000000, 0.000000], nanite_cluster_bounds_scale: float = 0.000000, spline_boundary_min: float = 0.000000, spline_boundary_max: float = 0.000000, smooth_interp_roll_scale: bool = False) -> None
unreal.PCGSplineMeshParams.forward_axis(value: PCGSplineMeshForwardAxis) -> None
unreal.PCGSplineMeshParams.nanite_cluster_bounds_scale(value: float) -> None
unreal.PCGSplineMeshParams.scale_mesh_to_bounds(value: bool) -> None
unreal.PCGSplineMeshParams.scale_mesh_to_landscape_spline_full_width(value: bool) -> None
unreal.PCGSplineMeshParams.smooth_interp_roll_scale(value: bool) -> None
unreal.PCGSplineMeshParams.spline_boundary_max(value: float) -> None
unreal.PCGSplineMeshParams.spline_boundary_min(value: float) -> None
unreal.PCGSplineMeshParams.spline_up_dir(value: Vector) -> None
```

## `unreal.PCGSplineProjectionData(PCGProjectionData)`

```python
unreal.PCGSplineProjectionData.projected_position(value: InterpCurveVector2D) -> None
```

## `unreal.PCGSplineSamplerParams(StructBase)`

```python
unreal.PCGSplineSamplerParams.__init__(dimension: PCGSplineSamplingDimension = PCGSplineSamplingDimension.ON_SPLINE, mode: PCGSplineSamplingMode = PCGSplineSamplingMode.SUBDIVISION, fill: PCGSplineSamplingFill = PCGSplineSamplingFill.FILL, subdivisions_per_segment: int = 0, distance_increment: float = 0.000000, num_samples: int = 0, num_planar_subdivisions: int = 0, num_height_subdivisions: int = 0, start_offset: float = 0.000000, end_offset: float = 0.000000, max_random_offset_normalized: float = 0.000000, fit_to_curve: bool = False, interior_sample_spacing: float = 0.000000, interior_border_sample_spacing: float = 0.000000, treat_spline_as_polyline: bool = False, interior_orientation: PCGSplineSamplingInteriorOrientation = PCGSplineSamplingInteriorOrientation.UNIFORM, project_onto_surface: bool = False, interior_density_falloff_curve: RuntimeFloatCurve = [], compute_direction_delta: bool = False, next_direction_delta_attribute: Name = "None", compute_curvature: bool = False, curvature_attribute: Name = "None", compute_segment_index: bool = False, segment_index_attribute: Name = "None", compute_subsegment_index: bool = False, subsegment_index_attribute: Name = "None", compute_tangents: bool = False, arrive_tangent_attribute: Name = "None", leave_tangent_attribute: Name = "None", compute_alpha: bool = False, alpha_attribute: Name = "None", compute_distance: bool = False, distance_attribute: Name = "None", compute_input_key: bool = False, input_key_attribute: Name = "None", unbounded: bool = False, point_steepness: float = 0.000000, seeding_mode: PCGSplineSamplingSeedingMode = PCGSplineSamplingSeedingMode.SEED_FROM_POSITION, seed_from_local_position: bool = False, seed_from2d_position: bool = False) -> None
unreal.PCGSplineSamplerParams.alpha_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.arrive_tangent_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.compute_alpha(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_curvature(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_direction_delta(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_distance(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_input_key(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_segment_index(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_subsegment_index(value: bool) -> None
unreal.PCGSplineSamplerParams.compute_tangents(value: bool) -> None
unreal.PCGSplineSamplerParams.curvature_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.dimension(value: PCGSplineSamplingDimension) -> None
unreal.PCGSplineSamplerParams.distance_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.distance_increment(value: float) -> None
unreal.PCGSplineSamplerParams.end_offset(value: float) -> None
unreal.PCGSplineSamplerParams.fill(value: PCGSplineSamplingFill) -> None
unreal.PCGSplineSamplerParams.fit_to_curve(value: bool) -> None
unreal.PCGSplineSamplerParams.input_key_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.interior_border_sample_spacing(value: float) -> None
unreal.PCGSplineSamplerParams.interior_density_falloff_curve(value: RuntimeFloatCurve) -> None
unreal.PCGSplineSamplerParams.interior_orientation(value: PCGSplineSamplingInteriorOrientation) -> None
unreal.PCGSplineSamplerParams.interior_sample_spacing(value: float) -> None
unreal.PCGSplineSamplerParams.leave_tangent_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.max_random_offset_normalized(value: float) -> None
unreal.PCGSplineSamplerParams.mode(value: PCGSplineSamplingMode) -> None
unreal.PCGSplineSamplerParams.next_direction_delta_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.num_height_subdivisions(value: int) -> None
unreal.PCGSplineSamplerParams.num_planar_subdivisions(value: int) -> None
unreal.PCGSplineSamplerParams.num_samples(value: int) -> None
unreal.PCGSplineSamplerParams.point_steepness(value: float) -> None
unreal.PCGSplineSamplerParams.project_onto_surface(value: bool) -> None
unreal.PCGSplineSamplerParams.seed_from2d_position(value: bool) -> None
unreal.PCGSplineSamplerParams.seed_from_local_position(value: bool) -> None
unreal.PCGSplineSamplerParams.seeding_mode(value: PCGSplineSamplingSeedingMode) -> None
unreal.PCGSplineSamplerParams.segment_index_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.start_offset(value: float) -> None
unreal.PCGSplineSamplerParams.subdivisions_per_segment(value: int) -> None
unreal.PCGSplineSamplerParams.subsegment_index_attribute(value: Name) -> None
unreal.PCGSplineSamplerParams.treat_spline_as_polyline(value: bool) -> None
unreal.PCGSplineSamplerParams.unbounded(value: bool) -> None
```

## `unreal.PCGSplineSamplerSettings(PCGSettings)`

```python
unreal.PCGSplineSamplerSettings.params(value: PCGSplineSamplerParams) -> None
unreal.PCGSplineSamplerSettings.sampler_params(value: PCGSplineSamplerParams) -> None
```

## `unreal.PCGSplineToSegmentSettings(PCGSettings)`

```python
unreal.PCGSplineToSegmentSettings.extract_angles(value: bool) -> None
unreal.PCGSplineToSegmentSettings.extract_clockwise_info(value: bool) -> None
unreal.PCGSplineToSegmentSettings.extract_connectivity_info(value: bool) -> None
unreal.PCGSplineToSegmentSettings.extract_tangents(value: bool) -> None
```

## `unreal.PCGSplitPointsSettings(PCGSettings)`

```python
unreal.PCGSplitPointsSettings.split_axis(value: PCGSplitAxis) -> None
unreal.PCGSplitPointsSettings.split_position(value: float) -> None
```

## `unreal.PCGSubdivideSegmentSettings(PCGSubdivisionBaseSettings)`

```python
unreal.PCGSubdivideSegmentSettings.accept_incomplete_subdivision(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.extremity_neighbor_index_attribute_name(value: Name) -> None
unreal.PCGSubdivideSegmentSettings.flip_axis_as_attribute(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.flip_axis_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSubdivideSegmentSettings.is_final_attribute_name(value: Name) -> None
unreal.PCGSubdivideSegmentSettings.is_first_attribute_name(value: Name) -> None
unreal.PCGSubdivideSegmentSettings.module_index_attribute_name(value: Name) -> None
unreal.PCGSubdivideSegmentSettings.output_extremity_attributes(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.output_extremity_neighbor_index_attribute(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.output_module_index_attribute(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.should_flip_axis(value: bool) -> None
unreal.PCGSubdivideSegmentSettings.subdivision_axis(value: PCGSplitAxis) -> None
```

## `unreal.PCGSubdivideSplineSettings(PCGSubdivisionBaseSettings)`

```python
unreal.PCGSubdivideSplineSettings.accept_incomplete_subdivision(value: bool) -> None
unreal.PCGSubdivideSplineSettings.is_final_attribute_name(value: Name) -> None
unreal.PCGSubdivideSplineSettings.is_first_attribute_name(value: Name) -> None
unreal.PCGSubdivideSplineSettings.module_height(value: float) -> None
unreal.PCGSubdivideSplineSettings.module_height_as_attribute(value: bool) -> None
unreal.PCGSubdivideSplineSettings.module_height_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSubdivideSplineSettings.module_index_attribute_name(value: Name) -> None
unreal.PCGSubdivideSplineSettings.output_extremity_attributes(value: bool) -> None
unreal.PCGSubdivideSplineSettings.output_module_index_attribute(value: bool) -> None
```

## `unreal.PCGSubdivisionBaseSettings(PCGSettings)`

```python
unreal.PCGSubdivisionBaseSettings.debug_color_attribute_name(value: Name) -> None
unreal.PCGSubdivisionBaseSettings.forward_attributes_from_modules_info(value: bool) -> None
unreal.PCGSubdivisionBaseSettings.grammar_selection(value: PCGGrammarSelection) -> None
unreal.PCGSubdivisionBaseSettings.module_info_as_input(value: bool) -> None
unreal.PCGSubdivisionBaseSettings.modules_info(value: Array[PCGSubdivisionSubmodule]) -> None
unreal.PCGSubdivisionBaseSettings.modules_info_attribute_names(value: PCGSubdivisionModuleAttributeNames) -> None
unreal.PCGSubdivisionBaseSettings.output_debug_color_attribute(value: bool) -> None
unreal.PCGSubdivisionBaseSettings.output_scalable_attribute(value: bool) -> None
unreal.PCGSubdivisionBaseSettings.output_size_attribute(value: bool) -> None
unreal.PCGSubdivisionBaseSettings.scalable_attribute_name(value: Name) -> None
unreal.PCGSubdivisionBaseSettings.seed_attribute(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGSubdivisionBaseSettings.size_attribute_name(value: Name) -> None
unreal.PCGSubdivisionBaseSettings.symbol_attribute_name(value: Name) -> None
unreal.PCGSubdivisionBaseSettings.use_seed_attribute(value: bool) -> None
```

## `unreal.PCGSubdivisionModuleAttributeNames(StructBase)`

```python
unreal.PCGSubdivisionModuleAttributeNames.__init__(symbol_attribute_name: Name = "None", size_attribute_name: Name = "None", provide_scalable: bool = False, scalable_attribute_name: Name = "None", provide_debug_color: bool = False, debug_color_attribute_name: Name = "None") -> None
unreal.PCGSubdivisionModuleAttributeNames.debug_color_attribute_name(value: Name) -> None
unreal.PCGSubdivisionModuleAttributeNames.provide_debug_color(value: bool) -> None
unreal.PCGSubdivisionModuleAttributeNames.provide_scalable(value: bool) -> None
unreal.PCGSubdivisionModuleAttributeNames.scalable_attribute_name(value: Name) -> None
unreal.PCGSubdivisionModuleAttributeNames.size_attribute_name(value: Name) -> None
unreal.PCGSubdivisionModuleAttributeNames.symbol_attribute_name(value: Name) -> None
```

## `unreal.PCGSubdivisionSubmodule(StructBase)`

```python
unreal.PCGSubdivisionSubmodule.__init__(symbol: Name = "None", size: float = 0.000000, scalable: bool = False, debug_color: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.PCGSubdivisionSubmodule.debug_color(value: Vector4) -> None
unreal.PCGSubdivisionSubmodule.scalable(value: bool) -> None
unreal.PCGSubdivisionSubmodule.size(value: float) -> None
unreal.PCGSubdivisionSubmodule.symbol(value: Name) -> None
```

## `unreal.PCGSurfaceData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGSurfaceData.local_bounds() -> Box
unreal.PCGSurfaceData.transform() -> Transform
```

## `unreal.PCGSurfaceSamplerSettings(PCGSettings)`

```python
unreal.PCGSurfaceSamplerSettings.apply_density_to_points(value: bool) -> None
unreal.PCGSurfaceSamplerSettings.keep_zero_density_points(value: bool) -> None
unreal.PCGSurfaceSamplerSettings.looseness(value: float) -> None
unreal.PCGSurfaceSamplerSettings.point_extents(value: Vector) -> None
unreal.PCGSurfaceSamplerSettings.point_steepness(value: float) -> None
unreal.PCGSurfaceSamplerSettings.points_per_squared_meter(value: float) -> None
unreal.PCGSurfaceSamplerSettings.unbounded(value: bool) -> None
```

## `unreal.PCGSwitchSettings(PCGSettings)`

```python
unreal.PCGSwitchSettings.enum_selection(value: EnumSelector) -> None
unreal.PCGSwitchSettings.int_options(value: Array[int]) -> None
unreal.PCGSwitchSettings.integer_selection(value: int) -> None
unreal.PCGSwitchSettings.selection_mode(value: PCGControlFlowSelectionMode) -> None
unreal.PCGSwitchSettings.string_options(value: Array[str]) -> None
unreal.PCGSwitchSettings.string_selection(value: str) -> None
```

## `unreal.PCGTaggedData(StructBase)`

```python
unreal.PCGTaggedData.__init__(data: PCGData = None, tags: Set[str] = [], pin: Name = "None", is_used_multiple_times: bool = False) -> None
unreal.PCGTaggedData.data(value: PCGData) -> None
unreal.PCGTaggedData.is_used_multiple_times() -> bool
unreal.PCGTaggedData.pin(value: Name) -> None
unreal.PCGTaggedData.tags(value: Set[str]) -> None
```

## `unreal.PCGTestMyColorStruct(StructBase)`

```python
unreal.PCGTestMyColorStruct.__init__(b: float = 0.000000, g: float = 0.000000, r: float = 0.000000, a: float = 0.000000) -> None
unreal.PCGTestMyColorStruct.a() -> float
unreal.PCGTestMyColorStruct.b() -> float
unreal.PCGTestMyColorStruct.g() -> float
unreal.PCGTestMyColorStruct.r() -> float
```

## `unreal.PCGUnionData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGUnionData.add_data(data: PCGSpatialData) -> None
unreal.PCGUnionData.data() -> Array[PCGSpatialData]
unreal.PCGUnionData.density_function(value: PCGUnionDensityFunction) -> None
unreal.PCGUnionData.initialize(a: PCGSpatialData, b: PCGSpatialData) -> None
unreal.PCGUnionData.union_type(value: PCGUnionType) -> None
```

## `unreal.PCGUnionSettings(PCGSettings)`

```python
unreal.PCGUnionSettings.density_function(value: PCGUnionDensityFunction) -> None
unreal.PCGUnionSettings.type(value: PCGUnionType) -> None
```

## `unreal.PCGUnitTestDummyComponent(ActorComponent)`

```python
unreal.PCGUnitTestDummyComponent.int_property() -> int
```

## `unreal.PCGUserParameterGetSettings(PCGSettings)`

```python
unreal.PCGUserParameterGetSettings.force_object_and_struct_extraction(value: bool) -> None
```

## `unreal.PCGVisualizeAttributeSettings(PCGSettings)`

```python
unreal.PCGVisualizeAttributeSettings.attribute_source(value: PCGAttributePropertyInputSelector) -> None
unreal.PCGVisualizeAttributeSettings.color(value: Color) -> None
unreal.PCGVisualizeAttributeSettings.custom_prefix_string(value: str) -> None
unreal.PCGVisualizeAttributeSettings.duration(value: float) -> None
unreal.PCGVisualizeAttributeSettings.local_offset(value: Vector) -> None
unreal.PCGVisualizeAttributeSettings.point_limit(value: int) -> None
unreal.PCGVisualizeAttributeSettings.prefix_with_attribute_name(value: bool) -> None
unreal.PCGVisualizeAttributeSettings.prefix_with_index(value: bool) -> None
unreal.PCGVisualizeAttributeSettings.visualize_enabled(value: bool) -> None
```

## `unreal.PCGVolume(Volume)`

```python
unreal.PCGVolume.pcg_component(value: PCGComponent) -> None
```

## `unreal.PCGVolumeData(PCGSpatialDataWithPointCache)`

```python
unreal.PCGVolumeData.volume(value: Volume) -> None
unreal.PCGVolumeData.voxel_size(value: Vector) -> None
```

## `unreal.PCGVolumeSamplerSettings(PCGSettings)`

```python
unreal.PCGVolumeSamplerSettings.point_steepness(value: float) -> None
unreal.PCGVolumeSamplerSettings.unbounded(value: bool) -> None
unreal.PCGVolumeSamplerSettings.voxel_size(value: Vector) -> None
```

## `unreal.PCGWeightedByCategoryEntryList(StructBase)`

```python
unreal.PCGWeightedByCategoryEntryList.__init__(category_entry: str = "", is_default: bool = False, weighted_mesh_entries: Array[PCGMeshSelectorWeightedEntry] = []) -> None
unreal.PCGWeightedByCategoryEntryList.category_entry(value: str) -> None
unreal.PCGWeightedByCategoryEntryList.is_default(value: bool) -> None
unreal.PCGWeightedByCategoryEntryList.weighted_mesh_entries(value: Array[PCGMeshSelectorWeightedEntry]) -> None
```

## `unreal.ProceduralFoliageComponent(ActorComponent)`

```python
unreal.ProceduralFoliageComponent.allow_bsp(value: bool) -> None
unreal.ProceduralFoliageComponent.allow_foliage(value: bool) -> None
unreal.ProceduralFoliageComponent.allow_landscape(value: bool) -> None
unreal.ProceduralFoliageComponent.allow_static_mesh(value: bool) -> None
unreal.ProceduralFoliageComponent.allow_translucent(value: bool) -> None
unreal.ProceduralFoliageComponent.foliage_spawner(value: ProceduralFoliageSpawner) -> None
unreal.ProceduralFoliageComponent.overlap(value: float) -> None
unreal.ProceduralFoliageComponent.procedural_foliage(value: ProceduralFoliageSpawner) -> None
unreal.ProceduralFoliageComponent.show_debug_tiles(value: bool) -> None
unreal.ProceduralFoliageComponent.tile_overlap(value: float) -> None
```

## `unreal.ProceduralFoliageEditorLibrary(BlueprintFunctionLibrary)`

```python
unreal.ProceduralFoliageEditorLibrary.clear_procedural_foliage_components(procedural_foliage_components: Array[ProceduralFoliageComponent]) -> None
unreal.ProceduralFoliageEditorLibrary.clear_procedural_foliage_volumes(procedural_foliage_volumes: Array[ProceduralFoliageVolume]) -> None
unreal.ProceduralFoliageEditorLibrary.resimulate_procedural_foliage_components(procedural_foliage_components: Array[ProceduralFoliageComponent]) -> None
unreal.ProceduralFoliageEditorLibrary.resimulate_procedural_foliage_volumes(procedural_foliage_volumes: Array[ProceduralFoliageVolume]) -> None
```

## `unreal.ProceduralFoliageInstance(StructBase)`

```python
unreal.ProceduralFoliageInstance.__init__(location: Vector = [0.000000, 0.000000, 0.000000], age: float = 0.000000, normal: Vector = [0.000000, 0.000000, 0.000000]) -> None
unreal.ProceduralFoliageInstance.age(value: float) -> None
unreal.ProceduralFoliageInstance.location(value: Vector) -> None
unreal.ProceduralFoliageInstance.normal(value: Vector) -> None
```

## `unreal.ProceduralFoliageSpawner(Object)`

```python
unreal.ProceduralFoliageSpawner.minimum_quad_tree_size() -> float
unreal.ProceduralFoliageSpawner.num_unique_tiles() -> int
unreal.ProceduralFoliageSpawner.random_seed() -> int
unreal.ProceduralFoliageSpawner.simulate(num_steps: int = -1) -> None
unreal.ProceduralFoliageSpawner.tile_size() -> float
```

## `unreal.ProceduralFoliageTypeData(FoliageTypeObject)`

```python
unreal.ProceduralFoliageTypeData.__init__() -> None
```

## `unreal.ProceduralFoliageVolume(Volume)`

```python
unreal.ProceduralFoliageVolume.procedural_component() -> ProceduralFoliageComponent
```

## `unreal.ProceduralMeshComponent(MeshComponent)`

```python
unreal.ProceduralMeshComponent.add_collision_convex_mesh(convex_verts: Array[Vector]) -> None
unreal.ProceduralMeshComponent.clear_all_mesh_sections() -> None
unreal.ProceduralMeshComponent.clear_collision_convex_meshes() -> None
unreal.ProceduralMeshComponent.clear_mesh_section(section_index: int) -> None
unreal.ProceduralMeshComponent.create_mesh_section(section_index: int, vertices: Array[Vector], triangles: Array[int], normals: Array[Vector], uv0: Array[Vector2D], vertex_colors: Array[Color], tangents: Array[ProcMeshTangent], create_collision: bool) -> None
unreal.ProceduralMeshComponent.create_mesh_section_linear_color(section_index: int, vertices: Array[Vector], triangles: Array[int], normals: Array[Vector], uv0: Array[Vector2D], uv1: Array[Vector2D], uv2: Array[Vector2D], uv3: Array[Vector2D], vertex_colors: Array[LinearColor], tangents: Array[ProcMeshTangent], create_collision: bool, srgb_conversion: bool = False) -> None
unreal.ProceduralMeshComponent.get_num_sections() -> int
unreal.ProceduralMeshComponent.is_mesh_section_visible(section_index: int) -> bool
unreal.ProceduralMeshComponent.set_mesh_section_visible(section_index: int, new_visibility: bool) -> None
unreal.ProceduralMeshComponent.update_mesh_section(section_index: int, vertices: Array[Vector], normals: Array[Vector], uv0: Array[Vector2D], vertex_colors: Array[Color], tangents: Array[ProcMeshTangent]) -> None
unreal.ProceduralMeshComponent.update_mesh_section_linear_color(section_index: int, vertices: Array[Vector], normals: Array[Vector], uv0: Array[Vector2D], uv1: Array[Vector2D], uv2: Array[Vector2D], uv3: Array[Vector2D], vertex_colors: Array[LinearColor], tangents: Array[ProcMeshTangent], srgb_conversion: bool = True) -> None
unreal.ProceduralMeshComponent.use_async_cooking() -> bool
unreal.ProceduralMeshComponent.use_complex_as_simple_collision() -> bool
```

## `unreal.ProceduralMeshLibrary(BlueprintFunctionLibrary)`

```python
unreal.ProceduralMeshLibrary.calculate_tangents_for_mesh(vertices: Array[Vector], triangles: Array[int], u_vs: Array[Vector2D]) -> Tuple[Array[Vector], Array[ProcMeshTangent]]
unreal.ProceduralMeshLibrary.convert_quad_to_triangles(triangles: Array[int], vert0: int, vert1: int, vert2: int, vert3: int) -> Array[int]
unreal.ProceduralMeshLibrary.copy_procedural_mesh_from_static_mesh_component(static_mesh_component: StaticMeshComponent, lod_index: int, proc_mesh_component: ProceduralMeshComponent, create_collision: bool) -> None
unreal.ProceduralMeshLibrary.create_grid_mesh_split(num_x: int, num_y: int, grid_spacing: float = 16.000000) -> Tuple[Array[int], Array[Vector], Array[Vector2D], Array[Vector2D]]
unreal.ProceduralMeshLibrary.create_grid_mesh_triangles(num_x: int, num_y: int, winding: bool) -> Array[int]
unreal.ProceduralMeshLibrary.create_grid_mesh_welded(num_x: int, num_y: int, grid_spacing: float = 16.000000) -> Tuple[Array[int], Array[Vector], Array[Vector2D]]
unreal.ProceduralMeshLibrary.generate_box_mesh(box_radius: Vector) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D], Array[ProcMeshTangent]]
unreal.ProceduralMeshLibrary.get_section_from_procedural_mesh(proc_mesh: ProceduralMeshComponent, section_index: int) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D], Array[ProcMeshTangent]]
unreal.ProceduralMeshLibrary.get_section_from_static_mesh(mesh: StaticMesh, lod_index: int, section_index: int) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector2D], Array[ProcMeshTangent]]
unreal.ProceduralMeshLibrary.slice_procedural_mesh(proc_mesh: ProceduralMeshComponent, plane_position: Vector, plane_normal: Vector, create_other_half: bool, cap_option: ProcMeshSliceCapOption, cap_material: MaterialInterface) -> ProceduralMeshComponent
```

## `unreal.PythonLandscapeLib(BlueprintFunctionLibrary)`

```python
unreal.PythonLandscapeLib.add_adjacent_landscape_proxy(world_in: World, source_landscape: LandscapeProxy, direction: int) -> LandscapeStreamingProxy
unreal.PythonLandscapeLib.assign_layer_info(landscape_proxy: LandscapeProxy, index: int, layer_info: LandscapeLayerInfoObject) -> bool
unreal.PythonLandscapeLib.cal_landscape_size(section_size: int, sections_per_component: int, component_count_x: int, component_count_y: int) -> Tuple[int, int]
unreal.PythonLandscapeLib.clear_all_layers(landscape_proxy: LandscapeProxy) -> bool
unreal.PythonLandscapeLib.clear_layer(landscape_proxy: LandscapeProxy, layer_name: str) -> bool
unreal.PythonLandscapeLib.create_landscape(landscape_transform: Transform, section_size: int, sections_per_component: int, component_count_x: int, component_count_y: int) -> Landscape
unreal.PythonLandscapeLib.create_landscape_proxy(landscape_transform: Transform, section_size: int, sections_per_component: int, component_count_x: int, component_count_y: int, shared_landscape_actor: Landscape) -> LandscapeStreamingProxy
unreal.PythonLandscapeLib.create_landscape_proxy_with_guid(landscape_transform: Transform, section_size: int, sections_per_component: int, component_count_x: int, component_count_y: int, guid: Guid, quads_space_offset_x: int = -1, quads_space_offset_y: int = -1) -> LandscapeStreamingProxy
unreal.PythonLandscapeLib.get_heightmap_data(landscape: LandscapeProxy) -> Array[int]
unreal.PythonLandscapeLib.get_landscape_components(landscape_proxy: LandscapeProxy) -> Array[LandscapeComponent]
unreal.PythonLandscapeLib.get_landscape_extent(landscape_proxy: LandscapeProxy) -> Tuple[int, int, int, int]
unreal.PythonLandscapeLib.get_landscape_guid(landscape_proxy: LandscapeProxy) -> Guid
unreal.PythonLandscapeLib.get_layer_names(landscape_proxy: LandscapeProxy) -> Array[str]
unreal.PythonLandscapeLib.get_used_paint_layers(landscape_proxy: LandscapeProxy) -> Array[str]
unreal.PythonLandscapeLib.get_visibility_data(landscape_proxy: LandscapeProxy) -> Optional[Array[int]]
unreal.PythonLandscapeLib.get_weightmap_data(landscape_proxy: LandscapeProxy, layer_name: str) -> Optional[Array[int]]
unreal.PythonLandscapeLib.landscape_flush_grass_components(landscape_proxy: LandscapeProxy, flush_grass_maps: bool = True) -> None
unreal.PythonLandscapeLib.landscape_get_grass_components(landscape_proxy: LandscapeProxy) -> Array[HierarchicalInstancedStaticMeshComponent]
unreal.PythonLandscapeLib.landscape_update_grass(landscape_proxy: LandscapeProxy, cameras: Array[Vector], force_sync: bool) -> None
unreal.PythonLandscapeLib.recalculate_normals(landscape_proxy: LandscapeProxy) -> bool
unreal.PythonLandscapeLib.set_heightmap_data(landscape: LandscapeProxy, height_data: Array[int]) -> bool
unreal.PythonLandscapeLib.set_weightmap_data(landscape_proxy: LandscapeProxy, layer_name: str, data: Array[int]) -> bool
```

## `unreal.RealCurve(IndexedCurve)`

```python
unreal.RealCurve.__init__() -> None
```

## `unreal.RichCurve(RealCurve)`

```python
unreal.RichCurve.__init__() -> None
```

## `unreal.RichCurveKey(StructBase)`

```python
unreal.RichCurveKey.__init__(interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_LINEAR, tangent_mode: RichCurveTangentMode = RichCurveTangentMode.RCTM_AUTO, tangent_weight_mode: RichCurveTangentWeightMode = RichCurveTangentWeightMode.RCTWM_WEIGHTED_NONE, time: float = 0.000000, value: float = 0.000000) -> None
unreal.RichCurveKey.interp_mode(value: RichCurveInterpMode) -> None
unreal.RichCurveKey.tangent_mode(value: RichCurveTangentMode) -> None
unreal.RichCurveKey.tangent_weight_mode(value: RichCurveTangentWeightMode) -> None
unreal.RichCurveKey.time(value: float) -> None
unreal.RichCurveKey.value(value: float) -> None
```

## `unreal.RigCurve(RigElement)`

```python
unreal.RigCurve.__init__(name: Name = "None", index: int = 0, value: float = 0.000000) -> None
unreal.RigCurve.value() -> float
```

## `unreal.RigCurveElement(RigBaseElement)`

```python
unreal.RigCurveElement.__init__(key: RigElementKey = [RigElementType.NONE, "None"], index: int = 0, sub_index: int = 0, created_at_instruction_index: int = 0, selected: bool = False) -> None
```

## `unreal.RigUnit_CurveExists(RigUnit)`

```python
unreal.RigUnit_CurveExists.__init__(curve: Name = "None", exists: bool = False) -> None
unreal.RigUnit_CurveExists.curve(value: Name) -> None
unreal.RigUnit_CurveExists.exists() -> bool
```

## `unreal.RigUnit_FitChainToCurve(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitChainToCurve.__init__(execute_context: ControlRigExecuteContext = [], start_bone: Name = "None", end_bone: Name = "None", bezier: RigVMFourPointBezier = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, sampling_precision: int = 0, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], pole_vector_position: Vector = [0.000000, 0.000000, 0.000000], rotations: Array[RigUnit_FitChainToCurve_Rotation] = [], rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_FitChainToCurve_DebugSettings = [False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000], [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_FitChainToCurve.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_FitChainToCurve.bezier(value: RigVMFourPointBezier) -> None
unreal.RigUnit_FitChainToCurve.debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
unreal.RigUnit_FitChainToCurve.end_bone(value: Name) -> None
unreal.RigUnit_FitChainToCurve.maximum() -> float
unreal.RigUnit_FitChainToCurve.minimum() -> float
unreal.RigUnit_FitChainToCurve.pole_vector_position(value: Vector) -> None
unreal.RigUnit_FitChainToCurve.primary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurve.propagate_to_children() -> bool
unreal.RigUnit_FitChainToCurve.rotation_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_FitChainToCurve.rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
unreal.RigUnit_FitChainToCurve.sampling_precision() -> int
unreal.RigUnit_FitChainToCurve.secondary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurve.start_bone(value: Name) -> None
unreal.RigUnit_FitChainToCurve.weight(value: float) -> None
```

## `unreal.RigUnit_FitChainToCurveItemArray(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitChainToCurveItemArray.__init__(execute_context: ControlRigExecuteContext = [], items: Array[RigElementKey] = [], bezier: RigVMFourPointBezier = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, sampling_precision: int = 0, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], pole_vector_position: Vector = [0.000000, 0.000000, 0.000000], rotations: Array[RigUnit_FitChainToCurve_Rotation] = [], rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_FitChainToCurve_DebugSettings = [False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000], [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_FitChainToCurveItemArray.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_FitChainToCurveItemArray.bezier(value: RigVMFourPointBezier) -> None
unreal.RigUnit_FitChainToCurveItemArray.debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
unreal.RigUnit_FitChainToCurveItemArray.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_FitChainToCurveItemArray.maximum() -> float
unreal.RigUnit_FitChainToCurveItemArray.minimum() -> float
unreal.RigUnit_FitChainToCurveItemArray.pole_vector_position(value: Vector) -> None
unreal.RigUnit_FitChainToCurveItemArray.primary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurveItemArray.propagate_to_children() -> bool
unreal.RigUnit_FitChainToCurveItemArray.rotation_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_FitChainToCurveItemArray.rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
unreal.RigUnit_FitChainToCurveItemArray.sampling_precision() -> int
unreal.RigUnit_FitChainToCurveItemArray.secondary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurveItemArray.weight(value: float) -> None
```

## `unreal.RigUnit_FitChainToCurvePerItem(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitChainToCurvePerItem.__init__(execute_context: ControlRigExecuteContext = [], items: RigElementKeyCollection = [[]], bezier: RigVMFourPointBezier = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, sampling_precision: int = 0, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], pole_vector_position: Vector = [0.000000, 0.000000, 0.000000], rotations: Array[RigUnit_FitChainToCurve_Rotation] = [], rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_FitChainToCurve_DebugSettings = [False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000], [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_FitChainToCurvePerItem.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_FitChainToCurvePerItem.bezier(value: RigVMFourPointBezier) -> None
unreal.RigUnit_FitChainToCurvePerItem.debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
unreal.RigUnit_FitChainToCurvePerItem.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_FitChainToCurvePerItem.maximum() -> float
unreal.RigUnit_FitChainToCurvePerItem.minimum() -> float
unreal.RigUnit_FitChainToCurvePerItem.pole_vector_position(value: Vector) -> None
unreal.RigUnit_FitChainToCurvePerItem.primary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurvePerItem.propagate_to_children() -> bool
unreal.RigUnit_FitChainToCurvePerItem.rotation_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_FitChainToCurvePerItem.rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
unreal.RigUnit_FitChainToCurvePerItem.sampling_precision() -> int
unreal.RigUnit_FitChainToCurvePerItem.secondary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToCurvePerItem.weight(value: float) -> None
```

## `unreal.RigUnit_FitChainToCurve_DebugSettings(StructBase)`

```python
unreal.RigUnit_FitChainToCurve_DebugSettings.__init__(enabled: bool = False, scale: float = 0.000000, curve_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], segments_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], world_offset: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]) -> None
unreal.RigUnit_FitChainToCurve_DebugSettings.curve_color(value: LinearColor) -> None
unreal.RigUnit_FitChainToCurve_DebugSettings.enabled(value: bool) -> None
unreal.RigUnit_FitChainToCurve_DebugSettings.scale(value: float) -> None
unreal.RigUnit_FitChainToCurve_DebugSettings.segments_color(value: LinearColor) -> None
unreal.RigUnit_FitChainToCurve_DebugSettings.world_offset(value: Transform) -> None
```

## `unreal.RigUnit_FitChainToCurve_Rotation(StructBase)`

```python
unreal.RigUnit_FitChainToCurve_Rotation.__init__(rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000], ratio: float = 0.000000) -> None
unreal.RigUnit_FitChainToCurve_Rotation.ratio() -> float
unreal.RigUnit_FitChainToCurve_Rotation.rotation(value: Quat) -> None
```

## `unreal.RigUnit_FitChainToSplineCurve(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitChainToSplineCurve.__init__(execute_context: ControlRigExecuteContext = [], items: RigElementKeyCollection = [[]], spline: ControlRigSpline = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, sampling_precision: int = 0, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], pole_vector_position: Vector = [0.000000, 0.000000, 0.000000], rotations: Array[RigUnit_FitChainToCurve_Rotation] = [], rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_FitChainToCurve_DebugSettings = [False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000], [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_FitChainToSplineCurve.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_FitChainToSplineCurve.debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
unreal.RigUnit_FitChainToSplineCurve.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_FitChainToSplineCurve.maximum() -> float
unreal.RigUnit_FitChainToSplineCurve.minimum() -> float
unreal.RigUnit_FitChainToSplineCurve.pole_vector_position(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurve.primary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurve.propagate_to_children() -> bool
unreal.RigUnit_FitChainToSplineCurve.rotation_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_FitChainToSplineCurve.rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
unreal.RigUnit_FitChainToSplineCurve.sampling_precision() -> int
unreal.RigUnit_FitChainToSplineCurve.secondary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurve.spline(value: ControlRigSpline) -> None
unreal.RigUnit_FitChainToSplineCurve.weight(value: float) -> None
```

## `unreal.RigUnit_FitChainToSplineCurveItemArray(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitChainToSplineCurveItemArray.__init__(execute_context: ControlRigExecuteContext = [], items: Array[RigElementKey] = [], spline: ControlRigSpline = [], alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT, minimum: float = 0.000000, maximum: float = 0.000000, sampling_precision: int = 0, primary_axis: Vector = [0.000000, 0.000000, 0.000000], secondary_axis: Vector = [0.000000, 0.000000, 0.000000], pole_vector_position: Vector = [0.000000, 0.000000, 0.000000], rotations: Array[RigUnit_FitChainToCurve_Rotation] = [], rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR, weight: float = 0.000000, propagate_to_children: bool = False, debug_settings: RigUnit_FitChainToCurve_DebugSettings = [False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000], [1.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]]) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.alignment() -> ControlRigCurveAlignment
unreal.RigUnit_FitChainToSplineCurveItemArray.debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.maximum() -> float
unreal.RigUnit_FitChainToSplineCurveItemArray.minimum() -> float
unreal.RigUnit_FitChainToSplineCurveItemArray.pole_vector_position(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.primary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.propagate_to_children() -> bool
unreal.RigUnit_FitChainToSplineCurveItemArray.rotation_ease_type() -> RigVMAnimEasingType
unreal.RigUnit_FitChainToSplineCurveItemArray.rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.sampling_precision() -> int
unreal.RigUnit_FitChainToSplineCurveItemArray.secondary_axis(value: Vector) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.spline(value: ControlRigSpline) -> None
unreal.RigUnit_FitChainToSplineCurveItemArray.weight(value: float) -> None
```

## `unreal.RigUnit_FitSplineCurveToChain(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitSplineCurveToChain.__init__(execute_context: ControlRigExecuteContext = [], items: RigElementKeyCollection = [[]], spline: ControlRigSpline = []) -> None
unreal.RigUnit_FitSplineCurveToChain.items(value: RigElementKeyCollection) -> None
unreal.RigUnit_FitSplineCurveToChain.spline(value: ControlRigSpline) -> None
```

## `unreal.RigUnit_FitSplineCurveToChainItemArray(RigUnit_HighlevelBaseMutable)`

```python
unreal.RigUnit_FitSplineCurveToChainItemArray.__init__(execute_context: ControlRigExecuteContext = [], items: Array[RigElementKey] = [], spline: ControlRigSpline = []) -> None
unreal.RigUnit_FitSplineCurveToChainItemArray.items(value: Array[RigElementKey]) -> None
unreal.RigUnit_FitSplineCurveToChainItemArray.spline(value: ControlRigSpline) -> None
```

## `unreal.RigUnit_GetCurveValue(RigUnit)`

```python
unreal.RigUnit_GetCurveValue.__init__(curve: Name = "None", valid: bool = False, value: float = 0.000000) -> None
unreal.RigUnit_GetCurveValue.curve(value: Name) -> None
unreal.RigUnit_GetCurveValue.valid() -> bool
unreal.RigUnit_GetCurveValue.value() -> float
```

## `unreal.RigUnit_SetCurveValue(RigUnitMutable)`

```python
unreal.RigUnit_SetCurveValue.__init__(execute_context: ControlRigExecuteContext = [], curve: Name = "None", value: float = 0.000000) -> None
unreal.RigUnit_SetCurveValue.curve(value: Name) -> None
unreal.RigUnit_SetCurveValue.value(value: float) -> None
```

## `unreal.RigUnit_SetSplinePoints(RigUnitMutable)`

```python
unreal.RigUnit_SetSplinePoints.__init__(execute_context: ControlRigExecuteContext = [], points: Array[Vector] = [], spline: ControlRigSpline = []) -> None
unreal.RigUnit_SetSplinePoints.points(value: Array[Vector]) -> None
unreal.RigUnit_SetSplinePoints.spline(value: ControlRigSpline) -> None
```

## `unreal.RigUnit_UnsetCurveValue(RigUnitMutable)`

```python
unreal.RigUnit_UnsetCurveValue.__init__(execute_context: ControlRigExecuteContext = [], curve: Name = "None") -> None
unreal.RigUnit_UnsetCurveValue.curve(value: Name) -> None
```

## `unreal.RuntimeCurveLinearColor(StructBase)`

```python
unreal.RuntimeCurveLinearColor.__init__() -> None
```

## `unreal.RuntimeFloatCurve(StructBase)`

```python
unreal.RuntimeFloatCurve.__init__() -> None
```

## `unreal.RuntimeVectorCurve(StructBase)`

```python
unreal.RuntimeVectorCurve.__init__() -> None
```

## `unreal.SequencerCurveEditorObject(Object)`

```python
unreal.SequencerCurveEditorObject.apply_filter(filter: CurveEditorFilterBase) -> None
unreal.SequencerCurveEditorObject.close_curve_editor() -> None
unreal.SequencerCurveEditorObject.delete_color_for_channels(class_: Class) -> str
unreal.SequencerCurveEditorObject.empty_selection() -> None
unreal.SequencerCurveEditorObject.get_channels_with_selected_keys() -> Array[SequencerChannelProxy]
unreal.SequencerCurveEditorObject.get_custom_color_for_channel(class_: Class, identifier: str) -> LinearColor
unreal.SequencerCurveEditorObject.get_selected_keys(channel_proxy: SequencerChannelProxy) -> Array[int]
unreal.SequencerCurveEditorObject.has_custom_color_for_channel(class_: Class, identifier: str) -> bool
unreal.SequencerCurveEditorObject.is_curve_editor_open() -> bool
unreal.SequencerCurveEditorObject.is_curve_shown(channel: SequencerChannelProxy) -> bool
unreal.SequencerCurveEditorObject.open_curve_editor() -> None
unreal.SequencerCurveEditorObject.select_keys(channel: SequencerChannelProxy, indices: Array[int]) -> None
unreal.SequencerCurveEditorObject.set_custom_color_for_channel(class_: Class, identifier: str, new_color: LinearColor) -> None
unreal.SequencerCurveEditorObject.set_custom_color_for_channels(class_: Class, identifiers: Array[str], new_colors: Array[LinearColor]) -> None
unreal.SequencerCurveEditorObject.set_random_color_for_channels(class_: Class, identifiers: Array[str]) -> None
unreal.SequencerCurveEditorObject.show_curve(channel: SequencerChannelProxy, show_curve: bool) -> None
```

## `unreal.ShallowWaterSimulationGrid(StructBase)`

```python
unreal.ShallowWaterSimulationGrid.__init__() -> None
```

## `unreal.SoftSplineMeshComponentDescriptor(SplineMeshComponentDescriptorBase)`

```python
unreal.SoftSplineMeshComponentDescriptor.__init__() -> None
```

## `unreal.SourceGeometryPartID(ElementID)`

```python
unreal.SourceGeometryPartID.__init__(id_value: int = 0) -> None
```

## `unreal.SplineComponent(PrimitiveComponent)`

```python
unreal.SplineComponent.add_point(point: SplinePoint, update_spline: bool = True) -> None
unreal.SplineComponent.add_points(points: Array[SplinePoint], update_spline: bool = True) -> None
unreal.SplineComponent.add_spline_local_point(position: Vector) -> None
unreal.SplineComponent.add_spline_point(position: Vector, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.add_spline_point_at_index(position: Vector, index: int, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.add_spline_world_point(position: Vector) -> None
unreal.SplineComponent.b_always_render_in_editor(value: bool) -> None
unreal.SplineComponent.clear_spline_points(update_spline: bool = True) -> None
unreal.SplineComponent.convert_spline_segment_to_poly_line(spline_point_start_index: int, coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float) -> Optional[Array[Vector]]
unreal.SplineComponent.convert_spline_to_poly_line(coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float) -> Optional[Array[Vector]]
unreal.SplineComponent.convert_spline_to_poly_line_with_distances(coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float) -> Optional[Tuple[Array[Vector], Array[float]]]
unreal.SplineComponent.convert_spline_to_polyline_in_distance_range(coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float, start_dist_along_spline: float, end_dist_along_spline: float, allow_wrapping_if_closed: bool = True) -> Optional[Tuple[Array[Vector], Array[float]]]
unreal.SplineComponent.convert_spline_to_polyline_in_time_range(coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float, start_time_along_spline: float, end_time_along_spline: float, use_constant_velocity: bool, allow_wrapping_if_closed: bool = True) -> Optional[Tuple[Array[Vector], Array[float]]]
unreal.SplineComponent.default_up_vector(value: Vector) -> None
unreal.SplineComponent.divide_spline_into_polyline_recursive(start_distance_along_spline: float, end_distance_along_spline: float, coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float) -> Optional[Array[Vector]]
unreal.SplineComponent.divide_spline_into_polyline_recursive_with_distances(start_distance_along_spline: float, end_distance_along_spline: float, coordinate_space: SplineCoordinateSpace, max_square_distance_from_spline: float) -> Optional[Tuple[Array[Vector], Array[float]]]
unreal.SplineComponent.draw_debug(value: bool) -> None
unreal.SplineComponent.duration(value: float) -> None
unreal.SplineComponent.find_direction_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.find_input_key_closest_to_world_location(world_location: Vector) -> float
unreal.SplineComponent.find_location_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.find_right_vector_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.find_roll_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> float
unreal.SplineComponent.find_rotation_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Rotator
unreal.SplineComponent.find_scale_closest_to_world_location(world_location: Vector) -> Vector
unreal.SplineComponent.find_tangent_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.find_transform_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace, use_scale: bool = False) -> Transform
unreal.SplineComponent.find_up_vector_closest_to_world_location(world_location: Vector, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_arrive_tangent_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_default_up_vector(coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_direction_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_direction_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_direction_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_direction_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_distance_along_spline_at_location(location: Vector, coordinate_space: SplineCoordinateSpace) -> float
unreal.SplineComponent.get_distance_along_spline_at_spline_input_key(key: float) -> float
unreal.SplineComponent.get_distance_along_spline_at_spline_point(point_index: int) -> float
unreal.SplineComponent.get_float_property_at_spline_input_key(key: float, property_name: Name) -> float
unreal.SplineComponent.get_float_property_at_spline_point(index: int, property_name: Name) -> float
unreal.SplineComponent.get_input_key_at_distance_along_spline(distance: float) -> float
unreal.SplineComponent.get_input_key_value_at_distance_along_spline(distance: float) -> float
unreal.SplineComponent.get_input_key_value_at_spline_point(point_index: int) -> float
unreal.SplineComponent.get_leave_tangent_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_local_location_and_tangent_at_spline_point(point_index: int) -> Tuple[Vector, Vector]
unreal.SplineComponent.get_location_and_tangent_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Tuple[Vector, Vector]
unreal.SplineComponent.get_location_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_location_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_location_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_location_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_num_spline_points() -> int
unreal.SplineComponent.get_number_of_spline_points() -> int
unreal.SplineComponent.get_number_of_spline_segments() -> int
unreal.SplineComponent.get_right_vector_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_right_vector_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_right_vector_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_right_vector_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_roll_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> float
unreal.SplineComponent.get_roll_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> float
unreal.SplineComponent.get_roll_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> float
unreal.SplineComponent.get_roll_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> float
unreal.SplineComponent.get_rotation_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Rotator
unreal.SplineComponent.get_rotation_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Rotator
unreal.SplineComponent.get_rotation_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Rotator
unreal.SplineComponent.get_rotation_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Rotator
unreal.SplineComponent.get_scale_at_distance_along_spline(distance: float) -> Vector
unreal.SplineComponent.get_scale_at_spline_input_key(key: float) -> Vector
unreal.SplineComponent.get_scale_at_spline_point(point_index: int) -> Vector
unreal.SplineComponent.get_scale_at_time(time: float, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_spline_length() -> float
unreal.SplineComponent.get_spline_point_at(point_index: int, coordinate_space: SplineCoordinateSpace) -> SplinePoint
unreal.SplineComponent.get_spline_point_type(point_index: int) -> SplinePointType
unreal.SplineComponent.get_tangent_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_tangent_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_tangent_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_tangent_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_time_at_distance_along_spline(distance: float) -> float
unreal.SplineComponent.get_transform_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace, use_scale: bool = False) -> Transform
unreal.SplineComponent.get_transform_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace, use_scale: bool = False) -> Transform
unreal.SplineComponent.get_transform_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace, use_scale: bool = False) -> Transform
unreal.SplineComponent.get_transform_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False, use_scale: bool = False) -> Transform
unreal.SplineComponent.get_up_vector_at_distance_along_spline(distance: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_up_vector_at_spline_input_key(key: float, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_up_vector_at_spline_point(point_index: int, coordinate_space: SplineCoordinateSpace) -> Vector
unreal.SplineComponent.get_up_vector_at_time(time: float, coordinate_space: SplineCoordinateSpace, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_vector_property_at_spline_input_key(key: float, property_name: Name) -> Vector
unreal.SplineComponent.get_vector_property_at_spline_point(index: int, property_name: Name) -> Vector
unreal.SplineComponent.get_world_direction_at_distance_along_spline(distance: float) -> Vector
unreal.SplineComponent.get_world_direction_at_time(time: float, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_world_location_at_distance_along_spline(distance: float) -> Vector
unreal.SplineComponent.get_world_location_at_spline_point(point_index: int) -> Vector
unreal.SplineComponent.get_world_location_at_time(time: float, use_constant_velocity: bool = False) -> Vector
unreal.SplineComponent.get_world_rotation_at_distance_along_spline(distance: float) -> Rotator
unreal.SplineComponent.get_world_rotation_at_time(time: float, use_constant_velocity: bool = False) -> Rotator
unreal.SplineComponent.get_world_tangent_at_distance_along_spline(distance: float) -> Vector
unreal.SplineComponent.input_spline_points_to_construction_script(value: bool) -> None
unreal.SplineComponent.is_closed_loop() -> bool
unreal.SplineComponent.remove_spline_point(index: int, update_spline: bool = True) -> None
unreal.SplineComponent.set_closed_loop(closed_loop: bool, update_spline: bool = True) -> None
unreal.SplineComponent.set_closed_loop_at_position(closed_loop: bool, key: float, update_spline: bool = True) -> None
unreal.SplineComponent.set_default_up_vector(up_vector: Vector, coordinate_space: SplineCoordinateSpace) -> None
unreal.SplineComponent.set_draw_debug(show: bool) -> None
unreal.SplineComponent.set_location_at_spline_point(point_index: int, location: Vector, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_override_construction_script(override: bool) -> None
unreal.SplineComponent.set_rotation_at_spline_point(point_index: int, rotation: Rotator, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_scale_at_spline_point(point_index: int, scale_vector: Vector, update_spline: bool = True) -> None
unreal.SplineComponent.set_selected_spline_segment_color(segment_color: LinearColor) -> None
unreal.SplineComponent.set_spline_local_points(points: Array[Vector]) -> None
unreal.SplineComponent.set_spline_point_type(point_index: int, type: SplinePointType, update_spline: bool = True) -> None
unreal.SplineComponent.set_spline_points(points: Array[Vector], coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_spline_world_points(points: Array[Vector]) -> None
unreal.SplineComponent.set_tangent_at_spline_point(point_index: int, tangent: Vector, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_tangent_color(tangent_color: LinearColor) -> None
unreal.SplineComponent.set_tangents_at_spline_point(point_index: int, arrive_tangent: Vector, leave_tangent: Vector, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_unselected_spline_segment_color(segment_color: LinearColor) -> None
unreal.SplineComponent.set_up_vector_at_spline_point(point_index: int, up_vector: Vector, coordinate_space: SplineCoordinateSpace, update_spline: bool = True) -> None
unreal.SplineComponent.set_world_location_at_spline_point(point_index: int, location: Vector) -> None
unreal.SplineComponent.stationary_endpoints(value: bool) -> None
unreal.SplineComponent.update_spline() -> None
```

## `unreal.SplineCurves(StructBase)`

```python
unreal.SplineCurves.__init__() -> None
```

## `unreal.SplineMeshComponent(StaticMeshComponent)`

```python
unreal.SplineMeshComponent.get_boundary_max() -> float
unreal.SplineMeshComponent.get_boundary_min() -> float
unreal.SplineMeshComponent.get_end_offset() -> Vector2D
unreal.SplineMeshComponent.get_end_position() -> Vector
unreal.SplineMeshComponent.get_end_roll() -> float
unreal.SplineMeshComponent.get_end_scale() -> Vector2D
unreal.SplineMeshComponent.get_end_tangent() -> Vector
unreal.SplineMeshComponent.get_forward_axis() -> SplineMeshAxis
unreal.SplineMeshComponent.get_spline_up_dir() -> Vector
unreal.SplineMeshComponent.get_start_offset() -> Vector2D
unreal.SplineMeshComponent.get_start_position() -> Vector
unreal.SplineMeshComponent.get_start_roll() -> float
unreal.SplineMeshComponent.get_start_scale() -> Vector2D
unreal.SplineMeshComponent.get_start_tangent() -> Vector
unreal.SplineMeshComponent.set_boundary_max(boundary_max: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_boundary_min(boundary_min: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_offset(end_offset: Vector2D, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_position(end_pos: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_roll(end_roll: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_roll_degrees(end_roll_degrees: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_scale(end_scale: Vector2D = [1.000000, 1.000000], update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_end_tangent(end_tangent: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_forward_axis(forward_axis: SplineMeshAxis, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_spline_up_dir(spline_up_dir: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_and_end(start_pos: Vector, start_tangent: Vector, end_pos: Vector, end_tangent: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_offset(start_offset: Vector2D, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_position(start_pos: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_roll(start_roll: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_roll_degrees(start_roll_degrees: float, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_scale(start_scale: Vector2D = [1.000000, 1.000000], update_mesh: bool = True) -> None
unreal.SplineMeshComponent.set_start_tangent(start_tangent: Vector, update_mesh: bool = True) -> None
unreal.SplineMeshComponent.update_mesh() -> None
```

## `unreal.SplineMeshComponentDescriptorBase(StructBase)`

```python
unreal.SplineMeshComponentDescriptorBase.__init__() -> None
```

## `unreal.SplineMeshParams(StructBase)`

```python
unreal.SplineMeshParams.__init__() -> None
```

## `unreal.SplinePoint(StructBase)`

```python
unreal.SplinePoint.__init__(input_key: float = 0.000000, position: Vector = [0.000000, 0.000000, 0.000000], arrive_tangent: Vector = [0.000000, 0.000000, 0.000000], leave_tangent: Vector = [0.000000, 0.000000, 0.000000], rotation: Rotator = [0.000000, 0.000000, 0.000000], scale: Vector = [0.000000, 0.000000, 0.000000], type: SplinePointType = SplinePointType.LINEAR) -> None
unreal.SplinePoint.arrive_tangent(value: Vector) -> None
unreal.SplinePoint.input_key(value: float) -> None
unreal.SplinePoint.leave_tangent(value: Vector) -> None
unreal.SplinePoint.position(value: Vector) -> None
unreal.SplinePoint.rotation(value: Rotator) -> None
unreal.SplinePoint.scale(value: Vector) -> None
unreal.SplinePoint.type(value: SplinePointType) -> None
```

## `unreal.SpriteGeometryCollection(StructBase)`

```python
unreal.SpriteGeometryCollection.__init__() -> None
```

## `unreal.SpriteGeometryShape(StructBase)`

```python
unreal.SpriteGeometryShape.__init__() -> None
```

## `unreal.TimeStretchCurve(StructBase)`

```python
unreal.TimeStretchCurve.__init__() -> None
```

## `unreal.TimeStretchCurveMarker(StructBase)`

```python
unreal.TimeStretchCurveMarker.__init__() -> None
```

## `unreal.ToggleWaterDataParams(ParamsBase)`

```python
unreal.ToggleWaterDataParams.__init__(show_water: bool = False, refresh_scene: bool = False) -> None
unreal.ToggleWaterDataParams.refresh_scene(value: bool) -> None
unreal.ToggleWaterDataParams.show_water(value: bool) -> None
```

## `unreal.UsdGeometryCacheAssetUserData(UsdMeshAssetUserData)`

```python
unreal.UsdGeometryCacheAssetUserData.layer_start_offset_seconds(value: float) -> None
```

## `unreal.VectorCurve(AnimCurveBase)`

```python
unreal.VectorCurve.__init__() -> None
```

## `unreal.WaterBody(Actor)`

```python
unreal.WaterBody.get_audio_intensity_at_spline_input_key(key: float) -> float
unreal.WaterBody.get_exclusion_volumes() -> Array[WaterBodyExclusionVolume]
unreal.WaterBody.get_islands() -> Array[WaterBodyIsland]
unreal.WaterBody.get_river_to_lake_transition_material_instance() -> MaterialInstanceDynamic
unreal.WaterBody.get_river_to_ocean_transition_material_instance() -> MaterialInstanceDynamic
unreal.WaterBody.get_water_body_component() -> WaterBodyComponent
unreal.WaterBody.get_water_body_type() -> WaterBodyType
unreal.WaterBody.get_water_material_instance() -> MaterialInstanceDynamic
unreal.WaterBody.get_water_spline() -> WaterSplineComponent
unreal.WaterBody.get_water_velocity_at_spline_input_key(key: float) -> float
unreal.WaterBody.get_water_velocity_vector_at_spline_input_key(key: float) -> Vector
unreal.WaterBody.on_water_body_changed(shape_or_position_changed: bool, weightmap_settings_changed: bool = False) -> None
unreal.WaterBody.set_water_material(material: MaterialInterface) -> None
unreal.WaterBody.set_water_waves(water_waves: WaterWavesBase) -> None
unreal.WaterBody.spline_comp() -> WaterSplineComponent
unreal.WaterBody.water_body_component() -> WaterBodyComponent
unreal.WaterBody.water_body_index() -> int
unreal.WaterBody.water_waves() -> WaterWavesBase
```

## `unreal.WaterBodyBrushCache(StructBase)`

```python
unreal.WaterBodyBrushCache.__init__(cache_render_target: TextureRenderTarget2D = None, cache_is_valid: bool = False) -> None
unreal.WaterBodyBrushCache.cache_is_valid(value: bool) -> None
unreal.WaterBodyBrushCache.cache_render_target(value: TextureRenderTarget2D) -> None
```

## `unreal.WaterBodyBrushCacheContainer(Object)`

```python
unreal.WaterBodyBrushCacheContainer.cache(value: WaterBodyBrushCache) -> None
```

## `unreal.WaterBodyComponent(PrimitiveComponent)`

```python
unreal.WaterBodyComponent.affects_landscape(value: bool) -> None
unreal.WaterBodyComponent.always_generate_water_mesh_tiles() -> bool
unreal.WaterBodyComponent.collision_height_offset(value: float) -> None
unreal.WaterBodyComponent.curve_settings(value: WaterCurveSettings) -> None
unreal.WaterBodyComponent.get_collision_components(only_enabled_components: bool = True) -> Array[PrimitiveComponent]
unreal.WaterBodyComponent.get_exclusion_volumes() -> Array[WaterBodyExclusionVolume]
unreal.WaterBodyComponent.get_islands() -> Array[WaterBodyIsland]
unreal.WaterBodyComponent.get_max_wave_height() -> float
unreal.WaterBodyComponent.get_river_to_lake_transition_material() -> MaterialInterface
unreal.WaterBodyComponent.get_river_to_lake_transition_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_river_to_ocean_transition_material() -> MaterialInterface
unreal.WaterBodyComponent.get_river_to_ocean_transition_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_standard_renderable_components() -> Array[PrimitiveComponent]
unreal.WaterBodyComponent.get_underwater_post_process_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_water_body_actor() -> WaterBody
unreal.WaterBodyComponent.get_water_info_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_water_lod_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_water_material() -> MaterialInterface
unreal.WaterBodyComponent.get_water_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_water_spline() -> WaterSplineComponent
unreal.WaterBodyComponent.get_water_static_mesh_material_instance() -> MaterialInstanceDynamic
unreal.WaterBodyComponent.get_water_surface_info_at_location(location: Vector, include_depth: bool = False) -> Tuple[Vector, Vector, Vector, float]
unreal.WaterBodyComponent.get_water_velocity_at_spline_input_key(key: float) -> float
unreal.WaterBodyComponent.get_water_waves() -> WaterWavesBase
unreal.WaterBodyComponent.layer_weightmap_settings(value: Map[Name, WaterBodyWeightmapSettings]) -> None
unreal.WaterBodyComponent.on_water_body_changed(shape_or_position_changed: bool, weightmap_settings_changed: bool = False, user_triggered_changed: bool = False) -> None
unreal.WaterBodyComponent.overlap_material_priority() -> int
unreal.WaterBodyComponent.set_underwater_post_process_material(material: MaterialInterface) -> None
unreal.WaterBodyComponent.set_water_and_under_water_post_process_material(water_material: MaterialInterface, under_water_post_process_material: MaterialInterface) -> None
unreal.WaterBodyComponent.set_water_body_static_mesh_enabled(enabled: bool) -> None
unreal.WaterBodyComponent.set_water_material(material: MaterialInterface) -> None
unreal.WaterBodyComponent.set_water_static_mesh_material(material: MaterialInterface) -> None
unreal.WaterBodyComponent.set_water_zone_override(water_zone_override: WaterZone) -> None
unreal.WaterBodyComponent.shape_dilation(value: float) -> None
unreal.WaterBodyComponent.target_wave_mask_depth(value: float) -> None
unreal.WaterBodyComponent.underwater_post_process_material() -> MaterialInterface
unreal.WaterBodyComponent.underwater_post_process_settings(value: UnderwaterPostProcessSettings) -> None
unreal.WaterBodyComponent.water_body_index() -> int
unreal.WaterBodyComponent.water_heightmap_settings(value: WaterBodyHeightmapSettings) -> None
unreal.WaterBodyComponent.water_hlod_material() -> MaterialInterface
unreal.WaterBodyComponent.water_info_material() -> MaterialInterface
unreal.WaterBodyComponent.water_material() -> MaterialInterface
unreal.WaterBodyComponent.water_mesh_override(value: StaticMesh) -> None
unreal.WaterBodyComponent.water_nav_area_class(value: Class) -> None
unreal.WaterBodyComponent.water_static_mesh_material() -> MaterialInterface
unreal.WaterBodyComponent.water_zone_override() -> WaterZone
```

## `unreal.WaterBodyExclusionVolume(PhysicsVolume)`

```python
unreal.WaterBodyExclusionVolume.water_bodies() -> Array[WaterBody]
unreal.WaterBodyExclusionVolume.water_body_to_ignore(value: WaterBody) -> None
```

## `unreal.WaterBodyHeightmapSettings(StructBase)`

```python
unreal.WaterBodyHeightmapSettings.__init__(blend_mode: WaterBrushBlendType = WaterBrushBlendType.ALPHA_BLEND, invert_shape: bool = False, falloff_settings: WaterFalloffSettings = [WaterBrushFalloffMode.ANGLE, 45.000000, 1024.000000, 0.000000, 0.000000], effects: WaterBrushEffects = [[True, 2], [0.000000, 0.000000, 16.000000, 3.000000], [0.000000, 0.000000, None, -128.000000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000], [0.010000, 0.010000], [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]]) -> None
unreal.WaterBodyHeightmapSettings.blend_mode(value: WaterBrushBlendType) -> None
unreal.WaterBodyHeightmapSettings.effects(value: WaterBrushEffects) -> None
unreal.WaterBodyHeightmapSettings.falloff_settings(value: WaterFalloffSettings) -> None
unreal.WaterBodyHeightmapSettings.invert_shape(value: bool) -> None
```

## `unreal.WaterBodyIsland(Actor)`

```python
unreal.WaterBodyIsland.get_water_spline() -> WaterSplineComponent
unreal.WaterBodyIsland.spline_comp() -> WaterSplineComponent
unreal.WaterBodyIsland.water_curve_settings(value: WaterCurveSettings) -> None
unreal.WaterBodyIsland.water_heightmap_settings(value: WaterBodyHeightmapSettings) -> None
unreal.WaterBodyIsland.water_weightmap_settings(value: Map[Name, WaterBodyWeightmapSettings]) -> None
```

## `unreal.WaterBodyOceanComponent(WaterBodyComponent)`

```python
unreal.WaterBodyOceanComponent.collision_extents() -> Vector
unreal.WaterBodyOceanComponent.ocean_extents() -> Vector2D
```

## `unreal.WaterBodyRiverComponent(WaterBodyComponent)`

```python
unreal.WaterBodyRiverComponent.lake_transition_material() -> MaterialInterface
unreal.WaterBodyRiverComponent.ocean_transition_material() -> MaterialInterface
unreal.WaterBodyRiverComponent.set_lake_and_ocean_transition_materials(lake_transition: MaterialInterface, ocean_transition: MaterialInterface) -> None
unreal.WaterBodyRiverComponent.set_lake_transition_material(mat: MaterialInterface) -> None
unreal.WaterBodyRiverComponent.set_ocean_transition_material(mat: MaterialInterface) -> None
```

## `unreal.WaterBodyWeightmapSettings(StructBase)`

```python
unreal.WaterBodyWeightmapSettings.__init__(falloff_width: float = 0.000000, edge_offset: float = 0.000000, modulation_texture: Texture2D = None, texture_tiling: float = 0.000000, texture_influence: float = 0.000000, midpoint: float = 0.000000, final_opacity: float = 0.000000) -> None
unreal.WaterBodyWeightmapSettings.edge_offset(value: float) -> None
unreal.WaterBodyWeightmapSettings.falloff_width(value: float) -> None
unreal.WaterBodyWeightmapSettings.final_opacity(value: float) -> None
unreal.WaterBodyWeightmapSettings.midpoint(value: float) -> None
unreal.WaterBodyWeightmapSettings.modulation_texture(value: Texture2D) -> None
unreal.WaterBodyWeightmapSettings.texture_influence(value: float) -> None
unreal.WaterBodyWeightmapSettings.texture_tiling(value: float) -> None
```

## `unreal.WaterBrushEffectBlurring(StructBase)`

```python
unreal.WaterBrushEffectBlurring.__init__(blur_shape: bool = False, radius: int = 0) -> None
unreal.WaterBrushEffectBlurring.blur_shape(value: bool) -> None
unreal.WaterBrushEffectBlurring.radius(value: int) -> None
```

## `unreal.WaterBrushEffectCurlNoise(StructBase)`

```python
unreal.WaterBrushEffectCurlNoise.__init__(curl1_amount: float = 0.000000, curl2_amount: float = 0.000000, curl1_tiling: float = 0.000000, curl2_tiling: float = 0.000000) -> None
unreal.WaterBrushEffectCurlNoise.curl1_amount(value: float) -> None
unreal.WaterBrushEffectCurlNoise.curl1_tiling(value: float) -> None
unreal.WaterBrushEffectCurlNoise.curl2_amount(value: float) -> None
unreal.WaterBrushEffectCurlNoise.curl2_tiling(value: float) -> None
```

## `unreal.WaterBrushEffectCurves(StructBase)`

```python
unreal.WaterBrushEffectCurves.__init__(use_curve_channel: bool = False, elevation_curve_asset: CurveFloat = None, channel_edge_offset: float = 0.000000, channel_depth: float = 0.000000, curve_ramp_width: float = 0.000000) -> None
unreal.WaterBrushEffectCurves.channel_depth(value: float) -> None
unreal.WaterBrushEffectCurves.channel_edge_offset(value: float) -> None
unreal.WaterBrushEffectCurves.curve_ramp_width(value: float) -> None
unreal.WaterBrushEffectCurves.elevation_curve_asset(value: CurveFloat) -> None
unreal.WaterBrushEffectCurves.use_curve_channel(value: bool) -> None
```

## `unreal.WaterBrushEffectDisplacement(StructBase)`

```python
unreal.WaterBrushEffectDisplacement.__init__(displacement_height: float = 0.000000, displacement_tiling: float = 0.000000, texture: Texture2D = None, midpoint: float = 0.000000, channel: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], weightmap_influence: float = 0.000000) -> None
unreal.WaterBrushEffectDisplacement.channel(value: LinearColor) -> None
unreal.WaterBrushEffectDisplacement.displacement_height(value: float) -> None
unreal.WaterBrushEffectDisplacement.displacement_tiling(value: float) -> None
unreal.WaterBrushEffectDisplacement.midpoint(value: float) -> None
unreal.WaterBrushEffectDisplacement.texture(value: Texture2D) -> None
unreal.WaterBrushEffectDisplacement.weightmap_influence(value: float) -> None
```

## `unreal.WaterBrushEffectSmoothBlending(StructBase)`

```python
unreal.WaterBrushEffectSmoothBlending.__init__(inner_smooth_distance: float = 0.000000, outer_smooth_distance: float = 0.000000) -> None
unreal.WaterBrushEffectSmoothBlending.inner_smooth_distance(value: float) -> None
unreal.WaterBrushEffectSmoothBlending.outer_smooth_distance(value: float) -> None
```

## `unreal.WaterBrushEffectTerracing(StructBase)`

```python
unreal.WaterBrushEffectTerracing.__init__(terrace_alpha: float = 0.000000, terrace_spacing: float = 0.000000, terrace_smoothness: float = 0.000000, mask_length: float = 0.000000, mask_start_offset: float = 0.000000) -> None
unreal.WaterBrushEffectTerracing.mask_length(value: float) -> None
unreal.WaterBrushEffectTerracing.mask_start_offset(value: float) -> None
unreal.WaterBrushEffectTerracing.terrace_alpha(value: float) -> None
unreal.WaterBrushEffectTerracing.terrace_smoothness(value: float) -> None
unreal.WaterBrushEffectTerracing.terrace_spacing(value: float) -> None
```

## `unreal.WaterBrushEffects(StructBase)`

```python
unreal.WaterBrushEffects.__init__(blurring: WaterBrushEffectBlurring = [True, 2], curl_noise: WaterBrushEffectCurlNoise = [0.000000, 0.000000, 16.000000, 3.000000], displacement: WaterBrushEffectDisplacement = [0.000000, 0.000000, None, -128.000000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000], smooth_blending: WaterBrushEffectSmoothBlending = [0.010000, 0.010000], terracing: WaterBrushEffectTerracing = [0.000000, 256.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.WaterBrushEffects.blurring(value: WaterBrushEffectBlurring) -> None
unreal.WaterBrushEffects.curl_noise(value: WaterBrushEffectCurlNoise) -> None
unreal.WaterBrushEffects.displacement(value: WaterBrushEffectDisplacement) -> None
unreal.WaterBrushEffects.smooth_blending(value: WaterBrushEffectSmoothBlending) -> None
unreal.WaterBrushEffects.terracing(value: WaterBrushEffectTerracing) -> None
```

## `unreal.WaterBrushManager(WaterLandscapeBrush)`

```python
unreal.WaterBrushManager.blur_edges_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.brush_angle_falloff_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.brush_angle_falloff_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.brush_curve_rt_cache() -> Map[CurveFloat, WaterBodyBrushCache]
unreal.WaterBrushManager.brush_width_falloff_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.brush_width_falloff_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.canvas_segment_size(value: float) -> None
unreal.WaterBrushManager.composite_water_body_texture_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.composite_water_body_texture_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.debug_distance_field_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.debug_distance_field_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.disable_brush_texture_effects(value: bool) -> None
unreal.WaterBrushManager.distance_divisor(value: float) -> None
unreal.WaterBrushManager.distance_field_cache_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.distance_field_cache_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.draw_canvas_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.draw_canvas_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.find_edges() -> None
unreal.WaterBrushManager.find_edges_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.force_update() -> None
unreal.WaterBrushManager.get_water_cache_key(water_brush: Actor) -> Tuple[WaterBodyBrushCacheContainer, WaterBodyBrushCache]
unreal.WaterBrushManager.island_falloff_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.island_falloff_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.jump_step_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.landscape_quads() -> IntPoint
unreal.WaterBrushManager.landscape_rt_res() -> IntPoint
unreal.WaterBrushManager.landscape_transform() -> Transform
unreal.WaterBrushManager.render_river_spline_depth_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.river_spline_mi_ds(value: Array[MaterialInstanceDynamic]) -> None
unreal.WaterBrushManager.setup_default_materials() -> None
unreal.WaterBrushManager.show_distance(value: bool) -> None
unreal.WaterBrushManager.show_gradient(value: bool) -> None
unreal.WaterBrushManager.show_grid(value: bool) -> None
unreal.WaterBrushManager.single_blur_step() -> None
unreal.WaterBrushManager.single_jump_step() -> None
unreal.WaterBrushManager.sort_water_bodies_for_brush_render() -> Array[WaterBody]
unreal.WaterBrushManager.spline_mesh_extension(value: float) -> None
unreal.WaterBrushManager.use_dynamic_preview_rt(value: bool) -> None
unreal.WaterBrushManager.water_clear_height(value: float) -> None
unreal.WaterBrushManager.weightmap_material(value: MaterialInterface) -> None
unreal.WaterBrushManager.weightmap_mid(value: MaterialInstanceDynamic) -> None
unreal.WaterBrushManager.world_size() -> Vector
```

## `unreal.WaterCurveSettings(StructBase)`

```python
unreal.WaterCurveSettings.__init__(use_curve_channel: bool = False, elevation_curve_asset: CurveFloat = None, channel_edge_offset: float = 0.000000, channel_depth: float = 0.000000, curve_ramp_width: float = 0.000000) -> None
unreal.WaterCurveSettings.channel_depth(value: float) -> None
unreal.WaterCurveSettings.channel_edge_offset(value: float) -> None
unreal.WaterCurveSettings.curve_ramp_width(value: float) -> None
unreal.WaterCurveSettings.elevation_curve_asset(value: CurveFloat) -> None
unreal.WaterCurveSettings.use_curve_channel(value: bool) -> None
```

## `unreal.WaterFalloffSettings(StructBase)`

```python
unreal.WaterFalloffSettings.__init__(falloff_mode: WaterBrushFalloffMode = WaterBrushFalloffMode.ANGLE, falloff_angle: float = 0.000000, falloff_width: float = 0.000000, edge_offset: float = 0.000000, z_offset: float = 0.000000) -> None
unreal.WaterFalloffSettings.edge_offset(value: float) -> None
unreal.WaterFalloffSettings.falloff_angle(value: float) -> None
unreal.WaterFalloffSettings.falloff_mode(value: WaterBrushFalloffMode) -> None
unreal.WaterFalloffSettings.falloff_width(value: float) -> None
unreal.WaterFalloffSettings.z_offset(value: float) -> None
```

## `unreal.WaterLandscapeBrush(LandscapeBlueprintBrush)`

```python
unreal.WaterLandscapeBrush.blueprint_get_render_targets(height_render_target: TextureRenderTarget2D) -> TextureRenderTarget2D
unreal.WaterLandscapeBrush.blueprint_on_render_target_textures_updated(velocity_texture: Texture2D) -> None
unreal.WaterLandscapeBrush.blueprint_water_bodies_changed() -> None
unreal.WaterLandscapeBrush.blueprint_water_body_changed(actor: Actor) -> None
unreal.WaterLandscapeBrush.clear_actor_cache(actor: Actor) -> None
unreal.WaterLandscapeBrush.clear_water_body_cache(water_body: WaterBody) -> None
unreal.WaterLandscapeBrush.force_water_texture_update() -> None
unreal.WaterLandscapeBrush.get_actor_cache(actor: Actor, cache_class: Class) -> Object
unreal.WaterLandscapeBrush.get_actors_affecting_landscape() -> Array[WaterBrushActorInterface]
unreal.WaterLandscapeBrush.get_water_bodies(water_body_class: Class) -> Array[WaterBody]
unreal.WaterLandscapeBrush.get_water_body_cache(water_body: WaterBody, cache_class: Class) -> Object
unreal.WaterLandscapeBrush.get_water_body_islands(water_body_island_class: Class) -> Array[WaterBodyIsland]
unreal.WaterLandscapeBrush.set_actor_cache(actor: Actor, cache: Object) -> None
unreal.WaterLandscapeBrush.set_water_body_cache(water_body: WaterBody, cache: Object) -> None
```

## `unreal.WaterMeshComponent(MeshComponent)`

```python
unreal.WaterMeshComponent.is_enabled() -> bool
```

## `unreal.WaterMeshInfo(StructBase)`

```python
unreal.WaterMeshInfo.__init__(local_to_parent_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], ways: Array[WaterWayInfo] = []) -> None
unreal.WaterMeshInfo.local_to_parent_transform(value: Transform) -> None
unreal.WaterMeshInfo.ways(value: Array[WaterWayInfo]) -> None
```

## `unreal.WaterSplineComponent(SplineComponent)`

```python
unreal.WaterSplineComponent.k2_synchronize_and_broadcast_data_change() -> None
```

## `unreal.WaterSplineCurveDefaults(StructBase)`

```python
unreal.WaterSplineCurveDefaults.__init__() -> None
```

## `unreal.WaterWayInfo(StructBase)`

```python
unreal.WaterWayInfo.__init__(local_to_parent_transform: Transform = [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], water_body_height: float = 0.000000, corner_radius: float = 0.000000, corner_split_seg_num: int = 0, align_z: bool = False, inverse_normal: bool = False, use_global_rounded_corner: bool = False, water_mat_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT, ripple_scale: float = 0.000000, wave_rotate: float = 0.000000, wave_speed_x: float = 0.000000, water_color: str = "", wave_height: float = 0.000000, transparent_depth: float = 0.000000, water_transparency: float = 0.000000, wave_intensity: float = 0.000000, wave_scale: float = 0.000000, nodes: Array[WaterNodeInfo] = []) -> None
unreal.WaterWayInfo.align_z(value: bool) -> None
unreal.WaterWayInfo.corner_radius(value: float) -> None
unreal.WaterWayInfo.corner_split_seg_num(value: int) -> None
unreal.WaterWayInfo.inverse_normal(value: bool) -> None
unreal.WaterWayInfo.local_to_parent_transform(value: Transform) -> None
unreal.WaterWayInfo.nodes(value: Array[WaterNodeInfo]) -> None
unreal.WaterWayInfo.ripple_scale(value: float) -> None
unreal.WaterWayInfo.transparent_depth(value: float) -> None
unreal.WaterWayInfo.use_global_rounded_corner(value: bool) -> None
unreal.WaterWayInfo.water_body_height(value: float) -> None
unreal.WaterWayInfo.water_color(value: str) -> None
unreal.WaterWayInfo.water_mat_name(value: AssetName) -> None
unreal.WaterWayInfo.water_transparency(value: float) -> None
unreal.WaterWayInfo.wave_height(value: float) -> None
unreal.WaterWayInfo.wave_intensity(value: float) -> None
unreal.WaterWayInfo.wave_rotate(value: float) -> None
unreal.WaterWayInfo.wave_scale(value: float) -> None
unreal.WaterWayInfo.wave_speed_x(value: float) -> None
```

## `unreal.WaterZone(Actor)`

```python
unreal.WaterZone.get_water_zone_index() -> int
unreal.WaterZone.on_water_info_texture_array_created(value: OnWaterInfoTextureArrayCreated) -> None
unreal.WaterZone.render_target_resolution() -> IntPoint
unreal.WaterZone.set_far_mesh_material(far_material: MaterialInterface) -> None
unreal.WaterZone.water_info_texture(value: TextureRenderTarget2D) -> None
unreal.WaterZone.water_info_texture_array() -> TextureRenderTarget2DArray
unreal.WaterZone.water_info_texture_array_num_slices() -> int
unreal.WaterZone.water_mesh() -> WaterMeshComponent
unreal.WaterZone.zone_extent(value: Vector2D) -> None
```

## `unreal.WdpCurve2D(StructBase)`

```python
unreal.WdpCurve2D.__init__() -> None
```

## `unreal.WdpGeometryAPI(StandardApiClassBase)`

```python
unreal.WdpGeometryAPI.create_geometry_entities_from_geo_json(params: CreateGeometryEntitiesParams) -> Optional[CreateGeometryEntitiesResult]
unreal.WdpGeometryAPI.create_geometry_entities_from_shapefile(params: CreateGeometryEntitiesParams) -> Optional[CreateGeometryEntitiesResult]
unreal.WdpGeometryAPI.disable_geometry_draw(params: ParamsBase) -> Optional[ResultBase]
unreal.WdpGeometryAPI.enable_geometry_draw(params: ParamsBase) -> Optional[ResultBase]
unreal.WdpGeometryAPI.end_show_coord(params: ParamsBase) -> Optional[ResultBase]
unreal.WdpGeometryAPI.start_show_coord(params: WdpStartShowCoordParams) -> Optional[ResultBase]
```

## `unreal.WdpGeometryBPLibrary(BlueprintFunctionLibrary)`

```python
unreal.WdpGeometryBPLibrary.create_arc2d(start_point: Vector2D, end_point: Vector2D, control_point: Vector2D) -> WdpArc2D
unreal.WdpGeometryBPLibrary.create_circle(origin: Vector2D, radius: float) -> WdpLoop2D
unreal.WdpGeometryBPLibrary.create_rectangle(start: Vector2D, end: Vector2D) -> WdpLoop2D
unreal.WdpGeometryBPLibrary.polygon2d_to_polygon(polygon: WdpPolygon2D, z: float = 0.000000) -> WdpPolygon
unreal.WdpGeometryBPLibrary.polygon_to_polygon2d(polygon: WdpPolygon) -> WdpPolygon2D
unreal.WdpGeometryBPLibrary.triangulate_polygon(polygon: WdpPolygon) -> Optional[Tuple[Array[Vector], Array[int]]]
unreal.WdpGeometryBPLibrary.triangulate_polygon2d(polygon: WdpPolygon2D, level: WdpCurveSplitLevel = WdpCurveSplitLevel.LOW) -> Optional[Tuple[Array[Vector2D], Array[int]]]
unreal.WdpGeometryBPLibrary.triangulate_polyline(polygon: WdpPolyline, width: float) -> Optional[Tuple[Array[Vector], Array[int]]]
```

## `unreal.WdpModelerWaterDataParams(ParamsBase)`

```python
unreal.WdpModelerWaterDataParams.__init__() -> None
```

## `unreal.WdpModelerWaterVertexAttribute(StructBase)`

```python
unreal.WdpModelerWaterVertexAttribute.__init__(corner_radius: float = 0.000000, corner_split_num: int = 0) -> None
unreal.WdpModelerWaterVertexAttribute.corner_radius() -> float
unreal.WdpModelerWaterVertexAttribute.corner_split_num() -> int
```

## `unreal.WimDynamicWaterAPI(StandardApiClassBase)`

```python
unreal.WimDynamicWaterAPI.toggle_water_data(transaction_params: ToggleWaterDataParams) -> Optional[ResultBase]
```

## `unreal.glTFRuntimeProceduralMeshConfig(StructBase)`

```python
unreal.glTFRuntimeProceduralMeshConfig.__init__(reverse_winding: bool = False, build_simple_collision: bool = False, box_collisions: Array[Box] = [], sphere_collisions: Array[Vector4] = [], use_complex_as_simple_collision: bool = False, pivot_position: EglTFRuntimePivotPosition = EglTFRuntimePivotPosition.ASSET, materials_config: glTFRuntimeMaterialsConfig = [EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False, False, 0.000000, False, {}, [TextureCompressionSettings.TC_DEFAULT, TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False, False, 0], "", False, None, {}, False, None, True, EglTFRuntimePointsTriangulationMode.OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True, EglTFRuntimeLinesTriangulationMode.OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, {}, {}, {}]) -> None
unreal.glTFRuntimeProceduralMeshConfig.box_collisions(value: Array[Box]) -> None
unreal.glTFRuntimeProceduralMeshConfig.build_simple_collision(value: bool) -> None
unreal.glTFRuntimeProceduralMeshConfig.materials_config(value: glTFRuntimeMaterialsConfig) -> None
unreal.glTFRuntimeProceduralMeshConfig.pivot_position(value: EglTFRuntimePivotPosition) -> None
unreal.glTFRuntimeProceduralMeshConfig.reverse_winding(value: bool) -> None
unreal.glTFRuntimeProceduralMeshConfig.sphere_collisions(value: Array[Vector4]) -> None
unreal.glTFRuntimeProceduralMeshConfig.use_complex_as_simple_collision(value: bool) -> None
```

