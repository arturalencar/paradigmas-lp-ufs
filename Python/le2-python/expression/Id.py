from expressao import Expressao
from util.tipo import Tipo


class Id(Expressao):

    def __init__(self, str_name: str):
        self._id_name = str_name

    @property
    def id_name(self) -> str:
        return self._id_name

    @id_name.setter
    def id_name(self, value: str):
        self._id_name = value

    def __eq__(self, other) -> bool:

        if isinstance(other, Id):
            return self._id_name == other._id_name
        return False

    def __hash__(self) -> int:

        return hash(self._id_name)

    def __str__(self) -> str:

        return self._id_name

    def avaliar(self, ambiente):

        return ambiente.get(self)

    def checa_tipo(self, amb) -> bool:

        return True

    def get_tipo(self, amb) -> Tipo:

        return amb.get(self)
