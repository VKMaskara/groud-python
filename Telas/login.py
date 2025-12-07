import caminho_ajuste
# ============================================================
# Importações
# ============================================================
import os
import json
import re
import design
from design import tela, pergunta, pergunta_sim_nao, anim_sucesso, anim_erro, info, container

ARQUIVO_USUARIOS = "usuarios.json"  # Arquivo de armazenamento

# ============================================================2
# Funções auxiliares
# ============================================================

def carregar_usuarios():
    """Carrega usuários do JSON, retorna dicionário vazio se não existir ou erro."""
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return {}

def salvar_usuarios(usuarios):
    """Salva dicionário de usuários no JSON."""
    try:
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
    except IOError:
        anim_erro("Erro ao salvar usuários!")

def validar_nome(nome):
    """Valida se o nome contém apenas letras e espaços (sem números)."""
    nome = nome.strip()
    if any(c.isdigit() for c in nome):
        return False
    return bool(re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", nome))

def validar_cpf(cpf_raw):
    """Valida CPF (11 dígitos, dígitos verificadores corretos)."""
    cpf = re.sub(r"[^0-9]", "", cpf_raw)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    def calc(parcial, peso):
        soma = sum(int(d) * (peso - i) for i, d in enumerate(parcial))
        dig = (soma * 10) % 11
        return dig if dig < 10 else 0
    return cpf[-2:] == f"{calc(cpf[:9], 10)}{calc(cpf[:10], 11)}"

def confirmar_voltar(acao="continuar"):
    """
    Pergunta ao usuário se quer prosseguir ou voltar.
    Retorna True se deseja continuar, False se deseja voltar.
    """
    resposta = pergunta_sim_nao(f"Deseja {acao}?")
    if resposta == "N":
        info("Retornando à tela anterior...")
        return False
    return True

# ============================================================
# Cadastro de usuário
# ============================================================

def cadastrar_usuario(usuarios):
    """Realiza o cadastro de um novo usuário com opção de voltar."""
    tela("Cadastrar Usuário")

    while True:
        nome = pergunta("Digite seu nome")
        if not validar_nome(nome):
            anim_erro("Nome inválido! Use apenas letras e espaços.")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break

    while True:
        cpf_raw = pergunta("Digite seu CPF (com ou sem pontuação)")
        if not validar_cpf(cpf_raw):
            anim_erro("CPF inválido!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        cpf = re.sub(r"[^0-9]", "", cpf_raw)
        if cpf in usuarios:
            anim_erro("Já existe um cadastro com este CPF!")
            if not confirmar_voltar("tentar outro CPF"):
                return
            continue
        break

    senha = pergunta("Digite sua senha")
    pergunta_sec = pergunta("Digite sua pergunta secreta para recuperação")
    resposta_sec = pergunta("Digite a resposta da pergunta secreta").lower().strip()

    usuarios[cpf] = {
        "nome": nome,
        "senha": senha,
        "pergunta": pergunta_sec,
        "resposta": resposta_sec,
        "tentativas": 0,
        "bloqueado": False
    }

    salvar_usuarios(usuarios)
    anim_sucesso("Usuário cadastrado com sucesso!")

# ============================================================
# Troca de senha
# ============================================================

def trocar_senha(usuarios, cpf):
    tela("Trocar Senha")
    while True:
        senha_atual = pergunta("Digite sua senha atual")
        if senha_atual != usuarios[cpf]["senha"]:
            anim_erro("Senha incorreta!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break
    while True:
        nova = pergunta("Digite sua nova senha")
        confirmar = pergunta("Confirme a nova senha")
        if nova != confirmar:
            anim_erro("As senhas não coincidem!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break
    usuarios[cpf]["senha"] = nova
    salvar_usuarios(usuarios)
    anim_sucesso("Senha alterada com sucesso!")

# ============================================================
# Excluir conta
# ============================================================

def excluir_conta(usuarios, cpf):
    tela("Excluir Conta")
    if pergunta_sim_nao("Tem certeza que deseja excluir sua conta?") == "S":
        del usuarios[cpf]
        salvar_usuarios(usuarios)
        anim_sucesso("Conta excluída com sucesso!")
        return True
    else:
        info("Operação cancelada.")
        return False

# ============================================================
# Recuperação de senha
# ============================================================

def recuperar_senha(usuarios):
    tela("Recuperar Senha")
    while True:
        cpf_raw = pergunta("Digite seu CPF")
        cpf = re.sub(r"[^0-9]", "", cpf_raw)
        if cpf not in usuarios:
            anim_erro("CPF não encontrado!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break
    usuario = usuarios[cpf]
    info(f"Pergunta secreta: {usuario['pergunta']}")
    resposta = pergunta("Resposta").lower().strip()
    if resposta != usuario["resposta"]:
        anim_erro("Resposta incorreta!")
        return
    while True:
        nova = pergunta("Digite sua nova senha")
        confirmar = pergunta("Confirme a nova senha")
        if nova != confirmar:
            anim_erro("As senhas não coincidem!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break
    usuario["senha"] = nova
    usuario["tentativas"] = 0
    usuario["bloqueado"] = False
    salvar_usuarios(usuarios)
    anim_sucesso("Senha redefinida com sucesso!")

# ============================================================
# Login
# ============================================================

def fazer_login(usuarios):
    tela("Login")
    while True:
        cpf_raw = pergunta("Digite seu CPF")
        cpf = re.sub(r"[^0-9]", "", cpf_raw)
        if cpf not in usuarios:
            anim_erro("CPF não encontrado!")
            if not confirmar_voltar("tentar novamente"):
                return
            continue
        break
    usuario = usuarios[cpf]
    if usuario["bloqueado"]:
        anim_erro("Conta bloqueada!")
        info("Use a recuperação de senha para desbloquear.")
        return
    while True:
        senha = pergunta("Digite sua senha")
        if senha == usuario["senha"]:
            usuario["tentativas"] = 0
            salvar_usuarios(usuarios)
            anim_sucesso(f"Bem-vindo(a), {usuario['nome']}!")

            # Redirecionamento pós-login
            try:
                from Telas import menu
                menu.menu_principal()
            except ImportError:
                print("menu.py não encontrado!")
            return

        usuario["tentativas"] += 1
        salvar_usuarios(usuarios)

        if usuario["tentativas"] >= 3:
            usuario["bloqueado"] = True
            salvar_usuarios(usuarios)
            anim_erro("Conta BLOQUEADA!")
            info("Use a recuperação de senha para desbloquear.")
            return

        anim_erro(f"Senha incorreta! Tentativas: {usuario['tentativas']}/3")
        if not confirmar_voltar("tentar novamente"):
            return

# ============================================================
# Menu principal do sistema
# ============================================================

def mostrar_menu():
    tela("Sistema de Login")
    container("Desenvolvido por: Diego Teles", animado=False)
    print()
    print("[1] Fazer login")
    print("[2] Cadastrar usuário")
    print("[3] Recuperar senha")
    print("[4] Sair\n")
    return pergunta("Escolha uma opção")

# ============================================================
# Programa principal
# ============================================================

def main():
    usuarios = carregar_usuarios()
    while True:
        opcao = mostrar_menu()
        if opcao == "1":
            fazer_login(usuarios)
        elif opcao == "2":
            cadastrar_usuario(usuarios)
        elif opcao == "3":
            recuperar_senha(usuarios)
        elif opcao == "4":
            anim_sucesso("Encerrando o sistema...")
            break
        else:
            anim_erro("Opção inválida!")

# ============================================================
# Executa apenas se for o arquivo principal
# ============================================================

if __name__ == "__main__":
    main()
