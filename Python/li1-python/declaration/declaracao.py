from abc import ABC, abstractmethod

class Declaracao(ABC):
    @abstractmethod
    def elabora(self, ambiente):
        pass

    @abstractmethod
    def checaTipo(self, ambiente) -> bool:
        pass
