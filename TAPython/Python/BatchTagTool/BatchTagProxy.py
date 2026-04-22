"""
BatchTagProxy — SDetailsView 用的虚拟 UObject 代理。

此模块必须只被导入一次（不能随 InitPyCmd 的 importlib.reload 反复执行），
否则 `@unreal.uclass()` 会因重复注册同名 UClass 而报错。

BatchTagTool.py 中以普通 `from BatchTagTool import BatchTagProxy` 导入，
Python 的模块缓存会保证装饰器仅在首次导入时运行一次。
"""

import unreal


@unreal.uclass()
class BatchTagProxy(unreal.Object):
    """单属性代理对象：一个 FName 数组，供 SDetailsView 原生渲染数组编辑器。"""

    edit_tags = unreal.uproperty(
        unreal.Array(unreal.Name),
        meta={"DisplayName": "Tags（交集预览 / 待应用列表）"},
    )
