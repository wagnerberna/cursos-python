class Node:
    def __init__(self, value):
        # dado armazenado / apontamento próx. nó
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node(valor: {self.value}, proximo nó: {self.next})"
