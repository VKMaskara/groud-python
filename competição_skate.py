import os
import design
import random
competidores = {}
def limpar():
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear')

def ficha():
    print

def cadastro():
    nome = input("\nNome do Skatista: ")
    manobras = int(input("Quantas manobras? "))
    notas = []

    for i in range(manobras):
        nota = int(random.random() * 10)
        notas.append(nota)

    print("O skatista fez", manobras, "manobras e recebeu as notas:", notas)

    
def ranking():
    print("\n---RANKING FINAL---")
    ordem = sorted(competidores.items(),key=lambda x: x[1]['media'],reverse = True)
    for i, (nome, dados) in enumerate(ordem, 1):
        print(f"{i}º - {nome} ({dados['media']:.2f})")

while True:
    print("\n\n---COMPETIÇÃO DE SKATE---\n\nOs jurados darão as notas para as manobras dos skatistas.\n\n1 - CADASTRAR SKATISTA\n2 - MOSTRAR RANKING\n3 - SAIR")

    opc = input("Escolha: ")
    if opc == "1":
        while True:
            cadastro()  # chama a função de cadastro

            resp = input('\nDeseja continuar no cadastro? [S/N] ').strip().upper()

            while resp not in ('S', 'N'):
                print("\nResposta inválida. Tente novamente.")
                resp = input('Deseja continuar no cadastro? [S/N] ').strip().upper()

            if resp == 'N':
                break  # sai do loop principal

        print("\nEncerrando...")


    elif opc == "2":
        ranking()
    elif opc == "3":
        break
    else:
        print("Opção invalida")