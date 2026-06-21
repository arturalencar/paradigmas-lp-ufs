from command.io_comando import IO
from expression.id import Id
from memory.erro_tipo_entrada_exception import ErroTipoEntradaException

class Read(IO):
    def __init__(self, idArg: Id):
        self.id = idArg

    def executar(self, ambiente):
        valorID = ambiente.get(self.id)
        valorRead = ambiente.read()
        if valorID.getTipo(None).eIgual(valorRead.getTipo(None)):
            ambiente.changeValor(self.id, valorRead)
        else:
            raise ErroTipoEntradaException(
                f"Tipo do valor de entrada lido incompatível com tipo da variável ({self.id.getIdName()})"
            )
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return True
