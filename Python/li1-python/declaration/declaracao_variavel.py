from declaration.declaracao import Declaracao

class DeclaracaoVariavel(Declaracao):
    def __init__(self, idArg, expressao):
        self.id = idArg
        self.expressao = expressao

    def elabora(self, ambiente):
        ambiente.map(self.getId(), self.getExpressao().avaliar(ambiente))
        return ambiente

    def getExpressao(self):
        return self.expressao

    def getId(self):
        return self.id

    def checaTipo(self, ambiente) -> bool:
        result = self.getExpressao().checaTipo(ambiente)
        if result:
            ambiente.map(self.getId(), self.getExpressao().getTipo(ambiente))
        return result
