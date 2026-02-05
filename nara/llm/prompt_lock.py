PROMPT_LOCK = {}

# nara/llm/prompt_lock.py
"""
Enterprise Prompt Lock

Goal:
- Detect prompt drift (auditability)
- Never hard-crash regression runs
- Auto-update lock in dev mode
"""

import os
import json
import hashlib


LOCK_DIR = os.path.join("nara", "llm", "locks")
os.makedirs(LOCK_DIR, exist_ok=True)


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def lock(name: str, prompt_hash: str):
    """
    If prompt changed:
    - log warning
    - update lock file
    """

    lock_path = os.path.join(LOCK_DIR, f"{name}.json")

    if not os.path.exists(lock_path):
        with open(lock_path, "w") as f:
            json.dump({"hash": prompt_hash}, f, indent=2)
        return

    with open(lock_path, "r") as f:
        old = json.load(f).get("hash")

    if old != prompt_hash:
        print(f"[PROMPT WARNING] Prompt changed for '{name}'. Updating lock.")
        with open(lock_path, "w") as wf:
            json.dump({"hash": prompt_hash}, wf, indent=2)
        return
