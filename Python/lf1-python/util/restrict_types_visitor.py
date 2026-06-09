"""
Equivalente ao RestrictTypesVisitor.java do lf1.

Realiza inferência/restrição de tipos dos identificadores de parâmetros
percorrendo a AST da expressão corpo de uma função.

O método estático visit() despacha para o handler correto com base
no tipo concreto da expressão, restringindo o mapeamento Id->Tipo
conforme os contextos de uso encontrados.
"""
from util.tipo import Tipo


class RestrictTypesVisitor:
    """
    Visitante estático para inferência de tipos de parâmetros de função.
    Percorre recursivamente a AST e restringe os tipos dos Ids presentes
    no mapa map_id_tipo de acordo com o contexto de uso.
    """

    @staticmethod
    def visit(expressao, ambiente, map_id_tipo: dict, tipo_esperado: Tipo) -> dict:
        """
        Ponto de entrada do visitante.

        :param expressao:    nó raiz a ser visitado.
        :param ambiente:     ambiente de compilação atual.
        :param map_id_tipo:  mapeamento Id -> Tipo a ser refinado.
        :param tipo_esperado: tipo esperado neste contexto.
        :return: mapeamento (possivelmente refinado).
        """
        # Importações locais para evitar ciclos e resolver nomes dinamicamente
        from expression.exp_soma import ExpSoma
        from expression.exp_sub import ExpSub
        from expression.exp_equals import ExpEquals
        from expression.valor_inteiro import ValorInteiro
        from expression.valor_string import ValorString
        from expression.valor_booleano import ValorBooleano
        from expression.id import Id

        # Importações opcionais de expressões le2 que podem existir
        try:
            from expression.exp_and import ExpAnd
        except ImportError:
            ExpAnd = None
        try:
            from expression.exp_or import ExpOr
        except ImportError:
            ExpOr = None
        try:
            from expression.exp_not import ExpNot
        except ImportError:
            ExpNot = None
        try:
            from expression.exp_concat import ExpConcat
        except ImportError:
            ExpConcat = None
        try:
            from expression.exp_length import ExpLength
        except ImportError:
            ExpLength = None
        try:
            from expression.exp_menos import ExpMenos
        except ImportError:
            ExpMenos = None

        # Expressões do lf1
        from expression.if_then_else import IfThenElse
        from expression.exp_declaracao import ExpDeclaracao

        # Despachante baseado no tipo concreto da expressão
        if isinstance(expressao, Id):
            return RestrictTypesVisitor._visit_id(
                expressao, ambiente, map_id_tipo, tipo_esperado)

        if isinstance(expressao, ValorInteiro):
            return map_id_tipo  # terminais não alteram o mapa

        if isinstance(expressao, ValorBooleano):
            return map_id_tipo

        if isinstance(expressao, (ValorString,)):
            return map_id_tipo

        if isinstance(expressao, ExpSoma):
            return RestrictTypesVisitor._visit_exp_binaria_inteiro(
                expressao, ambiente, map_id_tipo)

        if isinstance(expressao, ExpSub):
            return RestrictTypesVisitor._visit_exp_binaria_inteiro(
                expressao, ambiente, map_id_tipo)

        if ExpAnd and isinstance(expressao, ExpAnd):
            return RestrictTypesVisitor._visit_exp_binaria_booleano(
                expressao, ambiente, map_id_tipo)

        if ExpOr and isinstance(expressao, ExpOr):
            return RestrictTypesVisitor._visit_exp_binaria_booleano(
                expressao, ambiente, map_id_tipo)

        if ExpNot and isinstance(expressao, ExpNot):
            return RestrictTypesVisitor.visit(
                expressao.exp, ambiente, map_id_tipo, Tipo.TIPO_BOOLEANO)

        if ExpConcat and isinstance(expressao, ExpConcat):
            aux = RestrictTypesVisitor.visit(
                expressao.esq, ambiente, map_id_tipo, Tipo.TIPO_STRING)
            return RestrictTypesVisitor.visit(
                expressao.dir, ambiente, aux, Tipo.TIPO_STRING)

        if ExpLength and isinstance(expressao, ExpLength):
            return RestrictTypesVisitor.visit(
                expressao.exp, ambiente, map_id_tipo, Tipo.TIPO_STRING)

        if ExpMenos and isinstance(expressao, ExpMenos):
            return RestrictTypesVisitor.visit(
                expressao.exp, ambiente, map_id_tipo, Tipo.TIPO_INTEIRO)

        if isinstance(expressao, ExpEquals):
            return map_id_tipo  # equals não restringe por si só

        if isinstance(expressao, IfThenElse):
            return RestrictTypesVisitor._visit_if_then_else(
                expressao, ambiente, map_id_tipo, tipo_esperado)

        if isinstance(expressao, ExpDeclaracao):
            return RestrictTypesVisitor._visit_exp_declaracao(
                expressao, ambiente, map_id_tipo, tipo_esperado)

        # Expressão desconhecida — retorna o mapa sem alterações
        return map_id_tipo

    # ------------------------------------------------------------------ #
    # Handlers especializados                                               #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _visit_id(id_expr, ambiente, map_id_tipo: dict, tipo_esperado: Tipo) -> dict:
        """Restringe o tipo do Id se ele estiver no mapa."""
        for id_key, tipo_atual in list(map_id_tipo.items()):
            if id_key == id_expr:
                map_id_tipo[id_key] = tipo_esperado.intersecao(tipo_atual)
        return map_id_tipo

    @staticmethod
    def _visit_exp_binaria_inteiro(expressao, ambiente, map_id_tipo: dict) -> dict:
        """Visita expressão binária inteira (soma, sub): restringe ambos os lados a INTEIRO."""
        aux = RestrictTypesVisitor.visit(
            expressao.esq, ambiente, map_id_tipo, Tipo.TIPO_INTEIRO)
        return RestrictTypesVisitor.visit(
            expressao.dir, ambiente, aux, Tipo.TIPO_INTEIRO)

    @staticmethod
    def _visit_exp_binaria_booleano(expressao, ambiente, map_id_tipo: dict) -> dict:
        """Visita expressão binária booleana (and, or): restringe ambos os lados a BOOLEANO."""
        aux = RestrictTypesVisitor.visit(
            expressao.esq, ambiente, map_id_tipo, Tipo.TIPO_BOOLEANO)
        return RestrictTypesVisitor.visit(
            expressao.dir, ambiente, aux, Tipo.TIPO_BOOLEANO)

    @staticmethod
    def _visit_if_then_else(expressao, ambiente, map_id_tipo: dict,
                            tipo_esperado: Tipo) -> dict:
        """Visita IfThenElse: condição -> BOOLEANO, ramos -> tipo_esperado."""
        aux = RestrictTypesVisitor.visit(
            expressao.condicao, ambiente, map_id_tipo, Tipo.TIPO_BOOLEANO)
        aux = RestrictTypesVisitor.visit(
            expressao.then, ambiente, aux, tipo_esperado)
        return RestrictTypesVisitor.visit(
            expressao.else_expressao, ambiente, aux, tipo_esperado)

    @staticmethod
    def _visit_exp_declaracao(expressao, ambiente, map_id_tipo: dict,
                               tipo_esperado: Tipo) -> dict:
        """
        Visita ExpDeclaracao funcional: percorre cada declaração e o corpo.
        Equivalente a _visitExpDeclaracao() do Java.
        """
        from declaration.dec_funcao import DecFuncao

        ambiente.incrementa()
        mapa = map_id_tipo

        for dec_funcional in expressao.seqdec_funcional:
            tipo_procurado = None
            try:
                if dec_funcional.get_aridade() == 0:
                    tipo_procurado = dec_funcional.get_expressao().get_tipo(ambiente)
                    ambiente.map(dec_funcional.get_id(), tipo_procurado)
                else:
                    dec_funcao = dec_funcional  # é um DecFuncao
                    tipo = dec_funcao.get_funcao().get_tipo(ambiente)
                    tipo_procurado = tipo
                    if tipo is not Tipo.TIPO_INDEFINIDO:
                        ambiente.map(dec_funcional.get_id(), tipo)
            except Exception:
                pass  # VariavelJaDeclarada / VariavelNaoDeclarada silenciadas

            mapa = RestrictTypesVisitor.visit(
                dec_funcional.get_expressao(), ambiente, mapa, tipo_procurado)

        mapa = RestrictTypesVisitor.visit(
            expressao.expressao, ambiente, mapa, tipo_esperado)

        ambiente.restaura()
        return mapa
