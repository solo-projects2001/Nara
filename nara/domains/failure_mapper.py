from nara.domains.failures import DOMAIN_FAILURES

def map_failure(domain: str, raw: dict) -> dict:
    stderr = raw.get("stderr", "")
    exit_code = raw.get("exit_code", 0)

    if domain == "interpreted":
        if "SyntaxError" in stderr:
            return {"type": "syntax_error"}
        if "ModuleNotFoundError" in stderr:
            return {"type": "module_not_found"}
        if exit_code != 0:
            return {"type": "runtime_error"}

    if domain == "compiled":
        if "error:" in stderr:
            return {"type": "compile_error"}
        if exit_code != 0:
            return {"type": "runtime_error"}

    if domain == "shell":
        if "not found" in stderr:
            return {"type": "command_not_found"}
        if exit_code != 0:
            return {"type": "nonzero_exit"}

    if domain == "data":
        if exit_code != 0:
            return {"type": "query_error"}
        if not raw.get("stdout"):
            return {"type": "empty_result"}

    return {"type": "unknown"}
