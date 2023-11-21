'''
01. Faça um programa que leia três números e, para cada um, imprimir o dobro. O    cálculo deverá ser realizado por uma função e o resultado impresso ao final do  programa. 
'''
def retorna_dobro(numeros):
    quadrados = []
    for i in numeros:
        quadrados.append(i**2)
    
    return quadrados

'''
02. Faça um programa que receba as notas de três provas e calcule a média. Para o cálculo, escreva uma função. O programa deve imprimir a média ao final.
'''
def calcular_media(notas):
    return sum(notas) / len(notas)

'''
03. Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um programa que permita entrar com o valor de um produto e o percentual de desconto e imprimir o novo valor com base no percentual informado. Para fazer o cálculo, implemente uma função.
'''
def aplica_desconto(valor, desconto):
    desconto = valor * (desconto / 100)
    novo_valor = valor - desconto
    return novo_valor

print(aplica_desconto(100, 0.3))

'''
04. Faça um programa que leia o saldo e o % de reajuste de uma aplicação financeira e imprimir o novo saldo após o reajuste. O cálculo deve ser feito por uma função.
'''
def calcula_reajuste(saldo, percentual):
    reajuste = saldo * (percentual / 100)
    novo_saldo = saldo + reajuste
    return novo_saldo 


'''
05. Faça um programa que verifique quantas vezes um número é divisível por outro. A função deve receber dois parâmetros, o dividendo e o divisor. Ao ler o divisor, é importante verificar se ele é menor que o dividendo. Ao final imprima o resultado.
'''
def verifica_vezes(dividendo, divisor):
    if divisor >= dividendo:
        return "O divisor deve ser menor que o dividendo"
    
    contador = 0
    while dividendo % divisor == 0:
        dividendo = dividendo / divisor
        contador += 1


'''
06. Faça um programa que verifique se um número é primo por meio de um função.
Ao final imprima o resultado. 
'''
def verifica_primo(numero):
    primo = None
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    
    if contador == 2:
        primo = True
    else:
        primo = False

    return primo
    
print(verifica_primo(7))

'''
7. Faça um programa que leia a base e a altura de um retângulo e imprima o perí-
metro, a área e a diagonal. Para fazer os cálculos, implemente três funções, cada
uma deve realizar um cálculo especifico conforme solicitado. Utilize as fórmulas
a seguir.
'''
import math
def calcular_perimetro(base, altura):
    return 2 * (base + altura)

def calcular_area(base, altura):
    return base * altura

def calcular_diagonal(base, altura):
    return math.sqrt(base**2 + altura**2)

'''
9. Faça um programa que leia o saldo e o % de reajuste de uma aplicação financeira e imprimir o novo saldo após o reajuste. O cálculo deve ser feito por uma função.
'''
def calcular_novo_saldo(saldo, percentual_reajuste):
    reajuste = saldo * (percentual_reajuste / 100)
    novo_saldo = saldo + reajuste
    return novo_saldo

'''
10. Faça um programa que leia uma lisa com tamanho 10 de números inteiros. Após
ler, uma função deve criar uma nova lista com base na primeira, mas, a nova
lista deve ser ordenada de forma crescente. O programa deve imprimir esta nova
lista após a ordenação
'''
inteiros = []
for i in range(10):
    numero = int(input("Numero: "))
    inteiros.append(numero)
    
def ordenar(lista):
    lista2 = lista.copy()
    return sorted(lista2)


print(ordenar(inteiros))

'''
11. Implemente um programa que leia uma mensagem e um caractere. Após a leitura, o programa deve, por meio de função, retirar todas as ocorrências do caractere informado na mensagem colocando * em seu lugar. A função deve também retornar o total de caracteres retirados. Ao final, o programa deve imprimir a frase ajustada e a quantidade de caracteres substituídos.
'''
msg = input("Mensagem: ")
char = input("Caractere: ")
def substituir(msg, char):
    nova_msg = ""
    contador = 0
    for i in msg:
        if i == char:
            nova_msg += "*"
            contador += 1
        else:
            nova_msg += i
    return nova_msg, contador

msg_ajust, total = substituir(msg, char)
print("Mensagem ajustada:", msg_ajust)
print("Total de char substituidos:", total)


'''
12. Faça um programa que leia 20 de números inteiros e armazene em uma lista.
Após essa leitura, o programa deve ler um novo número inteiro para ser buscado
na lista. Uma função deve verificar se o número lido por último está na lista e
retornar a posição do número na lista, caso esteja, ou -1, caso não esteja.
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inteiro = int(input("Inteiro: "))
def verificar_numero(lista, numero):
    if numero in lista:
        return lista.index(numero)
    else:
        return f'Não existe numero na lista!'
    
print(verificar_numero(lista, inteiro))