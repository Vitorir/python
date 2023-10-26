'''
Leia o salario de um trabalhador e o valor da prestação de um
empréstimo. Se a prestação for maior do que 20% do salário imprima:
Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
'''
salario = float(input("Salario: "))
prestacao = float(input("Prestacao: "))

if prestacao > (salario * 0.2):
    print("Emprestimo concedido")
else:
    print("nao concedido")

'''
Faça um programa que receba a altura e o sexo de uma pessoa e calcule
e mostre seu peso ideal, utilizando as seguintes formulas (onde h
corresponde a altura):
Homens: (72,7 * h) - 58
Mulheres: (62, 1 * h) - 44,7
'''
altura = float(input("Altura: "))
sexo = input("Sexo: ")

if sexo in 'Mm':
    peso_ideal = (72.7 * altura) - 52
elif sexo in 'Ff':
    peso_ideal = (62.1 * altura) - 44.7
    
print("Peso Ideal: {:.2f}".format(peso_ideal))

'''
Faça um algoritmo que calcule a media ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
'''
nota1 = int(input("Nota da Prova 1: "))
nota2 = int(input("Nota da Prova 2: "))
nota3 = int(input("Nota da Prova 3: "))
ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

if ponderada > 60:
    print("Aprovado!")
else:
    print("Reprovado")


'''
Faça um programa para montar a tabela de multiplicação
de números de 1 a 10 (ex.: 1 x 1 = 1, 1 x 2 = 2, etc.)
'''
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    
'''
Faça um programa para determinar o número de dígitos de
um número inteiro positivo informado.
'''
numero = int(input("Digite um número: "))
digitos = 0

while numero != 0:
    numero = numero // 10
    digitos += 1
print(digitos)

'''
Faça um programa para calcular a série de Fibonacci para
um número informado pelo usuário, sendo F(0) = 0, F(1) = 1
e F(n)= F(n-1)+F(n-2)
'''
n = int(input('Numero: '))
a, b = 0, 1

if n == 0:
    resultado = a
elif n == 1:
    resultado = b
else:
    for i in range(2, n+1):
        resultado = a + b
        a = b
        b = resultado

print(f"O número na posição {n} na série de Fibonacci é: {resultado}")


'''
Listas e Tuplas
Faça um Programa que leia uma lista de 5 números
inteiros, mostre a soma, a multiplicação e os números.
'''
inteiros = []
mult = 1
for i in range(5):
    num = int(input('numero: '))
    inteiros.append(num)
    mult *= num

soma = sum(inteiros)
print(soma, mult)

'''
Faça um Programa que peça a altura de 5 pessoas,
armazene cada altura e Imprima as alturas na ordem
inversa a ordem lida.
'''
alturas = []
for i in range(5):
    altura = float(input("Altura: "))
    alturas.insert(0, altura)
    
for i in alturas:
    print(i)

alturas = []
for i in range(5):
    altura = float(input("Altura: "))
    alturas.append(altura)
    

for i in reversed(altura):
    print(i)


'''
Faça um Programa que leia 5 números inteiros, calcule e
mostre a soma dos quadrados dos elementos do vetor.
'''
inteiros = []
ao_quadrado = []
for i in range(5):
    num = int(input("num: "))
    inteiros.append(num)
    ao_quadrado.append(num**2)

quadrados = [x**2 for x in inteiros]
print(sum(quadrados))
print(sum(ao_quadrado))

agendas = []
for i in range(2):
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    agenda = {
        'cpf': cpf,
        'nome': nome,
        'idade': idade
    }

    agendas.append(agenda)

for i in agendas:
    print(f"A {i['nome']} com cpf {i['cpf']} tem {i['idade']} anos")


agendas = [
    {"cpf": "11111111111", "nome": "João", "idade": 30},
    {"cpf": "22222222222", "nome": "Maria", "idade": 25},
    {"cpf": "33333333333", "nome": "Pedro", "idade": 35},
    {"cpf": "44444444444", "nome": "Ana", "idade": 28},
    {"cpf": "55555555555", "nome": "Mariana", "idade": 32}
]

for i in agendas:
    print(f"{i['cpf']}, {i['idade']}, {i['nome']}")

'''
Considere um sistema onde os dados são armazenados
em dicionários. Nesse sistema existe um dicionario
principal e o dicionário de backup. Cada vez que o
dicionário principal atinge tamanho 5, ele imprime os
dados na tela e apaga o seu conteúdo. Crie um programa
que insira dados em um dicionário, realizando o backup a
cada dado e excluindo os dados do dicionário principal
quando ele atingir tamanho 5.
'''
principal = {}
backup = {}

for i in range(10):
    chave = input("Digite o CPF: ")
    valor = input("Email: ")

    principal[chave] = valor

    if len(principal) > 5:
        for chave, valor in principal.items():
            print(f"{chave} - {valor}")
            
        backup.update(principal)
        principal.clear()
        
print(f"Dicionario de backup: {backup}")


'''
Funções
Faça uma função chamada somaImposto. A função possui dois
parâmetros: taxa_imposto, que é a porcentagem de imposto sobre
vendas e custo, que é o custo de um item antes do imposto. A
função retorna o valor de custo alterado para incluir o imposto
sobre vendas.
'''
def somaImposto(taxa, custo):
    valor_imposto = custo * (taxa / 100)
    custo_total = custo + valor_imposto
    return custo_total

print(somaImposto(10, 100))


'''
Faça um programa que converta da notação de 24 horas para a
notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M; 6:44 em 6:44 A.M. A função recebe dois
parâmetros, a hora e o minuto.
'''
def converter_hora(hora, minuto):
    if hora == 00:
        hora_real = 12
        sufix = 'PM'
    elif hora < 12:
        hora_real = hora
        sufix = 'AM'
    elif hora == 12:
        hora_real = hora
        sufix = 'PM'
    elif hora > 12:
        hora_real = hora - 12
        sufix = 'PM'
    return f"{hora_real}:{minuto} {sufix}"

print(converter_hora(6, 44))