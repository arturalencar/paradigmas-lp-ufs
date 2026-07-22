from expression.exp_binaria import ExpBinaria
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpSoma(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir)
        self.operador = "+"

    def avaliar(self, ambiente):
        v_esq = self.esq.avaliar(ambiente)
        v_dir = self.dir.avaliar(ambiente)
        return ValorInteiro(v_esq.valor() + v_dir.valor())

    def checaTipo(self, ambiente):
        if not self.esq.checaTipo(ambiente) or not self.dir.checaTipo(ambiente):
            return False
        return self.esq.getTipo(ambiente).eInteiro() and self.dir.getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente):
        return TipoPrimitivo.inteiro()
