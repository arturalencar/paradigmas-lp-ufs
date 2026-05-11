from exp_unaria import ExpUnaria
from expressao import Expressao
from .valor_booleano import ValorBooleano
from util.tipo import Tipo

# ExpNot.java
class ExpNot(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self) -> ValorBooleano:
        # Usamos 'not' do Python
        return ValorBooleano(not self.exp.avaliar().valor)

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.exp.get_tipo().e_booleano()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO