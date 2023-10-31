clientes = [
    {'nome': 'fulano', 'email': 'fulano@gmail.com', 'telefone': '987654321'},
    {'nome': 'beltrano', 'email': 'beltrano@gmail.com', 'telefone': '987652345'}
]
estoque = [
    {'nome': 'Teclado', 'preco': 29, 'qtd': 2},
    {'nome': 'Mouse', 'preco': 99, 'qtd': 2},
    {'nome': 'Notebook', 'preco': 3000, 'qtd': 2},
    {'nome': 'Headset', 'preco': 150, 'qtd': 2},
    {'nome': 'GPU', 'preco': 2000, 'qtd': 2}]

def vender():
    nome = input("Nome: ")
    cliente = None

    # verifica se existe cliente, e o seleciona
    for i in clientes:
        if i['nome'] == nome:
            cliente = i

    # mostra os dados do cliente, senao retorna erro
    if cliente:
        for chave, valor in cliente.items():
            print(f'{chave} - {valor}\n')
    else:
        print("Cliente não cadastrado")

    # lista os produtos
    for i, produto in enumerate(estoque[:10], start=1):
        print(f"{i} - {produto['nome']} - {produto['preco']}")

    # pergunta escolha
    escolha = int(input("Digite a opção: "))
    if escolha < 1 or escolha > len(estoque):
        print("Opção invalida")

    produto_escolhido = estoque[escolha - 1]
    qtd = int(input("Qtd: "))

    # atualizar estoque
    if qtd <= produto_escolhido['qtd'] and qtd > 0:
        produto_escolhido['qtd'] -= qtd
    else:
        print("Quantidade invalida")

    # calcular total
    total = produto_escolhido['preco'] * qtd

    print(f'Total a ser pago: {total}')

def exibir_estoque():
     for i in estoque:
        for chave, valor in i.items():
            print(f'{chave}: {valor}')
        print('\n')

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    endereco = input("Endereco: ")
    tel = input("Tel: ")

    clientes.append({'nome': nome, 'email': email, 'endereco': endereco, 'tel': tel})
    print("Cadastro realizado com sucesso!")

def cadastrar_produto():
    nome = input("Nome: ")
    preco = float(input("Preco: "))
    qtd = int(input("Qtd: "))

    if qtd < 0 or preco < 0:
        print("Valores invalidos!")
        return

    estoque.append({'nome': nome, 'preco': preco, 'qtd': qtd})
    print("Produto realizado com sucesso!")

def menu():
    print('1 - Vender\n'
                      '2 - Estoque\n'
                      '3 - Cadastrar Cliente\n'
                      '4 - Cadastrar Produto\n'
                      '5 - Sair\n')


while True:
    menu()
    opcao = int(input('Digite a opcao: '))

    match opcao:
        case 1:
            vender()
        case 2:
            exibir_estoque()
        case 3:
            cadastrar_cliente()
        case 4:
            cadastrar_produto()
        case 5:
            break
        case _:
            print("Opcao invalida")