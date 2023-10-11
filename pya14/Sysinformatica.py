class Fatura():

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.quantidade = qtd
        self.valor = 0.0

    def GerarFatura(self):
        self.valor = self.preco * self.quantidade

    def visualizar(self):
        print(f"Item: {self.nome}")
        print(f"preco: {self.preco}")
        print(f"quantidade: {self.quantidade}")
        print(f"valor: {self.valor}")

sys = Fatura('Teclado', 99, 3)
sys.GerarFatura()
sys.visualizar()