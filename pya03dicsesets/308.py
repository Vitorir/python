'''
emails = ['americanas@gmail.com', 'magazineluiza@gmail.com', 'casasbahia@gmail.com']

emails_ordenados = [
    {'americanas': 'americanas@gmail.com', 'contato': '34331215'}, 
    {'magazine': 'magazine@gmail.com'},
    {'casasbahia': 'casasbahia@gmail.com'}
]

usuarios = [
    {'Nome': 'Fulano', 'Idade': 34, 'email': 'fulano@gmail.com', 'contato': '85987612345'},
    {'Nome': 'Beltrano', 'Idade': 30, 'email': 'beltrano@gmail.com', 'contato': '85987612345'},
]

print(usuarios[1]['email'])

# JSON - Notação de objeto javascript
# Documentos Firestore
# Documentos MONGODB
'''


# Sets
'''
Transforma a lista abaixo em um set: lista = [1,2,6,9,5,2]
'''
# lista = [1,2,6,9,5,2]
# set1 = set(lista)
# print(set1)

# '''
# Remova um elemento do conjunto e mostre qual foi excluído;
# '''
# excluido = set1.remove(2)
# print(excluido)

# '''
# Verifique se o número 9 existe no set;
# '''
# print(9 in set1)

# '''
# Adicione o número 10 ao conjunto;
# '''
# set1.add(10)
# print(set1)

# '''
# Remova o item 5 do set;
# '''
# set1.remove(5)
# print(set1)

# '''
# Crie uma cópia do conjunto;
# '''
# copia = set1.copy()
# print(copia)

# '''
# Atualize um conjunto pela a união com outro conjunto.
# '''
# outro_conjunto = {-1,-2,-3,-4,-5}

# '''
# Faça união do conjunto da questão 6 com da 7;
# '''
# uniao = copia.union(outro_conjunto)
# print(f'Uniao: {uniao}')


# Dicionarios
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2015
}

print(carro)

x = carro['modelo']
print(x)
x = carro.get('modelo', "Erro, marca não está no dicionario!")
print(x)

y = carro.values()
print(y)

carro['ano'] = 1990
print(carro)

carro.update({"marca": "Toy"})
print(carro)


'''
01. Crie um dicionário d e coloque nele seus dados: nome, idade, 
telefone, endereço;
'''
d = {
    "nome": "fulano",
    "idade": 23,
    "telefone": "859123456",
    "endereco": {
        "logradouro": "São José das Quantas",
        "numero": 277,
        "UF": "CE",
        "Bairro": "Zé das Oliveiras"
    }
}
print(d["nome"])

dict = {}
dict['nome'] = input("Digite nome: ")


for chave, valor in dict.items():
    print(chave, valor)

# 05
tamanho = int(input("Digite o tamanho da agenda: "))
agenda = {}

for i in range(tamanho):
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    agenda[nome] = telefone

    

for chave, valor in agenda.items():
    print(f"Nome {chave} - Telefone: {valor}")

nome = input("Digite o nome: ")
if nome in agenda:
    print(f"Telefone do contato: {nome} é {agenda[nome]}")
else:
    print("Não encontrado!")


'''
06. Crie um programa que armazena um grupo de 3 pessoas 
contendo o número de telefone de cada uma, a idade de 
cada uma, depois mostre todas as informações e a informação 
apenas de uma pessoa.
'''

pessoas = {
    "pessoa1": {
        "telefone": "(85) 99876-5432",
        "idade": 25
    },
    "pessoa2": {
        "telefone": "(85) 99876-1234",
        "idade": 30
    },
    "pessoa3": {
        "telefone": "(85) 99876-9876",
        "idade": 35
    }
}

for pessoa, dados in pessoas.items():
    print(f"{pessoa} - {dados['telefone']} - {dados['idade']}")

especifica = input("Digite uma pessoa específica: ")
if especifica in pessoas:
    print(f"{pessoas[especifica]['telefone']}, {pessoas[especifica]['idade']}")
else:
    print("Pessoa não está contida no grupo")