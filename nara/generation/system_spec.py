# nara/generation/system_spec.py
import json
import os


def write_system_spec(root: str, structure: dict):
    design_dir = os.path.join(root, "design")
    os.makedirs(design_dir, exist_ok=True)

    spec = {
        "intent": structure["_intent"]["raw"],
        "domain": structure["_domain"]["domain"],
        "blueprint": structure["_system"].get("blueprint"),
        "components": [c["name"] for c in structure.get("components", [])],
    }

    with open(os.path.join(design_dir, "system_spec.json"), "w") as f:
        json.dump(spec, f, indent=2)
