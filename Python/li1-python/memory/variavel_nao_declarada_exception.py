from memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException
# Note: Id will be implemented in expression package
# from ..expression.Id import Id

class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_obj):
        super().__init__(f"Variável {id_obj} não declarada.")
