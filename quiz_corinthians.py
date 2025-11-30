#Código feito por Vinicius de Olveira Meira  
#Neste código eu irei fazer um quiz sobre o time do corinthians para ver o nivel de conhecimento da pessoa sobre o time 
import design
design.limpar_tela()
def corinthians():
        design.digitar("Iniciando o sistema")
        design.digitar("Bem vindo ao quiz do Sport Club Corinthians Paulista SCCP")
        design.digitar("Este quiz tera 5 perguntas sobgre o SCCP")
        while True:
                pergunta = design.pergunta_sim_nao("Está pronto para iniciar o quiz? ").upper().strip()[0]
                design.limpar_tela()

                if pergunta == "S":
                        design.loading("Iniciando o Quiz")
                        perguntas = list()
                        design.limpar_tela()

                        # Pergunta 1
                        design.digitar("1) Qual foi o ano de fundação do Corinthians?")
                        print("A) 1900")
                        print("B) 1911")
                        print("C) 1910")
                        print("D) 1920")
                        perguntas.append(input("Resposta: ").upper().strip()[0])
                        design.limpar_tela()

                        # Pergunta 2
                        print("2) Qual o ano de fundação da Neo Química Arena?")
                        print("A) 10 de Maio de 2014")
                        print("B) 18 de Maio de 2014")
                        print("C) 14 de Maio de 2014")
                        print("D) 20 de Maio de 2014")
                        perguntas.append(input("Resposta: ").upper().strip()[0])
                        design.limpar_tela()

                        # Pergunta 3
                        print("3) Qual o maior artilheiro da Neo Química Arena?")
                        print("A) Róger Guedes")
                        print("B) Yuri Alberto")
                        print("C) Ángel Romero")
                        print("D) Jô")
                        perguntas.append(input("Resposta: ").upper().strip()[0])
                        design.limpar_tela()

                        # Pergunta 4
                        print("4) Quem é o maior ídolo do Corinthians?")
                        print("A) Cássio")
                        print("B) Sócrates")
                        print("C) Marcelinho Carioca")
                        print("D) Neto")
                        perguntas.append(input("Resposta: ").upper().strip()[0])
                        design.limpar_tela()

                        # Pergunta 5
                        print("5) Quem é o jogador com mais jogos pelo Corinthians?")
                        print("A) Ronaldo")
                        print("B) Fagner")
                        print("C) Cássio")
                        print("D) Luizinho")
                        perguntas.append(input("Resposta: ").upper().strip()[0])
                        design.limpar_tela()

                        # Corrige acertos
                        design.loading("Computando respostas")
                        design.limpar_tela()

                        gabarito = ['C', 'A', 'B', 'A', 'C']
                        acertos = sum(1 for i in range(5) if perguntas[i] == gabarito[i])

                        if acertos==0:
                                design.digitar(f"Você acertou {acertos} questões, você não é um fã do Corinthians")
                        if acertos==2:
                                design.digitar(f"Você acertou {acertos} questões, você é um falso fã do Corinthians")
                        if acertos==3:
                                design.digitar(f"Você acertou {acertos} questões, você entende um pouco do Corinthians")
                        if acertos==4:
                                design.digitar(f"Você acertou {acertos} questões, você é um bom entendedor do Corinthians")
                        if acertos==5:
                                design.digitar(f"Você acertou {acertos} questões, você é um verdadeiro fã do Corinthians")
                        elif acertos==1:
                                design.digitar(f"Você acertou {acertos} questões, você não é um fã do Corinthians")

                        # Repetição
                        continuar = design.pergunta_sim_nao("Deseja refazer o quiz? ").upper().strip()[0]
                        design.limpar_tela()

                        if continuar == "S":
                                design.loading("Reiniciando")
                                continue   # VOLTA PARA O COMEÇO DO while TRUE
                        else:
                                design.digitar("Obrigado por fazer o quiz do maior time do Brasil")
                        break      # FINALIZA DE VEZ

                else:
                        pergunta1=design.pergunta_sim_nao("Tem certeza disso?").upper().strip()[0]
                        design.limpar_tela()
                        if pergunta1 == "N":
                                design.digitar("Obrigado por repensar nos seus atos")
                                design.limpar_tela()
                                design.loading("Reiniciando")
                                continue
                        else:
                                design.digitar("Escolha sua cara")
                        break

corinthians()