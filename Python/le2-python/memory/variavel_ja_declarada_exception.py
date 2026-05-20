from expression.id import Id


class VariavelJaDeclaradaException(Exception):

    def __init__(self, id_arg: Id):

        mensagem = f"Variavel {id_arg} ja declarada."
        super().__init__(mensagem)
