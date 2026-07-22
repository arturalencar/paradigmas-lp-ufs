from util.lista import Lista

class ListaDeclaracaoParametro(Lista):
    def __init__(self, declaracao=None, lista_declaracao=None):
        if declaracao is None:
            super().__init__(None, None)
        else:
            super().__init__(declaracao, lista_declaracao)

    def checaTipo(self, ambiente):
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getHead().checaTipo(ambiente) and self.getTail().checaTipo(ambiente)
            else:
                return self.getHead().checaTipo(ambiente)
        else:
            return True

    def elabora(self, ambiente):
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().elabora(self.getHead().elabora(ambiente))
            else:
                return self.getHead().elabora(ambiente)
        else:
            return ambiente

    def getTipos(self):
        retorno = []
        head_temp = self.getHead()
        tail_temp = self.getTail()

        while head_temp is not None:
            retorno.append(head_temp.getTipo())
            if tail_temp is not None:
                head_temp = tail_temp.getHead()
                tail_temp = tail_temp.getTail()
            else:
                head_temp = None

        return retorno
