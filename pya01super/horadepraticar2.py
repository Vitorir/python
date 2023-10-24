'''
1 - Você é um operador de caixa em um supermercado e precisa
implementar um programa para registrar as compras dos clientes. O
programa deve solicitar o nome e o preço de cada produto e somar o total
da compra no final. O operador pode inserir o nome e o preço de cada
produto repetidamente até que ele deseje encerrar a compra, digitando um
valor especial (por exemplo, -1). Utilize o laço de repetição while para
permitir a inserção contínua dos preços dos produtos até que o operador
decida encerrar a compra.
'''
soma = 0
while True:
    nome = str(input("Digite o nome do produto: ou -1 para terminar"))
    if nome == '-1':
        break

    preco = float(input("Digite o preco do produto: "))
    soma = soma + preco
    
print(f"Total: {soma:.2f}")

'''
2 - Você foi contratado como desenvolvedor para criar um programa que
verifique a senha digitada pelos usuários. O programa deve solicitar ao
usuário que digite uma senha e verificar se ela atende aos critérios
estabelecidos. Os critérios são os seguintes:
•A senha deve ter no mínimo 8 caracteres e no máximo 12 caracteres.
'''
while True:
    senha_digitada=str(input('Digite sua senha: '))
    if 12 >= len(senha_digitada) >= 8:
        print('Senha correta!')
        break
    else:
        print("Digite de novo!")

