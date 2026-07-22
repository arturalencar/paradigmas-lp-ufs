from expression.valor_concreto import ValorConcreto
from util.tipo_primitivo import TipoPrimitivo

class ValorString(ValorConcreto[str]):
    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self, amb):
        return TipoPrimitivo.STRING

    def __str__(self):
        return f'"{super().__str__()}"'

    def clone(self) -> 'ValorString':
        return ValorString(self.valor())
