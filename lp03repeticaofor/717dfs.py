'''
01. Faça um programa em Python que leia um valor inteiro e mostre a tabuada
de 1 a 10 do valor lido.
'''
inteiro = int(input("inteiro: "))
for i in range(1, 11):
    print(f"{inteiro} * {i} = {inteiro * i}")

'''
02. Faça um programa que leia um nome de usuário e verifique se o mesmo esta
contido na lista de usuários criados, se estiver mostre uma mensagem com o nome.
'''
usuarios = ["Gabriel", "Danny", "Arthur"]
usuario = input("Usuario: ")
if usuario in usuarios:
    print(usuario)

nomes = ["Gabriel", "Danny", "Arthur"]
sobrenomes = ['Silva', 'Santos']

for nome in nomes:
    for sobrenome in sobrenomes:
        nome = nome + " "  + sobrenome
    print(nome)

'''
03. Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis
por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos
em sequência.
'''
for i in range(5, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")

'''
04. Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. Por exemplo,
se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
'''
num = int(input("Num: "))
soma = 0
for i in range(1, num+1):
    soma += i
print(soma)

'''
Slide 16.
 Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. Para cada consumidor, são digitados os seguintes dados: 
• número do consumidor 
• quantidade de kWh consumidos durante o mês 
• tipo (código) do consumidor 
1-residencial, preço em reais por kWh = 0,3 
2-comercial, preço em reais por kWh = 0,5 
3-industrial, preço em reais por kWh = 0,7 
Os dados devem ser lidos até que seja encontrado o consumidor com número 0 (zero). 
O programa deve calcular e imprimir: 
• O custo total para cada consumidor 
• O total de consumo para os três tipos de consumidor 
• A média de consumo dos tipos 1 e 2 

'''

total_residencial = 0
total_comercial = 0
total_industrial = 0

count_residencial = 0
count_comercial = 0

while True:
    numero = int(input("Numero do consumidor: "))

    if numero == 0:
        break
    
    kWh = float(input("KWh: "))
    tipo = input("Tipo do consumidor: ")

    

    if tipo == "residencial":
        custo = kWh * 0.3
        total_residencial += custo
        count_residencial += 1
    elif tipo == 'comercial':
        custo = kWh * 0.5
        total_comercial += custo
        count_comercial += 1
    elif tipo == 'industrial':
        custo = kWh * 0.7
        total_industrial += custo

total_consumo = total_residencial + total_comercial + total_industrial
media_dos2 = (total_comercial + total_residencial) / (count_comercial + count_residencial)

print(f"Total consumo residencial: R${total_residencial:.2f}")
print(f"Total consumo comercial: R${total_comercial:.2f}")
print(f"Total consumo industrial: R${total_industrial:.2f}")
print(f"Total consumo: {total_consumo}")
print(f"Media_dos2 {media_dos2}")

'''
Slide 17
Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
que na lista oficial de cada país consta, além de outros dados, peso e idade de
12 jogadores, crie um programa que apresente as seguintes informações: 

• O peso médio e a idade média de cada um dos times; 
• O atleta mais pesado de cada time; 
• O atleta mais jovem de cada time; 
• O peso médio e a idade média de todos os participantes. 
'''
soma_peso = 0
soma_idade = 0

mais_pesado = 0
nome_pesado = ''
mais_jovem = 100
nome_jovem = ''

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    idade = int(input("idade: "))

    soma_peso += peso
    soma_idade += idade

    if peso > mais_pesado:
        mais_pesado = peso
        nome_pesado = nome

    if idade < mais_jovem:
        mais_jovem = idade
        nome_jovem = nome


media_peso = soma_peso / 3
media_idade = soma_idade / 3

print(f"\nMédias: {media_idade:.2f}, {media_peso}")
print(f"Mais jovem: {nome_jovem} - {mais_jovem}")
print(f"Mais pesado: {nome_pesado} - {mais_pesado}")

'''
Na Usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
radioativo. Sabendo-se que este perde 25% de sua massa a cada 30 segundos,
criar um programa em Python que imprima o tempo necessário para que a massa deste material se torne menor que 0,10 grama.
O programa deve calcular o tempo para várias massas.
'''
massa_inicial = float(input("Insira a massa inicial do material em gramas: "))

tempo = 0 
while massa_inicial > 0.1:
    massa_inicial *= 0.75 
    tempo += 30

print(f"Tempo necessário para que a massa seja menor que 0,10 gramas: {tempo} segundos")


'''
Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação e seu peso. Faça um programa que imprima
a identificação e o peso do boi mais gordo e do boi mais magro (supondo que não haja empates).
'''
num_bois = 90

mais_gordo_peso = 0
mais_magro_peso = float('inf')
mais_gordo_identificacao = ''
mais_magro_identificacao = ''

for i in range(num_bois):
    identificacao = input(f"Informe a identificação do boi {i + 1}: ")
    peso = float(input(f"Informe o peso do boi {i + 1}: "))

    if peso > mais_gordo_peso:
        mais_gordo_peso = peso
        mais_gordo_identificacao = identificacao

    if peso < mais_magro_peso:
        mais_magro_peso = peso
        mais_magro_identificacao = identificacao

print(f"Boi mais gordo: Identificação - {mais_gordo_identificacao}, Peso - {mais_gordo_peso}")
print(f"Boi mais magro: Identificação - {mais_magro_identificacao}, Peso - {mais_magro_peso}")

'''
Faça um programa em Python que imprima uma matriz de 4 linhas por 4 colunas,
sendo que na primeira linha devem ser impressos os valores de 1 à 4 e
partir da segunda linha, os valores impressos devem ser múltiplos da linha anterior.
'''

print("1 2 3 4")
linha_anterior = 1

for i in range(3):
    linha_atual = ""
    for j in range(1, 5):
        linha_atual += str(linha_anterior * (j + 1)) + " "
    linha_anterior = linha_anterior * 2
    print(linha_atual.strip())
