from declaration.declaracao import Declaracao

class DeclaracaoComposta(Declaracao):
    def __init__(self, parametro1: Declaracao, parametro2: Declaracao):
        self.declaracao1 = parametro1
        self.declaracao2 = parametro2

    def elabora(self, ambiente):
        return self.declaracao2.elabora(self.declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente) -> bool:
        return self.declaracao1.checaTipo(ambiente) and self.declaracao2.checaTipo(ambiente)
