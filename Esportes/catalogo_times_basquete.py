
#Feito por Vinícius de Paula 
from design import * # Importa todas as funções e variáveis do módulo 'design'
                    # (como limpar_tela, titulo_secao, container, pergunta, 
                    # digitar, anim_erro, COR_TITULO, etc.).

# Função principal para exibir o menu inicial do catálogo.
def mostrar_menu():
    # 'limpar_tela()' apaga o conteúdo anterior no console.
    limpar_tela()
    # 'titulo_secao()' exibe um título formatado no topo.
    titulo_secao("CATÁLOGO DE BASQUETE", animar=False)
    # 'container()' exibe as opções do menu dentro de caixas formatadas.
    container("1 - Ver história geral do basquete")
    container("2 - Ver times ")
    container("3 - Sair")
    # 'pergunta()' solicita a entrada do usuário e retorna a escolha.
    return pergunta("Escolha uma opção")

limpar_tela() # Limpa a tela logo na inicialização do script.

#--- Funções para exibir o conteúdo da história e dos times ---

# Exibe a história geral do basquete.
def historia_geral():
    limpar_tela()
    # Exibe um título formatado.
    container("--- HISTÓRIA DO BASQUETE ---", cor=COR_TITULO)
    # 'digitar()' exibe o texto com um efeito de digitação.
    digitar("""
O basquete foi criado em 1891 por James Naismith, nos Estados Unidos.
Com o tempo, tornou-se um dos esportes mais populares do mundo,
principalmente por causa da NBA, que reúne os melhores jogadores do planeta.
""")
    # Pausa a execução até o usuário pressionar ENTER.
    input("Pressione ENTER para continuar...")


# Exibe a história do Los Angeles Lakers.
def historia_lakers():
    container("--- LOS ANGELES LAKERS ---", cor=COR_TITULO)
    digitar("""

Fundados em 1947, os Lakers são uma das franquias mais vitoriosas da NBA.
Grandes nomes: Magic Johnson, Kareem Abdul-Jabbar, Kobe Bryant, Shaq, LeBron James.
""")


# Exibe a história do Boston Celtics.
def historia_celtics():
    container("--- BOSTON CELTICS ---", cor=COR_TITULO)
    digitar("""

Os Celtics são conhecidos por sua dinastia nos anos 50 e 60.
Bill Russell e Larry Bird são alguns dos maiores ídolos.
""")


# Exibe a história do Chicago Bulls.
def historia_bulls():
    container("--- CHICAGO BULLS ---", cor=COR_TITULO)
    digitar("""

Famosos pela era de Michael Jordan nos anos 90,
os Bulls dominaram a NBA com 6 títulos em 8 anos.
""")


# Exibe a história do Golden State Warriors.
def historia_warriors():
    container("--- GOLDEN STATE WARRIORS ---", cor=COR_TITULO)
    digitar("""

Conhecidos pelo estilo revolucionário de arremessos de três pontos.
Stephen Curry liderou a franquia a vários títulos recentes.
""")


# Exibe a história do Miami Heat.
def historia_heat():
    container("--- MIAMI HEAT ---", cor=COR_TITULO)
    digitar("""

Fundado em 1988, ganhou destaque com Dwyane Wade,
a era 'Big Three' (LeBron, Wade e Bosh) e o técnico Erik Spoelstra.
""")


# Exibe a história do San Antonio Spurs.
def historia_spurs():
    container("--- SAN ANTONIO SPURS ---", cor=COR_TITULO)
    digitar("""

Franquia marcada por disciplina e regularidade.
Tim Duncan, Tony Parker e Manu Ginóbili formaram o lendário 'Big Three'.
""")


# Exibe a história do New York Knicks.
def historia_knicks():
    container("--- NEW YORK KNICKS ---", cor=COR_TITULO)
    digitar("""

Um dos times mais tradicionais e valiosos da NBA, localizado no Madison Square Garden.
Teve destaque especialmente nas décadas de 70 e 90.
""")


# Exibe a história do Brooklyn Nets.
def historia_nets():
    container("--- BROOKLYN NETS ---", cor=COR_TITULO)
    digitar("""

Os Nets já passaram por New Jersey e agora chamam o Brooklyn de casa.
Nos últimos anos, tiveram estrelas como Kevin Durant e Kyrie Irving.
""")


# Exibe a história do Toronto Raptors.
def historia_raptors():
    container("--- TORONTO RAPTORS ---", cor=COR_TITULO)
    digitar("""

Primeira franquia canadense campeã da NBA (2019), liderada por Kawhi Leonard.
""")


# Exibe a história do Dallas Mavericks.
def historia_mavericks():
    container("--- DALLAS MAVERICKS ---", cor=COR_TITULO)
    digitar("""

Time do lendário Dirk Nowitzki, campeão em 2011.
Atualmente conhecido pelo talento de Luka Dončić.
""")


# Exibe a história do Phoenix Suns.
def historia_suns():
    container("--- PHOENIX SUNS ---", cor=COR_TITULO)
    digitar("""

Famosos por grandes jogadores como Steve Nash e Charles Barkley.
Chegaram às finais em 2021 liderados por Chris Paul e Devin Booker.
""")


# Dicionário que armazena os dados dos times.
# A chave (string) é o número da opção no menu de times.
# O valor é uma tupla: (Nome do time, Função que exibe a história do time).
TIMES = {
    "1": ("Los Angeles Lakers", historia_lakers),
    "2": ("Boston Celtics", historia_celtics),
    "3": ("Chicago Bulls", historia_bulls),
    "4": ("Golden State Warriors", historia_warriors),
    "5": ("Miami Heat", historia_heat),
    "6": ("San Antonio Spurs", historia_spurs),
    "7": ("New York Knicks", historia_knicks),
    "8": ("Brooklyn Nets", historia_nets),
    "9": ("Toronto Raptors", historia_raptors),
    "10": ("Dallas Mavericks", historia_mavericks),
    "11": ("Phoenix Suns", historia_suns),
}

# Função para exibir o menu de times disponíveis.
def menu_times():
    limpar_tela()
    container("--- TIMES DA NBA ---", cor=COR_TITULO)
    # Itera sobre o dicionário TIMES para exibir cada opção.
    # 'key' é o número (ex: "1") e 'nome' é o nome do time.
    for key, (nome, _) in TIMES.items():
        container(f"{key} - {nome}")
    container("0 - Voltar")
    # Retorna a escolha do usuário.
    return pergunta("Escolha um time")

# Função que gerencia a seleção e exibição da história de um time.
def entrar_time():
    # Inicia um loop infinito (WHILE TRUE) para manter o menu de times
    # aberto até que o usuário escolha '0' (Voltar) ou um time válido.
    while True:
        escolha = menu_times()

        # IF para verificar se a escolha é a opção '0' (Voltar).
        if escolha == "0":
            return # Sai da função, voltando ao menu principal.
        
        # IF para verificar se a escolha é uma chave válida no dicionário TIMES.
        if escolha in TIMES:
            # Desempacota a tupla do time. O nome é ignorado (_),
            # e a função de história é armazenada em 'funcao_historia'.
            _, funcao_historia = TIMES[escolha]
            limpar_tela()
            funcao_historia() # Chama a função específica de história do time.
            input("\nPressione ENTER para voltar ao menu...")
            return # Sai da função após o usuário ler a história.
        
        # ELSE executado se a opção não for '0' nem uma chave válida no TIMES.
        else:
            anim_erro("Opção inválida. Tente novamente.")
            # O loop 'while True' recomeça, exibindo o menu de times novamente.

# Função principal (main) do programa.
def main():
    # Inicia o loop principal (WHILE TRUE) para manter o programa em execução
    # até que o usuário escolha a opção '3' (Sair).
    while True:
        escolha = mostrar_menu() # Exibe o menu principal e obtém a escolha.
        limpar_tela()

        # IF para a opção '1' (Ver história geral do basquete).
        if escolha == "1":
            historia_geral()
            limpar_tela()
        
        # ELIF (Else If) para a opção '2' (Ver times).
        elif escolha == "2":
            entrar_time() # Chama a função que gerencia o menu e a exibição dos times.
            limpar_tela()
        
        # ELIF para a opção '3' (Sair).
        elif escolha == "3":
            limpar_tela()
            print("Saindo... ")
            break # Encerra o loop 'while True', finalizando a função 'main'.
        
        # ELSE executado se a opção não for '1', '2' ou '3'.
        else:
            anim_erro("Opção inválida. Tente novamente.")
            # O loop 'while True' recomeça, exibindo o menu principal novamente.

if __name__ == "__main__":     
    main() # Inicia a execução do programa chamando a função 'main'.