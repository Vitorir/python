from random import *

def gerar_lista_inteiros(n1):
    lista = []
    for i in range(n1):
        item = randint(1, 100)
        lista.append(item)
    return lista

print(gerar_lista_inteiros(10))