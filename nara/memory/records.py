from dataclasses import dataclass
from datetime import datetime

@dataclass
class FailureRecord:
    intent: str
    domain: str
    failure_type: str
    timestamp: str

@dataclass
class RepairOutcome:
    failure_type: str
    repaired: bool
    timestamp: str
