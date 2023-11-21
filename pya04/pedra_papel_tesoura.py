import random

empates = 0
vitorias = 0
derrotas = 0

def gerar_escolha_usuario():
    jogador = int(input("1 - Pedra; 2 - Papel; 3 - Tesoura"))
    return jogador

def gerar_escolha_computador():
    maquina = random.choice(['pedra', 'papel', 'tesoura'])
    return maquina

def checar_vitorioso(jogador, maquina):
    if jogador == maquina:
        print('empate')
        empates+=1
    elif jogador == 'pedra' and maquina == 'tesoura' or jogador == 'papel' and maquina == 'pedra' or jogador == 'tesoura' and maquina == 'papel':
        print('vitoria')
        vitorias+=1
    else:
        print('derrota')

jogador = gerar_escolha_usuario()
maquina = gerar_escolha_computador()
checar_vitorioso(jogador, maquina)