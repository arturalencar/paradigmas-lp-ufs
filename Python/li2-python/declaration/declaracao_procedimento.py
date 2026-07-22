from declaration.declaracao import Declaracao

class DeclaracaoProcedimento(Declaracao):
    def __init__(self, id, def_procedimento):
        self.id = id
        self.def_procedimento = def_procedimento

    def elabora(self, ambiente):
        ambiente.mapProcedimento(self.id, self.def_procedimento)
        return ambiente

    def getId(self):
        return self.id

    def checaTipo(self, ambiente):
        ambiente.map(self.id, self.def_procedimento.getTipo())
        parametros_formais = self.def_procedimento.getParametrosFormais()
        if parametros_formais.checaTipo(ambiente):
            ambiente.incrementa()
            ambiente = parametros_formais.elabora(ambiente)
            resposta = self.def_procedimento.getComando().checaTipo(ambiente)
            ambiente.restaura()
        else:
            resposta = False
        return resposta

    def getDefProcedimento(self):
        return self.def_procedimento
