# Mikaely --> Simulador de financiamento com juros simples

import time #importando tempo (para pequenas pausas)
import design



Lista = [] #Para guardar os cálculos feitos (histórico)

while True: #Inicia um loop
    
    design.limpar_tela()  #Limpa a tela 
    #Tela de menu principal
   # print("\n=== SIMULADOR DE FINANCIAMENTO COM JUROS SIMPLES ===")
    design.titulo_secao("SIMULADOR DE FINANCIAMENTO COM JUROS SIMPLES") 
    print("1 -> Fazer novo cálculo")
    print("2 -> Ver histórico")
    print("3 -> Sair")

    opcao = input("Escolha uma das opções:  ").strip().lower()  # tratamento de caractere 
                                                                    #.strip().lower() primeiro tira os espaços, depois deixa os letras minúsculas.
                                       
                                                                
    #------------------------------------------- 1° opção --------------------------------------------  
    if opcao == "1": #Verifica se o usuário escolheu a opção 1
        print("\n---Novo cálculo---") 
    elif opcao == "2":
        print("\n---Histórico de cálculos---")
        print("-----------------------")
        print(f'"Total de cálculos realizados: {len(Lista)}"')

        # Mostrar histórico completo
        if len(Lista) == 0:
            print("Nenhum cálculo ainda.")
        else:
            for i, item in enumerate(Lista, start=1):
                print(f"\nRegistro {i}:")
                print(" Capital:", item["Capital"])
                print(" Taxa:", item["Taxa"])
                print(" Tempo:", item["Tempo"])
                print(" Juros:", item["Juros"])
                print(" Total:", item["Total"])

        input("\nPressione ENTER para voltar ao menu...")
        continue   
    elif opcao == "3":
        print("\n---Saindo do programa---")
        print("-----------------------")
        break  # encerra o programa
    else:
        design.anim_erro("Opção inválida. Tente novamente.")
        continue  # volta para o início do loop
            
    #--ler capital (valor inicial)--
    capital = input("Capital (R$): ").replace(",", ".")  #pede para o usuário digitar o capital e substitui vírgula por ponto
    capital = float(capital)  #Transforma o valor digitado (string) para número decimal (float)
    
    #--Ler taxa--
    taxa = input("Taxa (ex: 0.05 para 5%): ").replace(",", ".")  # lê a taxa de juros e troca vírgula por ponto
    taxa = float(taxa)  #Transforma a taxa para número decimal

    #--Ler tempo--
    tempo = input("Tempo (meses): ").replace(",", ".")  # lê o tempo em meses e troca vírgula por ponto
    tempo = float(tempo)  #Transforma o tempo para número decimal

    #--Cálculo de juros simples--
    juros = capital * taxa * tempo  # calcula o valor dos juros: capital * taxa * tempo
    total = capital + juros  # calcula o valor total a pagar (capital + juros)

    print("\nCalculando...")  # mensagem para simular um pequeno processamento
    time.sleep(0.5)  # pausa de meio segundo

    print(f"Juros: R$ {juros:.2f}")  # mostra os juros calculados, com 2 casas decimais
    print(f"Total: R$ {total:.2f}")  # mostra o valor total a pagar, com 2 casas decimais
    input("\nPressione ENTER para voltar ao menu...")

    #--Salvar no histórico--
    Lista.append({  # adiciona um registro ao histórico (lista de dicionários) #.append adiciona o item ao final da lista
        "Capital": capital,  #guarda o capital digitado
        "Taxa": taxa,        #guarda a taxa digitada
        "Tempo": tempo,      #guarda o tempo digitado
        "Juros": juros,      #guarda o valor dos juros calculados
        "Total": total       #guarda o valor total calculado
    })

    #------------------------------------------ 2° Opção --------------------------------------------
    if opcao == "2":  # verifica se o usuário escolheu a opção 2 
        print("\n=== HISTÓRICO ===")  # mostra um título para a tela de histórico

        if len(Lista) == 0:  # verifica se a lista (histórico) está vazia
            print("Nenhum cálculo ainda.")  # se estiver vazia, avisa o usuário
        else:  # se houver registros no histórico (Lista)
            for i, item in enumerate(Lista, start=1):  #Percorre cada registro da lista com índice começando em 1
                print(f"\nRegistro {i}:")  #Mostra o número do registro
                print(" Capital:", item["Capital"])  # Corrigido: Mostra o valor do capital daquele registro
                print(" Taxa:", item["Taxa"])        # Corrigido: Mostra a taxa de juros daquele registro
                print(" Tempo:", item["Tempo"])      # Corrigido: Mostra o tempo daquele registro
                print(" Juros:", item["Juros"])      # Corrigido: Mostra o valor dos juros calculados
                print(" Total:", item["Total"])      # Corrigido: Mostra o valor total calculado (capital + juros)
            
#-------------------------------------------- 3° opção ----------------------------------------------
    if opcao == "3":
        print("Saindo...") 
        break  # encerra o programa
 

    