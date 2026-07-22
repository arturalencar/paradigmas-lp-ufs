from util.tipo import Tipo

class TipoProcedimento(Tipo):
    def __init__(self, tipos_parametros_formais):
        self.tipos_parametros_formais = list(tipos_parametros_formais)

    def eBooleano(self):
        return False

    def eIgual(self, tipo):
        if isinstance(tipo, TipoProcedimento):
            if len(self.tipos_parametros_formais) != len(tipo.tipos_parametros_formais):
                return False
            for t1, t2 in zip(self.tipos_parametros_formais, tipo.tipos_parametros_formais):
                if not t1.eIgual(t2):
                    return False
            return True
        return tipo.eIgual(self)

    def eInteiro(self):
        return False

    def eString(self):
        return False

    def eValido(self):
        retorno = True
        for tipo in self.tipos_parametros_formais:
            retorno = retorno and tipo.eValido()
        return retorno

    def getNome(self):
        return "{" + ",".join([t.getNome() for t in self.tipos_parametros_formais]) + "}"

    def intersecao(self, outroTipo):
        if outroTipo.eIgual(self):
            return self
        else:
            return None
