from memory.contexto_execucao_imperativa import ContextoExecucaoImperativa
from memory.ambiente_execucao_imperativa2 import AmbienteExecucaoImperativa2
from memory.contexto import Contexto
from exception.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from exception.procedimento_ja_declarado_exception import ProcedimentoJaDeclaradoException
from exception.procedimento_nao_declarado_exception import ProcedimentoNaoDeclaradoException

class ContextoExecucaoImperativa2(ContextoExecucaoImperativa, AmbienteExecucaoImperativa2):
    def __init__(self, entrada=None):
        super().__init__(entrada)
        self.contexto_procedimentos = Contexto()

    def incrementa(self):
        super().incrementa()
        self.contexto_procedimentos.incrementa()

    def restaura(self):
        super().restaura()
        self.contexto_procedimentos.restaura()

    def mapProcedimento(self, idArg, procedimentoId):
        try:
            self.contexto_procedimentos.map(idArg, procedimentoId)
        except VariavelJaDeclaradaException:
            raise ProcedimentoJaDeclaradoException(idArg)

    def getProcedimento(self, idArg):
        try:
            return self.contexto_procedimentos.get(idArg)
        except VariavelNaoDeclaradaException:
            raise ProcedimentoNaoDeclaradoException(idArg)
