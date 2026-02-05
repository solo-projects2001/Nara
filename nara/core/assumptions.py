def detect_invalid_assumption(result: dict) -> bool:
    stderr = result["stderr"]
    signals = [
        "TypeError",
        "AttributeError",
        "NoneType",
        "unexpected"
    ]
    return any(s in stderr for s in signals)
