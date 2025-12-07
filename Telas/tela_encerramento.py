import caminho_ajuste

import design #importa o arquivo design.py
from design import COR_TITULO, COR_SUCESSO
design.limpar_tela() #função que limpa a tela

#tela encerramento - Samara Soares

def main():
    design.titulo_secao("Obrigado por usar o programa dos Macacos da Programação!") #mensagem de agradecimento ao usuario
    design.titulo_secao("Esperamos que tenha gostado dos nossos serviços!") #mensagem 

    design.container("ETEC ITAPEVI - 2º MÓDULO DE DESENVOLVIMENTO DE SISTEMAS") #mensagem do curso que desenvolveu o programa


    design.container("Cordenadores:", cor=COR_TITULO)
    design.container("-Vitor Kauê")
    design.container("-Glauber Almeida")

    print()

    design.container("Revisores:", cor=COR_TITULO)
    design.container("-Luiz Carlos")
    design.container("-Luis Henrique") 

    print()

    design.container("Design:", cor=COR_TITULO)
    design.container("-Nicolas Breno")

    print()

    design.container("Tela de inicio e encerramento", cor=COR_TITULO)
    design.container("-Samara Soares")

    print()

    design.container("Login:", cor=COR_TITULO)
    design.container("-Diego")

    print()

    design.container("Menu:", cor=COR_TITULO)
    design.container("-Edneuza")

    print()

    design.container("Programas de Jogos:", cor=COR_TITULO)

    design.container("Jogo do 21:", cor=COR_SUCESSO)
    design.container("-Jessé")
    print()
    design.container("Termo:", cor=COR_SUCESSO)
    design.container("-Anna")
    print()
    design.container("Jogo do dado:", cor=COR_SUCESSO)
    design.container("-Renato")

    print()

    design.container("Programas de Cálculos:", cor=COR_TITULO)

    design.container("Folha de pagamento:", cor=COR_SUCESSO)
    design.container("-Gustavo Santos")
    print()
    design.container("Cálculo de área e volume:", cor=COR_SUCESSO)
    design.container("-Gustavo Souza")
    print()
    design.container("Conversor de temperatura:", cor=COR_SUCESSO)
    design.container("-Christian")
    print()
    design.container("Cálculo de combustível:", cor=COR_SUCESSO)
    design.container("-Vinnícius Ribeiro")

    print()

    design.container("Programas de Esportes:", cor=COR_TITULO)

    design.container("Torneio de Skate:", cor=COR_SUCESSO)
    design.container("-Gustavo Valim")
    print()
    design.container("Quiz do Corinthians:", cor=COR_SUCESSO)
    design.container("-Vinícius Oliveira")
    print()
    design.container("IMC de Atletas", cor=COR_SUCESSO)
    design.container("-Thiago")
    print()
    design.container("Catálogo de Basquete:", cor=COR_SUCESSO)
    design.container("-Vinícius de Paula")

    print()

    design.container("Programas Financeiros:", cor=COR_TITULO)

    design.container("Bolsa de valores:", cor=COR_SUCESSO)
    design.container("-Arthur Lima")
    print()
    design.container("Cálculo de imposto:", cor=COR_SUCESSO)
    design.container("-Maycon")
    print()
    design.container("Financiamento de juros simples", cor=COR_SUCESSO)
    design.container("-Mikaelly")

    print()

    design.container("Outros Programas:", cor=COR_TITULO)

    design.container("Avaliação de filmes:", cor=COR_SUCESSO)
    design.container("-Rodrigo")
    print()
    design.container("Verificador de senhas:", cor=COR_SUCESSO)
    design.container("-Juliana")
    print()
    design.container("Organizador de tarefas:", cor=COR_SUCESSO)
    design.container("-Kaique")
    print()
    design.container("Playlist musical:", cor=COR_SUCESSO)
    design.container("-Camilly")

if __name__ == "__main__":
    pass