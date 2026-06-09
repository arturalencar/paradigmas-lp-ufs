from abc import ABC, abstractmethod
from expression.id import Id


class Ambiente(ABC):
    def incrementa(self):

        pass

    def restaura(self):

        pass

    def map(self, id_arg: Id, tipo_id):

        pass

    def get(self, id_arg: Id):

        pass
