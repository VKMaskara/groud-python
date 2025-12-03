# program afeito com a finalidade de organizar tarefas e conseguir determinar se esta concluida ou não 
# feito por Kaique Sousa  

import time                           # importa o módulo time para usar pausas (sleep)
import design                         # importa o módulo responsável pela interface visual

tarefas = []                          # cria uma lista vazia para armazenar todas as tarefas


# ---------------- FUNÇÕES DO SISTEMA ---------------- #

def mostrar_menu():                   # função que mostra o menu principal com as opções
    design.titulo_secao("Menu Principal", animar=False)  # exibe o título "Menu Principal" sem animação
    design.digitar(f"{design.COR_INFO}OPÇÕES:{design.RESET}", 0.005)  # escreve "OPÇÕES:" usando estilo/color

    design.digitar("1 - Adicionar tarefa", 0.005)  # mostra a opção 1 no menu
    design.digitar("2 - Marcar tarefa como concluída", 0.005)  # mostra a opção 2 no menu
    design.digitar("3 - Remover tarefa", 0.005)  # mostra a opção 3 no menu
    design.digitar("4 - Listar tarefas", 0.005)  # mostra a opção 4 no menu
    design.digitar("5 - Sair", 0.005)  # mostra a opção 5 no menu


# ----------- REQUISITO 1: ADICIONAR TAREFAS EM SEQUÊNCIA ----------- #

def adicionar_tarefa():                # função que permite adicionar uma ou várias tarefas seguidas
    while True:                        # loop que mantém a função até o usuário decidir voltar ao menu
        design.limpar_tela()           # limpa a tela/console antes de mostrar a seção
        design.titulo_secao("Adicionar Nova Tarefa")  # exibe título da seção de adicionar tarefa

        nome = design.pergunta("Digite o nome da tarefa").strip()  # pede o nome da tarefa e remove espaços em branco

        if nome == "":                 # verifica se o usuário deixou o nome vazio
            design.anim_erro("Tarefa não pode ser vazia!")  # mostra animação/erro informando que não pode ficar vazio
            time.sleep(1)              # pausa curta para o usuário ver a mensagem
            continue                   # volta para o início do loop e pede o nome novamente

        tarefa = {"nome": nome, "status": "pendente"}  # cria um dicionário representando a tarefa (nome + status)
        tarefas.append(tarefa)        # adiciona o dicionário na lista global 'tarefas'

        design.anim_sucesso(f"Tarefa '{nome}' adicionada com sucesso!")  # mostra animação de sucesso
        time.sleep(1)                 # pausa para o usuário ver a confirmação

        # Pergunta se deseja adicionar mais
        continuar = design.pergunta("Adicionar outra tarefa? (s/n)").lower().strip()  # pede confirmação e normaliza
        if continuar != "s":          # se a resposta NÃO for 's' (sim)
            break                     # sai do loop e volta para o menu principal



def listar_tarefas():                  # função que mostra a lista formatada de tarefas com status
    design.limpar_tela()               # limpa a tela antes de mostrar a lista
    design.titulo_secao("Lista de Tarefas")  # exibe o título da seção

    if not tarefas:                    # verifica se a lista 'tarefas' está vazia
        design.info("Nenhuma tarefa cadastrada.")  # informa que não há tarefas
        time.sleep(1.5)                # pequena pausa para o usuário ler a mensagem
        return                         # encerra a função

    for i, t in enumerate(tarefas, start=1):  # percorre cada tarefa com índice começando em 1
        if t['status'] == 'concluida':       # verifica se a tarefa foi marcada como concluída
            status = f"{design.COR_SUCESSO}[✓ CONCLUÍDA]{design.RESET}"  # cria texto de status concluída
        else:
            status = f"{design.COR_INFO}[- PENDENTE]{design.RESET}"  # cria texto de status pendente

        design.digitar(                       # imprime cada tarefa formatada: número - nome [status]
            f"{design.COR_BRANCO}{i}{design.RESET} - {t['nome']} {status}",
            0.002
        )

    design.info("Fim da lista de tarefas.")  # mensagem final após listar tudo
    time.sleep(2)                             # pausa para o usuário ver a lista antes de voltar



# Função auxiliar simples
def listar_tarefas_simples():        # função que imprime uma versão simples/compacta das tarefas (usada por outras funções)
    if not tarefas:                  # se não houver tarefas
        design.info("Nenhuma tarefa cadastrada.")  # avisa o usuário
        return                       # retorna sem fazer mais nada

    design.info("Tarefas Atuais:")   # cabeçalho simples
    for i, t in enumerate(tarefas, start=1):  # percorre tarefas com índice
        status = (                   # escolhe o símbolo/estilo de status rapidamente
            f"{design.COR_SUCESSO}[✓]{design.RESET}"
            if t['status'] == 'concluida'
            else f"{design.COR_ERRO}[-]{design.RESET}"
        )
        print(f"{design.COR_BRANCO}{i} - {t['nome']} {status}")  # imprime linha simples (usando print)
    print()                           # linha em branco para separar/formatar saída



# ----------- REQUISITO 2: ERRO DE INPUT VOLTA AO INPUT ----------- #

def concluir_tarefa():               # função para marcar uma tarefa como concluída
    while True:                       # loop para que, em caso de erro de entrada, o usuário possa tentar novamente
        design.limpar_tela()          # limpa a tela antes de mostrar a seção
        design.titulo_secao("Concluir Tarefa")  # exibe título da seção

        listar_tarefas_simples()      # mostra a lista simples para o usuário escolher o número
        if not tarefas:               # se não houver tarefas cadastradas
            return                    # sai da função (não há nada para concluir)

        escolha = design.pergunta("Escolha o número da tarefa para concluir")  # pede o número da tarefa

        if not escolha.isdigit():     # verifica se a entrada é somente dígitos (número)
            design.anim_erro("Entrada inválida! Digite um número válido.")  # mostra erro de entrada inválida
            time.sleep(1)             # pausa curta
            continue                  # volta para o começo do loop e pede a entrada de novo

        escolha = int(escolha)        # converte a escolha para inteiro

        if 1 <= escolha <= len(tarefas):  # verifica se o número está dentro do intervalo de tarefas existentes
            nome = tarefas[escolha - 1]['nome']  # obtém o nome da tarefa selecionada
            tarefas[escolha - 1]["status"] = "concluida"  # altera o status para 'concluida'

            design.anim_sucesso(f"Tarefa '{nome}' marcada como CONCLUÍDA!")  # mostra sucesso
            time.sleep(1.5)          # pausa para o usuário ver a confirmação
            return                   # encerra a função (tarefa concluída com sucesso)
        else:
            design.anim_erro("Número inválido! Tente novamente.")  # se número fora do intervalo, avisa
            time.sleep(1)             # pausa curta e o loop repete



def remover_tarefa():                # função para remover uma tarefa da lista
    while True:                       # loop para permitir novas tentativas em caso de erro de input
        design.limpar_tela()          # limpa a tela para mostrar a seção
        design.titulo_secao("Remover Tarefa")  # exibe o título da seção

        listar_tarefas_simples()      # mostra as tarefas atualmente cadastradas
        if not tarefas:               # se a lista estiver vazia
            return                    # sai da função (não há nada para remover)

        escolha = design.pergunta("Escolha o número da tarefa para remover")  # pede o número a remover

        if not escolha.isdigit():     # valida se a entrada é numérica
            design.anim_erro("Entrada inválida! Digite um número válido.")  # mostra erro
            time.sleep(1)             # pausa curta
            continue                  # volta a pedir a escolha

        escolha = int(escolha)        # converte a entrada para inteiro

        if 1 <= escolha <= len(tarefas):  # verifica se o número é válido
            tarefa_removida = tarefas.pop(escolha - 1)  # remove a tarefa da lista e guarda o dicionário removido
            design.anim_sucesso(f"Tarefa '{tarefa_removida['nome']}' REMOVIDA com sucesso!")  # sucesso
            time.sleep(1.5)          # pausa para o usuário ver a confirmação
            return                   # sai da função depois de remover
        else:
            design.anim_erro("Número inválido! Tente novamente.")  # se inválido, avisa e repete o loop
            time.sleep(1)



# ---------------- LOOP PRINCIPAL DO PROGRAMA ---------------- #

while True:                           # loop principal que mantém o programa em execução até o usuário escolher sair
    design.limpar_tela()              # limpa a tela a cada iteração do menu
    mostrar_menu()                    # chama a função que exibe o menu principal

    opcao = design.pergunta("Escolha uma opção").strip()  # pede a opção do usuário e remove espaços

    if opcao == "1":                  # se usuário escolher '1', chama a função de adicionar tarefa
        adicionar_tarefa()
    elif opcao == "2":                # se escolher '2', chama a função para concluir tarefa
        concluir_tarefa()
    elif opcao == "3":                # se escolher '3', chama a função para remover tarefa
        remover_tarefa()
    elif opcao == "4":                # se escolher '4', chama a função que lista todas as tarefas
        listar_tarefas()
    elif opcao == "5":                # se escolher '5', realiza limpeza e encerra o loop (sai do programa)
        design.info("Saindo do organizador...")  # informa que está saindo
        design.loading("Finalizando", ciclos=3)  # animação de finalização
        design.limpar_tela()          # limpa a tela antes de encerrar
        break                         # interrompe o loop principal e termina o programa
    else:
        design.anim_erro("Opção inválida! Tente novamente.")  # se a opção não bater com nenhuma, mostra erro
        time.sleep(1)                 # pausa para o usuário ver a mensagem antes de mostrar o menu de novo
