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
        res_exp = self.expressao.checaTipo(ambiente)
        tipo_av = self.av.getTipo(ambiente)
        tipo_exp = self.expressao.getTipo(ambiente)
        print("Atribuicao checaTipo:", res_exp, tipo_av.getNome(), tipo_exp.getNome())
        return res_exp and (
            tipo_av == tipo_exp or
            tipo_exp == TipoClasse.TIPO_NULL
        )
