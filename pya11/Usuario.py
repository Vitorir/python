class Usuario:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.idade = 0
        self.genero = None

    def cadastrar_usuario(self):
        print('-----CADASTRO-------')
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.idade = int(input("Idade: "))
        self.genero = input("Genero: ")

    def exibir_dados(self):
        print('----DADOS----\n'
              f'NOME: {self.nome}\n'
              f'CPF: {self.cpf}\n'
              f'Idade: {self.idade}\n'
              f'Genero: {self.genero}\n'
              f'-----------\n')

u1 = Usuario()
u1.cadastrar_usuario()
u1.exibir_dados()