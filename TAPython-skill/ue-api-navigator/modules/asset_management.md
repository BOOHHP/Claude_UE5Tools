# Unreal Python API — Asset Management

> Auto-generated from PythonStub. AI must use these exact signatures for the current UE version.

## `unreal.AesAssetData(TableRowBase)`

```python
unreal.AesAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = []) -> None
unreal.AesAssetData.child_assets(value: Array[AesAssetChildMetaData]) -> None
unreal.AesAssetData.collision_data(value: AesAssetCollisionData) -> None
unreal.AesAssetData.meta_data(value: AesAssetMetaData) -> None
unreal.AesAssetData.size_data(value: AesAssetSizeData) -> None
```

## `unreal.AesAssetDataLibrary(TableRowBase)`

```python
unreal.AesAssetDataLibrary.__init__(type: AesAssetType = AesAssetType.OBJECT, data_table: SoftObjectPath = [""]) -> None
unreal.AesAssetDataLibrary.data_table(value: SoftObjectPath) -> None
unreal.AesAssetDataLibrary.type() -> AesAssetType
```

## `unreal.AesClusterAssetData(AesAssetData)`

```python
unreal.AesClusterAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = []) -> None
```

## `unreal.AesFacadeAssetData(AesAssetData)`

```python
unreal.AesFacadeAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesFacadeAssetTagData = [6000.000000, 0.000000, 1, [255, 255, 255, 255], AesFacadeLayoutType.SINGLE, ["None", 0, 0, "None", False, {}, "", [""]], {}, {}, {}, "", {}, {}]) -> None
unreal.AesFacadeAssetData.tag_data(value: AesFacadeAssetTagData) -> None
```

## `unreal.AesGridLayoutAssetData(AesAssetData)`

```python
unreal.AesGridLayoutAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesGridLayoutAssetTagData = [1200.000000, 150.000000, [0.000000, 0.000000], []]) -> None
unreal.AesGridLayoutAssetData.tag_data(value: AesGridLayoutAssetTagData) -> None
```

## `unreal.AesInstanceSplineAssetData(AesAssetData)`

```python
unreal.AesInstanceSplineAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesInstanceSplineAssetTagData = [False, False, SplinePointType.CURVE, 0.000000, 0.000000, [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [], []], [], [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [], []], False, False, SplineDeformType.CURVE, SplineMeshAxis.X, [0.000000, 0.000000, 0.000000], False, False, AesSplineSizeControlType.SCALE, [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], 0.000000, [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], 0.000000, SplineResampleType.INTERPOLATING, False, SplinePlacementType.CONTINUOUS, 0.000000, 0.000000, SplineAlignmentType.NORMAL, 1.000000, 1.000000, False, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], True, True, False, 0.000000, {"FID": 0.000000}]) -> None
unreal.AesInstanceSplineAssetData.tag_data(value: AesInstanceSplineAssetTagData) -> None
```

## `unreal.AesLandmarkAssetData(AesAssetData)`

```python
unreal.AesLandmarkAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesLandmarkAssetTagData = [[""], "None", 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]) -> None
unreal.AesLandmarkAssetData.tag_data(value: AesLandmarkAssetTagData) -> None
```

## `unreal.AesModularBuildingAssetData(AesAssetData)`

```python
unreal.AesModularBuildingAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesModularBuildingAssetTagData = [300.000000, 0.000000, 600.000000, 1, 0, LandCover.ARTIFICIAL_SURFACES, "None", [255, 255, 255, 255], 0.000000, 0, RoofShape.FLAT, [255, 255, 255, 255], AesBuildingPrefabType.NONE, "", [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], [], [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], [["None", 0, 0, "None", False, {}, "", [""]], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], [], []], [], [], 0.000000]) -> None
unreal.AesModularBuildingAssetData.tag_data(value: AesModularBuildingAssetTagData) -> None
```

## `unreal.AesObjectAssetData(AesAssetData)`

```python
unreal.AesObjectAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesObjectAssetTagData = [[""], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [], {}, {"FID": 0.000000}]) -> None
unreal.AesObjectAssetData.tag_data(value: AesObjectAssetTagData) -> None
```

## `unreal.AesRoadLaneAssetData(AesAssetData)`

```python
unreal.AesRoadLaneAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesRoadLaneAssetTagData = [BuilderType.LANE, False, False, True, True, SplinePointType.CURVE, SplineResampleType.INTERPOLATING, "", DrivingDirection.RIGHT, [1, 1], [1, 1], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], 0, True, False, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000], 0.000000, 0.000000, True, True, False, 0.000000, [], [], [], {}, False, "", [""]]) -> None
unreal.AesRoadLaneAssetData.tag_data(value: AesRoadLaneAssetTagData) -> None
```

## `unreal.AesRoofAssetData(AesAssetData)`

```python
unreal.AesRoofAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data: AesRoofAssetTagData = [RoofShape.FLAT, 0.000000, 1, [255, 255, 255, 255], [[""], -1, 1200.000000], [[""], -1, 1200.000000], 30.000000]) -> None
unreal.AesRoofAssetData.tag_data(value: AesRoofAssetTagData) -> None
```

## `unreal.AesSlotAssetData(AesAssetData)`

```python
unreal.AesSlotAssetData.__init__(meta_data: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]], size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False, []], collision_data: AesAssetCollisionData = [AesAssetCollisionType.NONE, ["/Script/AesRenderResource.AesCollisionComponent"]], child_assets: Array[AesAssetChildMetaData] = [], tag_data_list: Array[AesSlotAssetTagData] = []) -> None
unreal.AesSlotAssetData.tag_data_list(value: Array[AesSlotAssetTagData]) -> None
```

## `unreal.AnimMontageFactory(Factory)`

```python
unreal.AnimMontageFactory.source_animation(value: AnimSequence) -> None
unreal.AnimMontageFactory.target_skeleton(value: Skeleton) -> None
```

## `unreal.AnimSequenceFactory(Factory)`

```python
unreal.AnimSequenceFactory.preview_skeletal_mesh(value: SkeletalMesh) -> None
unreal.AnimSequenceFactory.target_skeleton(value: Skeleton) -> None
```

## `unreal.AssetData(StructBase)`

```python
unreal.AssetData.__init__(package_name: Name = "None", package_path: Name = "None", asset_name: Name = "None", asset_class_path: TopLevelAssetPath = [""]) -> None
unreal.AssetData.asset_class() -> Name
unreal.AssetData.asset_class_path() -> TopLevelAssetPath
unreal.AssetData.asset_name() -> Name
unreal.AssetData.find_asset_native_class() -> Class
unreal.AssetData.get_asset() -> Object
unreal.AssetData.get_class() -> Class
unreal.AssetData.get_export_text_name() -> str
unreal.AssetData.get_full_name() -> str
unreal.AssetData.get_tag_value(tag_name: Name) -> Optional[str]
unreal.AssetData.is_asset_loaded() -> bool
unreal.AssetData.is_redirector() -> bool
unreal.AssetData.is_u_asset() -> bool
unreal.AssetData.is_valid() -> bool
unreal.AssetData.package_name() -> Name
unreal.AssetData.package_path() -> Name
unreal.AssetData.to_soft_object_path() -> SoftObjectPath
```

## `unreal.AssetRegistry(Interface)`

```python
unreal.AssetRegistry.get_all_assets(include_only_on_disk_assets: bool = False) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_all_cached_paths() -> Array[str]
unreal.AssetRegistry.get_ancestor_class_names(class_path_name: TopLevelAssetPath) -> Optional[Array[TopLevelAssetPath]]
unreal.AssetRegistry.get_asset_by_object_path(object_path: Name, include_only_on_disk_assets: bool = False) -> AssetData
unreal.AssetRegistry.get_assets(filter: ARFilter, skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_assets_by_class(class_path_name: TopLevelAssetPath, search_sub_classes: bool = False) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_assets_by_package_name(package_name: Name, include_only_on_disk_assets: bool = False, skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_assets_by_path(package_path: Name, recursive: bool = False, include_only_on_disk_assets: bool = False) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_assets_by_paths(package_paths: Array[Name], recursive: bool = False, include_only_on_disk_assets: bool = False) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_dependencies(package_name: Name, dependency_options: AssetRegistryDependencyOptions) -> Optional[Array[Name]]
unreal.AssetRegistry.get_derived_class_names(class_names: Array[TopLevelAssetPath], excluded_class_names: Set[TopLevelAssetPath]) -> Set[TopLevelAssetPath]
unreal.AssetRegistry.get_in_memory_assets(filter: ARFilter, skip_ar_filtered_assets: bool = True) -> Optional[Array[AssetData]]
unreal.AssetRegistry.get_referencers(package_name: Name, reference_options: AssetRegistryDependencyOptions) -> Optional[Array[Name]]
unreal.AssetRegistry.get_sub_paths(base_path: str, recurse: bool) -> Array[str]
unreal.AssetRegistry.has_assets(package_path: Name, recursive: bool = False) -> bool
unreal.AssetRegistry.is_loading_assets() -> bool
unreal.AssetRegistry.is_search_all_assets() -> bool
unreal.AssetRegistry.is_search_async() -> bool
unreal.AssetRegistry.k2_get_asset_by_object_path(object_path: SoftObjectPath, include_only_on_disk_assets: bool = False, skip_ar_filtered_assets: bool = True) -> AssetData
unreal.AssetRegistry.prioritize_search_path(path_to_prioritize: str) -> None
unreal.AssetRegistry.run_assets_through_filter(asset_data_list: Array[AssetData], filter: ARFilter) -> Array[AssetData]
unreal.AssetRegistry.scan_files_synchronous(file_paths: Array[str], force_rescan: bool = False) -> None
unreal.AssetRegistry.scan_modified_asset_files(file_paths: Array[str]) -> None
unreal.AssetRegistry.scan_paths_synchronous(paths: Array[str], force_rescan: bool = False, ignore_deny_list_scan_filters: bool = False) -> None
unreal.AssetRegistry.search_all_assets(synchronous_search: bool) -> None
unreal.AssetRegistry.use_filter_to_exclude_assets(asset_data_list: Array[AssetData], filter: ARFilter) -> Array[AssetData]
unreal.AssetRegistry.wait_for_completion() -> None
unreal.AssetRegistry.wait_for_package(package_name: str) -> None
```

## `unreal.AssetRegistryDependencyOptions(StructBase)`

```python
unreal.AssetRegistryDependencyOptions.__init__(include_soft_package_references: bool = False, include_hard_package_references: bool = False, include_searchable_names: bool = False, include_soft_management_references: bool = False, include_hard_management_references: bool = False) -> None
unreal.AssetRegistryDependencyOptions.include_hard_management_references(value: bool) -> None
unreal.AssetRegistryDependencyOptions.include_hard_package_references(value: bool) -> None
unreal.AssetRegistryDependencyOptions.include_searchable_names(value: bool) -> None
unreal.AssetRegistryDependencyOptions.include_soft_management_references(value: bool) -> None
unreal.AssetRegistryDependencyOptions.include_soft_package_references(value: bool) -> None
```

## `unreal.AssetRegistryHelpers(Object)`

```python
unreal.AssetRegistryHelpers.create_asset_data(asset: Object, allow_blueprint_class: bool = False) -> AssetData
unreal.AssetRegistryHelpers.find_asset_native_class(asset_data: AssetData) -> Class
unreal.AssetRegistryHelpers.get_asset(asset_data: AssetData) -> Object
unreal.AssetRegistryHelpers.get_asset_registry() -> AssetRegistry
unreal.AssetRegistryHelpers.get_blueprint_assets(filter: ARFilter) -> Array[AssetData]
unreal.AssetRegistryHelpers.get_class(asset_data: AssetData) -> Class
unreal.AssetRegistryHelpers.get_export_text_name(asset_data: AssetData) -> str
unreal.AssetRegistryHelpers.get_full_name(asset_data: AssetData) -> str
unreal.AssetRegistryHelpers.get_tag_value(asset_data: AssetData, tag_name: Name) -> Optional[str]
unreal.AssetRegistryHelpers.is_asset_loaded(asset_data: AssetData) -> bool
unreal.AssetRegistryHelpers.is_redirector(asset_data: AssetData) -> bool
unreal.AssetRegistryHelpers.is_u_asset(asset_data: AssetData) -> bool
unreal.AssetRegistryHelpers.is_valid(asset_data: AssetData) -> bool
unreal.AssetRegistryHelpers.set_filter_tags_and_values(filter: ARFilter, tags_and_values: Array[TagAndValue]) -> ARFilter
unreal.AssetRegistryHelpers.sort_by_asset_name(assets: Array[AssetData], sort_order: AssetRegistrySortOrder) -> Array[AssetData]
unreal.AssetRegistryHelpers.sort_by_predicate(assets: Array[AssetData], sorting_predicate: SortingPredicate, sort_order: AssetRegistrySortOrder) -> Array[AssetData]
unreal.AssetRegistryHelpers.to_soft_object_path(asset_data: AssetData) -> SoftObjectPath
```

## `unreal.AssetRegistryHelpers_SortingPredicate(DelegateBase)`

```python
unreal.AssetRegistryHelpers_SortingPredicate.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.AssetTools(Interface)`

```python
unreal.AssetTools.begin_advanced_copy_packages(input_names_to_copy: Array[Name], target_path: str, on_copy_complete: AdvancedCopyCompletedEvent) -> None
unreal.AssetTools.create_asset(asset_name: str, package_path: str, asset_class: Class, factory: Factory, calling_context: Name = "None") -> Object
unreal.AssetTools.create_asset_with_dialog(asset_name: str, package_path: str, asset_class: Class, factory: Factory, calling_context: Name = "None", call_configure_properties: bool = True) -> Object
unreal.AssetTools.create_unique_asset_name(base_package_name: str, suffix: str) -> Tuple[str, str]
unreal.AssetTools.diff_against_depot(object: Object, package_path: str, package_name: str) -> None
unreal.AssetTools.diff_assets(old_asset: Object, new_asset: Object, old_revision: RevisionInfo, new_revision: RevisionInfo) -> None
unreal.AssetTools.duplicate_asset(asset_name: str, package_path: str, original_object: Object) -> Object
unreal.AssetTools.duplicate_asset_with_dialog(asset_name: str, package_path: str, original_object: Object) -> Object
unreal.AssetTools.duplicate_asset_with_dialog_and_title(asset_name: str, package_path: str, original_object: Object, dialog_title: Text) -> Object
unreal.AssetTools.export_assets(assets_to_export: Array[str], export_path: str) -> None
unreal.AssetTools.export_assets_with_dialog(assets_to_export: Array[str], prompt_for_individual_filenames: bool) -> None
unreal.AssetTools.find_soft_references_to_object(target_object: SoftObjectPath) -> Array[Object]
unreal.AssetTools.import_asset_tasks(import_tasks: Array[AssetImportTask]) -> None
unreal.AssetTools.import_assets_automated(import_data: AutomatedAssetImportData) -> Array[Object]
unreal.AssetTools.import_assets_with_dialog(destination_path: str) -> Array[Object]
unreal.AssetTools.migrate_packages(package_names_to_migrate: Array[Name], destination_path: str, options: MigrationOptions = [False, False, AssetMigrationConflict.SKIP, ""]) -> None
unreal.AssetTools.open_editor_for_assets(assets: Array[Object]) -> None
unreal.AssetTools.rename_assets(assets_and_names: Array[AssetRenameData]) -> bool
unreal.AssetTools.rename_assets_with_dialog(assets_and_names: Array[AssetRenameData], auto_checkout: bool = False) -> AssetRenameResult
unreal.AssetTools.rename_referencing_soft_object_paths(packages_to_check: Array[Package], asset_redirector_map: Map[SoftObjectPath, SoftObjectPath]) -> None
```

## `unreal.AssetToolsHelpers(Object)`

```python
unreal.AssetToolsHelpers.get_asset_tools() -> AssetTools
```

## `unreal.BlendSpaceFactory1D(Factory)`

```python
unreal.BlendSpaceFactory1D.preview_skeletal_mesh(value: SkeletalMesh) -> None
unreal.BlendSpaceFactory1D.target_skeleton(value: Skeleton) -> None
```

## `unreal.BlendSpaceFactoryNew(Factory)`

```python
unreal.BlendSpaceFactoryNew.preview_skeletal_mesh(value: SkeletalMesh) -> None
unreal.BlendSpaceFactoryNew.target_skeleton(value: Skeleton) -> None
```

## `unreal.CSVImportFactory(Factory)`

```python
unreal.CSVImportFactory.automated_import_settings(value: CSVImportSettings) -> None
```

## `unreal.ContentBrowserAssetContextMenuContext(Object)`

```python
unreal.ContentBrowserAssetContextMenuContext.contains_unsupported_assets() -> bool
unreal.ContentBrowserAssetContextMenuContext.get_selected_objects() -> Array[Object]
unreal.ContentBrowserAssetContextMenuContext.load_selected_objects(load_tags: Set[Name]) -> Array[Object]
unreal.ContentBrowserAssetContextMenuContext.load_selected_objects_if_needed() -> Array[Object]
unreal.ContentBrowserAssetContextMenuContext.selected_assets() -> Array[AssetData]
```

## `unreal.ContentBrowserDataClassFilter(StructBase)`

```python
unreal.ContentBrowserDataClassFilter.__init__(class_names_to_include: Array[str] = [], class_names_to_exclude: Array[str] = [], recursive_class_names_to_include: bool = False, recursive_class_names_to_exclude: bool = False) -> None
unreal.ContentBrowserDataClassFilter.class_names_to_exclude(value: Array[str]) -> None
unreal.ContentBrowserDataClassFilter.class_names_to_include(value: Array[str]) -> None
unreal.ContentBrowserDataClassFilter.recursive_class_names_to_exclude(value: bool) -> None
unreal.ContentBrowserDataClassFilter.recursive_class_names_to_include(value: bool) -> None
```

## `unreal.ContentBrowserDataCollectionFilter(StructBase)`

```python
unreal.ContentBrowserDataCollectionFilter.__init__(include_child_collections: bool = False) -> None
unreal.ContentBrowserDataCollectionFilter.include_child_collections(value: bool) -> None
```

## `unreal.ContentBrowserDataFilter(StructBase)`

```python
unreal.ContentBrowserDataFilter.__init__(recursive_paths: bool = False, item_type_filter: ContentBrowserItemTypeFilter = ContentBrowserItemTypeFilter.INCLUDE_NONE, item_category_filter: ContentBrowserItemCategoryFilter = ContentBrowserItemCategoryFilter.INCLUDE_NONE, item_attribute_filter: ContentBrowserItemAttributeFilter = ContentBrowserItemAttributeFilter.INCLUDE_NONE) -> None
unreal.ContentBrowserDataFilter.item_attribute_filter(value: ContentBrowserItemAttributeFilter) -> None
unreal.ContentBrowserDataFilter.item_category_filter(value: ContentBrowserItemCategoryFilter) -> None
unreal.ContentBrowserDataFilter.item_type_filter(value: ContentBrowserItemTypeFilter) -> None
unreal.ContentBrowserDataFilter.recursive_paths(value: bool) -> None
```

## `unreal.ContentBrowserDataMenuContext_AddNewMenu(Object)`

```python
unreal.ContentBrowserDataMenuContext_AddNewMenu.can_be_modified() -> bool
unreal.ContentBrowserDataMenuContext_AddNewMenu.contains_valid_package_path() -> bool
unreal.ContentBrowserDataMenuContext_AddNewMenu.owner_domain() -> ContentBrowserDataMenuContext_AddNewMenuDomain
unreal.ContentBrowserDataMenuContext_AddNewMenu.selected_paths() -> Array[Name]
```

## `unreal.ContentBrowserDataMenuContext_DragDropMenu(Object)`

```python
unreal.ContentBrowserDataMenuContext_DragDropMenu.can_copy() -> bool
unreal.ContentBrowserDataMenuContext_DragDropMenu.can_move() -> bool
unreal.ContentBrowserDataMenuContext_DragDropMenu.dragged_items() -> Array[ContentBrowserItem]
unreal.ContentBrowserDataMenuContext_DragDropMenu.drop_target_item() -> ContentBrowserItem
```

## `unreal.ContentBrowserDataMenuContext_FileMenu(Object)`

```python
unreal.ContentBrowserDataMenuContext_FileMenu.can_be_modified() -> bool
unreal.ContentBrowserDataMenuContext_FileMenu.can_view() -> bool
unreal.ContentBrowserDataMenuContext_FileMenu.contains_unsupported_assets() -> bool
unreal.ContentBrowserDataMenuContext_FileMenu.has_cooked_packages() -> bool
unreal.ContentBrowserDataMenuContext_FileMenu.selected_items() -> Array[ContentBrowserItem]
```

## `unreal.ContentBrowserDataMenuContext_FolderMenu(Object)`

```python
unreal.ContentBrowserDataMenuContext_FolderMenu.can_be_modified() -> bool
unreal.ContentBrowserDataMenuContext_FolderMenu.selected_items() -> Array[ContentBrowserItem]
```

## `unreal.ContentBrowserDataObjectFilter(StructBase)`

```python
unreal.ContentBrowserDataObjectFilter.__init__(object_names_to_include: Array[Name] = [], object_names_to_exclude: Array[Name] = [], on_disk_objects_only: bool = False) -> None
unreal.ContentBrowserDataObjectFilter.object_names_to_exclude(value: Array[Name]) -> None
unreal.ContentBrowserDataObjectFilter.object_names_to_include(value: Array[Name]) -> None
unreal.ContentBrowserDataObjectFilter.on_disk_objects_only(value: bool) -> None
```

## `unreal.ContentBrowserDataPackageFilter(StructBase)`

```python
unreal.ContentBrowserDataPackageFilter.__init__(package_names_to_include: Array[Name] = [], package_names_to_exclude: Array[Name] = [], package_paths_to_include: Array[Name] = [], package_paths_to_exclude: Array[Name] = [], recursive_package_paths_to_include: bool = False, recursive_package_paths_to_exclude: bool = False) -> None
unreal.ContentBrowserDataPackageFilter.package_names_to_exclude(value: Array[Name]) -> None
unreal.ContentBrowserDataPackageFilter.package_names_to_include(value: Array[Name]) -> None
unreal.ContentBrowserDataPackageFilter.package_paths_to_exclude(value: Array[Name]) -> None
unreal.ContentBrowserDataPackageFilter.package_paths_to_include(value: Array[Name]) -> None
unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_exclude(value: bool) -> None
unreal.ContentBrowserDataPackageFilter.recursive_package_paths_to_include(value: bool) -> None
```

## `unreal.ContentBrowserDataSubsystem(EditorSubsystem)`

```python
unreal.ContentBrowserDataSubsystem.activate_all_data_sources() -> None
unreal.ContentBrowserDataSubsystem.activate_data_source(name: Name) -> bool
unreal.ContentBrowserDataSubsystem.deactivate_all_data_sources() -> None
unreal.ContentBrowserDataSubsystem.deactivate_data_source(name: Name) -> bool
unreal.ContentBrowserDataSubsystem.get_active_data_sources() -> Array[Name]
unreal.ContentBrowserDataSubsystem.get_available_data_sources() -> Array[Name]
unreal.ContentBrowserDataSubsystem.get_item_at_path(path: Name, item_type_filter: ContentBrowserItemTypeFilter) -> ContentBrowserItem
unreal.ContentBrowserDataSubsystem.get_items_at_path(path: Name, item_type_filter: ContentBrowserItemTypeFilter) -> Array[ContentBrowserItem]
unreal.ContentBrowserDataSubsystem.get_items_under_path(path: Name, filter: ContentBrowserDataFilter) -> Array[ContentBrowserItem]
```

## `unreal.ContentBrowserFolderContentsFilter(StructBase)`

```python
unreal.ContentBrowserFolderContentsFilter.__init__(item_type_filter: ContentBrowserItemTypeFilter = ContentBrowserItemTypeFilter.INCLUDE_NONE, item_category_filter: ContentBrowserItemCategoryFilter = ContentBrowserItemCategoryFilter.INCLUDE_NONE, item_attribute_filter: ContentBrowserItemAttributeFilter = ContentBrowserItemAttributeFilter.INCLUDE_NONE) -> None
unreal.ContentBrowserFolderContentsFilter.item_attribute_filter(value: ContentBrowserItemAttributeFilter) -> None
unreal.ContentBrowserFolderContentsFilter.item_category_filter(value: ContentBrowserItemCategoryFilter) -> None
unreal.ContentBrowserFolderContentsFilter.item_type_filter(value: ContentBrowserItemTypeFilter) -> None
```

## `unreal.ContentBrowserFolderContext(ContentBrowserMenuContext)`

```python
unreal.ContentBrowserFolderContext.can_be_modified() -> bool
unreal.ContentBrowserFolderContext.no_folder_on_disk() -> bool
unreal.ContentBrowserFolderContext.num_asset_paths() -> int
unreal.ContentBrowserFolderContext.num_class_paths() -> int
unreal.ContentBrowserFolderContext.selected_package_paths() -> Array[str]
```

## `unreal.ContentBrowserItem(StructBase)`

```python
unreal.ContentBrowserItem.__init__() -> None
unreal.ContentBrowserItem.get_display_name() -> Text
unreal.ContentBrowserItem.get_virtual_path() -> Name
unreal.ContentBrowserItem.is_file() -> bool
unreal.ContentBrowserItem.is_folder() -> bool
```

## `unreal.ContentBrowserItemLibrary(BlueprintFunctionLibrary)`

```python
unreal.ContentBrowserItemLibrary.get_display_name(item: ContentBrowserItem) -> Text
unreal.ContentBrowserItemLibrary.get_virtual_path(item: ContentBrowserItem) -> Name
unreal.ContentBrowserItemLibrary.is_file(item: ContentBrowserItem) -> bool
unreal.ContentBrowserItemLibrary.is_folder(item: ContentBrowserItem) -> bool
```

## `unreal.ContentBrowserItemPath(StructBase)`

```python
unreal.ContentBrowserItemPath.__init__(path: Name = "None", path_type: ContentBrowserPathType = ContentBrowserPathType.NONE) -> None
unreal.ContentBrowserItemPath.get_internal_path() -> Name
unreal.ContentBrowserItemPath.get_virtual_path() -> Name
unreal.ContentBrowserItemPath.set_path(path: Name, path_type: ContentBrowserPathType) -> None
```

## `unreal.ContentBrowserItemPathExtensions(BlueprintFunctionLibrary)`

```python
unreal.ContentBrowserItemPathExtensions.get_internal_path(item_path: ContentBrowserItemPath) -> Name
unreal.ContentBrowserItemPathExtensions.get_virtual_path(item_path: ContentBrowserItemPath) -> Name
unreal.ContentBrowserItemPathExtensions.set_path(item_path: ContentBrowserItemPath, path: Name, path_type: ContentBrowserPathType) -> ContentBrowserItemPath
```

## `unreal.ControlRigBlueprintFactory(Factory)`

```python
unreal.ControlRigBlueprintFactory.create_control_rig_from_skeletal_mesh_or_skeleton(selected_object: Object, modular_rig: bool = False) -> ControlRigBlueprint
unreal.ControlRigBlueprintFactory.create_new_control_rig_asset(desired_package_path: str, modular_rig: bool = False) -> ControlRigBlueprint
```

## `unreal.DataTableFactory(Factory)`

```python
unreal.DataTableFactory.struct(value: ScriptStruct) -> None
```

## `unreal.EditorAssetLibrary(BlueprintFunctionLibrary)`

```python
unreal.EditorAssetLibrary.checkout_asset(asset_to_checkout: str) -> bool
unreal.EditorAssetLibrary.checkout_directory(directory_path: str, recursive: bool = True) -> bool
unreal.EditorAssetLibrary.checkout_loaded_asset(asset_to_checkout: Object) -> bool
unreal.EditorAssetLibrary.checkout_loaded_assets(assets_to_checkout: Array[Object]) -> bool
unreal.EditorAssetLibrary.consolidate_assets(asset_to_consolidate_to: Object, assets_to_consolidate: Array[Object]) -> bool
unreal.EditorAssetLibrary.delete_asset(asset_path_to_delete: str) -> bool
unreal.EditorAssetLibrary.delete_directory(directory_path: str) -> bool
unreal.EditorAssetLibrary.delete_loaded_asset(asset_to_delete: Object) -> bool
unreal.EditorAssetLibrary.delete_loaded_assets(assets_to_delete: Array[Object]) -> bool
unreal.EditorAssetLibrary.do_assets_exist(asset_paths: Array[str]) -> bool
unreal.EditorAssetLibrary.does_asset_exist(asset_path: str) -> bool
unreal.EditorAssetLibrary.does_directory_exist(directory_path: str) -> bool
unreal.EditorAssetLibrary.does_directory_have_assets(directory_path: str, recursive: bool = True) -> bool
unreal.EditorAssetLibrary.duplicate_asset(source_asset_path: str, destination_asset_path: str) -> Object
unreal.EditorAssetLibrary.duplicate_directory(source_directory_path: str, destination_directory_path: str) -> bool
unreal.EditorAssetLibrary.duplicate_loaded_asset(source_asset: Object, destination_asset_path: str) -> Object
unreal.EditorAssetLibrary.find_asset_data(asset_path: str) -> AssetData
unreal.EditorAssetLibrary.find_package_referencers_for_asset(asset_path: str, load_assets_to_confirm: bool = False) -> Array[str]
unreal.EditorAssetLibrary.get_metadata_tag(object: Object, tag: Name) -> str
unreal.EditorAssetLibrary.get_metadata_tag_values(object: Object) -> Map[Name, str]
unreal.EditorAssetLibrary.get_package_for_object(object: Object) -> Package
unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(loaded_asset: Object) -> str
unreal.EditorAssetLibrary.get_project_root_asset_directory() -> str
unreal.EditorAssetLibrary.get_tag_values(asset_path: str) -> Map[Name, str]
unreal.EditorAssetLibrary.list_asset_by_tag_value(tag_name: Name, tag_value: str) -> Array[str]
unreal.EditorAssetLibrary.list_assets(directory_path: str, recursive: bool = True, include_folder: bool = False) -> Array[str]
unreal.EditorAssetLibrary.load_asset(asset_path: str) -> Object
unreal.EditorAssetLibrary.load_blueprint_class(asset_path: str) -> Class
unreal.EditorAssetLibrary.make_directory(directory_path: str) -> bool
unreal.EditorAssetLibrary.remove_metadata_tag(object: Object, tag: Name) -> None
unreal.EditorAssetLibrary.rename_asset(source_asset_path: str, destination_asset_path: str) -> bool
unreal.EditorAssetLibrary.rename_directory(source_directory_path: str, destination_directory_path: str) -> bool
unreal.EditorAssetLibrary.rename_loaded_asset(source_asset: Object, destination_asset_path: str) -> bool
unreal.EditorAssetLibrary.save_asset(asset_to_save: str, only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetLibrary.save_directory(directory_path: str, only_if_is_dirty: bool = True, recursive: bool = True) -> bool
unreal.EditorAssetLibrary.save_loaded_asset(asset_to_save: Object, only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetLibrary.save_loaded_assets(assets_to_save: Array[Object], only_if_is_dirty: bool = True) -> bool
unreal.EditorAssetLibrary.set_metadata_tag(object: Object, tag: Name, value: str) -> None
unreal.EditorAssetLibrary.sync_browser_to_objects(asset_paths: Array[str]) -> None
```

## `unreal.Factory(Object)`

```python
unreal.Factory.asset_import_task(value: AssetImportTask) -> None
unreal.Factory.automated_import_data(value: AutomatedAssetImportData) -> None
unreal.Factory.context_class(value: Class) -> None
unreal.Factory.create_new(value: bool) -> None
unreal.Factory.edit_after_new(value: bool) -> None
unreal.Factory.editor_import(value: bool) -> None
unreal.Factory.formats(value: Array[str]) -> None
unreal.Factory.script_factory_can_import(filename: str) -> bool
unreal.Factory.script_factory_create_file(task: AssetImportTask) -> bool
unreal.Factory.supported_class(value: Class) -> None
unreal.Factory.text(value: bool) -> None
```

## `unreal.FbxSceneImportFactory(SceneImportFactory)`

```python
unreal.FbxSceneImportFactory.scene_import_options(value: FbxSceneImportOptions) -> None
unreal.FbxSceneImportFactory.scene_import_options_skeletal_mesh(value: FbxSceneImportOptionsSkeletalMesh) -> None
unreal.FbxSceneImportFactory.scene_import_options_static_mesh(value: FbxSceneImportOptionsStaticMesh) -> None
```

## `unreal.InterchangeActorFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeActorFactoryNode.get_custom_actor_class_name() -> Optional[str]
unreal.InterchangeActorFactoryNode.get_custom_global_transform() -> Optional[Transform]
unreal.InterchangeActorFactoryNode.get_custom_local_transform() -> Optional[Transform]
unreal.InterchangeActorFactoryNode.get_custom_mobility() -> Optional[int]
unreal.InterchangeActorFactoryNode.set_custom_actor_class_name(attribute_value: str) -> bool
unreal.InterchangeActorFactoryNode.set_custom_global_transform(attribute_value: Transform, add_apply_delegate: bool = True) -> bool
unreal.InterchangeActorFactoryNode.set_custom_local_transform(attribute_value: Transform, add_apply_delegate: bool = True) -> bool
unreal.InterchangeActorFactoryNode.set_custom_mobility(attribute_value: int, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeAnimSequenceFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_name(index: int) -> str
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_names() -> Array[str]
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_names_count() -> int
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_name(index: int) -> str
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_names() -> Array[str]
unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_names_count() -> int
unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixe(index: int) -> str
unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixes() -> Array[str]
unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixes_count() -> int
unreal.InterchangeAnimSequenceFactoryNode.get_custom_add_curve_metadata_to_skeleton() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_custom_attribute_curves() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_morph_target_curves() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_non_curve_custom_attributes() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_do_not_import_curve_with_zero() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_attribute_curves() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_range_start() -> Optional[float]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_range_stop() -> Optional[float]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_sample_rate() -> Optional[float]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_material_drive_parameter_on_custom_attribute() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_remove_curve_redundant_keys() -> Optional[bool]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_skeleton_factory_node_uid() -> Optional[str]
unreal.InterchangeAnimSequenceFactoryNode.get_custom_skeleton_soft_object_path() -> Optional[SoftObjectPath]
unreal.InterchangeAnimSequenceFactoryNode.get_morph_target_node_animation_payload_keys() -> Map[str, InterchangeAnimationPayLoadKey]
unreal.InterchangeAnimSequenceFactoryNode.get_object_class() -> Class
unreal.InterchangeAnimSequenceFactoryNode.get_scene_node_animation_payload_keys() -> Map[str, InterchangeAnimationPayLoadKey]
unreal.InterchangeAnimSequenceFactoryNode.initialize_anim_sequence_node(unique_id: str, display_label: str) -> None
unreal.InterchangeAnimSequenceFactoryNode.remove_animated_attribute_curve_name(attribute_curve_name: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.remove_animated_attribute_step_curve_name(attribute_step_curve_name: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.remove_animated_material_curve_suffixe(material_curve_suffixe: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_animated_attribute_curve_name(attribute_curve_name: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_animated_attribute_step_curve_name(attribute_step_curve_name: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_animated_material_curve_suffixe(material_curve_suffixe: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_animation_payload_keys_for_morph_target_node_uids(morph_target_animation_payload_key_uids: Map[str, str], morph_target_animation_payload_key_types: Map[str, int]) -> None
unreal.InterchangeAnimSequenceFactoryNode.set_animation_payload_keys_for_scene_node_uids(scene_node_animation_payload_key_uids: Map[str, str], scene_node_animation_payload_key_types: Map[str, int]) -> None
unreal.InterchangeAnimSequenceFactoryNode.set_custom_add_curve_metadata_to_skeleton(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_custom_attribute_curves(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_morph_target_curves(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_non_curve_custom_attributes(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_do_not_import_curve_with_zero(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_attribute_curves(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_range_start(attribute_value: float) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_range_stop(attribute_value: float) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_sample_rate(attribute_value: float) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_material_drive_parameter_on_custom_attribute(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_remove_curve_redundant_keys(attribute_value: bool) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_skeleton_factory_node_uid(attribute_value: str) -> bool
unreal.InterchangeAnimSequenceFactoryNode.set_custom_skeleton_soft_object_path(attribute_value: SoftObjectPath) -> bool
```

## `unreal.InterchangeBaseLightFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangeBaseLightFactoryNode.get_custom_intensity() -> Optional[float]
unreal.InterchangeBaseLightFactoryNode.get_custom_light_color() -> Optional[Color]
unreal.InterchangeBaseLightFactoryNode.get_custom_temperature() -> Optional[float]
unreal.InterchangeBaseLightFactoryNode.get_custom_use_temperature() -> Optional[bool]
unreal.InterchangeBaseLightFactoryNode.set_custom_intensity(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeBaseLightFactoryNode.set_custom_light_color(attribute_value: Color, add_apply_delegate: bool = True) -> bool
unreal.InterchangeBaseLightFactoryNode.set_custom_temperature(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeBaseLightFactoryNode.set_custom_use_temperature(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeBaseMaterialFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeBaseMaterialFactoryNode.get_custom_is_material_import_enabled() -> Optional[bool]
unreal.InterchangeBaseMaterialFactoryNode.set_custom_is_material_import_enabled(attribute_value: bool) -> bool
```

## `unreal.InterchangeCommonPipelineDataFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeCommonPipelineDataFactoryNode.get_bake_meshes() -> Optional[bool]
unreal.InterchangeCommonPipelineDataFactoryNode.get_bake_pivot_meshes() -> Optional[bool]
unreal.InterchangeCommonPipelineDataFactoryNode.get_custom_global_offset_transform() -> Optional[Transform]
unreal.InterchangeCommonPipelineDataFactoryNode.set_bake_meshes(attribute_value: bool) -> bool
unreal.InterchangeCommonPipelineDataFactoryNode.set_bake_pivot_meshes(attribute_value: bool) -> bool
unreal.InterchangeCommonPipelineDataFactoryNode.set_custom_global_offset_transform(node_container: InterchangeBaseNodeContainer, attribute_value: Transform) -> bool
```

## `unreal.InterchangeDecalActorFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangeDecalActorFactoryNode.get_custom_decal_material_path_name() -> Optional[str]
unreal.InterchangeDecalActorFactoryNode.get_custom_decal_size() -> Optional[Vector]
unreal.InterchangeDecalActorFactoryNode.get_custom_sort_order() -> Optional[int]
unreal.InterchangeDecalActorFactoryNode.get_object_class() -> Class
unreal.InterchangeDecalActorFactoryNode.set_custom_decal_material_path_name(attribute_value: str) -> bool
unreal.InterchangeDecalActorFactoryNode.set_custom_decal_size(attribute_value: Vector, add_apply_delegate: bool = True) -> bool
unreal.InterchangeDecalActorFactoryNode.set_custom_sort_order(attribute_value: int, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeDecalMaterialFactoryNode(InterchangeBaseMaterialFactoryNode)`

```python
unreal.InterchangeDecalMaterialFactoryNode.get_custom_diffuse_texture_path() -> Optional[str]
unreal.InterchangeDecalMaterialFactoryNode.get_custom_normal_texture_path() -> Optional[str]
unreal.InterchangeDecalMaterialFactoryNode.get_object_class() -> Class
unreal.InterchangeDecalMaterialFactoryNode.set_custom_diffuse_texture_path(attribute_value: str) -> bool
unreal.InterchangeDecalMaterialFactoryNode.set_custom_normal_texture_path(attribute_value: str) -> bool
```

## `unreal.InterchangeFactoryBase(Object)`

```python
unreal.InterchangeFactoryBase.get_factory_class() -> Class
```

## `unreal.InterchangeFactoryBaseNode(InterchangeBaseNode)`

```python
unreal.InterchangeFactoryBaseNode.add_factory_dependency_uid(dependency_uid: str) -> bool
unreal.InterchangeFactoryBaseNode.get_custom_level_uid() -> Optional[str]
unreal.InterchangeFactoryBaseNode.get_custom_reference_object() -> Optional[SoftObjectPath]
unreal.InterchangeFactoryBaseNode.get_custom_sub_path() -> Optional[str]
unreal.InterchangeFactoryBaseNode.get_factory_dependencies() -> Array[str]
unreal.InterchangeFactoryBaseNode.get_factory_dependencies_count() -> int
unreal.InterchangeFactoryBaseNode.get_factory_dependency(index: int) -> str
unreal.InterchangeFactoryBaseNode.get_reimport_strategy_flags() -> ReimportStrategyFlags
unreal.InterchangeFactoryBaseNode.is_runtime_import_allowed() -> bool
unreal.InterchangeFactoryBaseNode.remove_factory_dependency_uid(dependency_uid: str) -> bool
unreal.InterchangeFactoryBaseNode.set_custom_level_uid(attribute_value: str) -> bool
unreal.InterchangeFactoryBaseNode.set_custom_reference_object(attribute_value: SoftObjectPath) -> bool
unreal.InterchangeFactoryBaseNode.set_custom_sub_path(attribute_value: str) -> bool
unreal.InterchangeFactoryBaseNode.set_force_node_reimport() -> bool
unreal.InterchangeFactoryBaseNode.set_reimport_strategy_flags(reimport_strategy_flags: ReimportStrategyFlags) -> bool
unreal.InterchangeFactoryBaseNode.set_skip_node_import() -> bool
unreal.InterchangeFactoryBaseNode.should_force_node_reimport() -> bool
unreal.InterchangeFactoryBaseNode.should_skip_node_import() -> bool
unreal.InterchangeFactoryBaseNode.unset_force_node_reimport() -> bool
unreal.InterchangeFactoryBaseNode.unset_skip_node_import() -> bool
```

## `unreal.InterchangeLevelFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeLevelFactoryNode.add_custom_actor_factory_node_uid(actor_factory_node_uid: str) -> bool
unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uid(index: int) -> str
unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uid_count() -> int
unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uids() -> Array[str]
unreal.InterchangeLevelFactoryNode.get_custom_create_world_partition_level() -> Optional[bool]
unreal.InterchangeLevelFactoryNode.get_custom_scene_import_asset_factory_node_uid() -> Optional[str]
unreal.InterchangeLevelFactoryNode.get_custom_should_create_level() -> Optional[bool]
unreal.InterchangeLevelFactoryNode.get_object_class() -> Class
unreal.InterchangeLevelFactoryNode.remove_custom_actor_factory_node_uid(actor_factory_node_uid: str) -> bool
unreal.InterchangeLevelFactoryNode.set_custom_create_world_partition_level(attribute_value: bool) -> bool
unreal.InterchangeLevelFactoryNode.set_custom_scene_import_asset_factory_node_uid(attribute_value: str) -> bool
unreal.InterchangeLevelFactoryNode.set_custom_should_create_level(attribute_value: bool) -> bool
```

## `unreal.InterchangeLevelInstanceActorFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangeLevelInstanceActorFactoryNode.get_custom_level_reference() -> Optional[str]
unreal.InterchangeLevelInstanceActorFactoryNode.set_custom_level_reference(attribute_value: str) -> bool
```

## `unreal.InterchangeLevelSequenceFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeLevelSequenceFactoryNode.add_custom_animation_track_uid(animation_track_uid: str) -> bool
unreal.InterchangeLevelSequenceFactoryNode.get_custom_animation_track_uid(index: int) -> str
unreal.InterchangeLevelSequenceFactoryNode.get_custom_animation_track_uid_count() -> int
unreal.InterchangeLevelSequenceFactoryNode.get_custom_animation_track_uids() -> Array[str]
unreal.InterchangeLevelSequenceFactoryNode.get_custom_frame_rate() -> Optional[float]
unreal.InterchangeLevelSequenceFactoryNode.get_object_class() -> Class
unreal.InterchangeLevelSequenceFactoryNode.remove_custom_animation_track_uid(animation_track_uid: str) -> bool
unreal.InterchangeLevelSequenceFactoryNode.set_custom_frame_rate(attribute_value: float) -> bool
```

## `unreal.InterchangeLightFactoryNode(InterchangeBaseLightFactoryNode)`

```python
unreal.InterchangeLightFactoryNode.get_custom_attenuation_radius() -> Optional[float]
unreal.InterchangeLightFactoryNode.get_custom_ies_brightness_scale() -> Optional[float]
unreal.InterchangeLightFactoryNode.get_custom_ies_texture() -> Optional[str]
unreal.InterchangeLightFactoryNode.get_custom_intensity_units() -> Optional[LightUnits]
unreal.InterchangeLightFactoryNode.get_custom_rotation() -> Optional[Rotator]
unreal.InterchangeLightFactoryNode.get_custom_use_ies_brightness() -> Optional[bool]
unreal.InterchangeLightFactoryNode.set_custom_attenuation_radius(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightFactoryNode.set_custom_ies_brightness_scale(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightFactoryNode.set_custom_ies_texture(attribute_value: str) -> bool
unreal.InterchangeLightFactoryNode.set_custom_intensity_units(attribute_value: LightUnits, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightFactoryNode.set_custom_rotation(attribute_value: Rotator, add_apply_delegate: bool = True) -> bool
unreal.InterchangeLightFactoryNode.set_custom_use_ies_brightness(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeMaterialExpressionFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeMaterialExpressionFactoryNode.get_custom_expression_class_name() -> Optional[str]
unreal.InterchangeMaterialExpressionFactoryNode.set_custom_expression_class_name(attribute_value: str) -> bool
```

## `unreal.InterchangeMaterialFactoryNode(InterchangeBaseMaterialFactoryNode)`

```python
unreal.InterchangeMaterialFactoryNode.connect_output_to_anisotropy(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_base_color(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat_normal(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat_roughness(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_cloth(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_displacement(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_emissive_color(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_fuzz_color(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_metallic(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_normal(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_occlusion(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_opacity(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_refraction(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_roughness(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_specular(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_subsurface(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_surface_coverage(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_tangent(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_output_to_transmission_color(expression_node_uid: str, output_name: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_anisotropy(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_base_color(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat_normal(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat_roughness(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_cloth(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_displacement(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_emissive_color(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_fuzz_color(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_metallic(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_normal(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_occlusion(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_opacity(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_refraction(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_roughness(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_specular(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_subsurface(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_surface_coverage(expression_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_tangent(expression_node_uid: str) -> bool
unreal.InterchangeMaterialFactoryNode.connect_to_transmission_color(attribute_value: str) -> bool
unreal.InterchangeMaterialFactoryNode.get_anisotropy_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_base_color_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_clear_coat_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_clear_coat_normal_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_clear_coat_roughness_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_cloth_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_custom_blend_mode() -> Optional[BlendMode]
unreal.InterchangeMaterialFactoryNode.get_custom_opacity_mask_clip_value() -> Optional[float]
unreal.InterchangeMaterialFactoryNode.get_custom_refraction_method() -> Optional[RefractionMode]
unreal.InterchangeMaterialFactoryNode.get_custom_screen_space_reflections() -> Optional[bool]
unreal.InterchangeMaterialFactoryNode.get_custom_shading_model() -> Optional[MaterialShadingModel]
unreal.InterchangeMaterialFactoryNode.get_custom_translucency_lighting_mode() -> Optional[TranslucencyLightingMode]
unreal.InterchangeMaterialFactoryNode.get_custom_two_sided() -> Optional[bool]
unreal.InterchangeMaterialFactoryNode.get_displacement_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_emissive_color_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_fuzz_color_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_metallic_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_normal_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_object_class() -> Class
unreal.InterchangeMaterialFactoryNode.get_occlusion_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_opacity_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_refraction_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_roughness_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_specular_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_subsurface_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_surface_coverage_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_tangent_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.get_transmission_color_connection() -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFactoryNode.set_custom_blend_mode(attribute_value: BlendMode, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_opacity_mask_clip_value(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_refraction_method(attribute_value: RefractionMode, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_screen_space_reflections(attribute_value: bool) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_shading_model(attribute_value: MaterialShadingModel, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_translucency_lighting_mode(attribute_value: TranslucencyLightingMode, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMaterialFactoryNode.set_custom_two_sided(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeMaterialFunctionCallExpressionFactoryNode(InterchangeMaterialExpressionFactoryNode)`

```python
unreal.InterchangeMaterialFunctionCallExpressionFactoryNode.get_custom_material_function_dependency() -> Optional[str]
unreal.InterchangeMaterialFunctionCallExpressionFactoryNode.set_custom_material_function_dependency(attribute_value: str) -> bool
```

## `unreal.InterchangeMaterialFunctionFactoryNode(InterchangeBaseMaterialFactoryNode)`

```python
unreal.InterchangeMaterialFunctionFactoryNode.get_input_connection(input_name: str) -> Optional[Tuple[str, str]]
unreal.InterchangeMaterialFunctionFactoryNode.get_object_class() -> Class
```

## `unreal.InterchangeMaterialInstanceFactoryNode(InterchangeBaseMaterialFactoryNode)`

```python
unreal.InterchangeMaterialInstanceFactoryNode.get_custom_instance_class_name() -> Optional[str]
unreal.InterchangeMaterialInstanceFactoryNode.get_custom_parent() -> Optional[str]
unreal.InterchangeMaterialInstanceFactoryNode.set_custom_instance_class_name(attribute_value: str) -> bool
unreal.InterchangeMaterialInstanceFactoryNode.set_custom_parent(attribute_value: str) -> bool
```

## `unreal.InterchangeMeshActorFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangeMeshActorFactoryNode.get_custom_animation_asset_uid_to_play() -> Optional[str]
unreal.InterchangeMeshActorFactoryNode.get_custom_geometric_transform() -> Optional[Transform]
unreal.InterchangeMeshActorFactoryNode.get_slot_material_dependencies() -> Map[str, str]
unreal.InterchangeMeshActorFactoryNode.get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
unreal.InterchangeMeshActorFactoryNode.remove_slot_material_dependency_uid(slot_name: str) -> bool
unreal.InterchangeMeshActorFactoryNode.set_custom_animation_asset_uid_to_play(attribute_value: str) -> bool
unreal.InterchangeMeshActorFactoryNode.set_custom_geometric_transform(attribute_value: Transform) -> bool
unreal.InterchangeMeshActorFactoryNode.set_slot_material_dependency_uid(slot_name: str, material_dependency_uid: str) -> bool
```

## `unreal.InterchangeMeshFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeMeshFactoryNode.add_lod_data_unique_id(lod_data_unique_id: str) -> bool
unreal.InterchangeMeshFactoryNode.get_custom_compute_weighted_normals() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_keep_sections_separate() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_lod_group() -> Optional[Name]
unreal.InterchangeMeshFactoryNode.get_custom_recompute_normals() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_recompute_tangents() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_remove_degenerates() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_use_backwards_compatible_f16_trunc_u_vs() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_use_full_precision_u_vs() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_use_high_precision_tangent_basis() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_use_mikk_t_space() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_ignore() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_override() -> Optional[Color]
unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_replace() -> Optional[bool]
unreal.InterchangeMeshFactoryNode.get_lod_data_count() -> int
unreal.InterchangeMeshFactoryNode.get_lod_data_unique_ids() -> Array[str]
unreal.InterchangeMeshFactoryNode.get_slot_material_dependencies() -> Map[str, str]
unreal.InterchangeMeshFactoryNode.get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
unreal.InterchangeMeshFactoryNode.remove_lod_data_unique_id(lod_data_unique_id: str) -> bool
unreal.InterchangeMeshFactoryNode.remove_slot_material_dependency_uid(slot_name: str) -> bool
unreal.InterchangeMeshFactoryNode.reset_slot_material_dependencies() -> bool
unreal.InterchangeMeshFactoryNode.set_custom_compute_weighted_normals(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_keep_sections_separate(attribute_value: bool) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_lod_group(attribute_value: Name, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_recompute_normals(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_recompute_tangents(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_remove_degenerates(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_use_backwards_compatible_f16_trunc_u_vs(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_use_full_precision_u_vs(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_use_high_precision_tangent_basis(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_use_mikk_t_space(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_ignore(attribute_value: bool) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_override(attribute_value: Color) -> bool
unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_replace(attribute_value: bool) -> bool
unreal.InterchangeMeshFactoryNode.set_slot_material_dependency_uid(slot_name: str, material_dependency_uid: str) -> bool
```

## `unreal.InterchangePhysicalCameraFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangePhysicalCameraFactoryNode.get_custom_focal_length() -> Optional[float]
unreal.InterchangePhysicalCameraFactoryNode.get_custom_focus_method() -> Optional[CameraFocusMethod]
unreal.InterchangePhysicalCameraFactoryNode.get_custom_sensor_height() -> Optional[float]
unreal.InterchangePhysicalCameraFactoryNode.get_custom_sensor_width() -> Optional[float]
unreal.InterchangePhysicalCameraFactoryNode.set_custom_focal_length(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangePhysicalCameraFactoryNode.set_custom_focus_method(attribute_value: CameraFocusMethod, add_apply_delegate: bool = True) -> bool
unreal.InterchangePhysicalCameraFactoryNode.set_custom_sensor_height(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangePhysicalCameraFactoryNode.set_custom_sensor_width(attribute_value: float, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangePhysicsAssetFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangePhysicsAssetFactoryNode.get_custom_skeletal_mesh_uid() -> Optional[str]
unreal.InterchangePhysicsAssetFactoryNode.get_object_class() -> Class
unreal.InterchangePhysicsAssetFactoryNode.initialize_physics_asset_node(unique_id: str, display_label: str, asset_class: str) -> None
unreal.InterchangePhysicsAssetFactoryNode.set_custom_skeletal_mesh_uid(attribute_value: str) -> bool
```

## `unreal.InterchangePointLightFactoryNode(InterchangeLightFactoryNode)`

```python
unreal.InterchangePointLightFactoryNode.get_custom_light_falloff_exponent() -> Optional[float]
unreal.InterchangePointLightFactoryNode.get_custom_use_inverse_squared_falloff() -> Optional[bool]
unreal.InterchangePointLightFactoryNode.set_custom_light_falloff_exponent(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangePointLightFactoryNode.set_custom_use_inverse_squared_falloff(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeRectLightFactoryNode(InterchangeLightFactoryNode)`

```python
unreal.InterchangeRectLightFactoryNode.get_custom_source_height() -> Optional[float]
unreal.InterchangeRectLightFactoryNode.get_custom_source_width() -> Optional[float]
unreal.InterchangeRectLightFactoryNode.set_custom_source_height(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeRectLightFactoryNode.set_custom_source_width(attribute_value: float, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeSceneVariantSetsFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeSceneVariantSetsFactoryNode.add_custom_variant_set_uid(variant_uid: str) -> bool
unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uid(index: int) -> str
unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uid_count() -> int
unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uids() -> Array[str]
unreal.InterchangeSceneVariantSetsFactoryNode.get_object_class() -> Class
unreal.InterchangeSceneVariantSetsFactoryNode.remove_custom_variant_set_uid(variant_uid: str) -> bool
```

## `unreal.InterchangeSkeletalMeshFactoryNode(InterchangeMeshFactoryNode)`

```python
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_bone_influence_limit() -> Optional[int]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_create_physics_asset() -> Optional[bool]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_content_type() -> Optional[InterchangeSkeletalMeshContentType]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_morph_target() -> Optional[bool]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_import_vertex_attributes() -> Optional[bool]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_merge_morph_target_shape_with_same_name() -> Optional[bool]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_morph_threshold_position() -> Optional[float]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_physic_asset_soft_object_path() -> Optional[SoftObjectPath]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_skeleton_soft_object_path() -> Optional[SoftObjectPath]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_position() -> Optional[float]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_tangent_normal() -> Optional[float]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_threshold_uv() -> Optional[float]
unreal.InterchangeSkeletalMeshFactoryNode.get_custom_use_high_precision_skin_weights() -> Optional[bool]
unreal.InterchangeSkeletalMeshFactoryNode.get_object_class() -> Class
unreal.InterchangeSkeletalMeshFactoryNode.initialize_skeletal_mesh_node(unique_id: str, display_label: str, asset_class: str) -> None
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_bone_influence_limit(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_create_physics_asset(attribute_value: bool) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_content_type(attribute_value: InterchangeSkeletalMeshContentType) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_morph_target(attribute_value: bool) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_import_vertex_attributes(attribute_value: bool) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_merge_morph_target_shape_with_same_name(attribute_value: bool) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_morph_threshold_position(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_physic_asset_soft_object_path(attribute_value: SoftObjectPath) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_skeleton_soft_object_path(attribute_value: SoftObjectPath) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_position(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_tangent_normal(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_threshold_uv(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSkeletalMeshFactoryNode.set_custom_use_high_precision_skin_weights(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeSkeletonFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeSkeletonFactoryNode.get_custom_root_joint_uid() -> Optional[str]
unreal.InterchangeSkeletonFactoryNode.get_custom_skeletal_mesh_factory_node_uid() -> Optional[str]
unreal.InterchangeSkeletonFactoryNode.get_custom_use_time_zero_for_bind_pose() -> Optional[bool]
unreal.InterchangeSkeletonFactoryNode.get_object_class() -> Class
unreal.InterchangeSkeletonFactoryNode.initialize_skeleton_node(unique_id: str, display_label: str, asset_class: str) -> None
unreal.InterchangeSkeletonFactoryNode.set_custom_root_joint_uid(attribute_value: str) -> bool
unreal.InterchangeSkeletonFactoryNode.set_custom_skeletal_mesh_factory_node_uid(attribute_value: str) -> bool
unreal.InterchangeSkeletonFactoryNode.set_custom_use_time_zero_for_bind_pose(attribute_value: bool) -> bool
```

## `unreal.InterchangeSpotLightFactoryNode(InterchangePointLightFactoryNode)`

```python
unreal.InterchangeSpotLightFactoryNode.get_custom_inner_cone_angle() -> Optional[float]
unreal.InterchangeSpotLightFactoryNode.get_custom_outer_cone_angle() -> Optional[float]
unreal.InterchangeSpotLightFactoryNode.set_custom_inner_cone_angle(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeSpotLightFactoryNode.set_custom_outer_cone_angle(attribute_value: float, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeStandardCameraFactoryNode(InterchangeActorFactoryNode)`

```python
unreal.InterchangeStandardCameraFactoryNode.get_custom_aspect_ratio() -> Optional[float]
unreal.InterchangeStandardCameraFactoryNode.get_custom_far_clip_plane() -> Optional[float]
unreal.InterchangeStandardCameraFactoryNode.get_custom_field_of_view() -> Optional[float]
unreal.InterchangeStandardCameraFactoryNode.get_custom_near_clip_plane() -> Optional[float]
unreal.InterchangeStandardCameraFactoryNode.get_custom_projection_mode() -> Optional[CameraProjectionMode]
unreal.InterchangeStandardCameraFactoryNode.get_custom_width() -> Optional[float]
unreal.InterchangeStandardCameraFactoryNode.set_custom_aspect_ratio(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStandardCameraFactoryNode.set_custom_far_clip_plane(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStandardCameraFactoryNode.set_custom_field_of_view(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStandardCameraFactoryNode.set_custom_near_clip_plane(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStandardCameraFactoryNode.set_custom_projection_mode(attribute_value: CameraProjectionMode, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStandardCameraFactoryNode.set_custom_width(attribute_value: float, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeStaticMeshFactoryNode(InterchangeMeshFactoryNode)`

```python
unreal.InterchangeStaticMeshFactoryNode.add_socket_uid(socket_uid: str) -> bool
unreal.InterchangeStaticMeshFactoryNode.add_socket_uids(socket_uids: Array[str]) -> bool
unreal.InterchangeStaticMeshFactoryNode.get_custom_auto_compute_lod_screen_sizes() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_custom_build_nanite() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_custom_build_reversed_index_buffer() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_custom_build_scale3d() -> Optional[Vector]
unreal.InterchangeStaticMeshFactoryNode.get_custom_distance_field_replacement_mesh() -> Optional[SoftObjectPath]
unreal.InterchangeStaticMeshFactoryNode.get_custom_distance_field_resolution_scale() -> Optional[float]
unreal.InterchangeStaticMeshFactoryNode.get_custom_dst_lightmap_index() -> Optional[int]
unreal.InterchangeStaticMeshFactoryNode.get_custom_generate_distance_field_as_if_two_sided() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_custom_generate_lightmap_u_vs() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_custom_max_lumen_mesh_cards() -> Optional[int]
unreal.InterchangeStaticMeshFactoryNode.get_custom_min_lightmap_resolution() -> Optional[int]
unreal.InterchangeStaticMeshFactoryNode.get_custom_src_lightmap_index() -> Optional[int]
unreal.InterchangeStaticMeshFactoryNode.get_custom_support_face_remap() -> Optional[bool]
unreal.InterchangeStaticMeshFactoryNode.get_lod_screen_size_count() -> int
unreal.InterchangeStaticMeshFactoryNode.get_lod_screen_sizes() -> Array[float]
unreal.InterchangeStaticMeshFactoryNode.get_object_class() -> Class
unreal.InterchangeStaticMeshFactoryNode.get_socket_uid_count() -> int
unreal.InterchangeStaticMeshFactoryNode.get_socket_uids() -> Array[str]
unreal.InterchangeStaticMeshFactoryNode.initialize_static_mesh_node(unique_id: str, display_label: str, asset_class: str) -> None
unreal.InterchangeStaticMeshFactoryNode.remove_socket_ud(socket_uid: str) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_auto_compute_lod_screen_sizes(attribute_value: bool) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_build_nanite(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_build_reversed_index_buffer(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_build_scale3d(attribute_value: Vector, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_distance_field_replacement_mesh(attribute_value: SoftObjectPath, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_distance_field_resolution_scale(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_dst_lightmap_index(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_generate_distance_field_as_if_two_sided(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_generate_lightmap_u_vs(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_max_lumen_mesh_cards(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_min_lightmap_resolution(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_src_lightmap_index(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_custom_support_face_remap(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeStaticMeshFactoryNode.set_lod_screen_sizes(lod_screen_sizes: Array[float]) -> bool
```

## `unreal.InterchangeTexture2DArrayFactoryNode(InterchangeTextureFactoryNode)`

```python
unreal.InterchangeTexture2DArrayFactoryNode.get_custom_address_x() -> Optional[int]
unreal.InterchangeTexture2DArrayFactoryNode.get_custom_address_y() -> Optional[int]
unreal.InterchangeTexture2DArrayFactoryNode.get_custom_address_z() -> Optional[int]
unreal.InterchangeTexture2DArrayFactoryNode.set_custom_address_z(attribute_value: int, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeTexture2DFactoryNode(InterchangeTextureFactoryNode)`

```python
unreal.InterchangeTexture2DFactoryNode.get_custom_address_x() -> Optional[TextureAddress]
unreal.InterchangeTexture2DFactoryNode.get_custom_address_y() -> Optional[TextureAddress]
unreal.InterchangeTexture2DFactoryNode.get_source_block(block_index: int) -> Optional[str]
unreal.InterchangeTexture2DFactoryNode.get_source_block_by_coordinates(x: int, y: int) -> Optional[str]
unreal.InterchangeTexture2DFactoryNode.get_source_blocks() -> Map[int, str]
unreal.InterchangeTexture2DFactoryNode.set_custom_address_x(attribute_value: TextureAddress, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTexture2DFactoryNode.set_custom_address_y(attribute_value: TextureAddress, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTexture2DFactoryNode.set_source_block(block_index: int, source_file: str) -> None
unreal.InterchangeTexture2DFactoryNode.set_source_block_by_coordinates(x: int, y: int, source_file: str) -> None
unreal.InterchangeTexture2DFactoryNode.set_source_blocks(source_blocks: Map[int, str]) -> None
```

## `unreal.InterchangeTextureFactoryNode(InterchangeFactoryBaseNode)`

```python
unreal.InterchangeTextureFactoryNode.get_custom_adjust_brightness() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_brightness_curve() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_hue() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_max_alpha() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_min_alpha() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_rgb_curve() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_saturation() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_adjust_vibrance() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_allow_non_power_of_two() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_custom_alpha_coverage_thresholds() -> Optional[Vector4]
unreal.InterchangeTextureFactoryNode.get_custom_chroma_key_color() -> Optional[Color]
unreal.InterchangeTextureFactoryNode.get_custom_chroma_key_threshold() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_color_space() -> Optional[TextureColorSpace]
unreal.InterchangeTextureFactoryNode.get_custom_composite_power() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_composite_texture_mode() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_compression_no_alpha() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_custom_compression_quality() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_compression_settings() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_defer_compression() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_custom_downscale() -> Optional[float]
unreal.InterchangeTextureFactoryNode.get_custom_downscale_options() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_filter() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_lod_bias() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_lod_group() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_lossy_compression_amount() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_max_texture_size() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_mip_gen_settings() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_mip_load_options() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_padding_color() -> Optional[Color]
unreal.InterchangeTextureFactoryNode.get_custom_power_of_two_mode() -> Optional[int]
unreal.InterchangeTextureFactoryNode.get_custom_prefer_compressed_source_data() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_custom_srgb() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_custom_translated_texture_node_uid() -> Optional[str]
unreal.InterchangeTextureFactoryNode.get_custom_virtual_texture_streaming() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_customb_chroma_key_texture() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_customb_do_scale_mips_for_alpha_coverage() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_customb_flip_green_channel() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_customb_preserve_border() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_customb_use_legacy_gamma() -> Optional[bool]
unreal.InterchangeTextureFactoryNode.get_object_class() -> Class
unreal.InterchangeTextureFactoryNode.initialize_texture_node(unique_id: str, display_label: str, asset_name: str) -> None
unreal.InterchangeTextureFactoryNode.set_custom_adjust_brightness(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_brightness_curve(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_hue(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_max_alpha(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_min_alpha(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_rgb_curve(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_saturation(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_adjust_vibrance(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_allow_non_power_of_two(attribute_value: bool) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_alpha_coverage_thresholds(attribute_value: Vector4, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_chroma_key_color(attribute_value: Color, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_chroma_key_threshold(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_color_space(attribute_value: TextureColorSpace, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_composite_power(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_composite_texture_mode(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_compression_no_alpha(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_compression_quality(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_compression_settings(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_defer_compression(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_downscale(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_downscale_options(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_filter(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_lod_bias(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_lod_group(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_lossy_compression_amount(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_max_texture_size(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_mip_gen_settings(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_mip_load_options(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_padding_color(attribute_value: Color, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_power_of_two_mode(attribute_value: int, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_prefer_compressed_source_data(attribute_value: bool) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_srgb(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_translated_texture_node_uid(attribute_value: str) -> bool
unreal.InterchangeTextureFactoryNode.set_custom_virtual_texture_streaming(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_customb_chroma_key_texture(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_customb_do_scale_mips_for_alpha_coverage(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_customb_flip_green_channel(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_customb_preserve_border(attribute_value: bool, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureFactoryNode.set_customb_use_legacy_gamma(attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

## `unreal.InterchangeTextureLightProfileFactoryNode(InterchangeTexture2DFactoryNode)`

```python
unreal.InterchangeTextureLightProfileFactoryNode.get_custom_brightness() -> Optional[float]
unreal.InterchangeTextureLightProfileFactoryNode.get_custom_texture_multiplier() -> Optional[float]
unreal.InterchangeTextureLightProfileFactoryNode.set_custom_brightness(attribute_value: float, add_apply_delegate: bool = True) -> bool
unreal.InterchangeTextureLightProfileFactoryNode.set_custom_texture_multiplier(attribute_value: float, add_apply_delegate: bool = True) -> bool
```

## `unreal.LiveLinkBlueprintVirtualSubjectFactory(BlueprintFactory)`

```python
unreal.LiveLinkBlueprintVirtualSubjectFactory.role(value: Class) -> None
```

## `unreal.PackageTools(Object)`

```python
unreal.PackageTools.filename_to_package_name(filename: str) -> str
unreal.PackageTools.package_name_to_filename(package_name: str, extension: str = "") -> str
unreal.PackageTools.sanitize_package_name(package_name: str) -> str
```

## `unreal.PoseAssetFactory(Factory)`

```python
unreal.PoseAssetFactory.pose_names(value: Array[str]) -> None
unreal.PoseAssetFactory.source_animation(value: AnimSequence) -> None
```

## `unreal.PyTestObjectLibrary(BlueprintFunctionLibrary)`

```python
unreal.PyTestObjectLibrary.is_bool_set(obj: PyTestObject) -> bool
```

## `unreal.ReimportFbxSceneFactory(FbxSceneImportFactory)`

```python
unreal.ReimportFbxSceneFactory.script_reimport_helper(obj: Object) -> None
```

## `unreal.RigDispatchFactory(RigVMDispatchFactory)`

```python
unreal.RigDispatchFactory.__init__() -> None
```

## `unreal.RigVMAssetDataFilterDynamic(DelegateBase)`

```python
unreal.RigVMAssetDataFilterDynamic.__init__(*args: Any, **kwargs: Any) -> None
```

## `unreal.RigVMDispatchFactory(StructBase)`

```python
unreal.RigVMDispatchFactory.__init__() -> None
```

## `unreal.SmartObjectLibrary(BlueprintFunctionLibrary)`

```python
unreal.SmartObjectLibrary.add_multiple_smart_objects(smart_object_actors: Array[Actor]) -> bool
unreal.SmartObjectLibrary.add_or_remove_multiple_smart_objects(smart_object_actors: Array[Actor], add: bool) -> bool
unreal.SmartObjectLibrary.add_or_remove_smart_object(smart_object: Actor, enabled: bool) -> bool
unreal.SmartObjectLibrary.add_smart_object(smart_object_actor: Actor) -> bool
unreal.SmartObjectLibrary.conv_smart_object_claim_handle_to_string(result: SmartObjectClaimHandle) -> str
unreal.SmartObjectLibrary.conv_smart_object_definition_to_string(definition: SmartObjectDefinition) -> str
unreal.SmartObjectLibrary.conv_smart_object_handle_to_string(handle: SmartObjectHandle) -> str
unreal.SmartObjectLibrary.conv_smart_object_request_result_to_string(result: SmartObjectRequestResult) -> str
unreal.SmartObjectLibrary.conv_smart_object_slot_handle_to_string(handle: SmartObjectSlotHandle) -> str
unreal.SmartObjectLibrary.equal_smart_object_handle_smart_object_handle(a: SmartObjectHandle, b: SmartObjectHandle) -> bool
unreal.SmartObjectLibrary.equal_smart_object_slot_handle_smart_object_slot_handle(a: SmartObjectSlotHandle, b: SmartObjectSlotHandle) -> bool
unreal.SmartObjectLibrary.find_smart_objects_in_actor(filter: SmartObjectRequestFilter, search_actor: Actor, user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectLibrary.find_smart_objects_in_component(filter: SmartObjectRequestFilter, smart_object_component: SmartObjectComponent, user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectLibrary.find_smart_objects_in_list(world_context_object: Object, filter: SmartObjectRequestFilter, actor_list: Array[Actor], user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectLibrary.find_smart_objects_in_targeting_request(world_context_object: Object, filter: SmartObjectRequestFilter, targeting_handle: TargetingRequestHandle, user_actor: Actor = None) -> Optional[Array[SmartObjectRequestResult]]
unreal.SmartObjectLibrary.get_blackboard_value_as_so_claim_handle(node_owner: BTNode, key: BlackboardKeySelector) -> SmartObjectClaimHandle
unreal.SmartObjectLibrary.get_value_as_so_claim_handle(blackboard_component: BlackboardComponent, key_name: Name) -> SmartObjectClaimHandle
unreal.SmartObjectLibrary.is_valid_smart_object_claim_handle(handle: SmartObjectClaimHandle) -> bool
unreal.SmartObjectLibrary.is_valid_smart_object_handle(handle: SmartObjectHandle) -> bool
unreal.SmartObjectLibrary.is_valid_smart_object_slot_handle(handle: SmartObjectSlotHandle) -> bool
unreal.SmartObjectLibrary.k2_set_smart_object_enabled(smart_object: Actor, enabled: bool) -> bool
unreal.SmartObjectLibrary.mark_smart_object_slot_as_claimed(world_context_object: Object, slot_handle: SmartObjectSlotHandle, user_actor: Actor = None, claim_priority: SmartObjectClaimPriority = SmartObjectClaimPriority.NORMAL) -> SmartObjectClaimHandle
unreal.SmartObjectLibrary.mark_smart_object_slot_as_free(world_context_object: Object, claim_handle: SmartObjectClaimHandle) -> bool
unreal.SmartObjectLibrary.mark_smart_object_slot_as_occupied(world_context_object: Object, claim_handle: SmartObjectClaimHandle, definition_class: Class) -> SmartObjectBehaviorDefinition
unreal.SmartObjectLibrary.not_equal_smart_object_handle_smart_object_handle(a: SmartObjectHandle, b: SmartObjectHandle) -> bool
unreal.SmartObjectLibrary.not_equal_smart_object_slot_handle_smart_object_slot_handle(a: SmartObjectSlotHandle, b: SmartObjectSlotHandle) -> bool
unreal.SmartObjectLibrary.remove_multiple_smart_objects(smart_object_actors: Array[Actor]) -> bool
unreal.SmartObjectLibrary.remove_smart_object(smart_object_actor: Actor) -> bool
unreal.SmartObjectLibrary.set_blackboard_value_as_so_claim_handle(node_owner: BTNode, key: BlackboardKeySelector, value: SmartObjectClaimHandle) -> None
unreal.SmartObjectLibrary.set_multiple_smart_objects_enabled(smart_object_actors: Array[Actor], enabled: bool) -> bool
unreal.SmartObjectLibrary.set_smart_object_enabled(smart_object_actor: Actor, enabled: bool) -> bool
unreal.SmartObjectLibrary.set_value_as_so_claim_handle(blackboard_component: BlackboardComponent, key_name: Name, value: SmartObjectClaimHandle) -> None
unreal.SmartObjectLibrary.smart_object_claim_handle_invalid() -> SmartObjectClaimHandle
```

## `unreal.SoundCueFactoryNew(Factory)`

```python
unreal.SoundCueFactoryNew.initial_dialogue_wave(value: DialogueWave) -> None
unreal.SoundCueFactoryNew.initial_sound_wave(value: SoundWave) -> None
```

## `unreal.TypedElementAssetDataInterface(Interface)`

```python
unreal.TypedElementAssetDataInterface.get_all_referenced_asset_datas(element_handle: ScriptTypedElementHandle) -> Array[AssetData]
unreal.TypedElementAssetDataInterface.get_asset_data(element_handle: ScriptTypedElementHandle) -> AssetData
```

## `unreal.TypedElementAssetDataReferencedOptions(StructBase)`

```python
unreal.TypedElementAssetDataReferencedOptions.__init__(only_top_level_asset: bool = False) -> None
unreal.TypedElementAssetDataReferencedOptions.only_top_level_asset(value: bool) -> None
```

