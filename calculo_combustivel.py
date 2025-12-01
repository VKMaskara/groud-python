from design import tela, pergunta, info, anim_sucesso, anim_erro, COR_INFO, COR_TITULO, COR_SUCESSO, COR_ERRO, RESET, limpar_tela
# importa as funções de interface, cores e animações do design 

import time  # importa biblioteca Python para usar pausas

# ------------------- ESTRUTURA DE DADOS -------------------

historico_calculos = []  # lista para armazenar histórico de viagens 

combustiveis = {  # dicionário com tipos de combustível e preços
    "gasolina": 0.0,  # valor inicial do preço da gasolina
    "alcool": 0.0     # valor inicial do preço do álcool
}

# ------------------- FUNÇÃO PRINCIPAL -------------------

def calcular_custo_combustivel():  # função começa com verbo de ação e está em snake_case
    tela("Cálculo de custo do combustível")  # chama a tela com título centralizado (design)
    
    info("Insira os dados para estimar o custo da viagem")  # exibe mensagem informativa

    distancia_viagem = float(pergunta("Digite a distância da viagem em KM").strip())  
    # coleta distância e aplica strip() para remover espaços

    consumo_veiculo = float(pergunta("Digite o consumo do veículo (KM por litro)").strip())  
    # coleta consumo e aplica strip()

    combustiveis["gasolina"] = float(pergunta("Digite o preço da gasolina (R$)").strip())
    # coleta preço gasolina, aplica strip(), salva no dicionário

    combustiveis["alcool"] = float(pergunta("Digite o preço do álcool (R$)").strip())
    # coleta preço álcool, aplica strip(), salva no dicionário

    litros_necessarios = distancia_viagem / consumo_veiculo
    # calcula total gasto em litros

    custo_total_gasolina = litros_necessarios * combustiveis["gasolina"]
    # calcula custo total da gasolina

    custo_total_alcool = litros_necessarios * combustiveis["alcool"]
    # calcula custo total do álcool

    historico_calculos.append(f"{distancia_viagem}km | {litros_necessarios:.2f}L | Gas: {custo_total_gasolina:.2f} | Alc: {custo_total_alcool:.2f}")
    # adiciona o resultado do cálculo na lista de histórico como string

    print(COR_INFO + "\nResultados calculados, aguarde..." + RESET)  # imprime mensagem com cor do design
    time.sleep(1)  # pausa usando biblioteca time
    
    tela("Resultado da viagem")   
     
    print(COR_TITULO + "\n===== RESULTADO DA VIAGEM =====" + RESET)  # imprime cabeçalho com cor do design

    print(f"Distância informada: {distancia_viagem} KM")  
    # exibe a distância informada

    print(f"Consumo do veículo: {consumo_veiculo} KM/L")  
    # exibe o consumo do veículo

    print(f"Litros necessários: {litros_necessarios:.2f} L")  
    # exibe litros necessários formatado

    print(COR_TITULO + "\nCustos:" + RESET)  # imprime seção de custos

    print(f"• Gasolina: R$ {custo_total_gasolina:.2f}")  
    # exibe custo gasolina com prefixo moeda

    print(f"• Álcool: R$ {custo_total_alcool:.2f}")  
    # exibe custo álcool

    if custo_total_alcool <= custo_total_gasolina * 0.7:  
        # condição para verificar se o álcool compensa 
        anim_sucesso("Álcool é a melhor opção para essa viagem")  
        # chama animação de sucesso do design se o álcool compensar
    else:  
        # caso a gasolina compense mais
        anim_erro("Gasolina é a melhor opção para essa viagem")  
        # chama animação de erro do design se a gasolina compensar 

    print(COR_INFO + "\n===== HISTÓRICO =====" + RESET)  # imprime título do histórico

    for item in historico_calculos:  # percorre a lista do histórico
        print("→ " + item)  # imprime cada item do histórico

    print("\n")  # pula linha no final para organização visual

# ------------------- EXECUÇÃO DO PROGRAMA -------------------

calcular_custo_combustivel()  
# chama a função principal para executar o programa 