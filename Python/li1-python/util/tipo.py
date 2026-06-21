from abc import ABC, abstractmethod

class Tipo(ABC):
    @abstractmethod
    def getNome(self) -> str:
        pass

    @abstractmethod
    def eInteiro(self) -> bool:
        pass

    @abstractmethod
    def eBooleano(self) -> bool:
        pass

    @abstractmethod
    def eString(self) -> bool:
        pass

    @abstractmethod
    def eIgual(self, tipo: 'Tipo') -> bool:
        pass

    @abstractmethod
    def eValido(self) -> bool:
        pass

    @abstractmethod
    def intersecao(self, outroTipo: 'Tipo') -> 'Tipo':
        pass
