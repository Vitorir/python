'''
Leia os dados de um usuário - nome, sobrenome, idade, email - e
imprima-os enumerando os mesmos.
'''

usuario = {}
usuario['nome'] = input("NOme: ")
usuario['sobrenome'] = input("Sobrenome: ")
usuario['idade'] = input("Idade: ")
usuario['email'] = input("Email: ")

for i, valor in enumerate(usuario.values()):
    print(f'{i} - {valor}')



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
notas = []
soma = 0
for i in range(4):
    nota = float(input("Nota: "))
    soma += nota
    notas.append(nota)

minimo = min(notas)
maximo = max(notas)
media = soma / 4

situacao = ''
