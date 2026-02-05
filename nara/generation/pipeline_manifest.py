# nara/generation/pipeline_manifest.py
"""
Writes deterministic pipeline + contract proof artifacts.
"""

import json
import os


def write_pipeline(root: str, components: list):
    design_dir = os.path.join(root, "design")
    os.makedirs(design_dir, exist_ok=True)

    nodes = []
    edges = []
    contracts = {}

    # Linear deterministic ordering for now
    for i, c in enumerate(components):
        nodes.append({"id": c["name"], "role": c["role"]})
        contracts[c["name"]] = c.get("contracts", {})

        if i > 0:
            edges.append([components[i - 1]["name"], c["name"]])

    with open(os.path.join(design_dir, "pipeline.json"), "w") as f:
        json.dump({"nodes": nodes, "edges": edges}, f, indent=2)

    with open(os.path.join(design_dir, "contracts.json"), "w") as f:
        json.dump(contracts, f, indent=2)
