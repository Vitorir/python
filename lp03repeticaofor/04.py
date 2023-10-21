qtd_aprovados = 0
soma = 0
count = 1
while count <= 3:
    nota = float(input("Digite a nota: "))
    if nota >= 7:
        qtd_aprovados += 1
    soma += nota
    count += 1

media = soma / 3
percentual_reprovados = ((3 - qtd_aprovados) / 3) * 100
print(qtd_aprovados, media, percentual_reprovados)