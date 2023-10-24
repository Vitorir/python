# 1°: Faça um programa que leia 3 números e informe o maior número.
# FOR
# maior = 0
# for i in range(3):
#     num = int(input("Digite um numero: "))
#     if num > maior:
#         maior = num
# print(maior)

# WHILE
# maior = 0
# cont = 1
# while cont <= 3:
#     num = int(input("Digite um numero: "))
#     if num > maior:
#         maior = num
#     cont += 1
# print(maior)

'''
2°: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de SOMA de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.
'''
# FOR
# numero = int(input("Digite numero: "))
# for i in range(1, 11):
#     soma = numero + i
#     print(f'{numero} + {i} = {soma}')

# WHILE
numero = int(input("Digite numero: "))
cont = 1
while cont <= 10:
    soma = numero + cont
    print(f'{numero} + {cont} = {soma}')
    cont += 1

'''
3°: Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
# FOR
# soma = 0
# for i in range(5):
#     num = float(input('Informe um valor: '))
#     soma += num
# media = soma / 5
# print(f'A soma é {soma}, a média é {media}.')

# WHILE
# soma = 0
# count = 0
# while count < 5:
#     num = float(input('Informe um valor: '))
#     soma += num
#     count += 1
# media = soma / 5
# print(f'A soma é {soma}, a média é {media}.')

'''
4°: Faça um programa que receba várias notas e que calcule e mostre a média das notas digitadas.
Finalize digitando a nota igual a zero.
'''
# WHILE
soma = 0
conta_notas = 0
nota = 1
while nota != 0:
    nota = float(input('Nota: '))
    if nota != 0:
        soma += nota
        conta_notas += 1

media = soma / conta_notas
print(media)