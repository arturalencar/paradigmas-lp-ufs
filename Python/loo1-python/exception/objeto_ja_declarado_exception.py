class ObjetoJaDeclaradoException(Exception):
    def __init__(self, msg=""):
        super().__init__(f"{self.__class__.__name__}: {msg}")
