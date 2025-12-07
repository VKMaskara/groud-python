import caminho_ajuste

from design import *
import sys
 


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
            import Telas.tela_encerramento
            Telas.tela_encerramento.main()

            sys.exit()
        else:
            anim_erro('Opção inválida! Tente novamente.')


def submenu_jogos():
    while True:
        limpar_tela()
        container('--- SUBMENU JOGOS ---')
        digitar('1. Jogo do 21')
        digitar('2. Jogo de Palavras')
        digitar('3. Jogo do Dado')
        digitar("0. Voltar")

        opcão = pergunta('Escolha uma opção: ')

        if opcão == '1':
           import Jogos.jogo_21
           Jogos.jogo_21.main()
        elif opcão == '2':
            import Jogos.jogo_de_palavras
            Jogos.jogo_de_palavras.main()
        elif opcão == '3':
            import Jogos.jogo_dados
            Jogos.jogo_dados.main()   
        elif opcão == "0":
            break
        else:
            anim_erro('Opção inválida!')


def submenu_calculos():
    while True:
        limpar_tela()   
        container('--- SUBMENU CÁLCULOS ---')
        digitar('1. Cálculo de Combustível')
        digitar('2. Conversor de Temperatura')
        digitar('3. Cálculo de Folha de Pagamento' )
        digitar('4. Cálculo de Área')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
          import Calculos.calculo_combustivel
          Calculos.calculo_combustivel.main()
        elif opc == '2':
          import Calculos.conversor_de_temperatura
          Calculos.conversor_de_temperatura.main()
        elif opc == '3':
            import Calculos.calculo_folha_de_pagamento
            Calculos.calculo_folha_de_pagamento.main()
        elif opc == '4':
            import Calculos.calculo_area
            Calculos.calculo_area.main()
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
          import Esportes.programa_atleta_imc
          Esportes.programa_atleta_imc.main()
        elif opc == '2':
            import Esportes.competicao_skate
            Esportes.competicao_skate.main()
        elif opc == '3':
            import Esportes.quiz_corinthians as quiz_corinthians
            quiz_corinthians.main()
        elif opc == '4':
            import Esportes.catalogo_times_basquete
            Esportes.catalogo_times_basquete.main()
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
        digitar('3. Impostos de Renda')
        digitar('4. Bolsa de Valores')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            import Financeiro.financas_pessoais
            Financeiro.financas_pessoais.main()
        elif opc == '2':
            import Financeiro.financiamento_de_juros
            Financeiro.financiamento_de_juros.main()
        elif opc == '3':
            import Financeiro.imposto_de_renda
            Financeiro.imposto_de_renda.main()
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
        digitar('4. Verificador de Senha')
        digitar('0. Voltar')

        opc = pergunta('Escolha uma opção: ')

        if opc == '1':
            import Outros.catalogo_de_filmes
            Outros.catalogo_de_filmes.menu_principal()
        elif opc == "2":
            import Outros.organizador_de_tarefas
            Outros.organizador_de_tarefas.main()
        elif opc == '3':
            anim_erro('ESSE CÓDIGO AINDA NÃO FOI FINALIZADO!')
            input(COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")
            #import list_musica
            #list_musica.main()
        elif opc == '4':
            import Outros.verificador_senha
            Outros.verificador_senha.main()
        elif opc == '0':
            break
        else:
            anim_erro('Opção inválida!')

if __name__ == "__main__":
    menu_principal()
