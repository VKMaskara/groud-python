
# program afeito com a finalidade de organizar tarefas e conseguir determinar se esta concluida ou não 
# feito por Kaique Sousa  

import time        # importa o módulo time, usado para pausas (time.sleep)
import design      # importa o módulo 'design', responsável pela interface visual (cores, prints animados)

def main():        # função principal do programa
    tarefas = []   # lista onde todas as tarefas serão armazenadas

    # ------------------------ MOSTRAR MENU ------------------------ #

    def mostrar_menu():   # função que mostra o menu principal ao usuário
        design.titulo_secao("Menu Principal", animar=False)  # exibe o título da seção
        design.digitar(f"{design.COR_INFO}OPÇÕES:{design.RESET}", 0.005)  # escreve "OPÇÕES:" lentamente
        design.digitar("1 - Adicionar tarefa", 0.005)        # opção 1
        design.digitar("2 - Marcar tarefa como concluída", 0.005)  # opção 2
        design.digitar("3 - Remover tarefa", 0.005)          # opção 3
        design.digitar("4 - Listar tarefas", 0.005)          # opção 4
        design.digitar("5 - Sair", 0.005)                    # opção 5

    # ------------------------ ADICIONAR TAREFA ------------------------ #

    def adicionar_tarefa():   # função que adiciona uma ou várias tarefas
        while True:           # loop para permitir adicionar várias tarefas seguidas
            design.limpar_tela()               # limpa a tela
            design.titulo_secao("Adicionar Nova Tarefa")  # mostra o título

            nome = design.pergunta("Digite o nome da tarefa").strip()  # pede o nome da tarefa

            if nome == "":                     # verifica se o nome está vazio
                design.anim_erro("Tarefa não pode ser vazia!")  # avisa o erro
                time.sleep(1)                  # pausa para o usuário ver
                continue                       # volta ao início e pede novamente

            tarefa = {"nome": nome, "status": "pendente"}  # cria uma tarefa com nome + status
            tarefas.append(tarefa)             # adiciona à lista de tarefas

            design.anim_sucesso(f"Tarefa '{nome}' adicionada com sucesso!")  # mensagem de sucesso
            time.sleep(1)                      # pausa para mostrar a mensagem

            while True:      # valida se o usuário digitou apenas s ou n
                continuar = design.pergunta("Adicionar outra tarefa? (s/n)").lower().strip()
                if continuar in ["s", "n"]:    # só aceita s ou n
                    break                      # sai da validação
                design.anim_erro("Digite apenas 's' ou 'n'.")  # caso contrário, erro
                time.sleep(1)

            if continuar != "s":               # se digitou 'n', sai dessa função
                break

    # ------------------------ LISTAR TAREFAS ------------------------ #

    def listar_tarefas():     # função que mostra a lista completa de tarefas
        design.limpar_tela()  # limpa a tela antes de listar
        design.titulo_secao("Lista de Tarefas")  # mostra o título

        if not tarefas:       # se a lista está vazia
            design.info("Nenhuma tarefa cadastrada.")  # mensagem informando isso
            input("Pressione ENTER para continuar...") # espera o usuário ler
            return            # sai da função

        for i, t in enumerate(tarefas, start=1):   # percorre as tarefas
            if t["status"] == "concluida":        # se estiver concluída
                status = f"{design.COR_SUCESSO}[✓ CONCLUÍDA]{design.RESET}"
            else:                                  # se estiver pendente
                status = f"{design.COR_INFO}[- PENDENTE]{design.RESET}"

            design.digitar(                        # imprime o número, nome e status
                f"{design.COR_BRANCO}{i}{design.RESET} - {t['nome']} {status}",
                0.002
            )

        input("Pressione ENTER para continuar...")  # espera antes de voltar ao menu

    # ------------------------ LISTAGEM SIMPLES ------------------------ #

    def listar_tarefas_simples():    # lista as tarefas de forma simples (usada em remover e concluir)
        if not tarefas:              # verifica se não tem tarefas
            design.info("Nenhuma tarefa cadastrada.")  # avisa o usuário
            return

        design.info("Tarefas Atuais:")   # título simples
        for i, t in enumerate(tarefas, start=1):   # percorre tarefas
            if t["status"] == "concluida":
                status = f"{design.COR_SUCESSO}[✓]{design.RESET}"   # concluída
            else:
                status = f"{design.COR_ERRO}[-]{design.RESET}"       # pendente

            print(f"{design.COR_BRANCO}{i} - {t['nome']} {status}")  # imprime a tarefa
        print()  # linha em branco

    # ------------------------ CONCLUIR TAREFA ------------------------ #

    def concluir_tarefa():    # função que marca uma tarefa como concluída
        while True:           # permite tentar novamente caso erro
            design.limpar_tela()  # limpa a tela
            design.titulo_secao("Concluir Tarefa")  # título da seção

            listar_tarefas_simples()   # mostra lista simples

            if not tarefas:            # se não há tarefas
                design.info("Nenhuma tarefa cadastrada.")
                time.sleep(2)          # deixa tempo para ler
                return                 # sai da função

            escolha = design.pergunta("Escolha o número da tarefa para concluir")  # pede número

            if not escolha.isdigit():  # valida se é número
                design.anim_erro("Entrada inválida! Digite um número válido.")
                time.sleep(1)
                continue               # volta ao início

            escolha = int(escolha)     # converte para inteiro

            if 1 <= escolha <= len(tarefas):  # verifica se está no intervalo
                nome = tarefas[escolha - 1]["nome"]  # pega o nome
                tarefas[escolha - 1]["status"] = "concluida"  # marca como concluída

                design.anim_sucesso(f"Tarefa '{nome}' marcada como CONCLUÍDA!")  # sucesso
                time.sleep(1.5)
                return                 # sai da função
            else:
                design.anim_erro("Número inválido! Tente novamente.")  # erro de número
                time.sleep(1)

    # ------------------------ REMOVER TAREFA ------------------------ #

    def remover_tarefa():   # função que remove uma tarefa da lista
        while True:         # loop para corrigir entradas erradas
            design.limpar_tela()   # limpa tela
            design.titulo_secao("Remover Tarefa")  # título

            listar_tarefas_simples()  # mostra lista

            if not tarefas:    # se lista estiver vazia
                design.info("Nenhuma tarefa cadastrada.")
                time.sleep(1.5)
                return

            escolha = design.pergunta("Escolha o número da tarefa para remover")  # pede o número

            if not escolha.isdigit():   # verifica se é número
                design.anim_erro("Entrada inválida! Digite um número válido.")
                time.sleep(1)
                continue

            escolha = int(escolha)      # converte para inteiro

            if 1 <= escolha <= len(tarefas):  # se número é válido
                removida = tarefas.pop(escolha - 1)  # remove a tarefa
                design.anim_sucesso(f"Tarefa '{removida['nome']}' REMOVIDA com sucesso!")
                time.sleep(1.5)
                return                   # sai da função
            else:
                design.anim_erro("Número inválido! Tente novamente.")
                time.sleep(1)

    # ------------------------ LOOP PRINCIPAL ------------------------ #

    while True:             # mantém o programa rodando até o usuário sair
        design.limpar_tela()     # limpa a tela
        mostrar_menu()           # mostra o menu principal

        opcao = design.pergunta("Escolha uma opção").strip()  # lê a escolha do usuário

        if opcao == "1":
            adicionar_tarefa()   # adiciona tarefa
        elif opcao == "2":
            concluir_tarefa()    # conclui tarefa
        elif opcao == "3":
            remover_tarefa()     # remove tarefa
        elif opcao == "4":
            listar_tarefas()     # lista tarefas
        elif opcao == "5":
            design.info("Saindo do organizador...")  # mensagem de saída
            design.loading("Finalizando", ciclos=3)  # animação
            design.limpar_tela()
            break                 # encerra o loop (finaliza o programa)
        else:
            design.anim_erro("Opção inválida! Tente novamente.")  # erro
            time.sleep(1)

# só executa o programa caso o arquivo seja rodado diretamente
if __name__ == "__main__":
    main()   # chama a função principal
