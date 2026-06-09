"""
Equivalente ao ContextoExecucaoFuncional.java do lf1.

Implementa AmbienteExecucaoFuncional usando dois contextos internos:
  - pilha_id_valor     (ContextoExecucao)  : variáveis Id -> Valor
  - pilha_id_valor_func (Contexto genérico) : funções    Id -> ValorFuncao

A pilha de funções é compartilhada (mesma lista de dicionários),
espelhando o comportamento do Java onde:
  this.pilhaIdValorFunc.setPilha(this.pilhaFuncao)
"""
from memory.contexto_execucao import ContextoExecucao
from memory.contexto import Contexto    
from .ambiente_execucao_funcional import AmbienteExecucaoFuncional


class ContextoExecucaoFuncional(AmbienteExecucaoFuncional):
    """
    Contexto de execução funcional.

    Mantém duas pilhas separadas mas sincronizadas:
      pilha_id_valor      -> variáveis comuns
      pilha_id_valor_func -> funções (ValorFuncao)

    As pilhas crescem/diminuem juntas via incrementa()/restaura().
    """

    def __init__(self):
        # Pilha para variáveis (Id -> Valor)
        self._pilha_id_valor = ContextoExecucao()

        # Contexto genérico para funções, compartilhando a mesma pilha
        # interna que o Java faz com setPilha()
        self._pilha_id_valor_func = Contexto()
        # A pilha de funções é a lista interna do Contexto genérico
        self._pilha_funcao = self._pilha_id_valor_func.pilha

    # ------------------------------------------------------------------ #
    # Controle de escopo                                                    #
    # ------------------------------------------------------------------ #

    def incrementa(self):
        """Abre um novo escopo em ambas as pilhas."""
        self._pilha_id_valor.incrementa()
        self._pilha_id_valor_func.incrementa()

    def restaura(self):
        """Fecha o escopo atual em ambas as pilhas."""
        self._pilha_id_valor.restaura()
        self._pilha_id_valor_func.restaura()

    # ------------------------------------------------------------------ #
    # Operações de variáveis (AmbienteExecucao)                             #
    # ------------------------------------------------------------------ #

    def map(self, id_arg, valor):
        """Mapeia id_arg -> valor na pilha de variáveis."""
        self._pilha_id_valor.map(id_arg, valor)

    def get(self, id_arg):
        """Busca o valor de id_arg na pilha de variáveis."""
        return self._pilha_id_valor.get(id_arg)

    # ------------------------------------------------------------------ #
    # Operações de funções (AmbienteExecucaoFuncional)                      #
    # ------------------------------------------------------------------ #

    def map_funcao(self, id_arg, funcao) -> None:
        """Mapeia id_arg -> ValorFuncao na pilha de funções."""
        self._pilha_id_valor_func.map(id_arg, funcao)

    def get_funcao(self, id_arg):
        """Retorna a ValorFuncao associada ao id_arg."""
        return self._pilha_id_valor_func.get(id_arg)

    # ------------------------------------------------------------------ #
    # Acesso às pilhas internas (equivalente aos getters protegidos Java)   #
    # ------------------------------------------------------------------ #

    @property
    def pilha_id_valor(self):
        return self._pilha_id_valor

    @property
    def pilha_id_valor_func(self):
        return self._pilha_id_valor_func

    @property
    def pilha_funcao(self):
        return self._pilha_funcao

    def clone(self):
        """Retorna uma cópia do contexto de execução funcional, achatando as pilhas."""
        retorno = ContextoExecucaoFuncional()
        
        # Clona a pilha de variáveis
        retorno._pilha_id_valor = self._pilha_id_valor.clone()

        # Acha a pilha de funções
        nova_pilha_func = []
        novo_map_func = {}
        nova_pilha_func.append(novo_map_func)

        for mapa in self._pilha_id_valor_func.pilha:
            for identificador, valor in mapa.items():
                novo_map_func[identificador] = valor

        retorno._pilha_id_valor_func.set_pilha(nova_pilha_func)
        retorno._pilha_funcao = retorno._pilha_id_valor_func.pilha

        return retorno
