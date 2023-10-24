# 1. Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre
# essa lista e exiba cada número elevado ao quadrado.
numeros = [2, 5, 8, 11, 14]
for i in numeros:
    print(i ** 2)

# Dada a tupla de nomes de países: ("Brasil", "Canadá", "Austrália", "Espanha", "Índia"), crie um
# programa que itere sobre a tupla e exiba na tela cada país seguido pelo número de
# caracteres presentes em seu nome.

paises = ("Brasil", "Canadá", "Austrália", "Espanha", "Índia")
for i in paises:
    print(i, len(i))

# 1. Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
# preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
# que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela. em python
lista = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
valor = 0
for item, preco in lista:
    valor += preco


# 1. Considere a seguinte lista de palavras: ["Python", "é", "uma", "linguagem", "poderosa"]. Escreva
# um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4
# letras.
palavras = ["Python", "é", "uma", "linguagem", "poderosa"]
for i in palavras:
    if len(i) > 5:
        print(i)

