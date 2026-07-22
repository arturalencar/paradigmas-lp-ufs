from declaration.declaracao import Declaracao

class DeclaracaoVariavel(Declaracao):
    def __init__(self, id, expressao):
        self.id = id
        self.expressao = expressao

    def elabora(self, ambiente):
        ambiente.map(self.id, self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente):
        result = self.expressao.checaTipo(ambiente)
        if result:
            ambiente.map(self.id, self.expressao.getTipo(ambiente))
        return result
