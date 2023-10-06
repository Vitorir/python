# faça um programa que leia o sexo da pessoa, identificado pelos valores ‘M’ ou ‘F’.
# Caso esteja errado, peça para digitar novamente e
# dê 3 tentativas.
'''
for tentativa in range(3):
    sexo = input("Digite o sexo (M/F): ").upper()  # Converte a entrada para maiúsculas
    if sexo == 'M' or sexo == 'F':
        print(f"Sexo digitado: {sexo}")
        break
    else:
        print("Sexo incorreto. Tente novamente.")
else:
    print("Você excedeu o número de tentativas permitidas.")
'''
# ■ Crie um programa que leia dois valores e mostre
# uma tabela de multiplicação do primeiro valor pelo
# segundo valor a partir de 1.
'''
n1 = 3
n2 = 4

for i in range(1, 4 + 1):
    print(f"{n1} * {i} = {n1 * i}")
'''

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
# deseja ver a tabuada.
numero = int(input("Digite o numero: "))
for i in range(1, 10):
    print(f"{i} * {numero}: {numero * i}")