from expression.valor_concreto import ValorConcreto
from util.tipo_primitivo import TipoPrimitivo

class ValorInteiro(ValorConcreto):
    def __init__(self, valor):
        super().__init__(valor)

    def checaTipo(self, ambiente):
        return True

    def getTipo(self, ambiente):
        return TipoPrimitivo.inteiro()
