from util.tipo import Tipo

class TipoProcedimento(Tipo):
    def __init__(self, tipos_parametros):
        self.tipos_parametros = tipos_parametros
        
    def getNome(self):
        return "procedimento"

    def eValido(self):
        return True

    def equals(self, outro_tipo):
        if not isinstance(outro_tipo, TipoProcedimento):
            return False
        if len(self.tipos_parametros) != len(outro_tipo.tipos_parametros):
            return False
        for t1, t2 in zip(self.tipos_parametros, outro_tipo.tipos_parametros):
            if t1 != t2 and not t1.equals(t2):
                return False
        return True
        
    def __eq__(self, outro):
        return self.equals(outro)
