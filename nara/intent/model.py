from dataclasses import dataclass
from enum import Enum

class IntentKind(str, Enum):
    FORBIDDEN = "forbidden"
    AMBIGUOUS = "ambiguous"
    ANALYSIS = "analysis"
    EXECUTABLE = "executable"
    HYBRID = "hybrid"

@dataclass
class IntentClassification:
    kind: IntentKind
    reason: str
    confidence: float
