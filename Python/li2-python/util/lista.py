class Lista:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def length(self):
        if self.head is None:
            return 0
        if self.tail is None:
            return 1
        return 1 + self.tail.length()

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def __str__(self):
        if self.head is None:
            return "[]"
        if self.tail is None:
            return f"[{self.head}]"
        return f"[{self.head}] @ {self.tail}"
