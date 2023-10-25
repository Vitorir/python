from tkinter import *

# Funcoes
def cadastrar():
    nome = usuario_entrada.get()
    senha = senha_entrada.get()

    usuario = {
        'nome': nome,
        'senha': senha
    }

    usuarios.append(usuario)
    print(f"Usuario {nome} cadastrado com sucesso!")
    print(f"Os alunos cadastrados são {usuarios}")
    limpar()

def limpar():
    usuario_entrada.delete(0, END)
    senha_entrada.delete(0, END)



janela = Tk()

usuarios = []
# Labels
titulo = Label(text="Sistema de cadastro")
user = Label(text="Usuairo: ")
senha = Label(text="Senha: ")

# Entries
usuario_entrada = Entry(janela)
senha_entrada = Entry(janela)

# Butoes
logar = Button(text="Cadastrar", command=cadastrar)

# Posicionamento
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
user.grid(row=1, column=0, padx=10, pady=5)
usuario_entrada.grid(row=1, column=1, padx=10, pady=5)

senha.grid(row=2, column=0, padx=10, pady=5)
senha_entrada.grid(row=2, column=1, padx=10, pady=5)

logar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()