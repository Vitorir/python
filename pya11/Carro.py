class Carro():
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0

    def ligar(self):
        print("Carro ligado!")
        
    def desligar(self):
        if self.velocidade > 0:
            self.velocidade = 0
        print("Carro desligado!")
    
    def acelerar(self, valor):
        self.velocidade += valor

    def desacelerar(self, valor):
        self.velocidade -= valor

    def status(self):
        print(f"""
                {self.marca}
                {self.modelo}
                {self.ano}
                Velocidade: {self.velocidade}
                """)

meuCarro = Carro('Toyota', 'Corolla', 'Prata', 2010)
meuCarro.ligar()
meuCarro.acelerar(60)
meuCarro.status()

meuCarro.desacelerar(20)
meuCarro.status()
meuCarro.desligar()
meuCarro.status()