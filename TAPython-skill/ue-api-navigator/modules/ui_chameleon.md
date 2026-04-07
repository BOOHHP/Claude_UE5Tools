# Unreal Python API — Ui Chameleon

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AesEditorContextMenuItemWidget(UserWidget)`

```python
unreal.AesEditorContextMenuItemWidget.can_execute_command() -> bool
unreal.AesEditorContextMenuItemWidget.execute_command() -> None
unreal.AesEditorContextMenuItemWidget.item_text(value: TextBlock) -> None
unreal.AesEditorContextMenuItemWidget.item_text_string(value: str) -> None
```

## `unreal.AesEditorContextMenuWidget(UserWidget)`

```python
unreal.AesEditorContextMenuWidget.menu_item_container(value: VerticalBox) -> None
unreal.AesEditorContextMenuWidget.menu_root(value: PanelWidget) -> None
```

## `unreal.AesEditorIndicatorWidget(UserWidget)`

```python
unreal.AesEditorIndicatorWidget.glyph_image(value: Image) -> None
unreal.AesEditorIndicatorWidget.glyph_type(value: AesEditorIndicatorGlyphType) -> None
unreal.AesEditorIndicatorWidget.text(value: TextBlock) -> None
unreal.AesEditorIndicatorWidget.text_string(value: str) -> None
```

## `unreal.AesEditorMainWidget(UserWidget)`

```python
unreal.AesEditorMainWidget.create_property_proxy() -> None
unreal.AesEditorMainWidget.drag_border(value: EarthDragBorderWidget) -> None
unreal.AesEditorMainWidget.drag_command_class(value: Class) -> None
unreal.AesEditorMainWidget.is_property_proxy_created() -> bool
unreal.AesEditorMainWidget.property_list_window(value: AesEditorWindowWidget) -> None
```

## `unreal.AesEditorWindowWidget(UserWidget)`

```python
unreal.AesEditorWindowWidget.get_widget() -> Widget
unreal.AesEditorWindowWidget.widget_container(value: WidgetSwitcher) -> None
```

## `unreal.AesPOIUserWidget(UserWidget)`

```python
unreal.AesPOIUserWidget.image() -> Image
unreal.AesPOIUserWidget.text() -> TextBlock
```

## `unreal.AssetThumbnailWidget(Widget)`

```python
unreal.AssetThumbnailWidget.get_resolution() -> IntPoint
unreal.AssetThumbnailWidget.resolution(value: IntPoint) -> None
unreal.AssetThumbnailWidget.set_asset(asset_data: AssetData) -> None
unreal.AssetThumbnailWidget.set_asset_by_object(object: Object) -> None
unreal.AssetThumbnailWidget.set_resolution(resolution: IntPoint) -> None
unreal.AssetThumbnailWidget.set_thumbnail_settings(thumbnail_settings: AssetThumbnailWidgetSettings) -> None
unreal.AssetThumbnailWidget.thumbnail_settings(value: AssetThumbnailWidgetSettings) -> None
```

## `unreal.AssetThumbnailWidgetSettings(StructBase)`

```python
unreal.AssetThumbnailWidgetSettings.__init__(force_generic_thumbnail: bool = False, allow_hint_text: bool = False, allow_real_time_on_hovered: bool = False, allow_asset_specific_thumbnail_overlay: bool = False, thumbnail_label: ThumbnailLabelType_BlueprintType = ThumbnailLabelType_BlueprintType.CLASS_NAME, highlighted_text_delegate: GetHighlightTextDelegate = GetHighlightTextDelegate(), hint_color_and_opacity: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], override_asset_type_color: bool = False, asset_type_color_override: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], generic_thumbnail_size: int = 0, color_strip_orientation: ThumbnailColorStripOrientation_BlueprintType = ThumbnailColorStripOrientation_BlueprintType.HORIZONTAL_BOTTOM_EDGE) -> None
unreal.AssetThumbnailWidgetSettings.allow_asset_specific_thumbnail_overlay(value: bool) -> None
unreal.AssetThumbnailWidgetSettings.allow_hint_text(value: bool) -> None
unreal.AssetThumbnailWidgetSettings.allow_real_time_on_hovered(value: bool) -> None
unreal.AssetThumbnailWidgetSettings.asset_type_color_override(value: LinearColor) -> None
unreal.AssetThumbnailWidgetSettings.color_strip_orientation(value: ThumbnailColorStripOrientation_BlueprintType) -> None
unreal.AssetThumbnailWidgetSettings.force_generic_thumbnail(value: bool) -> None
unreal.AssetThumbnailWidgetSettings.generic_thumbnail_size(value: int) -> None
unreal.AssetThumbnailWidgetSettings.highlighted_text_delegate(value: GetHighlightTextDelegate) -> None
unreal.AssetThumbnailWidgetSettings.hint_color_and_opacity(value: LinearColor) -> None
unreal.AssetThumbnailWidgetSettings.override_asset_type_color(value: bool) -> None
unreal.AssetThumbnailWidgetSettings.padding(value: Margin) -> None
unreal.AssetThumbnailWidgetSettings.thumbnail_label(value: ThumbnailLabelType_BlueprintType) -> None
```

## `unreal.AudioOscilloscopePanelStyle(SlateWidgetStyle)`

```python
unreal.AudioOscilloscopePanelStyle.__init__(time_ruler_style: FixedSampleSequenceRulerStyle = [15.000000, [[255.000000, 0.100000, 0.200000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 1.000000, 1.000000, 0.900000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[1.000000, 1.000000, 1.000000, 0.900000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "Regular", 10.000000, 0, 0.000000, False, False, 1.000000], 5.000000, [[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 1280.000000, 30.000000], value_grid_style: SampledSequenceValueGridOverlayStyle = [[[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000, [[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "Regular", 10.000000, 0, 0.000000, False, False, 1.000000], 1280.000000, 720.000000], wave_viewer_style: SampledSequenceViewerStyle = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000, [[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[0.000000, 0.000000, 0.000000, 0.500000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000, 2.500000, [[0.020000, 0.020000, 0.020000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 1280.000000, 720.000000], trigger_threshold_line_style: TriggerThresholdLineStyle = [[1.000000, 1.000000, 1.000000, 1.000000]]) -> None
unreal.AudioOscilloscopePanelStyle.time_ruler_style(value: FixedSampleSequenceRulerStyle) -> None
unreal.AudioOscilloscopePanelStyle.trigger_threshold_line_style(value: TriggerThresholdLineStyle) -> None
unreal.AudioOscilloscopePanelStyle.value_grid_style(value: SampledSequenceValueGridOverlayStyle) -> None
unreal.AudioOscilloscopePanelStyle.wave_viewer_style(value: SampledSequenceViewerStyle) -> None
```

## `unreal.AudioPanelWidgetInterface(Interface)`

```python
unreal.AudioPanelWidgetInterface.get_editor_name() -> Text
unreal.AudioPanelWidgetInterface.get_icon_brush_name() -> Name
```

## `unreal.AudioVectorscopePanelStyle(SlateWidgetStyle)`

```python
unreal.AudioVectorscopePanelStyle.__init__(value_grid_style: SampledSequenceValueGridOverlayStyle = [[[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 1.000000, [[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "Regular", 10.000000, 0, 0.000000, False, False, 1.000000], 1280.000000, 720.000000], vector_viewer_style: SampledSequenceVectorViewerStyle = [[[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [1.000000, 1.000000, 1.000000, 1.000000], 1.000000]) -> None
unreal.AudioVectorscopePanelStyle.value_grid_style(value: SampledSequenceValueGridOverlayStyle) -> None
unreal.AudioVectorscopePanelStyle.vector_viewer_style(value: SampledSequenceVectorViewerStyle) -> None
```

## `unreal.ButtonWidgetStyle(SlateWidgetStyleContainerBase)`

```python
unreal.ButtonWidgetStyle.button_style(value: ButtonStyle) -> None
```

## `unreal.CanvasPanel(PanelWidget)`

```python
unreal.CanvasPanel.add_child_to_canvas(content: Widget) -> CanvasPanelSlot
```

## `unreal.CanvasPanelSlot(PanelSlot)`

```python
unreal.CanvasPanelSlot.auto_size(value: bool) -> None
unreal.CanvasPanelSlot.get_alignment() -> Vector2D
unreal.CanvasPanelSlot.get_anchors() -> Anchors
unreal.CanvasPanelSlot.get_auto_size() -> bool
unreal.CanvasPanelSlot.get_layout() -> AnchorData
unreal.CanvasPanelSlot.get_offsets() -> Margin
unreal.CanvasPanelSlot.get_position() -> Vector2D
unreal.CanvasPanelSlot.get_size() -> Vector2D
unreal.CanvasPanelSlot.get_z_order() -> int
unreal.CanvasPanelSlot.layout_data(value: AnchorData) -> None
unreal.CanvasPanelSlot.set_alignment(alignment: Vector2D) -> None
unreal.CanvasPanelSlot.set_anchors(anchors: Anchors) -> None
unreal.CanvasPanelSlot.set_auto_size(inb_auto_size: bool) -> None
unreal.CanvasPanelSlot.set_layout(layout_data: AnchorData) -> None
unreal.CanvasPanelSlot.set_offsets(offset: Margin) -> None
unreal.CanvasPanelSlot.set_position(position: Vector2D) -> None
unreal.CanvasPanelSlot.set_size(size: Vector2D) -> None
unreal.CanvasPanelSlot.set_z_order(z_order: int) -> None
unreal.CanvasPanelSlot.z_order(value: int) -> None
```

## `unreal.ChameleonData(Object)`

```python
unreal.ChameleonData.add_column(aka_name: Name, label: str) -> None
unreal.ChameleonData.add_detail_customization(object: Object, tools_path: str) -> bool
unreal.ChameleonData.append_slot_from_json(aka_name: Name, json_content: str, column: int = -1, row: int = -1) -> bool
unreal.ChameleonData.bind_uobject_to_browser(aka_name: Name, name: str, object: Object, is_permanent: bool = True) -> None
unreal.ChameleonData.can_go_back(aka_name: Name) -> bool
unreal.ChameleonData.can_go_forward(aka_name: Name) -> bool
unreal.ChameleonData.clear_breadcrumbs_string(aka_name: Name, pop_all_crumbs_to_clear: bool = False) -> None
unreal.ChameleonData.clear_detail_customization() -> None
unreal.ChameleonData.clear_graph_panel(aka_name: Name) -> int
unreal.ChameleonData.flash_chameleon_window(tools_path: str) -> bool
unreal.ChameleonData.get_all_akas() -> Array[str]
unreal.ChameleonData.get_all_widgets_paths() -> Array[str]
unreal.ChameleonData.get_breadcrumbs_count_string(aka_name: Name) -> int
unreal.ChameleonData.get_chameleon_desired_size(tools_path: str) -> Vector2D
unreal.ChameleonData.get_chameleon_window_position(tools_path: str) -> Vector2D
unreal.ChameleonData.get_chameleon_window_size(tools_path: str, client_size_in_screen: bool = False) -> Vector2D
unreal.ChameleonData.get_combo_box_items(aka_name: Name) -> Optional[Array[str]]
unreal.ChameleonData.get_combo_box_selected_item(aka_name: Name) -> Optional[str]
unreal.ChameleonData.get_context_strings() -> str
unreal.ChameleonData.get_customized_object(unique_id: int) -> Object
unreal.ChameleonData.get_detail_panel_customized_class_names() -> Array[Name]
unreal.ChameleonData.get_float_value(aka_name: Name) -> Optional[float]
unreal.ChameleonData.get_graph_panel_content_as_json(aka_name: Name) -> str
unreal.ChameleonData.get_graph_panel_nodes(aka_name: Name) -> Array[EdGraphNode]
unreal.ChameleonData.get_graph_selected_node(aka_name: Name) -> Array[EdGraphNode]
unreal.ChameleonData.get_int_value(aka_name: Name) -> Optional[int]
unreal.ChameleonData.get_is_checked(aka_name: Name) -> bool
unreal.ChameleonData.get_is_expanded(aka_name: Name) -> bool
unreal.ChameleonData.get_list_view_items(aka_name: Name) -> Tuple[Array[str], Array[int]]
unreal.ChameleonData.get_list_view_multi_column_items(aka_name: Name) -> Tuple[Array[str], int]
unreal.ChameleonData.get_list_view_multi_column_selection(aka_name: Name) -> Optional[Array[int]]
unreal.ChameleonData.get_python_flag() -> bool
unreal.ChameleonData.get_scroll_box_offsets(aka_name: Name) -> Map[str, float]
unreal.ChameleonData.get_text(aka_name: Name) -> Optional[str]
unreal.ChameleonData.get_title_text_of_page(aka_name: Name) -> str
unreal.ChameleonData.get_top_scroll_box_offsets(tools_path: str) -> Map[str, float]
unreal.ChameleonData.get_tree_view_items(aka_name: Name) -> Optional[Tuple[Array[str], Array[int]]]
unreal.ChameleonData.get_url(aka_name: Name) -> str
unreal.ChameleonData.get_visibility(aka_name: Name) -> str
unreal.ChameleonData.get_widget_path(aka_name: Name) -> str
unreal.ChameleonData.get_widget_path_from_aka(aka_name: Name) -> str
unreal.ChameleonData.go_back(aka_name: Name) -> None
unreal.ChameleonData.go_forward(aka_name: Name) -> None
unreal.ChameleonData.hatch_egg(object: Object) -> bool
unreal.ChameleonData.insert_slot_from_json(aka_name: Name, json_content: str, index: int) -> bool
unreal.ChameleonData.is_page_loaded(aka_name: Name) -> bool
unreal.ChameleonData.is_page_loading(aka_name: Name) -> bool
unreal.ChameleonData.launch_chameleon_tool(tools_path: str = "") -> bool
unreal.ChameleonData.load_page_from_string(aka_name: Name, contents: str, dummy_url: str) -> None
unreal.ChameleonData.load_url(aka_name: Name, new_url: str) -> None
unreal.ChameleonData.log_all_saved_detail_customization() -> None
unreal.ChameleonData.modal_window(tools_path: str) -> bool
unreal.ChameleonData.pop_breadcrumb_string(aka_name: Name) -> str
unreal.ChameleonData.push_breadcrumb_string(aka_name: Name, crumb_text: str, new_crumb_data: str) -> None
unreal.ChameleonData.reload_page(aka_name: Name) -> None
unreal.ChameleonData.remove_widget_at(aka_name: Name, index: int) -> bool
unreal.ChameleonData.request_close(tools_path: str = "") -> bool
unreal.ChameleonData.request_close_modal_window(tools_path: str) -> bool
unreal.ChameleonData.scroll_to(aka_name: Name, line_index: int = 0, offset: int = 0) -> bool
unreal.ChameleonData.set_button_color_and_opacity(aka_name: Name, color: LinearColor) -> None
unreal.ChameleonData.set_chameleon_window_position(tools_path: str, new_position: Vector2D) -> bool
unreal.ChameleonData.set_chameleon_window_size(tools_path: str, new_size: Vector2D) -> bool
unreal.ChameleonData.set_collapsed(aka_name: Name, collapsed: bool) -> None
unreal.ChameleonData.set_color(aka_name: Name, color: LinearColor) -> bool
unreal.ChameleonData.set_color_and_opacity(aka_name: Name, color: LinearColor) -> None
unreal.ChameleonData.set_column_lable(aka_name: Name, index: int, label: str) -> None
unreal.ChameleonData.set_combo_box_items(aka_name: Name, str_array: Array[str]) -> bool
unreal.ChameleonData.set_combo_box_selected_item(aka_name: Name, index: int) -> bool
unreal.ChameleonData.set_content_from_json(aka_name: Name, json_content: str) -> bool
unreal.ChameleonData.set_desired_size_override(aka_name: Name, desired_size_override: Vector2D) -> None
unreal.ChameleonData.set_dpi_scale(aka_name: Name, value: float) -> bool
unreal.ChameleonData.set_float_value(aka_name: Name, value: float) -> None
unreal.ChameleonData.set_graph_panel_content_from_json(aka_name: Name, json_content: str) -> bool
unreal.ChameleonData.set_grid_panel_column_fill(aka_name: Name, index: int, value: float) -> None
unreal.ChameleonData.set_image_data(aka_name: Name, raw_data: Array[int], width: int, height: int, channel_num: int = 4, bgr: bool = True, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
unreal.ChameleonData.set_image_data_base64(aka_name: Name, base64_string: str, width: int, height: int, channel_num: int = 4, bgr: bool = True, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
unreal.ChameleonData.set_image_data_from_memory(aka_name: Name, address: int, length: int, width: int, height: int, channel_num: int = 4, bgr: bool = True, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
unreal.ChameleonData.set_image_data_from_texture2d(aka_name: Name, texture2d: Texture2D, mip_level: int = 0, ignore_alpha: bool = False, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> bool
unreal.ChameleonData.set_image_from(aka_name: Name, image_file_path: str, brush_width: int = 256, brush_height: int = 256, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
unreal.ChameleonData.set_image_from_path(aka_name: Name, image_file_path: str, brush_width: int = 256, brush_height: int = 256, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
unreal.ChameleonData.set_image_pixels(aka_name: Name, pixel_colors: Array[LinearColor], width: int, height: int) -> None
unreal.ChameleonData.set_int_value(aka_name: Name, value: int) -> None
unreal.ChameleonData.set_is_checked(aka_name: Name, checked: bool) -> None
unreal.ChameleonData.set_is_expanded(aka_name: Name, expanded: bool, animated: bool = False) -> None
unreal.ChameleonData.set_list_view_items(aka_name: Name, str_array: Array[str]) -> None
unreal.ChameleonData.set_list_view_multi_column_items(aka_name: Name, flattened_str_array: Array[str], column_count: int) -> None
unreal.ChameleonData.set_list_view_multi_column_line(aka_name: Name, line_index: int, line_content_array: Array[str], rebuild_list: bool) -> None
unreal.ChameleonData.set_list_view_multi_column_selections(aka_name: Name, indexes: Array[int]) -> None
unreal.ChameleonData.set_list_view_selections(aka_name: str, indexes: Array[int]) -> None
unreal.ChameleonData.set_max_aspect_ratio(aka_name: Name, max_aspect_ratio: float) -> None
unreal.ChameleonData.set_menu_item_can_execute(id: int, can_execute: bool) -> None
unreal.ChameleonData.set_min_aspect_ratio(aka_name: Name, min_aspect_ratio: float) -> None
unreal.ChameleonData.set_object(aka_name: Name, object: Object) -> None
unreal.ChameleonData.set_progress_bar_percent(aka_name: Name, percent: float) -> None
unreal.ChameleonData.set_python_flag(is_ready: bool) -> None
unreal.ChameleonData.set_scroll_box_offset(aka_name: Name, offset: float) -> bool
unreal.ChameleonData.set_text(aka_name: Name, text: str) -> None
unreal.ChameleonData.set_text_read_only(aka_name: Name, read_only: bool) -> None
unreal.ChameleonData.set_tool_tip_text(aka_name: Name, tool_tip_text: str) -> None
unreal.ChameleonData.set_tree_view_items(aka_name: Name, str_array: Array[str], parent_indices: Array[int]) -> None
unreal.ChameleonData.set_visibility(aka_name: Name, visibility_str: str) -> bool
unreal.ChameleonData.snapshot_chameleon_window(tools_path: str, override_window_size: Vector2D = [0.000000, 0.000000], image_file_path: str = "") -> str
unreal.ChameleonData.snapshot_sketch(override_window_size: Vector2D = [0.000000, 0.000000], image_file_path: str = "") -> str
unreal.ChameleonData.spawn_function_to_graph(aka_name: Name, module: Class, function_name: str) -> EdGraphNode
unreal.ChameleonData.spawn_function_to_graph_with_spawner(aka_name: Name, bp_function_spawner: Object) -> EdGraphNode
unreal.ChameleonData.spawn_to_graph_by_class(aka_name: Name, node_class: Class, update: bool = True) -> EdGraphNode
unreal.ChameleonData.stop_load_page(aka_name: Name) -> None
unreal.ChameleonData.unbind_uobject_to_browser(aka_name: Name, name: str, object: Object, is_permanent: bool = True) -> None
```

## `unreal.ChamferLengthWidget(UserWidget)`

```python
unreal.ChamferLengthWidget.get_chamfer_length() -> float
unreal.ChamferLengthWidget.set_chamfer_length(chamfer_length: float) -> None
```

## `unreal.ComboBoxKey_GenerateWidgetEvent(DelegateBase)`

```python
unreal.ComboBoxKey_GenerateWidgetEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.CompassWidgetBase(UserWidget)`

```python
unreal.CompassWidgetBase.end_compass() -> bool
unreal.CompassWidgetBase.start_compass(position: Vector2D, size: int, bg_url: str, needle_url: str, anchors: str) -> bool
```

## `unreal.ContentWidget(PanelWidget)`

```python
unreal.ContentWidget.get_content() -> Widget
unreal.ContentWidget.get_content_slot() -> PanelSlot
unreal.ContentWidget.set_content(content: Widget) -> PanelSlot
```

## `unreal.CoverWindowStyle(StructBase)`

```python
unreal.CoverWindowStyle.__init__(url: str = "", size: Vector2D = [0.000000, 0.000000], offset: Vector2D = [0.000000, 0.000000]) -> None
unreal.CoverWindowStyle.offset(value: Vector2D) -> None
unreal.CoverWindowStyle.size(value: Vector2D) -> None
unreal.CoverWindowStyle.url(value: str) -> None
```

## `unreal.Covering3DWidgetComponent(MeshComponent)`

```python
unreal.Covering3DWidgetComponent.change_screen_layer(source_layer_name: Name, target_layer_name: Name) -> None
unreal.Covering3DWidgetComponent.get_current_draw_size() -> Vector2D
unreal.Covering3DWidgetComponent.get_cylinder_arc_angle() -> float
unreal.Covering3DWidgetComponent.get_draw_at_desired_size() -> bool
unreal.Covering3DWidgetComponent.get_draw_size() -> Vector2D
unreal.Covering3DWidgetComponent.get_geometry_mode() -> CoveringWidgetGeometryMode
unreal.Covering3DWidgetComponent.get_manually_redraw() -> bool
unreal.Covering3DWidgetComponent.get_material_instance() -> MaterialInstanceDynamic
unreal.Covering3DWidgetComponent.get_owner_player() -> LocalPlayer
unreal.Covering3DWidgetComponent.get_pivot() -> Vector2D
unreal.Covering3DWidgetComponent.get_redraw_time() -> float
unreal.Covering3DWidgetComponent.get_render_target() -> TextureRenderTarget2D
unreal.Covering3DWidgetComponent.get_tick_when_offscreen() -> bool
unreal.Covering3DWidgetComponent.get_two_sided() -> bool
unreal.Covering3DWidgetComponent.get_user_widget_object() -> UserWidget
unreal.Covering3DWidgetComponent.get_widget() -> UserWidget
unreal.Covering3DWidgetComponent.get_widget_space() -> CoveringWidgetSpace
unreal.Covering3DWidgetComponent.get_window_focusable() -> bool
unreal.Covering3DWidgetComponent.get_window_visibility() -> CoveringWindowVisibility
unreal.Covering3DWidgetComponent.is_widget_visible() -> bool
unreal.Covering3DWidgetComponent.request_redraw() -> None
unreal.Covering3DWidgetComponent.set_background_color(new_background_color: LinearColor) -> None
unreal.Covering3DWidgetComponent.set_cylinder_arc_angle(cylinder_arc_angle: float) -> None
unreal.Covering3DWidgetComponent.set_draw_at_desired_size(draw_at_desired_size: bool) -> None
unreal.Covering3DWidgetComponent.set_draw_size(size: Vector2D) -> None
unreal.Covering3DWidgetComponent.set_geometry_mode(geometry_mode: CoveringWidgetGeometryMode) -> None
unreal.Covering3DWidgetComponent.set_manually_redraw(use_manual_redraw: bool) -> None
unreal.Covering3DWidgetComponent.set_owner_player(local_player: LocalPlayer) -> None
unreal.Covering3DWidgetComponent.set_pivot(pivot: Vector2D) -> None
unreal.Covering3DWidgetComponent.set_redraw_time(redraw_time: float) -> None
unreal.Covering3DWidgetComponent.set_tick_mode(tick_mode: CoveringTickMode) -> None
unreal.Covering3DWidgetComponent.set_tick_when_offscreen(want_tick_when_offscreen: bool) -> None
unreal.Covering3DWidgetComponent.set_tint_color_and_opacity(new_tint_color_and_opacity: LinearColor) -> None
unreal.Covering3DWidgetComponent.set_two_sided(want_two_sided: bool) -> None
unreal.Covering3DWidgetComponent.set_widget(widget: UserWidget) -> None
unreal.Covering3DWidgetComponent.set_widget_space(new_space: CoveringWidgetSpace) -> None
unreal.Covering3DWidgetComponent.set_window_focusable(window_focusable: bool) -> None
unreal.Covering3DWidgetComponent.set_window_visibility(visibility: CoveringWindowVisibility) -> None
```

## `unreal.CoveringWidgetBase(UserWidget)`

```python
unreal.CoveringWidgetBase.check_unhovered_state(entity: WdpActorEntity, id: int, mouse_position: Vector2D, unhovered_widget: Widget = None) -> bool
unreal.CoveringWidgetBase.handle_on_destory(entity: WdpActorEntity, id: int) -> bool
unreal.CoveringWidgetBase.handle_on_hovered(entity: WdpActorEntity, id: int, mouse_position: Vector2D) -> bool
unreal.CoveringWidgetBase.handle_on_unhovered(entity: WdpActorEntity, id: int, mouse_position: Vector2D, is_pending: bool) -> bool
unreal.CoveringWidgetBase.on_hover_state_changed(entity: WdpActorEntity, id: int, is_hovered: bool, mouse_position: Vector2D) -> None
unreal.CoveringWidgetBase.on_wdp_focus_lost(entity: WdpActorEntity, id: int, mouse_position: Vector2D) -> None
unreal.CoveringWidgetBase.on_wdp_focus_received(entity: WdpActorEntity, id: int, mouse_position: Vector2D) -> None
```

## `unreal.CreateWindowParams(ParamsBase)`

```python
unreal.CreateWindowParams.__init__(point_entity_eid: str = "", window_style: CoverWindowStyle = ["", [600.000000, 510.000000], [0.000000, 0.000000]], coord_z_ref: int = 0) -> None
unreal.CreateWindowParams.coord_z_ref(value: int) -> None
unreal.CreateWindowParams.point_entity_eid(value: str) -> None
unreal.CreateWindowParams.window_style(value: CoverWindowStyle) -> None
```

## `unreal.CreateWindowParams_Batch(ParamsBase)`

```python
unreal.CreateWindowParams_Batch.__init__(default_param: CreateWindowsParams = ["", ["", [600.000000, 510.000000], [0.000000, 0.000000]], 0], batch_params: Array[CreateWindowsParams] = []) -> None
unreal.CreateWindowParams_Batch.batch_params(value: Array[CreateWindowsParams]) -> None
unreal.CreateWindowParams_Batch.default_param(value: CreateWindowsParams) -> None
```

## `unreal.CreateWindowsParams(StructBase)`

```python
unreal.CreateWindowsParams.__init__(point_entity_eid: str = "", window_style: CoverWindowStyle = ["", [600.000000, 510.000000], [0.000000, 0.000000]], coord_z_ref: int = 0) -> None
unreal.CreateWindowsParams.coord_z_ref(value: int) -> None
unreal.CreateWindowsParams.point_entity_eid(value: str) -> None
unreal.CreateWindowsParams.window_style(value: CoverWindowStyle) -> None
```

## `unreal.CustomPoiIconWidgetBase(CoveringWidgetBase)`

```python
unreal.CustomPoiIconWidgetBase.create_icon(widget_component: WidgetComponent, visible2d_atom: Visible2DAtom) -> bool
unreal.CustomPoiIconWidgetBase.set_icon_size(size: Vector2D) -> bool
unreal.CustomPoiIconWidgetBase.set_icon_url(url: str) -> bool
unreal.CustomPoiIconWidgetBase.set_icon_visible2d_atom(visible2d_atom: Visible2DAtom) -> bool
unreal.CustomPoiIconWidgetBase.set_poi_entity_actor(p_entity: CustomPoiEntity) -> None
```

## `unreal.CustomPoiWidgetBase(CoveringWidgetBase)`

```python
unreal.CustomPoiWidgetBase.create_poi(p_widget_component: CoveringWidgetComponent, point: Vector, enity_name: Name, custom_poi_entity_atom: CustomPoiEntityAtom) -> bool
unreal.CustomPoiWidgetBase.do_wdp_pick_action(pick: bool) -> None
unreal.CustomPoiWidgetBase.enable_debugging() -> None
unreal.CustomPoiWidgetBase.execute_scale_mode(scale_mode: str, location: Vector, threshold: float) -> None
unreal.CustomPoiWidgetBase.notify_button_clicked(select: bool) -> None
unreal.CustomPoiWidgetBase.notify_poi_image_load_finished(sucees: bool) -> None
unreal.CustomPoiWidgetBase.on_button_clicked(value: CustomPoiButtonClickedDelegate) -> None
unreal.CustomPoiWidgetBase.parent_visble2d_atom(value: Visible2DAtom) -> None
unreal.CustomPoiWidgetBase.parent_widget_class(value: Class) -> None
unreal.CustomPoiWidgetBase.parent_widget_component(value: CoveringWidgetComponent) -> None
unreal.CustomPoiWidgetBase.reset_z_order() -> None
unreal.CustomPoiWidgetBase.set_poi_entity_actor(p_entity: CustomPoiEntity) -> None
unreal.CustomPoiWidgetBase.set_point(point: Vector) -> bool
unreal.CustomPoiWidgetBase.set_z_order(z_order: int) -> None
unreal.CustomPoiWidgetBase.setgeneral_label_style(newgeneral_label_style: CustomPoiLabelContentStyle) -> bool
unreal.CustomPoiWidgetBase.setlabel_content(label_content: Array[str]) -> bool
unreal.CustomPoiWidgetBase.setlabel_style(label_style: CustomPoiLabelStyle) -> bool
unreal.CustomPoiWidgetBase.setmarker_activate_url(marker_activate_url: str) -> bool
unreal.CustomPoiWidgetBase.setmarker_normal_url(marker_normal_url: str) -> bool
unreal.CustomPoiWidgetBase.setmarker_offset(marker_offset: Vector2D) -> bool
unreal.CustomPoiWidgetBase.setmarker_size(marker_size: str) -> bool
unreal.CustomPoiWidgetBase.setmarker_visible(visible: bool) -> bool
unreal.CustomPoiWidgetBase.setspecific_label_style(newspecific_label_style: Map[str, CustomPoiLabelContentStyle]) -> bool
```

## `unreal.CustomWidgetNavigationDelegate(DelegateBase)`

```python
unreal.CustomWidgetNavigationDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.DeprecateSlateVector2D(Vector2f)`

```python
unreal.DeprecateSlateVector2D.__init__() -> None
```

## `unreal.Draw2DItemWidget(UserWidget)`

```python
unreal.Draw2DItemWidget.box_arr() -> Array[Box2D]
unreal.Draw2DItemWidget.get_lines() -> Array[Vector2D]
unreal.Draw2DItemWidget.style() -> RectangleStyle
```

## `unreal.DrawSelectBoxWidget(UserWidget)`

```python
unreal.DrawSelectBoxWidget.box_arr() -> Array[Box2D]
unreal.DrawSelectBoxWidget.get_lines() -> Array[Vector2D]
```

## `unreal.EarthDragBorderWidget(ContentWidget)`

```python
unreal.EarthDragBorderWidget.on_drag_enter_event(value: OnDragEnterEvent) -> None
unreal.EarthDragBorderWidget.on_drag_leave_event(value: OnDragLeaveEvent) -> None
unreal.EarthDragBorderWidget.on_drag_over_event(value: OnDragOverEvent) -> None
unreal.EarthDragBorderWidget.on_drop_handle(value: OnDropEvent) -> None
```

## `unreal.EarthNestTabContentWidget(EarthTabContentWidget)`

```python
unreal.EarthNestTabContentWidget.tab_list(value: EarthTabListWidget) -> None
```

## `unreal.EarthPropertyItemWidget(UserWidget)`

```python
unreal.EarthPropertyItemWidget.get_entity_type() -> AesEditingEntityType
unreal.EarthPropertyItemWidget.get_property_name() -> Name
unreal.EarthPropertyItemWidget.get_unique_bool_property() -> Optional[bool]
unreal.EarthPropertyItemWidget.get_unique_float_property() -> Optional[float]
unreal.EarthPropertyItemWidget.get_unique_int_property() -> Optional[int]
unreal.EarthPropertyItemWidget.get_unique_string_property() -> Optional[str]
unreal.EarthPropertyItemWidget.get_unique_vector_x_property() -> Optional[float]
unreal.EarthPropertyItemWidget.get_unique_vector_y_property() -> Optional[float]
unreal.EarthPropertyItemWidget.get_unique_vector_z_property() -> Optional[float]
unreal.EarthPropertyItemWidget.on_property_item_variant_changed(value: OnPropertyItemVariantChanged) -> None
unreal.EarthPropertyItemWidget.set_unique_bool_property(property_value: bool) -> None
unreal.EarthPropertyItemWidget.set_unique_float_property(property_value: float) -> None
unreal.EarthPropertyItemWidget.set_unique_int_property(property_value: int) -> None
unreal.EarthPropertyItemWidget.set_unique_string_property(property_value: str) -> None
unreal.EarthPropertyItemWidget.set_unique_vector_x_property(property_value: float) -> None
unreal.EarthPropertyItemWidget.set_unique_vector_y_property(property_value: float) -> None
unreal.EarthPropertyItemWidget.set_unique_vector_z_property(property_value: float) -> None
unreal.EarthPropertyItemWidget.show_property() -> None
```

## `unreal.EarthPropertyItemWidget_Color(EarthPropertyItemWidget)`

```python
unreal.EarthPropertyItemWidget_Color.get_unique_color_property() -> Optional[Color]
unreal.EarthPropertyItemWidget_Color.set_unique_color_property(property_value: Color) -> None
```

## `unreal.EarthPropertyItemWidget_Enum(EarthPropertyItemWidget)`

```python
unreal.EarthPropertyItemWidget_Enum.get_display_names() -> Array[str]
unreal.EarthPropertyItemWidget_Enum.get_unique_enum_property() -> Optional[int]
unreal.EarthPropertyItemWidget_Enum.set_unique_enum_property(property_value_index: int) -> None
```

## `unreal.EarthPropertyListWidget(EarthTabContentWidget)`

```python
unreal.EarthPropertyListWidget.add_child(child: Widget, flags: AesEditorPropertyFlags) -> None
unreal.EarthPropertyListWidget.clear_children() -> None
unreal.EarthPropertyListWidget.customized_item_class(value: Map[Name, Class]) -> None
unreal.EarthPropertyListWidget.get_all_children() -> Array[Widget]
unreal.EarthPropertyListWidget.refresh_list() -> None
unreal.EarthPropertyListWidget.set_entity_count(entity_count: int) -> None
unreal.EarthPropertyListWidget.set_entity_name(entity_name: str) -> None
unreal.EarthPropertyListWidget.typed_item_class(value: Map[EarthPropertyType, Class]) -> None
```

## `unreal.EarthTabButtonWidget(UserWidget)`

```python
unreal.EarthTabButtonWidget.auto_execute_command(value: bool) -> None
unreal.EarthTabButtonWidget.button(value: Button) -> None
unreal.EarthTabButtonWidget.button_display_name(value: Text) -> None
unreal.EarthTabButtonWidget.button_name(value: Name) -> None
unreal.EarthTabButtonWidget.button_texture(value: Texture) -> None
unreal.EarthTabButtonWidget.command_class(value: Class) -> None
unreal.EarthTabButtonWidget.command_key(value: str) -> None
unreal.EarthTabButtonWidget.command_param_key(value: str) -> None
unreal.EarthTabButtonWidget.execute_command_manually() -> None
unreal.EarthTabButtonWidget.execute_command_once() -> None
unreal.EarthTabButtonWidget.finish_command_manually() -> None
unreal.EarthTabButtonWidget.freeze_command(frozen: bool) -> None
unreal.EarthTabButtonWidget.get_checked() -> bool
unreal.EarthTabButtonWidget.get_enabled() -> bool
unreal.EarthTabButtonWidget.on_checked(value: OnEarthTabButtonChecked) -> None
unreal.EarthTabButtonWidget.on_clicked() -> None
unreal.EarthTabButtonWidget.on_unchecked(value: OnEarthTabButtonUnchecked) -> None
unreal.EarthTabButtonWidget.set_button_display_name(button_display_name: Text) -> None
unreal.EarthTabButtonWidget.set_button_style() -> None
unreal.EarthTabButtonWidget.set_button_texture(button_texture: Texture) -> None
unreal.EarthTabButtonWidget.set_checked(checked: bool) -> None
unreal.EarthTabButtonWidget.set_enabled(enabled: bool) -> None
unreal.EarthTabButtonWidget.widget_class(value: Class) -> None
unreal.EarthTabButtonWidget.widget_data(value: DataTable) -> None
```

## `unreal.EarthTabButtonWidget_MeshRegistry(EarthTabButtonWidget)`

```python
unreal.EarthTabButtonWidget_MeshRegistry.execute_command() -> None
```

## `unreal.EarthTabContentWidget(UserWidget)`

```python
unreal.EarthTabContentWidget.content_data(value: DataTable) -> None
unreal.EarthTabContentWidget.post_set_content_data() -> None
unreal.EarthTabContentWidget.set_content_data(content_data: DataTable) -> None
```

## `unreal.EarthTabListWidget(UserWidget)`

```python
unreal.EarthTabListWidget.add_panel_child(child: UserWidget) -> None
unreal.EarthTabListWidget.current_button(value: EarthTabButtonWidget) -> None
unreal.EarthTabListWidget.current_content(value: EarthTabContentWidget) -> None
unreal.EarthTabListWidget.get_current_index() -> int
unreal.EarthTabListWidget.on_changed(value: OnEarthTabButtonChanged) -> None
unreal.EarthTabListWidget.panel(value: PanelWidget) -> None
unreal.EarthTabListWidget.post_set_tab_list_info() -> None
unreal.EarthTabListWidget.set_tab_button_checked(index: int) -> None
unreal.EarthTabListWidget.set_tab_list_info(tab_list_info: DataTable) -> None
unreal.EarthTabListWidget.tab_buttons(value: Map[int, EarthTabButtonWidget]) -> None
unreal.EarthTabListWidget.tab_list_info(value: DataTable) -> None
unreal.EarthTabListWidget.widget_switcher(value: WidgetSwitcher) -> None
```

## `unreal.EarthTabListWidget_MeshRegistry(EarthTabListWidget)`

```python
unreal.EarthTabListWidget_MeshRegistry.button_class(value: Class) -> None
unreal.EarthTabListWidget_MeshRegistry.command_class(value: Class) -> None
unreal.EarthTabListWidget_MeshRegistry.layer_name(value: Name) -> None
unreal.EarthTabListWidget_MeshRegistry.refresh_button_textures() -> None
unreal.EarthTabListWidget_MeshRegistry.refresh_buttons() -> None
```

## `unreal.EditorUtilityLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorUtilityLibrary.convert_to_editor_utility_widget(widget_bp: WidgetBlueprint) -> None
unreal.EditorUtilityLibrary.get_actor_reference(path_to_actor: str) -> Actor
unreal.EditorUtilityLibrary.get_current_content_browser_item_path() -> ContentBrowserItemPath
unreal.EditorUtilityLibrary.get_current_content_browser_path() -> Optional[str]
unreal.EditorUtilityLibrary.get_selected_asset_data() -> Array[AssetData]
unreal.EditorUtilityLibrary.get_selected_assets() -> Array[Object]
unreal.EditorUtilityLibrary.get_selected_assets_of_class(asset_class: Class) -> Array[Object]
unreal.EditorUtilityLibrary.get_selected_blueprint_classes() -> Array[Class]
unreal.EditorUtilityLibrary.get_selected_folder_paths() -> Array[str]
unreal.EditorUtilityLibrary.get_selected_path_view_folder_paths() -> Array[str]
unreal.EditorUtilityLibrary.get_selection_bounds() -> Tuple[Vector, Vector, float]
unreal.EditorUtilityLibrary.get_selection_set() -> Array[Actor]
unreal.EditorUtilityLibrary.rename_asset(asset: Object, new_name: str) -> None
unreal.EditorUtilityLibrary.sync_browser_to_folders(folder_list: Array[str]) -> None
```

## `unreal.EditorUtilityObject(Object)`

```python
unreal.EditorUtilityObject.run() -> None
```

## `unreal.EditorUtilityTask(Object)`

```python
unreal.EditorUtilityTask.finish_executing_task() -> None
unreal.EditorUtilityTask.get_task_title_override() -> Text
unreal.EditorUtilityTask.receive_begin_execution() -> None
unreal.EditorUtilityTask.receive_cancel_requested() -> None
unreal.EditorUtilityTask.set_task_notification_text(text: Text) -> None
unreal.EditorUtilityTask.was_cancel_requested() -> bool
```

## `unreal.EditorUtilityWidget(UserWidget)`

```python
unreal.EditorUtilityWidget.auto_run_default_action() -> bool
unreal.EditorUtilityWidget.help_text(value: str) -> None
unreal.EditorUtilityWidget.on_default_action_clicked() -> None
unreal.EditorUtilityWidget.run() -> None
unreal.EditorUtilityWidget.tab_display_name(value: Text) -> None
```

## `unreal.GameViewportWidgetSlot(StructBase)`

```python
unreal.GameViewportWidgetSlot.__init__(anchors: Anchors = [[0.000000, 0.000000], [0.000000, 0.000000]], offsets: Margin = [0.000000, 0.000000, 0.000000, 0.000000], alignment: Vector2D = [0.000000, 0.000000], z_order: int = 0, auto_remove_on_world_removed: bool = False) -> None
unreal.GameViewportWidgetSlot.alignment(value: Vector2D) -> None
unreal.GameViewportWidgetSlot.anchors(value: Anchors) -> None
unreal.GameViewportWidgetSlot.auto_remove_on_world_removed(value: bool) -> None
unreal.GameViewportWidgetSlot.offsets(value: Margin) -> None
unreal.GameViewportWidgetSlot.z_order(value: int) -> None
```

## `unreal.GetWindowParams(ResultBase)`

```python
unreal.GetWindowParams.__init__(message: str = "", scene_change_info: WdpSceneChangeInfo = [[], [], []], success: bool = False, point_entity_eid: str = "", window_style: CoverWindowStyle = ["", [600.000000, 510.000000], [0.000000, 0.000000]], coord_z_ref: int = 0) -> None
unreal.GetWindowParams.coord_z_ref(value: int) -> None
unreal.GetWindowParams.point_entity_eid(value: str) -> None
unreal.GetWindowParams.window_style(value: CoverWindowStyle) -> None
```

## `unreal.GlobalEditorUtilityBase(Object)`

```python
unreal.GlobalEditorUtilityBase.auto_run_default_action() -> bool
unreal.GlobalEditorUtilityBase.clear_actor_selection_set() -> None
unreal.GlobalEditorUtilityBase.for_each_selected_actor() -> None
unreal.GlobalEditorUtilityBase.for_each_selected_asset() -> None
unreal.GlobalEditorUtilityBase.get_actor_reference(path_to_actor: str) -> Actor
unreal.GlobalEditorUtilityBase.get_editor_user_settings() -> EditorPerProjectUserSettings
unreal.GlobalEditorUtilityBase.get_selected_assets() -> Array[Object]
unreal.GlobalEditorUtilityBase.get_selection_bounds() -> Tuple[Vector, Vector, float]
unreal.GlobalEditorUtilityBase.get_selection_set() -> Array[Actor]
unreal.GlobalEditorUtilityBase.help_text(value: str) -> None
unreal.GlobalEditorUtilityBase.on_default_action_clicked() -> None
unreal.GlobalEditorUtilityBase.on_each_selected_actor(value: ForEachActorIteratorSignature) -> None
unreal.GlobalEditorUtilityBase.on_each_selected_asset(value: ForEachAssetIteratorSignature) -> None
unreal.GlobalEditorUtilityBase.rename_asset(asset: Object, new_name: str) -> None
unreal.GlobalEditorUtilityBase.select_nothing() -> None
unreal.GlobalEditorUtilityBase.set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
```

## `unreal.GridPanel(PanelWidget)`

```python
unreal.GridPanel.add_child_to_grid(content: Widget, row: int = 0, column: int = 0) -> GridSlot
unreal.GridPanel.column_fill() -> Array[float]
unreal.GridPanel.row_fill() -> Array[float]
unreal.GridPanel.set_column_fill(column_index: int, coefficient: float) -> None
unreal.GridPanel.set_row_fill(row_index: int, coefficient: float) -> None
```

## `unreal.MenuAnchor_GetUserWidget(DelegateBase)`

```python
unreal.MenuAnchor_GetUserWidget.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.MiniMapWidgetBase(UserWidget)`

```python
unreal.MiniMapWidgetBase.end_mini_map() -> bool
unreal.MiniMapWidgetBase.start_mini_map(position: Vector2D, size: float, bg_url: str, needle_url: str, mask_url: str, frame_url: str, mapping_anchors_a: Vector, mapping_anchors_b: Vector, anchors: str) -> bool
```

## `unreal.ObjectMixerEditorUWidget(Widget)`

```python
unreal.ObjectMixerEditorUWidget.object_mixer_widget_user_config(value: ObjectMixerWidgetUserConfig) -> None
```

## `unreal.ObjectMixerWidgetUserConfig(StructBase)`

```python
unreal.ObjectMixerWidgetUserConfig.__init__(default_filter_class: Class = None) -> None
unreal.ObjectMixerWidgetUserConfig.default_filter_class(value: Class) -> None
```

## `unreal.OnEditorUtilityPIEEvent(MulticastDelegateBase)`

```python
unreal.OnEditorUtilityPIEEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnEditorUtilityTaskDynamicDelegate(MulticastDelegateBase)`

```python
unreal.OnEditorUtilityTaskDynamicDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnHoveredWidgetChanged(MulticastDelegateBase)`

```python
unreal.OnHoveredWidgetChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.OnTakeRecorderPanelChanged(DelegateBase)`

```python
unreal.OnTakeRecorderPanelChanged.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.PanelSlot(Visual)`

```python
unreal.PanelSlot.get_content() -> Widget
```

## `unreal.PanelWidget(Widget)`

```python
unreal.PanelWidget.add_child(content: Widget) -> PanelSlot
unreal.PanelWidget.clear_children() -> None
unreal.PanelWidget.get_all_children() -> Array[Widget]
unreal.PanelWidget.get_child_at(index: int) -> Widget
unreal.PanelWidget.get_child_index(content: Widget) -> int
unreal.PanelWidget.get_children_count() -> int
unreal.PanelWidget.has_any_children() -> bool
unreal.PanelWidget.has_child(content: Widget) -> bool
unreal.PanelWidget.remove_child(content: Widget) -> bool
unreal.PanelWidget.remove_child_at(index: int) -> bool
```

## `unreal.PlaceWindowActionParams(ActionParamsBase)`

```python
unreal.PlaceWindowActionParams.name(value: str) -> None
unreal.PlaceWindowActionParams.offset(value: Vector2D) -> None
unreal.PlaceWindowActionParams.size(value: Vector2D) -> None
unreal.PlaceWindowActionParams.snap_mode(value: WdpSnapGroundMode) -> None
unreal.PlaceWindowActionParams.url(value: str) -> None
```

## `unreal.PlacedEditorUtilityBase(Actor)`

```python
unreal.PlacedEditorUtilityBase.clear_actor_selection_set() -> None
unreal.PlacedEditorUtilityBase.get_actor_reference(path_to_actor: str) -> Actor
unreal.PlacedEditorUtilityBase.get_level_viewport_camera_info() -> Optional[Tuple[Vector, Rotator]]
unreal.PlacedEditorUtilityBase.get_selection_set() -> Array[Actor]
unreal.PlacedEditorUtilityBase.help_text(value: str) -> None
unreal.PlacedEditorUtilityBase.select_nothing() -> None
unreal.PlacedEditorUtilityBase.set_actor_selection_state(actor: Actor, should_be_selected: bool) -> None
unreal.PlacedEditorUtilityBase.set_level_viewport_camera_info(camera_location: Vector, camera_rotation: Rotator) -> None
```

## `unreal.PoiIconWidgetBase(CoveringWidgetBase)`

```python
unreal.PoiIconWidgetBase.create_icon(widget_component: WidgetComponent, visible2d_atom: Visible2DAtom) -> bool
unreal.PoiIconWidgetBase.set_icon_size(size: Vector2D) -> bool
unreal.PoiIconWidgetBase.set_icon_url(url: str) -> bool
unreal.PoiIconWidgetBase.set_icon_visible2d_atom(visible2d_atom: Visible2DAtom) -> bool
unreal.PoiIconWidgetBase.set_poi_entity_actor(p_entity: PoiEntity) -> None
```

## `unreal.PoiWidgetBase(CoveringWidgetBase)`

```python
unreal.PoiWidgetBase.create_poi(p_widget_component: CoveringWidgetComponent, point: Vector, enity_name: Name, poi_entity_atom: PoiEntityAtom) -> bool
unreal.PoiWidgetBase.do_wdp_pick_action(pick: bool) -> None
unreal.PoiWidgetBase.enable_debugging() -> None
unreal.PoiWidgetBase.execute_scale_mode(scale_mode: str, location: Vector, threshold: float) -> None
unreal.PoiWidgetBase.notify_button_clicked(select: bool) -> None
unreal.PoiWidgetBase.notify_poi_image_load_finished(sucees: bool) -> None
unreal.PoiWidgetBase.on_button_clicked(value: MyButtonClickedDelegate) -> None
unreal.PoiWidgetBase.parent_visble2d_atom(value: Visible2DAtom) -> None
unreal.PoiWidgetBase.parent_widget_class(value: Class) -> None
unreal.PoiWidgetBase.parent_widget_component(value: CoveringWidgetComponent) -> None
unreal.PoiWidgetBase.reset_z_order() -> None
unreal.PoiWidgetBase.set_poi_entity_actor(p_entity: PoiEntity) -> None
unreal.PoiWidgetBase.set_point(point: Vector) -> bool
unreal.PoiWidgetBase.set_z_order(z_order: int) -> None
unreal.PoiWidgetBase.setgeneral_label_style(newgeneral_label_style: PoiLabelContentStyle) -> bool
unreal.PoiWidgetBase.setlabel_bg_image_url(label_bg_image_url: str) -> bool
unreal.PoiWidgetBase.setlabel_bg_offset(label_bg_offset: str) -> bool
unreal.PoiWidgetBase.setlabel_bg_size(label_bg_size: str) -> bool
unreal.PoiWidgetBase.setlabel_content(label_content: Array[str]) -> bool
unreal.PoiWidgetBase.setlabel_content_autowrap(auto_wrap: bool) -> bool
unreal.PoiWidgetBase.setlabel_content_justification(label_content_justification: str) -> bool
unreal.PoiWidgetBase.setlabel_content_offset(label_content_offset: Vector2D) -> bool
unreal.PoiWidgetBase.setlabel_contents(label_contents: Array[str]) -> bool
unreal.PoiWidgetBase.setlabel_top(top: bool) -> None
unreal.PoiWidgetBase.setlabel_ui(label_ui: str) -> bool
unreal.PoiWidgetBase.setlabel_visible(visible: bool) -> bool
unreal.PoiWidgetBase.setmarker_activate_url(marker_activate_url: str) -> bool
unreal.PoiWidgetBase.setmarker_normal_url(marker_normal_url: str) -> bool
unreal.PoiWidgetBase.setmarker_offset(marker_offset: Vector2D) -> bool
unreal.PoiWidgetBase.setmarker_size(marker_size: str) -> bool
unreal.PoiWidgetBase.setmarker_ui(marker_ui: str) -> bool
unreal.PoiWidgetBase.setmarker_visible(visible: bool) -> bool
unreal.PoiWidgetBase.setscroll_policy(policy: str) -> bool
unreal.PoiWidgetBase.setscroll_speed(speed: float) -> bool
unreal.PoiWidgetBase.setspecific_label_style(newspecific_label_style: Map[str, PoiLabelContentStyle]) -> bool
unreal.PoiWidgetBase.settext_box_width(box_width: float) -> bool
```

## `unreal.PointWidget(UserWidget)`

```python
unreal.PointWidget.data(value: PointGraphicsData) -> None
unreal.PointWidget.get_data() -> PointGraphicsData
unreal.PointWidget.on_close_clicked() -> None
unreal.PointWidget.refresh_widget() -> None
unreal.PointWidget.set_data(new_data: PointGraphicsData) -> None
unreal.PointWidget.set_image_color(in_color: LinearColor) -> None
```

## `unreal.PointsWidget(UserWidget)`

```python
unreal.PointsWidget.container_panel() -> CanvasPanel
unreal.PointsWidget.point_widgets() -> Map[Guid, PointWidget]
```

## `unreal.PreviewableWidgetVariant(StructBase)`

```python
unreal.PreviewableWidgetVariant.__init__(object_path: SoftObjectPath = [""]) -> None
unreal.PreviewableWidgetVariant.object_path() -> SoftObjectPath
```

## `unreal.ProgressWidgetStyle(SlateWidgetStyleContainerBase)`

```python
unreal.ProgressWidgetStyle.progress_bar_style(value: ProgressBarStyle) -> None
```

## `unreal.PyTestSlateTickDelegate(DelegateBase)`

```python
unreal.PyTestSlateTickDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.RealTimeVideoWidgetBase(CoveringWidgetBase)`

```python
unreal.RealTimeVideoWidgetBase.create_real_time_video(p_widget_component: CoveringWidgetComponent, point: Vector, enity_name: Name, real_time_video_entity_atom: RealTimeVideoEntityAtom) -> bool
unreal.RealTimeVideoWidgetBase.notify_real_time_video_load_finished(sucees: bool) -> None
unreal.RealTimeVideoWidgetBase.set_bg_overlap(new_bg_overlap: str) -> bool
unreal.RealTimeVideoWidgetBase.set_bg_padding(new_bg_padding: Array[int]) -> bool
unreal.RealTimeVideoWidgetBase.set_bg_url(new_bg_url: str) -> bool
unreal.RealTimeVideoWidgetBase.set_bokeh(new_bokeh: float) -> bool
unreal.RealTimeVideoWidgetBase.set_btn_activate_url(new_btn_activate_url: str) -> bool
unreal.RealTimeVideoWidgetBase.set_btn_normal_url(new_btn_normal_url: str) -> bool
unreal.RealTimeVideoWidgetBase.set_btn_offset(new_btn_offset: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_btn_size(new_btn_size: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_conrner_shift(new_conrner_shift: Array[Vector2D]) -> bool
unreal.RealTimeVideoWidgetBase.set_label_content(new_label_content: Array[str]) -> bool
unreal.RealTimeVideoWidgetBase.set_label_content_auto_wrap(new_label_content_auto_wrap: bool) -> bool
unreal.RealTimeVideoWidgetBase.set_label_content_justification(new_label_content_justification: str) -> bool
unreal.RealTimeVideoWidgetBase.set_label_offset(new_label_offset: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_label_size(new_label_size: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_offset(new_offset: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_point(point: Vector) -> bool
unreal.RealTimeVideoWidgetBase.set_real_time_video_entity_actor(p_entity: RealTimeVideoEntity) -> None
unreal.RealTimeVideoWidgetBase.set_resolution(new_resolution: Vector2D) -> bool
unreal.RealTimeVideoWidgetBase.set_state(new_state: str) -> bool
unreal.RealTimeVideoWidgetBase.set_url(new_url: str) -> bool
```

## `unreal.RoadStyleWidget(UserWidget)`

```python
unreal.RoadStyleWidget.get_f_class() -> str
unreal.RoadStyleWidget.get_prefab_id() -> str
unreal.RoadStyleWidget.set_f_class_and_prefab_id(class_: str, prefab_id: str) -> None
```

## `unreal.ScriptSlateIcon(StructBase)`

```python
unreal.ScriptSlateIcon.__init__(style_set_name: Name = "None", style_name: Name = "None", small_style_name: Name = "None") -> None
unreal.ScriptSlateIcon.small_style_name(value: Name) -> None
unreal.ScriptSlateIcon.style_name(value: Name) -> None
unreal.ScriptSlateIcon.style_set_name(value: Name) -> None
```

## `unreal.SlateAccessibleWidgetData_GetText(DelegateBase)`

```python
unreal.SlateAccessibleWidgetData_GetText.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.SlateBrush(StructBase)`

```python
unreal.SlateBrush.__init__(tint_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], draw_as: SlateBrushDrawType = SlateBrushDrawType.NO_DRAW_TYPE, tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE, mirroring: SlateBrushMirrorType = SlateBrushMirrorType.NO_MIRROR, image_size: DeprecateSlateVector2D = [0.000000, 0.000000], margin: Margin = [0.000000, 0.000000, 0.000000, 0.000000], resource_object: Object = None, outline_settings: SlateBrushOutlineSettings = [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]) -> None
unreal.SlateBrush.draw_as(value: SlateBrushDrawType) -> None
unreal.SlateBrush.image_size(value: DeprecateSlateVector2D) -> None
unreal.SlateBrush.margin(value: Margin) -> None
unreal.SlateBrush.mirroring(value: SlateBrushMirrorType) -> None
unreal.SlateBrush.outline_settings(value: SlateBrushOutlineSettings) -> None
unreal.SlateBrush.resource_object(value: Object) -> None
unreal.SlateBrush.texture_object(value: Object) -> None
unreal.SlateBrush.tiling(value: SlateBrushTileType) -> None
unreal.SlateBrush.tint_color(value: SlateColor) -> None
```

## `unreal.SlateBrushOutlineSettings(StructBase)`

```python
unreal.SlateBrushOutlineSettings.__init__(corner_radii: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000], color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], width: float = 0.000000, rounding_type: SlateBrushRoundingType = SlateBrushRoundingType.FIXED_RADIUS, use_brush_transparency: bool = False) -> None
unreal.SlateBrushOutlineSettings.color(value: SlateColor) -> None
unreal.SlateBrushOutlineSettings.corner_radii(value: Vector4) -> None
unreal.SlateBrushOutlineSettings.rounding_type(value: SlateBrushRoundingType) -> None
unreal.SlateBrushOutlineSettings.use_brush_transparency(value: bool) -> None
unreal.SlateBrushOutlineSettings.width(value: float) -> None
```

## `unreal.SlateChildSize(StructBase)`

```python
unreal.SlateChildSize.__init__(value: float = 0.000000, size_rule: SlateSizeRule = SlateSizeRule.AUTOMATIC) -> None
unreal.SlateChildSize.size_rule(value: SlateSizeRule) -> None
unreal.SlateChildSize.value(value: float) -> None
```

## `unreal.SlateColor(StructBase)`

```python
unreal.SlateColor.__init__(specified_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000], color_use_rule: SlateColorStylingMode = SlateColorStylingMode.USE_COLOR_SPECIFIED) -> None
unreal.SlateColor.color_use_rule(value: SlateColorStylingMode) -> None
unreal.SlateColor.specified_color(value: LinearColor) -> None
```

## `unreal.SlateFontInfo(StructBase)`

```python
unreal.SlateFontInfo.__init__(font_object: Object = None, font_material: Object = None, outline_settings: FontOutlineSettings = [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], typeface_font_name: Name = "None", size: float = 0.000000, letter_spacing: int = 0, skew_amount: float = 0.000000, force_monospaced: bool = False, material_is_stencil: bool = False, monospaced_width: float = 0.000000) -> None
unreal.SlateFontInfo.font_material(value: Object) -> None
unreal.SlateFontInfo.font_object(value: Object) -> None
unreal.SlateFontInfo.force_monospaced(value: bool) -> None
unreal.SlateFontInfo.letter_spacing(value: int) -> None
unreal.SlateFontInfo.material_is_stencil(value: bool) -> None
unreal.SlateFontInfo.monospaced_width(value: float) -> None
unreal.SlateFontInfo.outline_settings(value: FontOutlineSettings) -> None
unreal.SlateFontInfo.size(value: float) -> None
unreal.SlateFontInfo.skew_amount(value: float) -> None
unreal.SlateFontInfo.typeface_font_name(value: Name) -> None
```

## `unreal.SlateLibrary(BlueprintFunctionLibrary)`

```python
unreal.SlateLibrary.absolute_to_local(geometry: Geometry, absolute_coordinate: Vector2D) -> Vector2D
unreal.SlateLibrary.absolute_to_viewport(world_context_object: Object, absolute_desktop_coordinate: Vector2D) -> Tuple[Vector2D, Vector2D]
unreal.SlateLibrary.equal_equal_slate_brush(a: SlateBrush, b: SlateBrush) -> bool
unreal.SlateLibrary.get_absolute_size(geometry: Geometry) -> Vector2D
unreal.SlateLibrary.get_local_size(geometry: Geometry) -> Vector2D
unreal.SlateLibrary.get_local_top_left(geometry: Geometry) -> Vector2D
unreal.SlateLibrary.is_under_location(geometry: Geometry, absolute_coordinate: Vector2D) -> bool
unreal.SlateLibrary.local_to_absolute(geometry: Geometry, local_coordinate: Vector2D) -> Vector2D
unreal.SlateLibrary.local_to_viewport(world_context_object: Object, geometry: Geometry, local_coordinate: Vector2D) -> Tuple[Vector2D, Vector2D]
unreal.SlateLibrary.screen_to_viewport(world_context_object: Object, screen_position: Vector2D) -> Vector2D
unreal.SlateLibrary.screen_to_widget_absolute(world_context_object: Object, screen_position: Vector2D, include_window_position: bool = False) -> Vector2D
unreal.SlateLibrary.screen_to_widget_local(world_context_object: Object, geometry: Geometry, screen_position: Vector2D, include_window_position: bool = False) -> Vector2D
unreal.SlateLibrary.transform_scalar_absolute_to_local(geometry: Geometry, absolute_scalar: float) -> float
unreal.SlateLibrary.transform_scalar_local_to_absolute(geometry: Geometry, local_scalar: float) -> float
unreal.SlateLibrary.transform_vector_absolute_to_local(geometry: Geometry, absolute_vector: Vector2D) -> Vector2D
unreal.SlateLibrary.transform_vector_local_to_absolute(geometry: Geometry, local_vector: Vector2D) -> Vector2D
```

## `unreal.SlateModifierKeysState(StructBase)`

```python
unreal.SlateModifierKeysState.__init__() -> None
```

## `unreal.SlatePostBufferBlur(SlateRHIPostBufferProcessor)`

```python
unreal.SlatePostBufferBlur.gaussian_blur_strength(value: float) -> None
```

## `unreal.SlatePostBufferUpdateInfo(StructBase)`

```python
unreal.SlatePostBufferUpdateInfo.__init__() -> None
```

## `unreal.SlatePostSettings(StructBase)`

```python
unreal.SlatePostSettings.__init__(enabled: bool = False, post_processor_class: Class = None) -> None
unreal.SlatePostSettings.enabled(value: bool) -> None
unreal.SlatePostSettings.post_processor_class(value: Class) -> None
```

## `unreal.SlateSound(StructBase)`

```python
unreal.SlateSound.__init__(resource_object: Object = None) -> None
unreal.SlateSound.resource_object(value: Object) -> None
```

## `unreal.SlateWidgetStyle(StructBase)`

```python
unreal.SlateWidgetStyle.__init__() -> None
```

## `unreal.SoundEffectPresetWidgetInterface(AudioPanelWidgetInterface)`

```python
unreal.SoundEffectPresetWidgetInterface.get_class() -> Class
unreal.SoundEffectPresetWidgetInterface.on_constructed(preset: SoundEffectPreset) -> None
unreal.SoundEffectPresetWidgetInterface.on_property_changed(preset: SoundEffectPreset, property_name: Name) -> None
```

## `unreal.SoundSubmixWidgetInterface(Interface)`

```python
unreal.SoundSubmixWidgetInterface.on_constructed(sound_submix: SoundSubmixBase) -> None
```

## `unreal.SynthSlateStyle(SlateWidgetStyle)`

```python
unreal.SynthSlateStyle.__init__(size_type: SynthSlateSizeType = SynthSlateSizeType.SMALL, color_style: SynthSlateColorStyle = SynthSlateColorStyle.LIGHT) -> None
unreal.SynthSlateStyle.color_style(value: SynthSlateColorStyle) -> None
unreal.SynthSlateStyle.size_type(value: SynthSlateSizeType) -> None
```

## `unreal.TakeRecorderOverlayWidget(UserWidget)`

```python
unreal.TakeRecorderOverlayWidget.recorder() -> TakeRecorder
```

## `unreal.TakeRecorderPanel(Object)`

```python
unreal.TakeRecorderPanel.can_start_recording() -> Optional[Text]
unreal.TakeRecorderPanel.clear_pending_take() -> None
unreal.TakeRecorderPanel.get_frame_rate() -> FrameRate
unreal.TakeRecorderPanel.get_last_recorded_level_sequence() -> LevelSequence
unreal.TakeRecorderPanel.get_level_sequence() -> LevelSequence
unreal.TakeRecorderPanel.get_mode() -> TakeRecorderPanelMode
unreal.TakeRecorderPanel.get_sources() -> TakeRecorderSources
unreal.TakeRecorderPanel.get_take_meta_data() -> TakeMetaData
unreal.TakeRecorderPanel.set_frame_rate(frame_rate: FrameRate) -> None
unreal.TakeRecorderPanel.set_frame_rate_from_timecode(from_timecode: bool) -> None
unreal.TakeRecorderPanel.setup_for_editing(take_preset: TakePreset) -> None
unreal.TakeRecorderPanel.setup_for_recording_into_level_sequence(level_sequence_asset: LevelSequence) -> None
unreal.TakeRecorderPanel.setup_for_recording_level_sequence(level_sequence_asset: LevelSequence) -> None
unreal.TakeRecorderPanel.setup_for_recording_take_preset(take_preset_asset: TakePreset) -> None
unreal.TakeRecorderPanel.setup_for_viewing(level_sequence_asset: LevelSequence) -> None
unreal.TakeRecorderPanel.start_recording() -> None
unreal.TakeRecorderPanel.stop_recording() -> None
```

## `unreal.TextLayoutWidget(Widget)`

```python
unreal.TextLayoutWidget.apply_line_height_to_bottom_line(value: bool) -> None
unreal.TextLayoutWidget.auto_wrap_text(value: bool) -> None
unreal.TextLayoutWidget.justification(value: TextJustify) -> None
unreal.TextLayoutWidget.line_height_percentage(value: float) -> None
unreal.TextLayoutWidget.margin(value: Margin) -> None
unreal.TextLayoutWidget.shaped_text_options(value: ShapedTextOptions) -> None
unreal.TextLayoutWidget.wrap_text_at(value: float) -> None
unreal.TextLayoutWidget.wrapping_policy(value: TextWrappingPolicy) -> None
```

## `unreal.ToolBarStyle(SlateWidgetStyle)`

```python
unreal.ToolBarStyle.__init__(background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], expand_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], separator_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], label_style: TextBlockStyle = [[None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], TextTransformPolicy.NONE, TextOverflowPolicy.CLIP], editable_text_style: EditableTextBoxStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [4.000000, 2.000000, 4.000000, 2.000000], [[None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "Regular", 9.000000, 0, 0.000000, False, False, 1.000000], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000, 0.000000], 0], [[[0.000000, 0.000000, 0.000000, 0.000000], 0], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], TextTransformPolicy.NONE, TextOverflowPolicy.CLIP], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 16.000000]], toggle_button: CheckBoxStyle = [SlateCheckBoxType.CHECK_BOX, [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [2.000000, 0.000000, 0.000000, 0.000000], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]], combo_button_style: ComboButtonStyle = [[[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [0.000000, 0.000000, 0.000000, 0.000000], [5.000000, 5.000000, 5.000000, 5.000000], [2.000000, 2.000000, 2.000000, 2.000000], VerticalAlignment.V_ALIGN_CENTER], settings_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], settings_combo_button: ComboButtonStyle = [[[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [0.000000, 0.000000, 0.000000, 0.000000], [5.000000, 5.000000, 5.000000, 5.000000], [2.000000, 2.000000, 2.000000, 2.000000], VerticalAlignment.V_ALIGN_CENTER], settings_toggle_button: CheckBoxStyle = [SlateCheckBoxType.CHECK_BOX, [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [2.000000, 0.000000, 0.000000, 0.000000], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]], button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], label_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], uniform_block_width: float = 0.000000, uniform_block_height: float = 0.000000, num_columns: int = 0, icon_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], separator_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], separator_thickness: float = 0.000000, combo_button_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], button_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], check_box_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], block_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], indented_block_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], background_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], icon_size: DeprecateSlateVector2D = [0.000000, 0.000000], show_labels: bool = False, button_content_max_width: float = 0.000000, button_content_fill_width: float = 0.000000, icon_padding_with_visible_label: Margin = [0.000000, 0.000000, 0.000000, 0.000000], icon_padding_with_collapsed_label: Margin = [0.000000, 0.000000, 0.000000, 0.000000], vertical_alignment_override: type = ()) -> None
unreal.ToolBarStyle.background_brush(value: SlateBrush) -> None
unreal.ToolBarStyle.background_padding(value: Margin) -> None
unreal.ToolBarStyle.block_padding(value: Margin) -> None
unreal.ToolBarStyle.button_content_fill_width(value: float) -> None
unreal.ToolBarStyle.button_content_max_width(value: float) -> None
unreal.ToolBarStyle.button_padding(value: Margin) -> None
unreal.ToolBarStyle.button_style(value: ButtonStyle) -> None
unreal.ToolBarStyle.check_box_padding(value: Margin) -> None
unreal.ToolBarStyle.combo_button_padding(value: Margin) -> None
unreal.ToolBarStyle.combo_button_style(value: ComboButtonStyle) -> None
unreal.ToolBarStyle.editable_text_style(value: EditableTextBoxStyle) -> None
unreal.ToolBarStyle.expand_brush(value: SlateBrush) -> None
unreal.ToolBarStyle.icon_padding(value: Margin) -> None
unreal.ToolBarStyle.icon_padding_with_collapsed_label(value: Margin) -> None
unreal.ToolBarStyle.icon_padding_with_visible_label(value: Margin) -> None
unreal.ToolBarStyle.icon_size(value: DeprecateSlateVector2D) -> None
unreal.ToolBarStyle.indented_block_padding(value: Margin) -> None
unreal.ToolBarStyle.label_padding(value: Margin) -> None
unreal.ToolBarStyle.label_style(value: TextBlockStyle) -> None
unreal.ToolBarStyle.num_columns(value: int) -> None
unreal.ToolBarStyle.separator_brush(value: SlateBrush) -> None
unreal.ToolBarStyle.separator_padding(value: Margin) -> None
unreal.ToolBarStyle.separator_thickness(value: float) -> None
unreal.ToolBarStyle.settings_button_style(value: ButtonStyle) -> None
unreal.ToolBarStyle.settings_combo_button(value: ComboButtonStyle) -> None
unreal.ToolBarStyle.settings_toggle_button(value: CheckBoxStyle) -> None
unreal.ToolBarStyle.show_labels(value: bool) -> None
unreal.ToolBarStyle.toggle_button(value: CheckBoxStyle) -> None
unreal.ToolBarStyle.uniform_block_height(value: float) -> None
unreal.ToolBarStyle.uniform_block_width(value: float) -> None
unreal.ToolBarStyle.vertical_alignment_override(value: type) -> None
```

## `unreal.ToolMenuWidget(Widget)`

```python
unreal.ToolMenuWidget.full_menu_name() -> Name
unreal.ToolMenuWidget.menu_name() -> str
unreal.ToolMenuWidget.menu_type() -> MultiBoxType
```

## `unreal.ToolkitWidgetStyle(SlateWidgetStyle)`

```python
unreal.ToolkitWidgetStyle.__init__(title_background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], tool_details_background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], title_foreground_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], title_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], active_tool_title_border_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], tool_context_text_block_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000], title_font: SlateFontInfo = [None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000]) -> None
unreal.ToolkitWidgetStyle.active_tool_title_border_padding(value: Margin) -> None
unreal.ToolkitWidgetStyle.title_background_brush(value: SlateBrush) -> None
unreal.ToolkitWidgetStyle.title_font(value: SlateFontInfo) -> None
unreal.ToolkitWidgetStyle.title_foreground_color(value: SlateColor) -> None
unreal.ToolkitWidgetStyle.title_padding(value: Margin) -> None
unreal.ToolkitWidgetStyle.tool_context_text_block_padding(value: Margin) -> None
unreal.ToolkitWidgetStyle.tool_details_background_brush(value: SlateBrush) -> None
```

## `unreal.UniformGridPanel(PanelWidget)`

```python
unreal.UniformGridPanel.add_child_to_uniform_grid(content: Widget, row: int = 0, column: int = 0) -> UniformGridSlot
unreal.UniformGridPanel.min_desired_slot_height(value: float) -> None
unreal.UniformGridPanel.min_desired_slot_width(value: float) -> None
unreal.UniformGridPanel.set_min_desired_slot_height(min_desired_slot_height: float) -> None
unreal.UniformGridPanel.set_min_desired_slot_width(min_desired_slot_width: float) -> None
unreal.UniformGridPanel.set_slot_padding(slot_padding: Margin) -> None
unreal.UniformGridPanel.slot_padding(value: Margin) -> None
```

## `unreal.UpdateWindowParams(ParamsBase)`

```python
unreal.UpdateWindowParams.__init__(eid: str = "", point_entity_eid: str = "", window_style: CoverWindowStyle = ["", [600.000000, 510.000000], [0.000000, 0.000000]], coord_z_ref: int = 0) -> None
unreal.UpdateWindowParams.coord_z_ref(value: int) -> None
unreal.UpdateWindowParams.eid(value: str) -> None
unreal.UpdateWindowParams.point_entity_eid(value: str) -> None
unreal.UpdateWindowParams.window_style(value: CoverWindowStyle) -> None
```

## `unreal.UserWidget(Widget)`

```python
unreal.UserWidget.add_extension(extension_type: Class) -> UserWidgetExtension
unreal.UserWidget.add_to_player_screen(z_order: int = 0) -> bool
unreal.UserWidget.add_to_viewport(z_order: int = 0) -> None
unreal.UserWidget.bind_to_animation_event(animation: WidgetAnimation, delegate: WidgetAnimationDynamicEvent, animation_event: WidgetAnimationEvent, user_tag: Name = "None") -> None
unreal.UserWidget.bind_to_animation_finished(animation: WidgetAnimation, delegate: WidgetAnimationDynamicEvent) -> None
unreal.UserWidget.bind_to_animation_started(animation: WidgetAnimation, delegate: WidgetAnimationDynamicEvent) -> None
unreal.UserWidget.cancel_latent_actions() -> None
unreal.UserWidget.color_and_opacity(value: LinearColor) -> None
unreal.UserWidget.construct() -> None
unreal.UserWidget.destruct() -> None
unreal.UserWidget.flush_animations() -> None
unreal.UserWidget.foreground_color(value: SlateColor) -> None
unreal.UserWidget.get_alignment_in_viewport() -> Vector2D
unreal.UserWidget.get_anchors_in_viewport() -> Anchors
unreal.UserWidget.get_animation_current_time(animation: WidgetAnimation) -> float
unreal.UserWidget.get_extension(extension_type: Class) -> UserWidgetExtension
unreal.UserWidget.get_extensions(extension_type: Class) -> Array[UserWidgetExtension]
unreal.UserWidget.get_is_visible() -> bool
unreal.UserWidget.get_owning_player_camera_manager() -> PlayerCameraManager
unreal.UserWidget.get_owning_player_pawn() -> Pawn
unreal.UserWidget.is_animation_playing(animation: WidgetAnimation) -> bool
unreal.UserWidget.is_animation_playing_forward(animation: WidgetAnimation) -> bool
unreal.UserWidget.is_any_animation_playing() -> bool
unreal.UserWidget.is_focusable(value: bool) -> None
unreal.UserWidget.is_interactable() -> bool
unreal.UserWidget.is_listening_for_input_action(action_name: Name) -> bool
unreal.UserWidget.is_playing_animation() -> bool
unreal.UserWidget.listen_for_input_action(action_name: Name, event_type: InputEventType, consume: bool, callback: OnInputAction) -> None
unreal.UserWidget.on_added_to_focus_path(focus_event: FocusEvent) -> None
unreal.UserWidget.on_analog_value_changed(my_geometry: Geometry, analog_input_event: AnalogInputEvent) -> EventReply
unreal.UserWidget.on_animation_finished(animation: WidgetAnimation) -> None
unreal.UserWidget.on_animation_started(animation: WidgetAnimation) -> None
unreal.UserWidget.on_drag_cancelled(pointer_event: PointerEvent, operation: DragDropOperation) -> None
unreal.UserWidget.on_drag_detected(my_geometry: Geometry, pointer_event: PointerEvent) -> DragDropOperation
unreal.UserWidget.on_drag_enter(my_geometry: Geometry, pointer_event: PointerEvent, operation: DragDropOperation) -> None
unreal.UserWidget.on_drag_leave(pointer_event: PointerEvent, operation: DragDropOperation) -> None
unreal.UserWidget.on_drag_over(my_geometry: Geometry, pointer_event: PointerEvent, operation: DragDropOperation) -> bool
unreal.UserWidget.on_drop(my_geometry: Geometry, pointer_event: PointerEvent, operation: DragDropOperation) -> bool
unreal.UserWidget.on_focus_lost(focus_event: FocusEvent) -> None
unreal.UserWidget.on_focus_received(my_geometry: Geometry, focus_event: FocusEvent) -> EventReply
unreal.UserWidget.on_initialized() -> None
unreal.UserWidget.on_key_char(my_geometry: Geometry, character_event: CharacterEvent) -> EventReply
unreal.UserWidget.on_key_down(my_geometry: Geometry, key_event: KeyEvent) -> EventReply
unreal.UserWidget.on_key_up(my_geometry: Geometry, key_event: KeyEvent) -> EventReply
unreal.UserWidget.on_motion_detected(my_geometry: Geometry, motion_event: MotionEvent) -> EventReply
unreal.UserWidget.on_mouse_button_double_click(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_mouse_button_down(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_mouse_button_up(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_mouse_capture_lost() -> None
unreal.UserWidget.on_mouse_enter(my_geometry: Geometry, mouse_event: PointerEvent) -> None
unreal.UserWidget.on_mouse_leave(mouse_event: PointerEvent) -> None
unreal.UserWidget.on_mouse_move(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_mouse_wheel(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_paint(context: PaintContext) -> PaintContext
unreal.UserWidget.on_preview_key_down(my_geometry: Geometry, key_event: KeyEvent) -> EventReply
unreal.UserWidget.on_preview_mouse_button_down(my_geometry: Geometry, mouse_event: PointerEvent) -> EventReply
unreal.UserWidget.on_removed_from_focus_path(focus_event: FocusEvent) -> None
unreal.UserWidget.on_touch_ended(my_geometry: Geometry, touch_event: PointerEvent) -> EventReply
unreal.UserWidget.on_touch_force_changed(my_geometry: Geometry, touch_event: PointerEvent) -> EventReply
unreal.UserWidget.on_touch_gesture(my_geometry: Geometry, gesture_event: PointerEvent) -> EventReply
unreal.UserWidget.on_touch_moved(my_geometry: Geometry, touch_event: PointerEvent) -> EventReply
unreal.UserWidget.on_touch_started(my_geometry: Geometry, touch_event: PointerEvent) -> EventReply
unreal.UserWidget.on_visibility_changed(value: OnVisibilityChangedEvent) -> None
unreal.UserWidget.padding(value: Margin) -> None
unreal.UserWidget.pause_animation(animation: WidgetAnimation) -> float
unreal.UserWidget.play_animation(animation: WidgetAnimation, start_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_animation_at_time(animation: WidgetAnimation, start_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_animation_forward(animation: WidgetAnimation, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_animation_reverse(animation: WidgetAnimation, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_animation_time_range(animation: WidgetAnimation, start_at_time: float = 0.000000, end_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_animation_to(animation: WidgetAnimation, start_at_time: float = 0.000000, end_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> UMGSequencePlayer
unreal.UserWidget.play_sound(sound_to_play: SoundBase) -> None
unreal.UserWidget.pre_construct(is_design_time: bool) -> None
unreal.UserWidget.priority(value: int) -> None
unreal.UserWidget.queue_pause_animation(animation: WidgetAnimation) -> float
unreal.UserWidget.queue_play_animation(animation: WidgetAnimation, start_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> None
unreal.UserWidget.queue_play_animation_forward(animation: WidgetAnimation, playback_speed: float = 1.000000, restore_state: bool = False) -> None
unreal.UserWidget.queue_play_animation_reverse(animation: WidgetAnimation, playback_speed: float = 1.000000, restore_state: bool = False) -> None
unreal.UserWidget.queue_play_animation_time_range(animation: WidgetAnimation, start_at_time: float = 0.000000, end_at_time: float = 0.000000, num_loops_to_play: int = 1, play_mode: UMGSequencePlayMode = UMGSequencePlayMode.FORWARD, playback_speed: float = 1.000000, restore_state: bool = False) -> None
unreal.UserWidget.queue_stop_all_animations() -> None
unreal.UserWidget.queue_stop_animation(animation: WidgetAnimation) -> None
unreal.UserWidget.register_input_component() -> None
unreal.UserWidget.remove_extension(extension: UserWidgetExtension) -> None
unreal.UserWidget.remove_extensions(extension_type: Class) -> None
unreal.UserWidget.remove_from_viewport() -> None
unreal.UserWidget.reverse_animation(animation: WidgetAnimation) -> None
unreal.UserWidget.set_alignment_in_viewport(alignment: Vector2D) -> None
unreal.UserWidget.set_anchors_in_viewport(anchors: Anchors) -> None
unreal.UserWidget.set_animation_current_time(animation: WidgetAnimation, time: float) -> None
unreal.UserWidget.set_color_and_opacity(color_and_opacity: LinearColor) -> None
unreal.UserWidget.set_desired_size_in_viewport(size: Vector2D) -> None
unreal.UserWidget.set_foreground_color(foreground_color: SlateColor) -> None
unreal.UserWidget.set_input_action_blocking(should_block: bool) -> None
unreal.UserWidget.set_input_action_priority(new_priority: int) -> None
unreal.UserWidget.set_num_loops_to_play(animation: WidgetAnimation, num_loops_to_play: int) -> None
unreal.UserWidget.set_owning_player(local_player_controller: PlayerController) -> None
unreal.UserWidget.set_padding(padding: Margin) -> None
unreal.UserWidget.set_playback_speed(animation: WidgetAnimation, playback_speed: float = 1.000000) -> None
unreal.UserWidget.set_position_in_viewport(position: Vector2D, remove_dpi_scale: bool = True) -> None
unreal.UserWidget.stop_action(value: bool) -> None
unreal.UserWidget.stop_all_animations() -> None
unreal.UserWidget.stop_animation(animation: WidgetAnimation) -> None
unreal.UserWidget.stop_animations_and_latent_actions() -> None
unreal.UserWidget.stop_listening_for_all_input_actions() -> None
unreal.UserWidget.stop_listening_for_input_action(action_name: Name, event_type: InputEventType) -> None
unreal.UserWidget.tick(my_geometry: Geometry, delta_time: float) -> None
unreal.UserWidget.tick_frequency() -> WidgetTickFrequency
unreal.UserWidget.unbind_all_from_animation_finished(animation: WidgetAnimation) -> None
unreal.UserWidget.unbind_all_from_animation_started(animation: WidgetAnimation) -> None
unreal.UserWidget.unbind_from_animation_finished(animation: WidgetAnimation, delegate: WidgetAnimationDynamicEvent) -> None
unreal.UserWidget.unbind_from_animation_started(animation: WidgetAnimation, delegate: WidgetAnimationDynamicEvent) -> None
unreal.UserWidget.unregister_input_component() -> None
```

## `unreal.WaterMarkerWidgetBase(UserWidget)`

```python
unreal.WaterMarkerWidgetBase.water_marker_event(water_marker: WdpWatermarker) -> None
```

## `unreal.WdpProjectToolWidget(EditorUtilityWidget)`

```python
unreal.WdpProjectToolWidget.actor_name_editable_text_weak_ptr(value: EditableText) -> None
unreal.WdpProjectToolWidget.edit_id_tool_vertical_box(value: VerticalBox) -> None
unreal.WdpProjectToolWidget.eid_editable_text_weak_ptr(value: EditableText) -> None
unreal.WdpProjectToolWidget.instance_index_editable_text_weak_ptr(value: EditableText) -> None
unreal.WdpProjectToolWidget.instance_name_editable_text_weak_ptr(value: EditableText) -> None
unreal.WdpProjectToolWidget.layer_name(value: ComboBoxString) -> None
unreal.WdpProjectToolWidget.layer_name_for_update(value: ComboBoxString) -> None
unreal.WdpProjectToolWidget.node_id_editable_text_weak_ptr(value: EditableText) -> None
unreal.WdpProjectToolWidget.update_id() -> None
```

## `unreal.Widget(Visual)`

```python
unreal.Widget.add_field_value_changed_delegate(field_id: FieldNotificationId, delegate: FieldValueChangedDynamicDelegate) -> None
unreal.Widget.broadcast_field_value_changed(field_id: FieldNotificationId) -> None
unreal.Widget.clip_to_bounds(value: WidgetClipping) -> None
unreal.Widget.clipping(value: WidgetClipping) -> None
unreal.Widget.cursor(value: MouseCursor) -> None
unreal.Widget.flow_direction_preference(value: FlowDirectionPreference) -> None
unreal.Widget.force_layout_prepass() -> None
unreal.Widget.force_volatile(force: bool) -> None
unreal.Widget.get_accessible_summary_text() -> Text
unreal.Widget.get_accessible_text() -> Text
unreal.Widget.get_cached_geometry() -> Geometry
unreal.Widget.get_clipping() -> WidgetClipping
unreal.Widget.get_desired_size() -> Vector2D
unreal.Widget.get_game_instance() -> GameInstance
unreal.Widget.get_is_enabled() -> bool
unreal.Widget.get_opacity() -> float
unreal.Widget.get_owning_local_player() -> LocalPlayer
unreal.Widget.get_owning_player() -> PlayerController
unreal.Widget.get_paint_space_geometry() -> Geometry
unreal.Widget.get_parent() -> PanelWidget
unreal.Widget.get_render_opacity() -> float
unreal.Widget.get_render_transform_angle() -> float
unreal.Widget.get_tick_space_geometry() -> Geometry
unreal.Widget.get_visibility() -> SlateVisibility
unreal.Widget.has_any_user_focus() -> bool
unreal.Widget.has_focused_descendants() -> bool
unreal.Widget.has_keyboard_focus() -> bool
unreal.Widget.has_mouse_capture() -> bool
unreal.Widget.has_mouse_capture_by_user(user_index: int, pointer_index: int = -1) -> bool
unreal.Widget.has_user_focus(player_controller: PlayerController) -> bool
unreal.Widget.has_user_focused_descendants(player_controller: PlayerController) -> bool
unreal.Widget.invalidate_layout_and_volatility() -> None
unreal.Widget.is_enabled(value: bool) -> None
unreal.Widget.is_hovered() -> bool
unreal.Widget.is_in_viewport() -> bool
unreal.Widget.is_rendered() -> bool
unreal.Widget.is_visible() -> bool
unreal.Widget.is_volatile() -> bool
unreal.Widget.navigation() -> WidgetNavigation
unreal.Widget.opacity(value: float) -> None
unreal.Widget.pixel_snapping(value: WidgetPixelSnapping) -> None
unreal.Widget.remove_field_value_changed_delegate(field_id: FieldNotificationId, delegate: FieldValueChangedDynamicDelegate) -> None
unreal.Widget.remove_from_parent() -> None
unreal.Widget.render_opacity(value: float) -> None
unreal.Widget.render_transform(value: WidgetTransform) -> None
unreal.Widget.render_transform_pivot(value: Vector2D) -> None
unreal.Widget.reset_cursor() -> None
unreal.Widget.set_all_navigation_rules(rule: UINavigationRule, widget_to_focus: Name) -> None
unreal.Widget.set_clipping(clipping: WidgetClipping) -> None
unreal.Widget.set_cursor(cursor: MouseCursor) -> None
unreal.Widget.set_focus() -> None
unreal.Widget.set_is_enabled(is_enabled: bool) -> None
unreal.Widget.set_keyboard_focus() -> None
unreal.Widget.set_navigation_rule(direction: UINavigation, rule: UINavigationRule, widget_to_focus: Name) -> None
unreal.Widget.set_navigation_rule_base(direction: UINavigation, rule: UINavigationRule) -> None
unreal.Widget.set_navigation_rule_custom(direction: UINavigation, custom_delegate: CustomWidgetNavigationDelegate) -> None
unreal.Widget.set_navigation_rule_custom_boundary(direction: UINavigation, custom_delegate: CustomWidgetNavigationDelegate) -> None
unreal.Widget.set_navigation_rule_explicit(direction: UINavigation, widget: Widget) -> None
unreal.Widget.set_opacity(opacity: float) -> None
unreal.Widget.set_render_angle(angle: float) -> None
unreal.Widget.set_render_opacity(opacity: float) -> None
unreal.Widget.set_render_scale(scale: Vector2D) -> None
unreal.Widget.set_render_shear(shear: Vector2D) -> None
unreal.Widget.set_render_transform(transform: WidgetTransform) -> None
unreal.Widget.set_render_transform_angle(angle: float) -> None
unreal.Widget.set_render_transform_pivot(pivot: Vector2D) -> None
unreal.Widget.set_render_translation(translation: Vector2D) -> None
unreal.Widget.set_tool_tip(widget: Widget) -> None
unreal.Widget.set_tool_tip_text(tool_tip_text: Text) -> None
unreal.Widget.set_user_focus(player_controller: PlayerController) -> None
unreal.Widget.set_visibility(visibility: SlateVisibility) -> None
unreal.Widget.slot() -> PanelSlot
unreal.Widget.tool_tip_text(value: Text) -> None
unreal.Widget.tool_tip_widget() -> Widget
unreal.Widget.visibility(value: SlateVisibility) -> None
unreal.Widget.visiblity(value: SlateVisibility) -> None
```

## `unreal.WidgetCarouselNavigationBarStyle(SlateWidgetStyle)`

```python
unreal.WidgetCarouselNavigationBarStyle.__init__(highlight_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], left_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], center_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], right_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]]) -> None
unreal.WidgetCarouselNavigationBarStyle.center_button_style(value: ButtonStyle) -> None
unreal.WidgetCarouselNavigationBarStyle.highlight_brush(value: SlateBrush) -> None
unreal.WidgetCarouselNavigationBarStyle.left_button_style(value: ButtonStyle) -> None
unreal.WidgetCarouselNavigationBarStyle.right_button_style(value: ButtonStyle) -> None
```

## `unreal.WidgetChild(StructBase)`

```python
unreal.WidgetChild.__init__() -> None
```

## `unreal.WidgetComponent(MeshComponent)`

```python
unreal.WidgetComponent.get_current_draw_size() -> Vector2D
unreal.WidgetComponent.get_cylinder_arc_angle() -> float
unreal.WidgetComponent.get_draw_at_desired_size() -> bool
unreal.WidgetComponent.get_draw_size() -> Vector2D
unreal.WidgetComponent.get_geometry_mode() -> WidgetGeometryMode
unreal.WidgetComponent.get_manually_redraw() -> bool
unreal.WidgetComponent.get_material_instance() -> MaterialInstanceDynamic
unreal.WidgetComponent.get_owner_player() -> LocalPlayer
unreal.WidgetComponent.get_pivot() -> Vector2D
unreal.WidgetComponent.get_redraw_time() -> float
unreal.WidgetComponent.get_render_target() -> TextureRenderTarget2D
unreal.WidgetComponent.get_tick_when_offscreen() -> bool
unreal.WidgetComponent.get_two_sided() -> bool
unreal.WidgetComponent.get_user_widget_object() -> UserWidget
unreal.WidgetComponent.get_widget() -> UserWidget
unreal.WidgetComponent.get_widget_space() -> WidgetSpace
unreal.WidgetComponent.get_window_focusable() -> bool
unreal.WidgetComponent.get_window_visiblility() -> WindowVisibility
unreal.WidgetComponent.is_widget_visible() -> bool
unreal.WidgetComponent.request_redraw() -> None
unreal.WidgetComponent.request_render_update() -> None
unreal.WidgetComponent.set_background_color(new_background_color: LinearColor) -> None
unreal.WidgetComponent.set_cylinder_arc_angle(cylinder_arc_angle: float) -> None
unreal.WidgetComponent.set_draw_at_desired_size(draw_at_desired_size: bool) -> None
unreal.WidgetComponent.set_draw_size(size: Vector2D) -> None
unreal.WidgetComponent.set_geometry_mode(geometry_mode: WidgetGeometryMode) -> None
unreal.WidgetComponent.set_manually_redraw(use_manual_redraw: bool) -> None
unreal.WidgetComponent.set_owner_player(local_player: LocalPlayer) -> None
unreal.WidgetComponent.set_pivot(pivot: Vector2D) -> None
unreal.WidgetComponent.set_redraw_time(redraw_time: float) -> None
unreal.WidgetComponent.set_tick_mode(tick_mode: TickMode) -> None
unreal.WidgetComponent.set_tick_when_offscreen(want_tick_when_offscreen: bool) -> None
unreal.WidgetComponent.set_tint_color_and_opacity(new_tint_color_and_opacity: LinearColor) -> None
unreal.WidgetComponent.set_two_sided(want_two_sided: bool) -> None
unreal.WidgetComponent.set_widget(widget: UserWidget) -> None
unreal.WidgetComponent.set_widget_space(new_space: WidgetSpace) -> None
unreal.WidgetComponent.set_window_focusable(window_focusable: bool) -> None
unreal.WidgetComponent.set_window_visibility(visibility: WindowVisibility) -> None
```

## `unreal.WidgetEventField(StructBase)`

```python
unreal.WidgetEventField.__init__() -> None
```

## `unreal.WidgetInteractionComponent(SceneComponent)`

```python
unreal.WidgetInteractionComponent.debug_color(value: LinearColor) -> None
unreal.WidgetInteractionComponent.debug_line_thickness(value: float) -> None
unreal.WidgetInteractionComponent.debug_sphere_line_thickness(value: float) -> None
unreal.WidgetInteractionComponent.enable_hit_testing(value: bool) -> None
unreal.WidgetInteractionComponent.get2d_hit_location() -> Vector2D
unreal.WidgetInteractionComponent.get_hovered_widget_component() -> WidgetComponent
unreal.WidgetInteractionComponent.get_last_hit_result() -> HitResult
unreal.WidgetInteractionComponent.interaction_distance(value: float) -> None
unreal.WidgetInteractionComponent.interaction_source(value: WidgetInteractionSource) -> None
unreal.WidgetInteractionComponent.is_over_focusable_widget() -> bool
unreal.WidgetInteractionComponent.is_over_hit_test_visible_widget() -> bool
unreal.WidgetInteractionComponent.is_over_interactable_widget() -> bool
unreal.WidgetInteractionComponent.on_hovered_widget_changed(value: OnHoveredWidgetChanged) -> None
unreal.WidgetInteractionComponent.pointer_index(value: int) -> None
unreal.WidgetInteractionComponent.press_and_release_key(key: Key) -> bool
unreal.WidgetInteractionComponent.press_key(key: Key, repeat: bool = False) -> bool
unreal.WidgetInteractionComponent.press_pointer_key(key: Key) -> None
unreal.WidgetInteractionComponent.release_key(key: Key) -> bool
unreal.WidgetInteractionComponent.release_pointer_key(key: Key) -> None
unreal.WidgetInteractionComponent.scroll_wheel(scroll_delta: float) -> None
unreal.WidgetInteractionComponent.send_key_char(characters: str, repeat: bool = False) -> bool
unreal.WidgetInteractionComponent.set_custom_hit_result(hit_result: HitResult) -> None
unreal.WidgetInteractionComponent.set_focus(focus_widget: Widget) -> None
unreal.WidgetInteractionComponent.show_debug(value: bool) -> None
unreal.WidgetInteractionComponent.trace_channel(value: CollisionChannel) -> None
unreal.WidgetInteractionComponent.virtual_user_index(value: int) -> None
```

## `unreal.WidgetLayoutLibrary(BlueprintFunctionLibrary)`

```python
unreal.WidgetLayoutLibrary.get_mouse_position_on_platform() -> Vector2D
unreal.WidgetLayoutLibrary.get_mouse_position_on_viewport(world_context_object: Object) -> Vector2D
unreal.WidgetLayoutLibrary.get_mouse_position_scaled_by_dpi(player: PlayerController) -> Optional[Tuple[float, float]]
unreal.WidgetLayoutLibrary.get_player_screen_widget_geometry(player_controller: PlayerController) -> Geometry
unreal.WidgetLayoutLibrary.get_viewport_scale(world_context_object: Object) -> float
unreal.WidgetLayoutLibrary.get_viewport_size(world_context_object: Object) -> Vector2D
unreal.WidgetLayoutLibrary.get_viewport_widget_geometry(world_context_object: Object) -> Geometry
unreal.WidgetLayoutLibrary.project_world_location_to_widget_position(player_controller: PlayerController, world_location: Vector, player_viewport_relative: bool) -> Optional[Vector2D]
unreal.WidgetLayoutLibrary.remove_all_widgets(world_context_object: Object) -> None
unreal.WidgetLayoutLibrary.slot_as_border_slot(widget: Widget) -> BorderSlot
unreal.WidgetLayoutLibrary.slot_as_canvas_slot(widget: Widget) -> CanvasPanelSlot
unreal.WidgetLayoutLibrary.slot_as_grid_slot(widget: Widget) -> GridSlot
unreal.WidgetLayoutLibrary.slot_as_horizontal_box_slot(widget: Widget) -> HorizontalBoxSlot
unreal.WidgetLayoutLibrary.slot_as_overlay_slot(widget: Widget) -> OverlaySlot
unreal.WidgetLayoutLibrary.slot_as_safe_box_slot(widget: Widget) -> SafeZoneSlot
unreal.WidgetLayoutLibrary.slot_as_scale_box_slot(widget: Widget) -> ScaleBoxSlot
unreal.WidgetLayoutLibrary.slot_as_scroll_box_slot(widget: Widget) -> ScrollBoxSlot
unreal.WidgetLayoutLibrary.slot_as_size_box_slot(widget: Widget) -> SizeBoxSlot
unreal.WidgetLayoutLibrary.slot_as_uniform_grid_slot(widget: Widget) -> UniformGridSlot
unreal.WidgetLayoutLibrary.slot_as_vertical_box_slot(widget: Widget) -> VerticalBoxSlot
unreal.WidgetLayoutLibrary.slot_as_widget_switcher_slot(widget: Widget) -> WidgetSwitcherSlot
unreal.WidgetLayoutLibrary.slot_as_wrap_box_slot(widget: Widget) -> WrapBoxSlot
```

## `unreal.WidgetLibrary(BlueprintFunctionLibrary)`

```python
unreal.WidgetLibrary.cancel_drag_drop() -> None
unreal.WidgetLibrary.capture_joystick(reply: EventReply, capturing_widget: Widget, all_joysticks: bool = False) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.capture_mouse(reply: EventReply, capturing_widget: Widget) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.clear_user_focus(reply: EventReply, all_users: bool = False) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.detect_drag(reply: EventReply, widget_detecting_drag: Widget, drag_key: Key) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.detect_drag_if_pressed(pointer_event: PointerEvent, widget_detecting_drag: Widget, drag_key: Key) -> EventReply
unreal.WidgetLibrary.dismiss_all_menus() -> None
unreal.WidgetLibrary.draw_box(context: PaintContext, position: Vector2D, size: Vector2D, brush: SlateBrushAsset, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
unreal.WidgetLibrary.draw_line(context: PaintContext, position_a: Vector2D, position_b: Vector2D, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], anti_alias: bool = True, thickness: float = 1.000000) -> PaintContext
unreal.WidgetLibrary.draw_lines(context: PaintContext, points: Array[Vector2D], tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], anti_alias: bool = True, thickness: float = 1.000000) -> PaintContext
unreal.WidgetLibrary.draw_spline(context: PaintContext, start: Vector2D, start_dir: Vector2D, end: Vector2D, end_dir: Vector2D, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000], thickness: float = 1.000000) -> PaintContext
unreal.WidgetLibrary.draw_text(context: PaintContext, string: str, position: Vector2D, tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
unreal.WidgetLibrary.draw_text_formatted(context: PaintContext, text: Text, position: Vector2D, font: Font, font_size: float = 16.000000, font_type_face: Name = "Regular", tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000]) -> PaintContext
unreal.WidgetLibrary.end_drag_drop(reply: EventReply) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.get_all_widgets_of_class(world_context_object: Object, widget_class: Class, top_level_only: bool = True) -> Array[UserWidget]
unreal.WidgetLibrary.get_all_widgets_with_interface(world_context_object: Object, interface: Class, top_level_only: bool) -> Array[UserWidget]
unreal.WidgetLibrary.get_brush_resource(brush: SlateBrush) -> Object
unreal.WidgetLibrary.get_brush_resource_as_material(brush: SlateBrush) -> MaterialInterface
unreal.WidgetLibrary.get_brush_resource_as_texture2d(brush: SlateBrush) -> Texture2D
unreal.WidgetLibrary.get_drag_dropping_content() -> DragDropOperation
unreal.WidgetLibrary.get_dynamic_material(brush: SlateBrush) -> Tuple[MaterialInstanceDynamic, SlateBrush]
unreal.WidgetLibrary.get_input_event_from_character_event(event: CharacterEvent) -> InputEvent
unreal.WidgetLibrary.get_input_event_from_key_event(event: KeyEvent) -> InputEvent
unreal.WidgetLibrary.get_input_event_from_navigation_event(event: NavigationEvent) -> InputEvent
unreal.WidgetLibrary.get_input_event_from_pointer_event(event: PointerEvent) -> InputEvent
unreal.WidgetLibrary.get_key_event_from_analog_input_event(event: AnalogInputEvent) -> KeyEvent
unreal.WidgetLibrary.get_safe_zone_padding(world_context_object: Object) -> Tuple[Vector4, Vector2D, Vector4]
unreal.WidgetLibrary.handled() -> EventReply
unreal.WidgetLibrary.is_drag_dropping() -> bool
unreal.WidgetLibrary.lock_mouse(reply: EventReply, capturing_widget: Widget) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.make_brush_from_asset(brush_asset: SlateBrushAsset) -> SlateBrush
unreal.WidgetLibrary.make_brush_from_material(material: MaterialInterface, width: int = 32, height: int = 32) -> SlateBrush
unreal.WidgetLibrary.make_brush_from_texture(texture: Texture2D, width: int = 0, height: int = 0) -> SlateBrush
unreal.WidgetLibrary.no_resource_brush() -> SlateBrush
unreal.WidgetLibrary.release_joystick_capture(reply: EventReply, all_joysticks: bool = False) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.release_mouse_capture(reply: EventReply) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.restore_previous_window_title_bar_state() -> None
unreal.WidgetLibrary.set_brush_resource_to_material(brush: SlateBrush, material: MaterialInterface) -> SlateBrush
unreal.WidgetLibrary.set_brush_resource_to_texture(brush: SlateBrush, texture: Texture2D) -> SlateBrush
unreal.WidgetLibrary.set_color_vision_deficiency_type(type: ColorVisionDeficiency, severity: float, correct_deficiency: bool, show_correction_with_deficiency: bool) -> None
unreal.WidgetLibrary.set_focus_to_game_viewport() -> None
unreal.WidgetLibrary.set_hardware_cursor(world_context_object: Object, cursor_shape: MouseCursor, cursor_name: Name, hot_spot: Vector2D) -> bool
unreal.WidgetLibrary.set_input_mode_game_and_ui_ex(player_controller: PlayerController, widget_to_focus: Widget = None, mouse_lock_mode: MouseLockMode = MouseLockMode.DO_NOT_LOCK, hide_cursor_during_capture: bool = True, flush_input: bool = False) -> None
unreal.WidgetLibrary.set_input_mode_game_only(player_controller: PlayerController, flush_input: bool = False) -> None
unreal.WidgetLibrary.set_input_mode_ui_only_ex(player_controller: PlayerController, widget_to_focus: Widget = None, mouse_lock_mode: MouseLockMode = MouseLockMode.DO_NOT_LOCK, flush_input: bool = False) -> None
unreal.WidgetLibrary.set_mouse_position(reply: EventReply, new_mouse_position: Vector2D) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.set_user_focus(reply: EventReply, focus_widget: Widget, all_users: bool = False) -> Tuple[EventReply, EventReply]
unreal.WidgetLibrary.set_window_title_bar_close_button_active(active: bool) -> None
unreal.WidgetLibrary.set_window_title_bar_on_close_clicked_delegate(delegate: OnGameWindowCloseButtonClickedDelegate) -> None
unreal.WidgetLibrary.set_window_title_bar_state(title_bar_content: Widget, mode: WindowTitleBarMode, title_bar_drag_enabled: bool, window_buttons_visible: bool, title_bar_visible: bool) -> None
unreal.WidgetLibrary.unhandled() -> EventReply
unreal.WidgetLibrary.unlock_mouse(reply: EventReply) -> Tuple[EventReply, EventReply]
```

## `unreal.WidgetLibrary_OnGameWindowCloseButtonClickedDelegate(DelegateBase)`

```python
unreal.WidgetLibrary_OnGameWindowCloseButtonClickedDelegate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WidgetNavigation(Object)`

```python
unreal.WidgetNavigation.down() -> WidgetNavigationData
unreal.WidgetNavigation.left() -> WidgetNavigationData
unreal.WidgetNavigation.next() -> WidgetNavigationData
unreal.WidgetNavigation.previous() -> WidgetNavigationData
unreal.WidgetNavigation.right() -> WidgetNavigationData
unreal.WidgetNavigation.up() -> WidgetNavigationData
```

## `unreal.WidgetNavigationData(StructBase)`

```python
unreal.WidgetNavigationData.__init__(rule: UINavigationRule = UINavigationRule.ESCAPE, widget_to_focus: Name = "None") -> None
unreal.WidgetNavigationData.rule() -> UINavigationRule
unreal.WidgetNavigationData.widget_to_focus() -> Name
```

## `unreal.WidgetPreview(Object)`

```python
unreal.WidgetPreview.get_available_widget_slot_names() -> Array[Name]
unreal.WidgetPreview.get_widget_slot_names() -> Array[Name]
unreal.WidgetPreview.slot_widget_types(value: Map[Name, PreviewableWidgetVariant]) -> None
unreal.WidgetPreview.widget_type(value: PreviewableWidgetVariant) -> None
```

## `unreal.WidgetSwitcher(PanelWidget)`

```python
unreal.WidgetSwitcher.active_widget_index(value: int) -> None
unreal.WidgetSwitcher.get_active_widget() -> Widget
unreal.WidgetSwitcher.get_active_widget_index() -> int
unreal.WidgetSwitcher.get_num_widgets() -> int
unreal.WidgetSwitcher.get_widget_at_index(index: int) -> Widget
unreal.WidgetSwitcher.set_active_widget(widget: Widget) -> None
unreal.WidgetSwitcher.set_active_widget_index(index: int) -> None
```

## `unreal.WidgetSwitcherSlot(PanelSlot)`

```python
unreal.WidgetSwitcherSlot.horizontal_alignment(value: HorizontalAlignment) -> None
unreal.WidgetSwitcherSlot.padding(value: Margin) -> None
unreal.WidgetSwitcherSlot.set_horizontal_alignment(horizontal_alignment: HorizontalAlignment) -> None
unreal.WidgetSwitcherSlot.set_padding(padding: Margin) -> None
unreal.WidgetSwitcherSlot.set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
unreal.WidgetSwitcherSlot.vertical_alignment(value: VerticalAlignment) -> None
```

## `unreal.Widget_GenerateWidgetForObject(DelegateBase)`

```python
unreal.Widget_GenerateWidgetForObject.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GenerateWidgetForString(DelegateBase)`

```python
unreal.Widget_GenerateWidgetForString.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetBool(DelegateBase)`

```python
unreal.Widget_GetBool.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetCheckBoxState(DelegateBase)`

```python
unreal.Widget_GetCheckBoxState.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetFloat(DelegateBase)`

```python
unreal.Widget_GetFloat.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetInt32(DelegateBase)`

```python
unreal.Widget_GetInt32.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetLinearColor(DelegateBase)`

```python
unreal.Widget_GetLinearColor.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetMouseCursor(DelegateBase)`

```python
unreal.Widget_GetMouseCursor.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetSlateBrush(DelegateBase)`

```python
unreal.Widget_GetSlateBrush.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetSlateColor(DelegateBase)`

```python
unreal.Widget_GetSlateColor.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetSlateVisibility(DelegateBase)`

```python
unreal.Widget_GetSlateVisibility.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetText(DelegateBase)`

```python
unreal.Widget_GetText.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_GetWidget(DelegateBase)`

```python
unreal.Widget_GetWidget.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_OnPointerEvent(DelegateBase)`

```python
unreal.Widget_OnPointerEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.Widget_OnReply(DelegateBase)`

```python
unreal.Widget_OnReply.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WindowAPI(ApiClassBase)`

```python
unreal.WindowAPI.init_covering_screen_layer() -> None
```

## `unreal.WindowEntity(WdpActorEntity)`

```python
unreal.WindowEntity.widget_class() -> Class
unreal.WindowEntity.widget_component() -> CoveringWidgetComponent
```

## `unreal.WindowEntityAtom(EntityAtomBase)`

```python
unreal.WindowEntityAtom.layer_order(value: str) -> None
unreal.WindowEntityAtom.offset(value: Vector2D) -> None
unreal.WindowEntityAtom.set_offset(newoffset: Vector2D) -> bool
unreal.WindowEntityAtom.set_size(newsize: Vector2D) -> bool
unreal.WindowEntityAtom.set_url(newurl: str) -> bool
unreal.WindowEntityAtom.size(value: Vector2D) -> None
unreal.WindowEntityAtom.url(value: str) -> None
```

## `unreal.WindowLoadFinishedEvent(DelegateBase)`

```python
unreal.WindowLoadFinishedEvent.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.WindowStyle(SlateWidgetStyle)`

```python
unreal.WindowStyle.__init__(minimize_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], maximize_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], restore_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], close_button_style: ButtonStyle = [[[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]], title_text_style: TextBlockStyle = [[None, None, [0, False, False, False, None, [0.000000, 0.000000, 0.000000, 1.000000]], "None", 24.000000, 0, 0.000000, False, False, 1.000000], [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000], [[0.000000, 0.000000, 0.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], TextTransformPolicy.NONE, TextOverflowPolicy.CLIP], active_title_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], inactive_title_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], flash_title_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], background_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], outline_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], outline_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], border_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], border_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], child_background_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None, [[0.000000, 0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000, 0.000000], SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000, SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], window_corner_radius: int = 0, border_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.WindowStyle.active_title_brush(value: SlateBrush) -> None
unreal.WindowStyle.background_brush(value: SlateBrush) -> None
unreal.WindowStyle.background_color(value: SlateColor) -> None
unreal.WindowStyle.border_brush(value: SlateBrush) -> None
unreal.WindowStyle.border_color(value: SlateColor) -> None
unreal.WindowStyle.border_padding(value: Margin) -> None
unreal.WindowStyle.child_background_brush(value: SlateBrush) -> None
unreal.WindowStyle.close_button_style(value: ButtonStyle) -> None
unreal.WindowStyle.flash_title_brush(value: SlateBrush) -> None
unreal.WindowStyle.inactive_title_brush(value: SlateBrush) -> None
unreal.WindowStyle.maximize_button_style(value: ButtonStyle) -> None
unreal.WindowStyle.minimize_button_style(value: ButtonStyle) -> None
unreal.WindowStyle.outline_brush(value: SlateBrush) -> None
unreal.WindowStyle.outline_color(value: SlateColor) -> None
unreal.WindowStyle.restore_button_style(value: ButtonStyle) -> None
unreal.WindowStyle.title_text_style(value: TextBlockStyle) -> None
unreal.WindowStyle.window_corner_radius(value: int) -> None
```

## `unreal.WindowTitleBarArea(ContentWidget)`

```python
unreal.WindowTitleBarArea.double_click_toggles_fullscreen(value: bool) -> None
unreal.WindowTitleBarArea.set_horizontal_alignment(horizontal_alignment: HorizontalAlignment) -> None
unreal.WindowTitleBarArea.set_padding(padding: Margin) -> None
unreal.WindowTitleBarArea.set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
unreal.WindowTitleBarArea.window_buttons_enabled(value: bool) -> None
```

## `unreal.WindowTitleBarAreaSlot(PanelSlot)`

```python
unreal.WindowTitleBarAreaSlot.horizontal_alignment(value: HorizontalAlignment) -> None
unreal.WindowTitleBarAreaSlot.padding(value: Margin) -> None
unreal.WindowTitleBarAreaSlot.set_horizontal_alignment(horizontal_alignment: HorizontalAlignment) -> None
unreal.WindowTitleBarAreaSlot.set_padding(padding: Margin) -> None
unreal.WindowTitleBarAreaSlot.set_vertical_alignment(vertical_alignment: VerticalAlignment) -> None
unreal.WindowTitleBarAreaSlot.vertical_alignment(value: VerticalAlignment) -> None
```

## `unreal.WindowWidgetBase(CoveringWidgetBase)`

```python
unreal.WindowWidgetBase.all_hide() -> None
unreal.WindowWidgetBase.create_window(p_widget_component: CoveringWidgetComponent, point: Vector, enity_name: Name, window_entity_atom: WindowEntityAtom) -> bool
unreal.WindowWidgetBase.do_wdp_pick_action(pick: bool) -> None
unreal.WindowWidgetBase.execute_scale_mode(scale_mode: str, location: Vector, threshold: float) -> None
unreal.WindowWidgetBase.notify_button_clicked(select: bool) -> None
unreal.WindowWidgetBase.notify_window_load_finished(sucees: bool) -> None
unreal.WindowWidgetBase.parent_visble2d_atom(value: Visible2DAtom) -> None
unreal.WindowWidgetBase.parent_widget_class(value: Class) -> None
unreal.WindowWidgetBase.parent_widget_component(value: CoveringWidgetComponent) -> None
unreal.WindowWidgetBase.set_offset(new_offset: Vector2D) -> bool
unreal.WindowWidgetBase.set_point(point: Vector) -> bool
unreal.WindowWidgetBase.set_size(new_size: Vector2D) -> bool
unreal.WindowWidgetBase.set_url(new_url: str) -> bool
unreal.WindowWidgetBase.set_visible(value: bool) -> None
unreal.WindowWidgetBase.set_window_entity_actor(p_entity: WindowEntity) -> None
unreal.WindowWidgetBase.show_hide_window(show: bool) -> None
unreal.WindowWidgetBase.visible(value: bool) -> None
unreal.WindowWidgetBase.visible2d_atom(value: Visible2DAtom) -> None
```

