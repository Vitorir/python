# Método para construir uma coleção de objetos
# lista_pessoa = []
# for i in range(5):
#     nome = input("Digite nome: ")
#     sobrenome = input("Digite nome: ")
#     idade = int(input("Digite idade: "))


#     dicionario_pessoa = {
#         'nome': nome,
#         'sobrenome': sobrenome,
#         'idade': idade
#     }
#     lista_pessoa.append(dicionario_pessoa)

# for i in lista_pessoa:
    # print(i)

def gerar_pessoa(nome, sobrenome, idade):
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade
    }

