from exp_binaria import ExpBinaria
from valor_booleano import ValorBooleano
from util.tipo import Tipo


class ExpOr(ExpBinaria):

    def __init__(self, esq, dir):
        super().__init__(esq, dir, "or")

    def avaliar(self, amb):

        valor_esq = self.esq.avaliar(amb).valor
        valor_dir = self.dir.avaliar(amb).valor

        return ValorBooleano(valor_esq or valor_dir)

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:

        return self.esq.get_tipo(ambiente).e_booleano() and self.dir.get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente) -> Tipo:

        return Tipo.TIPO_BOOLEANO
