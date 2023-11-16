import random

vendas = int(input("1 - Registrar venda.\n2 - Encerrar. \nDigite a opção desejada: "))
clientes = [] # lista principal, armazena todos os clientes cadastrados
cadastros = 0 # armazena quantos cadastros foram realizados

if vendas == 1: # inicio do loop principal de registro de venda
    while True: # executa permanente, e so para em algum caso abaixo
        nome = input("digite o nome: ") # coleta de dados

        premiados = 0 # inicio do loop de sorteio
        if nome == "fim" and cadastros >= 5:
            for j in range(1,4,1): # loop para sorteio e remoção do premiado( para n ser o msm ganhador)
                premiado = random.choice(clientes) # escolhe um cadastro aleatorio
                print(f"O {j}º ganhador(a) foi {premiado}") # mostra quem foi o ganhador
                clientes.remove(premiado)  # remove o cadastro do ganhador da lista
            else:
                break # fim do loop de sorteio

        elif nome == "fim" and cadastros < 5: #inicio do loop de verificação de quantidade de cadastros
            continuar = int(input("1 - Encerrar expediente. \n2 - Continuar cadastros.\nDigite a opção desejada: "))
            if continuar == 1: # encerra o programa
                print(f"Apenas {cadastros} cadastros realizados, necessário ao menos 5.")
                break
            elif continuar == 2: # continua o ciclo de cadastros( nao reseta os anteriores)
                continue #fim do loop de verificação de quantidade de cadastros

        telefone = input("digite o telefone: ") # coleta de dados
        endereco = input("digite o endereço: ") # coleta de dados
        cadastros += 1 #adiciona +1  na variavel de contagem cadastro
        cliente = [nome,telefone,endereco] # cria uma lista de cada cliente
        clientes.append(cliente) # adiciona o cliente na lista principal (clientes)

elif vendas == 2: # apenas para caso a escolha seja encerrar, no menu inicial.
    print("Sistema encerrado.")

else:
    print("Opção inexistente, verifique e digite novamente.")