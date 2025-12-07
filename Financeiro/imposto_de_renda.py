
# ir_simulador.py
import math
import design

def calcular_imposto_anual(base_calculo: float) -> float:
    """Calcula imposto devido com a tabela anual simplificada."""
    if base_calculo <= 22599.00:
        return 0.0
    elif base_calculo <= 33919.80:
        return (base_calculo - 22599.00) * 0.075
    elif base_calculo <= 45012.60:
        return (33919.80 - 22599.00) * 0.075 + (base_calculo - 33919.80) * 0.15
    elif base_calculo <= 55976.16:
        return (
            (33919.80 - 22599.00) * 0.075 +
            (45012.60 - 33919.80) * 0.15 +
            (base_calculo - 45012.60) * 0.225
        )
    else:
        return (
            (33919.80 - 22599.00) * 0.075 +
            (45012.60 - 33919.80) * 0.15 +
            (55976.16 - 45012.60) * 0.225 +
            (base_calculo - 55976.16) * 0.275
        )

def main():
    while True:
        design.tela("Simulador IR — Auxílio")
        design.titulo_secao("Simulador de Imposto de Renda", animar=False)

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        design.digitar("Este programa serve para auxiliar na sua declaração de imposto de renda.\n")

        # LISTA DE SALÁRIOS
        salarios = []

        clt = design.pergunta_sim_nao("Você trabalhou com carteira assinada este ano (se houve algum mês sem trabalho apenas digite 0)?")
        if clt == "S":
            for mes in meses:
                while True:
                    try:
                        resposta = design.pergunta(f"Digite o seu salário bruto do mês de {mes} (apenas números)")
                        salario = float(resposta.replace(",", "."))
                        salarios.append(salario)
                        break
                    except ValueError:
                        design.anim_erro("Digite apenas números! Tente novamente.")

        if salarios:
            design.anim_sucesso("Salários cadastrados com sucesso!")
            for i, s in enumerate(salarios):
                print(f"{meses[i]}: R$ {s:.2f}")
        else:
            design.info("Nenhum salário informado (não houve CLT).")

        total_sal = sum(salarios)
        print(f"\nTotal anual: R$ {total_sal:.2f}")

        # DEPENDENTES (validação)
        while True:
            resp = design.pergunta("Possui quantos dependentes? (Se nenhum digite 0)")
            try:
                depen = int(resp)
                if depen < 0:
                    design.anim_erro("Digite um número válido (0 ou mais).")
                    continue
                break
            except ValueError:
                design.anim_erro("Digite apenas números!")

        deducao_dependentes = depen * 2275.08  # valor anual por dependente

        # DESPESAS EDUCAÇÃO (S/N/? com return após ?)
        while True:
            despesas_educ = design.pergunta("Possui alguma despesa com educação que é dedutível? (S/N/?)").upper()
            if despesas_educ == "?":
                print("\nDedutíveis:")
                print("- Creche e pré-escola")
                print("- Ensino fundamental")
                print("- Ensino médio")
                print("- Pós-graduação")
                print("- Educação profissional / técnico")
                print("- EJA (Educação de Jovens e Adultos)")
                input("\nPressione ENTER para continuar...")
                continue
            if despesas_educ in ("S", "N"):
                break
            design.anim_erro("Digite apenas 'S', 'N' ou '?'.")

        if despesas_educ == "S":
            while True:
                try:
                    valor_educ = float(design.pergunta("Qual o valor total? (Limite anual por pessoa: R$ 3.561,50)").replace(",", "."))
                    valor_educ_dedutivel = min(valor_educ, 3561.50)
                    break
                except ValueError:
                    design.anim_erro("Digite apenas números!")
        else:
            valor_educ_dedutivel = 0.0

        # DESPESAS SAÚDE (S/N/? com return após ?)
        while True:
            despesas_saude = design.pergunta("Possui alguma despesa com saúde que é dedutível? (S/N/?)").upper()
            if despesas_saude == "?":
                print("\nDedutíveis em saúde:")
                print("- Consultas médicas")
                print("- Dentista / ortodontia")
                print("- Psicólogo, fisioterapeuta, fonoaudiólogo, terapeuta ocupacional")
                print("- Exames laboratoriais")
                print("- Internações em hospitais e clínicas")
                print("- Cirurgias (inclui plásticas necessárias)")
                print("- Planos e seguros de saúde")
                print("- Próteses, aparelhos ortopédicos e similares")
                input("\nPressione ENTER para continuar...")
                continue
            if despesas_saude in ("S", "N"):
                break
            design.anim_erro("Digite apenas 'S', 'N' ou '?'.")

        if despesas_saude == "S":
            while True:
                try:
                    valor_saude = float(design.pergunta("Qual o valor total?").replace(",", "."))
                    valor_saude_dedutivel = valor_saude
                    break
                except ValueError:
                    design.anim_erro("Digite apenas números!")
        else:
            valor_saude_dedutivel = 0.0

        # IMPOSTO JÁ DESCONTADO NA FONTE
        fonte = design.pergunta_sim_nao("Alguma parte do imposto já foi descontada direto do seu salário?")
        if fonte == "S":
            while True:
                try:
                    imposto_pago = float(design.pergunta("Aproximadamente quanto já foi descontado no ano? R$").replace(",", "."))
                    break
                except ValueError:
                    design.anim_erro("Digite apenas números!")
        else:
            imposto_pago = 0.0

        # CALCULOS
        deducoes_totais = deducao_dependentes + valor_educ_dedutivel + valor_saude_dedutivel
        base_calculo = total_sal - deducoes_totais
        if base_calculo < 0:
            base_calculo = 0.0

        imposto_devido = calcular_imposto_anual(base_calculo)
        diferenca = imposto_devido - imposto_pago

        # MOSTRAR RESUMO
        design.tela("Resumo")
        design.container("Resumo da Simulação", animado=False)
        print(f"Renda anual total: R$ {total_sal:.2f}")
        print(f"Deduções aplicadas: R$ {deducoes_totais:.2f}")
        print(f"Base de cálculo: R$ {base_calculo:.2f}")
        print(f"Imposto devido: R$ {imposto_devido:.2f}")
        print(f"Imposto já pago: R$ {imposto_pago:.2f}\n")

        if diferenca > 0:
            design.anim_erro(f"Você ainda deve pagar: R$ {diferenca:.2f}")
        elif diferenca < 0:
            design.anim_sucesso(f"Você tem restituição: R$ {abs(diferenca):.2f}")
        else:
            design.info("Situação zerada / isento!")

        # REPETE SIMULAÇÃO
        repetir = design.pergunta_sim_nao("Deseja fazer outra simulação?")
        if repetir == "N":
            design.anim_sucesso("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()