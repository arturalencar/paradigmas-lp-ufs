from typing import cast

from util.tipo import Tipo
from expression.valor_concreto import ValorConcreto

class ValorString(ValorConcreto[str]):
    def __init__(self, valor: str):
        super().__init__(valor)

    def get_tipo(self):
        return Tipo.TIPO_STRING