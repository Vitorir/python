'''
7. Ler uma lista de 15 números inteiros e mostre cada número juntamente com a sua posição na lista. 
'''
inteiros = [10, 20, 33, 44, 512, 621, 7, 8, 9, 10, 11, 12]
for i, numero in enumerate(inteiros):
    print(f'{i+1} = {numero}')


'''
8. Faça um programa que armazene 15 números inteiros em um vetor e depois permita 
que o usuário digite um número inteiro para ser buscado no vetor, se for encontrado o programa 
deve imprimir a posição desse número no vetor, caso contrário, deve imprimir a mensagem: "Nao encontrado!".
'''
lista_inteiros = [21, 13, 22, 44, 12]
num = int(input("Digite um numero: "))
if num in lista_inteiros:
    print(lista_inteiros.index(num))
else:
    print("Não encontrado!")

'''
0. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. 
alcule e armazene a média. Armazene também a situação do aluno: 1- Aprovado ou 2-Reprovado. 
Ao final o programa deve imprimir uma listagem contendo as notas, a média e a situação de cada 
aluno. Utilize quantas listas forem necessárias para armazenar os dados.
'''
alunos = []

for i in range(2):
    nome = input("Nome: ")
    n1 = float(input("Nota: "))
    n2 = float(input("Nota2: "))

    media = (n1 + n2) / 2
    if media >= 7:
        situacao = 1
    else:
        situacao = 2
    
    alunos.append([nome, n1, n2, media, situacao])

for aluno in alunos:
    print(f'{aluno}')