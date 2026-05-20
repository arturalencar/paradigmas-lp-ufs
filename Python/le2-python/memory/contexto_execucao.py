from contexto import Contexto
from ambiente_execucao import AmbienteExecucao


class ContextoExecucao(Contexto, AmbienteExecucao):

    def __init__(self):

        super().__init__()

    def clone(self):

        retorno = ContextoExecucao()

        nova_pilha = []
        novo_map = {}
        nova_pilha.append(novo_map)

        for mapa in self.pilha:

            for identificador, valor in mapa.items():
                novo_map[identificador] = valor

        retorno.set_pilha(nova_pilha)

        return retorno
