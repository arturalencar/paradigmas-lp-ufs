from typing import cast

from .exp_binaria import ExpBinaria
from .valor_booleano import ValorBooleano
from .valor_string import ValorString
from util.tipo import Tipo

# ExpEquals.java
class ExpEquals(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "==")

    def avaliar(self) -> ValorBooleano:
        # Usamos o método is_equals que definimos na base ValorConcreto
        v1 = self._esq.avaliar()
        v2 = self._dir.avaliar()
        return ValorBooleano(v1.is_equals(v2))

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo() == self._dir.get_tipo()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO