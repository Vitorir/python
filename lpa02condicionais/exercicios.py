'''
Faça um Programa que peça as 4 notas bimestrais, mostre a média e a situação final do aluno.
Observação: para ser 
considerado aprovado a média deverá ser maior ou igual a 7.
'''

'''
Programa para adição de dois valores inteiros e exibição do resultado com ajustes baseados em sua magnitude:
'''
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))

soma = valor1 + valor2

if soma > 20:
    resultado = soma + 8
    print("Resultado é:", resultado)
else:
    resultado = soma - 5
    print("Resultado é:", resultado)


''''
Programa para verificar se um número é múltiplo de 3 ou não:

'''
numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")


'''
Programa para verificar se um número é divisível por 3 e 7:

'''
numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 7 == 0:
    print("É divisível por 3 e 7")
else:
    print("Não é divisível por 3 e 7")


'''
Programa para calcular a idade com base no ano de nascimento e no ano atual:

'''
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_nascimento > ano_atual or ano_nascimento < 0:
    print("Ano de nascimento inválido.")
else:
    idade = ano_atual - ano_nascimento
    print("A idade é:", idade)
