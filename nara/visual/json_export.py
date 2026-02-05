def export_json(nodes, edges) -> dict:
    return {
        "nodes": [{"name": n.name, "role": n.role} for n in nodes],
        "edges": [
            {"from": e.source, "to": e.target, "label": e.label}
            for e in edges
        ],
    }
