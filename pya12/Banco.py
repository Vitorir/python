class Conta:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def verificar(self):
        return f"""
        {self.id}
        {self.nome}
        {self.saldo}
"""

    def depositar(self, valor):
        self.saldo += valor

class Corrente(Conta):
    def __init__(self, id, nome, saldo):
        super().__init__(id, nome, saldo)

    def sacar(self, valor):
        self.saldo -= valor

class Poupanca(Conta):
    def __init__(self, id, nome, saldo, juros):
        super().__init__(id, nome, saldo)
        self.juros = juros

c1 = Corrente(1, 'fulano', 5000)
c1.sacar(1000)
print(c1.saldo)
c1.depositar(10000)
print(c1.verificar())

c2 = Poupanca(2, 'Sicrano', 2000, 2)
c2.depositar(5000)
print(c2.verificar())