# 1°: Escreva uma função lambda que receba um número e verifique se
# ele é par ou ímpar. A função deve retornar "par" se o número
# for par e "ímpar" caso contrário
x = int(input("Digite um numero: "))
par_ou_impar = lambda num : "par" if num % 2 == 0 else "impar"
print(par_ou_impar(x))

# 2°: Implemente uma função lambda que receba duas strings e retorne
#  a concatenação das duas, apenas se ambas as strings tiverem mais
#  de 5 caracteres. Caso contrário, a função deve retornar uma mensagem de erro
# s1 = input("Digite um texto: ")
# s2 = input("Digite um texto: ")

# concatenar = lambda s1, s2 : s1 + s2 if len(s1) > 5 and len(s2) > 5 else "Erro"
# print(concatenar(s1, s2))

# 3°: Implemente uma função lambda que receba um número e verifique
#  se ele é divisível por 3 e por 5. A função deve retornar "divisível" se a condição for 
# satisfeita e "não divisível" caso contrário
# num = int(input("Digite um numero: "))
# verificar_divisibilidade = lambda x : "divisível" if num % 3 == 0 and num % 5 == 0 else "não indivisível"
# print(verificar_divisibilidade(num))

# 4°: A partir de uma lista de strings, utilize map() e uma função
#  lambda para converter todas as letras em maiúsculas
lista = ['a', 'b', 'c', 'd']
maiusculas = list(map(lambda x : x.upper(), lista))
print(maiusculas)


# 5°: A partir de uma lista de palavras, utilize filter() e uma função
#  lambda para filtrar apenas as palavras que possuem mais de 5 letras
# palavras = ['Brasil', 'Uganda', 'Serra-Leoa', 'UK', 'Gana', 'Chile']
# filtradas = list(filter(lambda x : len(x) > 5), palavras)

# 6°: Dada uma lista de valores numéricos, utilize reduce() e uma
# função lambda para obter o valor máximo da lista
# from functools import reduce
# lista = [100, -4, 0, 30, 5]
# valor_max = reduce(lambda x, y : x + y, lista)

# 7°: A partir de uma lista de dicionários, cada um representando uma
#  pessoa com os campos "nome" e "idade", utilize map() e uma função
#  lambda para obter uma nova lista contendo apenas os nomes das pessoas
lista = [{'nome': 'fulano', 'idade': 15},
        {'nome': 'sicrano', 'idade': 20},
          {'nome': 'beltrano', 'idade': 25}]

nova_lista = list(map(lambda dic : dic['nome'], lista))
print(nova_lista)