import time
import os

def menu_principal():
    while True:
        print('\n=== MENU PRINCIPAL ===')
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
        print('1. Jogo da Forca')
        print('2. jogo da velha')
        print('3. Pedra, Papel ou Tesoura')
        print("0. Voltar")

        opcão = input('Escolha uma opção: ')

        if opcão == '1':
            print('Jogo da Forca...')
        elif opcão == "2":
            print('Jogo da velha...')
        elif opcão == "3":
            print('Pedra, Papel ou Tesoura...')
        elif opcão == "0":
            break
        else:
            print('Opção inválida!')


def submenu_calculos():
    while True:
        print('\n--- SUBMENU CÁLCULOS ---')
        print('1. Fatorial')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
            print('Fatorial...')
        elif opc == '2':
            print('subtração...')
        elif opc == '3':
            print('multiplicação')
        elif opc == '4':
            print('divisão...')
        elif opc == '0':
            break
        else:
            print('Opção inválida!')


def submenu_esporte():
    while True:
        print('\n--- SUBMENU ESPORTE ---')
        print('1.Truco')
        print('2. Pife')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
            print('Mostrando Truco...')
        elif opc == '2':
            print('Mostrando Pife...')
        elif opc == "0":
            break
        else:
            print("Opção inválida!")


def submenu_financeiro():
    while True:
        print('\n--- SUBMENU FINANCEIRO ---')
        print('1. Tabuada')
        print('2. Calculadora de juros')
        print('0. Voltar')

        opc = input('Escolha uma opção: ')

        if opc == '1':
            print('Convertendo moedas...')
        elif opc == '2':
            print('Calculando juros...')
        elif opc == "0":
            break
        else:
            print('Opção inválida!')


def submenu_outro():
    while True:
        print('\n--- SUBMENU OUTRO ---')
        print('1. Informações gerais')
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


# Executar o menu principal
menu_principal()