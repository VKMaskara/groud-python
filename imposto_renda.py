import os
import time
import design
import math


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
                salario = float(input(f"Digite o seu salário bruto do {mes}: R$ "))
                Salario_mensal.append(salario)

                #limpar
                
                break
            except ValueError:
                print("❌ Digite apenas números!")

# Exibição dos salários
print("Salários cadastrados com sucesso!\n")

#limpar

#passa por cada salário mensal
for i, salario in enumerate(Salario_mensal):
    print(f"{meses[i]}: R$ {salario:.2f}")

#mostra o total de salarios
total_sal = sum(Salario_mensal)
print(f"\nTotal anual: R$ {total_sal:.2f}")

#limpar


#DEPENDENTES

#pergunta se possui dependentes

depen= int(input(f"Possui quantos dependentes? (Se nenhum digite 0): "))

#limpar

#DESPESAS SIMBÓLICAS - EDUCAÇÃO

#pergunta se possui alguma despesa com educação

despesas_educ= input(f"Possui alguma despesa com educação que é dedutível? (Se não souber responder digite: ?): ")

#limpar

#explica o que é dedutível ou não
if despesas_educ == "?":
    print("as partes dedutíveis são: Creche e pré-escola \n Ensino fundamental \n Ensino médio \n Pós-graduação \n Educação profissional \n Eja \n ")
    

#limpar

#pergunta o valor total guardado tanto dedutível ou não
if despesas_educ == "S":
    valor_educ_dedutivel= int(input(f"Qual o valor total?: Esses gastos são dedutíveis até o limite anual de R$ 3.561,50 por pessoa (contribuinte, dependente ou alimentando)"))

else:
    valor_educ_nao_dedutivel= int(input(f"Qual o valor total?"))

#limpar

#DESPESAS SIMBÓLICAS - SAÚDE

#pergunta se possui alguma despesa com saúde

despesas_saude= input(f"Possui alguma despesa com saúde que é dedutível? (Se não souber responder digite: ?): ")

#limpar

#explica o que é dedutível ou não
if despesas_saude == "?":
    print("as partes dedutíveis são: - Consultas médicas (pagas a médicos). \n - Consultas odontológicas (pagas a dentistas). \n - Consultas ou sessões com profissionais de saúde habilitados: psicólogos, fisioterapeutas, terapeutas ocupacionais, fonoaudiólogos. \n - Internações(hospitais, clínicas e serviços hospitalares) \n - Exames laboratoriais e serviços radiológicos. \n - Cirurgias e procedimentos médicos (inclusive cirurgias plásticas se forem para preservar, recuperar ou manter a saúde física ou mental). \n - Próteses, órteses, aparelhos ortopédicos ou dentários (quando integrados à conta hospitalar ou emitidos por profissional autorizado), colocação e manutenção de aparelhos ortodônticos, lentes intra-oculares, marcapassos, placas, pinos usados em cirurgias quando parte de tratamento médico. \n - Planos e seguros de saúde (desde que contratados no Brasil e pagos para empresas que oferecem cobertura médica, hospitalar ou odontológica.) \n - Tratamentos de saúde e reabilitação para pessoas com deficiência física ou mental, desde que atestada por laudo médico e pago para entidades destinadas a esse atendimento.")
    

#limpar

#pergunta o valor total guardado tanto dedutível ou não
if despesas_saude == "S":
    valor_saude_dedutivel= int(input(f"Qual o valor total?: "))

else:
    valor_saude_nao_dedutivel= int(input(f"Qual o valor total?"))
