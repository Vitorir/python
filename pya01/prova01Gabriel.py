R = int(input("Quantos alunos serão cadastrados? "))

lista_alunos = []


for i in range(R):

    idade = int(input('Digite a idade: '))

    lista_alunos.append(idade)


c = 0

s = 0

while True:
    if c <= len(lista_alunos)-1:
        s = s + int(lista_alunos[c])
        c += 1
        continue
    else:
        break


med = s / R


print(f'A média de idade é {med}')
