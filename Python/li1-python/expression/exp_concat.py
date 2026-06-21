from expression.exp_binaria import ExpBinaria
from expression.valor_string import ValorString
from util.tipo_primitivo import TipoPrimitivo

class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "++")

    def avaliar(self, amb):
        valor_esq = self.getEsq().avaliar(amb)
        valor_dir = self.getDir().avaliar(amb)
        return ValorString(valor_esq.valor() + valor_dir.valor())

    def checaTipoElementoTerminal(self, ambiente) -> bool:
        return self.getEsq().getTipo(ambiente).eString() and self.getDir().getTipo(ambiente).eString()

    def getTipo(self, ambiente):
        return TipoPrimitivo.STRING

    def clone(self) -> 'ExpConcat':
        return ExpConcat(self.esq.clone(), self.dir.clone())
