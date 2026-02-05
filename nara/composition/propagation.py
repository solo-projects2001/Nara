def propagate_failure(graph: dict, failed_node: str) -> list[str]:
    affected = []
    for node, deps in graph.items():
        if failed_node in deps:
            affected.append(node)
    return affected
