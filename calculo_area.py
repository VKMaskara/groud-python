import math # Biblioteca matemática para constantes e funções matemáticas
from design import * # Importa funções de design para melhorar a interface do usuário

# -------------------------
# Funções de leitura segura
# -------------------------

def ler_int(mensagem): # Função para ler um número inteiro com tratamento de erro
    while True:
        try:
            return int(pergunta(mensagem))
        except:
            anim_erro("Digite um número inteiro válido.")

def ler_float(mensagem): # Função para ler um número float com tratamento de erro
    while True:
        try:
            return float(pergunta(mensagem).replace(",", "."))
        except:
            anim_erro("Digite um número válido.")

# -------------------------
# Funções de áreas
# -------------------------

def area_quadrado(lado): # Calcula a área do quadrado
    return lado ** 2

def area_retangulo(largura, altura): # Calcula a área do retângulo
    return largura * altura

def area_triangulo(base, altura):  # Calcula a área do triângulo
    return (base * altura) / 2

def area_circulo(raio): # Calcula a área do círculo
    return math.pi * (raio ** 2)

# -------------------------
# Funções de volumes
# -------------------------

def volume_cubo(lado): # Calcula o volume do cubo
    return lado ** 3

def volume_paralelepipedo(largura, altura, comprimento): # Calcula o volume do paralelepípedo
    return largura * altura * comprimento

def volume_cilindro(raio, altura): # Calcula o volume do cilindro
    return math.pi * (raio ** 2) * altura

def volume_esfera(raio): # Calcula o volume da esfera
    return (4/3) * math.pi * (raio ** 3)

# -------------------------
# Função para continuar ou sair
# -------------------------

def deseja_continuar(): # Pergunta ao usuário se deseja continuar ou sair
    print("\nO que deseja fazer agora?")
    container("1 - Voltar ao menu")
    container("2 - Sair")

    while True: 
        opicao = ler_int("Escolha --> ")
        if opicao == 1:
            return True
        elif opicao == 2:
            return False
        else:
            print("Opção inválida! Digite 1 ou 2.")
            limpar_tela()

# -------------------------
# Programa principal
# -------------------------

def main(): # Função principal do programa

    while True:
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
        
        opicao = ler_int("Escolha uma opção --> ") # Lê a opção do usuário

        limpar_tela()

        if opicao == 9: # Sair do programa
            info("Obrigado por utilizar o Programa de Cálculo de Volume e Área de Formas Geométricas")
            loading("Saindo")
            break

        if opicao < 1 or opicao > 9: # Opção inválida
            print("Opção inválida! Digite um número entre 1 e 9.")
            continue

        # --- Cálculos ---
        if opicao == 1: # Área do quadrado
            lado = ler_float("Lado (cm) --> ")
            print("Área =", area_quadrado(lado), "cm²")

        elif opicao == 2: # Área do retângulo
            largura = ler_float("Largura (cm) --> ")
            altura = ler_float("alturaura (cm) --> ")
            print("Área =", area_retangulo(largura, altura), "cm²")

        elif opicao == 3: # Área do triângulo
            base = ler_float("Base (cm) --> ")
            altura = ler_float("alturaura (cm) --> ")
            print("Área =", area_triangulo(base, altura), "cm²")

        elif opicao == 4:
            raio = ler_float("Raio (cm) --> ")
            print("Área =", area_circulo(raio), "cm²")

        elif opicao == 5: # Volume do cubo
            lado = ler_float("Lado (cm) --> ")
            print("Volume =", volume_cubo
        (lado), "cm³")

        elif opicao == 6: # Volume do paralelepípedo
            largura = ler_float("Largura (cm) --> ")
            altura = ler_float("alturaura (cm) --> ")
            comprimento = ler_float("Comprimento (cm) --> ")
            print("Volume =", volume_cilindro(largura, altura, comprimento), "cm³")

        elif opicao == 7: # Volume do cilindro
            raio = ler_float("Raio (cm) --> ")
            altura = ler_float("alturaura (cm) --> ")
            print("Volume =", volume_cilindro(raio, altura), "cm³")

        elif opicao == 8: # Volume da esfera
            raio = ler_float("Raio (cm) --> ")
            print("Volume =", volume_esfera(raio), "cm³")


        # ----------------------------
        # Perguntar se deseja continuar
        # ----------------------------
        if not deseja_continuar(): # Se o usuário não deseja continuar
            info("Obrigado por utilizar o Programa de Cálculo de Volume e Área de Formas Geométricas")
            loading("Saindo")
            break


main()
