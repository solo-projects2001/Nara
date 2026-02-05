def serialize_freeze(record) -> dict:
    return {
        "version": record.version,
        "reason": record.reason,
        "frozen_at": record.frozen_at,
        "confidence": record.confidence,
    }
