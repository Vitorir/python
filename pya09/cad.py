from tkinter import *

# Funções
def cadastrarAluno():
    nome = nome_entrada.get()
    idade = idade_entrada.get()
    email = email_entrada.get()
    
    print(f"Aluno: {nome} tem {idade} anos, seu email é: {email}")
    deletar()

def deletar():
    nome_entrada.delete(0, END)
    idade_entrada.delete(0, END)
    email_entrada.delete(0, END)

janela = Tk()

# Label
titulo = Label(text="Sistema de Cadastro")
nome = Label(text="Digite seu nome: ")
idade = Label(text="Digite sua idade: ")
email = Label(text="Digite seu email: ")
# Entry
nome_entrada = Entry(janela)
idade_entrada = Entry(janela)
email_entrada = Entry(janela)

# Botoes
botao_cadastrar = Button(text="Cadastrar", command=cadastrarAluno)

# Posicionamento
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
nome.grid(row=1, column=0, padx=10, pady=5)
nome_entrada.grid(row=1, column=1, padx=10, pady=5)
idade.grid(row=2, column=0, padx=10, pady=5)
idade_entrada.grid(row=2, column=1, padx=10, pady=5)
email.grid(row=3, column=0, padx=10, pady=5)
email_entrada.grid(row=3, column=1, padx=10, pady=5)

botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()