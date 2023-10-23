'''
Leia os dados de um usuário - nome, sobrenome, idade, email - e
imprima-os enumerando os mesmos.

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

nome = input("nome: ")
sobrenome = input("sobrenome: ")
idade = int(input("Idade: "))
email = input("Email: ")

notas = []
soma = 0
maior = 0
menor = 0
for i in range(4):
    nota = float(input("Digite nota: "))
    if maior < nota:
        maior = nota
    elif menor < nota:
        menor < nota
    soma += nota
    notas.append(nota)

media = soma / 4
situacao = ''
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'



aluno = {
    'nome': nome,
    'sobrenome': sobrenome,
    'maior-nota': maior,
    'menor-nota': menor,
    'media': media,
}

aluno['situacao'] = situacao

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")