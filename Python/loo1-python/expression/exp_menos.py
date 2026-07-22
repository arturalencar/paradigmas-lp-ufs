from expression.exp_unaria import ExpUnaria
from expression.expressao import Expressao
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self, amb):
        valor_inteiro = self.getExp().avaliar(amb)
        return ValorInteiro(-valor_inteiro.valor())

    def checaTipoElementoTerminal(self, amb) -> bool:
        return self.getExp().getTipo(amb).eInteiro()

    def getTipo(self, amb):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpMenos':
        return ExpMenos(self.exp.clone())
