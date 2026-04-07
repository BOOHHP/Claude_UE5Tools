#!/usr/bin/env python3
"""
generate_api_skills.py — UE Python Stub 领域切片工具

将 15MB 的 unreal.py 存根文件按功能领域拆分为轻量级 Markdown 文件，
供 AI Copilot 按需加载，实现渐进式上下文注入。

用法:
    python generate_api_skills.py <stub_path> [--output-dir <dir>]

示例:
    python generate_api_skills.py "C:/MyProject/Intermediate/PythonStub/unreal.py"
    python generate_api_skills.py ./unreal.py --output-dir ../ue-api-navigator/modules
"""

import os
import re
import json
import argparse
from collections import defaultdict

# ============================================================
# 领域路由规则：类名包含这些关键字的，归入对应领域
# ============================================================
ROUTING_RULES = {
    # ---- 高优先级：精确匹配 ----
    "asset_management": [
        "AssetRegistry", "AssetData", "AssetTools", "EditorAssetLibrary",
        "ContentBrowser", "ObjectLibrary", "Package", "Factory",
    ],
    "actor_level": [
        "Actor", "Level", "World", "Transform",
        "EditorLevelLibrary", "GameplayStatics", "Subsystem",
    ],
    "rendering": [
        "Material", "Texture", "Nanite", "Lumen",
        "Light", "Shader", "Render", "PostProcess", "Niagara",
        "StaticMesh", "SkeletalMesh",
    ],
    "animation": [
        "Anim", "Skeleton", "Bone", "Montage",
        "IKRig", "ControlRig", "Pose", "Groom",
    ],
    "blueprint": [
        "Blueprint", "Graph", "Node", "Pin",
        "EditorScripting", "K2Node",
    ],
    "ui_chameleon": [
        "Chameleon", "Slate", "Widget", "EditorUtility",
        "Toolbar", "Panel", "Window",
    ],
    "data_table": [
        "DataTable", "CurveTable", "CompositeDataTable",
        "UserDefined",
    ],
    # ---- 中优先级：从 core_misc 中分离 ----
    "physics_collision": [
        "Physics", "Collision", "Chaos", "Damage",
        "Constraint", "RigidBody", "Ragdoll",
    ],
    "geometry_procedural": [
        "Geometry", "Procedural", "PCG", "Spline", "Curve",
        "Landscape", "Foliage", "Water",
    ],
    "audio": [
        "Audio", "Sound", "Metasound", "Quartz",
        "Modular", "Synth",
    ],
    "ai_navigation": [
        "AIController", "BehaviorTree", "Blackboard",
        "Navigation", "NavMesh", "Crowd", "EQS",
        "StateTree", "MassEntity", "Mass",
    ],
    "sequencer_movie": [
        "MovieScene", "Sequencer", "LevelSequence",
        "MoviePipeline", "Interchange",
    ],
    "input_camera": [
        "Input", "Camera", "Player", "Character",
        "Pawn", "Controller", "EnhancedInput",
    ],
    "editor_tools": [
        "Editor", "Config", "Settings", "Developer",
    ],
}


def get_domain(class_name: str) -> str:
    """根据类名匹配领域。优先匹配更具体的关键字。"""
    name_lower = class_name.lower()
    for domain, keywords in ROUTING_RULES.items():
        if any(kw.lower() in name_lower for kw in keywords):
            return domain
    return "core_misc"


def parse_stub(stub_path: str) -> dict:
    """
    逐行扫描存根文件，提取类名和方法完整签名。
    返回: {domain: {class_name: {method_name: signature_str}}}
    """
    domain_db = defaultdict(lambda: defaultdict(dict))

    class_pattern = re.compile(r"^class (\w+)(?:\(([^)]*)\))?:")
    # 类内方法：使用贪婪匹配处理参数中的方括号
    # 例如: def foo(self, type: Union[Class, type] = Object.static_class()) -> Optional[Class]:
    method_pattern = re.compile(r"^\s+def (\w+)\((.*)\)(?:\s*->\s*(.+?))?:\s*$")
    # 模块顶层函数（无缩进）
    toplevel_pattern = re.compile(r"^def (\w+)\((.*)\)(?:\s*->\s*(.+?))?:\s*$")

    current_class = None
    current_domain = None
    current_bases = ""

    # 顶层函数归入特殊伪类 "_module_functions_"
    MODULE_FUNCS_KEY = "_module_functions_"
    domain_db["core_misc"][MODULE_FUNCS_KEY] = {"__bases__": ""}

    with open(stub_path, "r", encoding="utf-8") as f:
        for line in f:
            # 检测类定义
            class_match = class_pattern.match(line)
            if class_match:
                current_class = class_match.group(1)
                current_bases = class_match.group(2) or ""
                current_domain = get_domain(current_class)
                # 记录类本身（即使没有方法也保留）
                if current_class not in domain_db[current_domain]:
                    domain_db[current_domain][current_class] = {
                        "__bases__": current_bases,
                    }
                continue

            # 检测顶层函数（非缩进的 def）
            toplevel_match = toplevel_pattern.match(line)
            if toplevel_match:
                current_class = None  # 离开任何类上下文
                func_name = toplevel_match.group(1)
                raw_sig = toplevel_match.group(2)
                return_type = toplevel_match.group(3)

                if func_name.startswith("_"):
                    continue

                sig = f"{func_name}({raw_sig})"
                if return_type:
                    sig += f" -> {return_type.strip()}"

                domain_db["core_misc"][MODULE_FUNCS_KEY][func_name] = sig
                continue

            # 检测类内方法定义
            if current_class:
                def_match = method_pattern.match(line)
                if def_match:
                    method_name = def_match.group(1)
                    raw_sig = def_match.group(2)
                    return_type = def_match.group(3)

                    # 跳过私有方法（但保留 __init__）
                    if method_name.startswith("_") and method_name != "__init__":
                        continue

                    # 清理 self/cls 参数
                    clean_sig = re.sub(r"^\s*(?:self|cls)\s*,?\s*", "", raw_sig)

                    # 组装完整签名
                    sig = f"{method_name}({clean_sig})"
                    if return_type:
                        sig += f" -> {return_type.strip()}"

                    domain_db[current_domain][current_class][method_name] = sig

    return dict(domain_db)


def write_module_md(domain: str, classes: dict, output_dir: str) -> dict:
    """将单个领域的 API 写入 Markdown 文件。返回统计信息。"""
    md_path = os.path.join(output_dir, f"{domain}.md")
    class_count = 0
    method_count = 0

    MODULE_FUNCS_KEY = "_module_functions_"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Unreal Python API — {domain.replace('_', ' ').title()}\n\n")
        f.write(
            "> Auto-generated from PythonStub. "
            "AI must use these exact signatures for the current UE version.\n\n"
        )

        # 先输出顶层模块函数（如果有）
        if MODULE_FUNCS_KEY in classes:
            funcs = {k: v for k, v in classes[MODULE_FUNCS_KEY].items() if k != "__bases__"}
            if funcs:
                f.write("## Module-Level Functions\n\n")
                f.write("```python\n")
                for fn_name in sorted(funcs.keys()):
                    sig = funcs[fn_name]
                    f.write(f"unreal.{sig}\n")
                    method_count += 1
                f.write("```\n\n")

        for cls_name in sorted(classes.keys()):
            if cls_name == MODULE_FUNCS_KEY:
                continue

            methods = classes[cls_name]
            bases = methods.pop("__bases__", "")

            # 只输出有公开方法的类
            public_methods = {k: v for k, v in methods.items() if k != "__bases__"}
            if not public_methods:
                continue

            class_count += 1
            base_str = f"({bases})" if bases else ""
            f.write(f"## `unreal.{cls_name}{base_str}`\n\n")
            f.write("```python\n")

            for m_name in sorted(public_methods.keys()):
                sig = public_methods[m_name]
                f.write(f"unreal.{cls_name}.{sig}\n")
                method_count += 1

            f.write("```\n\n")

    return {"file": f"{domain}.md", "classes": class_count, "methods": method_count}


def write_stats(stats: list, output_dir: str):
    """写入统计摘要 JSON，供 SKILL.md 路由表参考。"""
    stats_path = os.path.join(output_dir, "_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(
            {"generated_modules": stats, "total_modules": len(stats)},
            f,
            indent=2,
            ensure_ascii=False,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Split UE PythonStub into domain-specific Markdown files for AI context injection."
    )
    parser.add_argument("stub_path", help="Path to unreal.py stub file")
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(__file__), "..", "modules"),
        help="Output directory for generated .md files (default: ../modules/)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.stub_path):
        print(f"Error: Stub file not found: {args.stub_path}")
        return 1

    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Parsing stub: {args.stub_path}")
    print(f"Output dir:   {args.output_dir}")

    domain_db = parse_stub(args.stub_path)

    all_stats = []
    total_classes = 0
    total_methods = 0

    for domain in sorted(domain_db.keys()):
        classes = domain_db[domain]
        stat = write_module_md(domain, classes, args.output_dir)
        all_stats.append(stat)
        total_classes += stat["classes"]
        total_methods += stat["methods"]
        print(f"  {stat['file']:30s}  {stat['classes']:>5d} classes  {stat['methods']:>6d} methods")

    write_stats(all_stats, args.output_dir)

    print(f"\nDone! {len(all_stats)} modules, {total_classes} classes, {total_methods} methods.")
    print(f"Stats written to: {os.path.join(args.output_dir, '_stats.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
