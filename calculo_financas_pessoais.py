'''
Glauber
O objetivo desse programa é:
    - Guardar os gastos em categorias
    - Exibir e auxiliar o usuario
'''


from design import *

def somente_entrada_numeros(texto):
    while True:
        try:
            resposta = float(pergunta(texto).replace(",", "."))
            break
        except ValueError:
            anim_erro("Dígito inválido! Digite apenas números.")
    return resposta

gastos_mensais = {
    "salario": float(),
    "comida": float(),
    "transporte": float(),
    "lazer": float(),
    "contas": float(),
    "outros": float(),
    "total": float()
    }

percentual_gastos_mensais = {
    "salario": 100,
    "comida": int(),
    "transporte": int(),
    "lazer": int(),
    "contas": int(),
    "outros": int(),
    "total": int()
}

menu = 0

while True:
    while True:
        limpar_tela()
        titulo_secao("Programa de Cálculo de Finanças Pessoais", animar=False)

        container("1 - Calcular gastos mensais", animado=False)
        container("2 - Analisar gastos mensais", animado=False)
        container("3 - Sair", animado=False)

        try:
            menu = int(pergunta("O que deseja fazer?"))
            
            if menu not in [1,2,3]:
                limpar_tela()
                anim_erro("Opção inválida!")
                continue
            break
        except ValueError:
            limpar_tela()
            anim_erro("Dígito inválido! Digite apenas números.")

    while menu == 1:
        limpar_tela()
        titulo_secao("Cálculo de Gastos Mensais", animar=False)

        container("Em relação a esse mês:")
        gastos_mensais["salario"] = somente_entrada_numeros("Qual o seu salário?")
        gastos_mensais["comida"] = somente_entrada_numeros("Quanto você gastou de comida?")
        gastos_mensais["transporte"] = somente_entrada_numeros("Quanto você gastou de transporte?")
        gastos_mensais["lazer"] = somente_entrada_numeros("Quanto você gastou de lazer?")
        gastos_mensais["contas"] = somente_entrada_numeros("Quanto você gastou com contas?")
        gastos_mensais["outros"] = somente_entrada_numeros("Quanto você gastou com outras coisas?")
        
        gastos_mensais["total"] = gastos_mensais["comida"] + gastos_mensais["transporte"] + gastos_mensais["lazer"] + gastos_mensais["contas"] + gastos_mensais["outros"]
        loading("Carregando")
        container("Valores registrados com sucesso!")
        input("Pressione ENTER para voltar...")
        menu = 0

        percentual_gastos_mensais["comida"] = gastos_mensais["comida"] / gastos_mensais["salario"] * 100    
        percentual_gastos_mensais["transporte"] = gastos_mensais["transporte"] / gastos_mensais["salario"] * 100
        percentual_gastos_mensais["lazer"] = gastos_mensais["lazer"] / gastos_mensais["salario"] * 100
        percentual_gastos_mensais["contas"] = gastos_mensais["contas"] / gastos_mensais["salario"] * 100
        percentual_gastos_mensais["outros"] = gastos_mensais["outros"] / gastos_mensais["salario"] * 100
        percentual_gastos_mensais["total"] = gastos_mensais["total"] / gastos_mensais["salario"] * 100

    while menu == 2:
        limpar_tela()
        titulo_secao("Análise de Gastos Mensais", animar=False)

        container("Gastos Mensais", cor=COR_TITULO)
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

        if percentual_gastos_mensais["total"] <= 85:
            info(COR_SUCESSO + f"Parábens! Você está lidando muito bem com o seu dinheiro. Sobraram: R${gastos_mensais['total'] - gastos_mensais['salario']:.2f}".replace(".", ","))
        if percentual_gastos_mensais["total"] > 85 and percentual_gastos_mensais["total"] <= 100:
            if percentual_gastos_mensais["total"] < 100:
                info(COR_PERGUNTA + "Fique mais atento com os seus gastos. Você gastou mais de 85% do seu salário")
            else:
                info(COR_PERGUNTA + "Você gastou todo o seu salário. Tome cuidado para não exceder seus gastos!")
        else:
            info(COR_ERRO + "Você gastou mais de 100% do seu salário. Tome cuidado para não se afundar em dívidas.")

        input("Pressione ENTER para voltar...")
        menu = 0

    if menu == 3:
        break