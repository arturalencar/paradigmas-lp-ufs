class DeclaracaoParametro:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def checaTipo(self, ambiente):
        return self.tipo.eValido()

    def elabora(self, ambiente):
        ambiente.map(self.id, self.tipo)
        return ambiente
