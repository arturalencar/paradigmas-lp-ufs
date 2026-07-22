class ErroTipoEntradaException(Exception):
    def __init__(self, msg="Tipo do valor de entrada lido incompatível"):
        super().__init__(msg)
