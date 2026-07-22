from expression.acesso_atributo import AcessoAtributo

class AcessoAtributoId(AcessoAtributo):
    def __init__(self, av, id_atributo):
        super().__init__(id_atributo)
        self.av = av

    def avaliar(self, ambiente):
        return self._obterValorDeIdNoAmbiente(ambiente)

    def getExpressaoObjeto(self):
        return self.av

    def checaTipo(self, ambiente):
        if self.av.checaTipo(ambiente):
            try:
                tipo = self.av.getTipo(ambiente)
                def_classe = ambiente.getDefClasse(tipo.getTipo())
                def_classe.getTipoAtributo(self.getId())
                return True
            except Exception:
                return False
        return False

    def getTipo(self, ambiente):
        nome_classe = self.av.getTipo(ambiente).getTipo()
        def_classe = ambiente.getDefClasse(nome_classe)
        tipo_atr = def_classe.getTipoAtributo(self.getId())
        return tipo_atr

    def getAv(self):
        return self.av

    def _obterValorDeIdNoAmbiente(self, ambiente):
        referencia = self.av.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        aux = objeto.getEstado()
        return aux.get(self.getId())
