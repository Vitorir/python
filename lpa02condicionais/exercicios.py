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

# 12
valor_hora = float(input("digite valor por hora"))
horas_trabalhadas = int(input("Horas trabalhadas: "))

valor_total = valor_hora * horas_trabalhadas
ir = valor_total * 0.11
print(ir)
inss = valor_total * 0.08
print(inss)
sindicato = valor_total * 0.05
print(sindicato)
salario_liquido = valor_total - ir - inss - sindicato
print(salario_liquido)

# lp 07
'''

7. Depois da liberação do governo para as mensalidades dos planos de saúde, as pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Faça um programa que entre com o nome e a idade de uma pessoa e imprima o nome e o valor que ela deverá pagar.
               Idade                                               Valor 
              Até 10 anos                                     R$30,00 
             Acima de 10 até 29 anos            R$60,00 
             Acima de 29 até 45 anos           R$120,00 
             Acima de 45 até 59 anos           R$150,00 
             Acima de 59 até 65 anos           R$250,00
             Maior que 65 anos                       R$400,00
'''
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade <= 10:
    valor = 30.00
elif idade <= 29:
    valor = 60.00
elif idade <= 45:
    valor = 120.00
elif idade <= 59:
    valor = 150.00
elif idade <= 65:
    valor = 250.00
else:
    valor = 400.00

print(f"Nome: {nome}")
print(f"Valor a ser pago: R$ {valor:.2f}")

