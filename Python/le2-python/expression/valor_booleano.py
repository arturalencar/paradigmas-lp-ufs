from .valor_concreto import ValorConcreto
from util.tipo import Tipo


class ValorBooleano(ValorConcreto):

    def __init__(self, valor: bool):
        super().__init__(valor)

    def get_tipo(self, amb) -> Tipo:
        return Tipo.TIPO_BOOLEANO
