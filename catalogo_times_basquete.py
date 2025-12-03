#Feito por Vinícius de Paula 
from design import *


def mostrar_menu():
    limpar_tela()
    titulo_secao("CATÁLOGO DE BASQUETE", animar=False)
    container("1 - Ver história geral do basquete")
    container("2 - Ver times ")
    container("3 - Sair")
    return pergunta("Escolha uma opção")

limpar_tela()
#funções para exibir as coisas :'D
def historia_geral():
    container("--- HISTÓRIA DO BASQUETE ---", cor=COR_TITULO)
    digitar("""
O basquete foi criado em 1891 por James Naismith, nos Estados Unidos.
Com o tempo, tornou-se um dos esportes mais populares do mundo,
principalmente por causa da NBA, que reúne os melhores jogadores do planeta.
""")
    input("Pressione ENTER para continuar...")


def historia_lakers():
    container("--- LOS ANGELES LAKERS ---", cor=COR_TITULO)
    digitar("""

Fundados em 1947, os Lakers são uma das franquias mais vitoriosas da NBA.
Grandes nomes: Magic Johnson, Kareem Abdul-Jabbar, Kobe Bryant, Shaq, LeBron James.
""")


def historia_celtics():
    container("--- BOSTON CELTICS ---", cor=COR_TITULO)
    digitar("""

Os Celtics são conhecidos por sua dinastia nos anos 50 e 60.
Bill Russell e Larry Bird são alguns dos maiores ídolos.
""")


def historia_bulls():
    container("--- CHICAGO BULLS ---", cor=COR_TITULO)
    digitar("""

Famosos pela era de Michael Jordan nos anos 90,
os Bulls dominaram a NBA com 6 títulos em 8 anos.
""")


def historia_warriors():
    container("--- GOLDEN STATE WARRIORS ---", cor=COR_TITULO)
    digitar("""

Conhecidos pelo estilo revolucionário de arremessos de três pontos.
Stephen Curry liderou a franquia a vários títulos recentes.
""")


def historia_heat():
    container("--- MIAMI HEAT ---", cor=COR_TITULO)
    digitar("""

Fundado em 1988, ganhou destaque com Dwyane Wade,
a era 'Big Three' (LeBron, Wade e Bosh) e o técnico Erik Spoelstra.
""")


def historia_spurs():
    container("--- SAN ANTONIO SPURS ---", cor=COR_TITULO)
    digitar("""

Franquia marcada por disciplina e regularidade.
Tim Duncan, Tony Parker e Manu Ginóbili formaram o lendário 'Big Three'.
""")


def historia_knicks():
    container("--- NEW YORK KNICKS ---", cor=COR_TITULO)
    digitar("""

Um dos times mais tradicionais e valiosos da NBA, localizado no Madison Square Garden.
Teve destaque especialmente nas décadas de 70 e 90.
""")


def historia_nets():
    container("--- BROOKLYN NETS ---", cor=COR_TITULO)
    digitar("""

Os Nets já passaram por New Jersey e agora chamam o Brooklyn de casa.
Nos últimos anos, tiveram estrelas como Kevin Durant e Kyrie Irving.
""")


def historia_raptors():
    container("--- TORONTO RAPTORS ---", cor=COR_TITULO)
    digitar("""

Primeira franquia canadense campeã da NBA (2019), liderada por Kawhi Leonard.
""")


def historia_mavericks():
    container("--- DALLAS MAVERICKS ---", cor=COR_TITULO)
    digitar("""

Time do lendário Dirk Nowitzki, campeão em 2011.
Atualmente conhecido pelo talento de Luka Dončić.
""")


def historia_suns():
    container("--- PHOENIX SUNS ---", cor=COR_TITULO)
    digitar("""

Famosos por grandes jogadores como Steve Nash e Charles Barkley.
Chegaram às finais em 2021 liderados por Chris Paul e Devin Booker.
""")


# dicionário dos times
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

#função para mostrar o menu de times
def menu_times():
    limpar_tela()
    container("--- TIMES DA NBA ---", cor=COR_TITULO)
    for key, (nome, _) in TIMES.items():
        container(f"{key} - {nome}")
    container("0 - Voltar")
    return pergunta("Escolha um time")

#função para ver um time
def entrar_time():
    while True:
        escolha = menu_times()

        if escolha == "0":
            return  
        if escolha in TIMES:
            _, funcao_historia = TIMES[escolha]
            limpar_tela()
            funcao_historia()
            input("\nPressione ENTER para voltar ao menu...")
            return  
        else:
            anim_erro("Opção inválida. Tente novamente.")

#estrutura principal do código
def main():
    while True:
        escolha = mostrar_menu()

        if escolha == "1":
            historia_geral()
        elif escolha == "2":
            entrar_time()
        elif escolha == "3":
            print("Saindo... ")
            break
        else:
            anim_erro("Opção inválida. Tente novamente.")

main()