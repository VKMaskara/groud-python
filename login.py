"""
Desenvolvido por: Diego Teles
"""

# ------------------------------------------------------------
# Importações de módulos do Python e do sistema visual design.py
# ------------------------------------------------------------
import os           # Usado para verificar a existência de arquivos
import json         # Usado para ler e escrever arquivos JSON
import re           # Usado para validar formatos usando expressões regulares
import design       # Importa todo o sistema de design (animações, cores, UI)
from design import (
    titulo_secao, 
    container, 
    pergunta, 
    pergunta_sim_nao, 
    anim_sucesso, 
    anim_erro, 
    info, 
    tela, 
    loading 
)

# Nome do arquivo que armazena os usuários registrados
ARQUIVO_USUARIOS = "usuarios.json"


# ============================================================
# 🔄 Carregar usuários do JSON
# ============================================================
def carregar_usuarios():
    # Se o arquivo não existir, retorna um dicionário vazio
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}

    try:
        # Abre o arquivo JSON em modo leitura
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            # Converte o conteúdo do arquivo JSON para um dicionário Python
            return json.load(arquivo)
    except (IOError, json.JSONDecodeError):
        # Caso ocorra erro ao ler o arquivo, retorna dicionário vazio
        return {}


# ============================================================
# 💾 Salvar usuários
# ============================================================
def salvar_usuarios(usuarios):
    try:
        # Abre o arquivo em modo escrita
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
            # Salva o dicionário no formato JSON
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
    except IOError:
        # Se houver erro ao salvar, exibe animação de erro
        design.anim_erro("Erro ao salvar usuários!")


# ============================================================
# 🆔 Validação de CPF
# ============================================================
def validar_cpf(cpf_raw):
    # Remove tudo que não for número
    cpf = re.sub(r"[^0-9]", "", cpf_raw)

    # Regras básicas: deve ter 11 dígitos e não pode ter todos iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Função interna usada para calcular os dígitos verificadores
    def calcular_digito(parcial, peso_inicial):
        soma = 0
        peso = peso_inicial

        # Para cada dígito do CPF, multiplica pelo peso e soma
        for digito in parcial:
            soma += int(digito) * peso
            peso -= 1

        # Regra matemática do CPF
        resto = (soma * 10) % 11

        # Se resto for maior que 9, retorna 0
        return resto if resto < 10 else 0

    # Calcula os dois dígitos verificadores do CPF
    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    # Retorna True somente se os dígitos conferem
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])


# ============================================================
# 📌 Cadastro de usuário
# ============================================================
def cadastrar_usuario(usuarios):
    # Limpa a tela e exibe título com animação
    design.tela("Cadastrar Usuário")

    # Solicita o nome do usuário com input estilizado
    nome = design.pergunta("Digite seu nome")

    # Solicita o CPF
    cpf_raw = design.pergunta("Digite seu CPF (com ou sem pontuação)")

    # Valida o CPF
    if not validar_cpf(cpf_raw):
        design.anim_erro("CPF inválido!")
        return

    # Converte CPF para apenas números
    cpf = re.sub(r"[^0-9]", "", cpf_raw)

    # Verifica se já existe cadastro com o mesmo CPF
    if cpf in usuarios:
        design.anim_erro("Este CPF já está cadastrado!")
        return

    # Solicita a senha
    senha = design.pergunta("Digite sua senha")

    # Salva nome e senha no dicionário de usuários
    usuarios[cpf] = {"nome": nome, "senha": senha}

    # Salva alterações no arquivo JSON
    salvar_usuarios(usuarios)

    # Exibe mensagem de sucesso animada
    design.anim_sucesso("Usuário cadastrado com sucesso!")


# ============================================================
# 🔐 Login
# ============================================================
def realizar_login(usuarios):
    # Limpa tela e mostra título
    design.tela("Login")

    # Solicita CPF
    cpf_raw = design.pergunta("CPF")

    # Remove caracteres não numéricos
    cpf = re.sub(r"[^0-9]", "", cpf_raw)

    # Solicita senha
    senha = design.pergunta("Senha")

    # Verifica se existe o CPF e se a senha está correta
    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        # Mensagem de boas-vindas
        design.anim_sucesso(f"Bem-vindo, {usuarios[cpf]['nome']}!")

        try:
            # Importa dinamicamente o menu principal
            from menu_principal import main as menu_principal_main
            menu_principal_main()

        except ImportError:
            # Caso o arquivo não exista, avisa o usuário
            design.info("menu_principal.py não encontrado. Login concluído.")
    else:
        # Mensagem de erro caso CPF/senha estejam incorretos
        design.anim_erro("CPF ou senha incorretos!")


# ============================================================
# 📋 Menu Principal do Sistema de Login
# ============================================================
def mostrar_menu():
    # Exibe tela com título
    design.tela("Sistema de Login")

    # Exibe autoria dentro de um container visual
    design.container("Desenvolvido por: Diego Teles", animado=False)
    print()

    # Exibe opções do menu
    print("[1] Cadastrar usuário")
    print("[2] Login")
    print("[3] Sair\n")

    # Retorna a escolha do usuário
    return design.pergunta("Escolha uma opção")


# ============================================================
# ▶️ Programa Principal
# ============================================================
def main():
    # Carrega usuários existentes
    usuarios = carregar_usuarios()

    # Loop do menu principal
    while True:
        opcao = mostrar_menu()

        # Cadastro
        if opcao == "1":
            cadastrar_usuario(usuarios)

        # Login
        elif opcao == "2":
            realizar_login(usuarios)

        # Sair do programa
        elif opcao == "3":
            design.anim_sucesso("Encerrando o programa...")
            break

        # Caso a opção não exista
        else:
            design.anim_erro("Opção inválida!")


# Executa o programa apenas se for o arquivo principal
if __name__ == "__main__":
    main()
