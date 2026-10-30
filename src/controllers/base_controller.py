from abc import ABC, abstractmethod

class BaseController(ABC):
    @abstractmethod
    def can_handel(self, command: str) -> bool:
        pass
    
    @abstractmethod
    def execute(self, command: str) -> None:
        pass