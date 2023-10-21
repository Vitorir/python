# 1 Faça um programa que leia 3 números e imprima o maior deles.
# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite um numero: "))
# n3 = float(input("Digite um numero: "))

# if n1 > n2 and n1 > n3:
#     print ("O maior número é ", n1)
# elif n2 > n1 and n2 > n3:
#     print("O maior numero é ", n2)
# else:
#     print(n3)

'''
2 - Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o mesmo número de pontos, criar um programa que informe se uma equipe foi classificada, de acordo com a seguinte especificação: 
      • Ler os pontos obtidos por cada jogador da equipe; 
      • Mostrar esses valores em ordem decrescente; 
      • Se a soma dos pontos for maior do que 100, imprimir a        média aritmética entre eles, caso contrário, imprimir a mensagem "Equipe desclassificada".
# '''
# j1 = int(input("Digite pontos: "))
# j2 = int(input("Digite pontos: "))
# j3 = int(input("Digite pontos: "))

# maior = j1
# menor = j1

# if j2 > maior:
#     maior = j2
# elif j2 < menor:
#     menor = j2
    
# if j3 > maior:
#     maior = j3
# elif j3 < menor:
#     menor = j3

# soma = j1 + j2 + j3
# medio = soma - (maior + menor) # o resto que sobrar tirando maior e menor

# print("O valor em ordem decrescente é:", maior, medio, menor)
# if soma > 100:
#     media = soma / 3
#     print(media)
# else: 
#     print("Equipe desqualificada")

# '''
# 2 - segunda solução
# '''
# ponto1 = int(input("Digite os pontos do jogador 1: "))
# ponto2 = int(input("Digite os pontos do jogador 2: "))
# ponto3 = int(input("Digite os pontos do jogador 3: "))

# # Ordenação dos números em ordem decrescente com estruturas condicionais
# if ponto1 >= ponto2 and ponto1 >= ponto3:
#     maior = ponto1
#     if ponto2 >= ponto3:
#         medio = ponto2
#         menor = ponto3
#     else:
#         medio = ponto3
#         menor = ponto2
# elif ponto2 >= ponto1 and ponto2 >= ponto3:
#     maior = ponto2
#     if ponto1 >= ponto3:
#         medio = ponto1
#         menor = ponto3
#     else:
#         medio = ponto3
#         menor = ponto1
# else:
#     maior = ponto3
#     if ponto1 >= ponto2:
#         medio = ponto1
#         menor = ponto2
#     else:
#         medio = ponto2
#         menor = ponto1

# # Imprime os pontos em ordem decrescente
# print("Pontos em ordem decrescente:", maior, medio, menor)


'''
slide 4 - 01. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 
'''

# count = 1
# while count <= 50:
#     if count % 2 != 0:
#         print(count)
#     count += 1

'''
02. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
user = input("Digite usuario: ")
senha = input("Digite senha: ")

while user == senha:
    print("Senha não pode ser igual ao usuario")
    user = input('Insira o usuario: ')
    senha = input('Insira o senha: ')
    
print("Senha aceita com sucesso")

'''
03. Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
count = 1
soma = 0
while count <= 5:
    num = int(input("Digite um número: "))
    soma += num
    count += 1
media = soma / count
print(soma, media)

'''
04. Em uma escola, os alunos das turmas do fundamental fizeram uma prova de matemática. Cada turma possui um número de alunos. 
Criar um programa que imprima: 
• quantidade de alunos aprovados; 
• média de cada turma; 
• percentual de reprovados. 

Obs.: Considere aprovado com nota >= 7.0
'''

# Solicita ao usuário o número de alunos na turma
numero_alunos = int(input("Digite o número de alunos na turma: "))

# Inicializa variáveis para cálculos
total_alunos = 0
aprovados = 0
soma_notas = 0

# Loop para obter as notas e calcular estatísticas
for i in range(numero_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    if nota >= 7.0:
        aprovados += 1
    soma_notas += nota
    total_alunos += 1

# Calcula média da turma e percentual de reprovados
media_turma = soma_notas / total_alunos
percentual_reprovados = ((total_alunos - aprovados) / total_alunos) * 100

# Imprime as estatísticas da turma
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Média da turma: {media_turma:.2f}")
print(f"Percentual de reprovados: {percentual_reprovados:.2f}%")

'''
05. Uma pesquisa de opinião realizada no Ceará com 50 pessoas, teve as seguintes perguntas: 
• Qual o seu time de coração? 
1-Fortaleza; 
2-Ceará; 
3-Ferroviário; 
4-Icasa; 
5-Outros 
• Onde você mora? 
1-Fortaleza; 
2-Caucaia; 
3-Outros 
• Qual o seu salário? 
'''

# Inicializa as variáveis para contagem e cálculos
fortaleza_torcedores = 0
ceara_torcedores = 0
ferroviario_torcedores = 0
icasa_torcedores = 0
outros_torcedores = 0
fortaleza_salario_total = 0
fortaleza_contagem = 0
caucaia_ferroviario = 0
fortaleza_ceara = 0

# Loop para realizar a pesquisa com 50 pessoas
for _ in range(50):
    time = int(input("Qual o seu time de coração? (Digite o número correspondente) "))
    moradia = int(input("Onde você mora? (Digite o número correspondente) "))
    salario = float(input("Qual o seu salário? "))

    if time == 1:
        fortaleza_torcedores += 1
        fortaleza_salario_total += salario
        fortaleza_contagem += 1
    elif time == 2:
        ceara_torcedores += 1
        if moradia == 1:
            fortaleza_ceara += 1
    elif time == 3:
        ferroviario_torcedores += 1
        if moradia == 2:
            caucaia_ferroviario += 1
    elif time == 4:
        icasa_torcedores += 1
    elif time == 5:
        outros_torcedores += 1

# Calcula as médias e imprime as estatísticas
if fortaleza_contagem > 0:
    media_salario_fortaleza = fortaleza_salario_total / fortaleza_contagem
    print(f"Número de torcedores do Fortaleza: {fortaleza_torcedores}")
    print(f"Média salarial dos torcedores do Fortaleza: {media_salario_fortaleza}")
    print(f"Número de pessoas moradoras de Caucaia, torcedores do Ferroviário: {caucaia_ferroviario}")
    print(f"Número de pessoas de Fortaleza, torcedores do Ceará: {fortaleza_ceara}")
else:
    print("Nenhum torcedor do Fortaleza participou da pesquisa.")
