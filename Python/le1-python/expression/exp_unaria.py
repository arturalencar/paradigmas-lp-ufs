from abc import ABC, abstractmethod
from typing import Any
from .expressao import Expressao
from .valor_inteiro import ValorInteiro
from .valor_booleano import ValorBooleano
from util.tipo import Tipo

# ExpUnaria.java
class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    @property
    def exp(self) -> Expressao:
        return self._exp

    def __str__(self) -> str:
        return f"{self._operador} {self._exp}"

    def checa_tipo(self) -> bool:
        return self._exp.checa_tipo() and self._checa_tipo_elemento_terminal()

    @abstractmethod
    def _checa_tipo_elemento_terminal(self) -> bool:
        pass
