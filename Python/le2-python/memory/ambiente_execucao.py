from abc import abstractmethod
from .ambiente import Ambiente


class AmbienteExecucao(Ambiente):

    @abstractmethod
    def clone(self):

        pass
