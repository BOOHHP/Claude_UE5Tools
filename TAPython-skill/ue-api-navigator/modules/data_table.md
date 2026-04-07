# Unreal Python API — Data Table

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.CompositeCurveTable(CurveTable)`

```python
unreal.CompositeCurveTable.parent_tables() -> Array[CurveTable]
```

## `unreal.CompositeDataTable(DataTable)`

```python
unreal.CompositeDataTable.parent_tables() -> Array[DataTable]
```

## `unreal.CurveTableRowHandle(StructBase)`

```python
unreal.CurveTableRowHandle.__init__(curve_table: CurveTable = None, row_name: Name = "None") -> None
unreal.CurveTableRowHandle.curve_table(value: CurveTable) -> None
unreal.CurveTableRowHandle.row_name(value: Name) -> None
```

## `unreal.DataTable(Object)`

```python
unreal.DataTable.does_row_exist(row_name: Name) -> bool
unreal.DataTable.export_to_csv_file(csv_file_path: str) -> bool
unreal.DataTable.export_to_csv_string() -> Optional[str]
unreal.DataTable.export_to_json_file(json_file_path: str) -> bool
unreal.DataTable.export_to_json_string() -> Optional[str]
unreal.DataTable.fill_from_csv_file(csv_file_path: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTable.fill_from_csv_string(csv_string: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTable.fill_from_json_file(json_file_path: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTable.fill_from_json_string(json_string: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTable.get_column_as_string(property_name: Name) -> Array[str]
unreal.DataTable.get_column_export_names() -> Array[str]
unreal.DataTable.get_column_name_from_export_name(column_export_name: str) -> Optional[Name]
unreal.DataTable.get_column_names() -> Array[Name]
unreal.DataTable.get_row_names() -> Array[Name]
unreal.DataTable.get_row_struct() -> ScriptStruct
```

## `unreal.DataTableCategoryHandle(StructBase)`

```python
unreal.DataTableCategoryHandle.__init__(data_table: DataTable = None, column_name: Name = "None", row_contents: Name = "None") -> None
unreal.DataTableCategoryHandle.column_name(value: Name) -> None
unreal.DataTableCategoryHandle.data_table(value: DataTable) -> None
unreal.DataTableCategoryHandle.row_contents(value: Name) -> None
```

## `unreal.DataTableFunctionLibrary(BlueprintFunctionLibrary)`

```python
unreal.DataTableFunctionLibrary.does_data_table_row_exist(table: DataTable, row_name: Name) -> bool
unreal.DataTableFunctionLibrary.evaluate_curve_table_row(curve_table: CurveTable, row_name: Name, xy: float, context_string: str) -> Tuple[EvaluateCurveTableResult, float]
unreal.DataTableFunctionLibrary.export_data_table_to_csv_file(data_table: DataTable, csv_file_path: str) -> bool
unreal.DataTableFunctionLibrary.export_data_table_to_csv_string(data_table: DataTable) -> Optional[str]
unreal.DataTableFunctionLibrary.export_data_table_to_json_file(data_table: DataTable, json_file_path: str) -> bool
unreal.DataTableFunctionLibrary.export_data_table_to_json_string(data_table: DataTable) -> Optional[str]
unreal.DataTableFunctionLibrary.fill_data_table_from_csv_file(data_table: DataTable, csv_file_path: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTableFunctionLibrary.fill_data_table_from_csv_string(data_table: DataTable, csv_string: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTableFunctionLibrary.fill_data_table_from_json_file(data_table: DataTable, json_file_path: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTableFunctionLibrary.fill_data_table_from_json_string(data_table: DataTable, json_string: str, import_row_struct: ScriptStruct = None) -> bool
unreal.DataTableFunctionLibrary.get_data_table_column_as_string(data_table: DataTable, property_name: Name) -> Array[str]
unreal.DataTableFunctionLibrary.get_data_table_column_export_names(table: DataTable) -> Array[str]
unreal.DataTableFunctionLibrary.get_data_table_column_name_from_export_name(table: DataTable, column_export_name: str) -> Optional[Name]
unreal.DataTableFunctionLibrary.get_data_table_column_names(table: DataTable) -> Array[Name]
unreal.DataTableFunctionLibrary.get_data_table_row_names(table: DataTable) -> Array[Name]
unreal.DataTableFunctionLibrary.get_data_table_row_struct(table: DataTable) -> ScriptStruct
unreal.DataTableFunctionLibrary.remove_data_table_row(data_table: DataTable, row_name: Name) -> None
```

## `unreal.DataTableRowHandle(StructBase)`

```python
unreal.DataTableRowHandle.__init__(data_table: DataTable = None, row_name: Name = "None") -> None
unreal.DataTableRowHandle.data_table(value: DataTable) -> None
unreal.DataTableRowHandle.row_name(value: Name) -> None
```

## `unreal.InterchangeUserDefinedAttributeInfo(StructBase)`

```python
unreal.InterchangeUserDefinedAttributeInfo.__init__(name: str = "") -> None
unreal.InterchangeUserDefinedAttributeInfo.name(value: str) -> None
```

## `unreal.InterchangeUserDefinedAttributesAPI(Object)`

```python
unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_boolean(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str, value: bool, payload_key: str, requires_delegate: bool = False) -> bool
unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_double(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str, value: float, payload_key: str, requires_delegate: bool = False) -> bool
unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_f_string(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str, value: str, payload_key: str, requires_delegate: bool = False) -> bool
unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_float(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str, value: float, payload_key: str, requires_delegate: bool = False) -> bool
unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_int32(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str, value: int, payload_key: str, requires_delegate: bool = False) -> bool
unreal.InterchangeUserDefinedAttributesAPI.duplicate_all_user_defined_attribute(interchange_source_node: InterchangeBaseNode, interchange_destination_node: InterchangeBaseNode, add_source_node_name: bool) -> None
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_boolean(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> Optional[Tuple[bool, str]]
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_double(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> Optional[Tuple[float, str]]
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_f_string(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> Optional[Tuple[str, str]]
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_float(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> Optional[Tuple[float, str]]
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_infos(interchange_node: InterchangeBaseNode) -> Array[InterchangeUserDefinedAttributeInfo]
unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_int32(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> Optional[Tuple[int, str]]
unreal.InterchangeUserDefinedAttributesAPI.remove_user_defined_attribute(interchange_node: InterchangeBaseNode, user_defined_attribute_name: str) -> bool
```

## `unreal.PCGDataTableRowToParamDataSettings(PCGSettings)`

```python
unreal.PCGDataTableRowToParamDataSettings.data_table(value: DataTable) -> None
unreal.PCGDataTableRowToParamDataSettings.row_name(value: Name) -> None
unreal.PCGDataTableRowToParamDataSettings.synchronous_load(value: bool) -> None
```

## `unreal.PCGLoadDataTableSettings(PCGExternalDataSettings)`

```python
unreal.PCGLoadDataTableSettings.data_table(value: DataTable) -> None
unreal.PCGLoadDataTableSettings.output_type(value: PCGExclusiveDataType) -> None
unreal.PCGLoadDataTableSettings.synchronous_load(value: bool) -> None
```

## `unreal.PythonDataTableLib(BlueprintFunctionLibrary)`

```python
unreal.PythonDataTableLib.add_row(data_table: DataTable, row_name: Name) -> bool
unreal.PythonDataTableLib.duplicate_row(data_table: DataTable, source_row_name: Name, row_name: Name) -> bool
unreal.PythonDataTableLib.get_column_name(data_table: DataTable, column_id: int, friendly_name: bool = True) -> Name
unreal.PythonDataTableLib.get_column_names(data_table: DataTable, friendly_name: bool = True, include_name: bool = False) -> Array[Name]
unreal.PythonDataTableLib.get_data_table_struct(data_table: DataTable) -> ScriptStruct
unreal.PythonDataTableLib.get_data_table_struct_path(data_table: DataTable) -> str
unreal.PythonDataTableLib.get_flatten_data_table(data_table: DataTable, include_header: bool = False) -> Array[str]
unreal.PythonDataTableLib.get_property_as_string(data_table: DataTable, row_name: Name, column_name: Name) -> str
unreal.PythonDataTableLib.get_property_as_string_at(data_table: DataTable, row_id: int, column_id: int) -> str
unreal.PythonDataTableLib.get_row_name(data_table: DataTable, row_id: int) -> Name
unreal.PythonDataTableLib.get_row_names(data_table: DataTable) -> Array[Name]
unreal.PythonDataTableLib.get_shape(data_table: DataTable) -> Array[int]
unreal.PythonDataTableLib.get_table_as_json(data_table: DataTable) -> str
unreal.PythonDataTableLib.move_row(data_table: DataTable, row_name: Name, up: bool, num_rows_to_move_by: int = 1) -> bool
unreal.PythonDataTableLib.remove_row(data_table: DataTable, row_name: Name) -> bool
unreal.PythonDataTableLib.rename_row(data_table: DataTable, old_name: Name, new_name: Name) -> bool
unreal.PythonDataTableLib.reset_row(data_table: DataTable, row_name: Name) -> bool
unreal.PythonDataTableLib.set_property_by_string(data_table: DataTable, row_name: Name, column_name: Name, value_as_string: str) -> bool
unreal.PythonDataTableLib.set_property_by_string_at(data_table: DataTable, row_index: int, column_index: int, value_as_string: str) -> bool
```

## `unreal.RigUnit_UserDefinedEvent(RigVMFunction_UserDefinedEvent)`

```python
unreal.RigUnit_UserDefinedEvent.__init__(execute_context: RigVMExecuteContext = [], event_name: Name = "None") -> None
```

## `unreal.RigVMFunction_UserDefinedEvent(RigVMStruct)`

```python
unreal.RigVMFunction_UserDefinedEvent.__init__(execute_context: RigVMExecuteContext = [], event_name: Name = "None") -> None
unreal.RigVMFunction_UserDefinedEvent.event_name() -> Name
unreal.RigVMFunction_UserDefinedEvent.execute_context() -> RigVMExecuteContext
```

## `unreal.UserDefinedCaptureProtocol(MovieSceneImageCaptureProtocolBase)`

```python
unreal.UserDefinedCaptureProtocol.generate_filename(frame_metrics: FrameMetrics) -> str
unreal.UserDefinedCaptureProtocol.get_current_frame_metrics() -> FrameMetrics
unreal.UserDefinedCaptureProtocol.on_begin_finalize() -> None
unreal.UserDefinedCaptureProtocol.on_can_finalize() -> bool
unreal.UserDefinedCaptureProtocol.on_capture_frame() -> None
unreal.UserDefinedCaptureProtocol.on_finalize() -> None
unreal.UserDefinedCaptureProtocol.on_pause_capture() -> None
unreal.UserDefinedCaptureProtocol.on_pixels_received(pixels: CapturedPixels, id: CapturedPixelsID, frame_metrics: FrameMetrics) -> None
unreal.UserDefinedCaptureProtocol.on_pre_tick() -> None
unreal.UserDefinedCaptureProtocol.on_setup() -> bool
unreal.UserDefinedCaptureProtocol.on_start_capture() -> None
unreal.UserDefinedCaptureProtocol.on_tick() -> None
unreal.UserDefinedCaptureProtocol.on_warm_up() -> None
unreal.UserDefinedCaptureProtocol.resolve_buffer(buffer: Texture, buffer_id: CapturedPixelsID) -> None
unreal.UserDefinedCaptureProtocol.start_capturing_final_pixels(stream_id: CapturedPixelsID) -> None
unreal.UserDefinedCaptureProtocol.stop_capturing_final_pixels() -> None
unreal.UserDefinedCaptureProtocol.world() -> World
```

## `unreal.UserDefinedImageCaptureProtocol(UserDefinedCaptureProtocol)`

```python
unreal.UserDefinedImageCaptureProtocol.compression_quality(value: int) -> None
unreal.UserDefinedImageCaptureProtocol.enable_compression(value: bool) -> None
unreal.UserDefinedImageCaptureProtocol.format(value: DesiredImageFormat) -> None
unreal.UserDefinedImageCaptureProtocol.generate_filename_for_buffer(buffer: Texture, stream_id: CapturedPixelsID) -> str
unreal.UserDefinedImageCaptureProtocol.generate_filename_for_current_frame() -> str
unreal.UserDefinedImageCaptureProtocol.write_image_to_disk(pixel_data: CapturedPixels, stream_id: CapturedPixelsID, frame_metrics: FrameMetrics, copy_image_data: bool = False) -> None
```

