# nara/core/provenance.py
"""
Artifact Provenance Layer

Enterprise invariant:
- Every generated file has metadata trace
"""

import hashlib
import json
import os
from datetime import datetime


def file_hash(path: str) -> str:
    data = open(path, "rb").read()
    return hashlib.sha256(data).hexdigest()[:16]


def write_meta(path: str, role: str, intent: str):
    meta = {
        "role": role,
        "intent": intent,
        "generated_at": datetime.utcnow().isoformat(),
        "hash": file_hash(path),
    }

    with open(path + ".meta.json", "w") as f:
        json.dump(meta, f, indent=2)
