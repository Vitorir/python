class Animal:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

    def comer(self):
        return f"O {self.nome} está comendo"
    
    def visualizar(self):
        print(f'Nome: {self.nome}\n'
              f'Raca: {self.raca}\n'
              f'Peso: {self.peso}\n')
    
class Cachorro(Animal):
    def __init__(self, nome:str, raca:str, peso:float):
        super().__init__(nome, raca, peso)
    
class Gato(Animal):
    def __init__(self, nome, raca, peso):
        super().__init__(nome, raca, peso)

    

c1 = Cachorro('Rex', 'Pitbull', 8)
g1 = Gato('Garfield', 'persa', 5)
c1.visualizar()
g1.visualizar()

print(c1.comer())
print(g1.comer())

