from exp_binaria import ExpBinaria
from valor_inteiro import ValorInteiro
from util.tipo import Tipo


class ExpSoma(ExpBinaria):

    def __init__(self, esq, dir):
        super().__init__(esq, dir, "+")

    def avaliar(self, amb):

        valor_esq = self.esq.avaliar(amb).valor
        valor_dir = self.dir.avaliar(amb).valor

        # Cria e retorna uma nova instância de ValorInteiro com o resultado da soma
        return ValorInteiro(valor_esq + valor_dir)

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:

        return self.esq.get_tipo(ambiente).e_inteiro() and self.dir.get_tipo(ambiente).e_inteiro()

    def get_tipo(self, ambiente) -> Tipo:

        return Tipo.TIPO_INTEIRO
