from util.tipo import Tipo

class TipoClasse(Tipo):
    TIPO_NULL = None  # Will be initialized below

    def __init__(self, id_classe):
        self.id_classe = id_classe

    def eValido(self, ambiente=None):
        if ambiente is None:
            return self.id_classe is not None
        try:
            ambiente.getDefClasse(self.id_classe)
            return True
        except Exception:
            return False

    def getTipo(self):
        return self.id_classe

    def getNome(self):
        if self.id_classe is None:
            return "null"
        return self.id_classe.getIdName()

    def eInteiro(self):
        return False

    def eBooleano(self):
        return False

    def eString(self):
        return False

    def eIgual(self, tipo):
        if isinstance(tipo, TipoClasse):
            if self.id_classe is None or tipo.id_classe is None:
                return True
            return self.id_classe == tipo.id_classe
        return False

    def intersecao(self, outroTipo):
        if self.eIgual(outroTipo):
            return self
        return None

    def __eq__(self, other):
        if isinstance(other, TipoClasse):
            if self.id_classe is None or other.id_classe is None:
                return True
            return self.id_classe == other.id_classe
        return False

    def __hash__(self):
        if self.id_classe is None:
            return hash(None)
        return hash(self.id_classe)

    def __str__(self):
        return self.getNome()

TipoClasse.TIPO_NULL = TipoClasse(None)
