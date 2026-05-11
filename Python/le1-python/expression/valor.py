from typing import TypeVar, Generic, Any
from abc import ABC, abstractmethod
from .expressao import Expressao

# Valor.java (Interface pura vira uma classe base ou Protocol)
class Valor(Expressao, ABC):
    @property
    @abstractmethod
    def valor(self) -> Any:
        """Todo valor concreto deve implementar esta propriedade"""
        pass
    
    @abstractmethod
    def is_equals(self, outro: 'Valor') -> bool:
        pass
