# UE Python API 导航器

中文版 | [English](README.md)

一个 Copilot 技能，为 AI 提供**精确、版本准确**的 Unreal Engine Python API 签名 — 通过从项目 PythonStub 中提取的真实方法签名替代猜测，彻底消除 API 幻觉。

## 痛点

AI 模型经常在 UE Python API 调用上产生幻觉：错误的方法名、不正确的参数、或在用户引擎版本中根本不存在的 API。而 37MB 的 `unreal.py` 存根文件对任何 LLM 上下文窗口来说都太大了。

## 解决方案

将庞大的存根文件拆分为 **15 个按领域划分的模块**，AI 按需加载 — 只获取当前任务所需的精确 API 签名。

**覆盖范围**：15 个领域，7,629 个类，44,235 个方法。

## 工作原理

```
用户需求 → AI 分析任务领域 → 加载相关模块 → 使用精确签名编写代码
```

1. **路由** — SKILL.md 包含路由表，将任务类型映射到模块文件
2. **加载** — AI 只读取相关的 `modules/<domain>.md`（通常 26KB–438KB，而非 37MB）
3. **实现** — 代码使用经过验证的签名编写，而非依赖训练数据的猜测

## 模块索引

| 模块 | 领域 | 类数 | 方法数 |
|------|------|-----:|-------:|
| `asset_management.md` | 资产增删改查、工厂、内容浏览器 | 92 | 789 |
| `actor_level.md` | Actor、关卡、世界、变换 | 607 | 3,624 |
| `rendering.md` | 材质、纹理、网格、Nanite、光照 | 510 | 3,680 |
| `animation.md` | 骨骼、动画、骨骼、蒙太奇 | 532 | 2,631 |
| `blueprint.md` | 蓝图图表、节点、K2Node | 293 | 1,912 |
| `ui_chameleon.md` | TAPython UI、Slate 控件、工具栏 | 136 | 1,125 |
| `geometry_procedural.md` | PCG、样条线、地形、植被、水体 | 557 | 3,636 |
| `input_camera.md` | 输入、摄像机、玩家、控制器 | 318 | 2,734 |
| `editor_tools.md` | 编辑器工具、设置、开发工具 | 244 | 1,909 |
| `audio.md` | 音频、MetaSound、Quartz、合成器 | 178 | 1,304 |
| `sequencer_movie.md` | Sequencer、MovieScene、LevelSequence | 155 | 1,043 |
| `physics_collision.md` | 物理、碰撞、Chaos、刚体 | 165 | 727 |
| `ai_navigation.md` | AI、行为树、导航、Mass | 79 | 249 |
| `data_table.md` | 数据表、曲线表、结构体 | 16 | 111 |
| `core_misc.md` | 模块级函数、PythonBPLib、其他 | 3,747 | 18,761 |

## 目录结构

```
ue-api-navigator/
├── SKILL.md                    # 技能定义：路由表 + 协议
├── README.md                   # 英文说明
├── README_CN.md                # 本文件
├── modules/                    # 15 个按领域划分的 API 参考文件
│   ├── asset_management.md
│   ├── actor_level.md
│   ├── rendering.md
│   ├── animation.md
│   ├── blueprint.md
│   ├── ui_chameleon.md
│   ├── geometry_procedural.md
│   ├── input_camera.md
│   ├── editor_tools.md
│   ├── audio.md
│   ├── sequencer_movie.md
│   ├── physics_collision.md
│   ├── ai_navigation.md
│   ├── data_table.md
│   ├── core_misc.md
│   └── _stats.json             # 模块生成统计信息
└── tools/
    └── generate_api_skills.py  # 从 PythonStub 重新生成模块的脚本
```

## 重新生成模块

当 UE 引擎版本变更或插件增减时：

```bash
python tools/generate_api_skills.py "/path/to/YourProject/Intermediate/PythonStub/unreal.py"
```

此脚本会重新扫描存根文件并生成所有领域模块的最新签名。

## 与 tapython-generator 的协作

本技能与 [tapython-generator](../tapython-generator/) 协同工作：

| 技能 | 职责 |
|------|------|
| **tapython-generator** | MVC 架构：MenuConfig.json + UI.json + Logic.py |
| **ue-api-navigator** | 为 Logic.py 中的 `unreal.xxx` 调用提供精确 API 签名 |

## 核心设计原则

- **"先查后写"** — AI 在编写引擎交互代码之前先加载经过验证的签名
- **渐进加载** — 只加载相关领域，最小化 Token 消耗
- **hasattr 兜底** — 当模块中找不到 API 时，使用防御性的 `hasattr()` 检测
- **探针脚本** — 对于真正未知的 API，生成轻量级内省脚本供用户在 TAPython REPL 中运行
