from typing import cast

from util.tipo import Tipo
from expression.valor_concreto import ValorConcreto        

class ValorBooleano(ValorConcreto[bool]):
    def __init__(self, valor: bool):
        super().__init__(valor)

    def get_tipo(self):
        return Tipo.TIPO_BOOLEANO