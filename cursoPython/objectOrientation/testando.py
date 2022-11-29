class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O titular {} possui um saldo de {}".format(self.titular, self.saldo))

    def deposito(self,valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor

    def transfere(self, origem, destino, valor):
        origem.saca(valor)
        destino.deposito(valor)