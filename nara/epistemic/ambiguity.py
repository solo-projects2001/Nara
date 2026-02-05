AMBIGUOUS_KEYWORDS = {
    "secure",
    "efficient",
    "scalable",
    "robust",
    "intelligent",
    "optimize",
}

def detect_ambiguity(intent: str) -> list[str]:
    found = []
    low = intent.lower()
    for k in AMBIGUOUS_KEYWORDS:
        if k in low:
            found.append(k)
    return found
