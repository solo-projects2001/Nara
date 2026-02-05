FORBIDDEN_PATTERNS = [
    "forever",
    "self improve endlessly",
    "without stopping",
    "become perfect",
    "autonomous agent",
    "general intelligence",
]

def detect_forbidden(intent: str) -> bool:
    low = intent.lower()
    return any(p in low for p in FORBIDDEN_PATTERNS)
