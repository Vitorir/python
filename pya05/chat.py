# Lista de produtos disponíveis no estoque
estoque = []

# Lista de clientes cadastrados
clientes = []

def exibir_menu():
    print("MENU PRINCIPAL")
    print("1. Vender")
    print("2. Estoque")
    print("3. Cadastrar Cliente")
    print("4. Cadastrar Produto")
    print("5. Sair")

def vender():
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = None
    
    # Verificar se o cliente está cadastrado
    for c in clientes:
        if c["nome"] == nome_cliente:
            cliente = c
            break
    
    if cliente:
        print("Dados do cliente:")
        print("Nome:", cliente["nome"])
        print("Endereço:", cliente["endereco"])
        print("Email:", cliente["email"])
        print("Telefone:", cliente["telefone"])
    else:
        print("Cliente não cadastrado.")
    
    print("Produtos disponíveis:")
    if estoque:
        for i, produto in enumerate(estoque[:10]):
            print(f"{i+1}. {produto['nome']} - R$ {produto['preco']}")
        
        escolha = input("Digite o número do produto a ser vendido (ou '0' para sair): ")
        
        if escolha == "0":
            return
        
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(estoque):
                raise ValueError
        except ValueError:
            print("Opção inválida.")
            return
        
        produto_escolhido = estoque[escolha - 1]
        
        quantidade = input("Digite a quantidade a ser vendida: ")
        
        try:
            quantidade = int(quantidade)
            if quantidade <= 0 or quantidade > produto_escolhido["quantidade"]:
                raise ValueError
        except ValueError:
            print("Quantidade inválida.")
            return
        
        # Atualizar estoque
        produto_escolhido["quantidade"] -= quantidade
        
        # Calcular total da venda
        total = produto_escolhido["preco"] * quantidade
        
        print("Venda realizada com sucesso.")
        print("Total: R$", total)
    else:
        print("Nenhum produto disponível no estoque.")

def exibir_estoque():
    print("Estoque:")
    if estoque:
        for produto in estoque:
            print("Nome:", produto["nome"])
            print("Código:", produto["codigo"])
            print("Quantidade:", produto["quantidade"])
            print("----")
    else:
        print("Nenhum produto disponível no estoque.")

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        "nome": nome,
        "endereco": endereco,
        "email": email,
        "telefone": telefone
    }
    
    clientes.append(cliente)
    
    print("Cliente cadastrado com sucesso.")

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    codigo = input("Digite o código do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade inicial em estoque: "))
    
    if quantidade < 0 or preco < 0:
        print("Valores inválidos.")
        return
    
    produto = {
        "nome": nome,
        "codigo": codigo,
        "preco": preco,
        "quantidade": quantidade
    }
    
    estoque.append(produto)
    
    print("Produto cadastrado com sucesso.")

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        vender()
    elif opcao == "2":
        exibir_estoque()
    elif opcao == "3":
        cadastrar_cliente()
    elif opcao == "4":
        cadastrar_produto()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")