texto = input("Digite um texto: ")

def conta_caracteres(texto):
    espaco = 0
    pontuacao = 0
    
    for i in texto:
        if i in '.,!?':
            pontuacao += 1
        elif i == ' ':
            espaco += 1

    letras = len(texto) - (espaco + pontuacao)
            
    return letras, espaco, pontuacao


letras, espaco, pontuacao = conta_caracteres(texto)
print(f"a quantidade de letras é: {letras}, espaco {espaco}, pontuacao {pontuacao}")