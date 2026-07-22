from declaration.dec_procedimento import DecProcedimento

class DecProcedimentoComposta(DecProcedimento):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def getProcedimento(self, nome_metodo):
        try:
            return self.d1.getProcedimento(nome_metodo)
        except Exception:
            return self.d2.getProcedimento(nome_metodo)

    def elabora(self, ambiente):
        return self.d2.elabora(self.d1.elabora(ambiente))

    def checaTipo(self, ambiente):
        res1 = self.d1.checaTipo(ambiente)
        res2 = self.d2.checaTipo(ambiente)
        print("DecProcedimentoComposta:", res1, res2)
        return res1 and res2
