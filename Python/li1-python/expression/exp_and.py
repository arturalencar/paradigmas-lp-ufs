from expression.exp_binaria import ExpBinaria
from expression.valor_booleano import ValorBooleano
from util.tipo_primitivo import TipoPrimitivo

class ExpAnd(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "and")

    def avaliar(self, amb):
        valor_esq = self.getEsq().avaliar(amb)
        valor_dir = self.getDir().avaliar(amb)
        return ValorBooleano(valor_esq.valor() and valor_dir.valor())

    def checaTipoElementoTerminal(self, ambiente) -> bool:
        return self.getEsq().getTipo(ambiente).eBooleano() and self.getDir().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpAnd':
        return ExpAnd(self.esq.clone(), self.dir.clone())
