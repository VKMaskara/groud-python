import os
import time
import sys
import random
import design

# ============================================================
# 🎨 PALETA DE CORES (ANSI)
# ============================================================

RESET = "\033[0m"

COR_TITULO   = "\033[36m"
COR_PERGUNTA = "\033[33m"
COR_INFO     = "\033[35m"
COR_SUCESSO  = "\033[32m"
COR_ERRO     = "\033[31m"
COR_BRANCO   = "\033[37m"


# ============================================================
# FUNÇÕES BÁSICAS
# ============================================================


def pegar_carta():
    return random.randint(1, 11)

def mostrar_maos(jogador, computador, revelar=False):
    print(f"\nSua mão: {jogador}  (total: {sum(jogador)})")

    if revelar:
        print(f"Mão do sistema: {computador}  (total: {sum(computador)})")
    else:
        print(f"Mão do sistema: [{computador[0]}, '?']")


# ============================================================
# INTELIGÊNCIA DO COMPUTADOR
# ============================================================

def turno_do_computador(mao_computador, total_jogador):
    """
    Estrategia:
    - Se o jogador estourou, o computador não joga.
    - Se total do computador < 16 → comprar.
    - Se total do computador < total do jogador → comprar.
    - Se total do computador ≥ total do jogador → parar.
    """

    while True:
        total_c = sum(mao_computador)

        # Se já passou do jogador, ele para
        if total_c >= total_jogador and total_c >= 16:
            break

        # Compra carta
        mao_computador.append(pegar_carta())

        # Se estourou, para também
        if sum(mao_computador) > 21:
            break

    return mao_computador


# ============================================================
# INTRODUÇÃO DO JOGO
# ============================================================

design.limpar_tela()
design.titulo_secao("BEM-VINDO AO MEGA 21 😎😎")
time.sleep(1)

design.limpar_tela()
design.tela("CARREGANDO SEU JOGO... 😎")
time.sleep(2)
design.limpar_tela()


# ============================================================
# SISTEMA DE APOSTAS
# ============================================================

saldo = 500  # saldo inicial

while True:

    design.limpar_tela()
    print(COR_TITULO + f"SALDO ATUAL: R$ {saldo}" + RESET)

    # Entrada da aposta
    while True:
        try:
            aposta = int(input(COR_PERGUNTA + "\nQuanto deseja apostar? R$: " + RESET))

            if aposta <= 0:
                print(COR_ERRO + "A aposta deve ser maior que 0!" + RESET)
                continue

            if aposta > saldo:
                print(COR_ERRO + "Você não tem saldo suficiente!" + RESET)
                continue

            break
        except:
            print(COR_ERRO + "Digite um valor válido!" + RESET)

    # ============================================================
    # INÍCIO DA RODADA
    # ============================================================

    jogador = [pegar_carta(), pegar_carta()]
    computador = [pegar_carta(), pegar_carta()]

    # TURNO DO JOGADOR
    while True:
        design.limpar_tela()
        print(COR_TITULO + f"SALDO: R$ {saldo} | APOSTA: R$ {aposta}" + RESET)
        mostrar_maos(jogador, computador)

        # Estouros
        if sum(jogador) > 21:
            design.anim_erro("VOCÊ ESTOUROU!!! 🤡🤡")
            saldo -= aposta
            break

        escolha = input(COR_PERGUNTA + "\nDeseja mais uma carta? (S/N): " + RESET).lower().strip()

        if escolha in ("s", "sim"):
            jogador.append(pegar_carta())
            continue

        elif escolha in ("n", "nao", "não"):
            break

        else:
            print(COR_INFO + "Use S para continuar ou N para parar." + RESET)
            time.sleep(1)

    # TURNO DO COMPUTADOR
    if sum(jogador) <= 21:
        computador = turno_do_computador(computador, sum(jogador))

        design.limpar_tela()
        mostrar_maos(jogador, computador, revelar=True)
        time.sleep(1)

        total_j = sum(jogador)
        total_c = sum(computador)

        # RESULTADOS
        if total_c > 21:
            design.anim_sucesso("O SISTEMA ESTOUROU — VOCÊ GANHOU! 😎")
            saldo += aposta

        elif total_j > total_c:
            design.anim_sucesso("VOCÊ GANHOU!! 😎😎")
            saldo += aposta

        elif total_j < total_c:
            design.anim_erro("VOCÊ PERDEU!!! 🤡🤡")
            saldo -= aposta

        else:
            print(COR_INFO + "\n🤝 Empate! A aposta foi devolvida." + RESET)
            time.sleep(2)

    # ============================================================
    # ENCERRAMENTO OU NOVA RODADA
    # ============================================================

    if saldo <= 0:
        design.anim_erro("VOCÊ FICOU SEM DINHEIRO!!! 🤡")
        time.sleep(2)
        break

    jogar_novamente = input(COR_PERGUNTA + "\nDeseja jogar novamente? (S/N): " + RESET).lower().strip()

    if jogar_novamente not in ("s", "sim"):
        design.limpar_tela()
        print(COR_SUCESSO + f"VOCÊ SAIU COM R$ {saldo}. OBRIGADO POR JOGAR! 😎" + RESET)
        time.sleep(2)
        design.limpar_tela()
        break
