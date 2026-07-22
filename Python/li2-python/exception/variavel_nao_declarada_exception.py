from exception.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException

class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Variavel {id} nao declarada.")
