# nara/core/dag/builder.py
from nara.core.dag.schema import DAGNode

def build_dag(components: list):
    """
    GEN-5: Real DAG (not linear only).
    Default: fan-in reporter depends on all others.
    """
    nodes = []

    if not components:
        return nodes

    if len(components) == 1:
        c = components[0]
        return [DAGNode(id=c["name"], entrypoint=c["entrypoint"], depends_on=[])]

    # all except last are independent
    for c in components[:-1]:
        nodes.append(
            DAGNode(
                id=c["name"],
                entrypoint=c["entrypoint"],
                depends_on=[],
            )
        )

    # last depends on all previous
    last = components[-1]
    nodes.append(
        DAGNode(
            id=last["name"],
            entrypoint=last["entrypoint"],
            depends_on=[c["name"] for c in components[:-1]],
        )
    )

    return nodes
