from valor_concreto import ValorConcreto
from util.tipo import Tipo


class ValorInteiro(ValorConcreto):

    def __init__(self, valor: int):
        super().__init__(valor)

    def get_tipo(self, amb) -> Tipo:

        return Tipo.TIPO_INTEIRO
