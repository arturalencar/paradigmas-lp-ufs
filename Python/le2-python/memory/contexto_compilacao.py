from contexto import Contexto
from ambiente_compilacao import AmbienteCompilacao


class ContextoCompilacao(Contexto, AmbienteCompilacao):

    def __init__(self):
        super().__init__()
