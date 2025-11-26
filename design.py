# ============================================================
# design.py — Sistema Oficial de Visual, Animações e Layout
# ============================================================
# Este módulo define:
#   • Paleta de cores ANSI (sem bibliotecas externas)
#   • Funções de animação (digitação, loading, sucesso, erro)
#   • Funções padronizadas de input
#   • Sistema de títulos centralizados para qualquer módulo
#   • Containers e seções com bordas
#   • Tela padrão com transição
# ============================================================

import os
import time
import platform
import shutil
import sys


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


# ============================================================
# 🎞️ FUNÇÕES DE ANIMAÇÃO
# ============================================================

def digitar(texto, velocidade=0.015):
    """Efeito de digitação estilo máquina de escrever."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()


def loading(texto="Carregando", ciclos=3, tempo=0.45):
    """Animação simples de carregamento."""
    for _ in range(ciclos):
        for pontos in [" .  ", " .. ", " ..."]:
            print(f"{texto}{pontos}", end="\r", flush=True)
            time.sleep(tempo)
    print(" " * 30, end="\r")  # limpa linha


def anim_sucesso(msg):
    """Mensagem de sucesso animada."""
    for i in range(3):
        print(COR_SUCESSO + f"[✓] {msg}" + "." * i + RESET, end="\r")
        time.sleep(0.25)
    print(COR_SUCESSO + f"[✓] {msg}" + RESET)


def anim_erro(msg):
    """Mensagem de erro com piscada."""
    for _ in range(2):
        print(COR_ERRO + f"[X] {msg}" + RESET, end="\r")
        time.sleep(0.25)
        print(" " * (len(msg) + 5), end="\r")
        time.sleep(0.25)
    print(COR_ERRO + f"[X] {msg}" + RESET)


# ============================================================
# 🧹 LIMPAR TELA
# ============================================================

def limpar_tela():
    """Limpa a tela em qualquer sistema operacional."""
    os.system("cls" if platform.system() == "Windows" else "clear")


# ============================================================
# 🏷️ TÍTULO CENTRALIZADO (FUNÇÃO PRINCIPAL DO SISTEMA)
# ============================================================

def titulo_secao(texto, cor=COR_TITULO, animar=True):
    """
    Exibe um título grande, centralizado, com bordas,
    que pode ser importado em qualquer arquivo do projeto.
    """
    largura = shutil.get_terminal_size().columns
    texto_formatado = f" {texto.upper()} "
    linha = "═" * len(texto_formatado)

    def digitar_linha(l):
        for c in l:
            print(c, end="", flush=True)
            time.sleep(0.004)
        print()

    print()

    if animar:
        digitar_linha(cor + linha.center(largura) + RESET)
        digitar_linha(cor + texto_formatado.center(largura) + RESET)
        digitar_linha(cor + linha.center(largura) + RESET)
    else:
        print(cor + linha.center(largura) + RESET)
        print(cor + texto_formatado.center(largura) + RESET)
        print(cor + linha.center(largura) + RESET)

    print()


# ============================================================
# 📦 CONTAINERS VISUAIS
# ============================================================

def container(texto, cor=COR_BRANCO, animado=True):
    """Cria uma caixa visual estilosa com bordas."""
    largura = len(texto) + 4
    topo = cor + "┌" + "─" * largura + "┐" + RESET
    meio = cor + f"│  {texto}  │" + RESET
    baixo = cor + "└" + "─" * largura + "┘" + RESET

    if animado:
        digitar(topo, 0.002)
        digitar(meio, 0.002)
        digitar(baixo, 0.002)
    else:
        print(topo)
        print(meio)
        print(baixo)


# ============================================================
# 🟡 INPUTS PADRONIZADOS
# ============================================================

def pergunta(texto):
    """Input estilizado com cor + digitação."""
    digitar(COR_PERGUNTA + f"{texto}:" + RESET, 0.01)
    return input("> ").strip()


def pergunta_sim_nao(texto):
    """Input S/N padronizado."""
    while True:
        digitar(COR_PERGUNTA + f"{texto} (S/N):" + RESET, 0.01)
        resposta = input("> ").strip().upper()

        if resposta in ("S", "N"):
            return resposta
        digitar("Entrada inválida! Digite apenas 'S' ou 'N'.\n", 0.01)



# ============================================================
# 📨 MENSAGENS INFORMATIVAS
# ============================================================

def info(msg):
    digitar(COR_INFO + f"[i] {msg}" + RESET, 0.01)


# ============================================================
# 🖥️ TELA PADRÃO (com transição)
# ============================================================

def tela(titulo_texto):
    """Limpa a tela e abre uma nova seção com animação."""
    limpar_tela()
    titulo_secao(titulo_texto)
