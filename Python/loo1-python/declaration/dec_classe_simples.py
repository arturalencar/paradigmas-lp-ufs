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
        resposta = False
        ambiente.incrementa()
        ambiente.mapDefClasse(self.id_classe, DefClasse(self.id_classe, self.dec_variavel, self.dec_procedimento))
        try:
            if self.dec_variavel.checaTipo(ambiente):
                ambiente_aux = self.dec_variavel.elabora(ambiente)
                if self.dec_procedimento.checaTipo(ambiente_aux):
                    resposta = True
        except Exception:
            resposta = False
        finally:
            ambiente.restaura()
            
        return resposta
