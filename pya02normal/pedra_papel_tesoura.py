import random
opcoes = ["pedra", 'papel', 'tesoura']

computador = random.choice(opcoes)
jogador = input("Escolha pedra, papel ou tesoura: ").lower()
print(computador)

if jogador == computador:
    print("Empate!")
elif jogador == 'pedra' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'papel' or jogador == 'pedra' and computador == 'papel':
    print("Ganhou!")
else:
    print("Perdeu!")