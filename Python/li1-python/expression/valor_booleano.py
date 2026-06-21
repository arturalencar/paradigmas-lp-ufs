from expression.valor_concreto import ValorConcreto
from util.tipo_primitivo import TipoPrimitivo

class ValorBooleano(ValorConcreto[bool]):
    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self, amb):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ValorBooleano':
        return ValorBooleano(self.valor())
