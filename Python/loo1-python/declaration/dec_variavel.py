from declaration.declaracao import Declaracao

class DecVariavel(Declaracao):
    def getTipo(self, id_var):
        raise NotImplementedError()
