# 1. Faça um programa para imprimir os números de 1 a 10. Utilize a função
# range() para criar a coleção de números.
# for i in range(1, 10):
    # print(i)


# 2. Faça um programa para imprimir os números pares de 1 a 20. Utilize a
# função range() para criar a coleção de números.
# for i in range(1, 21):
    # if i % 2 == 0:
        # print(i)

# 3. Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a
# função range() para criar a coleção de números.
# for i in range(1, 20):
    # if i % 2 != 0:
        # print(i)


# 4. Faça um programa para calcular a soma dos números de 1 a 100. Utilize a
# função range() para criar a coleção de números.
# soma = 0
# for i in range(1, 100):
    # soma += i
# print(soma)

# 5. Faça um programa para calcular a média de uma lista de números.
# lista = [1, 2, 3]
# soma = 0
# for i in lista:
#     soma += i

# media = soma / len(lista)
# print(media)

# Faça um programa para verificar se um número é primo. Utilize a
# condicional IF dentro do laço FOR.
'''numero = int(input("Digite um numero: "))
contador = 0
for i in range(2, numero):
    if numero % i == 0:
        contador += 1

if contador == 0:
    print("Numero é primo")
else:
    print("Numero não é primo")
'''
# 7. Faça um programa para Imprimir os caracteres de uma string
# separadamente.
#for i in 'string':
#    print(i, end=" ")

# 8. Faça um programa para contar quantas vogais existem em uma palavra.
# Utilize a condicional IF dentro do laço FOR.
'''vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input("Digite uma palavra: "))
count = 0
for i in palavra:
    if i in vogais:
        count += 1
print(f"Existem {count} vogais no código")
'''
# 9. Faça um programa para contar quantas consoantes existem em uma
# palavra. Utilize a condicional IF dentro do laço FOR.
'''cont_vogais = 0
cont_consoantes = 0
count_simbolo = 0
palavra = str(input("Digite uma palavra: "))

for i in palavra:
    if i in 'aeiou':
        cont_vogais += 1
    elif i in ',.!? ':
        count_simbolo += 1
    else:
        cont_consoantes += 1
print(f"Existem {cont_vogais} vogais, {count_simbolo} simbolos e {cont_consoantes} ocnsoantes")
'''
# 10. Faça um programa para verificar se uma palavra é um palíndromo.
# Exemplo: ‘amor’ = ‘roma’ (NÃO É) / ‘arara’ = ‘arara’ (É PALÍNDROMO).
'''palavra = str(input("Digite uma palavra: "))
invertida = palavra[::-1]

if palavra == invertida:
    print('é palíndromo')
else:
    print("Não é palindromo")
'''