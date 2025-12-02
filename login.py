"""
Desenvolvido por: Diego Teles
"""

import re
import json
import os
import design
ARQUIVO_USUARIOS = "usuarios.json"


# ---------------------------------------------------------
# Função: carregar_usuarios
# ---------------------------------------------------------
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return {}


# ---------------------------------------------------------
# Função: salvar_usuarios
# ---------------------------------------------------------
def salvar_usuarios(usuarios):
    try:
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Erro ao salvar usuários: {e}")


# ---------------------------------------------------------
# Função: validar_cpf
# ---------------------------------------------------------
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(parcial, peso_inicial):
        soma = 0
        peso = peso_inicial
        for digito in parcial:
            soma += int(digito) * peso
            peso -= 1
        resto = (soma * 10) % 11
        return resto if resto < 10 else 0

    dig1 = calc_digito(cpf[:9], 10)
    dig2 = calc_digito(cpf[:10], 11)

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


# ---------------------------------------------------------
# Carregar usuários
# ---------------------------------------------------------
usuarios = carregar_usuarios()


# ---------------------------------------------------------
# Cadastrar usuário
# ---------------------------------------------------------
def cadastrar_usuario():
    print("\n--- CADASTRAR USUÁRIO ---")
    nome = input("Nome: ").strip()
    cpf_raw = input("CPF (pode usar pontos/traço ou só números): ").strip()

    if not validar_cpf(cpf_raw):
        print("❌ CPF inválido!")
        return

    cpf = re.sub(r'[^0-9]', '', cpf_raw)

    if cpf in usuarios:
        print("❌ Este CPF já está cadastrado!")
        return

    senha = input("Senha: ")

    usuarios[cpf] = {"nome": nome, "senha": senha}
    salvar_usuarios(usuarios)
    print("✔ Usuário cadastrado e salvo com sucesso!")


# ---------------------------------------------------------
# Login
# ---------------------------------------------------------
def login():
    print("\n--- LOGIN ---")
    cpf_raw = input("CPF: ").strip()
    cpf = re.sub(r'[^0-9]', '', cpf_raw)
    senha = input("Senha: ")

    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        print(f"✔ Login bem-sucedido! Bem-vindo, {usuarios[cpf]['nome']}!")
        from menu_principal import main
        main()
    else:
        print("❌ CPF ou senha incorretos.")


# ---------------------------------------------------------
# Menu
# ---------------------------------------------------------
def mostrar_menu():
    print("\n=== SISTEMA DE LOGIN ===")
    print("Desenvolvido por: Diego Teles")  
    print("------------------------------")
    print("[1] Cadastrar usuário")
    print("[2] Login")
    print("[3] Sair")


# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    while True:
        mostrar_menu()
        opc = input("Escolha: ").strip()

        if opc == "1":
            cadastrar_usuario()
        elif opc == "2":
            login()
        elif opc == "3":
            print("Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()

if __name__ == "__main__":

    main()
