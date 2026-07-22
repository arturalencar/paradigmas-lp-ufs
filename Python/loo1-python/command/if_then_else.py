from command.comando import Comando
from expression.expressao import Expressao

class IfThenElse(Comando):
    def __init__(self, expressao: Expressao, comandoThen: Comando, comandoElse: Comando):
        self.expressao = expressao
        self.comandoThen = comandoThen
        self.comandoElse = comandoElse

    def executar(self, ambiente):
        if self.expressao.avaliar(ambiente).valor():
            return self.comandoThen.executar(ambiente)
        else:
            return self.comandoElse.executar(ambiente)

    def checaTipo(self, ambiente) -> bool:
        return self.expressao.checaTipo(ambiente) and \
               self.expressao.getTipo(ambiente).eBooleano() and \
               self.comandoThen.checaTipo(ambiente) and \
               self.comandoElse.checaTipo(ambiente)
