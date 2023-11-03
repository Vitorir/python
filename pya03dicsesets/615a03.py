usuario = {
    'username': 'fulano123',
    'password': 'senha123',
    'email': 'fulano123@gmail.com',
    'idade': 24,
    'profissional': True
}

print(len(usuario))
lista_chaves = list(usuario) # username, password, email, idade, profissional

usuarios_publicos = usuario.copy()
del usuarios_publicos['password']
del usuarios_publicos['email']
print(usuarios_publicos)



#Questão 1
#Dado O Dicionário pessoa com a seguinte estrutura: {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True},
#faça um programa que imprima na tela quantas chaves existem nesse dicionário, e quais os nomes de cada uma delas

pessoa = {
    "Nome": "Abel",
    "Idade": 28, 
    "Altura": 1.79, 
    "Habilitacao": True
}
print(f"Esse dicionário tem {len(pessoa)} chaves")

lista_chaves = list(pessoa) #["Nome", "Idade", "Altura", "Habilitação"]

for chave in lista_chaves:
    print(chave)



#Questão 2
#Dado o Dicionário Animal com a seguinte estrutura: {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": 1, "Adestrado": "Sim"},
#faça um programa que cheque se o cachorro tem mais de 2 anos de idade, se tiver, crie uma nova chave chamada "Vacinado" e atribua o valor de True, caso contrário mude o valor da chave "Adestrado" para "Não"

animal = {
    "Especie": "Cachorro", 
    "Raça": "Pinscher", 
    "Idade": 5, 
    "Adestrado": "Sim"
    }

if animal["Idade"] > 2:
    animal["Vacinado"] = True
else:
    animal["Adestrado"] = "Não"

print(animal)



#Questão 3
# Dado o dicionário Carro com a seguinte estrutura: {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"},
# faça um programa que cheque se existe uma chave chamada "Cor" no dicionário, se existir, delete ela se não crie uma e atribua a ela "vermelho".
carro = {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"}
if 'Cor' in carro.keys():
    del carro['Cor']
else:
    carro['Cor'] = 'vermelho'

print(carro)


#Questão 4
#Dado o dicionário Computador com a seguinte estrutura {"Processador": "I7", "Memoria": "16GB", "SSD": "256GB"}
#faça um programa que crie uma copia desse dicionário e  guarde ele em outra variável chamada Computador2
# e depois limpe o dicionario Computador
computador = {"Processador": "I7", "Memoria": "16GB", "SSD": "256GB"}
computador2 = computador.copy()
computador.clear()
print(computador)
print(computador2)

#Questão 6
#Dado o lista["Banda", "Musica"], crie apartir dessa lista um #dicionário e depois insira na key Banda o valor
#  "Iron Maiden", e no #campo "Música" o valor "Powerslave", depois faça uma busca nesse #objeto criado Cuja busca irá buscar
#  por duas chaves diferentes, uma #chave chamada Banda  e outra chave chamada "Integrantes", caso a chave #exista dentro
#  do dicionário mostre ela na tela, caso não existe mostra #uma mensagem informando que a chave procurada não existe
lista= ["Banda", "Musica"]
dicio = dict.fromkeys(lista)

dicio['Banda'] = 'Iron Maiden'
dicio['Musica'] = 'Powerslave'

print(dicio.get('Banda', 'Não existe banda nesse dicionário'))
print(dicio.get('Integrantes', 'Não existe Integrantes nesse dicionário'))
print('Banda' in dicio)
print('Integrantes' in dicio)


#Questão 7
#Dado o dicionário Turma com a seguinte estrutura {"Modulo": "Python", "Duracao": 4.5, "Nome": "515 DFS", "Alunos": 30}
#faça um programa que itere sobre esse dicionario como uma lista e mostre na tela o nome da chave - o valor 
# e depois mostre usando a função keys apenas as chaves que existem nesse dicionário
turma = {
    'Modulo': 'Python',
    'Duracao': 4.5,
    'Nome': '515 DFS',
    'Alunos': 30
}

