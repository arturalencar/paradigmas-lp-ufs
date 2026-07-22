from expression.valor import Valor

class ValorRef(Valor):
    VALOR_INICIAL = 1

    def __init__(self, valor):
        self._valor = valor

    def avaliar(self, ambiente):
        return self

    def checaTipo(self, ambiente):
        return True

    def getTipo(self, ambiente):
        from util.tipo_primitivo import TipoPrimitivo
        return TipoPrimitivo.INTEIRO

    def reduzir(self, ambiente):
        return self

    def clone(self):
        return self

    def valor(self):
        return self._valor

    def incrementa(self):
        self._valor += 1
        return self

    def __eq__(self, other):
        if isinstance(other, ValorRef):
            return self._valor == other._valor
        return False

    def isEquals(self, obj):
        return self == obj

    def __hash__(self):
        return hash(self._valor)

    def __str__(self):
        return f"Ref({self._valor})"
