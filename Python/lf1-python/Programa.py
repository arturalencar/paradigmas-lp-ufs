from memory.contexto_compilacao import ContextoCompilacao
from memory.contexto_execucao_funcional import ContextoExecucaoFuncional


class Programa:
    """
    Equivalente ao Programa.java do lf1.
    Usa ContextoExecucaoFuncional (em vez de ContextoExecucao simples)
    para suportar mapeamento de funções além de variáveis.
    """

    def __init__(self, exp):
        self._exp = exp

    def executar(self):
        """Avalia a expressão num ambiente de execução funcional."""
        amb_exec = ContextoExecucaoFuncional()
        return self._exp.avaliar(amb_exec)

    def checa_tipo(self) -> bool:
        """Verifica os tipos da expressão num ambiente de compilação."""
        amb_comp = ContextoCompilacao()
        return self._exp.checa_tipo(amb_comp)

    @property
    def expressao(self):
        return self._exp
