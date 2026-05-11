from typing import cast

from expression.exp_binaria import ExpBinaria
from expression.valor_booleano import ValorBooleano
from expression.valor_string import ValorString
from expression.valor_inteiro import ValorInteiro  # Para suporte a tipos concretos
from util.tipo import Tipo

# ExpConcat.java
class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "++")

    def avaliar(self) -> ValorString:
        return ValorString(str(self._esq.avaliar().valor) + str(self._dir.avaliar().valor))

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo().e_string() and self._dir.get_tipo().e_string()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_STRING