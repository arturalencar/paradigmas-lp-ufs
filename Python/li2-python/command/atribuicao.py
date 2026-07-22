from command.comando import Comando

class Atribuicao(Comando):
    def __init__(self, id, expressao):
        self.id = id
        self.expressao = expressao

    def executar(self, ambiente):
        ambiente.changeValor(self.id, self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente):
        tipo_variavel = ambiente.get(self.id)
        tipo_expressao = self.expressao.getTipo(ambiente)
        return tipo_variavel.eIgual(tipo_expressao)
