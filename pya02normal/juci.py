'''
Dada a lista abaixo, faça o que se pede:
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Lista reversa;
Lista ordenada;

Acrescente ao final da lista o número 27;
Exclua o número 9;
Apague o elemento de posição 10;
Faça a soma dos elementos;
Mostre o menor elemento da lista;
Mostre os número pares;
Mostre os números ímpares;
Acrescente os número 89 e 91 após o número 4;
'''
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista.reverse()
print(lista)
lista.sort()
print(lista)

lista.append(27)
print(lista)
lista.remove(9)
print(lista)
lista.pop(10)
print(lista)
print(sum(lista))
print(min(lista))

print(list(filter(lambda x : x % 2 == 0, lista)))
for i in lista:
    if i % 2 != 0:
        print(i)

lista.insert(4, (89, 91))
print(lista)

'''
2. Ler uma lista de 5 números inteiros e mostre cada número da lista.
'''
# lista = []
# for i in range(5):
#     numero = float(input("Numero: "))
#     lista.append(numero)

# for numero in lista:
#     print(numero, end=" ")

'''
3. Ler uma lista de 10 números inteiros e mostre-os na ordem inversa. 
'''
inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inteiros.reverse()
print(inteiros)

reverso = sorted(inteiros, reverse=True)
print("Reverso: ", reverso)

'''
5. Ler uma lista com 20 idades e exibir a maior e menor.
'''
idades = [12, 42, 30, 25, 80]
print(max(idades))
print(min(idades))

'''
. Faça um programa que armazene 10 letras em uma lista e 
imprima uma listagem numerada.
'''
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i, letra in enumerate(letras):
    print(f'{i + 1} => {letra}')

'''
8. Faça um programa que armazene 15 números inteiros em um vetor e depois 
permita que o usuário digite um número inteiro para ser buscado no vetor, se 
for encontrado o programa deve imprimir a posição desse número no vetor, 
caso contrário, deve imprimir a mensagem: "Nao encontrado!".
'''
# num_inteiros = []
# num_inteiro = int(input("Numero inteiro: "))
# while num_inteiro != 0:
#     num_inteiros.append(num_inteiro)

#     num_inteiro = int(input("Numero inteiro: "))

# numero = int(input("Numero a ser buscado: "))
# for n in num_inteiros:
#     if n == numero:
#         print(f'Número encontrado!')
#         break
    
# if numero not in num_inteiros:
#     print(f'Nao encontrado!')

'''
9. Faça um programa que armazene 8 números em uma lista e imprima 
todos os números. Ao final, imprima o total de números múltiplos de seis. 
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 12]
total = 0
for i in numeros:
    if i % 6 == 0:
        print(i)
        total += 1
print(f'Total de numeros foram: {total}')

'''
10. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. 
Calcule e armazene a média. Armazene também a situação do aluno: 
1- Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma 
listagem contendo as notas, a média e a situação de cada aluno. 
Utilize quantas listas forem necessárias para armazenar os dados.
'''

# alunos = []
# for i in range(1, 3):
#     nome = input("Nome: ")
#     n1 = float(input("Nota 1: "))
#     n2 = float(input("Nota 2: "))

#     media = (n1 + n2) / 2

#     if media >= 7:
#         situacao = 'Aprovado'
#     elif media >= 5 and media < 7:
#         situacao = 'Recuperacao'
#     else:
#         situacao = 'Reprovado'
    
#     alunos.append([nome, [n1, n2], media, situacao])

# for aluno in alunos:
#     print("Nome: ", aluno[0])
#     print("Notas: ", aluno[1])
#     print("Media: ", aluno[2])
#     print("Situacao: ", aluno[3])


'''
11. Crie uma lista com os nomes dos super-heróis que devem participar da Iniciativa Vingadores seguindo a ordem: 
• Homem de Ferro 
• Capitão América 
• Thor 
• Hulk 
• Viúva Negra 
• Gavião Arqueiro
a. Agora, inclua o Homem-Aranha no final da lista e imprima em qual posição está o Thor.
b. Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte da Iniciativa Vingadores, então retire-os da lista.
'''
herois = ['• Homem de Ferro', 
'• Capitão América ',
'Thor',
'• Hulk ',
'Viúva Negra', 
'• Gavião Arqueiro']
herois.append('Homem-Aranha')
print(herois.index('Thor'))
herois.remove('Viúva Negra')
herois.pop(0)
print(herois)


'''
12. Crie um programa que leia 5 números inteiros e os armazene em uma lista de tal forma que 
todos os números maiores ou iguais que o primeiro fiquem ao lado direito e 
todos os menores fiquem ao lado esquerdo.
'''

lista_inteiros = []
primeiro = int(input("Pirmeiro numero: "))
lista_inteiros.append(primeiro)

for i in range(5):
    num = int(input("Num: "))
    if num >= primeiro:
        lista_inteiros.append(num)
    else:
        lista_inteiros.insert(0, num)
print(lista_inteiros)

'''
Dada uma tupla T de n valores inteiros, escreva um programa 
que remova todos os números pares da tupla.
'''
T = (1, 2, 3, 4, 5, 6, 7)
lista = list(T)
lista_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)


'''
Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na 
prova 1 e na prova 2, respectivamente, escreva um programa que calcule a média da turma nas 
provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média.
'''
P1 = (4, 5.3, 7.1, 8, 10, 9.2)
P2 = (2.4, 3.2, 1.7, 8.8, 0, 3.2)
media_p1 = sum(P1)/ len(P1)
print(media_p1)
media_p2 = sum(P2)/ len(P2)
print(media_p2)


'''
Dadas duas tuplas L1 e L2, com n e m valores inteiros, respectivamente, escreva um 
programa que concatene as tuplas L1 e L2 em uma nova tupla L3. Em seguida, imprima a tupla 
L3 ordenada de maneira crescente e decrescente.
'''
l1 = ('a', 'b', 'c', 'd', 'e', 'f')
l2 = ('g', 'h', 'i', 'j')
l3 = l1 + l2
print(sorted(l3))
print(sorted(l3, reverse=True))