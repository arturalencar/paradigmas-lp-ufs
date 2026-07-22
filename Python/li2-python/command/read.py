from command.io_comando import IO

class Read(IO):
    def __init__(self, id):
        self.id = id

    def executar(self, ambiente):
        ambiente.map(self.id, ambiente.read())
        return ambiente

    def checaTipo(self, ambiente):
        return True # assumimos que a variavel existe e aceita a entrada
