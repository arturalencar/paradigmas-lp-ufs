from typing import TypeVar, Generic
from expression.valor import Valor

T = TypeVar('T')

class ValorConcreto(Valor, Generic[T]):
    def __init__(self, valor: T):
        self._valor = valor

    def __str__(self):
        return str(self._valor)

    def valor(self) -> T:
        return self._valor

    def isEquals(self, obj: 'ValorConcreto[T]') -> bool:
        return self.valor() == obj.valor()

    def avaliar(self, amb) -> Valor:
        return self

    def checaTipo(self, amb) -> bool:
        return True

    def __hash__(self):
        return hash(self._valor)

    def __eq__(self, obj):
        if self is obj:
            return True
        if obj is None or not isinstance(obj, ValorConcreto):
            return False
        return self._valor == obj._valor

    def reduzir(self, ambiente) -> 'Valor':
        return self

    def clone(self) -> 'ValorConcreto[T]':
        pass
