n = int(input("Digite um numero natural: "))
count = 1
soma = 1
while count <= n:
    if n == 0:
        print(f"Fatorial de {n} é 1!")
    else:
        soma *= count
        count += 1
print(soma)