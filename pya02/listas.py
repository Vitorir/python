# Introdução
lista_frequencia = ['Ana', 'Beatriz', 'Caio', 'Davi']

print(lista_frequencia[0])
print(lista_frequencia[1])
print(lista_frequencia[2])

registro = ['Fulano', 35, 'Masculino', 1.75, '70kg']
nome, idade, sexo, altura, peso = registro
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Peso: {peso}")

# Média
# nota1 = float(input("Digite uma nota: "))
# nota2 = float(input("Digite uma nota: "))
# nota3 = float(input("Digite uma nota: "))
# nota4 = float(input("Digite uma nota: "))

# notas = [nota1, nota2, nota3, nota4]
# print(notas[0])
# print(notas[1])

notass = []
soma = 0
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notass.append(nota)
    soma += 0

media = sum(notass) / len(notass)


# Fatiamento
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = numeros[1:-1:2]
impares = numeros[0:-1:2]
print(pares, impares)



# Palindromo
palavra = "Ola, Mundo!"
reverso = palavra[0:3]
print(reverso)


'''
1. Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre
essa lista e exiba cada número elevado ao quadrado.
'''
lista = [2, 5, 8, 11, 14]
qd = []
quadrados = [x**2 for x in lista]
for i in quadrados:
    qd.append(i**2)

'''
1. Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
'''
lista = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
soma = 0
for i in lista:
    soma += i[1]

print(soma)


'''
Escreva comandos para:
Inserir “pera” e 76 no final da lista.
Inserir o valor “gato” na posição de índice 3.
Inserir o valor 99 no início da lista.
Encontrar o índice de “oi”.
Contar o número de ocorrências de 76 na lista.
Remover a primeira ocorrência de 76 da lista.
'''

lista = []
lista.append("pera")
lista.append(76)
lista.insert(0, 99)
lista.append('oi')
print(lista.index('oi'))
print(lista.count(76))
print(lista)
lista.remove(76)
print(lista)

'''
Escreva uma função que recebe a lista de inteiros do exercício anterior e retorna 
o maior valor na lista. (Observação: existe uma a função nativa max que faz o serviço, 
mas você não deve usá-la.)
'''
inteiros = [1, 2, 3, 4 ,20, 15, 13, 31]
maior = 0
menor = inteiros[4]

for numero in inteiros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(maior, menor)