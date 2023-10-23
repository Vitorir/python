# Ler dados do usuário
print("Digite os dados do usuário:")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("Idade: ")
email = input("Email: ")

print("\nDados do usuário:")
print(f"1. Nome: {nome}")
print(f"2. Sobrenome: {sobrenome}")
print(f"3. Idade: {idade}")
print(f"4. Email: {email}")

# Calcular informações do aluno
print("\nDigite as notas do aluno:")
notas = []
for i in range(4):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

situacao = "Aprovado" if media >= 6 else "Reprovado"

info_aluno = {
    'Nome do aluno': nome + " " + sobrenome,
    'Notas obtidas': notas,
    'Maior nota': maior_nota,
    'Menor nota': menor_nota,
    'Média': media,
    'Situação': situacao
}

print("\nInformações do aluno:")
for key, value in info_aluno.items():
    print(f"{key}: {value}")

# Lista de alunos
alunos = []
numero_alunos = int(input("\nDigite o número de alunos: "))
for _ in range(numero_alunos):
    nome_aluno = input("Nome do aluno: ")
    notas_aluno = []
    for i in range(4):
        nota = float(input(f"Nota {i + 1} para {nome_aluno}: "))
        notas_aluno.append(nota)

    maior_nota_aluno = max(notas_aluno)
    menor_nota_aluno = min(notas_aluno)
    media_aluno = sum(notas_aluno) / len(notas_aluno)

    situacao_aluno = "Aprovado" if media_aluno >= 6 else "Reprovado"

    info_aluno = {
        'Nome do aluno': nome_aluno,
        'Notas obtidas': notas_aluno,
        'Maior nota': maior_nota_aluno,
        'Menor nota': menor_nota_aluno,
        'Média': media_aluno,
        'Situação': situacao_aluno
    }

    alunos.append((media_aluno, info_aluno))

# Imprimir alunos aprovados em ordem decrescente de média
alunos_aprovados = [aluno for aluno in alunos if aluno[0] >= 6]
alunos_aprovados.sort(reverse=True)

print("\nAlunos Aprovados:")
for aluno in alunos_aprovados:
    print(f"Nome: {aluno[1]['Nome do aluno']}, Média: {aluno[0]}")
