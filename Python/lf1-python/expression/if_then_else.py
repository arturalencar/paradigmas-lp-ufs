"""
Equivalente ao IfThenElse.java do lf1.

Expressão condicional: if <condicao> then <then> else <else>.
"""
from util.tipo import Tipo


class IfThenElse:
    """
    Expressão if-then-else funcional.

    Avalia a condição; se True avalia o ramo then, senão o ramo else.
    Equivalente a IfThenElse.java do lf1.
    """

    def __init__(self, condicao, then_expressao, else_expressao):
        """
        :param condicao:        expressão booleana de teste.
        :param then_expressao:  expressão avaliada se condição for True.
        :param else_expressao:  expressão avaliada se condição for False.
        """
        self.condicao = condicao
        self.then = then_expressao
        self.else_expressao = else_expressao

    # ------------------------------------------------------------------ #
    # Avaliação                                                             #
    # ------------------------------------------------------------------ #

    def avaliar(self, ambiente):
        """
        Avalia a condição e retorna o valor do ramo correspondente.
        """
        cond_valor = self.condicao.avaliar(ambiente)
        # ValorBooleano tem propriedade .valor
        if cond_valor.valor:
            return self.then.avaliar(ambiente)
        else:
            return self.else_expressao.avaliar(ambiente)

    # ------------------------------------------------------------------ #
    # Verificação de tipos                                                   #
    # ------------------------------------------------------------------ #

    def checa_tipo(self, ambiente) -> bool:
        """
        Verifica que:
          - a condição é booleana
          - os tipos do then e do else têm interseção não-vazia
        """
        if not self.condicao.get_tipo(ambiente).e_booleano():
            return False
        tipo_then = self.then.get_tipo(ambiente)
        tipo_else = self.else_expressao.get_tipo(ambiente)
        if tipo_then.intersecao(tipo_else).e_void():
            return False
        return True

    def get_tipo(self, ambiente) -> Tipo:
        """Retorna a interseção dos tipos dos dois ramos."""
        tipo_then = self.then.get_tipo(ambiente)
        tipo_else = self.else_expressao.get_tipo(ambiente)
        return tipo_then.intersecao(tipo_else)

    # ------------------------------------------------------------------ #
    # Getters (usados por RestrictTypesVisitor)                             #
    # ------------------------------------------------------------------ #

    def get_condicao(self):
        return self.condicao

    def get_then(self):
        return self.then

    def get_else_expressao(self):
        return self.else_expressao

    def __str__(self) -> str:
        return (f"if ({self.condicao}) "
                f"then ({self.then}) "
                f"else ({self.else_expressao})")
