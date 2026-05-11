from expression.exp_unaria import ExpUnaria
from expression.expressao import Expressao
from expression.valor_inteiro import ValorInteiro
from util.tipo import Tipo

# ExpLength.java
class ExpLength(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self) -> ValorInteiro:
        # Pythonice: usamos len() em vez de .length()
        conteudo = self.exp.avaliar().valor
        return ValorInteiro(len(str(conteudo)))

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.exp.get_tipo().e_string()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO