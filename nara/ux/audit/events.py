# nara/ux/audit/events.py
import os, json
from datetime import datetime

LOG_DIR = "generated/decision_logs"

def load_events(limit=500):
    events = []
    if not os.path.isdir(LOG_DIR):
        return events
    for fname in sorted(os.listdir(LOG_DIR)):
        path = os.path.join(LOG_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    rec["_source"] = fname
                    events.append(rec)
                except Exception:
                    continue
    return events[-limit:]
