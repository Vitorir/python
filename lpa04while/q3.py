populacaoA = 80000
taxa_crescimentoA = 0.03

populacaoB = 200000
taxa_crescimentoB = 0.015

anos = 0

while populacaoA < populacaoB:
    populacaoA *= 1 + taxa_crescimentoA
    populacaoB *= 1 + taxa_crescimentoB
    anos += 1

print(f"Após {anos} anos, a população A, {int(populacaoA)}, igualou ou ultrapassou a população B, {int(populacaoB)}.")
