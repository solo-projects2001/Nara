def classify_meta(structure: dict, failures: int) -> str:
    if failures == 0:
        return "ok"
    if failures > 1 and len(structure["components"]) == 1:
        return "overfitting_repair"
    if failures > 0 and structure["system_type"] == "python_script":
        return "bad_structure_choice"
    return "unknown_meta_failure"
