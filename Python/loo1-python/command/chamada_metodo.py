from command.comando import Comando
from memory.contexto_execucao_oo1 import ContextoExecucaoOO1
from command.chamada_procedimento import ChamadaProcedimento
from expression.id import Id

class ChamadaMetodo(Comando):
    def __init__(self, expressao, nome_metodo, parametros_reais):
        self.expressao = expressao
        self.nome_metodo = nome_metodo
        self.parametros_reais = parametros_reais

    def executar(self, ambiente):
        vr = self.expressao.avaliar(ambiente)
        objeto = ambiente.getObjeto(vr)
        id_classe = objeto.getClasse()
        def_classe = ambiente.getDefClasse(id_classe)
        metodo = def_classe.getMetodo(self.nome_metodo)

        aux = ContextoExecucaoOO1(ambiente)
        aux.changeValor(Id("this"), vr)

        valores_dos_parametros = self.parametros_reais.avaliar(ambiente)
        ChamadaProcedimento(metodo, self.parametros_reais, valores_dos_parametros).executar(aux)
        return ambiente

    def checaTipo(self, ambiente):
        try:
            tipo_classe = self.expressao.getTipo(ambiente)
            def_classe = ambiente.getDefClasse(tipo_classe.getTipo())
            metodo = def_classe.getMetodo(self.nome_metodo)
            
            ambiente.incrementa()
            ambiente.map(Id("this"), tipo_classe)
            resposta = ChamadaProcedimento(metodo, self.parametros_reais).checaTipo(ambiente)
            ambiente.restaura()
            return resposta
        except Exception:
            return False
