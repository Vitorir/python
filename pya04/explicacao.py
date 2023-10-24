# Funções nativas
# print()
# input()
# def imprime_nome(nome:str, idade:int) -> str:
#     '''Imprime o nome e idade de uma pessoa'''
#     return f"{nome} tem {idade} anos"

# print(imprime_nome(idade=25, nome='Fulano'))

'''
IMC = peso / altura ** 2
Crie uma função para calcular o IMC de 4 pessoas.
Atenção: Use as seguintes estruturas:
-laço de repetição.
-listas
'''
# def calcular_imc(peso: float, altura: float):
#     resultado = peso / (altura ** 2)
#     return resultado

# lista_imcs = []

# for i in range(2):
#     nome = input("Nome: ")
#     peso = float(input("Digite o peso: "))
#     altura = float(input("Digite o altura: "))

#     pessoa_imc = calcular_imc(peso, altura)
#     pessoa = {
#         'nome': nome,
#         'imc': pessoa_imc
#     }

#     lista_imcs.append(pessoa)

# print(lista_imcs)

# for i in lista_imcs:
#     print(f"{i}")

'''
2.Crie uma função que retorne quantas letras possui uma palavra. Se for passado uma
frase, a função deverá retornar o número de letras, espaços vazios e quantos sinais
de pontuação.
'''
# def contador(string):
#     conta_letras = 0
#     conta_espaço = 0
#     conta_sinais = 0

#     if " " not in string:
#         return len(string)
    
#     else:
#         for letra in string:
#             if letra in " ":
#                 conta_espaço += 1
#             elif letra in "!@#$%¨&*(),.;'":
#                 conta_sinais += 1
#             else:
#                 conta_letras += 1

#     return f"""
#             Espaços: {conta_espaço}
#             Letras: {conta_letras}
#             Pontuação: {conta_sinais}
#             """

# print(contador("Ola, mundo!"))

# 3.Crie uma função que calcule o valor/hora do funcionário, em seguida implemente
# essa função em um programa de calcular hora e valor do funcionário.
# def calcular_valor(valor, horas):
#     return valor/horas

# valor = float(input("Digite quanto você ganha por mes: "))
# horas = int(input('Digite as horas: '))

# print(calcular_valor(valor, horas))

# 4.Crie Funções para calcular de acordo com os operadores matemáticos de uma
# calculadora:
def somar(n1, n2):
    return n1 + n2
def subtrair(n1, n2):
    return n1 - n2
def multiplicar(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    return n1 / n2

while True:
    opcao = input("""
            Escolha uma operação
            + - somar
            - - Subtrair
            / - Dividir
            * - Multiplicar
""")
    num1 = float(input("numero 1"))
    num2 = float(input("numero 2"))
    
    match opcao:
        case '+':
            print(somar(num1, num2))
        case '-':
            print(subtrair(num1, num2))
        case '*':
            print(multiplicar(num1, num2))
        case "/":
            print(dividir(num1, num2))
        case _:
            print("Operação invalida!")