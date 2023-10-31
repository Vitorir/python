'''
2 - Escreva um programa que solicite ao usuário um número inteiro e
imprima a tabuada desse número, de 1 a 10.
3 - Escreva um programa que solicite ao usuário uma frase e conte
quantas vogais (a, e, i, o, u) existem nessa frase.
4 - Escreva um programa que possa verificar uma sequência de 10
números se são par ou ímpar.
5 - Hora de otimizar a questão número 3, após ter criado seu programa que
conta quantas vogais existem numa frase, implemente mais uma
funcionalidade. O programa agora deve imprimir a quantidade de vogais e
consoantes encontradas.
'''

# Questão 2
numero = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Questão 3
frase = input("Digite uma frase: ")
vogais = "aeiou"
contador = 0

for char in frase:
    if char.lower() in vogais:
        contador += 1

print(f"A frase possui {contador} vogais.")


# Questão 4
numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")


# Questão 5
frase = input("Digite uma frase: ")
vogais = "aeiou"
vogais_contador = 0
consoantes_contador = 0

for char in frase:
    if char.lower() in vogais:
        vogais_contador += 1
    elif char.isalpha():
        consoantes_contador += 1

print(f"A frase possui {vogais_contador} vogais e {consoantes_contador} consoantes.")


'''
1 - Você é um operador de caixa em um supermercado e precisa
implementar um programa para registrar as compras dos clientes. O
programa deve solicitar o nome e o preço de cada produto e somar o total
da compra no final. O operador pode inserir o nome e o preço de cada
produto repetidamente até que ele deseje encerrar a compra, digitando um
valor especial (por exemplo, -1). Utilize o laço de repetição while para
permitir a inserção contínua dos preços dos produtos até que o operador
decida encerrar a compra.

2 - Você foi contratado como desenvolvedor para criar um programa que
verifique a senha digitada pelos usuários. O programa deve solicitar ao
usuário que digite uma senha e verificar se ela atende aos critérios
estabelecidos. Os critérios são os seguintes:
•A senha deve ter no mínimo 8 caracteres e no máximo 12 caracteres.
'''


# Questão 1
total = 0
while True:
    nome_produto = input("Digite o nome do produto (ou -1 para encerrar a compra): ")
    if nome_produto == '-1':
        break
    preco_produto = float(input("Digite o preço do produto: "))
    total += preco_produto

print(f"Total da compra: R${total:.2f}")


# Questão 2
senha = input("Digite a senha: ")
if 8 <= len(senha) <= 12:
    print("Senha atende aos critérios.")
else:
    print("A senha não atende aos critérios.")
