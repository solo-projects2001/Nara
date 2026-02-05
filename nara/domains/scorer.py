from abc import ABC, abstractmethod
from nara.domains.confidence import DomainMatch

class DomainScorer(ABC):
    @abstractmethod
    def score(self, intent: str) -> DomainMatch | None:
        pass
