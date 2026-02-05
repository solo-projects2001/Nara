from abc import ABC, abstractmethod

class DomainValidator(ABC):
    @abstractmethod
    def validate(self, result: dict):
        pass
