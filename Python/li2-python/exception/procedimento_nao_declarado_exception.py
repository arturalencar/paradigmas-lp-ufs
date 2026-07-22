from exception.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException

class ProcedimentoNaoDeclaradoException(IdentificadorNaoDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Procedimento {id} nao declarado.")
