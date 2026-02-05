def infer_dependencies(components):
    """
    Deterministic linear dependency graph.
    Always safe even if metadata is incomplete.
    """
    graph = []

    for i, c in enumerate(components):
        graph.append(
            {
                "id": i,
                "entrypoint": c["entrypoint"],
                "depends_on": i - 1 if i > 0 else None,
            }
        )

    return graph
