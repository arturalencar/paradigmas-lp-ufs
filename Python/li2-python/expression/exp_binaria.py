from expression.expressao import Expressao

class ExpBinaria(Expressao):
    def __init__(self, esq, dir):
        self.esq = esq
        self.dir = dir
        self.operador = ""

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def getOperador(self):
        return self.operador
