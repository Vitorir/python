# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
# o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# while True:
#     nota = float(input("Escreva uma nota: "))
#     if nota >= 0 and nota <= 10:
#         print(f"A nota é: {nota}")
#         break
#     else:
#         print("Valor inválido! Digite uma nova nota!")


# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
# informações.
# while True:
#     usuario = input("Digite o usuario: ")
#     senha = input("Senha: ")
#     if usuario != senha:
#         print("Login válido!")
#         break
#     else:
#         print("Erro! Digite usuario diferente de senha")


# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# while True:
#     nome = input("Digite nome: ")
#     if len(nome) > 3:
#         break
#     else:
#         print("Nome invalido!")

# while True:
#     idade = int(input("Digite idade: "))
#     if idade > 0 and idade < 150:
#         break
#     else:
#         print("Idade invalido!")

# while True:
#     sexo = input("digite sexo: ")
#     if sexo.lower() in ["f", "m"]:
#         break
#     else:
#         print("Sexo invalido!")

# while True:
#     estado_civil = input("digite estado civil: ")
#     if estado_civil.lower() in ['s', 'c', 'v', 'd']:
#         break
#     else:
#         print("Estado civil invalido!")

# print(f"nome: {nome}",
#       f"\nidade: {idade}",
#       f"\nsexo: {sexo}",
#       f"\nestado_civil: {estado_civil}"
#       )

# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.
for i in range(1, 21):
    print(i)


contador = 1
while contador <= 20:
    print(contador, end=" ")
    contador += 1

# 7. Faça um programa que leia 5 números e informe o maior número.
# maior = 0

# for i in range(5):
#     numero = float(input("Digite numero: "))
#     if numero > maior:
#         maior = numero
# print(maior)