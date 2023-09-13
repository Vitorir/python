qtd_alunos = int(input("Digite a qtd de alunos: "))
soma = 0

for i in range(qtd_alunos):
    idade = int(input(f"Digite a idade do {i + 1}º aluno: "))
    soma += idade

media = soma / qtd_alunos

print(
    f"Soma das idades: {soma}",
    f"\nMedia das idades: {media}",
)
