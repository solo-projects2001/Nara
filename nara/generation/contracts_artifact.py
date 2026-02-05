# nara/generation/contracts_artifact.py
import json
import os

def write_contracts(root: str, components: list):
    path = os.path.join(root, "design", "contracts.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            {"contracts": [c["schema"] for c in components]},
            f,
            indent=2,
        )
