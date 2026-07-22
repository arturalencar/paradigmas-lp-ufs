from abc import ABC, abstractmethod

class Expressao(ABC):
    @abstractmethod
    def avaliar(self, amb):
        pass

    @abstractmethod
    def checaTipo(self, amb) -> bool:
        pass

    @abstractmethod
    def getTipo(self, amb):
        pass

    @abstractmethod
    def reduzir(self, ambiente) -> 'Expressao':
        pass

    @abstractmethod
    def clone(self) -> 'Expressao':
        pass
