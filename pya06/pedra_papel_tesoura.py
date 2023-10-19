from random import *
def gerar_escolha():
    escolhas = ['pedra', 'papel', 'tesoura']
    computador = choice(escolhas)
    return computador


def gerar_escolha_usuario():
    escolha_usuario = input("""
            Digite a opcção: 
            pedra
            papel
            tesoura
""")
    return escolha_usuario


def checar_vitorioso(escolha_usuario, escolha_computador):
    if escolha_computador == escolha_usuario:
        return 'Empate'
    elif escolha_computador == 'pedra' and escolha_usuario == 'tesoura' or escolha_computador == 'tesoura' and escolha_usuario == 'papel' or escolha_computador == 'papel' and escolha_usuario == 'pedra':
        return 'Vitória'    
    else:
        return 'Derrota'
    
escolha_computador = gerar_escolha()
chute = gerar_escolha_usuario()

print(escolha_computador)
print(checar_vitorioso(escolha_computador, chute))