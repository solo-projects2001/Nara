from abc import ABC, abstractmethod

class DomainRuntime(ABC):
    @abstractmethod
    def command(self, subdomain: str, entrypoint: str) -> list[str]:
        pass
