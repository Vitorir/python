count = 1
torcedores_fortaleza = 0
torcedores_ceara = 0
torcedores_ferroviario = 0
torcedores_icasa = 0

salario_fortaleza = 0
caucaia_ferroviario = 0
fortaleza_ceara = 0

while count <= 3:
    clube = input("""Digite seu time: 
1-Fortaleza; 
2-Ceará; 
3-Ferroviário; 
4-Icasa; 
5-Outros 
""")
    
    moradia = input("""Digite bairro: 
                   
1-Fortaleza; 
2-Caucaia; 
3-Outros
""")

    salario = float(input("Digite seu salario: "))

    if clube == '1':
        torcedores_fortaleza += 1
        salario_fortaleza += salario
    elif clube == '2':
        torcedores_ceara += 1
        if moradia == '1':
            fortaleza_ceara += 1
    elif clube == '3':
        torcedores_ferroviario += 1
        if moradia == '2':
            caucaia_ferroviario += 1
    elif clube == '4':
        torcedores_icasa += 1
    count+=1

media_salarial = salario_fortaleza / torcedores_fortaleza
print(f"Numero de torcedores fortalza: {torcedores_fortaleza}")
print(f"Média salarial de torcedores fortalza: {media_salarial}")
print(f"Moradores de caucaia torcedores do ferroviario {caucaia_ferroviario}")
print(f"Numero de pessoas de Fortaleza torcedores do Ceara: {fortaleza_ceara}")
