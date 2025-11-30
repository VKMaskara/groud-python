# Código feito por Vinicius de Oliveira Meira  
# Neste código eu irei fazer um quiz sobre o time do Corinthians para ver o nível de conhecimento da pessoa sobre o time 

import design
import time
design.limpar_tela()  # Limpa a tela assim que o programa inicia

def corinthians():
        design.loading("Iniciando o sistema")  # Animação dizendo que o sistema está iniciando
        design.limpar_tela()  
        design.anim_sucesso("Sistema iniciado com sucesso")  # Informa que o sistema iniciou sem erros
        design.tela("Bem vindo ao quiz do Sport Club Corinthians Paulista SCCP")  # Tela de boas-vindas
        design.info("Este quiz terá 5 perguntas sobre o Corinthians")  # Mensagem explicando o quiz

        while True:  # Loop principal do sistema
                # Pergunta se o usuário deseja iniciar o quiz
                pergunta = design.pergunta_sim_nao("Está pronto para iniciar o quiz? ").upper().strip()[0]
                design.limpar_tela()

                if pergunta == "S":  # Caso o usuário queira iniciar
                        design.loading("Iniciando o Quiz")  
                        perguntas = list()  # Lista onde serão guardadas as respostas
                        design.limpar_tela()

                        # -------------------- PERGUNTA 1 --------------------
                        design.container("1) Qual foi o ano de fundação do Corinthians?")
                        design.container("A) 1900")
                        design.container("B) 1911")
                        design.container("C) 1910")
                        design.container("D) 1920")

                        # Laço para garantir que o usuário só responda A, B, C ou D
                        resp = ""
                        while resp not in ["A", "B", "C", "D"]:
                                entrada = design.pergunta("Resposta").upper().strip()  # Lê resposta
                                if entrada == "":  # Impede resposta vazia
                                        design.anim_erro("Digite uma letra!")
                                        continue

                                resp = entrada[0]  # Pega apenas a primeira letra
                                if resp not in ["A", "B", "C", "D"]:  # Validação
                                        design.anim_erro("Digite apenas A, B, C ou D!")

                        perguntas.append(resp)  # Guarda a resposta do usuário
                        design.limpar_tela()

                        # -------------------- PERGUNTA 2 --------------------
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

                        # -------------------- PERGUNTA 3 --------------------
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

                        # -------------------- PERGUNTA 4 --------------------
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

                        # -------------------- PERGUNTA 5 --------------------
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

                        # -------------------- CORREÇÃO DO QUIZ --------------------
                        design.loading("Computando respostas")
                        design.limpar_tela()

                        gabarito = ['C', 'A', 'B', 'A', 'C']  # Respostas corretas do quiz
                        acertos = sum(1 for i in range(5) if perguntas[i] == gabarito[i])  # Conta acertos

                        # Exibe resultado conforme número de acertos
                        if acertos == 0:
                                design.info("Você acertou 0 questões, você não é um fã do Corinthians")
                        if acertos == 2:
                                design.info("Você acertou 2 questões, você é um falso fã do Corinthians")
                        if acertos == 3:
                                design.info("Você acertou 3 questões, você entende um pouco do Corinthians")
                        if acertos == 4:
                                design.info("Você acertou 4 questões, você é um bom entendedor do Corinthians")
                        if acertos == 5:
                                design.info("Você acertou 5 questões, você é um verdadeiro fã do Corinthians")
                        elif acertos == 1:
                                design.info("Você acertou 1 questão, você não é um fã do Corinthians")

                        # Pergunta se deseja refazer o quiz
                        continuar = design.pergunta_sim_nao("Deseja refazer o quiz? ").upper().strip()[0]
                        design.limpar_tela()

                        if continuar == "S":  # Caso queira refazer
                                design.loading("Reiniciando")
                                continue   
                        else:
                                design.digitar("Obrigado por fazer o quiz do maior time do Brasil")
                        break    

                else:  # Caso o usuário não queira iniciar o quiz
                        pergunta1 = design.pergunta_sim_nao("Tem certeza disso?").upper().strip()[0]
                        design.limpar_tela()

                        if pergunta1 == "N":  # Caso ele mude de ideia
                                design.digitar("Obrigado por repensar nos seus atos")
                                for c in range(5, 0, -1):  # Pequena contagem antes de reiniciar
                                        time.sleep(0.4)
                                design.limpar_tela()
                                design.loading("Reiniciando")
                                continue
                        else:  # Caso ele realmente não queira jogar
                                design.digitar("Escolha sua cara")
                        break

corinthians()  # Chama a função e inicia o programa
