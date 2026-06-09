from abc import ABC, abstractmethod
from util.tipo import Tipo


class ExpressaoComplexa(ABC):

    @abstractmethod
    def avaliar(self, amb):

        pass

    @abstractmethod
    def checa_tipo(self, amb) -> bool:

        pass

    @abstractmethod
    def get_tipo(self, amb) -> Tipo:

        pass
