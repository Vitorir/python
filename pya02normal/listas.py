
lista_compras = ['maca', 'agua', 'fruta',  'pao', 'vinagre', 'detergente', 'sabao']
del lista_compras[0]
del lista_compras[2]

lista_atual = lista_compras.copy()
lista_compras.clear()

print(lista_atual)
print(lista_compras)

lista_limpeza = lista_compras[4:6]

usuarios = [
    ['fulano', 'fulano123'],
    ['beltrano', 'beltrano123'],
    ['sicrano', 'sicr123']
]

usuarios_autenticados = usuarios[:2]
print(usuarios_autenticados[0][0])
print(usuarios_autenticados[1][0])


musicas = ['Yellow Submarine', 'Yesterday', 'Hey, Jude', 'Lucy in the Sky']
musicas.remove('Hey, Jude')
musicas.remove('Lucy in the Sky')
musicas.append('Dont let me Down')
