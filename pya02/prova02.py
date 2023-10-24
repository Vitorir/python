qtd_valores = int(input('Digite a quantidade de valores: '))

numeros_pares = []
numeros_impares = []

for i in range(qtd_valores):
    valor = float(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

cont_pares = len(numeros_pares)
cont_impares = len(numeros_impares)

soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)


print(f'\nSão {cont_pares} números pares \nOs Números pares são: {tuple(numeros_pares)} \nA soma deles é: {soma_pares}\n'
      f'\nSão {cont_impares} números pares \nOs Números pares são: {numeros_impares}, \nA soma deles é: {soma_impares}')