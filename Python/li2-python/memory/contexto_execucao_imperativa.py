from memory.contexto_execucao import ContextoExecucao
from memory.ambiente_execucao_imperativa import AmbienteExecucaoImperativa
from exception.entrada_vazia_exception import EntradaVaziaException
from memory.lista_valor import ListaValor

class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):
    def __init__(self, entrada=None):
        super().__init__()
        self.entrada = entrada if entrada is not None else ListaValor()
        self.saida = ListaValor()

    def read(self):
        if self.entrada is None or self.entrada.getHead() is None:
            raise EntradaVaziaException()
        valor = self.entrada.getHead()
        self.entrada = self.entrada.getTail()
        return valor

    def write(self, valor):
        if self.saida is None:
            self.saida = ListaValor(valor)
        else:
            atual = self.saida
            while atual.getTail() is not None and atual.getTail().getHead() is not None:
                atual = atual.getTail()
            if atual.getHead() is None:
                self.saida = ListaValor(valor)
            else:
                atual.tail = ListaValor(valor)

    def getSaida(self):
        return self.saida

    def changeValor(self, idArg, valorId):
        from exception.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
        encontrou = False
        for escopo in reversed(self.pilha):
            if idArg.getNome() in escopo:
                escopo[idArg.getNome()] = valorId
                encontrou = True
                break
        if not encontrou:
            raise VariavelNaoDeclaradaException(idArg.getNome())
