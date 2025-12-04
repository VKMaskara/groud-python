from design import *
import random

competidores = {}

def main():

    def perfil():  # Função para mostrar o perfil de um skatista
        limpar_tela()
        titulo_secao("Perfil dos Skatistas", animar=False)

        if not competidores:
            anim_erro("Nenhum skatista foi cadastrado ainda.")
            input("\nPressione ENTER para voltar...")
            return

        print("Selecione um skatista:\n")
        nomes = list(competidores)

        for i, nome in enumerate(nomes, 1):
            container(f"{i} - {nome}")

        opcao = input("\nDigite o número do skatista: ").strip()

        if not opcao.isdigit():
            anim_erro("Você deve digitar apenas números!")
            input("\nPressione ENTER para voltar...")
            return

        opcao = int(opcao)

        if opcao < 1 or opcao > len(nomes):
            anim_erro("Número fora da lista!")
            input("\nPressione ENTER para voltar...")
            return

        nome_escolhido = nomes[opcao - 1]
        dados = competidores[nome_escolhido]
        numero_cadastro = opcao

        limpar_tela()
        titulo_secao(f"Perfil de {nome_escolhido}", animar=False)

        print("-" * 30)
        container(f"Número de cadastro: {numero_cadastro}")
        container(f"Notas: {dados['notas']}")
        container(f"Média final: {dados['media']:.2f}")
        print("-" * 30)

        input("\nPressione ENTER para voltar...")

    def cadastro():
        limpar_tela()
        titulo_secao("Cadastro de Skatista", animar=False)

        # Nome do skatista
        while True:
            nome = pergunta("Nome do skatista").title()

            if not nome.replace(" ", "").isalpha():
                anim_erro("O nome não pode conter números ou símbolos!")
                continue

            if nome in competidores:
                anim_erro("Este nome já foi cadastrado! Escolha outro.")
                continue

            break

        # Número de manobras
        while True:
            try:
                manobras = int(pergunta("Quantas manobras (1 a 20)"))
                if 1 <= manobras <= 20:
                    break
                else:
                    anim_erro("Digite um valor entre 1 e 20!")
            except ValueError:
                anim_erro("Você deve digitar um número inteiro!")

        limpar_tela()

        # Geração das notas
        notas = [random.randint(1, 10) for _ in range(manobras)]
        media = sum(notas) / len(notas)

        competidores[nome] = {
            'notas': notas,
            'media': media
        }

        anim_sucesso("Skatista cadastrado com sucesso!")
        print(f"\nO skatista fez {manobras} manobras e recebeu as notas: {notas}")
        print(f"Média: {media:.2f}")

    def ranking():  # Função para mostrar o ranking
        limpar_tela()
        titulo_secao("Ranking Final", animar=False)

        ordem = sorted(
            competidores.items(),
            key=lambda x: x[1]['media'],
            reverse=True
        )

        if not ordem:
            anim_erro("Nenhum skatista cadastrado!")
            input("\nPressione ENTER para voltar...")
            return

        for i, (nome, dados) in enumerate(ordem, 1):
            container(f"{i}º - {nome.ljust(20)}: Média {dados['media']:.2f}")

        input("\nPressione ENTER para voltar...")

    # ---------------- Loop Principal ----------------

    while True:
        limpar_tela()
        titulo_secao("COMPETIÇÃO DE SKATE", animar=False)

        container("1 - Cadastrar skatista")
        container("2 - Mostrar ranking")
        container("3 - Perfil do skatista")
        container("4 - Sair")

        opcao = pergunta("Escolha uma opção")

        if opcao == "1":
            while True:
                cadastro()

                resp = input('\nDeseja cadastrar outro skatista? [S/N] ').strip().upper()

                while resp not in ('S', 'N'):
                    anim_erro("Resposta inválida!")
                    resp = input('Deseja cadastrar outro skatista? [S/N] ').strip().upper()

                if resp == 'N':
                    break

        elif opcao == "2":
            ranking()

        elif opcao == "3":
            perfil()

        elif opcao == "4":
            limpar_tela()
            print("Fim da competição! Até a próxima.")
            break

        else:
            anim_erro("Opção inválida!")
            input("\nPressione ENTER...")

if __name__ == "__main__":
    main()