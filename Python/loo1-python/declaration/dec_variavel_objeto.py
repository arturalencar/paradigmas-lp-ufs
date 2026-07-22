from declaration.dec_variavel import DecVariavel
from command.new import New
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class DecVariavelObjeto(DecVariavel):
    def __init__(self, tipo, objeto, classe):
        self.tipo = tipo
        self.objeto = objeto
        self.classe = classe

    def getTipo(self, id_var=None):
        if id_var is not None:
            if self.objeto == id_var:
                return self.tipo
            else:
                raise VariavelNaoDeclaradaException(str(id_var))
        return self.tipo

    def elabora(self, ambiente):
        from declaration.declaracao_variavel import DeclaracaoVariavel
        from expression.valor_null import ValorNull

        aux = DeclaracaoVariavel(self.tipo, self.objeto, ValorNull()).elabora(ambiente)
        aux = New(self.objeto, self.classe).executar(aux)
        return aux

    def checaTipo(self, ambiente):
        from util.tipo_classe import TipoClasse
        tp_classe = TipoClasse(self.classe)
        if tp_classe.eValido(ambiente) and self.tipo.eValido(ambiente):
            resposta = tp_classe == self.tipo
            if resposta:
                ambiente.map(self.objeto, tp_classe)
            return resposta
        return False
