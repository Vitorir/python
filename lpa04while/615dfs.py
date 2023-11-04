'''
QUESTÕES EXTRAS:

FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO DIGITAR UMA SENHA
E VERIFICA SE É UMA SENHA FORTE

REGRAS:
UMA SENHA FORTE TEM QUE CONTAR NO MÍNIMO
1 LETRA MAIÚSCULA
1 LETRA MINÚSCULA
1 CARACTER ESPECIAL
1 NÚMERO 
8 DIGITOS
'''
# maiusculas = False
# minusculas = False
# especiais = False
# numero = False

# senha = input("Digite uma senha: ")
# for letra in senha:
#         if letra.isupper():
#             maiusculas = True
#         elif letra.islower():
#             minusculas = True
#         elif letra in '!@#$%¨&*()':
#             especiais = True
#         elif letra.isdigit():
#             numero = True

# if maiusculas and minusculas and especiais and numero and len(senha) > 8:
#      print('Senha forte!')
# else:
#      print('Senha fraca')

# maiusculas = 0
# minusculas = 0
# especiais = 0
# numeros = 0

# senha = input("Digite uma senha: ")

# for letra in senha:
#     if letra in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ':
#         maiusculas += 1
#     elif letra in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'.lower():
#         minusculas += 1
#     elif letra in '!@#$%¨&*()':
#         especiais += 1
#     elif letra in '0123456789':
#         numeros += 1

# if maiusculas >= 1 and minusculas >= 1 and especiais >= 1 and numeros >=1 and len(senha) >8:
#     print('Senha forte!')
# else:
#     print("Senha fraca")


'''
FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO DIGITAR UM NÚMERO INTEIRO
E MOSTRE NA TELE O SEU  FATORIAL
EXEMPLO:
5! = 5x4x3x2x1
'''
# numero = int(input("Numero: "))
# fat = 1
# for i in range(1, numero + 1):
#     fat = fat * i

# print(fat)


'''
Faça um programa que verifica se uma senha é forte:
critérios:
- Tem no mínimo 8 caracteres;
- Ter Letra
- Ter Número

Obs: com while
'''
# while True:
#     senha = input("Senha: ")
#     conta_numero = False
#     conta_letra = False

#     for i in senha:
#         if i.isdigit():
#             conta_numero = True
#         elif i.isalpha():
#             conta_letra = True
        
#     if conta_numero and conta_letra and len(senha) >= 8:
#         print("Senha valida")
#         break
#     else:
#         print("Senha invalida")

'''
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
# while True:
#     nota = float(input("Digite uma nota: "))

#     if 10 >= nota > 0:
#         print("Nota valida!")
#         break
#     else:
#         print("Nota invalida!")

'''
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''
# while True:
#     nome = input("Digite nome ")
#     senha = input("Digite senha: ")

#     if nome == senha:
#         print("Invalido!")
#     else:
#         print("Login bem sucedido!")
#         break

'''
3. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
# while True:
#     nome = input("Digite o nome: ")
#     if len(nome) > 3:
#         print("Correto")
#         break
#     else:
#         print("Digite de novo!")

# idade = int(input("Digite uma idade: "))
# while idade > 150 or idade < 0:
#     idade = int(input("Digite outra idade: "))

# print(f"Sua idade é: {idade}")

sexo = input("Sexo :")
while sexo != 'f' and sexo != 'm':
    sexo = input("Digite novamente: ")