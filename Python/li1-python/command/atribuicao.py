from command.comando import Comando
from expression.expressao import Expressao
from expression.id import Id

class Atribuicao(Comando):
    def __init__(self, idArg: Id, expressao: Expressao):
        self.id = idArg
        self.expressao = expressao

    def executar(self, ambiente):
        ambiente.changeValor(self.id, self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self.expressao.checaTipo(ambiente) and \
               self.id.getTipo(ambiente).eIgual(self.expressao.getTipo(ambiente))
