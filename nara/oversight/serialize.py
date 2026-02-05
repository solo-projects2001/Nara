def make_json_safe(obj):
    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    if hasattr(obj, "__dict__"):
        return {
            "__type__": obj.__class__.__name__,
            **{
                k: make_json_safe(v)
                for k, v in obj.__dict__.items()
                if not callable(v)
            }
        }

    if callable(obj):
        return "<callable>"

    return obj
