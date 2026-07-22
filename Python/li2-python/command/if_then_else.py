from command.comando import Comando
from util.tipo_primitivo import TipoPrimitivo

class IfThenElse(Comando):
    def __init__(self, expressao, comando_then, comando_else):
        self.expressao = expressao
        self.comando_then = comando_then
        self.comando_else = comando_else

    def executar(self, ambiente):
        if self.expressao.avaliar(ambiente).valor():
            return self.comando_then.executar(ambiente)
        else:
            return self.comando_else.executar(ambiente)

    def checaTipo(self, ambiente):
        if self.expressao.getTipo(ambiente).eBooleano():
            return self.comando_then.checaTipo(ambiente) and self.comando_else.checaTipo(ambiente)
        return False
