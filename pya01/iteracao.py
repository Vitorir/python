# Primo
'''
cont = 0
n = int(input('Insira um número para saber se ele é primo: '))

for c in range(1, n + 1):
    if n % c == 0: cont += 1

if cont >= 3: print('O número escolhido não é primo!')
else: print('O número escolhido é primo!')
'''

# Fatorial
'''
n = int(input("Digite um numero natural: "))
count = 1
soma = 1
while count <= n:
    if n == 0:
        print(f"Fatorial de {n} é 1!")
    else:
        soma *= count
        count += 1
print(f"Fatorial de {n} é {soma}")
'''
# Impares
'''
n = int(input("Digite a qtd de numeros: "))
count = 0
while count < 5:
    numero_impar = 2 * count + 1
    print(numero_impar)
    count += 1

'''
# Soma das cadeias
numero = int(input("Digite um numero inteiro: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f"""
centena: {centena}
dezena: {dezena}
unidade: {unidade}
""")