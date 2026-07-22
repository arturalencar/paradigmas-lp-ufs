from memory.lista_valor import ListaValor
from util.lista_tipo import ListaTipo

class ListaExpressao:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def avaliar(self, ambiente):
        if self.head is None:
            return ListaValor()
        
        valor = self.head.avaliar(ambiente)
        
        if self.tail is None:
            return ListaValor(valor)
            
        return ListaValor(valor, self.tail.avaliar(ambiente))

    def getTipos(self, ambiente):
        if self.head is None:
            return ListaTipo()
            
        tipo = self.head.getTipo(ambiente)
        
        if self.tail is None:
            return ListaTipo(tipo)
            
        return ListaTipo(tipo, self.tail.getTipos(ambiente))

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail
