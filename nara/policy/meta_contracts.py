ALLOWED_REPAIRS = {"syntax_error", "runtime_error"}
ALLOWED_ESCALATIONS = {"env_missing"}

def validate_decision(action: str, context: dict):
    if action == "repair":
        if context["failure_type"] not in ALLOWED_REPAIRS:
            raise RuntimeError("meta_contract_violation: invalid_repair")
    if action == "escalate":
        if context["failure_type"] not in ALLOWED_ESCALATIONS:
            raise RuntimeError("meta_contract_violation: invalid_escalation")
