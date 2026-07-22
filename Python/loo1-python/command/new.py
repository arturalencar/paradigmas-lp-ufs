from command.comando import Comando
from memory.contexto_execucao_oo1 import ContextoExecucaoOO1
from memory.contexto_objeto import ContextoObjeto
from memory.objeto import Objeto
from command.atribuicao import Atribuicao

class New(Comando):
    def __init__(self, av, classe):
        self.av = av
        self.classe = classe

    def executar(self, ambiente):
        def_classe = ambiente.getDefClasse(self.classe)
        dec_variavel = def_classe.getDecVariavel()

        aux = dec_variavel.elabora(ContextoExecucaoOO1(ambiente))
        
        # Pop the top scope to form the object's state
        estado_hash = aux.getPilha().pop()
        estado_obj = ContextoObjeto(estado_hash)
        objeto = Objeto(self.classe, estado_obj)

        vr = ambiente.getProxRef()
        ambiente.mapObjeto(vr, objeto)
        
        ambiente = Atribuicao(self.av, vr).executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente):
        from util.tipo_classe import TipoClasse
        tp_classe = TipoClasse(self.classe)
        return (self.av.checaTipo(ambiente) and
                tp_classe.eValido(ambiente) and
                tp_classe == self.av.getTipo(ambiente))

    def getClasse(self):
        return self.classe

    def getAv(self):
        return self.av
