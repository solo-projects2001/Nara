def serialize_hybrid_plan(plan) -> dict:
    return {
        "phases": [p.value for p in plan.phases],
        "reason": plan.reason,
    }
