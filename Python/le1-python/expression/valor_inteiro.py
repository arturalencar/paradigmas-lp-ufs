from typing import cast
from expression.valor_concreto import ValorConcreto        
from util.tipo import Tipo

class ValorInteiro(ValorConcreto[int]):
    def __init__(self, valor: int):
        super().__init__(valor)

    def get_tipo(self):
        return Tipo.TIPO_INTEIRO