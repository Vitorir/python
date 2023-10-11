from tkinter import * # pode utilizar sem chamar o apelido

# Funções
def imprimirSaudacao():
    print(f"""
            Seja bem vindo, {entrada.get()}! 
            """)
def deletar(indice):
    entrada.delete(indice)

janela = Tk()

# Labels
titulo = Label(text="INFINITY SCHOOL",
               fg="black",
               bg="red")
nome = Label(text="Insira seu nome: ")

# Entries
entrada = Entry()

# Botoes
enviar = Button(janela, text="submit", command=imprimirSaudacao)

# Definindo localização
# titulo.pack()
# nome.pack()
# entrada.pack(side="left", padx=10, pady=5)
# enviar.pack(side="left", padx=10, pady=5)

# Posicionamento
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
nome.grid(row=1, column=0, padx=10, pady=5)
entrada.grid(row=1, column=1, padx=10, pady=5)
enviar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop() # atualização contínua