from design import limpar_tela
from design import tela
from design import pergunta
from design import anim_sucesso
from design import anim_erro
import random
competidores = {}

def perfil():
    limpar_tela()
    tela("Perfil dos Skatistas")

    if not competidores:
        anim_erro("Nenhum skatista foi cadastrado ainda.")
        input("\nPressione ENTER para voltar...")
        return

    # Mostrar lista numerada
    print("Selecione um skatista:\n")
    nomes = list(competidores.keys())

    for i, nome in enumerate(nomes, 1):
        print(f"{i} - {nome}")

    # Escolha do usuário
    opc = input("\nDigite o número do skatista: ").strip()

    if not opc.isdigit():
        anim_erro("Você deve digitar apenas números!")
        input("\nPressione ENTER para voltar...")
        return

    opc = int(opc)

    if opc < 1 or opc > len(nomes):
        anim_erro("Número fora da lista!")
        input("\nPressione ENTER para voltar...")
        return

    # Recupera o skatista escolhido
    nome_escolhido = nomes[opc - 1]
    dados = competidores[nome_escolhido]

    limpar_tela()
    tela(f"Perfil de {nome_escolhido}")

    print(f"Notas: {dados['notas']}")
    print(f"Média final: {dados['media']:.2f}")
    print("-" * 30)

    input("\nPressione ENTER para voltar...")

def cadastro():
    limpar_tela()
    tela("Cadastro de Skatista")
    nome = pergunta("Nome do skatista")
    manobras = int(pergunta("Quantas manobras"))
    limpar_tela()
    notas = []
    anim_sucesso("Skatista cadastrado com sucesso!")


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
    tela("Ranking Final")
    
    ordem = sorted(competidores.items(), key=lambda x: x[1]['media'], reverse=True)

    if not ordem:
        anim_erro("Nenhum skatista cadastrado!")
        input("\nPressione ENTER para voltar...")
        return
    
    for i, (nome, dados) in enumerate(ordem, 1):
        print(f"{i}º - {nome}: média {dados['media']:.2f}")
    
    input("\nPressione ENTER para voltar...")


while True:
    tela("COMPETIÇÃO DE SKATE")

    print("1 - Cadastrar skatista")
    print("2 - Mostrar ranking")
    print("3 - Perfil do skatista")
    print("4 - Sair\n")

    opc = pergunta("Escolha uma opção")  # <-- SOMENTE AQUI

    if opc == "1":
        while True:
            cadastro()

            resp = input('\nDeseja continuar no cadastro? [S/N] ').strip().upper()

            while resp not in ('S', 'N'):
                anim_erro("Resposta inválida! Tente novamente.")
                resp = input('Deseja continuar no cadastro? [S/N] ').strip().upper()

            if resp == 'N':
                break

    elif opc == "2":
        ranking()

    elif opc == "3":
        perfil()

    elif opc == "4":
        limpar_tela()
        break

    else:
        anim_erro("Opção inválida!")
        input("\nPressione ENTER...")