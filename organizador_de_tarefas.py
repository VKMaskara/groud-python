import time
import design   # importa o módulo responsável pela interface visual

tarefas = []  # lista onde todas as tarefas serão armazenadas


# ---------------- FUNÇÕES DO SISTEMA ---------------- #

def mostrar_menu():
    design.titulo_secao("Menu Principal", animar=False)
    design.digitar(f"{design.COR_INFO}OPÇÕES:{design.RESET}", 0.005)

    design.digitar("1 - Adicionar tarefa", 0.005)
    design.digitar("2 - Marcar tarefa como concluída", 0.005)
    design.digitar("3 - Remover tarefa", 0.005)
    design.digitar("4 - Listar tarefas", 0.005)
    design.digitar("5 - Sair", 0.005)


# ----------- REQUISITO 1: ADICIONAR TAREFAS EM SEQUÊNCIA ----------- #

def adicionar_tarefa():
    while True:   # Loop para adicionar várias tarefas seguidas
        design.limpar_tela()
        design.titulo_secao("Adicionar Nova Tarefa")

        nome = design.pergunta("Digite o nome da tarefa").strip()

        if nome == "":
            design.anim_erro("Tarefa não pode ser vazia!")
            time.sleep(1)
            continue  # volta para repetir o input

        tarefa = {"nome": nome, "status": "pendente"}
        tarefas.append(tarefa)

        design.anim_sucesso(f"Tarefa '{nome}' adicionada com sucesso!")
        time.sleep(1)

        # Pergunta se deseja adicionar mais
        continuar = design.pergunta("Adicionar outra tarefa? (s/n)").lower().strip()
        if continuar != "s":   # qualquer coisa que NÂO seja "s" volta ao menu
            break



def listar_tarefas():
    design.limpar_tela()
    design.titulo_secao("Lista de Tarefas")

    if not tarefas:
        design.info("Nenhuma tarefa cadastrada.")
        time.sleep(1.5)
        return

    for i, t in enumerate(tarefas, start=1):
        if t['status'] == 'concluida':
            status = f"{design.COR_SUCESSO}[✓ CONCLUÍDA]{design.RESET}"
        else:
            status = f"{design.COR_INFO}[- PENDENTE]{design.RESET}"

        design.digitar(
            f"{design.COR_BRANCO}{i}{design.RESET} - {t['nome']} {status}",
            0.002
        )

    design.info("Fim da lista de tarefas.")
    time.sleep(2)



# Função auxiliar simples
def listar_tarefas_simples():
    if not tarefas:
        design.info("Nenhuma tarefa cadastrada.")
        return

    design.info("Tarefas Atuais:")
    for i, t in enumerate(tarefas, start=1):
        status = (
            f"{design.COR_SUCESSO}[✓]{design.RESET}"
            if t['status'] == 'concluida'
            else f"{design.COR_ERRO}[-]{design.RESET}"
        )
        print(f"{design.COR_BRANCO}{i} - {t['nome']} {status}")
    print()



# ----------- REQUISITO 2: ERRO DE INPUT VOLTA AO INPUT ----------- #

def concluir_tarefa():
    while True:   # loop para garantir que input errado volte para o input
        design.limpar_tela()
        design.titulo_secao("Concluir Tarefa")

        listar_tarefas_simples()
        if not tarefas:
            return

        escolha = design.pergunta("Escolha o número da tarefa para concluir")

        if not escolha.isdigit():
            design.anim_erro("Entrada inválida! Digite um número válido.")
            time.sleep(1)
            continue  # volta para o input

        escolha = int(escolha)

        if 1 <= escolha <= len(tarefas):
            nome = tarefas[escolha - 1]['nome']
            tarefas[escolha - 1]["status"] = "concluida"

            design.anim_sucesso(f"Tarefa '{nome}' marcada como CONCLUÍDA!")
            time.sleep(1.5)
            return  # encerra função
        else:
            design.anim_erro("Número inválido! Tente novamente.")
            time.sleep(1)



def remover_tarefa():
    while True:
        design.limpar_tela()
        design.titulo_secao("Remover Tarefa")

        listar_tarefas_simples()
        if not tarefas:
            return

        escolha = design.pergunta("Escolha o número da tarefa para remover")

        if not escolha.isdigit():
            design.anim_erro("Entrada inválida! Digite um número válido.")
            time.sleep(1)
            continue

        escolha = int(escolha)

        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            design.anim_sucesso(f"Tarefa '{tarefa_removida['nome']}' REMOVIDA com sucesso!")
            time.sleep(1.5)
            return
        else:
            design.anim_erro("Número inválido! Tente novamente.")
            time.sleep(1)



# ---------------- LOOP PRINCIPAL DO PROGRAMA ---------------- #

while True:
    design.limpar_tela()
    mostrar_menu()

    opcao = design.pergunta("Escolha uma opção").strip()

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        concluir_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        design.info("Saindo do organizador...")
        design.loading("Finalizando", ciclos=3)
        design.limpar_tela()
        break
    else:
        design.anim_erro("Opção inválida! Tente novamente.")
        time.sleep(1)
