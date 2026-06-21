from expression.exp_unaria import ExpUnaria
from expression.expressao import Expressao
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpLength(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self, amb):
        valor_string = self.getExp().avaliar(amb)
        return ValorInteiro(len(valor_string.valor()))

    def checaTipoElementoTerminal(self, amb) -> bool:
        return self.getExp().getTipo(amb).eString()

    def getTipo(self, amb):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpLength':
        return ExpLength(self.exp.clone())
