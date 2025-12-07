


decisoes =("A) criar play list\nB) acessar play list existente\nC) sair")


def inicio():
        print("bem vindo a sua play list interativa")
        while True:
                print(decisoes)
                escolha = input("deseja qual programa hj?").upper().strip()
                if escolha == "A":
                                vazio = []
                                nome = input("Qual será nome da play list?")
                                adicionar = input(f"play list {nome} criada, deseja adicionar musica?(s/n)").upper().strip()
                                if adicionar == "S":
                                        while True:
                                                musica = input("digite o nome da musica: ")
                                                artista = input("digite o nome do artista: ")
                                                vazio.append((musica, artista))
                                                print("musica adicionada com sucesso!")
                                                
                                                if not input("deseja adicionar mais musicas?(s/n)").upper().strip().startswith("S"):
                                                        print("ok, play list finalizada")
                                                        break
                                else:
                                        print("ok, play list criada sem musicas")
                                volta= input ("deseja ver sua play list? (s/n)").upper().strip()
                                if volta == "S":
                                        print(f"sua play list {nome} é composta por:")
                                        for musica, artista in vazio:
                                                print(f"musica: {musica} - artista: {artista}")
                                if input ("Deseja criar nova play list? (s/n) ") .upper ().strip() .startswith("S"):
                                