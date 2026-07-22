from exception.entrada_vazia_exception import EntradaVaziaException

class Programa:
    def __init__(self, dec_classe, comando):
        self.dec_classe = dec_classe
        self.comando = comando

    def executar(self, ambiente):
        if ambiente is None:
            raise Exception("Ambiente nao fornecido")

        ambiente = self.comando.executar(self.dec_classe.elabora(ambiente))
        return ambiente.getSaida()

    def checaTipo(self, ambiente):
        if ambiente is None:
            raise Exception("Ambiente nao fornecido")

        return self.dec_classe.checaTipo(ambiente) and self.comando.checaTipo(ambiente)
