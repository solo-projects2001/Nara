# nara/runtime/logging.py
"""
Generated-system runtime logging.

Enterprise invariant:
- Structured events, not random prints
- Human-auditable
"""

import json
import time


def log_event(event: str, payload: dict = None):
    record = {
        "ts": time.time(),
        "event": event,
        "payload": payload or {},
    }
    print(json.dumps(record))
