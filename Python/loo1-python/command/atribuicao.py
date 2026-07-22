from command.comando import Comando
from expression.acesso_atributo import AcessoAtributo

class Atribuicao(Comando):
    def __init__(self, av, expressao):
        self.av = av
        self.expressao = expressao

    def executar(self, ambiente):
        id_variavel = self.av.getId()
        if isinstance(self.av, AcessoAtributo):
            exp_av = self.av.getExpressaoObjeto()
            referencia = exp_av.avaliar(ambiente)
            obj = ambiente.getObjeto(referencia)
            obj.changeAtributo(id_variavel, self.expressao.avaliar(ambiente))
        else:
            ambiente.changeValor(id_variavel, self.expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente):
        from util.tipo_classe import TipoClasse
        return self.expressao.checaTipo(ambiente) and (
            self.av.getTipo(ambiente) == self.expressao.getTipo(ambiente) or
            self.expressao.getTipo(ambiente) == TipoClasse.TIPO_NULL
        )
