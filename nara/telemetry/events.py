import json
import os
from datetime import datetime

def log(event: str, payload: dict, path: str):
    record = {
        "time": datetime.utcnow().isoformat(),
        "event": event,
        "payload": payload
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")
