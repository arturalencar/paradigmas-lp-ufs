from expression.expressao import Expressao

class Id(Expressao):
    def __init__(self, id_nome):
        self.id_nome = id_nome

    def avaliar(self, ambiente):
        return ambiente.get(self)

    def checaTipo(self, ambiente):
        ambiente.get(self)
        return True

    def getTipo(self, ambiente):
        return ambiente.get(self)

    def getNome(self):
        return self.id_nome

    def __eq__(self, outro):
        if isinstance(outro, Id):
            return self.id_nome == outro.id_nome
        return False

    def __hash__(self):
        return hash(self.id_nome)

    def __str__(self):
        return self.id_nome
