from expression.exp_binaria import ExpBinaria
from expression.valor_booleano import ValorBooleano
from util.tipo_primitivo import TipoPrimitivo

class ExpOr(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir)
        self.operador = "or"

    def avaliar(self, ambiente):
        v_esq = self.esq.avaliar(ambiente)
        v_dir = self.dir.avaliar(ambiente)
        return ValorBooleano(v_esq.valor() or v_dir.valor())

    def checaTipo(self, ambiente):
        if not self.esq.checaTipo(ambiente) or not self.dir.checaTipo(ambiente):
            return False
        return self.esq.getTipo(ambiente).eBooleano() and self.dir.getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente):
        return TipoPrimitivo.booleano()
