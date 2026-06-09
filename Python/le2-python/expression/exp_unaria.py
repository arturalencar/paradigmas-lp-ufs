from abc import ABC, abstractmethod


class ExpUnaria(ABC):

    def __init__(self, exp, operador: str):
        self._exp = exp
        self._operador = operador

    @property
    def exp(self):

        return self._exp

    @property
    def operador(self) -> str:

        return self._operador

    def checa_tipo(self, amb) -> bool:

        return self.exp.checa_tipo(amb) and self._checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def _checa_tipo_elemento_terminal(self, amb) -> bool:

        pass
