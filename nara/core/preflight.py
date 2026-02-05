from nara.core.static_analysis import analyze

def preflight(path: str):
    result = analyze(path)
    if not result["ok"]:
        raise RuntimeError("preflight_failed")
