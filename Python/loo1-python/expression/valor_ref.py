class ValorRef:
    VALOR_INICIAL = 1

    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        return self._valor

    def incrementa(self):
        return ValorRef(self._valor + 1)

    def __eq__(self, other):
        if isinstance(other, ValorRef):
            return self._valor == other._valor
        return False

    def __hash__(self):
        return hash(self._valor)

    def __str__(self):
        return f"Ref({self._valor})"
