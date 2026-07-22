class This:
    def avaliar(self, ambiente):
        return self._obterValorDoObjetoThisNoAmbiente(ambiente)

    def checaTipo(self, ambiente):
        return True

    def getTipo(self, ambiente):
        from expression.id import Id
        try:
            return ambiente.get(Id("this"))
        except Exception as e:
            print("This.getTipo ERROR:", e)
            print("Pilha:", [ {k.getIdName() if hasattr(k, 'getIdName') else str(k): str(v)} for d in ambiente.getPilha() for k,v in d.items() ])
            raise e

    def _obterValorDoObjetoThisNoAmbiente(self, ambiente):
        from expression.id import Id
        return ambiente.getValor(Id("this"))
