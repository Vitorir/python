# while True:
#     genero = input("digite sexo")
#     if genero == "F" or genero == "M":
#         break
#     else:
#         print("Escreva o genero de novo")

# maior numero
# maior = 0
# count = 0
# while count < 4:
#     num = float(input("Digite um numero "))
#     if num > maior:
#         maior = num

#     count+= 1
# print(maior)

'''
■Desenvolva um programa que leia
seis números inteiros e mostre a
soma apenas daqueles que forem
pares. Se o valor digitado for ímpar,
desconsidere-o.
'''

# soma = 0
# for i in range(7):
#     num = float(input("numero: "))
#     if num % 2 == 0:
#         soma += num

'''
■ Desenvolva um programa que leia o
nome, idade e sexo de 3 pessoas.
No final do programa, exiba:
-a média de idade de todo o grupo.
-Qual o nome da pessoa mais velha.
-quantas pessoas têm menos de 20
anos.
'''

# soma = 0
# vinte = 0
# maior = 0
# idade_mais_velha = 0
# nome_mais_velha = ""

# for i in range(3):
#     nome = input('nome')
#     idade = int(input('idade'))
#     sexo = input('sexo')
    
#     if idade > idade_mais_velha:
#         idade_mais_velha = idade
#         nome_mais_velha = nome    

#     soma += idade
#     if idade < 20:
#         vinte+= 1;

# media = soma / 3

# print(f"A média de idade do grupo é: {media}",
#       f"A pessoa mais velha é {nome_mais_velha} com {idade_mais_velha}",
#       f"{vinte} pessoas tem menos de 20 anos"
#       )


'''
■ Crie um programa que leia dois valores e mostre
um menu para calcular.
1 - Somar
2 - Multiplicar
3 - Dividir
4 - Subtrair
5 - Sair do programa
'''

# for i in range(2):
#     valor = float(input('valor: '))
#     valor2 = float(input('valor2: '))
#     print("1 - somar")
#     print("2 - multiplicar")
#     print("3 - dividir")
#     print("4 - subtrair")
#     print("5 - sair do programa")

#     opcao = input("escolha uma opcao: ")

#     if opcao == '5':  # Corrigido para comparar com '5'
#         break

#     if opcao not in ["1", "2", "3", "4"]:
#         print("Opção invalida")
#     else:
#         if opcao == '1':
#             print(valor + valor2)
#         elif opcao == '2':
#             print(valor * valor2)
#         elif opcao == '3':
#             print(valor / valor2)
#         elif opcao == '4':
#             print(valor - valor2)

        
'''
'''