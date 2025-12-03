#Feito por Vinícius de Paula 
import design 


def mostrar_menu():
    design.titulo_secao("CATÁLOGO DE BASQUETE")
    design.container("1 - Ver história geral do basquete")
    design.container("2 - Entrar em um time")
    design.container("3 - Sair")
    return design.pergunta("Escolha uma opção")

design.limpar_tela()

def historia_geral():
    print("""
--- HISTÓRIA DO BASQUETE ---
O basquete foi criado em 1891 por James Naismith, nos Estados Unidos.
Com o tempo, tornou-se um dos esportes mais populares do mundo,
principalmente por causa da NBA, que reúne os melhores jogadores do planeta.
""")


def historia_lakers():
    print("""
--- LOS ANGELES LAKERS ---

Fundados em 1947, os Lakers são uma das franquias mais vitoriosas da NBA.
Grandes nomes: Magic Johnson, Kareem Abdul-Jabbar, Kobe Bryant, Shaq, LeBron James.
""")


def historia_celtics():
    print("""
--- BOSTON CELTICS ---

Os Celtics são conhecidos por sua dinastia nos anos 50 e 60.
Bill Russell e Larry Bird são alguns dos maiores ídolos.
""")


def historia_bulls():
    print("""
--- CHICAGO BULLS ---

Famosos pela era de Michael Jordan nos anos 90,
os Bulls dominaram a NBA com 6 títulos em 8 anos.
""")


def historia_warriors():
    print("""
--- GOLDEN STATE WARRIORS ---

Conhecidos pelo estilo revolucionário de arremessos de três pontos.
Stephen Curry liderou a franquia a vários títulos recentes.
""")


def historia_heat():
    print("""
--- MIAMI HEAT ---

Fundado em 1988, ganhou destaque com Dwyane Wade,
a era 'Big Three' (LeBron, Wade e Bosh) e o técnico Erik Spoelstra.
""")


def historia_spurs():
    print("""
--- SAN ANTONIO SPURS ---

Franquia marcada por disciplina e regularidade.
Tim Duncan, Tony Parker e Manu Ginóbili formaram o lendário 'Big Three'.
""")


def historia_knicks():
    print("""
--- NEW YORK KNICKS ---

Um dos times mais tradicionais e valiosos da NBA, localizado no Madison Square Garden.
Teve destaque especialmente nas décadas de 70 e 90.
""")


def historia_nets():
    print("""
--- BROOKLYN NETS ---

Os Nets já passaram por New Jersey e agora chamam o Brooklyn de casa.
Nos últimos anos, tiveram estrelas como Kevin Durant e Kyrie Irving.
""")


def historia_raptors():
    print("""
--- TORONTO RAPTORS ---

Primeira franquia canadense campeã da NBA (2019), liderada por Kawhi Leonard.
""")


def historia_mavericks():
    print("""
--- DALLAS MAVERICKS ---

Time do lendário Dirk Nowitzki, campeão em 2011.
Atualmente conhecido pelo talento de Luka Dončić.
""")


def historia_suns():
    print("""
--- PHOENIX SUNS ---

Famosos por grandes jogadores como Steve Nash e Charles Barkley.
Chegaram às finais em 2021 liderados por Chris Paul e Devin Booker.
""")


# DICIONÁRIO DOS TIMES
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


def menu_times():
    design.digitar("\n--- TIMES DA NBA ---")
    for key, (nome, _) in TIMES.items():
        design.digitar(f"{key} - {nome}")
    design.digitar("0 - Voltar")
    return input("Escolha um time: ")


def entrar_time():
    while True:
        escolha = menu_times()

        if escolha == "0":
            return  
        if escolha in TIMES:
            _, funcao_historia = TIMES[escolha]
            funcao_historia()
            input("\nPressione ENTER para voltar ao menu...")
            return  
        else:
            design.anim_erro("Opção inválida. Tente novamente.")


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
            print("Opção inválida. Tente novamente.")

main()