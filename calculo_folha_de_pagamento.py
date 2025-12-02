
#autor: Gustavo Dos Santos Silva

import os
import time

def limpar_tela():
    
    os.system("cls" if os.name == 'nt' else 'clear')

def calcular_inss(salario_bruto):
    
    # Lista de Tuplas: (Valor Limite, Porcentagem)
    tabela_inss = [
        (1518.00, 0.08),
        (2793.89, 0.09),
        (4190.83, 0.12),
        (float('inf'), 0.14) # float('inf') representa qualquer valor acima do anterior
    ]

    for limite, aliquota in tabela_inss:
        if salario_bruto <= limite:
            valor_desconto = salario_bruto * aliquota
            return valor_desconto
            
    return salario_bruto * 0.14 

def calcular_hora_extra(salario_hora, qtd_horas, tipo):
    """Calcula o valor total das horas extras."""
    multiplicador = 0
    
    if tipo == "50%":
        multiplicador = 1.5
    elif tipo == "100%":
        multiplicador = 2.0
    else:
        return 0.0, 0.0 # Retorna 0 se o tipo for inválido

    valor_da_hora = salario_hora * multiplicador
    total_receber = valor_da_hora * qtd_horas
    return valor_da_hora, total_receber

# --- Início do Programa Principal ---
def main():
    limpar_tela()
    print("Bem vindo ao programa de cálculo de folha de pagamento")

    
    salario = float(input("Digite o salário: "))
    carga_horaria = float(input("Digite a carga horária mensal: "))
    
    salario_hora = salario / carga_horaria
    print(f"O salário por hora é de : R$ {salario_hora:.2f}")

    # Processamento de Hora Extra
    hora_extra_qtd = float(input("Digite a quantidade de horas extras trabalhadas no mês: "))
    tipo_hora_extra = str(input("Digite o tipo de hora extra (50% ou 100%): "))

    
    valor_hora_com_acrescimo, total_hora_extra = calcular_hora_extra(salario_hora, hora_extra_qtd, tipo_hora_extra)

    if total_hora_extra > 0:
        print(f"O valor da hora extra ({tipo_hora_extra}) é de : R$ {valor_hora_com_acrescimo:.2f}")
        print(f"Total a receber de horas extras no mês : R$ {total_hora_extra:.2f}")
    else:
        print("Tipo de hora extra inválido ou sem horas trabalhadas.")

    
    calcular_descontos = input("Deseja calcular os descontos do salário? (sim/não): ").strip().lower()

    valetransporte = 0
    valor_inss = 0

    if calcular_descontos == "sim":
        print("Cálculo de descontos selecionado")
        
        # Vale transporte
        valetransporte = salario * 0.06
        time.sleep(1)
        print(f"Valor descontado de Vale transporte: R$ {valetransporte:.2f}")
        
        # INSS (Chamando a função que usa a lista de tuplas)
        valor_inss = calcular_inss(salario)
        time.sleep(1)
        print(f"Valor descontado de INSS: R$ {valor_inss:.2f}")
    else:
        print("Cálculo de descontos ignorado.")

    time.sleep(1)
    
    # Cálculo Final
    salario_liquido = salario + total_hora_extra - valetransporte - valor_inss
    
    print("-" * 30)
    print(f"Salário líquido é de : R$ {salario_liquido:.2f}")
    print("Obrigado por utilizar o programa de cálculo de folha de pagamento")
    time.sleep(2)

# Executa o programa
if __name__ == "__main__":
    main()