# 7 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Inicializar variáveis de máximo e mínimo
maior = num1
menor = num1

# Verificar se num2 é maior ou menor
if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

# Verificar se num3 é maior ou menor
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f"O maior número é {maior} e o menor número é {menor}.")


# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1

# Mostrar os números em ordem decrescente
print(f"Os números em ordem decrescente são: {maior}, {medio}, {menor}.")

