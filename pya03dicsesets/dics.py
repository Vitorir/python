# Construção de dicionário
dicionario = dict([('Modulo', 'Python'), ('Instituicao', 'Infinity')])
print(dicionario)

dicionario2 = dict(Modulo = 'Logica', Instituicao = 'Infinity', Codigo = 'DFS')
print(dicionario2)

# Métodos de dicionário
print(list(dicionario))
print(len(dicionario))
print(dicionario.items())
dicionario['Alunos'] = 25
print(dicionario)