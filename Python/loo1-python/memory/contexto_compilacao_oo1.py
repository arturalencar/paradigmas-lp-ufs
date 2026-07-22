from memory.contexto_compilacao_imperativa import ContextoCompilacaoImperativa
from memory.ambiente_compilacao_oo1 import AmbienteCompilacaoOO1
from exception.classe_ja_declarada_exception import ClasseJaDeclaradaException
from exception.classe_nao_declarada_exception import ClasseNaoDeclaradaException

class ContextoCompilacaoOO1(ContextoCompilacaoImperativa, AmbienteCompilacaoOO1):
    def __init__(self, entrada):
        super().__init__(entrada)
        self.map_def_classe = {}

    def mapDefClasse(self, idArg, defClasse):
        if idArg in self.map_def_classe:
            raise ClasseJaDeclaradaException(idArg.getIdName())
        self.map_def_classe[idArg] = defClasse

    def getDefClasse(self, idArg):
        if idArg not in self.map_def_classe:
            raise ClasseNaoDeclaradaException(idArg.getIdName())
        return self.map_def_classe[idArg]
