from abc import ABC, abstractmethod
from expression.expressao import Expressao

class ExpBinaria(Expressao):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self._esq = esq
        self._dir = dir
        self._operador = operador
        
    def __str__(self):
        return f"{self._esq} {self._operador} {self._dir}"
    
    def checa_tipo(self) -> bool:
        if not self._esq.checa_tipo() or not self._dir.checa_tipo():
            return False
        return self._checa_tipo_elemento_terminal()
        
    @abstractmethod
    def _checa_tipo_elemento_terminal(self) -> bool:
        """Método 'template' para subclasses."""
        pass