from abc import ABC, abstractmethod

class DomainAnalyzer(ABC):
    @abstractmethod
    def analyze(self, path: str) -> dict:
        pass
