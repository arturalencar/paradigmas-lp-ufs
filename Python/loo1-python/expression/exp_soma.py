from expression.exp_binaria import ExpBinaria
from expression.valor_inteiro import ValorInteiro
from util.tipo_primitivo import TipoPrimitivo

class ExpSoma(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "+")

    def avaliar(self, amb):
        valor_esq = self.getEsq().avaliar(amb)
        valor_dir = self.getDir().avaliar(amb)
        return ValorInteiro(valor_esq.valor() + valor_dir.valor())

    def checaTipoElementoTerminal(self, ambiente) -> bool:
        return self.getEsq().getTipo(ambiente).eInteiro() and self.getDir().getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ExpSoma':
        return ExpSoma(self.esq.clone(), self.dir.clone())
