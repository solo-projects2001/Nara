# nara/core/graph.py
"""
GEN5 Graph Builder (Validated DAG Plan)

- Produces executor_plan.json compatible DAG
- Default: fan-in final node depends on all previous
"""

def build_execution_graph(structure: dict):
    comps = structure.get("components", [])

    if not comps:
        return []

    if len(comps) == 1:
        c = comps[0]
        return [
            {"id": c["name"], "entrypoint": c["entrypoint"], "depends_on": []}
        ]

    nodes = []

    # Independent nodes
    for c in comps[:-1]:
        nodes.append(
            {"id": c["name"], "entrypoint": c["entrypoint"], "depends_on": []}
        )

    # Final node depends on all
    last = comps[-1]
    nodes.append(
        {
            "id": last["name"],
            "entrypoint": last["entrypoint"],
            "depends_on": [c["name"] for c in comps[:-1]],
        }
    )

    # Validate deps
    ids = {n["id"] for n in nodes}
    for n in nodes:
        for dep in n["depends_on"]:
            if dep not in ids:
                raise RuntimeError(f"dag_invalid_dependency: {dep}")

    return nodes
