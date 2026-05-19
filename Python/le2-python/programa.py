from contexto_execucao import ContextoExecucao
from contexto_compilacao import ContextoCompilacao


class Programa:
    def __init__(self, exp):
        self._exp = exp

    def executar(self):
        amb_exec = ContextoExecucao()
        return self._exp.avaliar(amb_exec)

    def checa_tipo(self) -> bool:
        amb_comp = ContextoCompilacao()
        return self._exp.checa_tipo(amb_comp)

    @property
    def expressao(self):
        return self._exp
