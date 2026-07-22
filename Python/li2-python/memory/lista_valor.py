from util.lista import Lista

class ListaValor(Lista):
    def __init__(self, valor=None, lista_valor=None):
        if valor is None:
            super().__init__(None, None)
        elif lista_valor is None:
            super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, lista_valor)
