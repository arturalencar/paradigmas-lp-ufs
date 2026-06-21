from memory.contexto import Contexto
from memory.ambiente_execucao import AmbienteExecucao

class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self):
        retorno = ContextoExecucao()
        retorno_pilha = [{}]
        novoMap = retorno_pilha[0]
        for d in self.pilha:
            for k, v in d.items():
                novoMap[k] = v
        retorno.setPilha(retorno_pilha)
        return retorno
