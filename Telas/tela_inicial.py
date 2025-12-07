import caminho_ajuste


import design #importa o arquivo design.py
import time #importa a biblioteca time para usar a função sleep
design.limpar_tela()

#tela inicial - Samara Soares

design.titulo_secao("Seja muito bem vindo ao programa dos Macacos da Programação!") #mensagem inicial que irá aparecer para o usuario
design.titulo_secao("Aqui você vai encontrar jogos, cálculos, esportes, financeiro e muito mais!") #mensagem explicando o programa

design.container("ETEC ITAPEVI - 2º MÓDULO DE DESENVOLVIMENTO DE SISTEMAS") #mensagem do curso que desenvolveu o programa

design.container("Toque a tecla ENTER para continuar") #texto instruindo o usuario a continuar
(input()) #usuario digita enter para continuar

design.limpar_tela() #função que limpa a tela

from login import main #importa a tela de login
main() #função que leva para a tela de login

