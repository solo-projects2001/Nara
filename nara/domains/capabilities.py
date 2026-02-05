import json
import os

CAP_PATH = os.path.join(
    os.path.dirname(__file__),
    "capabilities.json"
)

with open(CAP_PATH, "r", encoding="utf-8") as f:
    CAPABILITIES = json.load(f)

def domain_capable(domain: str, feature: str) -> bool:
    if domain not in CAPABILITIES:
        return False
    info = CAPABILITIES[domain]
    return info.get("enabled", False) and feature in info.get("features", [])
