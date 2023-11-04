# Variáveis para o total de países e jogadores
total_paises = 30
total_jogadores = total_paises * 12

# Variáveis para o peso total e idade total de todos os jogadores
peso_total = 0
idade_total = 0

# Variáveis para armazenar as informações dos atletas mais pesados e mais jovens de cada time
peso_mais_pesado = 0
idade_mais_jovem = float('inf')

# Laço para percorrer cada país
for pais in range(1, 3):
    peso_time = 0
    idade_time = 0

    # Laço para percorrer cada jogador de um time
    for jogador in range(1, 4):
        # Solicitar o peso e a idade do jogador
        peso = float(input(f"Informe o peso do jogador {jogador} do país {pais}: "))
        idade = int(input(f"Informe a idade do jogador {jogador} do país {pais}: "))

        # Atualizar o peso total e idade total de todos os jogadores
        peso_total += peso
        idade_total += idade

        # Atualizar o peso total e idade total de cada time
        peso_time += peso
        idade_time += idade

        # Verificar se o jogador é o mais pesado do time
        if peso > peso_mais_pesado:
            peso_mais_pesado = peso

        # Verificar se o jogador é o mais jovem do time
        if idade < idade_mais_jovem:
            idade_mais_jovem = idade

    # Calcular o peso médio e idade média de cada time
    peso_medio_time = peso_time / 4
    idade_medio_time = idade_time / 4

    # Exibir as informações do time
    print(f"No time {pais}:")
    print(f"Peso médio: {peso_medio_time} kg")
    print(f"Idade média: {idade_medio_time} anos")
    print()

# Calcular o peso médio e idade média de todos os jogadores
peso_medio_total = peso_total / total_jogadores
idade_medio_total = idade_total / total_jogadores

# Exibir as informações de todos os jogadores
print("No campeonato:")
print(f"Peso médio de todos os participantes: {peso_medio_total} kg")
print(f"Idade média de todos os participantes: {idade_medio_total} anos")