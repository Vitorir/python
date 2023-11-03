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

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
email = input("Email: ")

notas = []

for i in range(4):
    nota = float(input("Nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)

if media >= 7 and media < 10:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

aluno = {
    'nome': nome,
    'notas': notas,
    'maior nota': max(notas),
    'menor nota': min(notas),
    'media': media,
    'situacao': situacao
}



'''
Refaça o programa anterior e imprima a lista dos alunos aprovados em
ordem decrescente da maior média para a menor
'''
# Lista para armazenar os dados de todos os alunos
alunos = []

# Loop para ler os dados e calcular as médias dos alunos
while True:
    # Ler os dados do aluno
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome == 'sair':
        break
    
    notas = []
    for i in range(4):
        nota = float(input("Digite a nota {}: ".format(i+1)))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    
    # Criar o dicionário com as informações do aluno
    aluno = {
        "Nome": nome,
        "Notas": notas,
        "Média": media
    }
    
    # Adicionar o dicionário à lista de alunos
    alunos.append(aluno)

# Ordenar a lista de alunos em ordem decrescente da maior média para a menor
alunos_aprovados = sorted(alunos, key=lambda x: x["Média"], reverse=True)

# Imprimir a lista dos alunos aprovados
print("\nLista de alunos aprovados (em ordem decrescente da maior média para a menor):")
for aluno in alunos_aprovados:
    print("Nome:", aluno["Nome"])
    print("Média:", aluno["Média"])
    print()