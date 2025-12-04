import os
import design


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
def main():
      
    atletas = []


    # ============================================================
    # VALIDAÇÕES
    # ============================================================
    def validar_nome():
        while True:
            nome = pergunta("Nome do atleta").strip().title()

            if nome.replace(" ", "").isalpha():
                return nome
            else:
                anim_erro("O nome deve conter apenas letras e espaços!")


    def validar_float(msg, minimo=None, maximo=None):
        while True:
            valor = pergunta(msg).replace(",", ".")  # permite vírgula

            try:
                valor = float(valor)

                if valor <= 0:
                    anim_erro("O valor deve ser maior que zero!")
                    continue

                if minimo is not None and valor < minimo:
                    anim_erro(f"O valor mínimo permitido é {minimo}!")
                    continue

                if maximo is not None and valor > maximo:
                    anim_erro(f"O valor máximo permitido é {maximo}!")
                    continue

                return valor

            except ValueError:
                anim_erro("Digite um número válido!")


    # ============================================================
    # CADASTRAR ATLETA
    # ============================================================
    def cadastrar_atleta():
        tela("CADASTRO DE ATLETA")

        nome = validar_nome()
        peso = validar_float("Peso (kg)", minimo=20, maximo=300)
        altura = validar_float("Altura (m)", minimo=0.5, maximo=2.6)

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

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
        container("2 - Lista de atletas", animado=False)
        container("3 - Sair", animado=False)
        print()


    # ============================================================
    # LOOP PRINCIPAL
    # ============================================================
    while True:
        tela("SISTEMA ESPORTIVO DE IMC")
        mostrar_menu()

        opcao = pergunta("Escolha uma opção")

        # 🔥 Agora o menu valida opções inválidas
        if opcao not in ["1", "2", "3"]:
            anim_erro("Opção inválida! Tente novamente.")
            continue

        if opcao == "1":
            cadastrar_atleta()

        elif opcao == "2":
            listar_atletas()

        elif opcao == "3":
            tela("SAINDO DO SISTEMA")
            break

if __name__ == "__main__":
    main()