from abc import ABC, abstractmethod
from expression.expressao import Expressao

class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str):
        self.exp = exp
        self.operador = operador

    def getExp(self) -> Expressao:
        return self.exp

    def getOperador(self) -> str:
        return self.operador

    def checaTipo(self, amb) -> bool:
        return self.getExp().checaTipo(amb) and self.checaTipoElementoTerminal(amb)

    def __str__(self):
        return f"{self.operador} {self.exp}"

    @abstractmethod
    def checaTipoElementoTerminal(self, amb) -> bool:
        pass

    def reduzir(self, ambiente) -> Expressao:
        self.exp = self.exp.reduzir(ambiente)
        return self

    @abstractmethod
    def clone(self) -> 'ExpUnaria':
        pass
