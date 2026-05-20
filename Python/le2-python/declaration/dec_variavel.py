class DecVariavel:
    def __init__(self, id_arg, expressao_arg):
        self._id = id_arg
        self._expressao = expressao_arg

    @property
    def id(self):
        return self._id

    @property
    def expressao(self):
        return self._expressao
