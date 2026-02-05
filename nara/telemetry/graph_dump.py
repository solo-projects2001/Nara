import json

def dump(graph: dict, path: str):
    with open(path, "w") as f:
        json.dump(graph, f, indent=2)
