from declaration.dec_procedimento import DecProcedimento
from command.procedimento import Procedimento
from exception.procedimento_nao_declarado_exception import ProcedimentoNaoDeclaradoException

class DecProcedimentoSimples(DecProcedimento):
    def __init__(self, nome, parametros_formais, comando):
        self.nome = nome
        self.parametros_formais = parametros_formais
        self.comando = comando

    def getProcedimento(self, nome_metodo):
        if self.nome == nome_metodo:
            return Procedimento(self.parametros_formais, self.comando)
        else:
            raise ProcedimentoNaoDeclaradoException(nome_metodo.getIdName())

    def elabora(self, ambiente):
        ambiente.map(self.nome, Procedimento(self.parametros_formais, self.comando))
        return ambiente

    def checaTipo(self, ambiente):
        resposta = False
        ambiente.incrementa()
        ambiente.map(self.nome, Procedimento(self.parametros_formais, self.comando))
        try:
            if self.parametros_formais.checaTipo(ambiente):
                ambiente_aux = self.parametros_formais.elabora(ambiente)
                if self.comando.checaTipo(ambiente_aux):
                    resposta = True
        except Exception:
            resposta = False
        finally:
            ambiente.restaura()
            
        return resposta
