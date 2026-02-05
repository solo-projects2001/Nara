def assess_uncertainty(structure: dict) -> float:
    score = 0.0
    if len(structure.get("components", [])) > 3:
        score += 0.4
    if structure.get("system_type") == "multi_component":
        score += 0.3
    return min(score, 1.0)
