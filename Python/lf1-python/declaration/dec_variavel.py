"""
Equivalente ao DecVariavel.java do lf1.

Declaração de variável simples (aridade 0) compatível com
DeclaracaoFuncional, para uso dentro de ExpDeclaracao funcional.
"""

from util.tipo import Tipo
from .declaracao_funcional import DeclaracaoFuncional


class DecVariavel(DeclaracaoFuncional):
    """
    Declaração de variável: var <id> = <expressao>.
    Aridade sempre 0 (não é uma função).
    """

    def __init__(self, id_arg, expressao_arg):
        self._id = id_arg
        self._expressao = expressao_arg

    # ------------------------------------------------------------------ #
    # Propriedades                                                          #
    # ------------------------------------------------------------------ #

    @property
    def id(self):
        return self._id

    @property
    def expressao(self):
        return self._expressao

    # ------------------------------------------------------------------ #
    # DeclaracaoFuncional                                                   #
    # ------------------------------------------------------------------ #

    def get_id(self):
        return self._id

    def get_aridade(self) -> int:
        return 0

    def get_expressao(self):
        return self._expressao

    def get_tipo(self, ambiente) -> Tipo:
        """Delega ao tipo da expressão associada."""
        return self._expressao.get_tipo(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        """Delega à verificação de tipos da expressão associada."""
        return self._expressao.checa_tipo(ambiente)

    def __str__(self) -> str:
        return f"var {self._id} = {self._expressao}"
