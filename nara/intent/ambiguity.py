AMBIGUOUS_TERMS = [
    "secure",
    "efficient",
    "robust",
    "intelligent",
    "optimize",
    "scalable",
]

def detect_ambiguity(intent: str) -> list[str]:
    low = intent.lower()
    return [t for t in AMBIGUOUS_TERMS if t in low]
