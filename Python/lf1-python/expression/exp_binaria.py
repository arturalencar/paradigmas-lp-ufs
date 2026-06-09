from abc import ABC, abstractmethod


class ExpBinaria(ABC):
    """
    Uma expressao binaria contem duas expressoes e um operador.
    Esta classe serve como base abstrata para todas as expressoes binarias.
    """

    def __init__(self, esq, dir, operador: str):
        self._esq = esq
        self._dir = dir
        self._operador = operador

    @property
    def esq(self):
        """Retorna a expressao da esquerda"""
        return self._esq

    @property
    def dir(self):
        """Retorna a expressao da direita"""
        return self._dir

    @property
    def operador(self) -> str:
        """Retorna o operador desta expressao binaria"""
        return self._operador

    def __str__(self) -> str:
        """
        Retorna uma representacao String desta expressao. Util para depuracao.
        Equivalente ao toString() do Java.
        """
        return f"{self._esq} {self._operador} {self._dir}"

    def checa_tipo(self, amb) -> bool:
        """
        Realiza a verificacao de tipos desta expressao.
        """
        # Se a checagem de tipo interna da esquerda ou da direita falhar, retorna False
        if not self.esq.checa_tipo(amb) or not self.dir.checa_tipo(amb):
            return False

        # Caso as duas sub-expressões sejam válidas, delega a checagem específica para a subclasse
        return self._checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def _checa_tipo_elemento_terminal(self, amb) -> bool:
        """
        Metodo abstrato (Template Method) que deve ser implementado nas subclasses 
        para checar a compatibilidade dos tipos específicos da operação.
        """
        pass
