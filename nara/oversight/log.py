import json, os
from datetime import datetime

LOG_DIR = "generated/decision_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_decision(stage: str, payload: dict):
    record = {
        "ts": datetime.utcnow().isoformat(),
        "stage": stage,
        "payload": payload,
    }

    path = os.path.join(LOG_DIR, "trace.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
