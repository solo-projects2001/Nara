# nara/core/dag/validate.py
def validate_dag(nodes):
    ids = {n.id for n in nodes}

    for n in nodes:
        for dep in n.depends_on:
            if dep not in ids:
                raise RuntimeError(f"dag_invalid_dependency: {dep}")

    return True
