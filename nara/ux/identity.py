NARA_IDENTITY = {
    "name": "Nara",
    "type": "Meta-System",
    "layer": "control",
    "purpose": [
        "Design systems",
        "Execute generated artifacts locally",
        "Detect failures",
        "Classify failure causes",
        "Apply targeted repairs",
    ],
    "explicit_non_goals": [
        "Solve end-user tasks directly",
        "Act as a chatbot",
        "Provide general intelligence",
        "Run autonomously without bounds",
    ],
    "guarantees": [
        "Deterministic",
        "Offline-only",
        "Auditable",
        "Enterprise-safe",
    ],
}

def describe() -> dict:
    return NARA_IDENTITY
