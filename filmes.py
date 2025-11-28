# ===========================================================
# filmes.py — Catálogo de Filmes
# ===========================================================
# Feito por: Rodrigo Borges dos Santos

import os
import design

""" Dicionário com seleção de filmes """
dados = {
    'Transformers': {
        'Nota': 6.5,
        'Genero': 'Ação',
        'Sinopse': 'Um adolescente compra um carro que na verdade é um robô alienígena autônomo, envolvendo-o em uma guerra entre Autobots e Decepticons.'
    },
    'O Poderoso Chefão': {
        'Nota': 9.2,
        'Genero': 'Drama',
        'Sinopse': 'A saga da família Corleone, liderada por Vito Corleone, e a transformação de seu filho Michael no novo patriarca.'
    },
    'Interestelar': {
        'Nota': 8.6,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Um grupo de astronautas viaja através de um buraco de minhoca em busca de um novo lar para a humanidade.'
    },
    'Clube da Luta': {
        'Nota': 8.8,
        'Genero': 'Drama',
        'Sinopse': 'Um homem insone forma um clube de luta underground como terapia alternativa, mas a situação foge do controle.'
    },
    'Matrix': {
        'Nota': 8.7,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Um hacker descobre que a realidade é uma simulação e se junta a um grupo de rebeldes para lutar contra as máquinas.'
    },
    'Os Vingadores': {
        'Nota': 8.0,
        'Genero': 'Ação',
        'Sinopse': 'Os super-heróis mais poderosos da Terra se unem para impedir que Loki e seu exército alienígena dominem o mundo.'
    },
    'John Wick': {
        'Nota': 7.4,
        'Genero': 'Ação',
        'Sinopse': 'Um ex-assassino volta à ativa após um grupo de bandidos roubar seu carro e matar seu cachorro.'
    },
    'Mad Max: Estrada da Fúria': {
        'Nota': 8.1,
        'Genero': 'Ação',
        'Sinopse': 'Em um mundo pós-apocalíptico, Max se junta a um grupo que foge através do deserto em um caminhão-tanque.'
    },
    'Duro de Matar': {
        'Nota': 8.2,
        'Genero': 'Ação',
        'Sinopse': 'Um policial tenta salvar reféns em um arranha-céu durante uma festa de Natal.'
    },
    'Missão Impossível': {
        'Nota': 7.1,
        'Genero': 'Ação',
        'Sinopse': 'Agente Ethan Hunt deve descobrir o traidor que o incriminou por assassinato.'
    },
    'Velozes e Furiosos': {
        'Nota': 6.8,
        'Genero': 'Ação',
        'Sinopse': 'Um policial se infiltra no mundo das corridas de rua para investigar uma série de roubos.'
    },
    'Forrest Gump': {
        'Nota': 8.8,
        'Genero': 'Drama',
        'Sinopse': 'A vida de Forrest Gump, um homem simples que testemunha eventos históricos importantes.'
    },
    'A Lista de Schindler': {
        'Nota': 8.9,
        'Genero': 'Drama',
        'Sinopse': 'Na Segunda Guerra, Oskar Schindler salva judeus empregando-os em sua fábrica.'
    },
    'Um Sonho de Liberdade': {
        'Nota': 9.3,
        'Genero': 'Drama',
        'Sinopse': 'Dois homens presos formam um vínculo strong ao longo de vários anos.'
    },
    'Cidadão Kane': {
        'Nota': 8.3,
        'Genero': 'Drama',
        'Sinopse': 'Repórteres investigam a vida de um magnata das comunicações após sua morte.'
    },
    'Titanic': {
        'Nota': 7.9,
        'Genero': 'Drama',
        'Sinopse': 'Um romance proibido a bordo do famoso navio que naufragou em sua viagem inaugural.'
    },
    'Blade Runner 2049': {
        'Nota': 8.0,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Um novo blade runner descobre um segredo que pode mergulhar a sociedade no caos.'
    },
    'O Exterminador do Futuro': {
        'Nota': 8.1,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Um soldado do futuro é enviado ao passado para proteger Sarah Connor.'
    },
    'Distrito 9': {
        'Nota': 7.9,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Um alienígena e um humano formam uma aliança improvável em Johannesburgo.'
    },
    'A Chegada': {
        'Nota': 7.9,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Uma linguista tenta se comunicar com alienígenas que chegaram à Terra.'
    },
    'Gravidade': {
        'Nota': 7.7,
        'Genero': 'Ficção Científica',
        'Sinopse': 'Dois astronautas ficam à deriva no espaço após sua nave ser destruída.'
    },
    'O Sexto Sentido': {
        'Nota': 8.2,
        'Genero': 'Terror',
        'Sinopse': 'Um psicólogo infantil tenta ajudar um garoto que afirma ver fantasmas.'
    },
    'O Iluminado': {
        'Nota': 8.4,
        'Genero': 'Terror',
        'Sinopse': 'Uma família se isola em um hotel durante o inverno e eventos sobrenaturais ocorrem.'
    },
    'Corra!': {
        'Nota': 7.7,
        'Genero': 'Terror',
        'Sinopse': 'Um jovem afro-americano visita a família de sua namorada e descobre um segredo perturbador.'
    },
    'Se Beber, Não Case': {
        'Nota': 7.7,
        'Genero': 'Comédia',
        'Sinopse': 'Três amigos perdem o noivo durante sua despedida de solteiro em Las Vegas.'
    },
    'As Branquelas': {
        'Nota': 7.0,
        'Genero': 'Comédia',
        'Sinopse': 'Dois agentes do FBI se disfarçam de socialites para investigar um sequestro.'
    }
}

def obter_generos_numerados():
    """Retorna lista de gêneros numerados para seleção"""
    generos = sorted(set(info['Genero'] for info in dados.values()))
    return generos

def selecionar_genero_numerico():
    """Permite ao usuário selecionar gênero por número"""
    generos = obter_generos_numerados()
    
    design.titulo_secao("selecionar gênero", design.COR_INFO)
    
    for i, genero in enumerate(generos, 1):
        design.digitar(f"{i}. {genero}", 0.005)
    
    while True:
        try:
            escolha = int(design.pergunta(f"Digite o número do gênero (1-{len(generos)})"))
            if 1 <= escolha <= len(generos):
                return generos[escolha-1]
            else:
                design.anim_erro(f"Número inválido! Digite entre 1 e {len(generos)}")
        except ValueError:
            design.anim_erro("Digite apenas números!")

def mostrar_detalhes_filme(titulo_filme):
    """Mostra os detalhes de um filme específico"""
    if titulo_filme in dados:
        info = dados[titulo_filme]
        design.titulo_secao(f"informações sobre: {titulo_filme}", design.COR_INFO)
        design.container(f" Nota: {info['Nota']}/10", design.COR_BRANCO, False)
        design.container(f" Gênero: {info['Genero']}", design.COR_BRANCO, False)
        design.container(f" Sinopse: {info['Sinopse']}", design.COR_BRANCO, False)
        return True
    else:
        design.anim_erro(f"Filme '{titulo_filme}' não encontrado!")
        return False

def filmes_por_genero():
    """Lista filmes por gênero com seleção numérica"""
    genero_escolhido = selecionar_genero_numerico()
    
    design.titulo_secao(f"filmes do gênero: {genero_escolhido}", design.COR_INFO)
    
    encontrados = False
    filmes_genero = []
    
    for filme, info in dados.items():
        if info['Genero'] == genero_escolhido:
            filmes_genero.append((filme, info))
            encontrados = True
    
    if not encontrados:
        design.anim_erro(f"Nenhum filme encontrado no gênero '{genero_escolhido}'")
        return False
    
    for i, (filme, info) in enumerate(filmes_genero, 1):
        design.container(f"{i}. {filme}  {info['Nota']}/10", design.COR_BRANCO, False)
    
    """ Permite selecionar filme por número """
    while True:
        try:
            escolha = int(design.pergunta(f"Digite o número do filme para ver detalhes (1-{len(filmes_genero)}) ou 0 para voltar"))
            if escolha == 0:
                break
            elif 1 <= escolha <= len(filmes_genero):
                filme_selecionado = filmes_genero[escolha-1][0]
                mostrar_detalhes_filme(filme_selecionado)
                break
            else:
                design.anim_erro(f"Número inválido! Digite entre 1 e {len(filmes_genero)} ou 0 para voltar")
        except ValueError:
            design.anim_erro("Digite apenas números!")
    
    return True

def listar_todos_filmes():
    """Lista todos os filmes com opção de seleção por número"""
    design.titulo_secao("catálogo completo de filmes", design.COR_INFO)
    
    filmes_lista = list(dados.items())
    
    for i, (filme, info) in enumerate(filmes_lista, 1):
        design.container(f"{i:2d}. {filme} - {info['Genero']}  {info['Nota']}/10", design.COR_BRANCO, False)
    
    """ Permite selecionar filme por número """
    while True:
        try:
            escolha = int(design.pergunta(f"Digite o número do filme para ver detalhes (1-{len(filmes_lista)}) ou 0 para voltar"))
            if escolha == 0:
                break
            elif 1 <= escolha <= len(filmes_lista):
                filme_selecionado = filmes_lista[escolha-1][0]
                mostrar_detalhes_filme(filme_selecionado)
                break
            else:
                design.anim_erro(f"Número inválido! Digite entre 1 e {len(filmes_lista)} ou 0 para voltar")
        except ValueError:
            design.anim_erro("Digite apenas números!")
    
    return True

def menu_principal():
    while True:
        design.titulo_secao("catálogo de filmes", design.COR_TITULO)
        
        design.digitar("1.  Listar filmes por gênero", 0.005)
        design.digitar("2.  Ver catálogo completo", 0.005)
        design.digitar("3.  Sair", 0.005)
        
        while True:
            opcao = design.pergunta("Escolha uma opção (1-3)")
            
            if opcao in ['1', '2', '3']:
                break
            else:
                design.anim_erro("Opção inválida! Tente novamente.")
        
        if opcao == '1':
            design.tela("listar filmes por gênero")
            filmes_por_genero()
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '2':
            design.tela("catálogo completo")
            listar_todos_filmes()
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '3':
            design.titulo_secao("obrigado por usar este programa", design.COR_SUCESSO)
            design.digitar("Desenvolvido por: Rodrigo Borges dos Santos", 0.02)
            break

""" Iniciar o programa """
if __name__ == "__main__":
    design.tela("sistema de catálogo de filmes")
    design.loading("Iniciando Programa", 1, 0.2)
    menu_principal()