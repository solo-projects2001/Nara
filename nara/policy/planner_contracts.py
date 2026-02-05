MAX_COMPONENTS = 5
ALLOWED_SYSTEM_TYPES = {"python_script", "pipeline", "multi_component"}

def validate_plan(structure: dict):
    if structure["system_type"] not in ALLOWED_SYSTEM_TYPES:
        raise RuntimeError("planner_contract_violation: system_type")

    components = structure.get("components", [])
    if not components:
        raise RuntimeError("planner_contract_violation: no_components")

    if len(components) > MAX_COMPONENTS:
        raise RuntimeError("planner_contract_violation: too_many_components")
