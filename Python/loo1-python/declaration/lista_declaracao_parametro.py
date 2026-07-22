class ListaDeclaracaoParametro:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def length(self):
        if self.head is None:
            return 0
        if self.tail is None:
            return 1
        return 1 + self.tail.length()

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def checaTipo(self, ambiente):
        if self.head is None:
            return True
        if self.tail is None:
            return self.head.checaTipo(ambiente)
        return self.head.checaTipo(ambiente) and self.tail.checaTipo(ambiente)

    def elabora(self, ambiente):
        if self.head is not None:
            ambiente = self.head.elabora(ambiente)
        if self.tail is not None:
            ambiente = self.tail.elabora(ambiente)
        return ambiente
