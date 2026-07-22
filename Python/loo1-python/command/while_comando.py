from command.comando import Comando
from expression.expressao import Expressao

class While(Comando):
    def __init__(self, expressao: Expressao, comando: Comando):
        self.expressao = expressao
        self.comando = comando

    def executar(self, ambiente):
        while self.expressao.avaliar(ambiente).valor():
            ambiente = self.comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self.expressao.checaTipo(ambiente) and \
               self.expressao.getTipo(ambiente).eBooleano() and \
               self.comando.checaTipo(ambiente)
