# Sequencias
# lista = []
# lista2 = list()

# tupla = ()
# tupla2 = tuple()

# Operações
# lista_dados = [15, 'texto', 17.4, [1, 'Fulano'], (2, 'Sicrano')]
# print(lista_dados[0])
# print(lista_dados[-1])


# lista_dados.append((3, 'Beltrano'))

# print(lista_dados[0:-1])

# lista_compras = ['Laranja', 'pães', 'água', 'ovos']
# lista_comprados = lista_compras[1:3]
# print(lista_comprados)

# item = input("Qual item quer remover da lista? ")
# lista_compras.remove(item)
# print(lista_compras)

# linguagens = ['python', 'javascript', 'php']
# py, js, php = linguagens
# print(py, js, php)

# 1. Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre
# essa lista e exiba cada número elevado ao quadrado.
# numeros = [2, 5, 8, 11, 14]
# quadrados = []
# for i in numeros:
#     quadrados.append(i ** 2)

# quadrado = [x **2 for x in numeros]
# print(quadrados)

# 2. Dada a tupla de nomes de países: ("Brasil", "Canadá", "Austrália", "Espanha", "Índia"), crie um
# programa que itere sobre a tupla e exiba na tela cada país seguido pelo número de
# caracteres presentes em seu nome.
# tupla = ("Brasil", "Canadá", "Austrália", "Espanha", "Índia")
# for i in tupla:
#     print(i, len(i))

# 3. Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
# preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
# que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
frutas = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
valor_total = 0
for i in frutas:
    valor_total += i[1]
print(valor_total)

# 4. Considere a seguinte lista de palavras: ["Python", "é", "uma", "linguagem", "poderosa"]. Escreva
# um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4
# letras.
palavras = ["Python", "é", "uma", "linguagem", "poderosa"]
for i in palavras:
    if len(i) > 4:
        print(i)