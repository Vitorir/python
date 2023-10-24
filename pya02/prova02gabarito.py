listImpar = []

listPar = []

numImpar = 0

contImpar = 0

numPar = 0

contPar = 0



for i in range(1,11):

    num = int(input(f"digite um valor responsavel pelo indice {i} da lista: "))

    

    if(num % 2 == 0):

        contPar += 1

        numPar += num

        listPar.append(num)

    else:

        contImpar += 1

        numImpar += num

        listImpar.append(num)  

         

numTupla = (listPar, listImpar)



print("Numeros pares = ",end="")

for list in numTupla[0]:

    print(list, end=" ")

print("")

print("Numeros impares = ",end="")

for list in numTupla[1]:

    print(list, end=" ")



print (f"\nContem na lista {contPar} numeros pares e a soma de todos eles é de {numPar}")

print (f"Contem na lista {contImpar} numeros impares e a soma de todos eles é de {numImpar}")