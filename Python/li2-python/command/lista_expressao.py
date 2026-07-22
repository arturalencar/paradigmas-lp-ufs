from util.lista import Lista
from memory.lista_valor import ListaValor

class ListaExpressao(Lista):
    def __init__(self, expressao=None, lista_expressao=None):
        if expressao is None:
            super().__init__(None, None)
        elif lista_expressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, lista_expressao)

    def avaliar(self, ambiente):
        if self.length() >= 2:
            return ListaValor(self.getHead().avaliar(ambiente), self.getTail().avaliar(ambiente))
        elif self.length() == 1:
            return ListaValor(self.getHead().avaliar(ambiente))
        else:
            return ListaValor()

    def getTipos(self, ambiente):
        result = []
        if self.length() >= 2:
            result.append(self.getHead().getTipo(ambiente))
            result.extend(self.getTail().getTipos(ambiente))
        elif self.length() == 1:
            result.append(self.getHead().getTipo(ambiente))
        return result
