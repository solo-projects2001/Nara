from dataclasses import dataclass
from nara.hybrid.phases import HybridPhase

@dataclass
class HybridPlan:
    phases: list[HybridPhase]
    reason: str
