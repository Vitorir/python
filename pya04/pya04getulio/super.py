# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# lista_imcs = []
# for i in range(2):
#     nome = input("Digite o nome")
#     peso = float(input("Peso"))
#     altura = float(input("Altura"))

#     imc = calcular_imc(peso, altura)
#     pessoa = {
#         'nome': nome,
#         'imc': imc
#     }

#     lista_imcs.append(pessoa)

# for i in lista_imcs:
#     print(i['nome'])
#     print(i['imc'])

def conta_letras(string):
    conta_letra = 0
    conta_espaco = 0
    conta_sinais = 0
    if " " in string:
        for i in string:
            if i in " ":
                conta_espaco += 1
            elif i in "!@#$%¨&*()":
                conta_sinais += 1
            else:
                conta_letra += 1
        return f"{conta_letra}, {conta_espaco} e {conta_sinais} e tem {len(string)}"
    else:
        return len(string)
    
print(conta_letras("Alo"))

def calcular_hora(salario, horas):
    valor_hora = salario / horas