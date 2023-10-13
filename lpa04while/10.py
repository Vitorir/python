numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Certifique-se de que o primeiro número seja menor que o segundo número
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Números inteiros no intervalo entre {numero1} e {numero2} são:")
while numero1 <= numero2:
    print(numero1)
    numero1 += 1