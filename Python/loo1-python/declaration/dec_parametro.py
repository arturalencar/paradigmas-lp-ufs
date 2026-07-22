class DecParametro:
    def __init__(self, id_param, tipo):
        self.id_param = id_param
        self.tipo = tipo

    def getId(self):
        return self.id_param

    def getTipo(self):
        return self.tipo

    def checaTipo(self, ambiente):
        return self.tipo.eValido(ambiente)

    def elabora(self, ambiente):
        ambiente.map(self.id_param, self.tipo)
        return ambiente
