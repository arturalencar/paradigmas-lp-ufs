from typing import cast

from .exp_binaria import ExpBinaria
from .valor_booleano import ValorBooleano
from util.tipo import Tipo

# ExpAnd.java
class ExpAnd(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "and")

    def avaliar(self) -> ValorBooleano:
        # Pythonico: o operador 'and' já lida com a lógica booleana
        return ValorBooleano(self._esq.avaliar().valor and self._dir.avaliar().valor)

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo().e_booleano() and self._dir.get_tipo().e_booleano()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
