import pickle
import os

class ReadFile:
    def __init__(self, id, dir_exp, index):
        self.id = id
        self.dir = dir_exp
        self.index = index
        self.tipo_id = None

    def executar(self, ambiente):
        path = str(self.dir.avaliar(ambiente))
        objetos = []
        try:
            with open(path, 'rb') as f:
                while True:
                    try:
                        objetos.append(pickle.load(f))
                    except EOFError:
                        break
            
            prox_ref = ambiente.getProxRef()
            pos = int(str(self.index.avaliar(ambiente)))
            
            ambiente.mapObjeto(prox_ref, objetos[pos])
            ambiente.changeValor(self.id, prox_ref)
        except Exception as exc:
            import traceback
            traceback.print_exc()
            
        return ambiente

    def checaTipo(self, ambiente):
        self.tipo_id = self.id.getTipo(ambiente)
        return self.id.checaTipo(ambiente)
