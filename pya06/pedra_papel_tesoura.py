from random import *

# Criar um placar que vai contabilizar a quantidade de vezes 
# que o usuario e o computador ganhou
pontos_usuario = 0
pontos_computador = 0 
empates = 0

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
    global pontos_usuario, pontos_computador, empates
    
    if escolha_computador == escolha_usuario:
        empates += 1
        return 'Empate'
    elif escolha_computador == 'pedra' and escolha_usuario == 'tesoura' or escolha_computador == 'tesoura' and escolha_usuario == 'papel' or escolha_computador == 'papel' and escolha_usuario == 'pedra':
        pontos_usuario += 1
        return 'Vitória'

    else:
        pontos_computador += 1
        return 'Derrota'

def jogar():
    pc = gerar_escolha()
    chute = gerar_escolha_usuario()

    print(f"Escolha do usuario: {chute} | Escolha do computador: {pc}")
    print(checar_vitorioso(chute, pc))



def checar_placar():
    global pontos_usuario, pontos_computador
    print('Placar')
    print('=======================================')
    print('Usuario : ', pontos_usuario, " vs ", 'Computador: ', pontos_computador, "Empates: ", empates)

def checar_campeao(pontos_usuario, pontos_computador):
    if pontos_usuario > pontos_computador:
        return "Você é o Campeão"
    elif pontos_computador == pontos_usuario:
        return "Deu empate"
    else:
        return "Vocé perdeu"
    


def menu():
    while True:
        opcao = int(input("""
            Digite a opção: 
                          1 - Jogar
                          2 - Ver Placar
                          3 - Sair
"""))

        match opcao:
            case 1:
                jogar()
            case 2:
                checar_placar()  
            case 3:
                break  
            case _:
                print('Opção inválida! Tente novamente.')


menu()
