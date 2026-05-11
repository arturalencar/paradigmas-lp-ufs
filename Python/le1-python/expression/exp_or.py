from typing import cast

from expression.exp_binaria import ExpBinaria
from expression.valor_booleano import ValorBooleano
from expression.valor_string import ValorString
from expression.valor_inteiro import ValorInteiro  # Para suporte a tipos concretos
from util.tipo import Tipo

# ExpOr.java
class ExpOr(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "or")

    def avaliar(self) -> ValorBooleano:
        return ValorBooleano(self._esq.avaliar().valor or self._dir.avaliar().valor)

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo().e_booleano() and self._dir.get_tipo().e_booleano()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO