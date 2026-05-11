class Programa:
    def __init__(self, exp):
        self._exp = exp
        
    def executar(self):
        resultado = self._exp.avaliar()
        print(resultado)
        return resultado
        
    def checa_tipo(self) -> bool:
        return self._exp.checa_tipo()

    @property
    def expressao(self):
        return self._exp
    