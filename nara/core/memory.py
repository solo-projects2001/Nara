import json, os

BASE = "generated/projects/demo/memory.json"

def remember(key: str, value: dict):
    os.makedirs(os.path.dirname(BASE), exist_ok=True)
    data = {}
    if os.path.exists(BASE):
        with open(BASE) as f:
            data = json.load(f)
    data[key] = value
    with open(BASE, "w") as f:
        json.dump(data, f, indent=2)
