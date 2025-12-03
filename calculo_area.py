import math

# -------------------------
# Funções de leitura segura
# -------------------------

def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Digite um número inteiro válido.")

def ler_float(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Digite um número válido.")

# -------------------------
# Funções de áreas
# -------------------------

def area_quadrado(lado):
    return lado ** 2

def area_retangulo(lgr, alt):
    return lgr * alt

def area_triangulo(base, alt):
    return (base * alt) / 2

def area_circulo(r):
    return math.pi * (r ** 2)

# -------------------------
# Funções de volumes
# -------------------------

def vol_cubo(lado):
    return lado ** 3

def vol_paralelepipedo(lgr, alt, comprimento):
    return lgr * alt * comprimento

def vol_cilindro(r, alt):
    return math.pi * (r ** 2) * alt

def vol_esfera(r):
    return (4/3) * math.pi * (r ** 3)

# -------------------------
# Função para continuar ou sair
# -------------------------

def deseja_continuar():
    print("\nO que deseja fazer agora?")
    print("1 - Voltar ao menu")
    print("2 - Sair")

    while True:
        opc = ler_int("Escolha --> ")
        if opc == 1:
            return True
        elif opc == 2:
            return False
        else:
            print("Opção inválida! Digite 1 ou 2.")

# -------------------------
# Programa principal
# -------------------------

def main():

    while True:
        print("\n=== Cálculo de Áreas e Volumes ===")
        print("1 - Área do Quadrado")
        print("2 - Área do Retângulo")
        print("3 - Área do Triângulo")
        print("4 - Área do Círculo")
        print("5 - Volume do Cubo")
        print("6 - Volume do Paralelepípedo")
        print("7 - Volume do Cilindro")
        print("8 - Volume da Esfera")
        print("9 - Sair")

        opc = ler_int("Escolha uma opção --> ")

        if opc == 9:
            print("Obrigado por utilizar o Programa de Cálculo de Volume e Área de Formas Geométricas")
            print("Saindo...")
            break

        if opc < 1 or opc > 9:
            print("Opção inválida! Digite um número entre 1 e 9.")
            continue

        # --- Cálculos ---
        if opc == 1:
            lado = ler_float("Lado (cm) --> ")
            print("Área =", area_quadrado(lado), "cm²")

        elif opc == 2:
            lgr = ler_float("Largura (cm) --> ")
            alt = ler_float("Altura (cm) --> ")
            print("Área =", area_retangulo(lgr, alt), "cm²")

        elif opc == 3:
            base = ler_float("Base (cm) --> ")
            alt = ler_float("Altura (cm) --> ")
            print("Área =", area_triangulo(base, alt), "cm²")

        elif opc == 4:
            r = ler_float("Raio (cm) --> ")
            print("Área =", area_circulo(r), "cm²")

        elif opc == 5:
            lado = ler_float("Lado (cm) --> ")
            print("Volume =", vol_cubo(lado), "cm³")

        elif opc == 6:
            lgr = ler_float("Largura (cm) --> ")
            alt = ler_float("Altura (cm) --> ")
            comprimento = ler_float("Comprimento (cm) --> ")
            print("Volume =", vol_paralelepipedo(lgr, alt, comprimento), "cm³")

        elif opc == 7:
            r = ler_float("Raio (cm) --> ")
            alt = ler_float("Altura (cm) --> ")
            print("Volume =", vol_cilindro(r, alt), "cm³")

        elif opc == 8:
            r = ler_float("Raio (cm) --> ")
            print("Volume =", vol_esfera(r), "cm³")

        # ----------------------------
        # Perguntar se deseja continuar
        # ----------------------------
        if not deseja_continuar():
            print("Obrigado por utilizar o Programa de Cálculo de Volume e Área de Formas Geométricas")
            print("Saindo...")
            break


main()
