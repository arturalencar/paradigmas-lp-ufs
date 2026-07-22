from expression.valor import Valor

class ValorConcreto(Valor):
    def __init__(self, valor):
        self.valor_interno = valor

    def valor(self):
        return self.valor_interno

    def avaliar(self, ambiente):
        return self

    def __eq__(self, outro):
        if isinstance(outro, ValorConcreto):
            return self.valor_interno == outro.valor_interno
        return False

    def __str__(self):
        return str(self.valor_interno)
