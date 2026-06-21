from expression.exp_unaria import ExpUnaria
from expression.expressao import Expressao
from expression.valor_booleano import ValorBooleano
from util.tipo_primitivo import TipoPrimitivo

class ExpNot(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self, amb):
        valor_booleano = self.getExp().avaliar(amb)
        return ValorBooleano(not valor_booleano.valor())

    def checaTipoElementoTerminal(self, amb) -> bool:
        return self.getExp().getTipo(amb).eBooleano()

    def getTipo(self, amb):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpNot':
        return ExpNot(self.exp.clone())
