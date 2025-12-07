
import time
import design

def get_nonempty_string(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        design.anim_erro("Entrada inválida — por favor digite um valor não vazio.")

def get_float(prompt, min_value=None, allow_zero=True):
    while True:
        try:
            raw = input(prompt).replace(",", ".").strip()
            val = float(raw)
            if min_value is not None:
                if allow_zero:
                    if val < min_value:
                        design.anim_erro(f"Valor inválido — digite um número >= {min_value}.")
                        continue
                else:
                    if val <= min_value:
                        design.anim_erro(f"Valor inválido — digite um número > {min_value}.")
                        continue
            return val
        except ValueError:
            design.anim_erro("Entrada inválida — por favor digite um número válido.")
def get_yes_no(prompt):
    while True:
        r = input(prompt).strip().lower()
        if r in ("s", "n"):
            return r
        design.anim_erro("Resposta inválida — digite 's' para sim ou 'n' para não.")

nome = []  # tabela para armazenar o nome do colaborador
design.limpar_tela()
nome.append(get_nonempty_string("DIGITE O NOME DO COLABORADOR: "))

def main():  # função principal do sistema de cálculo de folha de pagamento
    design.limpar_tela()  # limpa a tela antes de iniciar o cálculo
    design.titulo_secao("Cálculo de Folha de Pagamento", animar=True)
    design.loading("Iniciando o sistema", ciclos=3, tempo=0.5)
    time.sleep(1)
    print(design.COR_TITULO + "Olá ,", nome[0], "bem vindo ao programa de cálculo de folha de pagamento" + design.RESET)
    print("-" * 50)  # Linha decorativa
    # Entradas principais
    salario = get_float("Digite o salário bruto: R$: ", min_value=0.0, allow_zero=False)  # pede ao usuário o salário bruto
    carga_horaria = get_float("Digite a carga horária mensal (ex: 220): ", min_value=0.0, allow_zero=False)  # pede ao usuário a carga horária mensal
    # Cálculo do salário por hora
    salario_hora = salario / carga_horaria  # calcula o salário por hora
    print(f"O salário por hora é de: R$ {salario_hora:.2f}")
    # Inicializando variável para evitar erro no cálculo final
    total_hora_extra = 0.0
    # Cálculo de Horas Extras
    hora_extra_100 = get_float("\nDigite a quantidade de horas extras trabalhadas em folgas/feriados no mês: ", min_value=0.0, allow_zero=True)
    hora_extra_50 = get_float("Digite a quantidade de horas extras trabalhadas em dias úteis no mês: ", min_value=0.0, allow_zero=True)  # pede ao usuário a quantidade de horas extras trabalhadas em dias uteis
    if hora_extra_50 > 0:
        valor_hora_extra_50 = salario_hora * 1.5  # calcula o valor da hora extra com adicional de 50%
        total_hora_extra_50 = valor_hora_extra_50 * hora_extra_50  # calcula o total de horas extras com adicional de 50%
        print(f"O valor da hora extra (50%) é: R$ {valor_hora_extra_50:.2f}")
        total_hora_extra += total_hora_extra_50  # acumula o total de horas extras
    if hora_extra_100 > 0:
        valor_hora_extra_100 = salario_hora * 2  # calcula o valor da hora extra com adicional de 100%
        total_hora_extra_100 = valor_hora_extra_100 * hora_extra_100  # calcula o total de horas extras com adicional de 100%
        print(f"O valor da hora extra (100%) é: R$ {valor_hora_extra_100:.2f}")
        total_hora_extra += total_hora_extra_100  # acumula o total de horas extras

    print(design.COR_SUCESSO + f"Total geral a receber de horas extras: R$ {total_hora_extra:.2f}" + design.RESET)
    # Inicializando variáveis de desconto
    valetransporte = 0.0  # inicializa o vale transporte
    inss = 0.0  # inicializa o INSS
    total_descontos = 0.0  # inicializa o total de descontos
    # Cálculo de Descontos
    print("-" * 50)
    calcular_desc = get_yes_no(design.COR_PERGUNTA + "Deseja calcular os descontos do salário? (s/n): " + design.RESET)
    if calcular_desc == "s":
        design.loading("Cálculo de desconto selecionado", ciclos=2, tempo=0.5)
        time.sleep(1)
        # Vale transporte
        valetransporte = salario * 0.06
        print(f"Valor descontado de Vale Transporte (6%): R$ {valetransporte:.2f}")
        time.sleep(1)
        # INSS - Tabela 2025
        if salario <= 1518:
            inss = salario * 0.08
        elif salario <= 2793.89:
            inss = salario * 0.09
        elif salario <= 4190.83:
            inss = salario * 0.12
        else:
            inss = salario * 0.14
        print(f"Valor descontado de INSS: R$ {inss:.2f}")
        time.sleep(1)
    total_descontos = valetransporte + inss
    design.limpar_tela()
    design.titulo_secao("Calculando o salário líquido", animar=True)
    time.sleep(1)
    # Cálculo Final
    salario_liquido = salario + total_hora_extra - valetransporte - inss
    print("-" * 50)
    print(f"RESUMO DA FOLHA DE PAGAMENTO DE {nome[0].upper()}:")
    print(f"Salário Bruto: R$   {salario:.2f}")
    print(f"Total de Horas Extras: R$   {total_hora_extra:.2f}")
    print(design.COR_ERRO + f"Total de Descontos: R$   {total_descontos:.2f}" + design.RESET)
    print(design.COR_SUCESSO + f"Salário Líquido a Receber: R$   {salario_liquido:.2f}" + design.RESET)
    design.loading("Finalizando o sistema", ciclos=3, tempo=0.5)
    design.titulo_secao("Obrigado por utilizar o sistema de cálculo de folha de pagamento", animar=True)

    time.sleep(1)


if __name__ == "__main__":
    main()
