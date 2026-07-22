from declaration.dec_classe import DecClasse
from memory.def_classe import DefClasse

class DecClasseSimples(DecClasse):
    def __init__(self, id_classe, dec_variavel, dec_procedimento):
        self.id_classe = id_classe
        self.dec_variavel = dec_variavel
        self.dec_procedimento = dec_procedimento

    def elabora(self, ambiente):
        ambiente.mapDefClasse(self.id_classe, DefClasse(self.id_classe, self.dec_variavel, self.dec_procedimento))
        return ambiente

    def checaTipo(self, ambiente):
        from expression.id import Id
        from util.tipo_classe import TipoClasse
        resposta = False
        ambiente.mapDefClasse(self.id_classe, DefClasse(self.id_classe, self.dec_variavel, self.dec_procedimento))
        ambiente.incrementa()
        try:
            var_checa = self.dec_variavel.checaTipo(ambiente)
            print("dec_variavel.checaTipo:", var_checa)
            if var_checa:
                ambiente.map(Id("this"), TipoClasse(self.id_classe))
                print("Pilha before proc_checa:", [ {k.getIdName() if hasattr(k, 'getIdName') else str(k): str(v)} for d in ambiente.getPilha() for k,v in d.items() ])
                proc_checa = self.dec_procedimento.checaTipo(ambiente)
                print("dec_procedimento.checaTipo:", proc_checa)
                if proc_checa:
                    resposta = True
        except Exception as e:
            print("Exception in DecClasseSimples:", e)
            import traceback
            traceback.print_exc()
            resposta = False
        finally:
            ambiente.restaura()
            
        return resposta
