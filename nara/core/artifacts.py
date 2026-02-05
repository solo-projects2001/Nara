# nara/core/artifacts.py
"""
Enterprise Artifact Generator (Final GEN)

Guarantees:
- Role-aware real skeletons (not print stubs)
- Deterministic proof artifacts always emitted
- Main pipeline orchestrator always present
"""

import os
import json
from datetime import datetime

from nara.generation.decomposer import decompose
from nara.generation.templates import TEMPLATES


def _write_json(path: str, obj: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)


def generate_artifacts(structure: dict):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    root = os.path.join("generated", "projects", ts)

    workspace = os.path.join(root, "workspace")
    design = os.path.join(root, "design")

    os.makedirs(workspace, exist_ok=True)
    os.makedirs(design, exist_ok=True)

    # --- Decompose into domain-real components ---
    components = decompose(structure)
    structure["components"] = components

    # --- Deterministic proof artifacts ---
    pipeline = {
        "nodes": [{"id": c["name"], "role": c["role"]} for c in components],
        "edges": [[components[i - 1]["name"], components[i]["name"]]
                  for i in range(1, len(components))],
    }

    contracts = {c["name"]: c["contracts"] for c in components}

    system_spec = {
        "intent": structure["_intent"]["raw"]
        if isinstance(structure["_intent"], dict)
        else str(structure["_intent"]),
        "blueprint": structure["_system"]["blueprint"],
        "domain": structure["_domain"]["domain"],
        "components": [c["name"] for c in components],
    }

    _write_json(os.path.join(design, "pipeline.json"), pipeline)
    _write_json(os.path.join(design, "contracts.json"), contracts)
    _write_json(os.path.join(design, "system_spec.json"), system_spec)

    # --- Generate role-aware component files ---
    file_map = {}

    for c in components:
        role = c["role"]
        code = TEMPLATES.get(role)

        if not code:
            code = f"""\
def run(data: dict) -> dict:
    return data
"""

        path = os.path.join(workspace, c["entrypoint"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)

        file_map[c["entrypoint"]] = c["entrypoint"]

    # --- Deterministic main orchestrator ---
    main_lines = ["data = {}"]
    for c in components:
        mod = c["entrypoint"].replace(".py", "")
        main_lines.append(f"from {mod} import run as {c['name']}")
    main_lines.append("")
    for c in components:
        main_lines.append(f"data = {c['name']}(data)")
    main_lines.append('print("PIPELINE_OK", data)')

    with open(os.path.join(workspace, "main.py"), "w") as f:
        f.write("\n".join(main_lines))

    file_map["main.py"] = "main.py"

    # --- Enterprise README ---
    with open(os.path.join(root, "README.md"), "w") as f:
        f.write(
            "# Generated System (Nara)\n\n"
            "Deterministic proof:\n"
            "- design/pipeline.json\n"
            "- design/contracts.json\n"
            "- design/system_spec.json\n\n"
            "Run:\n"
            "```bash\n"
            "python workspace/main.py\n"
            "```\n"
        )

    return {
        "root": root,
        "files": file_map,
        "domain": structure["_domain"],
        "graph": pipeline,
    }
