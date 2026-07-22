from command.comando import Comando

class While(Comando):
    def __init__(self, expressao, comando):
        self.expressao = expressao
        self.comando = comando

    def executar(self, ambiente):
        while self.expressao.avaliar(ambiente).valor():
            ambiente = self.comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente):
        if self.expressao.getTipo(ambiente).eBooleano():
            return self.comando.checaTipo(ambiente)
        return False
