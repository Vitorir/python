# 1
# def calcular_imc(peso:float, altura:float) -> float:
#     imc = peso / altura**2
#     return imc

# pessoas = []
# for i in range(2):
#     nome = input("Nome: ")
#     peso = float(input("Peso: "))
#     altura = float(input("Altura: "))

#     imc = calcular_imc(peso, altura)

#     pessoas.append((nome, imc))

# for i in pessoas:
#     print(f"A pessoa {i[0]} tem imc de {i[1]:.2f}")


# 2
# def calcular_caracteres(texto:str):
#     conta_letras = 0
#     conta_espacos = 0
#     conta_sinais = 0

#     if ' ' not in texto:
#         return f"Comprimento {len(texto)}"
#     else:
#         for i in texto:
#             if i == ' ':
#                 conta_espacos += 1
#             elif i in "!@#$%¨&*()":
#                 conta_sinais += 1
#             elif i.isalpha():
#                 conta_letras += 1 
#         return f"Sinais {conta_sinais}, Letras: {conta_letras}, Espacos {conta_espacos}"

# print(calcular_caracteres('Ola, Mundo!'))


# 3
# def calcular_valor_hora(salario:float, horas_de_trabalho:int):
#     valor_hora  = salario / horas_de_trabalho
#     return valor_hora

# funcionarios = []

# contador = 0
# while contador < 2:
#     nome = input("Nome: ")
#     salario = float(input("Digite seu salario: "))
#     horas_de_trabalho = int(input("Horas de trabalho"))

#     valor_hora = calcular_valor_hora(salario, horas_de_trabalho)

#     funcionarios.append((nome, valor_hora))
#     contador += 1

# print(funcionarios)
# for i in funcionarios:
#     print(f"\nFuncionario {i[0]} tem valor/hora {i[1]}")


# 4
def somar(n1, n2):
    return n1 + n2
def subtrair(n1, n2):
    return n1 - n2
def multiplicar(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    if n2 == 0:
        return f"Erro. Divisor não pode ser zero!"
    else:
        return n1 / n2

while True:
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    opcao = int(input("""
            Digite uma opcao:
            1 - Somar
                      2 - Subtrair
                       3 - Multiplicar
                      4 - Dividir
                      5 - Sair
"""))

    match opcao:
        case 1:
            print(somar(n1, n2))
        case 2:
            print(subtrair(n1, n2))
        case 3:
            print(multiplicar(n1, n2))
        case 4:
            print(dividir(n1, n2))
        case 5:
            break
        case _:
            print("Opcao invalida!")


'''
# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# lista_imcs = []
# for i in range(2):
#     nome = input("Digite o nome")
#     peso = float(input("Peso"))
#     altura = float(input("Altura"))

#     imc = calcular_imc(peso, altura)
#     pessoa = {
#         'nome': nome,
#         'imc': imc
#     }

#     lista_imcs.append(pessoa)

# for i in lista_imcs:
#     print(i['nome'])
#     print(i['imc'])

def conta_letras(string):
    conta_letra = 0
    conta_espaco = 0
    conta_sinais = 0
    if " " in string:
        for i in string:
            if i in " ":
                conta_espaco += 1
            elif i in "!@#$%¨&*()":
                conta_sinais += 1
            else:
                conta_letra += 1
        return f"{conta_letra}, {conta_espaco} e {conta_sinais} e tem {len(string)}"
    else:
        return len(string)
    
print(conta_letras("Alo"))

def calcular_hora(salario, horas):
    valor_hora = salario / horas
'''