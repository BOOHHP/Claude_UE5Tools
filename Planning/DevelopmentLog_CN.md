# TA 工具开发日志

## 2026-05-07 - SceneTools Iteration 2.1：先沉淀场景批处理底座

- 模块：`TAPython/Python/SceneTools/`
- 范围：记录下一阶段开发判断，并作为后续开发入口。
- 判断：优先把 SceneTools Iteration 2 打成稳定的场景批处理底座，再继续扩展 G-11、G-15、05、11 等场景类工具。
- 原因：当前 SceneTools 与 BatchTagTool 已反复出现同类共性需求：预览/执行、事务撤销、变更快照、统计报告、失败清单、分批处理与状态反馈；若继续横向新增单点工具，会重复实现这些能力。
- 开发顺序：先补强 `03_Actor落地检测` 的事务、快照、报告与分帧执行，再开发 G-11 批量修改物体渲染属性，随后推进 G-15 对齐/阵列/分布。
- 本轮实现入口：先在不改变 UI 的前提下增强 `execute_ground_snap()`，补充 `ScopedEditorTransaction`、执行快照与 changed/skipped/failed 报告，为后续统一批处理框架铺路。
- 修复验证：落地修正执行后已能通过 Ctrl+Z 回到原位置；关键修复为事务内对 Actor 与 RootComponent 调用 `modify()`，且事务创建失败时取消执行，避免无事务改位置。
- 下一步：进入 G-11 批量修改物体渲染属性 v1，先做关卡实例级 Actor/Component 渲染属性，不触碰蓝图源资产。
- G-11 v1：已在 SceneTools 新增“渲染属性”面板，支持 Actor Hidden In Game、组件 Hidden In Game、组件可见性、Cast Shadow、Max Draw Distance 的预览/执行。
- G-11 执行策略：执行前生成差异计划；执行时使用 `ScopedEditorTransaction`，并在写入前对目标 Actor/Component 调用 `modify()`；事务创建失败时取消执行，避免不可撤销修改。
- 验证结果：G-11 渲染属性批处理已在 UE 中验证功能正常；补齐 `_safe_object_name()` 后，预览/执行不再因组件命名中断。
- 下一步：进入 G-15 批量对齐/阵列/分布 v1。
- G-15 v1：已在 SceneTools 新增“对齐 / 分布”面板，支持按 X/Y/Z 轴对齐到首个 Actor、等距分布、按步长阵列。
- G-15 执行策略：执行前生成目标位置计划；执行时使用 `ScopedEditorTransaction`，并在移动前对 Actor 与 RootComponent 调用 `modify()`，保持 Ctrl+Z 撤销链路。
- G-15 交互修正：轴向选择由文本输入改为 X/Y/Z 多选勾选框；对齐、等距分布和步长阵列均可一次作用于多个轴，且至少保留一个轴向选中。
- 验证结果：G-15 对齐/分布/阵列已在 UE 中验证功能正常，多轴勾选交互可用。
- 分帧执行 v1：SceneTools 新增通用分帧任务入口；`03_Actor落地检测` 在待修正 Actor 数超过 50 时自动分帧执行，每批处理 50 个，并在工具关闭/热重载时注销后台回调。
- 分帧执行 v1.1：分帧入口已复用于 G-11/G-15；G-11 按待写入渲染属性变更项分批执行，G-15 按待移动 Actor 分批执行，同步路径仍作为小批量默认路径与后台驱动注册失败回退。
- 分帧执行修复：测试发现仅依赖 Slate post tick 时，后台任务不会稳定自动推进，表现为需要再次点击按钮才处理下一批；已改为优先使用 `unreal.PythonBPLib.set_timer()` 定时推进，Slate tick 仅作为兼容回退。
- 验证结果：分帧执行 timer 驱动方案已在 UE 中验证功能逻辑正确，点击一次后可自动推进后续批次，不再需要手动再次点击。
- 变换工具撤销修复：位置归零、旋转归零、缩放归一、全变换重置已接入 `ScopedEditorTransaction`，并在写入前对 Actor 与 RootComponent 调用 `modify(True)`；Transform 写入改为构造完整 `unreal.Transform` 后单次 `set_actor_transform()`，避免分散写入导致 Ctrl+Z 状态不一致。
- 热重载兼容修复：`InitPyCmd` / `OnClosePyCmd` 已改为 `getattr(SceneTools, 'on_close', lambda: None)()` 安全调用，避免旧版内存模块缺少 `on_close` 时抛出 AttributeError 并阻断 `importlib.reload()`。
- UI FontInfo 修复：SceneTools.json 中 18 处 `Font: ["Segoe UI", ...]` 数组格式已改为 Chameleon 可解析的 `FontObject + Size` 对象格式，避免打开工具时反复输出 `ParseFontInfo JsonValue Type Error, Need Object`。
- 验证结果：SceneTools 打开/关闭报错与 FontInfo 解析报错均已在 UE 中确认消除。
- 验证状态：`SceneTools.py` 已通过 Pylance 问题检查与 `python -m py_compile`；SceneTools Iteration 2.1 可进入收尾与下一阶段开发。

---

## 2026-05-06 - SceneTools：Actor 落地检测 v1

- 模块：`TAPython/Python/SceneTools/`
- 范围：并入 SceneTools Iteration 2 的 `03_Actor落地检测` 首个可用版本。
- UI：在 SceneTools 中新增“落地检测”折叠面板，提供碰撞 Profile、最大射线距离、修正阈值、地面偏移、起始偏移、预览和执行按钮。
- 逻辑：新增 `preview_ground_snap()` / `execute_ground_snap()`，按已选 Actor 生成落地计划并输出 `[SNAP] / [OK] / [MISS] / [ERR]` 预览结果。
- 命中策略：优先使用 `unreal.SystemLibrary.line_trace_single_by_profile()`；当 Trace Profile 未命中时，回退到场景 Actor Bounds 检测，取脚下最高表面作为地面高度。
- 执行策略：仅修正 `abs(deltaZ)` 大于阈值的 Actor，保持预览/执行双阶段。
- 验证：`SceneTools.json` 通过 UTF-8 JSON 解析；`SceneTools.py` 通过 Pylance 语法检查与 `python -m py_compile`。
- 已知限制：当前版本是同步批处理；1000+ Actor 场景仍需引入分帧队列。执行操作尚未记录 Ctrl+Z 事务或回滚快照。
- 下一步：继续 SceneTools Iteration 2 的 G-11 渲染属性批处理，或补强落地检测的分帧执行、回滚快照和更明确的碰撞通道配置。

---

## 2026-05-06 - BatchTagTool：P0/P1 优化 + 按Tag选Actor修复

- 模块：`TAPython/Python/BatchTagTool/`
- 提交：`004be08`（`BatchTagTool.py` +264/-64 · `BatchTagTool.json` +55/-1）
- 触发：`/tapython-generator` Sub-agent 全面代码审查，输出 P0/P1/P2 问题清单。
- **P0 安全性修复**：
  - "完全覆盖"写入新增 `chk_confirm_override` 确认 SCheckBox + 橙色警告文字；未勾选则拦截写入。
  - `on_closed()` 正确清理 `_tick_handle`，防止热重载后幽灵 tick 竞争。
- **P1 鲁棒性修复**：
  - `_on_tick` 捕获异常后单次告警（`_tick_error_reported`），状态栏提示用户手动重读。
  - Tag 规范化：`_normalize_tag_name()` / `_normalize_tag_list()` 去空格、过滤 None、去重。
  - `_write_target_tags()` 返回 `{changed, skipped, failed}` 统计，状态栏显示写入结果。
- **按Tag选Actor 修复**：根因为 `on_select_by_tag()` 只读 `_ni_selected_tags` 缓存，`OnSelectionChanged` 未触发时缓存为空；修复为按钮点击时主动调 `get_list_view_items()` 读取 SListView 当前选中下标，再映射到 `_ni_items_cache`。
- 验证：`python -m json.tool` + `python -m py_compile` + `get_errors` 均通过。
- 未实施（P2，留后续）：Tag 批量写入异步化、SDetailsView 与 SListView 双向联动、撤销历史命名优化。

---

## 2026-04-22 - BatchTagTool：从"自建数组 UI"升级为"SDetailsView 原生代理"

- 模块：`TAPython/Python/BatchTagTool/`（新建独立工具）
- 经历两代设计演进：
  - **第一代**（SceneTools 内嵌 Tag 面板 → 已拆出）：8 行 indexed/mixed 三态列表，自建索引行对齐 UE5 细节面板，Replace-All 覆写语义；在多选批量场景存在误操作风险。
  - **第二代**（当前版）：虚拟 UObject 代理（`BatchTagProxy.py`，独立 `@uclass` 模块）+ `SDetailsView` 绑定，原生数组编辑器接管 UI，代码量减少约 80%。
- **关键设计决策**：
  - `@uclass` 类独立模块，主模块 `importlib.reload` 不触碰 UClass 注册。
  - 增量合并 vs 完全覆盖双模式（增量安全追加 Tag，覆盖模式含 `ScopedEditorTransaction`）。
  - 交集预览工作流：选中 Actor → 自动计算 Tag 交集写入代理 → SDetailsView 显示共有 Tag → 用户增删 → 点击应用。
- **新增 Bug 记录（#8~#11）**：
  - `#8`：`create_file` 对已存在文件 append 而非 overwrite，文件末尾旧类覆盖新类。
  - `#9`：`@unreal.uclass()` reload 重复注册崩溃 → 代理类拆独立模块。
  - `#10`：`new_object` 返回代理被 GC 回收 → 需 `self.tag_proxy` 强引用。
  - `#11`：`set_object` 在 `__init__` 中调用无效（UI 未渲染完成）→ 延迟到 Slate tick 首帧。

---

## 2026-04-17 - SceneTools Tag 面板：对齐 UE5 原生 Actor 标签逻辑（完整重设计）

- 模块：`TAPython/Python/SceneTools/`（SceneTools Iteration 1 后续）
- 将 Tag 输入区从多行文本框完整重设计为动态索引列表，对齐 UE5 细节面板中 Actor 标签编辑行为。
- **三态展示逻辑**：无选中→0行；单选/多选且 Tag 一致→indexed 模式；多选且 Tag 各不相同→mixed 橙色提示。
- **Tag 写入语义改为 Replace-All**（完整覆盖目标 Actor 标签列表，对齐 UE5 原生行为）。
- 实时自动读取：`unreal.register_slate_post_tick_callback` 节流（每 ~15 帧）检测选中状态变化，自动刷新。
- **关键 Bug 修复（#4~#7，已同步 CommonPitfalls.md）**：
  - `#4`：`STextBlock` 的 `set_visible` 不生效 → 改用 `set_text("")` 置空模拟隐藏。
  - `#5`：`__init__` 中调用 `set_visible` 被静默忽略（UI 未渲染完）→ 改在 tick 首帧初始同步（`_initial_sync_done` 标志）。
  - `#6`：`SHorizontalBox`/`SVerticalBox` 不支持 `set_visible` → 用 `SBox` 包裹每行，`Aka` 注册到 `SBox`。
  - `#7`：`SExpandableArea` 的 `AreaTitle` 无效 → 改用 `HeaderContent`。

---

## 2026-04-09 - SceneTools：重构与场景可见性工作流交付

- 模块：`TAPython/Python/SceneTools/`（由 SceneSelectTool 重构而来）
- 将原 Scene Selection Tool 统一重命名为 SceneTools（Python、JSON、MenuConfig 全同步）。
- **新增功能**：针对已选 Actor 的编辑器可见性操作（隐藏已选 / 显示已选）。
- **兼容性处理**：Actor 编辑器可见性采用多级回退逻辑；Checkbox API 命名差异（`set_is_checked` vs `set_check_boxe_is_checked`）封装到 helper 方法；JSON 布尔回调参数问题改为无参独立回调。
- **UI 重构**：SceneTools 改为可折叠分组面板（选择工具 / 隐藏工具）+ 窗口高度自适应。
- 关键提交：`ad460c0`

---

## 2026-04-08 - 工作区初始化与首个可用工具交付

- 模块：`TAPython/Python/SceneTools/`（前身 SceneSelectTool）；README / MenuConfig
- 建立 Claude_UE5Tools 工作区，完成 TAPython 工具框架理解与菜单集成。
- **首个可用工具**：Scene Selection Tool（批量选择 Actor）
  - 当前关卡 / 所有关卡范围选择
  - 常见 Actor 类别：StaticMesh、蓝图 Actor、多种灯光类型、贴花、摄像机、触发器
  - 清空当前选择
- **关键技术决策**：SceneSelectTool 采用分层关卡解析策略（多级回退，减少 UE 版本 API 差异）；菜单名英文 + tooltip 中文描述。
- **文档建设**：新增 README.md / README_CN.md，补充 Python Additional Paths 配置、Chameleon Sketch 验证方法、UE 项目英文路径限制。
- **仓库配置**：TAPython-skill 从 git 子模块改为主仓库直接跟踪目录，避免外部权限依赖。
- 主仓库远端：`https://github.com/BOOHHP/Claude_UE5Tools.git`