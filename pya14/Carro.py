class Carro():
    def __init__(self, modelo:str, ano:int, cor:str, valor:float):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def ligar(self):
        print("Ligado")

    def desligar(self):
        print("Desligado")

    def visualizar(self):
        print(f"Item: {self.modelo}")
        print(f"preco: {self.ano}")
        print(f"quantidade: {self.cor}")
        print(f"valor: {self.valor}")

carros = []

carro1 = Carro('Corolla', 2010, 'Prata', 50000)
carro2 = Carro('Gol', 1947, 'Vermelho', 20000)
carro3 = Carro('Porsche', 2021, 'Preto', 100000)

for i in range(2):
    print("Digite os dados do carro: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    valor = float(input("Valor: "))

    carro = Carro(modelo, ano, cor, valor)
    carros.append(carro)

for i in carros:
    print(i.visualizar())