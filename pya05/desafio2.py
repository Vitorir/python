clientes = []
estoque = []

def menu():
    print('1 - Vender\n'
          '2 - Estoque\n'
          '3 - Cadastrar Cliente\n'
          '4 - Cadastrar Produto\n'
          '5 - Sair\n')
    

def vender():
    nome = input("Nome: ")
    cliente = None

    # verificando se existe cliente
    for i in clientes:
        if i['nome'] == nome:
            cliente = i

    # printando dados do cliente
    if cliente:
        for chave, valor in cliente.items():
            print(f'{chave} - {valor}')
    else:
        print("Cliente não cadastrado!")

    # listando produtos
    for i, produto in enumerate(estoque[:10]):
        print(f"{i} - {produto['nome'] - produto['preco']} - {produto['qtd']}")

    escolha = int(input("Digite opcao: "))
    produto_escolhido = estoque[escolha - 1]

    qtd = int(input("Quantidade: "))

    if qtd >= produto_escolhido['qtd'] and qtd > 0:
        produto_escolhido['qtd'] -= qtd
    else:
        print("Quantidade invalida!")

    total = produto_escolhido['preco'] * produto_escolhido['qtd']

    print(f'O total é: {total}')

    


def exibir_estoque():
    for i in estoque:
        for chave, valor in i.items():
            print(f'{chave}:{valor}')
        print(f'\n')

def cadastrar_cliente():
    # nome, endereço, e-mail e telefone.
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    tel = input("Tel: ")

    cliente = {
        'nome': nome,
        'email': email,
        'endereco': endereco,
        'tele': tel
    }

    clientes.append(cliente)
    print("Cliente adicionado com sucesso!\n")

def cadastrar_produto():
    #como nome, código, preço e quantidade
    nome = input("Nome: ")
    codigo = input("Codigo: ")
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))

    estoque.append({'nome': nome, 'codigo': codigo, 'preco': preco, 'qtd': qtd})


def main():
    while True:
        menu()
        opcao = int(input("opcao: "))

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
main()