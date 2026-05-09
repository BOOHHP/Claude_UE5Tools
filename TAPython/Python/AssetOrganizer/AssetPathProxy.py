import unreal


@unreal.uclass()
class AssetPathProxy(unreal.Object):
    scan_paths = unreal.uproperty(
        unreal.Array(unreal.Name),
        meta={"DisplayName": "扫描目录列表（/Game/...）"},
    )
