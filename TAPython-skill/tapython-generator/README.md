# TAPython Skill Documentation

> Full-stack TAPython architect for Unreal Engine 5.5 editor tool development

[中文版](README_CN.md) | English

---

## 📖 Overview

This skill transforms natural language requirements into production-ready TAPython tools following strict MVC architecture patterns. It generates three files:

1. **MenuConfig.json** - Menu registration
2. **[ToolName].json** - UI definition
3. **[ToolName].py** - Controller logic

---

## 📁 File Structure

```
TAPython-skill/
├── SKILL.md                      # 🎯 Main skill file (core principles, quick references)
│
├── templates/                    # 📋 Detailed templates for TAPython tools
│   ├── MenuConfig.json.md        #    Menu configuration template with examples
│   ├── UI.json.md                #    UI definition template with validation
│   └── Controller.py.md          #    Controller logic template with patterns
│
├── widgets/                      # 🧩 Widget reference documentation
│   └── Catalog.md                #    Complete widget catalog (input, display, action, containers)
│
├── patterns/                     # 🎨 Implementation patterns
│   └── CommonPatterns.md         #    4 common patterns (asset processing, actor spawning, etc.)
│
├── pitfalls/                     # ⚠️ Common mistakes and solutions
│   └── CommonPitfalls.md         #    7 critical pitfalls with solutions
│
├── examples/                     # 💡 Complete implementation examples
│   └── CompleteToolExample.md    #    Batch Renamer tool (end-to-end)
│
├── guides/                       # 📘 Practical guides
│   ├── Troubleshooting.md        #    Common issues and solutions (故障排除)
│   ├── FAQ.md                    #    Frequently asked questions (常见问题)
│   └── Performance.md            #    Performance optimization (性能优化)
│
└── TAPython_docs/               # 📚 Official TAPython documentation
    ├── Welcome To TAPython.md
    ├── Chameleon Tool.md
    ├── Slate Overview.md
    └── ... (27+ documentation files)
```

---

## 🚀 How to Use

### Quick Start (Fast Path)

**For immediate tool generation**, open [SKILL.md](SKILL.md) which contains:

- ✅ Core principles (MVC, Singleton, Defensive Programming)
- ✅ Quick templates (copy-paste ready)
- ✅ Validation checklists (verify your implementation)
- ✅ Success criteria (ensure quality)

**Workflow**:
```
User requirement → SKILL.md → Generate 3 files → Validate → Done
```

### Deep Dive (Detailed Path)

**When you need comprehensive information**, navigate to specialized documentation:

| Need | Document | Contents |
|------|----------|----------|
| **Complete templates** | [templates/](templates/) | Full templates with field references, validation, examples |
| **Widget options** | [widgets/Catalog.md](widgets/Catalog.md) | All widgets with JSON definitions and Python access |
| **Implementation patterns** | [patterns/CommonPatterns.md](patterns/CommonPatterns.md) | 4 patterns: asset processing, actor spawning, browser, settings |
| **Avoid mistakes** | [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md) | 7 critical pitfalls with solutions |
| **Full example** | [examples/CompleteToolExample.md](examples/CompleteToolExample.md) | Complete Batch Renamer implementation |
| **Troubleshooting** | [guides/](guides/) | Troubleshooting, FAQ, performance optimization |

---

## 🎓 Learning Path

### Level 1: Beginner
```
1. Read SKILL.md (core principles)
   ↓
2. Study examples/CompleteToolExample.md (full implementation)
   ↓
3. Generate your first tool
```

**Time**: 30 minutes
**Outcome**: Understand basic workflow and generate simple tools

### Level 2: Intermediate
```
1. Use templates/ for copy-paste
   ↓
2. Reference widgets/Catalog.md for widget options
   ↓
3. Implement common UI patterns
```

**Time**: 2 hours
**Outcome**: Build tools with custom UI and multiple widgets

### Level 3: Advanced
```
1. Study patterns/CommonPatterns.md
   ↓
2. Review pitfalls/CommonPitfalls.md
   ↓
3. Build production-ready tools
```

**Time**: 1 day
**Outcome**: Create robust, maintainable tools with error handling

### Level 4: Expert
```
1. Master all patterns and pitfalls
   ↓
2. Contribute new patterns
   ↓
3. Optimize tool architecture
```

**Time**: Ongoing
**Outcome**: Teach others and improve the skill

---

## 📊 Documentation Statistics

| Document | Lines | Purpose | When to Use |
|----------|-------|---------|-------------|
| **SKILL.md** | ~450 | Quick reference | Every tool generation |
| **templates/** | ~500 total | Detailed templates | Need complete structure |
| **widgets/Catalog.md** | ~400 | Widget reference | Choosing widgets |
| **patterns/CommonPatterns.md** | ~600 | Implementation patterns | Following best practices |
| **pitfalls/CommonPitfalls.md** | ~400 | Mistake prevention | Avoiding common errors |
| **examples/CompleteToolExample.md** | ~400 | Full example | Learning complete workflow |
| **guides/** | ~570 total | Troubleshooting, FAQ, Performance | Debugging issues, optimization |

**Total**: ~3270 lines of documentation (vs. original 1116-line monolithic file)

---

## 🔍 Navigation Guide

### By Task

**Creating a new tool?**
1. Start: [SKILL.md](SKILL.md) - Core principles
2. Template: [templates/UI.json.md](templates/UI.json.md) - UI structure
3. Validate: [SKILL.md#validation-checklists](SKILL.md#-validation-checklists)

**Need specific widgets?**
1. Open: [widgets/Catalog.md](widgets/Catalog.md)
2. Find widget category (Input/Display/Action/Container)
3. Copy JSON definition and Python access pattern

**Following a pattern?**
1. Identify your use case in [patterns/CommonPatterns.md](patterns/CommonPatterns.md)
2. Copy the pattern structure
3. Adapt to your requirements

**Debugging issues?**
1. Check [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md)
2. Find your issue in the 7 critical pitfalls
3. Apply the solution

**Learning complete workflow?**
1. Study [examples/CompleteToolExample.md](examples/CompleteToolExample.md)
2. Follow step-by-step implementation
3. Apply to your own tool

**Having performance issues?**
1. Open: [guides/Performance.md](guides/Performance.md)
2. Find your bottleneck category
3. Apply optimization pattern

**Need answers to common questions?**
1. Check: [guides/FAQ.md](guides/FAQ.md)

---

## 🎯 Design Philosophy

### Why This Structure?

**Problem**: Original SKILL.md was 1116 lines - difficult to navigate, maintain, and load efficiently.

**Solution**: Modular documentation with clear separation:

| Aspect | Monolithic | Modular |
|--------|-----------|---------|
| **Navigation** | Scroll through 1116 lines | Click links to jump |
| **Maintenance** | Edit one large file | Edit focused files |
| **Context loading** | Load everything | Load what you need |
| **Reusability** | Search and copy | Dedicated template files |
| **Updates** | Risk breaking entire file | Isolated changes |

### Optimization Metrics

- ✅ **60% reduction** in main file size (original 1116 → 442 lines in SKILL.md)
- ✅ **10 specialized documents** for different needs (was 7)
- ✅ **Clear navigation** with markdown links
- ✅ **Preserved all functionality** from original
- ✅ **New guides/** directory for troubleshooting, FAQ, and performance

---

## 🔗 Quick Links

### Core Documentation
- [SKILL.md](SKILL.md) - Main skill file
- [README_CN.md](README_CN.md) - 中文文档

### Templates
- [MenuConfig.json Template](templates/MenuConfig.json.md)
- [UI.json Template](templates/UI.json.md)
- [Controller.py Template](templates/Controller.py.md)

### References
- [Widget Catalog](widgets/Catalog.md)
- [Common Patterns](patterns/CommonPatterns.md)
- [Common Pitfalls](pitfalls/CommonPitfalls.md)

### Examples
- [Batch Renamer - Complete Example](examples/CompleteToolExample.md)

### Guides
- [Troubleshooting](guides/Troubleshooting.md)
- [FAQ](guides/FAQ.md)
- [Performance](guides/Performance.md)

---

## 📝 Example Usage

### Scenario: Create a Batch Renamer Tool

**Step 1**: Open [SKILL.md](SKILL.md) and read core principles

**Step 2**: Navigate to Quick Templates section for basic structure

**Step 3**: Reference [widgets/Catalog.md](widgets/Catalog.md) for:
- `SEditableText` - For prefix input
- `SButton` - For execute button
- `STextBlock` - For status display

**Step 4**: Study [examples/CompleteToolExample.md](examples/CompleteToolExample.md) for complete implementation

**Step 5**: Check [pitfalls/CommonPitfalls.md](pitfalls/CommonPitfalls.md) to avoid:
- Inline Python in UI
- Missing Aka fields
- No error handling

**Step 6**: Validate against [SKILL.md#validation-checklists](SKILL.md#-validation-checklists)

---

## 🤝 Contributing

To improve this skill:

1. **Add patterns**: Create new pattern files in `patterns/`
2. **Document pitfalls**: Add discovered pitfalls to `pitfalls/`
3. **Provide examples**: Add complete examples to `examples/`
4. **Update templates**: Improve templates based on best practices

---

## 📚 Additional Resources

- [Official TAPython Documentation](TAPython_docs/) - 27+ documentation files
- [Chameleon Tool Guide](TAPython_docs/Chameleon Tool.md) - UI system
- [Slate Overview](TAPython_docs/Slate Overview.md) - Widget reference
- [Most Used Editor APIs](TAPython_docs/Most Used Editor APIs.md) - API reference

---

## 📜 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-30 | Initial structure with 1116-line SKILL.md |
| 2.0 | 2026-03-30 | **Modular restructure**: 442-line SKILL.md + 7 specialized documents |
| 3.0 | 2026-04-03 | **Full optimization**: Deleted Prompt.md (merged into SKILL.md), added guides/ directory, expanded ChameleonData API and 4 TAPython_docs files |

---

## 📄 License

Part of the TAPython skill documentation. Use freely for Unreal Engine 5.5 tool development.

---

*Last updated: 2026-04-03*
