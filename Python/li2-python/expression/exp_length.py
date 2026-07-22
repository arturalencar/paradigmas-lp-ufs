from expression.exp_unaria import ExpUnaria
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpLength(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao)
        self.operador = "length"

    def avaliar(self, ambiente):
        v_exp = self.exp.avaliar(ambiente)
        return ValorInteiro(len(v_exp.valor()))

    def checaTipo(self, ambiente):
        if not self.exp.checaTipo(ambiente):
            return False
        return self.exp.getTipo(ambiente).eString()

    def getTipo(self, ambiente):
        return TipoPrimitivo.inteiro()
