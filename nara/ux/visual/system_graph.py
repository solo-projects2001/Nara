# nara/ux/visual/system_graph.py
import json
import os

def load_graph(run_id):
    path = os.path.join("generated/projects", run_id, "design", "system_graph.json")
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
