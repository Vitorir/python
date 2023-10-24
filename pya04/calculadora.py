def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 - n2


while True:
    print("Opções: ")
    print('1 - Somar')
    print('2 - subtrair')
    print('3 - dividir')
    print('4 - multiplicar')
    print("5 - Sair")
    opcao = input("Digite uma opcao")
   

    print("digite os dois numeros: ")
    n1 = float(input("Digite um numero"))
    n2 = float(input("Digite outro numero"))

    match opcao:
        case '1':
            print(somar(n1, n2))

        case  '2':
            subtrair(n1, n2)
        case '3':
            dividir(n1, n2)
        case '4':
            multiplicar(n1, n2)
        case '5':
            break