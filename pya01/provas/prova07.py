lista_notas = []


def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

while True:
        nota = float(input("Digite o valor da nota:  ou '-1' para parar"))

        if nota == -1:
            break

        if 0 <= nota <= 10:
            lista_notas.append(nota)
        else:
            print('Nota invalida')


for i, nota in enumerate(lista_notas, start=1):
    print(f"Aluno {i} teve nota: {nota:.2f}")

media = calcular_media(lista_notas)
print(f"Média da turma: {media:.2f}")