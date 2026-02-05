from datetime import datetime

def explain_decision(stage: str, decision: dict) -> dict:
    return {
        "stage": stage,
        "decision": decision,
        "timestamp": datetime.utcnow().isoformat()
    }
