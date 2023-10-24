'''
1 - Escreva um programa que solicite ao usuário um número inteiro positivo
e realize uma contagem regressiva a partir desse número até zero,
imprimindo cada número no processo.
'''
positivo = int(input("Digite um inteiro: "))

while positivo >= 0:
    print(positivo)
    positivo -= 1

'''
2 - Escreva um programa que solicite ao usuário um número inteiro e
imprima a tabuada desse número, de 1 a 10.
'''
count = 1
numero = float(input("Digite um numero: "))
while count <= 10:
    print(f"{count} * {numero} = {count * numero}")
    count += 1

for i in range(1, 10):
    print(f"{i} * {numero} = {i * numero}")

