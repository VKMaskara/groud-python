
import os 
import design  # importa o módulo de design gráfico do programa

# importa funções específicas do módulo design para facilitar o uso
from design import (
    titulo_secao,      # mostra um título estilizado na tela
    container,         # exibe um bloco de texto estilizado
    pergunta,          # faz uma pergunta ao usuário
    pergunta_sim_nao,  # faz pergunta de sim/não
    anim_sucesso,      # animação de sucesso
    anim_erro,         # animação de erro
    info,              # exibe informações
    tela,              # limpa e configura uma nova tela
    loading            # animação de carregamento
)

# função para calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)  # fórmula padrão do IMC

# função para classificar o IMC do atleta
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"  # classificação por IMC
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


# ============================================================
# LISTA DE ATLETAS
# ============================================================
def main():  # função principal do sistema
      
    atletas = []  # lista onde todos os atletas serão armazenados


    # ============================================================
    # VALIDAÇÕES
    # ============================================================
    def validar_nome():  # validação de nome
        while True:  # loop até o usuário digitar corretamente
            nome = pergunta("Nome do atleta").strip().title()  # pergunta + formatação

            if nome.replace(" ", "").isalpha():  # verifica se só tem letras
                return nome  # nome válido
            else:
                anim_erro("O nome deve conter apenas letras e espaços!")  # erro


    def validar_float(msg, minimo=None, maximo=None):  # valida números (peso/altura)
        while True:
            valor = pergunta(msg).replace(",", ".")  # troca vírgula por ponto

            try:
                valor = float(valor)  # tenta converter para número

                if valor <= 0:  # valor não pode ser menor ou igual a zero
                    anim_erro("O valor deve ser maior que zero!")
                    continue

                if minimo is not None and valor < minimo:  # verifica mínimo
                    anim_erro(f"O valor mínimo permitido é {minimo}!")
                    continue

                if maximo is not None and valor > maximo:  # verifica máximo
                    anim_erro(f"O valor máximo permitido é {maximo}!")
                    continue

                return valor  # valor válido

            except ValueError:  # caso não seja número
                anim_erro("Digite um número válido!")  # erro


    # ============================================================
    # CADASTRAR ATLETA
    # ============================================================
    def cadastrar_atleta():  # função para cadastrar atleta
        tela("CADASTRO DE ATLETA")  # limpa tela e mostra título

        nome = validar_nome()  # recebe nome validado
        peso = validar_float("Peso (kg)", minimo=20, maximo=300)  # peso válido
        altura = validar_float("Altura (m)", minimo=0.5, maximo=2.6)  # altura válida

        imc = calcular_imc(peso, altura)  # calcula o IMC
        classificacao = classificar_imc(imc)  # classifica o IMC

        atleta = {  # dicionário com os dados do atleta
            "nome": nome,
            "peso": peso,
            "altura": altura,
            "imc": round(imc, 2),  # IMC com 2 casas decimais
            "classificacao": classificacao
        }

        atletas.append(atleta)  # adiciona o atleta na lista

        tela("ATLETA CADASTRADO")  # mostra nova tela
        anim_sucesso(f"{nome} cadastrado com sucesso!")  # mensagem de sucesso

        container(f"IMC: {atleta['imc']} — {atleta['classificacao']}")  # exibe resumo

        input("\nPressione ENTER para continuar...")  # pausa


    # ============================================================
    # LISTAR ATLETAS
    # ============================================================
    def listar_atletas():  # função para listar todos os atletas
        tela("LISTA DE ATLETAS")  # nova tela

        if len(atletas) == 0:  # verifica se não há atletas
            anim_erro("Nenhum atleta cadastrado!")  # erro
            input("\nPressione ENTER para continuar...")
            return  # volta ao menu

        for a in atletas:  # percorre a lista de atletas
            container(
                f"Nome: {a['nome']}\n"
                f"Peso: {a['peso']} kg\n"
                f"Altura: {a['altura']} m\n"
                f"IMC: {a['imc']} ({a['classificacao']})"
            )
            print()  # linha em branco

        input("Pressione ENTER para continuar...")  # pausa


    # ============================================================
    # MENU
    # ============================================================
    def mostrar_menu():  # mostra as opções do menu principal
        titulo_secao("MENU PRINCIPAL", animar=False)  # título

        container("1 - Cadastrar atleta", animado=False)  # opção 1
        container("2 - Lista de atletas", animado=False)  # opção 2
        container("3 - Sair", animado=False)  # opção 3
        print()  # espaço


    # ============================================================
    # LOOP PRINCIPAL
    # ============================================================
    while True:  # loop infinito (até escolher sair)
        tela("SISTEMA ESPORTIVO DE IMC")  # título da tela
        mostrar_menu()  # exibe o menu

        opcao = pergunta("Escolha uma opção")  # lê opção

        if opcao not in ["1", "2", "3"]:  # valida opção
            anim_erro("Opção inválida! Tente novamente.")  # erro
            continue  # volta ao menu

        if opcao == "1":  # cadastrar atleta
            cadastrar_atleta()

        elif opcao == "2":  # listar atletas
            listar_atletas()

        elif opcao == "3":  # sair
            tela("SAINDO DO SISTEMA")  # animação
            break  # encerra loop principal

        input(design.COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")  # pausa


# executa o programa somente se rodado diretamente
if __name__ == "__main__":
    main()  # chama a função principal
