from expression.exp_unaria import ExpUnaria
from expression.valor_booleano import ValorBooleano
from util.tipo_primitivo import TipoPrimitivo

class ExpNot(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao)
        self.operador = "not"

    def avaliar(self, ambiente):
        v_exp = self.exp.avaliar(ambiente)
        return ValorBooleano(not v_exp.valor())

    def checaTipo(self, ambiente):
        if not self.exp.checaTipo(ambiente):
            return False
        return self.exp.getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente):
        return TipoPrimitivo.booleano()
