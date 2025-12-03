import os
import time
import design


#titulo
print("Este programa serve para auxiliar na sua declaração de imposto de renda.")

#limpar


# Lista de salários
Salario_mensal = []

clt = input("Você trabalhou com carteira assinada este ano (se houve algum mês não trabalho apenas digite 0)? (S/N): ").upper()

#limpar


#carteira assinada
if clt == "S":

    #lista de meses 
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    #loop para a passagem de meses
    for mes in meses:
        while True:
            try:
                salario = float(input(f"Digite o seu salário de {mes}: R$ "))
                Salario_mensal.append(salario)

                #limpar
                
                break
            except ValueError:
                print("❌ Digite apenas números!")

# Exibição dos salários
print("Salários cadastrados com sucesso!\n")

#passa por cada salário mensal
for i, salario in enumerate(Salario_mensal):
    print(f"{meses[i]}: R$ {salario:.2f}")

#mostra o total de salarios
total_sal = sum(Salario_mensal)
print(f"\nTotal anual: R$ {total_sal:.2f}")

#DEPENDENTES

#pergunta se possui dependentes

depen= int(input(f"Possui quantos dependentes? (Se nenhum digite 0): "))

#DESPESAS SIMBÓLICAS



