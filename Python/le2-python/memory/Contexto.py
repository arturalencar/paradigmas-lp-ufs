from expression.id import Id
from .variavel_ja_declarada_exception import VariavelJaDeclaradaException
from .variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from .identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
from .identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException


class Contexto:

    def __init__(self):

        self._pilha = []

    def incrementa(self):

        self._pilha.append({})

    def restaura(self):

        if self._pilha:
            self._pilha.pop()

    def map(self, id_arg: Id, valor_id):

        if not self._pilha:
            self.incrementa()

        topo_da_pilha = self._pilha[-1]

        if id_arg in topo_da_pilha:
            raise VariavelJaDeclaradaException(id_arg)

        topo_da_pilha[id_arg] = valor_id

    def get(self, id_arg: Id):

        for tabela_de_simbolos in reversed(self._pilha):
            if id_arg in tabela_de_simbolos:
                return tabela_de_simbolos[id_arg]

        raise VariavelNaoDeclaradaException(id_arg)

    @property
    def pilha(self):
        return self._pilha

    def set_pilha(self, nova_pilha: list):
        self._pilha = nova_pilha
