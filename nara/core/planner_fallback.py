def simplify(structure: dict) -> dict:
    if len(structure["components"]) > 1:
        structure["components"] = structure["components"][:1]
        structure["system_type"] = "python_script"
    return structure
