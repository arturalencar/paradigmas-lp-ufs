from memory.contexto_compilacao import ContextoCompilacao
from memory.ambiente_compilacao_imperativa import AmbienteCompilacaoImperativa

class ContextoCompilacaoImperativa(ContextoCompilacao, AmbienteCompilacaoImperativa):
    def __init__(self, lista=None):
        super().__init__()
        self.entrada = lista
