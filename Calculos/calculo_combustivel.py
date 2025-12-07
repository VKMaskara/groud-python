
from design import tela, pergunta, info, anim_sucesso, anim_erro, COR_INFO, COR_TITULO, COR_SUCESSO, COR_ERRO, RESET, limpar_tela
import time
import time

# ------------------- ESTRUTURA DE DADOS -------------------

def main():

    historico_calculos = []

    combustiveis = {
        "gasolina": 0.0,
        "alcool": 0.0
    }

    # ------------------- FUNÇÕES DE VALIDAÇÃO -------------------

    def input_float_validado(msg):
        while True:
            valor = pergunta(msg).strip().replace(",", ".")
            
            if valor.replace(".", "", 1).isdigit():
                num = float(valor)
                if num < 0:
                    print("❌ O valor não pode ser negativo!")
                else:
                    return num
            else:
                print("❌ Entrada inválida! Digite apenas números.")

    def input_float_maior_que_zero(msg):
        while True:
            num = input_float_validado(msg)
            if num == 0:
                print("❌ O valor não pode ser 0!")
            else:
                return num

    # ------------------- FUNÇÃO PRINCIPAL -------------------

    def calcular_custo_combustivel():
        limpar_tela()
        tela("Cálculo de custo do combustível")
        info("Insira os dados para estimar o custo da viagem")

        distancia_viagem = input_float_validado("Digite a distância da viagem em KM")
        consumo_veiculo = input_float_maior_que_zero("Digite o consumo do veículo (KM por litro)")

        combustiveis["gasolina"] = input_float_validado("Digite o preço da gasolina (R$)")
        combustiveis["alcool"] = input_float_validado("Digite o preço do álcool (R$)")

        litros_necessarios = distancia_viagem / consumo_veiculo
        custo_total_gasolina = litros_necessarios * combustiveis["gasolina"]
        custo_total_alcool = litros_necessarios * combustiveis["alcool"]

        historico_calculos.append(f"{distancia_viagem}km | {litros_necessarios:.2f}L | Gas: {custo_total_gasolina:.2f} | Alc: {custo_total_alcool:.2f}")

        print(COR_INFO + "\nResultados calculados, aguarde..." + RESET)
        time.sleep(1)

        limpar_tela()
        tela("Resultado da viagem")

        print(COR_TITULO + "\n===== RESULTADO DA VIAGEM =====" + RESET)
        print(f"Distância informada: {distancia_viagem} KM")
        print(f"Consumo do veículo: {consumo_veiculo} KM/L")
        print(f"Litros necessários: {litros_necessarios:.2f}".replace(".", ",") + " L")

        print(COR_TITULO + "\nCustos:" + RESET)
        print(f"• Gasolina: R$ {custo_total_gasolina:.2f}".replace(".", ","))
        print(f"• Álcool: R$ {custo_total_alcool:.2f}".replace(".", ","))

        percentual = (combustiveis["alcool"] / combustiveis["gasolina"]) * 100
        info(f"OBS: Álcool custa {percentual:.1f}% do valor da gasolina".replace(".", ","))

        if custo_total_alcool <= custo_total_gasolina * 0.7:
            anim_sucesso("Álcool é a melhor opção para essa viagem")
        else:
            anim_sucesso("Gasolina é a melhor opção para essa viagem")

        print(COR_INFO + "\n===== HISTÓRICO =====" + RESET)
        for item in historico_calculos:
            print("→ " + item.replace(".", ","))

        print("\n")
        input("Pressione para continuar...")

    # ------------------- EXECUÇÃO -------------------

    calcular_custo_combustivel()

if __name__ == "__main__":
    main()