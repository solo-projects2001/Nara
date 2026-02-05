from datetime import datetime
from nara.freeze.model import FreezeRecord

def generate_freeze(version: str, confidence: float, reason: str) -> FreezeRecord:
    return FreezeRecord(
        version=version,
        reason=reason,
        frozen_at=datetime.utcnow().isoformat(),
        confidence=confidence,
    )
