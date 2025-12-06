from design import *
 


def menu_principal():
    while True:
        limpar_tela()
        titulo_secao('=== MENU PRINCIPAL ===', animar=False)
        container('1. Jogos')
        container('2. Cálculos')
        container('3. Esporte')
        container('4. Financeiro')
        container('5. Outro')
        container('0. Sair')
        
        
        opcão = pergunta("Escolha uma opção: ")

        if opcão == '1':
            submenu_jogos()
        elif opcão == '2':
            submenu_calculos()
        elif opcão == '3':
            submenu_esporte()
        elif opcão == '4':
            submenu_financeiro()
        elif opcão == '5':
            submenu_outro()
        elif opcão == '0':
        
            loading("Encerrando")
            break
        else:
            anim_erro('Opção inválida! Tente novamente.')


def submenu_jogos():
    while True:
        limpar_tela()
        container('--- SUBMENU JOGOS ---')
        digitar('1. Jogo do 21')
        digitar('2. Jogo de Palavras')
        digitar('3. Jogo do dado')
        digitar("0. Voltar")

        opcão = pergunta('Escolha uma opção: ')

        if opcão == '1':
           import jogo_21
           jogo_21.main()
        elif opcão == '2':
            import jogo_de_palavras
            jogo_de_palavras.main()
        elif opcão == '3':
            import jogo_dados
            jogo_dados.main()   
        elif opcão == "0":
            break
        else:
            anim_erro('Opção inválida!')


def submenu_calculos():
    while True:
        limpar_tela()   
        container('--- SUBMENU CÁLCULOS ---')
        digitar('1. calculo_combustivel')
        digitar('2. Conversor de temperatura')
        digitar('3. Calculo de folha de pagamnento' )
        digitar('4. Cálculo de área')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
          import calculo_combustivel
          calculo_combustivel.main()
        elif opc == '2':
          import conversor_de_temperatura
          conversor_de_temperatura.main()
        elif opc == '3':
            import calculo_folha_de_pagamento
            calculo_folha_de_pagamento.main()
        elif opc == '4':
            import calculo_area
            calculo_area.main()
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')


def submenu_esporte():
    while True:
        limpar_tela()
        container('--- SUBMENU ESPORTE ---')
        digitar('1. IMC de Atletas')
        digitar('2. Competição de Skate')
        digitar('3. Quiz do Corinthians')
        digitar('4. Catalogo de Times de Basquete')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
          import programa_atleta_imc
          programa_atleta_imc.main()
        elif opc == '2':
            import competicao_skate
            competicao_skate.main()
        elif opc == '3':
            import quiz_corinthians
            quiz_corinthians.main()
        elif opc == '4':
            import catalogo_times_basquete
            catalogo_times_basquete.main()
        elif opc == "0":
            break
        else:
            anim_erro("Opção inválida!")


def submenu_financeiro():
    while True:
        limpar_tela()
        container('--- SUBMENU FINANCEIRO ---')
        digitar('1. Finanças Pessoais')
        digitar('2. Financiamento de Juros')
        digitar('3. impostos de renda')
        digitar('4. Bolsa de Valores')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            import financas_pessoais
            financas_pessoais.main()
        elif opc == '2':
            import financiamento_de_juros
            financiamento_de_juros.main()
        elif opc == '3':
            import ir_simulador
            ir_simulador.main()
        elif opc == '4':
            anim_erro('ESSE CÓDIGO AINDA NÃO FOI IMPLEMENTADO!')
            input(COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")
        elif opc == "0":
            break
        else:
            anim_erro('Opção inválida!')


def submenu_outro():
    while True:
        limpar_tela()
        container('--- SUBMENU OUTRO ---')
        digitar('1. Cátalogo de Filmes')
        digitar('2. Organizador de Tarefas')
        digitar('3. Playlist de Músicas')
        digitar('4. Verfificador de Senha')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            import catalogo_de_filmes
            catalogo_de_filmes.main()
        elif opc == "2":
            import organizador_de_tarefas
            organizador_de_tarefas.main()
        elif opc == '3':
            anim_erro('ESSE CÓDIGO AINDA NÃO FOI FINALIZADO!')
            input(COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")
            #import list_musica
            #list_musica.main()
        elif opc == '4':
            import verificador_senha
            verificador_senha.main()
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')

if __name__ == "__main__":
    menu_principal()
