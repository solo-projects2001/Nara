# nara/ux/freeze/viewer.py
import json
import os

BASE = "generated/projects"

def list_freezes():
    out = []
    if not os.path.isdir(BASE):
        return out
    for r in os.listdir(BASE):
        path = os.path.join(BASE, r, "FREEZE.json")
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                out.append({"run": r, **json.load(f)})
    return out
