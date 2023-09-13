print("Responda as perguntas com 'sim'/'nao'")

perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"]

respostas_positivas = 0

for i in perguntas:
    resposta = input(i + '\n')
    if resposta.lower() == 'sim':
        respostas_positivas+= 1

if respostas_positivas == 2:
    print('Suspeita')
elif 3 <= respostas_positivas <= 4:
    print('Cúmplice')
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")