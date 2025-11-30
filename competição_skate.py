import os
import design
import random
competidores = {}
def limpar():
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear')

def perfil():
    limpar()
    print("--- PERFIL DOS SKATISTAS ---\n")

    if not competidores:
        print("Nenhum skatista foi cadastrado ainda.")
        input("\nPressione ENTER para voltar...")
        return

    # Mostrar lista numerada
    print("Selecione um skatista:\n")
    nomes = list(competidores.keys())

    for i, nome in enumerate(nomes, 1):
        print(f"{i} - {nome}")

    # Escolha do usuário
    try:
        opc = int(input("\nDigite o número do skatista: "))
        if opc < 1 or opc > len(nomes):
            limpar()
            print("Opção inválida!")
            input("\nPressione ENTER para voltar...")
            return
    except ValueError:
        limpar()
        print("Entrada inválida!")
        input("\nPressione ENTER para voltar...")
        return

    # Recupera o skatista escolhido
    nome_escolhido = nomes[opc - 1]
    dados = competidores[nome_escolhido]

    limpar()
    print(f"--- PERFIL DE {nome_escolhido.upper()} ---\n")
    print(f"Notas: {dados['notas']}")
    print(f"Média: {dados['media']:.2f}")
    print("-" * 30)

    input("\nPressione ENTER para voltar...")

def cadastro():
    limpar()
    nome = input("\nNome do Skatista: ")
    limpar()
    manobras = int(input("Quantas manobras? "))
    notas = []

    for i in range(manobras):
        nota = int(random.random() * 10)
        notas.append(nota)

    media = sum(notas) / len(notas)

    competidores[nome] = {
        'notas': notas,
        'media': media
    }

    print("O skatista fez", manobras, "manobras e recebeu as notas:", notas)
    print(f"Média: {media:.2f}")

def ranking():
    limpar()
    print("---RANKING FINAL---")
    ordem = sorted(competidores.items(), key=lambda x: x[1]['media'], reverse=True)
    for i, (nome, dados) in enumerate(ordem, 1):
        print(f"{i}º - {nome} ({dados['media']:.2f})")

while True:
    limpar()
    print("---COMPETIÇÃO DE SKATE---\n\nOs jurados darão as notas para as manobras dos skatistas.\n\n1 - CADASTRAR SKATISTA\n2 - MOSTRAR RANKING\n3 - PERFIL DO SKATISTA\n4 - SAIR")

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
        input("\nPressione enter para continuar...")  

    elif opc == "3":
        perfil()
    elif opc == "4":
        limpar()
        break
    else:
        print("Opção inválida")