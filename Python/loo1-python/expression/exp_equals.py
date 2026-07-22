from expression.exp_binaria import ExpBinaria
from expression.valor_booleano import ValorBooleano
from util.tipo_primitivo import TipoPrimitivo

class ExpEquals(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "==")

    def avaliar(self, amb):
        esq_val = self.getEsq().avaliar(amb)
        dir_val = self.getDir().avaliar(amb)
        return ValorBooleano(esq_val.isEquals(dir_val))

    def checaTipoElementoTerminal(self, ambiente) -> bool:
        return self.getEsq().getTipo(ambiente).eIgual(self.getDir().getTipo(ambiente))

    def getTipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ExpEquals':
        return ExpEquals(self.esq.clone(), self.dir.clone())
