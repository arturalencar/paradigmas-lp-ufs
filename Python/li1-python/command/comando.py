from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, ambiente):
        pass

    @abstractmethod
    def checaTipo(self, ambiente) -> bool:
        pass
