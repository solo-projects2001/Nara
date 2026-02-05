import json

def export(run_id: str, src: str, dst: str):
    with open(src) as f:
        lines = f.readlines()

    graph = {
        "run_id": run_id,
        "nodes": [],
        "edges": []
    }

    for l in lines:
        obj = json.loads(l)
        if "id" in obj:
            graph["nodes"].append(obj)
        if "edge" in obj:
            graph["edges"].append(obj)

    with open(dst, "w") as f:
        json.dump(graph, f, indent=2)
