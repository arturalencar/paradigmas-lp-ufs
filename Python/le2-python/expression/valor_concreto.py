from abc import ABC
from expressao import Expressao


class ValorConcreto(Expressao, ABC):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):

        return self._valor

    def is_equals(self, obj) -> bool:

        if isinstance(obj, ValorConcreto):
            return self.valor == obj.valor
        return False

    def avaliar(self, amb):

        return self

    def checa_tipo(self, amb) -> bool:

        return True

    def __str__(self) -> str:

        return str(self._valor)
