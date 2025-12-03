import os
import design
import modulo_imc_

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

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
# ============================================================
# LISTA DE ATLETAS
# ============================================================
atletas = []


# ============================================================
# VALIDAÇÕES
# ============================================================
def validar_nome():
    while True:
        nome = pergunta("Nome do atleta").title()

        if nome == "":
            anim_erro("Nome não pode ser vazio!")
        else:
            return nome


def validar_float(msg):
    while True:
        valor = pergunta(msg)

        try:
            valor = float(valor)
            if valor <= 0:
                anim_erro("O valor deve ser maior que zero!")
            else:
                return valor

        except ValueError:
            anim_erro("Digite um número válido!")


# ============================================================
# CADASTRAR ATLETA
# ============================================================
def cadastrar_atleta():
    tela("CADASTRO DE ATLETA")

    nome = validar_nome()
    peso = validar_float("Peso (kg)")
    altura = validar_float("Altura (m)")

    imc = modulo_imc_.calcular_imc(peso, altura)
    classificacao = modulo_imc_.classificar_imc(imc)

    atleta = {
        "nome": nome,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

    atletas.append(atleta)

    tela("ATLETA CADASTRADO")
    anim_sucesso(f"{nome} cadastrado com sucesso!")

    container(f"IMC: {atleta['imc']} — {atleta['classificacao']}")

    input("\nPressione ENTER para continuar...")


# ============================================================
# LISTAR ATLETAS
# ============================================================
def listar_atletas():
    tela("LISTA DE ATLETAS")

    if len(atletas) == 0:
        anim_erro("Nenhum atleta cadastrado!")
        input("\nPressione ENTER para continuar...")
        return

    for a in atletas:
        container(
            f"Nome: {a['nome']}\n"
            f"Peso: {a['peso']} kg\n"
            f"Altura: {a['altura']} m\n"
            f"IMC: {a['imc']} ({a['classificacao']})"
        )
        print()

    input("Pressione ENTER para continuar...")


# ============================================================
# MENU
# ============================================================
def mostrar_menu():
    titulo_secao("MENU PRINCIPAL", animar=False)

    container("1 - Cadastrar atleta", animado=False)
    container("2 - Listar atletas", animado=False)
    container("3 - Sair", animado=False)

    print()


# ============================================================
# LOOP PRINCIPAL
# ============================================================
while True:
    tela("SISTEMA ESPORTIVO DE IMC")
    mostrar_menu()

    opcao = pergunta("Escolha uma opção")

    if opcao == "1":
        cadastrar_atleta()

    elif opcao == "2":
        listar_atletas()

    elif opcao == "3":
        tela("SAINDO DO SISTEMA")

