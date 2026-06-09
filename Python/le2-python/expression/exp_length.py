from exp_unaria import ExpUnaria
from valor_inteiro import ValorInteiro
from util.tipo import Tipo


class ExpLength(ExpUnaria):

    def __init__(self, exp):
        super().__init__(exp, "length")

    def avaliar(self, amb):

        string_nativa = self.exp.avaliar(amb).valor

        return ValorInteiro(len(string_nativa))

    def _checa_tipo_elemento_terminal(self, amb) -> bool:

        return self.exp.get_tipo(amb).e_string()

    def get_tipo(self, amb) -> Tipo:

        return Tipo.TIPO_INTEIRO
