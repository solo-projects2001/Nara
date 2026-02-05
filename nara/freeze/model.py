from dataclasses import dataclass
from datetime import datetime

@dataclass
class FreezeRecord:
    version: str
    reason: str
    frozen_at: str
    confidence: float
