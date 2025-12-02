import random 
import time
import os
import sys


# DEFINDOS AS FUNÇÕES DO PROGRAMA

def limpar_tela(): # Função para limpar a tela
    os.system('cls')
    

def tem():
     time.sleep(3)

def tempo():
    time.sleep(2.1)


def Menu(): # Função para exibir o menu inicial
    print(100*('-'))
    print('BEM-VINDO AO JOGO '.center(100))
    print(100*('-'))
    tempo()
    limpar_tela()
    print("\nIniciando o jogo...")
    tempo()
    limpar_tela()
    print("\nBoa sorte!")
    tempo()
    limpar_tela()

def fim():
    print('\n')
    print('OBRIGADO POR JOGAR O 21 ')
    time.sleep(3)
    limpar_tela()
    print('\n')
    print('ATÉ A PRÓXIMA !!! 😎😎 ')
    time.sleep(3)
    limpar_tela()
    print('\n')
    print('PROGRAMA ENCERANDO ............')
    time.sleep(3)
    limpar_tela()
     


# INICIO DO PROGRAMA 


limpar_tela()

def pegar_carta(): # Função para pegar uma carta aleatória entre 1 e 11
    return random.randint(1, 11) # Retorna um número aleatório entre 1 e 11

def mostrar_maos(jogador, computador, revelar=False): # Função para mostrar as mãos do usuário e do computador
    print(f"\nmão do usuário: {jogador} (total: {sum(jogador)})") # Mostra a mão do usuario e o total
    if revelar: # Se revelar for True, mostra a mão completa do computador
        print(f"Mão do sistema: {computador} (total: {sum(computador)})") # Mostra a mão do computador e o total
    else:
        print(f"Mão do sistema: [{computador[0]}, ? ]") # Mostra apenas a primeira carta do computador



        
jogador = [pegar_carta(), pegar_carta()] # Mão inicial do jogador com duas cartas
computador = [pegar_carta(), pegar_carta()] # Mão inicial do computador com duas cartas

while True: # Loop principal do jogo
    Menu() # CHAMANDO A FUNÇÃO DA TELA INICIAL 
    mostrar_maos(jogador, computador) # Mostra as mãos do jogador e do computador

    if sum(jogador) > 21: # Verifica se o jogador estourou
            print('\n')
            print("\n Você estourou! Perdeu. 🤡🤡 ")
        
 
    escolha = input("\n DESEJA MAIS UMA CARTA ?? (s/n): ").lower().strip() # Pergunta ao jogador se quer mais uma carta
    limpar_tela()

    if escolha == "s": # Se o jogador escolher 's', pega mais uma carta
            jogador.append(pegar_carta())

     
    elif escolha == "n":
         fim()
         sys.exit()
       
       
 
    elif escolha != "s":
         print('POR FAVOR USE (s) PARA CONTINUAR JOGANDO OU (n) PARA ENCERRAR O JOGO')
         tem()
         limpar_tela()
         continue
         


    

    # turno do computadort
    while sum(computador) < 17: # O computador continua pegando cartas enquanto a soma for menor que 17
        computador.append(pegar_carta())
    
    mostrar_maos(jogador, computador, revelar=True) # Mostra as mãos do jogador e do computador, revelando a mão do computador

    total_j = sum(jogador) # Calcula o total do jogador
    total_c = sum(computador) # Calcula o total do computador

    if total_c > 21: # Verifica se o computador estourou
        print(" O computador estourou!,  Você venceu! 😝😝😝😝😝😝😝😝")
        tem()
        limpar_tela()
    elif total_j > total_c: # Verifica quem tem o maior total
        print("\n🎉 Você venceu! 🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩")
        tem()
        limpar_tela()
    elif total_j < total_c: # Verifica quem tem o maior total
        print("\n❌ Você perdeu! 🤡🤡🤡🤡🤡🤡🤡🤡")
        tem()
        limpar_tela()
    else: # Se os totais forem iguais, é um empate
        print("\n🤝 Empate! 😎😎😎😎😎 ")
        tem()
        limpar_tela()
       