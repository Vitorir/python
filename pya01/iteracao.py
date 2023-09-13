cont = 0
n = int(input('Insira um número para saber se ele é primo: '))

for c in range(1, n + 1):
    if n % c == 0: cont += 1

if cont >= 3: print('O número escolhido não é primo!')
else: print('O número escolhido é primo!')