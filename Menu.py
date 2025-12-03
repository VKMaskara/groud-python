import time
import os
import design
 

design.limpar_tela()

def menu_principal():
    while True:
        design.titulo_secao('=== MENU PRINCIPAL ===')
        print('1. Jogos')
        print('2. Cálculos')
        print('3. Esporte')
        print('4. Financeiro')
        print('5. Outro')
        print('0. Sair')
        
        
        opcão = input("Escolha uma opção: ")

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
        
            for i in range(3, 0, -1):# Contagem regressiva para a próxima rodada
                print('Saindo em...')
                print(f" {i}")
                time.sleep(3)# Pausa de 1 segundo entre os números da contagem regressiva 
                os.system('cls')   
       
            print("Você saiu do Menu")
            break
        else:
            print('Opção inválida! Tente novamente.')


def submenu_jogos():
    while True:
        print('\n--- SUBMENU JOGOS ---')
        print('1. Jogo do 21')
        print('2. jogo_de_palavras')
        print('3. dado')
        print('4. competição_skate')
        print('4. quiz_corinthians')
        print("0. Voltar")

        opcão = input('Escolha uma opção: ')

        if opcão == '1':
           from jogo_21 import main
           main()
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
            print('Opção inválida!')


def submenu_calculos():
    while True:
        print('\n--- SUBMENU CÁLCULOS ---')
        print('1. calculo_combustivel')
        print('2. modulo_imc')
        print('3. calculo_folha_de_pagamnento' )
        print('4. Divisão')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
          from calculo_combustivel import main
          main()
        elif opc == '2':
          from  modulo_imc import main
          main()
        elif opc == '3':
           from calculo_folha_de_pagamento import main
           main()
        elif opc == '4':
            print('divisão...')
        elif opc == '0':
            break
        else:
            print('Opção inválida!')


def submenu_esporte():
    while True:
        print('\n--- SUBMENU ESPORTE ---')
        print('1.programa_esporte.imc')
        print('2. Pife')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
          from programa_esporte_imc import main
          main()
        elif opc == '2':
            print('Mostrando Pife...')
        elif opc == "0":
            break
        else:
            print("Opção inválida!")


def submenu_financeiro():
    while True:
        print('\n--- SUBMENU FINANCEIRO ---')
        print('1. calculo_financas_pessoais')
        print('2. financiamento_de_juros')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
            from calculo_financas_pessoais import main
            main()
        elif opc == '2':
            from financiamento_de_juros import main
            main()
        elif opc == "0":
            break
        else:
            print('Opção inválida!')


def submenu_outro():
    while True:
        print('\n--- SUBMENU OUTRO ---')
        print('1. ')
        print('2. Configurações')
        print( '0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
            print('Mostrando informações gerais...')
        elif opc == "2":
            print('Abrindo configurações...')
        elif opc == '0':
            break
        else:
            print('Opção inválida!')


