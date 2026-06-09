from memory.contexto import Contexto
from memory.ambiente_compilacao import AmbienteCompilacao


class ContextoCompilacao(Contexto, AmbienteCompilacao):

    def __init__(self):
        super().__init__()
