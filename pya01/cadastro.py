usuario = {}

def cadastro():
    nome = input("Digite o seu nome: ")
    usuario['nome'] = nome
    senha = input("Digite sua senha: ")
    usuario['senha'] = senha
    email = input("Digite o seu email: ")
    usuario['email'] = email
    cpf = input("Digite o seu cpf: ")
    usuario['cpf'] = cpf
    tel = input("Digite o seu tel: ")
    usuario['tel'] = tel
    print("Cadastro realizado com sucesso!")

print("==============================")

def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == usuario['nome'] and password == usuario['senha']:
            print("Login bem-sucedido!")
            break
        else:
            print("Username ou password Invalido!\n")

cadastro()
login()
