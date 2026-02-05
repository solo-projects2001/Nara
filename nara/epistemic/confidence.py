from dataclasses import dataclass

@dataclass
class DecisionConfidence:
    value: float  # 0.0 – 1.0
    reason: str

    def acceptable(self, threshold: float = 0.6) -> bool:
        return self.value >= threshold
