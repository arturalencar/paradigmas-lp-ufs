from expression.acesso_atributo import AcessoAtributo

class AcessoAtributoThis(AcessoAtributo):
    def __init__(self, this_expressao, id_atributo):
        super().__init__(id_atributo)
        self.this_expressao = this_expressao

    def avaliar(self, ambiente):
        return self._obterValorDeIdNoAmbiente(ambiente)

    def getExpressaoObjeto(self):
        return self.this_expressao

    def checaTipo(self, ambiente):
        try:
            tipo = self.this_expressao.getTipo(ambiente)
            def_classe = ambiente.getDefClasse(tipo.getTipo())
            def_classe.getTipoAtributo(self.getId())
            return True
        except Exception:
            return False

    def getTipo(self, ambiente):
        nome_classe = self.this_expressao.getTipo(ambiente).getTipo()
        def_classe = ambiente.getDefClasse(nome_classe)
        return def_classe.getTipoAtributo(self.getId())

    def getThis(self):
        return self.this_expressao

    def _obterValorDeIdNoAmbiente(self, ambiente):
        referencia = self.this_expressao.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        aux = objeto.getEstado()
        return aux.get(self.getId())
