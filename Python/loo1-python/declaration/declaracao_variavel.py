from declaration.declaracao import Declaracao
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class DeclaracaoVariavel(Declaracao):
    def __init__(self, *args):
        if len(args) == 3:
            # OO1: SimplesDecVariavel(tipo, id, expressao)
            self.tipo = args[0]
            self.id = args[1]
            self.expressao = args[2]
        elif len(args) == 2:
            # Imperativa: DeclaracaoVariavel(id, expressao)
            self.tipo = None
            self.id = args[0]
            self.expressao = args[1]
        else:
            raise ValueError("DeclaracaoVariavel expects 2 or 3 arguments")

    def getTipo(self, id_var=None):
        if id_var is not None:
            if self.id == id_var:
                return self.tipo
            else:
                raise VariavelNaoDeclaradaException(str(id_var))
        return self.tipo

    def elabora(self, ambiente):
        ambiente.map(self.getId(), self.getExpressao().avaliar(ambiente))
        return ambiente

    def getExpressao(self):
        return self.expressao

    def getId(self):
        return self.id

    def checaTipo(self, ambiente) -> bool:
        if self.tipo is not None:
            # Versão OO1 com tipo explícito
            from util.tipo_classe import TipoClasse
            resposta = False
            if self.expressao.checaTipo(ambiente):
                if isinstance(self.tipo, TipoClasse):
                    resposta = (self.expressao.getTipo(ambiente) == TipoClasse.TIPO_NULL or
                                self.expressao.getTipo(ambiente) == self.tipo)
                else:
                    resposta = self.expressao.getTipo(ambiente) == self.tipo
            if resposta:
                ambiente.map(self.getId(), self.tipo)
            return resposta
        else:
            # Versão imperativa sem tipo explícito
            result = self.getExpressao().checaTipo(ambiente)
            if result:
                ambiente.map(self.getId(), self.getExpressao().getTipo(ambiente))
            return result
