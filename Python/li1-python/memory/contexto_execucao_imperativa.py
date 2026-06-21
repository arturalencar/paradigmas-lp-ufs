from memory.contexto_execucao import ContextoExecucao
from memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from memory.ambiente_execucao_imperativa import AmbienteExecucaoImperativa
from memory.lista_valor import ListaValor
from memory.entrada_vazia_exception import EntradaVaziaException

class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):
    def __init__(self, entrada):
        super().__init__()
        self.entrada = entrada
        self.saida = ListaValor()

    def read(self):
        if self.entrada is None or self.entrada.getHead() is None:
            raise EntradaVaziaException()
        aux = self.entrada.getHead()
        self.entrada = self.entrada.getTail()
        return aux

    def getSaida(self):
        return self.saida

    def write(self, v):
        self.saida.write(v)

    def changeValor(self, idArg, valorId):
        encontrado = False
        for d in reversed(self.pilha):
            if idArg in d:
                d[idArg] = valorId
                encontrado = True
                break
        if not encontrado:
            raise VariavelNaoDeclaradaException(idArg)
