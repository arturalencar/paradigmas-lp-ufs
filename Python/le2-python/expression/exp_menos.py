from exp_unaria import ExpUnaria
from valor_inteiro import ValorInteiro
from util.tipo import Tipo


class ExpMenos(ExpUnaria):

    def __init__(self, exp):
        super().__init__(exp, "-")

    def avaliar(self, amb):

        valor_numerico = self.exp.avaliar(amb).valor

        # Cria e retorna uma nova instância de ValorInteiro com o sinal invertido
        return ValorInteiro(-valor_numerico)

    def _checa_tipo_elemento_terminal(self, amb) -> bool:

        return self.exp.get_tipo(amb).e_inteiro()

    def get_tipo(self, amb) -> Tipo:

        return Tipo.TIPO_INTEIRO
