from expression.expressao import Expressao
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class Id(Expressao):
    def __init__(self, strName: str):
        self.idName = strName

    def __str__(self):
        return self.idName

    def avaliar(self, ambiente):
        return ambiente.get(self)

    def checaTipo(self, amb) -> bool:
        amb.get(self)
        return True

    def getTipo(self, amb):
        return amb.get(self)

    def getIdName(self) -> str:
        return self.idName

    def setIdName(self, idName: str):
        self.idName = idName

    def __hash__(self):
        return hash(self.idName)

    def __eq__(self, obj):
        if not isinstance(obj, Id):
            return False
        return self.idName == obj.idName

    def reduzir(self, ambiente):
        try:
            valor = ambiente.get(self)
            return valor.clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> 'Id':
        return self
