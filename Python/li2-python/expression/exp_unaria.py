from expression.expressao import Expressao

class ExpUnaria(Expressao):
    def __init__(self, expressao):
        self.exp = expressao
        self.operador = ""

    def getExp(self):
        return self.exp

    def getOperador(self):
        return self.operador
