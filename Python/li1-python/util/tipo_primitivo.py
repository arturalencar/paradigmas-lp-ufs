from util.tipo import Tipo

class TipoPrimitivo(Tipo):
    INTEIRO = None
    BOOLEANO = None
    STRING = None

    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self) -> str:
        return self.nome

    def eInteiro(self) -> bool:
        return self.eIgual(TipoPrimitivo.INTEIRO)

    def eBooleano(self) -> bool:
        return self.eIgual(TipoPrimitivo.BOOLEANO)

    def eString(self) -> bool:
        return self.eIgual(TipoPrimitivo.STRING)

    def eIgual(self, tipo: Tipo) -> bool:
        ret = False
        if self.eValido():
            if tipo.eValido():
                ret = self.nome == tipo.getNome()
            else:
                ret = tipo.eIgual(self)
        return ret

    def eValido(self) -> bool:
        return self.nome is not None and len(self.nome) > 0

    def intersecao(self, outroTipo: Tipo) -> Tipo:
        if outroTipo.eIgual(self):
            return self
        else:
            return None

    def __str__(self) -> str:
        return self.nome

TipoPrimitivo.INTEIRO = TipoPrimitivo("INTEIRO")
TipoPrimitivo.BOOLEANO = TipoPrimitivo("BOOLEANO")
TipoPrimitivo.STRING = TipoPrimitivo("STRING")
