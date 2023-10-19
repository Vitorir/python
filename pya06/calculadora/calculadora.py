from operacoes.operadores import soma, subtrair, multiplicar, dividir
def menu():
    while True:
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite um numero: "))
        
        opcao = int(input("""
            Digite uma opcao
                      1- somar
                      2- subtrair
                      3- multiplicar
                      4 - dividir
                      5 - sair
"""))
        
        match opcao:
            case 1:
                print(soma(n1, n2))
            case 2:
                print(subtrair(n1, n2))
            case 3:
                print(multiplicar(n1, n2))
            case 4:
                print(dividir(n1, n2))
            case 5:
                break
            case _:
                print("Invalido!")

if __name__ == '__main__':
    menu()