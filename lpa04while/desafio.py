import random

clientes = []
while True:
    nome = input('Nome: ')
    if nome == 'sair':
        break

    telefone = input('Telefone: ')

    cliente = {
        'nome': nome,
        'telefone': telefone
    }

    clientes.append(cliente)

sorteados = []
while len(sorteados) < 2:
    escolhido = random.choice(clientes)

    if escolhido not in sorteados:
        sorteados.append(escolhido)

print("Clientes: ",clientes)
print("Os sorteados foram: ", sorteados)