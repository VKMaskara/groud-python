from design import *
import random
competidores = {}

def perfil(): # Função para mostrar o perfil de um skatista
    limpar_tela()
    titulo_secao("Perfil dos Skatistas", animar=False)

    if not competidores: # Verifica se há skatistas cadastrados
        anim_erro("Nenhum skatista foi cadastrado ainda.")
        input("\nPressione ENTER para voltar...")
        return

    print("Selecione um skatista:\n")
    nomes = list(competidores) 

    for i, nome in enumerate(nomes, 1): # Lista numerada de skatistas
        container(f"{i} - {nome}")

    opcao = input("\nDigite o número do skatista: ").strip()

    if not opcao.isdigit(): # Validação de entrada numérica
        anim_erro("Você deve digitar apenas números!")
        input("\nPressione ENTER para voltar...")
        return

    opcao = int(opcao)

    if opcao < 1 or opcao > len(nomes): # Verificação de intervalo válido
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

def cadastro(): # Função para cadastrar um skatista
    limpar_tela()
    titulo_secao("Cadastro de Skatista", animar=False)
    
    nome = pergunta("Nome do skatista").title() 
    
    while True: # Loop para garantir que o número de manobras seja válido
        try: 
            manobras_str = pergunta("Quantas manobras (mínimo 1)")
            manobras = int(manobras_str)
            if manobras >= 1: 
                break
            else: 
                anim_erro("O número de manobras deve ser 1 ou mais!")
        except ValueError:
            anim_erro("Você deve digitar um número inteiro!")
            
    limpar_tela()
    
    notas = []
    
    for o in range(manobras): # Coleta das notas para cada manobra
        nota = random.randint(1, 10) # Geração de nota aleatória entre 1 e 10
        notas.append(nota)

    media = sum(notas) / len(notas) # Cálculo da média das notas

    competidores[nome] = { # Armazenamento dos dados do skatista
        'notas': notas,
        'media': media
    }
    
    anim_sucesso("Skatista cadastrado com sucesso!")
    print("\nO skatista fez", manobras, "manobras e recebeu as notas:", notas)
    print(f"Média: {media:.2f}")

def ranking(): # Função para mostrar o ranking dos skatistas
    limpar_tela() 
    titulo_secao("Ranking Final", animar=False)
     
    ordem = sorted(competidores.items(), key=lambda x: x[1]['media'], reverse=True) # Ordenação por média decrescente

    if not ordem: # Verificação se há skatistas cadastrados
        anim_erro("Nenhum skatista cadastrado!")
        input("\nPressione ENTER para voltar...")
        return
    
    for i, (nome, dados) in enumerate(ordem, 1): # Exibição do ranking
        container(f"{i}º - {nome.ljust(20)}: Média {dados['media']:.2f}") 
    
    input("\nPressione ENTER para voltar...")

while True: # Loop principal do programa
    limpar_tela()
    titulo_secao("COMPETIÇÃO DE SKATE", animar=False)
    # Menu
    container("1 - Cadastrar skatista")
    container("2 - Mostrar ranking")
    container("3 - Perfil do skatista")
    container("4 - Sair")

    opcao = pergunta("Escolha uma opção")

    if opcao == "1": # Cadastrar skatista
        while True: # Loop para múltiplos cadastros
            cadastro()

            resp = input('\nDeseja cadastrar outro skatista? [S/N] ').strip().upper()

            while resp not in ('S', 'N'):
                anim_erro("Resposta inválida! Tente novamente.")
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