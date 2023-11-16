import random

cadastros = 0
clientes = []
while True:
    nome = input('Nome: ')
    if nome == 'sair' and cadastros >= 5:
        break
    telefone = input('Telefone: ')

    cliente = {
        'nome': nome,
        'telefone': telefone
    }

    clientes.append(cliente)
    cadastros += 1


sorteados = []
while len(sorteados) < 3:
    escolhido = random.choice(clientes)

    if escolhido not in sorteados:
        sorteados.append(escolhido)

# Faz a mesma coisa do código acima
escolhidos = random.sample(clientes, 3)

# Saída de dados
print("\nCLIENTES: ")
print("-"*30)
for cliente in clientes:
    print(f"Nome: {cliente['nome']}, Telefone: {cliente['telefone']}")


print("\nSORTEADOS")
print("-"*30)
for cliente in sorteados:
    print(f"{cliente['nome']}, {cliente['telefone']}")
