import os
import json

LOG_DIR = "generated/decision_logs"

def load_events():
    events = []
    if not os.path.exists(LOG_DIR):
        return events

    for f in os.listdir(LOG_DIR):
        path = os.path.join(LOG_DIR, f)
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                events.append(json.loads(line))
    return events
