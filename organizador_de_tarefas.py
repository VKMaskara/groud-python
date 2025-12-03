#Organizador de tarefas
#Feito por Kaique sousa  
import design  # importa o módulo responsável pela interface visual
import time    # importa time para usar pausas (sleep)

tarefas = []  # lista onde todas as tarefas serão armazenadas


# TELA INICIAL
design.tela("Sistema Oficial de Tarefas")  # mostra a tela inicial com título
design.loading("Carregando seu organizador", ciclos=4)  # animação de carregamento



# ---------------- FUNÇÕES DO SISTEMA ---------------- #

def mostrar_menu():
    design.titulo_secao("Menu Principal", animar=False)  # mostra o título do menu
    design.digitar(f"{design.COR_INFO}OPÇÕES:{design.RESET}", 0.005)  # mostra a palavra "OPÇÕES"

    design.digitar("1 - Adicionar tarefa", 0.005)  # opção 1
    design.digitar("2 - Marcar tarefa como concluída", 0.005)  # opção 2
    design.digitar("3 - Remover tarefa", 0.005)  # opção 3
    design.digitar("4 - Listar tarefas", 0.005)  # opção 4
    design.digitar("5 - Sair", 0.005)  # opção 5


def adicionar_tarefa():
    design.limpar_tela()  # limpa a tela
    design.titulo_secao("Adicionar Nova Tarefa")  # mostra o título da seção

    nome = design.pergunta("Digite o nome da tarefa").strip()  # recebe o nome da tarefa

    if nome == "":  # se o usuário não digitar nada
        design.anim_erro("Tarefa não pode ser vazia!")  # mensagem de erro
        time.sleep(1)  # pequena pausa
        return  # volta para o menu

    tarefa = {"nome": nome, "status": "pendente"}  # cria o dicionário da tarefa
    tarefas.append(tarefa)  # adiciona a tarefa na lista

    design.anim_sucesso(f"Tarefa '{nome}' adicionada com sucesso!")  # mostra sucesso
    time.sleep(1)  # pausa


def listar_tarefas():
    design.limpar_tela()  # limpa a tela
    design.titulo_secao("Lista de Tarefas")  # título da seção

    if not tarefas:  # se a lista estiver vazia
        design.info("Nenhuma tarefa cadastrada.")  # avisa o usuário
        time.sleep(1.5)  # pausa
        return  # encerra a função

    for i, t in enumerate(tarefas, start=1):  # percorre a lista com índice
        if t['status'] == 'concluida':  # se estiver concluída
            status_colorido = f"{design.COR_SUCESSO}[✓ CONCLUÍDA]{design.RESET}"  # texto verde
        else:  # se estiver pendente
            status_colorido = f"{design.COR_INFO}[- PENDENTE]{design.RESET}"  # texto azul

        # imprime tarefa com número, nome e status colorido
        design.digitar(f"{design.COR_BRANCO}{i}{design.RESET} - {t['nome']} {status_colorido}", 0.002)

    design.info("Fim da lista de tarefas.")  # mensagem final
    time.sleep(2)  # pausa


def concluir_tarefa():
    design.limpar_tela()  # limpa tela
    design.titulo_secao("Concluir Tarefa")  # título da seção

    listar_tarefas_simples()  # mostra lista simples
    if not tarefas:  # se não houver tarefas
        return  # sai

    escolha = design.pergunta("Escolha o número da tarefa para concluir")  # número da tarefa

    if not escolha.isdigit():  # se não for um número
        design.anim_erro("Entrada inválida! Digite um número válido.")  # erro
        time.sleep(1)
        return

    escolha = int(escolha)  # converte para número inteiro

    if 1 <= escolha <= len(tarefas):  # verifica se o número existe na lista
        nome_tarefa = tarefas[escolha - 1]['nome']  # pega o nome
        tarefas[escolha - 1]["status"] = "concluida"  # marca como concluída
        design.anim_sucesso(f"Tarefa '{nome_tarefa}' marcada como CONCLUÍDA!")  # sucesso
    else:
        design.anim_erro("Número inválido. Tarefa não encontrada.")  # erro

    time.sleep(1.5)


def remover_tarefa():
    design.limpar_tela()  # limpa a tela
    design.titulo_secao("Remover Tarefa")  # título da seção

    listar_tarefas_simples()  # mostra lista simples
    if not tarefas:  # se lista vazia
        return

    escolha = design.pergunta("Escolha o número da tarefa para remover")  # número da tarefa

    if not escolha.isdigit():  # validação
        design.anim_erro("Entrada inválida! Digite um número válido.")  # erro
        time.sleep(1)
        return

    escolha = int(escolha)  # transforma em inteiro

    if 1 <= escolha <= len(tarefas):  # verifica se existe
        tarefa_removida = tarefas.pop(escolha - 1)  # remove do índice
        design.anim_sucesso(f"Tarefa '{tarefa_removida['nome']}' REMOVIDA com sucesso!")  # sucesso
    else:
        design.anim_erro("Número inválido. Tarefa não encontrada.")  # erro

    time.sleep(1.5)



# Função auxiliar para listas rápidas
def listar_tarefas_simples():
    if not tarefas:  # se lista vazia
        design.info("Nenhuma tarefa cadastrada.")  # avisa
        return

    design.info("Tarefas Atuais:")  # título
    for i, t in enumerate(tarefas, start=1):  # percorre lista
        if t['status'] == 'concluida':  # concluída
            status_colorido = f"{design.COR_SUCESSO}[✓]{design.RESET}"  # verde
        else:  # pendente
            status_colorido = f"{design.COR_ERRO}[-]{design.RESET}"  # vermelho

        print(f"{design.COR_BRANCO}{i} - {t['nome']} {status_colorido}")  # imprime simples

    print()  # linha extra de separação



# ---------------- LOOP PRINCIPAL DO PROGRAMA ---------------- #

while True:  # loop infinito do menu
    design.limpar_tela()  # limpa tela
    mostrar_menu()  # mostra opções

    opcao = design.pergunta("Escolha uma opção")  # recebe a opção do usuário

    if opcao == "1":  # adicionar tarefa
        adicionar_tarefa()
    elif opcao == "2":  # concluir tarefa
        concluir_tarefa()
    elif opcao == "3":  # remover tarefa
        remover_tarefa()
    elif opcao == "4":  # listar tarefas
        listar_tarefas()
    elif opcao == "5":  # sair do sistema
        design.info("Saindo do organizador...")  # mensagem final
        design.loading("Finalizando", ciclos=3)  # mostra carregamento
        design.limpar_tela()  # limpa tudo
        break  # encerra o programa
    else:
        design.anim_erro("Opção inválida. Tente novamente.")  # erro caso opção não exista
        time.sleep(1)  # pausa
