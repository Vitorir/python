'''
FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO DIGITAR UM NÚMERO INTEIRO
E MOSTRE O RESULTADO DO SEU FATORIAL
'''
inteiro = int(input("Digite um numero inteiro: "))
fat = 1
for i in range(1, inteiro + 1):
    fat = fat * i
print(fat)

# Determinar se uma senha é forte. Critérios: ter 1 - letra maiuscula, 2 - letra minuscula, 3 - numero, 4 - caractere especial
# Resolução 1
# Inicializar contadores atribuindo o valor de False como padrão
contador_minusculas = False
contador_maiusculas = False
contador_numero = False
contador_caracteres = False

senha = input("Digite uma senha: ")
# Um laço para cada critério
for i in senha:
    if i in 'abcdefghijklmnopqrstuvxyz':
        contador_minusculas = True
for i in senha:
    if i in 'abcdefghijklmnopqrstuvxyz'.upper():
        contador_maiusculas = True
for i in senha:
    if i in '123456789':
        contador_numero = True
for i in senha:
    if i in '.,!@#$%¨&*() /*-+':
        contador_caracteres = True

# Se todas as condições forem verdadeiras, diz que a senha é forte
if contador_minusculas == True and contador_maiusculas == True and contador_numero == True and contador_caracteres == True:
    print("Senha forte")
else:
    print("Senha fraca")

# Resolução 2
minusculas = 0
maiusculas = 0
numeros = 0
caracteres = 0

senha = input("Digite uma senha: ")
# Um laço para cada critério
for i in senha:
    if i in 'abcdefghijklmnopqrstuvxyz':
        minusculas += 1
    elif i in 'abcdefghijklmnopqrstuvxyz'.upper():
        maiusculas += 1
    elif i in '123456789':
        numeros += 1
    elif i in '.,!@#$%¨&*() /*-+':
        caracteres += 1

if minusculas >= 1 and maiusculas >=1 and numeros >= 1 and caracteres >= 1:
    print("Senha forte")
else:
    print("Senha fraca")


'''
FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO INSERIR 5 NÚMEROS E EXIBA NA TELA QUAL FOI O MAIOR
DOS 5
'''
maior = 0
for i in range(5):
    numero = float(input("Digite um numero: "))
    if numero > maior:
        maior = numero
print(maior)
