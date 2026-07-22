from command.io_comando import IO
from expression.expressao import Expressao

class Write(IO):
    def __init__(self, expressao: Expressao):
        self.expressao = expressao

    def executar(self, ambiente):
        ambiente.write(self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self.expressao.checaTipo(ambiente)
