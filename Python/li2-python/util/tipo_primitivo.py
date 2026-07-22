from util.tipo import Tipo

class TipoPrimitivo(Tipo):
    TIPO_INTEIRO = 1
    TIPO_BOOLEANO = 2
    TIPO_STRING = 3

    def __init__(self, tipo):
        self.tipo = tipo

    def getNome(self):
        if self.tipo == self.TIPO_INTEIRO:
            return "inteiro"
        if self.tipo == self.TIPO_BOOLEANO:
            return "booleano"
        if self.tipo == self.TIPO_STRING:
            return "string"
        return "tipoVazio"

    def eInteiro(self):
        return self.tipo == self.TIPO_INTEIRO

    def eBooleano(self):
        return self.tipo == self.TIPO_BOOLEANO

    def eString(self):
        return self.tipo == self.TIPO_STRING

    def eValido(self):
        return self.tipo in [self.TIPO_INTEIRO, self.TIPO_BOOLEANO, self.TIPO_STRING]

    def eIgual(self, tipo):
        if isinstance(tipo, TipoPrimitivo):
            return self.tipo == tipo.tipo
        return False

    def intersecao(self, outroTipo):
        if outroTipo.eIgual(self):
            return self
        else:
            return None

    @classmethod
    def inteiro(cls):
        return cls(cls.TIPO_INTEIRO)

    @classmethod
    def booleano(cls):
        return cls(cls.TIPO_BOOLEANO)

    @classmethod
    def string(cls):
        return cls(cls.TIPO_STRING)
