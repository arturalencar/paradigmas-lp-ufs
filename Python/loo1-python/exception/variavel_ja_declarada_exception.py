from exception.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
# Note: Id will be implemented in expression package
# from ..expression.Id import Id

class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id_obj):
        super().__init__(f"Variável {id_obj} já declarada.")
