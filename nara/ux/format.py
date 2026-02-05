def format_result(result: dict) -> str:
    status = result.get("status")

    if status == "success":
        return "✔ SUCCESS — system generated and validated"

    if status == "rejected":
        return f"✖ REJECTED — {result.get('reason')}"

    if status == "stopped":
        return f"⏸ STOPPED — {result.get('reason')}"

    return str(result)
