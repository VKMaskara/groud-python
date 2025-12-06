import math                # Biblioteca matemática usada para pi e potências
from design import *       # Biblioteca gráfica/interface do seu projeto


# ============================================================
# LEITURA SEGURA — não permite valores inválidos ou negativos
# ============================================================

def ler_int(mensagem):
    """
    Lê um número inteiro do usuário com tratamento de erros.
    Não permite valores negativos.
    """
    while True:
        try:
            valor = int(pergunta(mensagem))     # Converte entrada para inteiro
            if valor < 0:
                anim_erro("O valor não pode ser negativo.")
                continue
            return valor
        except:
            anim_erro("Digite um número inteiro válido.")


def ler_float(mensagem):
    """
    Lê um número decimal do usuário.
    Aceita vírgula como separador.
    Não permite números menores ou iguais a zero.
    """
    while True:
        try:
            valor = float(pergunta(mensagem).replace(",", "."))
            if valor <= 0:
                anim_erro("A medida deve ser maior que zero.")
                continue
            return valor
        except:
            anim_erro("Digite um número válido.")


# ============================================================
# FORMATAÇÃO DE NÚMEROS
# ============================================================

def formatar(num):
    """
    Arredonda o número para 2 casas decimais
    e troca o ponto por vírgula.
    """
    return f"{num:.2f}".replace(".", ",")


# ============================================================
# CÁLCULOS DE ÁREAS
# ============================================================

def area_quadrado(lado):
    """Calcula a área do quadrado."""
    return lado ** 2

def area_retangulo(largura, altura):
    """Calcula a área do retângulo."""
    return largura * altura

def area_triangulo(base, altura):
    """Calcula a área do triângulo."""
    return (base * altura) / 2

def area_circulo(raio):
    """Calcula a área do círculo."""
    return math.pi * (raio ** 2)


# ============================================================
# CÁLCULOS DE VOLUMES
# ============================================================

def volume_cubo(lado):
    """Volume do cubo."""
    return lado ** 3

def volume_paralelepipedo(largura, altura, comprimento):
    """Volume do paralelepípedo."""
    return largura * altura * comprimento

def volume_cilindro(raio, altura):
    """Volume do cilindro."""
    return math.pi * (raio ** 2) * altura

def volume_esfera(raio):
    """Volume da esfera."""
    return (4/3) * math.pi * (raio ** 3)


# ============================================================
# MENU DE CONTINUAÇÃO
# ============================================================

def deseja_continuar():
    """
    Pergunta ao usuário se deseja voltar ao menu ou sair.
    Valida somente opções 1 e 2.
    """
    print("\nO que deseja fazer agora?")
    container("1 - Voltar ao menu")
    container("2 - Sair")

    while True:
        op = ler_int("Escolha --> ")

        if op == 1:
            return True      # Volta ao menu principal

        if op == 2:
            return False     # Sai do programa

        anim_erro("Opção inválida. Digite 1 ou 2.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    """
    Executa o programa principal.
    Mostra o menu, recebe as opções e chama os cálculos.
    """

    while True:  # Mantém o menu rodando até o usuário sair

        # Mostra o menu principal
        tela("=== Cálculo de Áreas e Volumes ===")
        container("1 - Área do Quadrado")
        container("2 - Área do Retângulo")
        container("3 - Área do Triângulo")
        container("4 - Área do Círculo")
        container("5 - Volume do Cubo")
        container("6 - Volume do Paralelepípedo")
        container("7 - Volume do Cilindro")
        container("8 - Volume da Esfera")
        container("9 - Sair")

        op = ler_int("Escolha uma opção --> ")
        limpar_tela()

        # Opção para sair
        if op == 9:
            info("Obrigado por utilizar o Programa de Cálculo de Volume e Área.")
            loading("Saindo")
            break

        # Validação do menu
        if op < 1 or op > 9:
            anim_erro("Opção inválida! Digite um número entre 1 e 9.")
            continue


        # ============================================================
        # CÁLCULOS
        # ============================================================

        if op == 1:  # Área do quadrado
            lado = ler_float("Lado (cm) --> ")
            resultado = area_quadrado(lado)


        elif op == 2:  # Área do retângulo
            largura = ler_float("Largura (cm) --> ")
            altura = ler_float("Altura (cm) --> ")

            # Retângulo não pode ter lados iguais
            if largura == altura:
                anim_erro("Para ser retângulo, largura e altura devem ser diferentes.")
                continue

            resultado = area_retangulo(largura, altura)


        elif op == 3:  # Área do triângulo
            base = ler_float("Base (cm) --> ")
            altura = ler_float("Altura (cm) --> ")
            resultado = area_triangulo(base, altura)


        elif op == 4:  # Área do círculo
            raio = ler_float("Raio (cm) --> ")
            resultado = area_circulo(raio)


        elif op == 5:  # Volume do cubo
            lado = ler_float("Lado (cm) --> ")
            resultado = volume_cubo(lado)


        elif op == 6:  # Volume do paralelepípedo
            largura = ler_float("Largura (cm) --> ")
            altura = ler_float("Altura (cm) --> ")
            comprimento = ler_float("Comprimento (cm) --> ")

            # Não pode ter 3 lados iguais
            if largura == altura == comprimento:
                anim_erro("As três medidas não podem ser iguais em um paralelepípedo.")
                continue

            resultado = volume_paralelepipedo(largura, altura, comprimento)


        elif op == 7:  # Volume do cilindro
            raio = ler_float("Raio (cm) --> ")
            altura = ler_float("Altura (cm) --> ")
            resultado = volume_cilindro(raio, altura)


        elif op == 8:  # Volume da esfera
            raio = ler_float("Raio (cm) --> ")
            resultado = volume_esfera(raio)


        # ============================================================
        # EXIBIÇÃO DO RESULTADO FORMATADO
        # ============================================================
        print("\nResultado =", formatar(resultado))


        # ============================================================
        # PERGUNTA SE DESEJA CONTINUAR
        # ============================================================
        if not deseja_continuar():
            info("Obrigado por utilizar o Programa de Cálculo.")
            loading("Saindo")
            break


# Executa o programa principal
main()
