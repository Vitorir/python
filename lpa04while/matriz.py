# Imprimindo a primeira linha
for j in range(1, 5):
    print(j, end=" ")
print()

# Imprimindo as linhas subsequentes
for i in range(2, 5):
    for j in range(1, 5):
        print((i-1) * j, end=" ")
    print()
