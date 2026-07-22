from expression.exp_unaria import ExpUnaria
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpMenos(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao)
        self.operador = "-"

    def avaliar(self, ambiente):
        v_exp = self.exp.avaliar(ambiente)
        return ValorInteiro(-v_exp.valor())

    def checaTipo(self, ambiente):
        if not self.exp.checaTipo(ambiente):
            return False
        return self.exp.getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente):
        return TipoPrimitivo.inteiro()
