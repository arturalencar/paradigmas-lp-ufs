class Procedimento:
    def __init__(self, parametros_formais, comando):
        self.parametros_formais = parametros_formais
        self.comando = comando

    def getParametrosFormais(self):
        return self.parametros_formais

    def getComando(self):
        return self.comando
