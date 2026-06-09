"""
Equivalente ao DecFuncao.java do lf1.

Declaração de função: fun <id> (<params>) = <corpo>.
"""
from util.tipo import Tipo
from .declaracao_funcional import DeclaracaoFuncional


class DecFuncao(DeclaracaoFuncional):
    """
    Declaração de função: fun <id> [params] = <corpo>.
    A aridade é o número de parâmetros formais.
    """

    def __init__(self, id_fun, valor_funcao):
        """
        :param id_fun:       Id com o nome da função.
        :param valor_funcao: ValorFuncao com parâmetros e corpo.
        """
        self._id = id_fun
        self._valor_funcao = valor_funcao

    # ------------------------------------------------------------------ #
    # Propriedades                                                          #
    # ------------------------------------------------------------------ #

    @property
    def id(self):
        return self._id

    @property
    def valor_funcao(self):
        return self._valor_funcao

    # ------------------------------------------------------------------ #
    # DeclaracaoFuncional                                                   #
    # ------------------------------------------------------------------ #

    def get_id(self):
        return self._id

    def get_aridade(self) -> int:
        return self._valor_funcao.get_aridade()

    def get_expressao(self):
        return self._valor_funcao.get_exp()

    def get_funcao(self):
        return self._valor_funcao

    def get_tipo(self, ambiente) -> Tipo:
        """
        Constrói o tipo da função: Tipo -> Tipo -> ... -> Tipo
        (uma cadeia com aridade+1 nós).
        Delega a ValorFuncao.get_tipo().
        """
        ambiente.incrementa()
        tipo = Tipo()
        for _ in range(self.get_aridade() - 1, -1, -1):
            tipo = Tipo(prox=tipo)
        ambiente.map(self._id, tipo)
        result = self._valor_funcao.get_tipo(ambiente)
        ambiente.restaura()
        return result

    def checa_tipo(self, ambiente) -> bool:
        """
        Registra o tipo da função no ambiente e delega a checagem
        ao ValorFuncao.
        """
        ambiente.incrementa()
        tipo = Tipo()
        for _ in range(self.get_aridade() - 1, -1, -1):
            tipo = Tipo(prox=tipo)
        ambiente.map(self._id, tipo)
        result = self._valor_funcao.checa_tipo(ambiente)
        ambiente.restaura()
        return result

    def __str__(self) -> str:
        lista_ids = self._valor_funcao.get_lista_id()
        params_str = ", ".join(str(p) for p in lista_ids) if lista_ids else ""
        return f"fun {self._id} ({params_str}) = {self._valor_funcao.get_exp()}"
