from typing import cast
from expression.exp_binaria import ExpBinaria
from expression.valor_inteiro import ValorInteiro
from expression.expressao import Expressao
from util.tipo import Tipo;

class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "+")

    def avaliar(self):
        # Em Python, o 'cast' (ValorInteiro) não é necessário devido ao dinamismo,
        # mas assumimos que o retorno de avaliar() possui o método .valor()
        esq_val = self._esq.avaliar()
        dir_val = self._dir.avaliar()
        return ValorInteiro(esq_val.valor + dir_val.valor);
    
    def _checa_tipo_elemento_terminal(self) -> bool:
        return self._esq.get_tipo().e_inteiro() and self._dir.get_tipo().e_inteiro()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO

