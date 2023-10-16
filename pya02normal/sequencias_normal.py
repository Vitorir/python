# 1. Faça um programa que leia o nome de uma pessoa e imprima o mesmo invertido
# nome = input("Digite um nome: ")
# invertido = nome[::-1]
# print(invertido)

# 2. Faça um programa que leia 4 notas de um aluno e imprima sua média. Após a média ser calculada,
# informe se o aluno foi ou não aprovado.
# a. Aprovado --- média maior ou igual a 7
# b. Reprovado --- média menor que 5
# c. Em recuperação --- média entre 5 e 7
# notas = []
# for i in range(2):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)

# media = sum(notas) / len(notas)

# 3. Faça um programa que leia 10 números e depois mostre o maior e o menor números lidos
# notas = []
# for i in range(4):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)

# print(min(notas))
# print(max(notas))

# ■ Faça um programa que leia 10 números inteiros e separe os mesmos em pares e ímpares. Mostre
# quantos pares foram lidos, bem como o maior e o menor número par. Faça o mesmo para os ímpares.
# pares = []
# impares = []

# for i in range(5):
#     inteiro = int(input("Digite um inteiro: "))
#     if inteiro % 2 == 0:
#         pares.append(inteiro)
#     else:
#         impares.append(inteiro)
    
# print(pares)
# print(impares)

# ■ Faça um programa que leia 10 números inteiros e imprima a lista ordenada em ordem crescente e
# decrescente.
# lista = []
# for i in range(10):
#     lista.append(i)

# print(sorted(lista))
# print(sorted(lista, reverse=True))

# ■ Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou.
# Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.
registros = []
for i in range(4):
    nome = input("Digite o nome do vendedor: ")
    valor = float(input("digite o valor: "))

    registros.append([nome, valor])

print(sorted(registros))
print(sorted(registros, reverse=True))


# ■ Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou.
# Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.
# Leitura dos nomes dos vendedores e valores de venda
vendedores = []
valores_venda = []

for i in range(4):
    nome_vendedor = input("Digite o nome do vendedor: ")
    valor_venda = float(input("Digite o valor total de venda realizado pelo vendedor: "))
    vendedores.append(nome_vendedor)
    valores_venda.append(valor_venda)

# Ordenação dos vendedores pelos valores de venda em ordem decrescente
vendedores_ordem_decrescente = [v for _, v in sorted(zip(valores_venda, vendedores), reverse=True)]

# ■ Faça um programa que leia os nomes dos 3 nadadores que subirão ao pódio na ordem do primeiro
# colocado para o terceiro. Imprima na tela a posição do nadador e seu nome.

nadadores = []

for i in range(3):
    nome_nadador = input("Digite o nome do nadador: ")
    nadadores.append(nome_nadador)

# Imprimir a posição e o nome dos nadadores
print("Resultado do pódio:")
print("1º lugar:", nadadores[0])
print("2º lugar:", nadadores[1])
print("3º lugar:", nadadores[2])