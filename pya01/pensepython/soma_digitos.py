numero = int(input("Digite um numero inteiro: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f"""
centena: {centena}
dezena: {dezena}
unidade: {unidade}
""")