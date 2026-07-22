from command.comando import Comando
from util.tipo_procedimento import TipoProcedimento

class ChamadaProcedimento(Comando):
    def __init__(self, nome_procedimento, parametros_reais):
        self.nome_procedimento = nome_procedimento
        self.parametros_reais = parametros_reais

    def executar(self, ambiente):
        procedimento = ambiente.getProcedimento(self.nome_procedimento)
        ambiente.incrementa()
        parametros_formais = procedimento.getParametrosFormais()
        ambiente = self._bindParameters(ambiente, parametros_formais)
        ambiente = procedimento.getComando().executar(ambiente)
        ambiente.restaura()
        return ambiente

    def _bindParameters(self, ambiente, parametros_formais):
        lista_valor = self.parametros_reais.avaliar(ambiente)
        while lista_valor is not None and lista_valor.length() > 0:
            ambiente.map(parametros_formais.getHead().getId(), lista_valor.getHead())
            parametros_formais = parametros_formais.getTail()
            lista_valor = lista_valor.getTail()
        return ambiente

    def checaTipo(self, ambiente):
        tipo_procedimento = ambiente.get(self.nome_procedimento)
        tipo_parametros_reais = TipoProcedimento(self.parametros_reais.getTipos(ambiente))
        if tipo_procedimento is None:
            return False
        return tipo_procedimento.eIgual(tipo_parametros_reais)
