from dataclasses import dataclass
from nara.epistemic.confidence import DecisionConfidence
from nara.memory.stats import failure_stats

@dataclass
class EpistemicState:
    confidence: DecisionConfidence
    ambiguities: list[str]

    def safe_to_proceed(self) -> bool:
        stats = failure_stats()
        if stats:
            most_common, count = stats.most_common(1)[0]
            if count > 5:
                return False
        return self.confidence.acceptable() and not self.ambiguities
