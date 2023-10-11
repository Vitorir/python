from tkinter import *

# Funções
def cadastrarAluno():
    nome = nome_entrada.get()
    idade = idade_entrada.get()
    nota = nota_entrada.get()

    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }

    alunos.append(aluno)
    print(f"Nome: {aluno['nome']}\n Idade: {aluno['idade']}\n Nota: {aluno['nota']}")

    nome_entrada.delete(0, END)
    idade_entrada.delete(0, END)
    nota_entrada.delete(0, END)

def visualizar():
    for i, aluno in enumerate(alunos):
        print(f"Nome do aluno {i+1}: {aluno['nome']}")
        print(f"Idade do Aluno: {i+1}: {aluno['idade']}")
        print(f"Nota do Aluno {i+1}: {aluno['nota']}")

janela = Tk()
alunos = []

# Label
titulo = Label(text="Sistema de Cadastro")
nome = Label(text="Nome: ")
idade = Label(text="Idade: ")
nota = Label(text="Nota: ")
# Entry
nome_entrada = Entry()
idade_entrada = Entry()
nota_entrada = Entry()
# Botão
botao_cadastrar = Button(text="Cadastrar", command=cadastrarAluno)

# Posicionamento
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
nome.grid(row=1, column=0, padx=10,pady=5)
nome_entrada.grid(row=1, column=1, padx=10,pady=5)
idade.grid(row=2, column=0, padx=10, pady=5)
idade_entrada.grid(row=2, column=1, padx=10, pady=5)
nota.grid(row=3, column=0, padx=10, pady=5)
nota_entrada.grid(row=3, column=1, padx=10, pady=5)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


janela.mainloop()