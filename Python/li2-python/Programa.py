class Programa:
    def __init__(self, comando):
        self.comando = comando

    def executar(self, ambiente):
        ambiente = self.comando.executar(ambiente)
        return ambiente.getSaida()

    def checaTipo(self, ambiente):
        return self.comando.checaTipo(ambiente)
