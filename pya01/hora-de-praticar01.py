# ■ Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

'''
while True:
    user = input("Digite um nome de usuario: ")
    password = input("Digite uma senha: ")
    # Condição de Parada
    if user != password:
        break
    else:
        print("Erro! A senha não pode ser igual a usuário")
'''

# Prova
# Definir variáveis
# user = 'vitor'
# password = '123'

# while True:
#     usuario = input("digite usuario: ")
#     senha = input("digite senha: ")

#     # Verificação
#     if usuario == user and senha == password:
#         print("Login validado!")
#         break
#     else:
#         print("Erro!")


# ■ Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade deve estar entre 0 e 150.")

while True:
        salario = float(input("Digite seu salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário deve ser maior que zero.")

while True:
    sexo = input("Digite seu sexo ('f' ou 'm'): ")
    if sexo.lower() in ['f', 'm']:
        break
    else:
        print("Sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ")
    if estado_civil.lower() in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")

print("\nInformações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)

# ■ Faça um programa que leia 5 números e informe o maior número.
'''
 maior = 0
 for i in range(5):
     num = float(input('Digite um numero: \n'))
     if maior < num:
         maior = num
 print(f'número: {maior:.1f}', num)
'''

# ■ Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
soma = 0
cont = 0
while(cont < 5):
    num = float(input('Digite um numero: \n'))
    soma += num # acumulador
    cont += 1
media = soma / cont
print(f'Soma: {soma}\n' + f'Cont: {cont}')
print(f'Media: {media}')
'''

# ■ Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
for i in range(1, 51):
    if i % 2 != 0:
        print(i)
'''

# Faça um Programa que verifique se a letra digitada pelo usuário é vogal ou consoante.
# while True:
#     letra = input("Digite a letra: ")

#     if letra.lower() == 'sair':
#         break

#     if len(letra) == 1:
#         letra.lower()

#         if letra in 'aeiou':
#             print("vogal")
#         else:
#             print("consoante")
#     else:
#         print("digite uma letra")
