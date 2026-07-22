from command.comando import Comando

class SequenciaComando(Comando):
    def __init__(self, comando1, comando2):
        self.comando1 = comando1
        self.comando2 = comando2

    def executar(self, ambiente):
        return self.comando2.executar(self.comando1.executar(ambiente))

    def checaTipo(self, ambiente):
        return self.comando1.checaTipo(ambiente) and self.comando2.checaTipo(ambiente)
