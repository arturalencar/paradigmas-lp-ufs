from exception.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException

class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Variavel {id} ja declarada.")
