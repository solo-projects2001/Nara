from nara.core.planner_fallback import simplify

def meta_repair(structure: dict, meta_failure: str) -> dict:
    if meta_failure in {"bad_structure_choice", "planner_uncertainty"}:
        return simplify(structure)
    return structure
