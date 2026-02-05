FORBIDDEN_KEYWORDS = {
    "limitless",
    "forever",
    "never stop",
    "autonomous agents",
    "self improving",
    "without bounds",
}

META_VIOLATIONS = [
    "directly answers",
    "answer user questions",
    "chatbot"
]


def violates_rules(intent: str) -> str | None:
    low = intent.lower()
    for k in FORBIDDEN_KEYWORDS:
        if k in low:
            return k
    return None
