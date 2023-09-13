# ■ Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos.
dicio = {}

# nome = input("Digite o nome")
# dicio['nome'] = nome
# sobrenome = input("Sobrenome")
# dicio['sobrenome'] = sobrenome
# idade = input("Idade")
# dicio['idade'] = idade
# email = input("Email")
# dicio['email'] = email


# ■ Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
# Lendo as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Armazenando as informações em um dicionário
aluno = {
    "Nome": "",
    "Notas": [nota1, nota2, nota3, nota4],
    "Maior Nota": max(nota1, nota2, nota3, nota4),
    "Menor Nota": min(nota1, nota2, nota3, nota4),
    "Média": media,
    "Situação": ""
}

# Verificando a situação do aluno
if media >= 7:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

# Imprimindo as informações do aluno
print("Informações do aluno:")
print("Nome: ", aluno["Nome"])
print("Notas: ", aluno["Notas"])
print("Maior Nota: ", aluno["Maior Nota"])
print("Menor Nota: ", aluno["Menor Nota"])
print("Média: ", aluno["Média"])
print("Situação: ", aluno["Situação"])