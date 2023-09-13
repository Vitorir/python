'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
'''
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota >= 0 and nota <=10:
        break
    else:
        print("Valor invalido!")

print("Nota válida: ", nota)

'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
'''

# Definir variáveis
usuario = 'vitor'
senha = '123'

while True:
    user = input("Digite um nome de usuario: ")
    password = input("Digite uma senha: ")
    # Condição de Parada
    if user != password:
        break
    else:
        print("Erro! A senha não pode ser igual a usuário")
