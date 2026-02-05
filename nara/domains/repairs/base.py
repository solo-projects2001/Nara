from abc import ABC, abstractmethod

class DomainRepair(ABC):
    @abstractmethod
    def repair(self, artifacts: dict, failure: dict) -> bool:
        pass
