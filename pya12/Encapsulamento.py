class Funcionario:
    def __init__(self, nome, cargo, valor_hora):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.__salario = 0
        self.__horas_trabalhadas = 0

    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. Use calcula_salario()")
    
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora        


    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    @horas_trabalhadas.setter
    def horas_trabalhadas(self, novas_horas):
        self.__horas_trabalhadas = novas_horas




f1 = Funcionario('Fulano', 'programador', 50)
print(f1.salario) # 0
f1.horas_trabalhadas = 40

f1.calcula_salario()
print(f1.salario) 

f1.salario = 1020
print(f1.salario)