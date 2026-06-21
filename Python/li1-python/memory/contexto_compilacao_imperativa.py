from memory.contexto_compilacao import ContextoCompilacao
from memory.ambiente_compilacao_imperativa import AmbienteCompilacaoImperativa
from memory.entrada_vazia_exception import EntradaVaziaException

class ContextoCompilacaoImperativa(ContextoCompilacao, AmbienteCompilacaoImperativa):
    def __init__(self, entrada):
        super().__init__()
        self.entrada = entrada

    def getTipoEntrada(self):
        if self.entrada is None or self.entrada.getHead() is None:
            raise EntradaVaziaException()
        aux = self.entrada.getHead().getTipo(self)
        self.entrada = self.entrada.getTail()
        return aux
