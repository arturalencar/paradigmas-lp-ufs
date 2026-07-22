from declaration.declaracao import Declaracao

class DeclaracaoComposta(Declaracao):
    def __init__(self, declaracao1, declaracao2):
        self.declaracao1 = declaracao1
        self.declaracao2 = declaracao2

    def elabora(self, ambiente):
        return self.declaracao2.elabora(self.declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente):
        return self.declaracao1.checaTipo(ambiente) and self.declaracao2.checaTipo(ambiente)
