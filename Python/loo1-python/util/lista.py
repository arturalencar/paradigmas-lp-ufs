from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Lista(Generic[T]):
    def __init__(self, valor: Optional[T] = None, lista: Optional['Lista[T]'] = None):
        self.head = valor
        self.tail = lista

    def length(self) -> int:
        if self.head is None:
            return 0
        elif self.tail is None:
            return 1
        else:
            return 1 + self.tail.length()

    def getHead(self) -> Optional[T]:
        return self.head

    def getTail(self) -> Optional['Lista[T]']:
        return self.tail

    def __str__(self) -> str:
        resposta = []
        self._formatar(resposta)
        return "".join(resposta)

    def _formatar(self, resposta: list):
        if self.head is not None:
            resposta.append(str(self.head))
            if self.tail is not None:
                resposta.append(" ")
                self.tail._formatar(resposta)
