def attribute(node: str, result: dict) -> dict:
    return {
        "component": node,
        "stderr": result["stderr"],
        "exit_code": result["exit_code"]
    }
