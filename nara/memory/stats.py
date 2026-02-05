import json
from collections import Counter
from nara.memory.store import FAILURES, REPAIRS

def _load(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [json.loads(l) for l in f]
    except FileNotFoundError:
        return []

def failure_stats():
    data = _load(FAILURES)
    return Counter(d["failure_type"] for d in data)

def repair_stats():
    data = _load(REPAIRS)
    return Counter(
        (d["failure_type"], d["repaired"]) for d in data
    )
