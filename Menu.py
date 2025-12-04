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
        digitar('\n--- SUBMENU JOGOS ---')
        digitar('1. Jogo do 21')
        digitar('2. jogo_de_palavras')
        digitar('3. dado')
        digitar('4. competição_skate')
        digitar('4. quiz_corinthians')
        digitar("0. Voltar")

        opcão = pergunta('Escolha uma opção: ')

        if opcão == '1':
           import jogo_21
           jogo_21.main()
        elif opcão == '2':
            from jogo_de_palavras import main
            main()
        elif opcão == '3':
            from dado import main
            main()
        elif opcão == '4':
            from competição_skate import main
            main()
        elif opcão == '4':
            from quiz_corinthians import main
            main()
        elif opcão == "0":
            break
        else:
            anim_erro('Opção inválida!')


def submenu_calculos():
    while True:
        digitar('\n--- SUBMENU CÁLCULOS ---')
        digitar('1. calculo_combustivel')
        digitar('2. Conversor de temperatura')
        digitar('3. calculo_folha_de_pagamnento' )
        digitar('4. Divisão')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
          import calculo_combustivel
          calculo_combustivel.main()
        elif opc == '2':
          import conversor_de_medidas
          conversor_de_medidas.main()
        elif opc == '3':
            import calculo_folha_de_pagamento
            calculo_folha_de_pagamento.main()
        elif opc == '4':
            digitar('divisão...')
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')


def submenu_esporte():
    while True:
        digitar('\n--- SUBMENU ESPORTE ---')
        digitar('1. IMC de Atletas')
        digitar('2. Pife')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
          import programa_atleta_imc
          programa_atleta_imc.main()
        elif opc == '2':
            digitar('Mostrando Pife...')
        elif opc == "0":
            break
        else:
            anim_erro("Opção inválida!")


def submenu_financeiro():
    while True:
        digitar('\n--- SUBMENU FINANCEIRO ---')
        digitar('1. calculo_financas_pessoais')
        digitar('2. financiamento_de_juros')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            from calculo_financas_pessoais import main
            main()
        elif opc == '2':
            from financiamento_de_juros import main
            main()
        elif opc == "0":
            break
        else:
            anim_erro('Opção inválida!')


def submenu_outro():
    while True:
        digitar('\n--- SUBMENU OUTRO ---')
        digitar('1. ')
        digitar('2. Configurações')
        digitar( '0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            digitar('Mostrando informações gerais...')
        elif opc == "2":
            digitar('Abrindo configurações...')
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')

if __name__ == "__main__":
    menu_principal()
