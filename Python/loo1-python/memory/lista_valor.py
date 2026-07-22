from util.lista import Lista

class ListaValor(Lista):
    def __init__(self, valor=None, listaValor=None):
        if listaValor is None:
            if valor is None:
                super().__init__()
            else:
                super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, listaValor)

    def write(self, valor):
        if self.getHead() is None:
            self.head = valor
            self.tail = ListaValor()
        else:
            self.getTail().write(valor)
