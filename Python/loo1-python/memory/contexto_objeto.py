class ContextoObjeto:
    def __init__(self, estado_hash=None):
        if estado_hash is None:
            self.estado = {}
        else:
            # Shallow copy the dictionary keys and values
            self.estado = estado_hash.copy()

    def remove(self, id_var):
        if id_var in self.estado:
            del self.estado[id_var]

    def put(self, id_var, valor):
        self.estado[id_var] = valor

    def containsKey(self, id_var):
        return id_var in self.estado

    def get(self, id_var):
        return self.estado.get(id_var)
