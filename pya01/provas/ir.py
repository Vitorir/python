'''
"Escreva um programa em Python que solicite ao usuário sua renda anual e, em seguida, calcule o imposto de renda de acordo com as seguintes faixas de renda e alíquotas (para o ano de 2021):

Até R$ 22.847,76: isento de imposto.
De R$ 22.847,77 a R$ 33.919,80: alíquota de 7,5%.
De R$ 33.919,81 a R$ 45.012,60: alíquota de 15%.
De R$ 45.012,61 a R$ 55.976,16: alíquota de 22,5%.
Acima de R$ 55.976,16: alíquota de 27,5%.
O programa deve exibir o valor do imposto de renda devido."
'''

# Método facil
# Metodo otimizado
faixas_e_aliquotas = [
    (22847.76, 0),             # Até R$ 22.847,76: isento de imposto.
    (33919.80, 7.5),           # De R$ 22.847,77 a R$ 33.919,80: alíquota de 7,5%.
    (45012.60, 15),           # De R$ 33.919,81 a R$ 45.012,60: alíquota de 15%.
    (55976.16, 22.5),         # De R$ 45.012,61 a R$ 55.976,16: alíquota de 22,5%.
    (float('inf'), 27.5) 
]

renda_anual = float(input("Digite a renda anual: "))
imposto = 0

for faixa, aliquota in faixas_e_aliquotas:
    if renda_anual <= faixa:
        imposto += (renda_anual * aliquota) / 100
        break
    else:
        imposto += (faixa * aliquota) / 100
        renda_anual -= faixa

print(f"O imposto foi de {imposto:.2f}")