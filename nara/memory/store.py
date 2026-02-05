import json
import os
from datetime import datetime
from nara.memory.records import FailureRecord, RepairOutcome

BASE = "generated/meta_memory"
FAILURES = os.path.join(BASE, "failures.jsonl")
REPAIRS = os.path.join(BASE, "repairs.jsonl")

os.makedirs(BASE, exist_ok=True)

def _append(path: str, obj: dict):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj) + "\n")

def record_failure(intent: str, domain: str, failure_type: str):
    rec = FailureRecord(
        intent=intent,
        domain=domain,
        failure_type=failure_type,
        timestamp=datetime.utcnow().isoformat()
    )
    _append(FAILURES, rec.__dict__)

def record_repair(failure_type: str, repaired: bool):
    rec = RepairOutcome(
        failure_type=failure_type,
        repaired=repaired,
        timestamp=datetime.utcnow().isoformat()
    )
    _append(REPAIRS, rec.__dict__)
