def default_contract():
    """
    Enterprise invariant:
    Contracts must always be JSON-serializable.
    No Python objects, no dataclasses, no hidden state.
    """
    return {
        "input": "json",
        "output": "json",
        "constraints": {
            "deterministic": True,
            "offline_only": True,
            "sandboxed": True,
        },
    }
