from exp_binaria import ExpBinaria
from valor_string import ValorString
from util.tipo import Tipo


class ExpConcat(ExpBinaria):

    def __init__(self, esq, dir):
        # Passa as sub-expressões e o operador de concatenação "++" para a superclasse
        super().__init__(esq, dir, "++")

    def avaliar(self, amb):

        valor_esq = self.esq.avaliar(amb).valor
        valor_dir = self.dir.avaliar(amb).valor

        return ValorString(valor_esq + valor_dir)

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        return self.esq.get_tipo(ambiente).e_string() and self.dir.get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente) -> Tipo:
        return Tipo.TIPO_STRING
