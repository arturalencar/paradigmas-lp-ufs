class DefClasse:
    def __init__(self, id_classe, dec_variavel, dec_procedimento):
        self.id_classe = id_classe
        self.dec_variavel = dec_variavel
        self.dec_procedimento = dec_procedimento

    def getDecVariavel(self):
        return self.dec_variavel

    def getMetodo(self, id_metodo):
        return self.dec_procedimento.getProcedimento(id_metodo)

    def getTipoAtributo(self, id_atributo):
        return self.dec_variavel.getTipo(id_atributo)

    def getIdClasse(self):
        return self.id_classe
