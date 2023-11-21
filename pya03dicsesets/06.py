usuario = ['fulano', 'fulano@gmail.com', 'senha123']
usuario2 = ['beltrano', 'beltrano@gmail.com', 'senha123']
usuario3 = ['sicrano', 'sicrano@gmail.com', 'senha123']

usuarios = [usuario, usuario2, usuario3]
print(usuarios)
print(usuarios[1][1])

usuario = {
    "id": '2839478239yfhdfbhsdbfh238',
    "nome": 'Fulano',
    "email": "fulano@gmail.com",
    "senha": 'senha123'
}

# Acessar valores
print(usuario['email'])
x = usuario.get('email', 'Erro, não existe essa chave!')
print(x)

print(usuario.keys())
print(usuario.values())


# Alterar valores
usuario['endereco'] = 'Rua São Jose das quantas, 277'
print(usuario['endereco'])

usuario['senha'] = 'Senha#$123321'
print(usuario['senha'])

usuario.update({"tel": "85987654321"})
print(usuario['tel'])

usuario['caracteristicas_fisicas'] = {
    'altura': 1.78,
    'peso': 76,
    'idade': 22,
    'cor': 'branco'
}

print(usuario)

'''
Leia os dados de um usuário - nome, sobrenome, idade, email - e
imprima-os enumerando os mesmos.
'''

# usuario = {}
# usuario['nome'] = input("NOme: ")
# usuario['sobrenome'] = input("Sobrenome: ")
# usuario['idade'] = input("Idade: ")
# usuario['email'] = input("Email: ")

'''
03
'''
dict = {}
num = int(input("Qtde de pessoas? ")) #2
for i in range(num):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    chave = f'pessoa {i+1}'
    dict[chave] = {
        "nome":nome,
        "idade":idade
    }  
print(dict)

'''
04. Também usando dict, imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave;
'''
for chave in sorted(usuario.keys()):
    valor = usuario[chave]
    print(f'{chave} - {valor}')

'''
05. Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os dados (nome, telefone) de todos os contatos do usuário de forma que a agenda fique completa, imprima todos os contatos e por fim, faça uma pesquisa pelo nome e apresente o telefone.
'''
agenda = {}

tam = int(input("Digite o tamanho da agenda: "))
for i in range(tam):
    nome = input("Nome")
    telefone = input("Telefone")
    agenda['nome'] = telefone
    
nome_pesquisa = input("Digite o nome a ser pesquisado: ")


'''
06. Crie um programa que armazena um grupo de 3
pessoas contendo o número de telefone de cada 
uma, a idade de cada uma, depois mostre todas as 
informações e a informação apenas de uma pessoa.
'''
grupo = {
    "pessoa1": {
        "tel": '85123984',
        'idade': 25
    },
    "pessoa2": {
        "tel": '851239842342',
        'idade': 23
    }
}

for pessoa, info in grupo.items():
    print(f'{pessoa} - {info}')


'''
06. estoque = {"tomate": [1000, 2.30],
 			    "alface": [500, 0.45],
 			    "batata": [2001, 1.20],
                "feijão": [100, 1.50]}

Dado o dicionário acima só efetue a venda e dê baixa no estoque quando a qtde em estoque for maior que a qtde solicitada.
'''



'''
Leia 4 notas de um aluno, calcule sua média e armazene em um
dicionário as seguintes informações:
a. Nome do aluno
b. As 4 notas obtidas
c. Maior nota
d. Menor nota
e. Média
f. Situação
Agora imprima as informações deste aluno na saída padrão

Refaça o programa anterior e imprima a lista dos alunos aprovados em
ordem decrescente da maior média para a menor
'''
# notas = []
# soma = 0
# for i in range(4):
#     nota = float(input("Nota: "))
#     soma += nota
#     notas.append(nota)

# minimo = min(notas)
# maximo = max(notas)
# media = soma / 4

# situacao = ''
