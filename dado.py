import random  #importa a biblioteca random para gerar números aleatórios
import os      #importa a biblioteca os para comandos do sistema operacional
#import design    #importa o módulo design para elementos visuais (assumindo que exista)

def limpar_tela():  #função para limpar a tela do terminal
   # """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')  #comando para limpar a tela dependendo do sistema operacional

def dado(): #função para simular o lançamento do dado
   # """Simula o lançamento de um dado de 6 faces"""
    return random.randint(1, 6) #retorna um número aleatório entre 1 e 6

def jogar(): #função principal do jogo
    #"""Executa o jogo principal entre dois jogadores"""
    limpar_tela() #limpa a tela antes de iniciar o jogo
    print("🎲 Bem-vindo ao Jogo do Dado! 🎲")  #bem vindos 
    print("=" * 40) #separador

    try:  #tenta obter o número de jogadas
        numero_jogadas = int(input("Quantas vezes cada jogador vai jogar? "))  #pede o número de jogadas
        if numero_jogadas <= 0:  #verifica se o número é positivo
            raise ValueError("Número deve ser positivo")  #lança um erro se o número não for positivo
    except ValueError:#captura o erro de valor inválido
        print("❌ Erro: Digite um número inteiro positivo válido!")  #mensagem de erro
        input("Pressione Enter para continuar...")  #pressiona enter para continuar
        return  #sai da função jogar

    resultados1 = []  #lista para armazenar os resultados do jogador 1
    resultados2 = []   #lista para armazenar os resultados do jogador 2
    soma1 = soma2 = 0  #variáveis para armazenar a soma dos resultados

    # Jogador 1
    print( "👤 Jogador 1 - Seus lançamentos:") #jogador 1 lançar o dado
    print("-" * 30) #separador
    for i in range(numero_jogadas):  #loop para o número de jogadas
        resultado = dado()  #lança o dado
        msg = f"🔢 Lançamento {i+1}: {resultado}"   #mensagem de lançamento e mostra resultado
        if resultado == 6:   #verifica se o resultado é 6
            msg += " ⭐ PARABÉNS - MAIOR NÚMERO! ⭐"   #mensagem especial porque tirou maior número dado
        print(msg)   #apresenta a mensagem
        resultados1.append(resultado)  #soma o resultado à lista do jogador 1
        soma1 += resultado    #soma o resultado à soma do jogador 1
        input("Pressione Enter para continuar...") #espera o jogador pressionar enter para continuar

    # Jogador 2
    limpar_tela() #limpa a tela antes do jogador 2
    print("🎲 Agora é a vez do Jogador 2! 🎲") #mensagen proximo jogar
    print(" 👤 Jogador 2 - Seus lançamentos:") #jogador 2 lançar o dado
    print("-" * 30)#separador
    for i in range(numero_jogadas): #loop para o número de jogadas
        resultado = dado() #lança o dado
        msg = f"🔢 Lançamento {i+1}: {resultado}"  #mensagem de lançamento e mostra resultado
        if resultado == 6: #verifica se o resultado é 6
            msg += " ⭐ PARABÉNS - MAIOR NÚMERO! ⭐"  #mensagem especial porque tirou maior número dado
        print(msg) #apresenta a mensagem
        resultados2.append(resultado) #soma o resultado à lista do jogador 2
        soma2 += resultado  #soma o resultado à soma do jogador 2
        input("Pressione Enter para continuar...") #espera o jogador pressionar enter para continuar

    # Resultados finais
    limpar_tela() #limpa a tela antes de mostrar os resultados finais
    print("🏆 RESULTADOS FINAIS 🏆") #aprersentar resultado finais
    print("=" * 50)#separador
    print(f"👤 Jogador 1: {resultados1}") #presenta resultado do jogador
    print(f"📊 Soma: {soma1}") #apresenta soma das jogada dos dados
    print(f"👤 Jogador 2: {resultados2}")  #presenta resultado do jogador
    print(f"📊 Soma: {soma2}") #apresenta soma das jogada dos dados
    print("-" * 50) #separador

    # Determinar vencedor
    if soma1 > soma2: #soma do jogador 1 maior que a do jogador 2
        print("🎉🏆 JOGADOR 1 VENCEU! 🏆🎉") #mensagem de vitória do jogador 1
    elif soma2 > soma1: #soma do jogador 2 maior que a do jogador 1
        print("🎉🏆 JOGADOR 2 VENCEU! 🏆🎉") #mensagem de vitória do jogador 2
    else: #empate
        print("🤝 EMPATE! 🤝") #mensagem de empate

    print( "Obrigado por jogar! 🎲") #mensagem de agradecimento
    input("Pressione Enter para voltar ao menu...")#espera o jogador pressionar enter para voltar ao menu
    limpar_tela()#limpa a tela

def instrucoes(): #mostra as instruções do jogo
    """Mostra as instruções do jogo"""
    limpar_tela()#limpa a tela antes de mostrar as instruções
    print("📖 INSTRUÇÕES DO JOGO 📖")#início das instruções como jogar
    print("=" * 40)#separador
    print("- Cada jogador lança o dado o mesmo número de vezes")#explicação do jogo
    print("- A soma total decide o vencedor")#explicação que soma decide o vencedor
    print("- 6 é o maior número! Ganha destaque especial ⭐")#dado numero 6 maior ganha destaque especial
    print("- Pressione Enter entre cada lançamento")#explicação para pressionar enter entre cada lançamento
    print( "✅ Boa sorte!")#mensagem de boa sorte
    input("Pressione Enter para voltar...")#espera o jogador pressionar enter para voltar ao menu

def tela_inicio(): #função para mostrar o menu inicial
    """Menu principal do jogo"""
    while True: #loop infinito para o menu
        limpar_tela() #limpa a tela antes de mostrar o menu
        print("🎲==🎲 JOGO DO DADO 🎲==🎲") #nome do jogo inicio
        print("1️⃣ - Jogar")#opção jogar
        print("2️⃣ - Instruções")#opção instruções
        print("3️⃣ - Sair")#opção sair
        print("=" * 25)#separador

        try:#tenta obter a opção do usuário
            opcao = input("Escolha uma opção: ").strip()#pede a opção do usuário e remove espaços em branco
            
            if opcao == "1":#se opção for 1
                jogar()#chama a função jogar
            elif opcao == "2":#se opção for 2
                instrucoes()#chama a função instruções
            elif opcao == "3":#se opção for 3
                print("🤗 Até logo! Obrigado por jogar!")#mensagem de agrdecimento
                break#sai do loop e termina o programa
            else:#se opção for inválida
                print("❌ Opção inválida!")#mensagem de erro
                input("Pressione Enter...")#espera o jogador pressionar enter para continuar
                
        except KeyboardInterrupt:#|captura interrupção do teclado (Ctrl+C)
            print( "🤗 Saindo...")#mensagem de saida do jogo
            break#sai do loop e termina o programa

# Inicia o programa
if __name__ == "__main__":#verifica se o script está sendo executado diretamente
    tela_inicio()#chama a função tela_inicio para iniciar o jogo
    limpar_tela()#limpa a tela
    #design.rodape()  #chama a função rodape do módulo design para mostrar o rodapé (assumindo que exista)
   # """ https://emojisparacopiar.com/#google_vignette""" #retirada dos emojis do site                 
    """👨🏽‍💻Renato de Oliveira👨🏽‍💻"""# Desenvolvedor Python
    
    # Fim do programa