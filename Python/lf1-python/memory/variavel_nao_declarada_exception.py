from expression.id import Id


class VariavelNaoDeclaradaException(Exception):

    def __init__(self, id_arg: Id):
        mensagem = f"Variavel {id_arg} nao declarada."
        super().__init__(mensagem)
