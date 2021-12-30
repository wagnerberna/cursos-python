from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print("falando.. B...")


# pessoa = A() (Erro ao instanciar)
pessoa = B()
pessoa.falar()
