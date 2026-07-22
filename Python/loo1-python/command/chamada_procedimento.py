from command.comando import Comando
from memory.contexto_execucao_oo1 import ContextoExecucaoOO1
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class ChamadaProcedimento(Comando):
    def __init__(self, procedimento, parametros_reais, valores_parametros=None):
        self.procedimento = procedimento
        self.parametros_reais = parametros_reais
        self.valores_parametros = valores_parametros

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self._bindParameters(ambiente, self.procedimento.getParametrosFormais())
        ambiente = self.procedimento.getComando().executar(ambiente)
        ambiente.restaura()
        return ambiente

    def _bindParameters(self, ambiente, parametros_formais):
        lista_valor = self.valores_parametros
        if lista_valor is None:
            lista_valor = self.parametros_reais.avaliar(ambiente)
        
        while lista_valor is not None and lista_valor.length() > 0:
            ambiente.map(parametros_formais.getHead().getId(), lista_valor.getHead())
            parametros_formais = parametros_formais.getTail()
            lista_valor = lista_valor.getTail()
        return ambiente

    def checaTipo(self, ambiente):
        ambiente.incrementa()
        parametros_formais = self.procedimento.getParametrosFormais()
        lista_tipo = self.parametros_reais.getTipos(ambiente)
        
        if lista_tipo.length() == parametros_formais.length():
            if lista_tipo.head() is None or parametros_formais.getHead() is None:
                resposta = True
            else:
                resposta = True
                while lista_tipo is not None and parametros_formais is not None:
                    if lista_tipo.head() != parametros_formais.getHead().getTipo():
                        resposta = False
                        break
                    lista_tipo = lista_tipo.tail()
                    parametros_formais = parametros_formais.getTail()
        else:
            resposta = False
            
        ambiente.restaura()
        return resposta
