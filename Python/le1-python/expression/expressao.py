from abc import ABC, abstractmethod
from util.tipo import Tipo
from valor import Valor

class Expressao(ABC):
    @abstractmethod
    def avaliar(self) -> Valor:
        pass
    
    @abstractmethod
    def checa_tipo(self) -> bool:
        pass
    
    @abstractmethod
    def get_tipo(self) -> Tipo:
        pass