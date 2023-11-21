# import random

# def gerar_escolha_jogador():
#     escolha = input("Digite sua escolha [Pedra - Papel - Tesoura]")

'''
Faça um programa que leia 3 números e imprima o maior deles.
'''
n1 = float(input("Numero: "))
n2 = float(input("Numero: "))
n3 = float(input("Numero: "))

if n1 == n2 == n3:
    print('são iguais')
elif n1 >= n2 and n1 >= n3:
    print(n1, 'é maior')
elif n2 >= n3 and n2 >= n1:
    print(n2, 'é maior')
else:
    print(n3, 'é maior')

'''
Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o mesmo número de pontos, criar um programa que informe se uma equipe foi classificada, de acordo com a seguinte especificação: 
      • Ler os pontos obtidos por cada jogador da equipe; 
      • Mostrar esses valores em ordem decrescente; 
      • Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles, caso contrário, imprimir a mensagem "Equipe desclassificada". 
'''
j1 = int(input("Pontos: "))
j2 = int(input("Pontos: "))
j3 = int(input("Pontos: "))

if j1 > j2 and j1 > j3:
    if j2 > j3:
        print(j1, j2, j3)
    else:
        print(j1, j3, j2)
elif j2 > j1 and j2 > j3:
    if j1 > j3:
        print(j2, j1, j3)
    elif j3 > j1:
        print(j2, j3, j1)

soma = j1 + j2 + j3
if soma > 100:
    media = soma / 3
    print(media)
else:
    print("Equipe desqualificada")

'''
01. Faça um programa que imprima na tela apenas os 
números ímpares entre 1 e 50. 
'''
num = 1
while num < 51:
    if num % 2 == 0:
        print(num)
    
    num+=1


'''
02. Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.
'''
usuario = input("Usuario: ")
senha = input("Senha: ")
while usuario == senha:
    print("Digite dados diferentes!")
    usuario = input("Usuario: ")
    senha = input("Senha: ")

'''
03. Faça um programa que leia 5 números e informe a soma e a 
média dos números.
'''
i = 0
soma = 0

while i < 5:
    num = input("Numero: ")
    soma += num

media = soma / 5

'''
4. Em uma escola, os alunos das turmas do fundamental fizeram uma prova de matemática. Cada turma possui um número de alunos. 
Criar um programa que imprima: 
• quantidade de alunos aprovados; 
• média de cada turma; 
• percentual de reprovados.

Obs.: Considere aprovado com nota >= 7.0
'''

i = 0
soma = 0
aprovados = 0
reprovados = 0

while i < 5:
    nota = float(input("Digite nota: "))
    
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

    soma += nota
    i += 1

print(aprovados)
print(soma / 5)
print((reprovados / 5) * 100)