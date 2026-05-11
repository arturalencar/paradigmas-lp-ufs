from exp_unaria import ExpUnaria
from expressao import Expressao
from .valor_inteiro import ValorInteiro
from util.tipo import Tipo

# ExpMenos.java (Menos Unário)
class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self) -> ValorInteiro:
        return ValorInteiro(-(self.exp.avaliar().valor))

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.exp.get_tipo().e_inteiro()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
