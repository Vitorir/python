class Fatura:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco_item = preco
        self.qtd_item = qtd

    def gerar_fatura(self):
        return self.qtd_item * self.preco_item
    
    