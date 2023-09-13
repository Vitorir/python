# Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.
'''
N = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
menor = N[0]
maior = N[0]
soma = 0
for i in N:
    soma += i
    if menor > i:
        menor = i
    if maior < i:
        maior = i
print(soma, menor, maior)
'''

'''
N = int(input('Digite o valor de numeros: \n'))
menor = 0; maior = 0; soma = 0
for i in range(N):
    num = float(input('Digite um numero: '))
    while num < 0 or num > 1000:
        num = float(input('Numero inválido! Digite outro numero'))
    soma += num
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

print(f'Soma: {soma} \nMaior: {maior} \nMenor: {menor}')
'''

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e
# menores que 16.
'''
while True:
    numero = int(input("Digite um numero de 0 a 15 "))

    if 0 < numero < 16:
        resultado = 1
        for n in range(1, numero + 1):
            resultado *= n
        print(resultado)
        break
    else:
        print('Erro')
'''

# ■ Faça um programa que peça um número inteiro e determine se ele é ou não
# um número primo. Um número primo é aquele que é divisível somente por ele
# mesmo e por 1.
cont = 0
n = int(input('Insira um número para saber se ele é primo: '))
eh_primo = False

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1

if cont >= 3:
    print('O número escolhido não é primo!')
else:
    eh_primo = True
    print('O número escolhido é primo!')
