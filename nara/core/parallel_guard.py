def can_parallelize(graph: dict) -> bool:
    return all(len(v["deps"]) == 0 for v in graph.values())
