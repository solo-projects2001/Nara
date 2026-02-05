def should_stop(reason: str) -> bool:
    HARD_STOPS = {
        "meta_contract_violation",
        "budget_exhausted",
        "invalid_assumption"
    }
    return reason in HARD_STOPS
