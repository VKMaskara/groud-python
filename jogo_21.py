
import os
import time
import sys
import random
import design

# ============================================================
# 🎨 PALETA DE CORES (ANSI)
# ============================================================

RESET = "\033[0m"

COR_TITULO   = "\033[36m"  # Ciano (títulos principais)
COR_PERGUNTA = "\033[33m"  # Amarelo (inputs)
COR_INFO     = "\033[35m"  # Magenta (informações)
COR_SUCESSO  = "\033[32m"  # Verde
COR_ERRO     = "\033[31m"  # Vermelho
COR_BRANCO   = "\033[37m"  # Branco (padrão de containers)


# INICIO DO PROGRAMA 
design.limpar_tela()
design.loading('CARREGANDO')
design.limpar_tela()


design.limpar_tela()
design.titulo_secao('BEM-VINDO A DIVERSÃO DO MEGA 21  😎😎')
design.limpar_tela()
 

design.limpar_tela()
design.titulo_secao('AGUARDE O SEU JOGO DE 21 ESTÁ CARREGANDO 😎😎')
design.limpar_tela()

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
    mostrar_maos(jogador, computador) # Mostra as mãos do jogador e do computador

    if sum(jogador) > 21: # Verifica se o jogador estourou
            print('\n')
            design.anim_erro('VOCÊ PERDEUUUUUUU !!! 🤡🤡')

      
    print('\n')
    escolha = input(COR_PERGUNTA +"\n DESEJA MAIS UMA CARTA ?? (SIM/S) (NÃO/N): " + RESET).lower().strip() # Pergunta ao jogador se quer mais uma carta
    print('\n')
   
  
    if escolha == "s": # Se o jogador escolher 's', pega mais uma carta
            jogador.append(pegar_carta())

     
    elif escolha == "n":
         design.limpar_tela()
         print('OBRIGADO POR JOGAR 21  😎')
         time.sleep(3)
         design.limpar_tela()
         print('ATÉ A PRÓXIMA !!!')
         time.sleep(3)
         design.limpar_tela()
         sys.exit()
       

    elif escolha != "s":
         print(COR_INFO +'POR FAVOR USE (s) PARA CONTINUAR JOGANDO OU (n) PARA ENCERRAR O JOGO' + RESET)
         time.sleep(3.0)
         design.limpar_tela()
         continue
         


    # turno do computadort
    while sum(computador) < 17: # O computador continua pegando cartas enquanto a soma for menor que 17
        computador.append(pegar_carta())
    
    mostrar_maos(jogador, computador, revelar=True) # Mostra as mãos do jogador e do computador, revelando a mão do computador

    total_j = sum(jogador) # Calcula o total do jogador
    total_c = sum(computador) # Calcula o total do computador

    if total_c > 21: # Verifica se o computador estourou
       design.anim_sucesso('VOCÊ GANHOOOOUUUU  😎😎😎!!!!!!!')
     
    elif total_j > total_c: # Verifica quem tem o maior total
        design.anim_sucesso('VOCÊ GANHOOOOUUUU  😎😎😎 !!!!!!!')
        time.sleep(3)
        
        
       
    elif total_j < total_c: # Verifica quem tem o maior total
        design.anim_erro('VOCÊ PERDEUUUU  🤡🤡🤡🤡!!!')
        time.sleep(3)
       
        
        
    else: # Se os totais forem iguais, é um empate
        print( COR_PERGUNTA+"\n🤝 Empate! 🤝🤝🤝🤝🤝" + RESET) 
        continue
     
       
