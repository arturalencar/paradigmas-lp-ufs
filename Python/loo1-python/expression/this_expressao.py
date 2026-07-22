class This:
    def avaliar(self, ambiente):
        return self._obterValorDoObjetoThisNoAmbiente(ambiente)

    def checaTipo(self, ambiente):
        return True

    def getTipo(self, ambiente):
        from expression.id import Id
        return ambiente.get(Id("this"))

    def _obterValorDoObjetoThisNoAmbiente(self, ambiente):
        from expression.id import Id
        return ambiente.getValor(Id("this"))
