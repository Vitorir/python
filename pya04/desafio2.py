clientes = []
produtos = []

# Função para exibir o menu principal
def exibir_menu():
    print("\nMenu Principal:")
    print("1. Vender")
    print("2. Estoque")
    print("3. Cadastrar Cliente")
    print("4. Cadastrar Produto")
    print("5. Sair")

# Função para realizar uma venda
def vender():
    nome_cliente = input("Digite o nome do cliente: ")
    cliente_encontrado = False
    for cliente in clientes:
        if cliente['nome'] == nome_cliente:
            cliente_encontrado = True
            print(f"Dados do cliente: {cliente}")
            break
    if not cliente_encontrado:
        print("Cliente não encontrado.")

    print("\nProdutos disponíveis:")
    exibir_estoque()
    codigo_produto = input("Digite o código do produto que deseja comprar: ")
    quantidade_venda = int(input("Digite a quantidade que deseja comprar: "))

    for produto in produtos:
        if produto['codigo'] == codigo_produto:
            if produto['quantidade'] >= quantidade_venda:
                produto['quantidade'] -= quantidade_venda
                total_venda = quantidade_venda * produto['preco']
                print(f"Venda realizada. Total a pagar: R${total_venda}")
            else:
                print("Quantidade insuficiente em estoque.")
            break
    else:
        print("Produto não encontrado.")

# Função para exibir o estoque
def exibir_estoque():
    print("\nEstoque:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Código: {produto['codigo']}, Quantidade: {produto['quantidade']}")

# Função para cadastrar um cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    novo_cliente = {
        'nome': nome,
        'endereco': endereco,
        'email': email,
        'telefone': telefone
    }
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso.")

# Função para cadastrar um produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    codigo = input("Digite o código do produto: ")

    # Verifica se o código já existe
    for produto in produtos:
        if produto['codigo'] == codigo:
            print("Código de produto já existente. Tente novamente com um código diferente.")
            return

    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade inicial em estoque: "))

    novo_produto = {
        'nome': nome,
        'codigo': codigo,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso.")

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        vender()
    elif opcao == "2":
        exibir_estoque()
    elif opcao == "3":
        cadastrar_cliente()
    elif opcao == "4":
        cadastrar_produto()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
