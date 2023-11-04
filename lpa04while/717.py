'''
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

qtd_residencial = 0
qtd_comercial = 0

while True:
    numero = int(input('Numero: '))
    if numero == 0:
        break

    kWh = float(input("kWh: "))
    tipo = input('Tipo: ')

    if tipo == 'residencial':
        custo = kWh * 0.3
        total_residencial += custo
        qtd_residencial += 1
    elif tipo == 'comercial':
        custo = kWh * 0.5
        total_comercial += custo
        qtd_comercial += 1
    elif tipo == 'industral':
        custo = kWh * 0.7
        total_industrial += custo

consumo_total = total_industrial + total_comercial + total_residencial
media = (total_residencial + total_comercial) / (qtd_comercial + qtd_residencial)

print(f'Total consumo residencial: {total_residencial}')
print(f'Total consumo comercial: {total_comercial}')
print(f'Total consumo industrial: {total_industrial}')
print(f'Total consumo: {consumo_total}')
print(f'Media consumo 1 e 2: {media}')


'''
Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se que na lista oficial de cada país consta, além de outros dados, peso e idade de 3 jogadores, crie um programa que apresente as seguintes informações: 

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
Na Usina de Angra dos Reis, os técnicos analisam a perda de massa de um material radioativo. Sabendo-se que este perde 25% de sua massa a 
cada 30 segundos, criar um programa em Python que imprima o tempo necessário para que a massa deste material se torne menor que 0,10 grama. 
O programa deve calcular o tempo para várias massas.
'''
while True:
    massa = float(input("Massa: "))
    if massa == 0:
        break

    perda = 0.25
    tempo = 0

    while massa >= 0.10:
        massa -= (massa * perda)
        tempo += 30
        
    print(f"O tempo para que a massa se reduzi a 0.10 grama é {tempo} segundos")


# Resolução 2
massa = float(input("Massa (digite 0 para encerrar): "))

while massa != 0:
    perda = 0.25
    tempo = 0

    while massa >= 0.10:
        massa -= (massa * perda)
        tempo += 30

    print(f"O tempo para que a massa se reduza a 0.10 grama é de {tempo} segundos.")
    massa = float(input("Massa (digite 0 para encerrar): "))



'''
Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contendo 
seu número de identificação e seu peso. Faça um programa que imprima a identificação e o peso do boi mais gordo e 
do boi mais magro (supondo que não haja empates).
'''
mais_gordo = 0
mais_magro = 1000

nome_gordo = ''
nome_magro = ''

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    if peso > mais_gordo:
        mais_gordo = peso
        nome_gordo = nome

    if peso < mais_magro:
        mais_magro = peso
        nome_magro = nome

print(f'O mais gordo foi {nome_gordo} com peso: {mais_gordo}')
print(f'O mais magro foi {nome_magro} com peso: {mais_magro}')


'''
Faça um programa em Python que imprima uma matriz de 4 linhas por 4 colunas, 
sendo que na primeira linha devem ser impressos os valores de 1 à 4 e partir da segunda linha, os valores impressos devem ser múltiplos 
da linha anterior.
'''
# Imprimindo a primeira linha
for j in range(1, 5):
    print(j, end=" ")
print()

# Imprimindo as linhas subsequentes
for i in range(2, 5):
    for j in range(1, 5):
        print((i-1) * j, end=" ")
    print()
