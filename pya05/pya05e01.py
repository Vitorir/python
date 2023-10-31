import time

def inverter_texto(string:str):
    return string[::-1]
    

def inverte_texto(string:str):
    invertida = ""
    for i in string:
        invertida = i + invertida

    return invertida

def invert_text(string):
    invertida = ''.join(reversed(string))
    return invertida

def retorna_maior(a,b):
    return max(a,b)

def enigmatica(a,b):
    if a > b: return a
    if b > a: return b

def retorna_palavra(lista):
    maior = 0
    for palavra in lista:
        comprimento = len(palavra)
        if comprimento > maior: maior = comprimento

    return maior

def imprime_cores(cores):
    for cor in cores:
        print(cor, flush=True)
        time.sleep(1)
        print('\033[0m', end='', flush=True)

cores = ['\033[44m]', 'azul', '\033[42m]', 'verde', '\033[43m']
print(imprime_cores(cores))

par_ou_impar = lambda x: "par" if x % 2 == 0 else "impar"

concatenar_strings = lambda str1, str2: str1 + str2 if len(str1) > 5 and len(str2) > 5 else "Erro: As duas strings devem ter mais de 5 caracteres."

verificar_maior_10 = lambda numero: numero if numero > 10 else numero / 2

verificar_divisivel_3_5 = lambda numero: "divisível" if numero % 3 == 0 and numero % 5 == 0 else "não divisível"

print(inverter_texto("Vitor"))
print(inverte_texto("Vitor"))
print(invert_text("Vitor"))
print(retorna_palavra(['hello', 'world', 'como vai voce']))