"""
Equivalente ao ExpDeclaracao.java do lf1.

ExpDeclaracao funcional suporta tanto DecVariavel quanto DecFuncao
na lista de declarações, ao contrário da versão le2 que só suportava
DecVariavel.

Separação entre variáveis e funções:
  - aridade 0  -> DecVariavel -> resolve_bindings -> pilha_id_valor
  - aridade > 0 -> DecFuncao  -> map_funcao       -> pilha_id_valor_func
"""
from memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from util.tipo import Tipo


class ExpDeclaracao:
    """
    Expressão let funcional:
      let <seqdec_funcional> in <expressao>

    Suporta mix de declarações de variáveis e funções.
    Equivalente a ExpDeclaracao.java do lf1.
    """

    def __init__(self, seqdec_funcional: list, expressao):
        """
        :param seqdec_funcional: lista de DeclaracaoFuncional (DecVariavel | DecFuncao).
        :param expressao:        corpo do let.
        """
        self.seqdec_funcional = seqdec_funcional
        self.expressao = expressao

    # ------------------------------------------------------------------ #
    # Avaliação                                                             #
    # ------------------------------------------------------------------ #

    def avaliar(self, ambiente):
        """
        1. Abre novo escopo.
        2. Resolve os bindings (variáveis e funções) ANTES de atualizar o ambiente
           (semântica colateral: todas as expressões são avaliadas no ambiente externo).
        3. Inclui os bindings no novo escopo.
        4. Avalia o corpo.
        5. Restaura o escopo.
        """
        ambiente.incrementa()

        aux_id_valor, aux_id_valor_funcao = self._resolve_bindings(ambiente)
        self._include_bindings(ambiente, aux_id_valor, aux_id_valor_funcao)

        result = self.expressao.avaliar(ambiente)
        ambiente.restaura()
        return result

    def _include_bindings(self, ambiente, aux_id_valor: dict,
                           aux_id_valor_funcao: dict) -> None:
        """Insere variáveis e funções no escopo atual."""
        for id_obj, valor in aux_id_valor.items():
            ambiente.map(id_obj, valor)
        for id_obj, valor_funcao in aux_id_valor_funcao.items():
            ambiente.map_funcao(id_obj, valor_funcao)

    def _resolve_bindings(self, ambiente):
        """
        Avalia/coleta os valores de todas as declarações no ambiente ATUAL
        (antes de criar o novo escopo já incrementado).

        Retorna (dict_variaveis, dict_funcoes).
        """
        aux_id_valor = {}
        aux_id_valor_funcao = {}

        for dec_funcional in self.seqdec_funcional:
            if dec_funcional.get_aridade() == 0:
                # É uma DecVariavel: avalia a expressão no ambiente atual
                aux_id_valor[dec_funcional.get_id()] = \
                    dec_funcional.get_expressao().avaliar(ambiente)
            else:
                # É uma DecFuncao: captura o ValorFuncao sem avaliar
                aux_id_valor_funcao[dec_funcional.get_id()] = \
                    dec_funcional.get_funcao()

        return aux_id_valor, aux_id_valor_funcao

    # ------------------------------------------------------------------ #
    # Verificação de tipos                                                   #
    # ------------------------------------------------------------------ #

    def checa_tipo(self, ambiente) -> bool:
        """
        1. Abre novo escopo de compilação.
        2. Checa os tipos de cada declaração.
        3. Resolve e inclui os tipos no ambiente.
        4. Checa o tipo do corpo.
        5. Restaura o escopo.
        """
        ambiente.incrementa()
        result = False
        try:
            result = self._check_type_bindings(ambiente)
            if result:
                resolved_types = self._resolve_type_bindings(ambiente)
                self._include_type_bindings(ambiente, resolved_types)
                result = self.expressao.checa_tipo(ambiente)
        finally:
            ambiente.restaura()
        return result

    def _check_type_bindings(self, ambiente) -> bool:
        """Checa os tipos de cada declaração individualmente."""
        for dec_funcional in self.seqdec_funcional:
            if not dec_funcional.checa_tipo(ambiente):
                ambiente.restaura()
                return False
        return True

    def _resolve_type_bindings(self, ambiente) -> dict:
        """Coleta Id -> Tipo de cada declaração, lançando exceção em duplicatas."""
        resolved_types = {}
        for dec_funcional in self.seqdec_funcional:
            id_dec = dec_funcional.get_id()
            if id_dec in resolved_types:
                raise VariavelJaDeclaradaException(id_dec)
            resolved_types[id_dec] = dec_funcional.get_tipo(ambiente)
        return resolved_types

    def _include_type_bindings(self, ambiente, resolved_types: dict) -> None:
        """Registra os tipos no ambiente de compilação."""
        for id_obj, tipo in resolved_types.items():
            ambiente.map(id_obj, tipo)

    def get_tipo(self, ambiente) -> Tipo:
        """Retorna o tipo do corpo após registrar as declarações."""
        ambiente.incrementa()
        for dec_funcional in self.seqdec_funcional:
            if dec_funcional.get_aridade() == 0:
                ambiente.map(
                    dec_funcional.get_id(),
                    dec_funcional.get_expressao().get_tipo(ambiente))
            else:
                tipo = dec_funcional.get_funcao().get_tipo(ambiente)
                if tipo is not Tipo.TIPO_INDEFINIDO:
                    ambiente.map(dec_funcional.get_id(), tipo)
        result = self.expressao.get_tipo(ambiente)
        ambiente.restaura()
        return result

    # ------------------------------------------------------------------ #
    # Getter auxiliar (usado por RestrictTypesVisitor)                      #
    # ------------------------------------------------------------------ #

    def get_seqdec_funcional(self) -> list:
        return self.seqdec_funcional

    def get_expressao(self):
        return self.expressao

    def __str__(self) -> str:
        decs = "; ".join(str(d) for d in self.seqdec_funcional)
        return f"let {decs} in {self.expressao}"
