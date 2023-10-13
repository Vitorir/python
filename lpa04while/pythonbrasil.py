# texto = 'texto'
# texto.count('t')
# text = str()

# while True:
#     nota = float(input("Digite uma nota: "))
#     if 0 <= nota <= 10:
#         print("valido")
#         break
#     else:
#         print("Invalido! Digite de novo!")

while True:
    sexo = input("Digite o sexo: [F | M]").upper()
    if sexo == "F":
        print("Feminino")
        break
    elif sexo == "M":
        print("Masculino")
        break
    else:
        print("Sexo invalido!")




while True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome invalido")

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade <= 150:
        break
    else:
        print("Idade invalida!")

while True:
    salario = float(input("Digite o salario: "))
    if salario > 0:
        break
    else:
        print("Salario invalido!")

while True:
    sexo = input("Sexo: [F ou M]")
    if sexo == 'f' or sexo == 'm':
        break
    else: 
        print("Invalido!")