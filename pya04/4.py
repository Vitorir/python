i = 0
soma = 0
aprovados = 0
reprovados = 0

while i < 5:
    nota = float(input("Digite nota: "))
    
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

    soma += nota
    i += 1

print(aprovados)
print(soma / 5)
print((reprovados / 5) * 100)

'''
'''
t_fortaleza = 0
t_ceara = 0
t_icasa = 0
salario_fortaleza = 0

ceara_fortaleza = 0

contador = 0
while contador <= 50:
    time = int(input(""))
    moradia = int(input(""))
    salario = float(input(""))

    if time == 1:
        t_fortaleza += 1
        salario_fortaleza += salario
    elif time == 2:
        t_ceara += 1

        if moradia == 1:
            ceara_fortaleza += 1
    