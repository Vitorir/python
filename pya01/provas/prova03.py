'''
[PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
'''

alunoLista = dict()


while True:

    print("-------- Listinha de matricula --------")
    print("///// Escolha uma opção /////")

    print("======== 1-Adicionar um aluno ========")

    print("======== 2-Remover um aluno =====")

    print("===== 3-Ver lista =====")

    print("======== 4-Sair ========")

    op = int(input("Sua opção é: "))

    match op:
        case 1:
            nomeAluno = input("Informe o nome do aluno: ")
            numeroMatricula = input("Informe o numero do matricula: ")
            alunoLista[nomeAluno] = numeroMatricula

        case 2:
            for nomeAluno, numeroMatricula in alunoLista.items():
                print(f"Nome: {nomeAluno}, Matrícula: {numeroMatricula}")

            matricula = input(
                "informe o aluno que você deseja remover de acordo com o numero de matricula: ")

            if matricula in alunoLista:

                del alunoLista[matricula]

                print("aluno removido")

        case 3:
            for nomeAluno, numeroMatricula in alunoLista.items():
                print(f"Nome: {nomeAluno}, Matrícula: {numeroMatricula}")
