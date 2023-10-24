# 1°: Faça uma função que recebe por parâmetro o tempo de duração de uma
# fábrica expressa em segundos e retorna também por parâmetro esse tempo em 
# horas, minutos e segundos
def converter_tempo(seg): # 10000
    hora = seg // 3600 # 2
    segs_restantes = seg % 3600 # 2800
    minutos = segs_restantes // 60 # 46
    segs_finais = segs_restantes % 60 # 40

    return hora, minutos, segs_finais

print(converter_tempo(10000))

# 2°: Faça uma função que recebe a idade de uma pessoa em anos,
#  meses e dias e retorna essa idade expressa em dias
def converte_idade(anos, meses, dias):
    total_dias = (anos * 365) + (meses * 30) + dias
    return total_dias

print(converte_idade(10, 7, 150))

# 3°: Faça uma função que recebe um valor inteiro e verifica se o valor
#  é positivo ou negativo. Se positivo verificar se é par ou impar
def verificar(valor):
    if valor > 0:
        if valor % 2 == 0:
            return f"Valor é positivo e par"
        else:
            return f"Valor é positivo e impar"
    else:
        return f"Valor negativo"

print(verificar(10))

# 4°: Faça uma função que recebe por parâmetro o raio de uma esfera e 
# calcula o seu volume (v = 4 / 3 * Pi * R³)
def calcula_volume(raio):
    return (4/3) * 3.14 * raio ** 3

print(calcula_volume(5))

# 5°: Faça uma função que receba um valor inteiro e positivo e calcula
# o seu fatorial
def fatorial(valor):
    fat = 1
    if valor == 0:
        return 1
    else:
        for i in range(1, valor + 1):
            fat = fat * i
    return fat

print(fatorial(5))

# Com recursão
def fatorial_recursivo(valor):
    if valor == 0:
        return 1
    else:
        return valor * fatorial_recursivo(valor - 1)
    
numero = int(input("Digite numero: "))
if numero < 0:
    print("Número inválido!")
else:
    print(f"O fatorial de {numero} é {fatorial_recursivo(numero)}")

# 6°: Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S:
def retorna_S(N):
    S = 0
    for i in range(1, N):
        S += 1/i

    return S

N = 5
print(f"O valor de S para N = {N:.2f} é {retorna_S(N):.2f}")