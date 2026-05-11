from abc import ABC, abstractmethod
from util.tipo import Tipo
class Expressao(ABC):
    @abstractmethod
    def avaliar(self) : 
        pass
    
    @abstractmethod
    def checa_tipo(self) -> bool:
        pass
    
    @abstractmethod
    def get_tipo(self) -> Tipo:
        pass