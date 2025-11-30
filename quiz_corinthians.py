#Código feito por Vinicius de Olveira Meira  
#Neste código eu irei fazer um quiz sobre o time do corinthians para ver o nivel de conhecimento da pessoa sobre o time 
import design
design.limpar_tela()

def corinthians():
        design.loading("Iniciando o sistema")
        design.limpar_tela()
        design.anim_sucesso("Sistema iniciado com sucesso")
        design.tela("Bem vindo ao quiz do Sport Club Corinthians Paulista SCCP")
        design.info("Este quiz tera 5 perguntas sobgre o Corinthians")

        while True:
                pergunta = design.pergunta_sim_nao("Está pronto para iniciar o quiz? ").upper().strip()[0]
                design.limpar_tela()

                if pergunta == "S":
                        design.loading("Iniciando o Quiz")
                        perguntas = list()
                        design.limpar_tela()

                        design.container("1) Qual foi o ano de fundação do Corinthians?")
                        design.container("A) 1900")
                        design.container("B) 1911")
                        design.container("C) 1910")
                        design.container("D) 1920")

                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()
                                if entrada == "":
                                        design.anim_erro("Digite uma letra!")
                                        continue
                                resp = entrada[0]
                                if resp not in ["A", "B", "C", "D"]:
                                        design.anim_erro("Digite apenas A, B, C ou D!")
                        perguntas.append(resp)

                        design.limpar_tela()

                        design.container("2) Qual o ano de fundação da Neo Química Arena?")
                        design.container("A) 10 de Maio de 2014")
                        design.container("B) 18 de Maio de 2014")
                        design.container("C) 14 de Maio de 2014")
                        design.container("D) 20 de Maio de 2014")

                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()
                                if entrada == "":
                                        design.anim_erro("Digite uma letra!")
                                        continue
                                resp = entrada[0]
                                if resp not in ["A", "B", "C", "D"]:
                                        design.anim_erro("Digite apenas A, B, C ou D!")
                        perguntas.append(resp)

                        design.limpar_tela()

                        design.container("3) Qual o maior artilheiro da Neo Química Arena?")
                        design.container("A) Róger Guedes")
                        design.container("B) Yuri Alberto")
                        design.container("C) Ángel Romero")
                        design.container("D) Jô")

                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()
                                if entrada == "":
                                        design.anim_erro("Digite uma letra!")
                                        continue
                                resp = entrada[0]
                                if resp not in ["A", "B", "C", "D"]:
                                        design.anim_erro("Digite apenas A, B, C ou D!")
                        perguntas.append(resp)

                        design.limpar_tela()

                        design.container("4) Quem é o maior ídolo do Corinthians?")
                        design.container("A) Cássio")
                        design.container("B) Sócrates")
                        design.container("C) Marcelinho Carioca")
                        design.container("D) Neto")

                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()
                                if entrada == "":
                                        design.anim_erro("Digite uma letra!")
                                        continue
                                resp = entrada[0]
                                if resp not in ["A", "B", "C", "D"]:
                                        design.anim_erro("Digite apenas A, B, C ou D!")
                        perguntas.append(resp)

                        design.limpar_tela()

                        design.container("5) Quem é o jogador com mais jogos pelo Corinthians?")
                        design.container("A) Ronaldo")
                        design.container("B) Fagner")
                        design.container("C) Cássio")
                        design.container("D) Luizinho")

                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()
                                if entrada == "":
                                        design.anim_erro("Digite uma letra!")
                                        continue
                                resp = entrada[0]
                                if resp not in ["A", "B", "C", "D"]:
                                        design.anim_erro("Digite apenas A, B, C ou D!")
                        perguntas.append(resp)

                        design.limpar_tela()

                        # Corrige acertos
                        design.loading("Computando respostas")
                        design.limpar_tela()

                        gabarito = ['C', 'A', 'B', 'A', 'C']
                        acertos = sum(1 for i in range(5) if perguntas[i] == gabarito[i])

                        if acertos==0:
                                design.info(f"Você acertou {acertos} questões, você não é um fã do Corinthians")
                        if acertos==2:
                                design.info(f"Você acertou {acertos} questões, você é um falso fã do Corinthians")
                        if acertos==3:
                                design.info(f"Você acertou {acertos} questões, você entende um pouco do Corinthians")
                        if acertos==4:
                                design.info(f"Você acertou {acertos} questões, você é um bom entendedor do Corinthians")
                        if acertos==5:
                                design.info(f"Você acertou {acertos} questões, você é um verdadeiro fã do Corinthians")
                        elif acertos==1:
                                design.info(f"Você acertou {acertos} questões, você não é um fã do Corinthians")

                        continuar = design.pergunta_sim_nao("Deseja refazer o quiz? ").upper().strip()[0]
                        design.limpar_tela()

                        if continuar == "S":
                                design.loading("Reiniciando")
                                continue   
                        else:
                                design.digitar("Obrigado por fazer o quiz do maior time do Brasil")
                        break    

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
