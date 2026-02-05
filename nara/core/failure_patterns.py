import json, os

BASE = "generated/failure_patterns.json"

def record(failure_type: str):
    data = {}
    if os.path.exists(BASE):
        with open(BASE) as f:
            data = json.load(f)
    data[failure_type] = data.get(failure_type, 0) + 1
    with open(BASE, "w") as f:
        json.dump(data, f, indent=2)
