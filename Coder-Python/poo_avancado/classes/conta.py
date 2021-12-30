from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("saldo precisa ser numérico")
        self._saldo = valor

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("valor precisa ser numérico")
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass
