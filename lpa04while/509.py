# Aula 04 - For
# Percorrendo coleções numéricas
for x in [1, 2, 3]:
    print(x)

for x in range(1, 11, 2):
    print(x)

# Percorrendo strings
alfabeto = "qwertyuiopasdfghjklçzxcvbnm"
for letra in alfabeto:
    if letra in 'aeiou':
        print(letra, "é uma vogal")

# Percorrendo listas
nomes = ['Joao', 'Gabriel', 'Lucas']
n = input("Digite um nome: ")

for nome in nomes:
    if nome == n:
        print("Parabéns, achamos o nome: ", nome)

# Questoes de cabeça
'''
1. Faça um programa que receba um texto e verifique quantos caracteres, espaços e numeros possui o texto

2. Faça um programa que leia uma senha e verifique se é uma senha forte. Critérios:
- Maiuscula
- Minuscula
- Numero
- especiais
'''

# Instruções break e continue



usuario = input("Usuario: ")
senha = input("Senha: ")

while usuario == senha:
    usuario = input("Usuario: ")
    senha = input("Senha: ")

'''
Slide 16
'''
qtd_res = 0
qtd_com = 0
qtd_ind = 0

total_res = 0
total_com = 0
total_ind = 0

ncons = int(input("Digie o numero do consmidor: "))
while ncons != 0:
    qtdKwh = int(input("Digite qtd de kwh: "))
    tipo = int(input("Digite o tipo do consumidor: "))

    if tipo == 1:
        calculo = qtdKwh * 0.3
        total_res += calculo
        qtd_res += 1
    elif tipo == 2:
        calculo = qtdKwh * 0.5
        total_com += calculo
        qtd_com += 1
    elif tipo == 3:
        calculo = qtdKwh * 0.7
        total_ind += calculo
        qtd_ind += 1

    ncons = int(input("Digite o numero do consumidor: "))

print(f'total_ind {total_ind}')
print(f'total_res {total_res}')
print(f'total_com {total_com}')
total = total_com + total_res + total_ind
print(total)

media_1_e_2 = (total_res + total_com) / (qtd_res + qtd_com)
print(media_1_e_2)


'''
slide 17
'''
somapeso = 0
somaidade = 0

maior_peso = 0
menor_idade = 100

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    idade = int(input("Idade: "))

    if peso > maior_peso:
        maior_peso = peso
    
    if idade < menor_idade:
        menor_idade = idade

print(f"Média peso: {somapeso / 3}")
print(f"Media idade: {somaidade / 3}")
print(f"Maior peso: {maior_peso}")
print(f"Menor idade: {menor_idade}")

'''
slide 19
'''
id_maisgordo = 0
id_maismagro = 0
mais_gordo = 0
mais_magro = 1000

for i in range(5):
    id = int(input("Digite o id: "))
    peso = float(input("Peso: "))

    if peso > mais_gordo:
        mais_gordo = peso
        id_maisgordo = id
    elif peso < mais_magro:
        mais_magro = peso
        id_maismagro = id

print(f"Id do mais gordo: {id_maisgordo} com peso: {mais_gordo}")
print(f"Id do mais gordo: {id_maismagro} com peso: {mais_magro}")


