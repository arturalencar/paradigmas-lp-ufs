from abc import ABC, abstractmethod
from expression.expressao import Expressao

class ExpBinaria(Expressao, ABC):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self.esq = esq
        self.dir = dir
        self.operador = operador

    def getEsq(self) -> Expressao:
        return self.esq

    def getDir(self) -> Expressao:
        return self.dir

    def getOperador(self) -> str:
        return self.operador

    def __str__(self):
        return f"{self.esq} {self.operador} {self.dir}"

    def checaTipo(self, amb) -> bool:
        if not self.getEsq().checaTipo(amb) or not self.getDir().checaTipo(amb):
            return False
        return self.checaTipoElementoTerminal(amb)

    @abstractmethod
    def checaTipoElementoTerminal(self, amb) -> bool:
        pass

    def reduzir(self, ambiente) -> Expressao:
        self.esq = self.esq.reduzir(ambiente)
        self.dir = self.dir.reduzir(ambiente)
        return self

    @abstractmethod
    def clone(self) -> 'ExpBinaria':
        pass
