# nara/ux/governance/approval.py
import json
import os
from datetime import datetime

QUEUE = "generated/approvals"
os.makedirs(QUEUE, exist_ok=True)

def request_approval(intent: str, reason: str):
    rec = {
        "intent": intent,
        "reason": reason,
        "ts": datetime.utcnow().isoformat(),
        "status": "pending",
    }
    path = os.path.join(QUEUE, f"{int(datetime.utcnow().timestamp())}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2)
    return path

def list_requests():
    reqs = []
    for f in os.listdir(QUEUE):
        with open(os.path.join(QUEUE, f), "r", encoding="utf-8") as fh:
            reqs.append(json.load(fh))
    return reqs
