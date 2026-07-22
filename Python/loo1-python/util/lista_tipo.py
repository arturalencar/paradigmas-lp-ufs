class ListaTipo:
    def __init__(self, head=None, tail=None):
        self._head = head
        self._tail = tail

    def length(self):
        if self._head is None:
            return 0
        if self._tail is None:
            return 1
        return 1 + self._tail.length()

    def head(self):
        return self._head

    def tail(self):
        return self._tail
