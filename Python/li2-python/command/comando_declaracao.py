from command.comando import Comando

class ComandoDeclaracao(Comando):
    def __init__(self, declaracao, comando):
        self.declaracao = declaracao
        self.comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self.declaracao.elabora(ambiente)
        ambiente = self.comando.executar(ambiente)
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente):
        ambiente.incrementa()
        resposta = self.declaracao.checaTipo(ambiente) and self.comando.checaTipo(ambiente)
        ambiente.restaura()
        return resposta
