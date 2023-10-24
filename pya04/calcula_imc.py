def calcular_imc(peso, altura):
    return peso / (altura ** 2)
    

pessoas = []

for i in range(2):
    peso = float(input("Digite peso: "))
    altura = float(input("Digite altura: "))

    pessoa_imc = calcular_imc(peso, altura)
    print(f"IMC calculado {pessoa_imc:.2f}")

    pessoa = {
        "altura": altura,
        "peso": peso,
        "imc": pessoa_imc
    }
    
    pessoas.append(pessoa)

for i, pessoa in enumerate(pessoas):
    print(f"Pessoa de numero {i + 1}")
    print(f"{pessoa['altura']}")
    print(f"{pessoa['peso']}")
    print(f"{pessoa['imc']}")
