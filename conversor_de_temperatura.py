import os
import time
import design
import locale  # Importando o módulo locale


# Configura a localidade para o Brasil (onde usamos vírgula como separador decimal)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

os.system('cls')

def C_F(C):
    return (C * 9/5) + 32

def C_K(C):
    return C + 273.15

def F_C(F):
    return (F - 32) * 5/9

def F_K(F):
    return (F - 32) * 5/9 + 273.15

def K_C(K):
    return K - 273.15

def K_F(K):
    return (K - 273.15) * 9/5 + 32


def escolher_unidade(mensagem):
    """Força a pessoa a escolher apenas C, F ou K"""
    while True:
        unidade = input(design.COR_PERGUNTA + mensagem).strip().upper()
        if unidade in ["C", "F", "K"]:
            return unidade
        else:
            print(design.COR_INFO + "\nOpção inválida! Digite apenas C, F ou K.\n")


def ler_temperatura(mensagem):
    """Garante que a pessoa digite apenas valores numéricos, aceitando vírgula."""
    while True:
        valor = input(design.COR_PERGUNTA + mensagem).strip()

        # Troca vírgula por ponto antes de tentar converter
        valor = valor.replace(",", ".")

        try:
            return float(valor)
        except ValueError:
            print(design.COR_INFO + "\nValor inválido! Digite apenas números.\n")


print(design.COR_SUCESSO + 'Obrigado por utilizar meu código. Vamos lá!!👍')
time.sleep(2)
os.system('cls')

def main():
    #  LOOP PRINCIPAL
    while True:

        # apresentação do código
        design.titulo_secao(
            'Esse código converte as unidades de medida das temperaturas. Ex: Celsius → Fahrenheit ou Kelvin.',
            design.COR_TITULO
        )

        # escolha do usuário
        escolha1 = escolher_unidade('\nEscolha a temperatura que você deseja converter -> (C), (F) ou (K) ? : ')
        escolha2 = escolher_unidade('\nEm qual você quer transformar -> (C), (F) ou (K) ? : ')

        time.sleep(1)
        os.system('cls')

        # Entrada de temperatura (VALIDADA)
        temperatura1 = ler_temperatura(f'\nLegal, vamos lá! Quantos graus {escolha1} você quer converter para {escolha2}? : ')

        # Processamento das conversões e exibição com vírgula
        if escolha1 == 'C' and escolha2 == 'F':
            resultado = C_F(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °F')

        elif escolha1 == 'C' and escolha2 == 'K':
            resultado = C_K(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °K')

        elif escolha1 == 'F' and escolha2 == 'C':
            resultado = F_C(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °C')

        elif escolha1 == 'F' and escolha2 == 'K':
            resultado = F_K(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °K')

        elif escolha1 == 'K' and escolha2 == 'C':
            resultado = K_C(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °C')

        elif escolha1 == 'K' and escolha2 == 'F':
            resultado = K_F(temperatura1)
            print(design.COR_SUCESSO + f'\nResultado: {locale.format_string("%.2f", resultado)} °F')

        else:
            print(design.COR_INFO + '\nAs unidades são iguais! Nada para converter.')

        #  Pergunta se quer repetir – AGORA VALIDADA CORRETAMENTE
        while True:
            repetir = input(design.COR_PERGUNTA + "\nDeseja fazer outra conversão? (S/N): ").strip().upper()
            if repetir in ["S", "N"]:
                break
            print(design.COR_INFO + "\nOpção inválida! Digite apenas S ou N.\n")

        if repetir == "N":
            break

        os.system('cls')  # limpa a tela para reiniciar o loop


    print(design.COR_SUCESSO + '\nObrigado por usar o conversor de temperaturas!!! 😊')
    input(design.COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")

if __name__ == "__main__":
    main()