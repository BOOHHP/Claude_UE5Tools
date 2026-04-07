# TAPython 技能文档

> ⚠️ **本文档为衍生版本** — 以 [README.md](README.md) 为主版本（Single Source of Truth）。如有内容不一致，请以 README.md 为准。

> 专为 Unreal Engine 5.5 编辑器工具开发的全栈 TAPython 架构师

中文版 | [English](README.md)

---

## 📖 概述

本技能将自然语言需求转换为生产级的 TAPython 工具，遵循严格的 MVC 架构模式。生成的文件包括：

1. **MenuConfig.json** - 菜单注册配置
2. **[工具名].json** - UI 界面定义
3. **[工具名].py** - 控制器逻辑

---

## 📁 文件结构

```
TAPython-skill/
├── SKILL.md                      # 🎯 主技能文件（核心原则、快速参考）
│
├── templates/                    # 📋 TAPython 工具的详细模板
│   ├── MenuConfig.json.md        #    菜单配置模板（含示例）
│   ├── UI.json.md                #    UI 定义模板（含验证）
│   └── Controller.py.md          #    控制器逻辑模板（含模式）
│
├── widgets/                      # 🧩 Widget 参考文档
│   └── Catalog.md                #    完整 Widget 目录（输入、显示、操作、容器）
│
├── patterns/                     # 🎨 实现模式
│   └── CommonPatterns.md         #    4 种常见模式（资产处理、Actor 生成等）
│
├── pitfalls/                     # ⚠️ 常见错误及解决方案
│   └── CommonPitfalls.md         #    7 个关键陷阱及解决方案
│
├── examples/                     # 💡 完整实现示例
│   └── CompleteToolExample.md    #    批量重命名工具（端到端示例）
│
├── guides/                       # 📘 实用指南
│   ├── Troubleshooting.md        #    常见问题及解决方案（故障排除）
│   ├── FAQ.md                    #    常见问题解答（FAQ）
│   └── Performance.md            #    性能优化指南
│
└── TAPython_docs/               # 📚 TAPython 官方文档
    ├── Welcome To TAPython.md
    ├── Chameleon Tool.md
    ├── Slate Overview.md
    └── ... (27+ 文档文件)
```

---

## 🚀 如何使用

### 快速上手（快速路径）

**立即生成工具**，打开 [SKILL.md](SKILL.md)，其中包含：

- ✅ 核心原则（MVC、单例模式、防御性编程）
- ✅ 快速模板（可直接复制粘贴）
- ✅ 验证清单（验证您的实现）
- ✅ 成功标准（确保质量）

**工作流程**：
```
用户需求 → SKILL.md → 生成 3 个文件 → 验证 → 完成
```

### 深入学习（详细路径）

**当需要全面信息时**，导航到专门的文档：

| 需求 | 文档 | 内容 |
|------|------|------|
| **完整模板** | [templates/](templates/) | 完整模板，包含字段引用、验证、示例 |
| **Widget 选项** | [widgets/Catalog.md](widgets/Catalog.md) | 所有 Widget，包含 JSON 定义和 Python 访问方法 |
| **实现模式** | [patterns/CommonPatterns.md](patterns/CommonPatterns.md) | 4 种模式：资产处理、Actor 生成、浏览器、设置 |
| **避免错误** | [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md) | 7 个关键陷阱及解决方案 |
| **完整示例** | [examples/CompleteToolExample.md](examples/CompleteToolExample.md) | 完整的批量重命名工具实现 |
| **故障排除** | [guides/](guides/) | 故障排除、常见问题、性能优化 |

---

## 🎓 学习路径

### 第 1 级：初学者
```
1. 阅读 SKILL.md（核心原则）
   ↓
2. 学习 examples/CompleteToolExample.md（完整实现）
   ↓
3. 生成您的第一个工具
```

**时间**：30 分钟
**成果**：理解基本工作流程，生成简单工具

### 第 2 级：中级
```
1. 使用 templates/ 进行复制粘贴
   ↓
2. 参考 widgets/Catalog.md 选择 Widget
   ↓
3. 实现常见的 UI 模式
```

**时间**：2 小时
**成果**：构建具有自定义 UI 和多个 Widget 的工具

### 第 3 级：高级
```
1. 学习 patterns/CommonPatterns.md
   ↓
2. 审查 pitfalls/CommonPitfalls.md
   ↓
3. 构建生产级工具
```

**时间**：1 天
**成果**：创建健壮、可维护的工具，具有完善的错误处理

### 第 4 级：专家
```
1. 掌握所有模式和陷阱
   ↓
2. 贡献新模式
   ↓
3. 优化工具架构
```

**时间**：持续进行
**成果**：教导他人，改进技能

---

## 📊 文档统计

| 文档 | 行数 | 用途 | 何时使用 |
|------|------|------|----------|
| **SKILL.md** | ~450 | 快速参考 | 每次工具生成 |
| **templates/** | ~500 总计 | 详细模板 | 需要完整结构 |
| **widgets/Catalog.md** | ~400 | Widget 参考 | 选择 Widget |
| **patterns/CommonPatterns.md** | ~600 | 实现模式 | 遵循最佳实践 |
| **pitfalls/CommonPitfalls.md** | ~400 | 错误预防 | 避免常见错误 |
| **examples/CompleteToolExample.md** | ~400 | 完整示例 | 学习完整工作流程 |
| **guides/** | ~570 总计 | 故障排除、FAQ、性能优化 | 调试问题、优化性能 |

**总计**：~3270 行文档（相比原来的 1116 行单一文件）

---

## 🔍 导航指南

### 按任务导航

**创建新工具？**
1. 起点：[SKILL.md](SKILL.md) - 核心原则
2. 模板：[templates/UI.json.md](templates/UI.json.md) - UI 结构
3. 验证：[SKILL.md#validation-checklists](SKILL.md#-validation-checklists)

**需要特定的 Widget？**
1. 打开：[widgets/Catalog.md](widgets/Catalog.md)
2. 找到 Widget 类别（输入/显示/操作/容器）
3. 复制 JSON 定义和 Python 访问模式

**遵循模式开发？**
1. 在 [patterns/CommonPatterns.md](patterns/CommonPatterns.md) 中识别您的用例
2. 复制模式结构
3. 根据需求调整

**调试问题？**
1. 查看 [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md)
2. 在 7 个关键陷阱中找到您的问题
3. 应用解决方案

**学习完整工作流程？**
1. 学习 [examples/CompleteToolExample.md](examples/CompleteToolExample.md)
2. 跟随逐步实现
3. 应用到您自己的工具

**遇到性能问题？**
1. 打开：[guides/Performance.md](guides/Performance.md)
2. 找到您的瓶颈类别
3. 应用优化方案

**需要常见问题的解答？**
1. 查看：[guides/FAQ.md](guides/FAQ.md)

---

## 🎯 设计理念

### 为什么采用这种结构？

**问题**：原始 SKILL.md 有 1116 行 - 难以导航、维护和高效加载。

**解决方案**：模块化文档，清晰分离：

| 方面 | 单一文件 | 模块化 |
|------|----------|--------|
| **导航** | 滚动浏览 1116 行 | 点击链接跳转 |
| **维护** | 编辑一个大文件 | 编辑专注的文件 |
| **上下文加载** | 加载所有内容 | 只加载需要的部分 |
| **可重用性** | 搜索并复制 | 专用模板文件 |
| **更新** | 有破坏整个文件的风险 | 隔离更改 |

### 优化指标

- ✅ **主文件减少 60%**（原始 1116 → 442 行 SKILL.md）
- ✅ **10 个专门文档**满足不同需求（原为 7 个）
- ✅ **清晰的导航**使用 Markdown 链接
- ✅ **保留所有原有功能**
- ✅ **新增 guides/** 目录，包含故障排除、FAQ 和性能优化

---

## 🔗 快速链接

### 核心文档
- [SKILL.md](SKILL.md) - 主技能文件
- [README.md](README.md) - English Documentation

### 模板
- [MenuConfig.json 模板](templates/MenuConfig.json.md)
- [UI.json 模板](templates/UI.json.md)
- [Controller.py 模板](templates/Controller.py.md)

### 参考
- [Widget 目录](widgets/Catalog.md)
- [常见模式](patterns/CommonPatterns.md)
- [常见陷阱](pitfalls/CommonPitfalls.md)

### 示例
- [批量重命名工具 - 完整示例](examples/CompleteToolExample.md)

### 指南
- [故障排除](guides/Troubleshooting.md)
- [常见问题](guides/FAQ.md)
- [性能优化](guides/Performance.md)

---

## 📝 使用示例

### 场景：创建批量重命名工具

**第 1 步**：打开 [SKILL.md](SKILL.md) 阅读核心原则

**第 2 步**：导航到快速模板部分获取基本结构

**第 3 步**：参考 [widgets/Catalog.md](widgets/Catalog.md) 了解：
- `SEditableText` - 用于前缀输入
- `SButton` - 用于执行按钮
- `STextBlock` - 用于状态显示

**第 4 步**：学习 [examples/CompleteToolExample.md](examples/CompleteToolExample.md) 获取完整实现

**第 5 步**：检查 [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md) 避免：
- UI 中的内联 Python
- 缺少 Aka 字段
- 没有错误处理

**第 6 步**：对照 [SKILL.md#validation-checklists](SKILL.md#-validation-checklists) 进行验证

---

## 🤝 贡献

改进此技能：

1. **添加模式**：在 `patterns/` 中创建新的模式文件
2. **文档化陷阱**：将发现的陷阱添加到 `pitfalls/`
3. **提供示例**：将完整示例添加到 `examples/`
4. **更新模板**：基于最佳实践改进模板

---

## 📚 其他资源

- [TAPython 官方文档](TAPython_docs/) - 27+ 文档文件
- [Chameleon Tool 指南](TAPython_docs/Chameleon Tool.md) - UI 系统
- [Slate 概述](TAPython_docs/Slate Overview.md) - Widget 参考
- [最常用的编辑器 API](TAPython_docs/Most Used Editor APIs.md) - API 参考

---

## 📜 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0 | 2026-03-30 | 初始结构，1116 行的 SKILL.md |
| 2.0 | 2026-03-30 | **模块化重构**：442 行 SKILL.md + 7 个专门文档 |
| 3.0 | 2026-04-03 | **全面优化**：删除 Prompt.md（合并至 SKILL.md）、新增 guides/ 目录、扩展 ChameleonData API 及 4 个 TAPython_docs 文件 |

---

## 📄 许可证

TAPython 技能文档的一部分。可自由用于 Unreal Engine 5.5 工具开发。

---

*最后更新：2026-04-03*
