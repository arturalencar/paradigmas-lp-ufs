from command.comando import Comando
from memory.ambiente_execucao_imperativa import AmbienteExecucaoImperativa
from memory.ambiente_compilacao_imperativa import AmbienteCompilacaoImperativa

class Programa:
    def __init__(self, comando: Comando):
        self.comando = comando

    def executar(self, ambienteExecucao: AmbienteExecucaoImperativa):
        ambienteExecucao = self.comando.executar(ambienteExecucao)
        return ambienteExecucao.getSaida()

    def checaTipo(self, ambienteCompilacao: AmbienteCompilacaoImperativa) -> bool:
        return self.comando.checaTipo(ambienteCompilacao)
