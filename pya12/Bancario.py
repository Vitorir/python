class Conta:
    def __init__(self, id:int, titular:str, saldo):
        self.identificador = id
        self.titular = titular
        self.saldo = saldo
    
    def vericar_informacoes(self):
        print(f'Vericar Informacoes\n'
              f'Id: {self.identificador}\n'
              f'Nome: {self.titular}\n'
              f'Saldo: {self.saldo}\n')
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor} realizado com sucesso"
        else:
            return "Valor inválido"

class ContaCorrente(Conta):
    def __init__(self, id, titular, saldo):
        super().__init__(id, titular, saldo)

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso")
        else:
            print("Saque invalido!")

        
class ContaPoupanca(Conta):
    def __init__(self, id, titular, saldo, juros):
        super().__init__(id, titular, saldo)
        self.juros = juros

cc = ContaCorrente(1, 'Fulano', 5000)
cc.depositar(5000)
cc.sacar(5000)
cc.vericar_informacoes()
cc.sacar(6000)
cc.vericar_informacoes()
