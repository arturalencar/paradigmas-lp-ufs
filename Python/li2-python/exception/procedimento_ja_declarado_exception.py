from exception.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException

class ProcedimentoJaDeclaradoException(IdentificadorJaDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Procedimento {id} já declarado.")
