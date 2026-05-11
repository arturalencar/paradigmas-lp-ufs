from typing import cast

from expression.exp_binaria import ExpBinaria
from expression.valor_inteiro import ValorInteiro
from expression.expressao import Expressao
from util.tipo import Tipo

class ExpSub(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "-")

    def avaliar(self):
        esq_val = self._esq.avaliar()
        dir_val = self._dir.avaliar()
        return ValorInteiro(esq_val.valor - dir_val.valor);
    
    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo().e_inteiro() and self._dir.get_tipo().e_inteiro()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO