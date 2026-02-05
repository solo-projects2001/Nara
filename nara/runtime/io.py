# nara/runtime/io.py
"""
Generated-system IO helpers.

Enterprise invariant:
- All outputs go to /out
- No hidden state
"""

import json
import os


def ensure_out():
    os.makedirs("out", exist_ok=True)


def write_json(name: str, data: dict):
    ensure_out()
    path = os.path.join("out", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return path
