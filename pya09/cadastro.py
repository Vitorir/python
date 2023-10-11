import tkinter as tk
from tkinter import messagebox


def cadastrar_aluno():
    nome = entry_nome.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()
    email = entry_email.get()

    # Verifica se os campos estão preenchidos
    if not nome or not senha or not confirmar_senha or not email:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    elif senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem. Tente novamente.")
    else:
        # Armazenar os dados do aluno (substitua esta parte pelo código para salvar em um banco de dados)
        alunos_cadastrados.append({"Nome": nome, "Senha": senha, "Email": email})
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)
    entry_email.delete(0, tk.END)


def exibir_alunos_cadastrados():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Alunos Cadastrados")
    segunda_janela.configure(bg="black")

    lista_alunos = tk.Listbox(segunda_janela, font=("Arial", 20), bg="black", fg="white")
    lista_alunos.pack()

    for aluno in alunos_cadastrados:
        lista_alunos.insert(tk.END, f"Nome: {aluno['Nome']},\n Email: {aluno['Email']}\n\n")


# Criar uma janela principal
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.configure(bg="black")  # Define o fundo da janela como preto

# Definir a fonte e o tamanho da fonte
fonte = ("Arial", 20)

# Criar rótulos e campos de entrada com texto branco, fonte grande e alinhados à esquerda
label_nome = tk.Label(janela, text="Nome:", bg="black", fg="white", font=fonte, anchor="w")
label_nome.pack()

entry_nome = tk.Entry(janela, font=fonte)
entry_nome.pack()

label_senha = tk.Label(janela, text="Senha:", bg="black", fg="white", font=fonte, anchor="w")
label_senha.pack()

entry_senha = tk.Entry(janela, show="*", font=fonte)  # Para ocultar a senha
entry_senha.pack()

label_confirmar_senha = tk.Label(janela, text="Confirmar Senha:", bg="black", fg="white", font=fonte, anchor="w")
label_confirmar_senha.pack()

entry_confirmar_senha = tk.Entry(janela, show="*", font=fonte)
entry_confirmar_senha.pack()

label_email = tk.Label(janela, text="Email:", bg="black", fg="white", font=fonte, anchor="w")
label_email.pack()

entry_email = tk.Entry(janela, font=fonte)
entry_email.pack()

# Botão para cadastrar o aluno
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_aluno, font=fonte)
botao_cadastrar.pack()

# Botão para exibir os alunos cadastrados
botao_exibir_alunos = tk.Button(janela, text="Exibir Alunos Cadastrados", command=exibir_alunos_cadastrados, font=fonte)
botao_exibir_alunos.pack()

# Lista para armazenar os dados dos alunos
alunos_cadastrados = []

# Iniciar a interface gráfica
janela.mainloop()