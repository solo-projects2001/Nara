import json
import os

def write_domain_artifact(path: str, selection):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(selection.as_dict(), f, indent=2)
