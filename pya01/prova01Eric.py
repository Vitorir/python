soma_idades = 0

quantidade_alunos = int(input('Quantos alunos tem na turma?'))

for i in range(1, quantidade_alunos + 1):
    idade_aluno = int(input(f'Digite a idade do aluno {i}: '))

contador = 0
while contador < 1:
    soma_idades += idade_aluno
contador += 1

media_idade = soma_idades / quantidade_alunos

print(f'\nTotal de alunos na turma: {quantidade_alunos}'
      f'\nSoma das idades: {soma_idades}'
      f'\nMédia das idades: {media_idade}')
