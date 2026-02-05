import hashlib
import json
import os

BASE = "generated/prompts"

def register(prompt_name: str, content: str) -> dict:
    h = hashlib.sha256(content.encode()).hexdigest()
    os.makedirs(BASE, exist_ok=True)
    path = os.path.join(BASE, f"{prompt_name}.json")
    data = {"hash": h, "content": content}
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return data
