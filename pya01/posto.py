litros = float(input('Qtd de litros\n'))
combustivel = (input('Qual combustivel: A - Alcool, G - Gasolina\n'))
preco_gasolina = 2.5
preco_alcool = 1.9

if combustivel == 'A':
    if litros <= 20:
        total = litros * preco_alcool * 0.97
    else:
        total = litros * preco_alcool * 0.95
elif combustivel == 'G':
    if litros <= 20:
        total = litros * preco_gasolina * 0.96
    else:
        total = litros * preco_gasolina * 0.94
else:
    print("Tipo de combustível inválido")

print(f'Valor total: R$ {total:.2f}')