import json
from datetime import datetime

def record(path: str, data: dict):
    data["time"] = datetime.utcnow().isoformat()
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")
