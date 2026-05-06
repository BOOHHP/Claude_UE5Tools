# TA 工具开发日志

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