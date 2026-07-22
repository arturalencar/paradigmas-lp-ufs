from command.io_comando import IO

class Write(IO):
    def __init__(self, expressao):
        self.expressao = expressao

    def executar(self, ambiente):
        ambiente.write(self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente):
        return self.expressao.checaTipo(ambiente) # assuming expressao has checaTipo
