class Animal:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo!")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Gato(Animal):
    def __init__(self, nome, cor, raca, peso):
        super().__init__(nome, cor)
        self.raca = raca
        self.peso = peso

chachorro = Cachorro('Doggo', 'Preto')
gato = Gato('Felino', 'Branco', 'Persa', 5)

print(gato.raca)
print(gato.peso)
chachorro.comer()
gato.comer()