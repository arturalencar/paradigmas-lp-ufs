"""
Equivalente à interface AmbienteExecucaoFuncional.java do lf1.

Estende AmbienteExecucao com suporte a mapeamento de funções:
  - map_funcao(id, valor_funcao)
  - get_funcao(id) -> ValorFuncao
"""
from abc import abstractmethod
from memory.ambiente_execucao import AmbienteExecucao


class AmbienteExecucaoFuncional(AmbienteExecucao):
    """
    Interface que estende AmbienteExecucao com operações para funções.
    Equivalente a AmbienteExecucaoFuncional.java.
    """

    @abstractmethod
    def map_funcao(self, id_arg, funcao) -> None:
        """
        Mapeia um identificador a uma ValorFuncao.

        :param id_arg: o identificador.
        :param funcao: a ValorFuncao.
        :raises VariavelJaDeclaradaException: se o id já estiver declarado.
        """
        ...

    @abstractmethod
    def get_funcao(self, id_arg):
        """
        Retorna a ValorFuncao associada ao identificador.

        :param id_arg: o identificador.
        :return: ValorFuncao associada.
        :raises VariavelNaoDeclaradaException: se o id não estiver declarado.
        """
        ...
