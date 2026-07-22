from util.tipo_procedimento import TipoProcedimento

class DefProcedimento:
    def __init__(self, parametros_formais, comando):
        self.parametros_formais = parametros_formais
        self.comando = comando

    def getComando(self):
        return self.comando

    def getParametrosFormais(self):
        return self.parametros_formais

    def getTipo(self):
        return TipoProcedimento(self.parametros_formais.getTipos())
