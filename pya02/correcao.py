soma = 0
while True:
    nota = float(input("Digite nota: "))
    
    if nota <= 0:
        print("Digite um número maior que zero!")
    else:
        soma += nota
        
    while n1 > 0 and n2 > 0 and n3 > 0 and n4 > 0 and n5 > 0:
        soma = n1+n2+n3+n4+n5
        media = soma/5
        print(f"A soma dos números inseridos é: {soma} ")
        print(f"E a media dos números é: {media}")
        break
    break