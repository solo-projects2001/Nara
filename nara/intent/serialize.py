def serialize_intent_classification(cls) -> dict:
    return {
        "kind": cls.kind.value,
        "reason": cls.reason,
        "confidence": cls.confidence,
    }
