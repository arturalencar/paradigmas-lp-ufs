from memory.contexto_execucao_imperativa import ContextoExecucaoImperativa
from memory.ambiente_execucao_oo1 import AmbienteExecucaoOO1
from exception.classe_ja_declarada_exception import ClasseJaDeclaradaException
from exception.classe_nao_declarada_exception import ClasseNaoDeclaradaException
from exception.objeto_ja_declarado_exception import ObjetoJaDeclaradoException
from exception.objeto_nao_declarado_exception import ObjetoNaoDeclaradoException
from expression.valor_ref import ValorRef

class ContextoExecucaoOO1(ContextoExecucaoImperativa, AmbienteExecucaoOO1):
    def __init__(self, entrada=None):
        super().__init__(entrada)
        self.map_def_classe = {}
        self.map_objetos = {}
        self.prox_ref = ValorRef(ValorRef.VALOR_INICIAL)

    def getMapDefClasse(self):
        return self.map_def_classe

    def getMapObjetos(self):
        return self.map_objetos

    def mapDefClasse(self, idArg, defClasse):
        if idArg in self.map_def_classe:
            raise ClasseJaDeclaradaException(idArg.getIdName())
        self.map_def_classe[idArg] = defClasse

    def mapObjeto(self, valorRef, objeto):
        if valorRef in self.map_objetos:
            raise ObjetoJaDeclaradoException(objeto.getClasse().getIdName())
        self.map_objetos[valorRef] = objeto

    def getDefClasse(self, idArg):
        if idArg not in self.map_def_classe:
            raise ClasseNaoDeclaradaException(idArg.getIdName())
        return self.map_def_classe[idArg]

    def getObjeto(self, valorRef):
        if valorRef not in self.map_objetos:
            raise ObjetoNaoDeclaradoException(str(valorRef))
        return self.map_objetos[valorRef]

    def getProxRef(self):
        aux = ValorRef(self.prox_ref.valor())
        self.prox_ref = self.prox_ref.incrementa()
        return aux

    def getRef(self):
        if self.prox_ref is None:
            self.prox_ref = ValorRef(ValorRef.VALOR_INICIAL)
        return self.prox_ref
