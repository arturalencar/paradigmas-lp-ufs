class ErroTipoEntradaException(Exception):
    def __init__(self, msg="Erro no tipo da entrada."):
        super().__init__(msg)
