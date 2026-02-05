import json
import os

BASE = "generated/patterns.json"

def store(signature: str, structure: dict):
    data = {}
    if os.path.exists(BASE):
        with open(BASE) as f:
            data = json.load(f)
    data[signature] = structure
    with open(BASE, "w") as f:
        json.dump(data, f, indent=2)

def fetch(signature: str):
    if not os.path.exists(BASE):
        return None
    with open(BASE) as f:
        return json.load(f).get(signature)
