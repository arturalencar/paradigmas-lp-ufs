import pickle
import os

class WriteFile:
    def __init__(self, id, dir_exp):
        self.id = id
        self.dir = dir_exp

    def executar(self, ambiente):
        path = str(self.dir.avaliar(ambiente))
        object_ref = self.id.avaliar(ambiente)
        object_val = ambiente.getObjeto(object_ref)
        
        try:
            if os.path.exists(path) and os.path.isfile(path) and os.path.getsize(path) > 0:
                with open(path, 'ab') as f:
                    pickle.dump(object_val, f)
            else:
                with open(path, 'wb') as f:
                    pickle.dump(object_val, f)
        except Exception as exc:
            import traceback
            traceback.print_exc()
            
        return ambiente

    def checaTipo(self, ambiente):
        return self.id.checaTipo(ambiente)
