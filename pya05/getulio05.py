'''
1°: Escreva uma função lambda que receba um número e verifique se ele é par
ou ímpar. A função deve retornar "par" se o número for par e "ímpar"
caso contrário
'''
par_ou_impar = lambda x : "par" if x % 2 == 0 else "impar"
print(par_ou_impar(3))

'''
2°: Implemente uma função lambda que receba duas strings e retorne a 
concatenação das duas, apenas se ambas as strings tiverem mais de 5
caracteres. Caso contrário, a função deve retornar uma mensagem de erro
'''
concatenar = lambda x, y : x + y if len(x) >= 5 and len(y) >= 5 else "Erro. Invalido"
print(concatenar("Vitor", "Ipiranga"))

'''
4°: A partir de uma lista de strings, utilize map() e uma função lambda
para converter todas as letras em maiúsculas
'''
lista = ['one', 'two', 'three', 'four', 'five', 'six']

converter = lambda lista : list(map(lambda x : x.upper(), lista))
print(converter(lista))