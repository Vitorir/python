while True:
    nome = input("Nome: ")
    while len(nome) < 3:
        print('nome invalido!')
        nome = input("Nome: ")

    idade = int(input("Idade: "))
    while idade < 0 or idade > 150:
        idade = int(input("Idade: "))

    sexo = input("Sexo: ")
    while sexo.lower() not in ['f', 'm']:
        sexo = input("Sexo: ")

    estado_civil = input("Estado Civil: ")
    while estado_civil.lower() not in ['s', 'c', 'v', 'd']:
        estado_civil = input("EstadoCivil: ")
    
    break