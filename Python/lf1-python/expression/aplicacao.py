"""
Equivalente ao Aplicacao.java do lf1.

Aplicação de função: <id_func>(<args>).

Ao avaliar:
  1. Obtém a ValorFuncao do ambiente funcional.
  2. Avalia cada argumento no ambiente ATUAL (passagem por valor).
  3. Abre novo escopo e mapeia parâmetros -> valores.
  4. Avalia o corpo da função.
  5. Restaura o escopo.
"""
from util.tipo import Tipo


class Aplicacao:
    """
    Aplicação de função: func(arg1, arg2, ...).
    Equivalente a Aplicacao.java do lf1.
    """

    def __init__(self, func, args_expressao: list):
        """
        :param func:            Id da função a ser aplicada.
        :param args_expressao:  lista de Expressao com os argumentos reais.
        """
        self._func = func
        self._args_expressao = args_expressao

    # ------------------------------------------------------------------ #
    # Avaliação                                                             #
    # ------------------------------------------------------------------ #

    def avaliar(self, ambiente):
        """
        Aplica a função ao seus argumentos avaliados.
        """
        # O ambiente deve ser um AmbienteExecucaoFuncional
        funcao = ambiente.get_funcao(self._func)

        # Resolve os bindings: avalia cada argumento ANTES de abrir o escopo
        map_id_valor = self._resolve_parameters_bindings(ambiente, funcao)

        # Abre novo escopo e vincula parâmetros -> valores
        ambiente.incrementa()
        self._include_value_bindings(ambiente, map_id_valor)

        # Avalia o corpo da função
        resultado = funcao.get_exp().avaliar(ambiente)
        ambiente.restaura()
        return resultado

    def _resolve_parameters_bindings(self, ambiente, funcao) -> dict:
        """
        Avalia cada expressão argumento e mapeia ao parâmetro formal correspondente.
        Preserva a ordem da lista de parâmetros.
        """
        parametros_id = funcao.get_lista_id()
        map_id_valor = {}

        iter_args = iter(self._args_expressao)
        for id_param in parametros_id:
            exp = next(iter_args)
            valor_real = exp.avaliar(ambiente)
            map_id_valor[id_param] = valor_real

        return map_id_valor

    def _include_value_bindings(self, ambiente, map_id_valor: dict) -> None:
        """Insere cada par (id, valor) no escopo atual do ambiente."""
        for id_obj, valor in map_id_valor.items():
            ambiente.map(id_obj, valor)

    # ------------------------------------------------------------------ #
    # Verificação de tipos                                                   #
    # ------------------------------------------------------------------ #

    def checa_tipo(self, ambiente) -> bool:
        """
        Verifica:
          - o tamanho da lista de argumentos bate com a aridade da função.
          - cada argumento é bem-tipado e compatível com o parâmetro esperado.
        """
        tipo_funcao = ambiente.get(self._func)
        return (self._check_argument_list_size(tipo_funcao)
                and self._check_argument_types(ambiente, tipo_funcao))

    def _check_argument_list_size(self, tipo_funcao) -> bool:
        """Verifica que o número de argumentos é igual à aridade da função."""
        tamanho_tipo = 0
        aux = tipo_funcao
        while aux is not None:
            tamanho_tipo += 1
            aux = aux.prox
        return (tamanho_tipo - 1) == len(self._args_expressao)

    def _check_argument_types(self, ambiente, tipo_funcao) -> bool:
        """Verifica que cada argumento é bem-tipado e compatível com o esperado."""
        result = True
        tipo_atual = tipo_funcao
        for arg in self._args_expressao:
            if not arg.checa_tipo(ambiente):
                result = False
            tipo_arg = arg.get_tipo(ambiente)
            if tipo_arg.intersecao(tipo_atual).e_void():
                result = False
            tipo_atual = tipo_atual.prox
        return result

    def get_tipo(self, ambiente) -> Tipo:
        """Retorna o tipo de retorno da função (último nó da cadeia de tipos)."""
        t = ambiente.get(self._func)
        while t.prox is not None:
            t = t.prox
        return t

    # ------------------------------------------------------------------ #
    # Getters                                                               #
    # ------------------------------------------------------------------ #

    def get_func(self):
        return self._func

    def get_args_expressao(self) -> list:
        return self._args_expressao

    def __str__(self) -> str:
        args_str = str(self._args_expressao)
        return f"{self._func} ({args_str})"
