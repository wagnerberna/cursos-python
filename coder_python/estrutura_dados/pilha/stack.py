# declarar o construtor para termos uma pilha vazia
class Stack:
    def __init__(self):
        self._data = list()

    # propriedade nos retorna o tamanho da pilha
    def size(self):
        return len(self._data)

    # propriedade nos indica se a pilha esta vazia
    def is_empty(self):
        return not bool(self.size())

    # push adiciona um novo valor no topo da pilha
    def push(self, value):
        self._data.append(value)

    # pop irá pegar o elemento do topo, DELETAR, e então retornar esse valor.
    def pop(self):
        if self.is_empty():
            return None
        # -1 se refere ao último objeto da pilha.
        # Ou seja, o valor do topo da pilha
        value = self._data[-1]
        del self._data[-1]
        return value

    # peek que somente lê o valor no topo da pilha e então o retorna
    def peek(self):
        if self.is_empty():
            return None
        value = self._data[-1]
        return value

    # clear limpar todos os elementos da pilha.
    def clear(self):
        self._data.clear()

    # __str__ que fará a impressão de todos os elementos que estão empilhados.
    #  Do primeiro ao último item inserido (da parte de baixo da pilha até o topo)
    def __str__(self):
        str_items = ""
        for i in range(self.size()):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < self.size():
                str_items += ", "

        return "Stack(" + str_items + ")"
