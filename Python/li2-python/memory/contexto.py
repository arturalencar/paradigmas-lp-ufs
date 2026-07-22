from exception.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class Contexto:
    def __init__(self):
        self.pilha = [{}]

    def incrementa(self):
        self.pilha.append({})

    def restaura(self):
        if len(self.pilha) > 1:
            self.pilha.pop()

    def map(self, idArg, valorId):
        topo = self.pilha[-1]
        if idArg.getNome() in topo:
            raise VariavelJaDeclaradaException(idArg.getNome())
        topo[idArg.getNome()] = valorId

    def get(self, idArg):
        for escopo in reversed(self.pilha):
            if idArg.getNome() in escopo:
                return escopo[idArg.getNome()]
        raise VariavelNaoDeclaradaException(idArg.getNome())
