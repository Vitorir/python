# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
# o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input("Digite uma nota: "))
    if nota >= 0 and nota <= 10:
        print("Valor válido!")
        break
    else:
        print("Valor inválido!")

# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
# informações.
while True:
    user = input("Digite usuario: ")
    senha = input("Digite senha: ")

    if user != senha:
        print("Login valido!")
        break
    else:
        print("Digite de novo!")

# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = input("Nome: ")
    if len(nome) > 3:
        break
    else:
        print("nome invalido!")

while True:
    idade = input("Idade: ")
    if idade > 0 and idade <= 150:
        break
    else:
        print("idade invalido!")

while True:
    salario = float(input("salario: "))
    if salario > 0:
        break
    else:
        print("salario invalido!")

while True:
    sexo = input("sexo: ").lower()
    if sexo in "fm":
        break
    else:
        print("sexo invalido!")

while True:
    estado_civil = input("estado_civil: ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("estado_civil invalido!")

# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
# uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
# anos necessários para que a população do país A ultrapasse ou iguale a população do
# país B, mantidas as taxas de crescimento.
populacaoA = 80000
taxa_a = 0.03
populacaoB = 200000
taxa_b = 0.015

conta_anos = 0

while populacaoA < populacaoB:
    populacaoA += (populacaoA * taxa_a)
    populacaoB += (populacaoB * taxa_b)
    
    conta_anos += 1

print(f"Populacao A: {int(populacaoA)}")
print(f"Populacao B: {int(populacaoB)}")
print(f"Demorou {conta_anos} para que que a populacao A igualasse ou superasse B")


# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas
# de crescimento iniciais. Valide a entrada e permita repetir a operação.
while True:
    conta_anos = 0
    populacaoA = int(input("Digite a população A: "))
    taxa_a = float(input("Digite a taxa com que A cresce: "))
    populacaoB = int(input("Digite a população de B: "))
    taxa_b = float(input("Digite a taxa com que B cresce: "))

    if populacaoA < populacaoB and taxa_a > taxa_b:
        while populacaoA < populacaoB:
            populacaoA += (populacaoA * taxa_a)
            populacaoB += (populacaoB * taxa_b)
            
            conta_anos += 1
        break
    else:
        print("Valores invalidos! Repita operação!")

print(f"Populacao A: {int(populacaoA)}")
print(f"Populacao B: {int(populacaoB)}")
print(f"Demorou {conta_anos} para que que a populacao A igualasse ou superasse B")

# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.
cont = 1
while cont <= 20:
    print(cont, end=" ")
    cont += 1

# 7. Faça um programa que leia 5 números e informe o maior número.
maior = 0
cont = 1
while cont <= 5:
    n = float(input("Digite numero: "))
    if n > maior:
        maior = n
    cont += 1
print(maior)

# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.
cont = 1
soma = 0
while cont <= 3:
    num = float(input('Insira um valor: '))
    soma += num
    cont += 1

media = soma / 3
print(f"{media:.2f}")

# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
cont = 1
while cont <= 50:
    if cont % 2 != 0:
        print(cont)
    cont += 1

# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que
# estão no intervalo compreendido por eles.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

while n1 < n2 - 1:
    print(n1)
    n1 += 1