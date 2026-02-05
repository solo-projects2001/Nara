import json

def load_run(history_path: str):
    with open(history_path) as f:
        return [json.loads(line) for line in f]

def replay(history_path: str):
    return load_run(history_path)

# nara/core/replay.py
"""
Deterministic Replay Layer

Goal:
- Same intent + same version → same run signature
- Enables enterprise reproducibility
"""

import hashlib


def intent_signature(intent: str, version: str = "v1") -> str:
    raw = (version + "::" + intent.strip()).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def run_id(intent: str, version: str = "v1") -> str:
    """
    Stable run folder id.
    """
    return f"{version}_{intent_signature(intent, version)}"
