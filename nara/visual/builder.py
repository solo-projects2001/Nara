from nara.visual.graph import GraphNode, GraphEdge

def build_graph(structure: dict):
    nodes = []
    edges = []

    components = structure.get("components", [])

    for i, c in enumerate(components):
        name = c.get("name") or c.get("entrypoint") or f"component_{i}"
        role = c.get("role", "unknown")

        nodes.append(GraphNode(name=name, role=role))

    for i in range(len(components) - 1):
        src = components[i]
        dst = components[i + 1]

        src_name = src.get("name") or src.get("entrypoint") or f"component_{i}"
        dst_name = dst.get("name") or dst.get("entrypoint") or f"component_{i+1}"

        edges.append(
            GraphEdge(
                source=src_name,
                target=dst_name,
                label="flow",
            )
        )

    return nodes, edges
