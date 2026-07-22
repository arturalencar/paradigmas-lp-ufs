from exception.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class Contexto:
    def __init__(self):
        self.pilha = []

    def incrementa(self):
        self.pilha.append({})

    def restaura(self):
        if self.pilha:
            self.pilha.pop()

    def map(self, idArg, valorId):
        if not self.pilha:
            self.incrementa()
        aux = self.pilha[-1]
        if idArg in aux:
            raise VariavelJaDeclaradaException(idArg)
        aux[idArg] = valorId

    def get(self, idArg):
        for aux in reversed(self.pilha):
            if idArg in aux:
                return aux[idArg]
        raise VariavelNaoDeclaradaException(idArg)

    def getPilha(self):
        return self.pilha

    def setPilha(self, pilha):
        self.pilha = pilha
