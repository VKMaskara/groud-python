'''
Autor do código: Glauber
O objetivo desse programa é:
    - Guardar os gastos em categorias
    - Exibir e auxiliar o usuario
'''

from design import *

def main():
    # Função que garante que o usuário só digite números
    def somente_entrada_numeros(texto):
        while True:
            try:
                # Converte a resposta para float, aceitando vírgula
                resposta = float(pergunta(texto).replace(",", "."))
                break
            except ValueError:
                # Se der erro, avisa e repete
                anim_erro("Dígito inválido! Digite apenas números.")
        return resposta

    # Dicionário que guarda os valores dos gastos do mês
    gastos_mensais = {
        "salario": float(),
        "comida": float(),
        "transporte": float(),
        "lazer": float(),
        "contas": float(),
        "outros": float(),
        "total": float()
    }

    # Dicionário que guarda os percentuais em relação ao salário
    percentual_gastos_mensais = {
        "salario": 100,
        "comida": int(),
        "transporte": int(),
        "lazer": int(),
        "contas": int(),
        "outros": int(),
        "total": int()
    }

    # Variáveis de controle do fluxo do menu
    menu = 0
    pular = False         # usado pra voltar pra opção 1 automaticamente
    tem_cadastro = False  # indica se os gastos já foram preenchidos

    while True:
        # Só mostra o menu principal se pular == False
        if not pular:
            while True:
                limpar_tela()
                titulo_secao("Programa de Cálculo de Finanças Pessoais", animar=False)

                container("1 - Adicionar gastos mensais", animado=False)
                container("2 - Analisar gastos mensais", animado=False)
                container("3 - Sair", animado=False)

                try:
                    menu = int(pergunta("O que deseja fazer?"))
                    
                    # Garante que a opção seja válida
                    if menu not in [1, 2, 3]:
                        anim_erro("Opção inválida!")
                        limpar_tela()
                        continue
                    break
                except ValueError:
                    anim_erro("Dígito inválido! Digite apenas números.")
                    limpar_tela()
                    
        # -------------------------
        # OPÇÃO 1 → Adicionar gastos
        # -------------------------
        while menu == 1:
            limpar_tela()
            titulo_secao("Cálculo de Gastos Mensais", animar=False)

            container("Em relação a esse mês:")
            salario = somente_entrada_numeros("Qual o seu salário?")

            # Garante salário mínimo de 100
            while salario < 100:
                limpar_tela()
                titulo_secao("Cálculo de Gastos Mensais", animar=False)
                container("Em relação a esse mês:", animado=False)
                anim_erro("Insira um valor acima de R$100,00")
                salario = somente_entrada_numeros("Qual o seu salário?")
        
            # Salva tudo no dicionário
            gastos_mensais["salario"] = salario
            gastos_mensais["comida"] = somente_entrada_numeros("Quanto você gastou de comida?")
            gastos_mensais["transporte"] = somente_entrada_numeros("Quanto você gastou de transporte?")
            gastos_mensais["lazer"] = somente_entrada_numeros("Quanto você gastou de lazer?")
            gastos_mensais["contas"] = somente_entrada_numeros("Quanto você gastou com contas?")
            gastos_mensais["outros"] = somente_entrada_numeros("Quanto você gastou com outras despezas?")
            
            # Soma total
            gastos_mensais["total"] = (
                gastos_mensais["comida"] +
                gastos_mensais["transporte"] +
                gastos_mensais["lazer"] +
                gastos_mensais["contas"] +
                gastos_mensais["outros"]
            )

            # Calcula percentuais em relação ao salário
            percentual_gastos_mensais["comida"] = gastos_mensais["comida"] / salario * 100
            percentual_gastos_mensais["transporte"] = gastos_mensais["transporte"] / salario * 100
            percentual_gastos_mensais["lazer"] = gastos_mensais["lazer"] / salario * 100
            percentual_gastos_mensais["contas"] = gastos_mensais["contas"] / salario * 100
            percentual_gastos_mensais["outros"] = gastos_mensais["outros"] / salario * 100
            percentual_gastos_mensais["total"] = gastos_mensais["total"] / salario * 100

            loading("Carregando")
            container("Valores registrados com sucesso!")
            input("Pressione ENTER para voltar...")

            # Volta ao menu principal
            menu = 0
            tem_cadastro = True
            pular = False

        # -------------------------
        # OPÇÃO 2 → Analisar gastos
        # -------------------------
        while menu == 2:
            if tem_cadastro:
                limpar_tela()
                titulo_secao("Análise de Gastos Mensais", animar=False)

                # Exibe todos os valores
                container(f"Gastos Mensais (Salário: {gastos_mensais['salario']:.2f})".replace(".", ","), cor=COR_TITULO)

                container(f"Salário: R${gastos_mensais['salario']:.2f}".replace(".", ","))
                container(f"Gastos com comida: R${gastos_mensais['comida']:.2f}".replace(".", ","))
                container(f"Gastos com transporte: R${gastos_mensais['transporte']:.2f}".replace(".", ","))
                container(f"Gastos com lazer: R${gastos_mensais['lazer']:.2f}".replace(".", ","))
                container(f"Gastos com contas: R${gastos_mensais['contas']:.2f}".replace(".", ","))
                container(f"Gastos com outras despezas: R${gastos_mensais['outros']:.2f}".replace(".", ","))
                container(f"Total dos gastos: R${gastos_mensais['total']:.2f}".replace(".", ","))

                container("Porcentagem Por Categoria (Em relação ao salário)", cor=COR_TITULO)
                container(f"Gastos com comida: {percentual_gastos_mensais['comida']:.0f}%")
                container(f"Gastos com transporte: {percentual_gastos_mensais['transporte']:.0f}%")
                container(f"Gastos com lazer: {percentual_gastos_mensais['lazer']:.0f}%")
                container(f"Gastos com contas: {percentual_gastos_mensais['contas']:.0f}%")
                container(f"Gastos com outras despezas: {percentual_gastos_mensais['outros']:.0f}%")
                container(f"Percentual total: {percentual_gastos_mensais['total']:.0f}%")

                # Análises de situação financeira
                if percentual_gastos_mensais["total"] <= 85:
                    info(COR_SUCESSO + f"Parábens! Você está lidando muito bem com o seu dinheiro. Sobraram: R${gastos_mensais['salario'] - gastos_mensais['total']:.2f}".replace(".", ","))

                elif percentual_gastos_mensais["total"] <= 100:
                    if percentual_gastos_mensais["total"] < 100:
                        info(COR_PERGUNTA + "Fique mais atento com os seus gastos. Você gastou mais de 85% do seu salário")
                    else:
                        info(COR_PERGUNTA + "Você gastou todo o seu salário. Tome cuidado para não exceder seus gastos!")

                else:
                    info(COR_ERRO + "Você gastou mais de 100% do seu salário. Tome cuidado para não se afundar em dívidas.")

                input("Pressione ENTER para voltar...")
                menu = 0

            else:
                # Caso ainda não tenha cadastro de gastos
                limpar_tela()
                titulo_secao("Análise de Gastos Mensais", animar=False)

                info("Você ainda não adicionou nenhum gasto mensal.")
                sim_ou_nao = pergunta_sim_nao("Deseja adicionar gastos?")

                if sim_ou_nao == "S":
                    pular = True
                    menu = 1
                    break
                else:
                    break

        # -------------------------
        # OPÇÃO 3 → Sair do programa
        # -------------------------
        if menu == 3:
            break

if __name__ == "__main__":
    main()