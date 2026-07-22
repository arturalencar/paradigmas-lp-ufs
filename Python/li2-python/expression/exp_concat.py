from expression.exp_binaria import ExpBinaria
from expression.valor_string import ValorString

class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir)
        self.operador = "++"

    def avaliar(self, ambiente):
        v_esq = self.esq.avaliar(ambiente)
        v_dir = self.dir.avaliar(ambiente)
        return ValorString(v_esq.valor() + v_dir.valor())

    def checaTipo(self, ambiente):
        if not self.esq.checaTipo(ambiente) or not self.dir.checaTipo(ambiente):
            return False
        return self.esq.getTipo(ambiente).eString() and self.dir.getTipo(ambiente).eString()

    def getTipo(self, ambiente):
        return self.esq.getTipo(ambiente)
