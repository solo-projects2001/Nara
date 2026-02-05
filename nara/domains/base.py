from abc import ABC, abstractmethod

class ExecutionDomain(ABC):
    name: str
    subdomains: list[str]

    @abstractmethod
    def detect(self, intent: str) -> bool:
        pass

    @abstractmethod
    def select_subdomain(self, intent: str) -> str:
        pass

    @abstractmethod
    def runner(self, subdomain: str) -> str:
        pass

    @abstractmethod
    def validator(self):
        pass

    @abstractmethod
    def repair_strategy(self):
        pass
