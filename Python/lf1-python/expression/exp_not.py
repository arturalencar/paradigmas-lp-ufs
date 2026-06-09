from .exp_unaria import ExpUnaria
from .valor_booleano import ValorBooleano
from util.tipo import Tipo


class ExpNot(ExpUnaria):

    def __init__(self, exp):

        super().__init__(exp, "~")

    def avaliar(self, amb):

        booleano_nativo = self.exp.avaliar(amb).valor

        return ValorBooleano(not booleano_nativo)

    def _checa_tipo_elemento_terminal(self, amb) -> bool:

        return self.exp.get_tipo(amb).e_booleano()

    def get_tipo(self, amb) -> Tipo:

        return Tipo.TIPO_BOOLEANO
