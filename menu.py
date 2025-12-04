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
        digitar('2. jogo_de_palavras')
        digitar('3. dado')
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
            digitar('divisão...')
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')


def submenu_esporte():
    while True:
        container('--- SUBMENU ESPORTE ---')
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
        container('--- SUBMENU FINANCEIRO ---')
        digitar('1. calculo_financas_pessoais')
        digitar('2. financiamento_de_juros')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            from financas_pessoais import main
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
        container('--- SUBMENU OUTRO ---')
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
