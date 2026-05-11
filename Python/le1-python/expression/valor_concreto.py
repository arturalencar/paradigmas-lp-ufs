from typing import TypeVar, Generic, Any
from abc import ABC
from expression.valor import Valor

# T representa o tipo interno (int, str, bool)
T = TypeVar('T')

class ValorConcreto(Valor, Generic[T], ABC):
    def __init__(self, valor: T):
        self._valor = valor

    @property
    def valor(self) -> T:
        """Retorna o valor bruto encapsulado."""
        return self._valor

    def avaliar(self) -> Valor:
        """Auto-avaliação: um valor avalia para si mesmo."""
        return self

    def checa_tipo(self) -> bool:
        """Valores concretos são sempre consistentes em termos de tipo."""
        return True

    def is_equals(self, outro: Any) -> bool:
        if hasattr(outro, 'valor'):
            return self.valor == outro.valor
        return False

    def __str__(self) -> str:
        return str(self._valor)
