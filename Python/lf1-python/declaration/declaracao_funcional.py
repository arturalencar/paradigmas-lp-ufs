"""
Equivalente à interface DeclaracaoFuncional.java do lf1.

Define o contrato que todas as declarações funcionais devem seguir:
  - DecVariavel  (aridade 0)
  - DecFuncao    (aridade >= 1)
"""
from abc import ABC, abstractmethod


class DeclaracaoFuncional(ABC):
    """Interface base para declarações funcionais."""

    @abstractmethod
    def get_id(self):
        """Retorna o identificador desta declaração."""
        ...

    @abstractmethod
    def get_aridade(self) -> int:
        """
        Retorna a aridade da declaração.
        Variáveis têm aridade 0; funções têm aridade >= 1.
        """
        ...

    @abstractmethod
    def get_expressao(self):
        """Retorna a expressão associada a esta declaração."""
        ...

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool:
        """
        Realiza a verificação de tipos desta declaração.

        :param ambiente: o ambiente de compilação.
        :return: True se os tipos são válidos; False caso contrário.
        """
        ...

    @abstractmethod
    def get_tipo(self, ambiente):
        """
        Retorna o tipo desta declaração.

        :param ambiente: o ambiente de compilação.
        :return: o Tipo desta declaração.
        """
        ...
