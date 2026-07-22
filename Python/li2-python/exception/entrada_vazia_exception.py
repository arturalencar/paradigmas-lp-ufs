class EntradaVaziaException(Exception):
    def __init__(self, msg="Entrada vazia."):
        super().__init__(msg)
