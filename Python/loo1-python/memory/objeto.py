from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class Objeto:
    def __init__(self, classe_objeto, estado_obj):
        self.classe_objeto = classe_objeto
        self.estado = estado_obj

    def getClasse(self):
        return self.classe_objeto

    def getEstado(self):
        return self.estado

    def setEstado(self, novo_estado):
        self.estado = novo_estado

    def mapThis(self, vr):
        from expression.id import Id
        id_this = Id("this")
        if self.estado.containsKey(id_this):
            self.estado.remove(id_this)
        self.estado.put(id_this, vr)

    def changeAtributo(self, id_variavel, valor):
        if self.estado.containsKey(id_variavel):
            self.estado.remove(id_variavel)
            self.estado.put(id_variavel, valor)
        else:
            raise VariavelNaoDeclaradaException(id_variavel.getIdName())
