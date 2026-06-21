from expression.valor_concreto import ValorConcreto
from util.tipo_primitivo import TipoPrimitivo

class ValorInteiro(ValorConcreto[int]):
    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self, amb):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ValorInteiro':
        return ValorInteiro(self.valor())
