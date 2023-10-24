'''
5 - Faça um programa para a leitura de quatro
notas de um aluno. O programa deve calcular a
média alcançada apresentar:
'''
# soma = 0
# for i in range(4):
#     nota = float(input("Digite o valor de uma nota: "))
#     print(nota)
#     soma = soma + nota # Padrão acumulador: atualização de variável

# media = soma / 4

# print(media)

# if media == 10:
#     print('Aprovado com distinção!')
# elif 10 > media >= 7:
#     print('Aprovado')
# else:
#     print('Reprovado!')

'''
Faça um Programa que receba 2 números e
em seguida pergunte ao usuário qual operação
ele deseja realizar. O resultado da operação
deve aparecer com uma frase que diga se o
número é: 
a. par ou ímpar;
b. positivo ou negativo;
'''


# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite um numero: "))

# opcao = int(input("\nInforme a operacao: \n1 - verificar paridade;\n 2 verificar naturalidade"))
# if opcao == 1:
#     if n1 % 2 == 0:
#         print("par")
#     else:
#         print("impar")
# elif opcao == 2:
#     if n1 > 0:
#         print('positivo')
#     elif n1 == 0:
#         print("zero")
#     else:
#         print("negativo")

empresa = 'INFINITY SCHOOL'
for letra in empresa:
    if letra in 'aeiou'.upper():
        print(letra)

numeros = range(5)
print(list(numeros))

# 1 - Noções de programação
# Programa / Programador
# Dados, tipos e conversão
# Comandos e expressões
# Operadores aritmeticos e relacionais
# Variaveis, definição e atualização
# Entrada de dados - input
# Saída de Dados - print