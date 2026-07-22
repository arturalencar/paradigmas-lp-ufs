from command.comando import Comando
from declaration.declaracao import Declaracao

class ComandoDeclaracao(Comando):
    def __init__(self, declaracao: Declaracao, comando: Comando):
        self.declaracao = declaracao
        self.comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self.comando.executar(self.declaracao.elabora(ambiente))
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        ambiente.incrementa()
        resposta = self.declaracao.checaTipo(ambiente) and self.comando.checaTipo(ambiente)
        ambiente.restaura()
        return resposta
