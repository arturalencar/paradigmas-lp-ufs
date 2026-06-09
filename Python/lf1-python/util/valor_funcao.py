"""
Equivalente ao ValorFuncao.java do lf1.

Encapsula os parâmetros formais e o corpo de uma função declarada.
Responsável por:
  - Fornecer a aridade (número de parâmetros).
  - Realizar checagem de tipos e inferência de tipo (get_tipo).
"""
from util.tipo import Tipo


class ValorFuncao:
    """
    Representa o valor de uma função: lista de parâmetros Id e expressão corpo.

    Equivalente a ValorFuncao.java:
      - argsId : List<Id>   -> lista de parâmetros formais
      - exp    : Expressao  -> corpo da função
    """

    def __init__(self, args_id: list, exp):
        """
        :param args_id: lista de Id com os parâmetros formais.
        :param exp:     expressão que constitui o corpo da função.
        """
        self._args_id = args_id
        self._exp = exp

    # ------------------------------------------------------------------ #
    # Getters                                                               #
    # ------------------------------------------------------------------ #

    def get_lista_id(self) -> list:
        """Retorna a lista de Id dos parâmetros formais."""
        return self._args_id

    def get_exp(self):
        """Retorna a expressão corpo da função."""
        return self._exp

    def get_aridade(self) -> int:
        """Retorna o número de parâmetros formais."""
        return len(self._args_id)

    # ------------------------------------------------------------------ #
    # Verificação de tipos                                                   #
    # ------------------------------------------------------------------ #

    def checa_tipo(self, ambiente) -> bool:
        """
        Registra cada parâmetro com seu tipo inferido no ambiente e
        verifica os tipos do corpo da função.

        Equivalente a ValorFuncao.checaTipo().
        """
        ambiente.incrementa()
        tipo = self.get_tipo(ambiente)
        for id_param in self._args_id:
            ambiente.map(id_param, Tipo(tipo.get()))
            tipo = tipo.prox

        ambiente.restaura()
        return True

    def get_tipo(self, ambiente) -> Tipo:
        """
        Infere o tipo desta função usando RestrictTypesVisitor e
        retorna a cadeia de tipos Tipo -> ... -> TipoResultado.

        Equivalente a ValorFuncao.getTipo().
        """
        from util.restrict_types_visitor import RestrictTypesVisitor

        # Cria mapa inicial Id -> Tipo() (todos indefinidos) para os parâmetros
        map_id_tipo: dict = {}
        ids_arg = list(self._args_id)
        for id_param in ids_arg:
            map_id_tipo[id_param] = Tipo()

        # Visita o corpo para restringir/inferir os tipos
        RestrictTypesVisitor.visit(self._exp, ambiente, map_id_tipo, Tipo())

        # Registra os tipos inferidos no ambiente
        ambiente.incrementa()
        for id_param, tipo_param in map_id_tipo.items():
            ambiente.map(id_param, tipo_param)

        # Obtém o tipo de retorno do corpo
        result = self._exp.get_tipo(ambiente)

        # Constrói a cadeia de tipos (currying): t0 -> t1 -> ... -> result
        for i in range(len(ids_arg) - 1, -1, -1):
            result = Tipo(map_id_tipo[ids_arg[i]].get(), result)

        ambiente.restaura()
        return result

    def __str__(self) -> str:
        params = ", ".join(str(p) for p in self._args_id)
        return f"fun ({params}) = {self._exp}"
