from abc import ABC, abstractmethod

class Ambiente(ABC):
    @abstractmethod
    def incrementa(self):
        pass

    @abstractmethod
    def restaura(self):
        pass

    @abstractmethod
    def map(self, idArg, tipoId):
        pass

    @abstractmethod
    def get(self, idArg):
        pass
