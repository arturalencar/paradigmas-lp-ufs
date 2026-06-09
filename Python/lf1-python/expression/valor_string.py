from util.tipo import Tipo
from .valor_concreto import ValorConcreto


class ValorString(ValorConcreto):

    def __init__(self, valor: str):
        super().__init__(valor)

    def get_tipo(self, amb) -> Tipo:
        return Tipo.TIPO_STRING
