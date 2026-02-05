# nara/core/intent_guard.py
"""
Enterprise Intent Guard

Invariant:
- Blocks only explicitly forbidden meta-intents
- Never blocks normal engineering/system design intents
- Deterministic, offline, no LLM calls
"""

class IntentRejected(Exception):
    pass


FORBIDDEN_PATTERNS = [
    "forever",
    "general intelligence",
    "self improve endlessly",
    "become conscious",
    "infinite loop of improvement",
]


def guard_intent(raw_intent: str):
    """
    Raise IntentRejected only for forbidden patterns.
    """
    low = raw_intent.strip().lower()

    for pat in FORBIDDEN_PATTERNS:
        if pat in low:
            raise IntentRejected(f"forbidden_intent: {pat}")

    return True
