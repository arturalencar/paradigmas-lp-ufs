class ValorNull:
    def valor(self):
        return None

    def __str__(self):
        return "null"

    def avaliar(self, ambiente):
        return self

    def checaTipo(self, ambiente):
        return True

    def getTipo(self, ambiente):
        from util.tipo_classe import TipoClasse
        return TipoClasse.TIPO_NULL

    def isEquals(self, obj):
        return isinstance(obj, ValorNull)
