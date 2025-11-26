# ============================================================
# filmes.py — Catálogo de Filmes
# ============================================================
# Feito por: Rodrigo Borges dos Santos

import os
import unicodedata
import design

# Dicionário com seleção de filmes
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

def normalizar_texto(texto):
    """
    Normaliza o texto removendo acentos, caracteres especiais
    e convertendo para minúsculas
    """
    # Remove acentos
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    
    # Remove caracteres especiais e converte para minúsculas
    texto = ''.join(c for c in texto if c.isalnum() or c.isspace())
    return texto.lower().strip()

def buscar_filme_por_titulo(titulo_busca):
    """
    Busca um filme pelo título com busca flexível
    """
    titulo_normalizado = normalizar_texto(titulo_busca)
    
    # Primeiro tenta busca exata
    if titulo_busca in dados:
        return titulo_busca
    
    # Busca flexível
    filmes_encontrados = []
    for titulo_filme in dados.keys():
        titulo_filme_normalizado = normalizar_texto(titulo_filme)
        
        # Verifica se o termo de busca está contido no título
        if titulo_normalizado in titulo_filme_normalizado:
            filmes_encontrados.append(titulo_filme)
    
    return filmes_encontrados

def buscar_genero_flexivel(genero_busca):
    """
    Busca gênero com correspondência flexível
    """
    genero_normalizado = normalizar_texto(genero_busca)
    generos_encontrados = []
    
    generos_disponiveis = set(info['Genero'] for info in dados.values())
    
    for genero in generos_disponiveis:
        genero_normalizado_disponivel = normalizar_texto(genero)
        
        # Verifica correspondência parcial
        if (genero_normalizado in genero_normalizado_disponivel or 
            genero_normalizado_disponivel in genero_normalizado):
            generos_encontrados.append(genero)
    
    return generos_encontrados

def buscar_filme(titulo_busca):
    """Busca um filme específico pelo título com busca flexível"""
    resultado = buscar_filme_por_titulo(titulo_busca)
    
    if isinstance(resultado, str):
        # Encontrou um filme exato
        info = dados[resultado]
        design.titulo_secao(f"informações sobre: {resultado}", design.COR_INFO)
        
        design.container(f"📊 Nota: {info['Nota']}/10", design.COR_BRANCO, False)
        design.container(f"🎭 Gênero: {info['Genero']}", design.COR_BRANCO, False)
        design.container(f"📖 Sinopse: {info['Sinopse']}", design.COR_BRANCO, False)
        return True
        
    elif resultado:
        # Encontrou múltiplos filmes
        design.info(f"Encontrei {len(resultado)} filmes com '{titulo_busca}':")
        
        for i, filme in enumerate(resultado, 1):
            design.digitar(f"{i}. {filme}", 0.01)
        
        # Pergunta qual filme o usuário quer ver
        if len(resultado) == 1:
            escolha = design.pergunta_sim_nao("Deseja ver detalhes deste filme")
            if escolha == 'S':
                info = dados[resultado[0]]
                design.titulo_secao(f"informações sobre: {resultado[0]}", design.COR_INFO)
                design.container(f"📊 Nota: {info['Nota']}/10", design.COR_BRANCO, False)
                design.container(f"🎭 Gênero: {info['Genero']}", design.COR_BRANCO, False)
                design.container(f"📖 Sinopse: {info['Sinopse']}", design.COR_BRANCO, False)
        else:
            try:
                escolha = int(design.pergunta(f"Digite o número do filme (1-{len(resultado)})"))
                if 1 <= escolha <= len(resultado):
                    info = dados[resultado[escolha-1]]
                    design.titulo_secao(f"informações sobre: {resultado[escolha-1]}", design.COR_INFO)
                    design.container(f"📊 Nota: {info['Nota']}/10", design.COR_BRANCO, False)
                    design.container(f"🎭 Gênero: {info['Genero']}", design.COR_BRANCO, False)
                    design.container(f"📖 Sinopse: {info['Sinopse']}", design.COR_BRANCO, False)
                else:
                    design.anim_erro("Opção inválida!")
            except ValueError:
                design.anim_erro("Opção inválida!")
        return True
    else:
        design.anim_erro(f"Nenhum filme encontrado com '{titulo_busca}'")
        return False

def filmes_por_genero(genero_busca):
    """Lista todos os filmes de um determinado gênero com busca flexível"""
    generos_encontrados = buscar_genero_flexivel(genero_busca)
    
    if not generos_encontrados:
        design.anim_erro(f"Nenhum gênero encontrado com '{genero_busca}'")
        return False
    
    # Se encontrou múltiplos gêneros, pergunta qual usar
    if len(generos_encontrados) > 1:
        design.info(f"Encontrei {len(generos_encontrados)} gêneros com '{genero_busca}':")
        for i, genero in enumerate(generos_encontrados, 1):
            design.digitar(f"{i}. {genero}", 0.01)
        
        try:
            escolha = int(design.pergunta(f"Digite o número do gênero (1-{len(generos_encontrados)})"))
            if 1 <= escolha <= len(generos_encontrados):
                genero_escolhido = generos_encontrados[escolha-1]
            else:
                design.anim_erro("Opção inválida! Usando o primeiro gênero.")
                genero_escolhido = generos_encontrados[0]
        except ValueError:
            design.anim_erro("Opção inválida! Usando o primeiro gênero.")
            genero_escolhido = generos_encontrados[0]
    else:
        genero_escolhido = generos_encontrados[0]
    
    # Lista os filmes do gênero escolhido
    design.titulo_secao(f"filmes do gênero: {genero_escolhido}", design.COR_INFO)
    
    encontrados = False
    for filme, info in dados.items():
        if info['Genero'] == genero_escolhido:
            design.container(f"🎬 {filme} ⭐ {info['Nota']}/10", design.COR_BRANCO, False)
            encontrados = True
    
    if not encontrados:
        design.anim_erro(f"Nenhum filme encontrado no gênero '{genero_escolhido}'")
        return False
    
    return True

def listar_todos_filmes():
    """Lista todos os filmes do catálogo"""
    design.titulo_secao("catálogo completo de filmes", design.COR_INFO)
    
    for i, (filme, info) in enumerate(dados.items(), 1):
        design.container(f"{i:2d}. {filme} - {info['Genero']} ⭐ {info['Nota']}/10", design.COR_BRANCO, False)

def listar_generos_disponiveis():
    """Lista todos os gêneros disponíveis no catálogo"""
    generos = set(info['Genero'] for info in dados.values())
    design.titulo_secao("gêneros disponíveis", design.COR_INFO)
    
    for i, genero in enumerate(sorted(generos), 1):
        design.container(f"{i}. {genero}", design.COR_BRANCO, False)
    
    return sorted(generos)

def menu_principal():
    """Menu principal de interação com o usuário"""
    while True:
        design.titulo_secao("catálogo de filmes", design.COR_TITULO)
        
        design.digitar("1. 🔍 Buscar filme por título", 0.01)
        design.digitar("2. 🎭 Listar filmes por gênero", 0.01)
        design.digitar("3. 📋 Ver catálogo completo", 0.01)
        design.digitar("4. 📚 Ver gêneros disponíveis", 0.01)
        design.digitar("5. 🚪 Sair", 0.01)
        
        opcao = design.pergunta("Escolha uma opção (1-5)")
        
        if opcao == '1':
            design.tela("buscar filme por título")
            design.titulo_secao("buscar filme", design.COR_INFO)
            
            titulo = design.pergunta("Digite o título do filme")
            buscar_filme(titulo)
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '2':
            design.tela("listar filmes por gênero")
            design.titulo_secao("filmes por gênero", design.COR_INFO)
            
            listar_generos_disponiveis()
            genero_escolhido = design.pergunta("Digite o nome do gênero que deseja ver")
            sucesso = filmes_por_genero(genero_escolhido)
            
            if sucesso:
                ver_detalhes = design.pergunta_sim_nao("Deseja ver detalhes de algum filme")
                if ver_detalhes == 'S':
                    titulo_filme = design.pergunta("Digite o título do filme")
                    buscar_filme(titulo_filme)
            
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '3':
            design.tela("catálogo completo")
            listar_todos_filmes()
            
            ver_detalhes = design.pergunta_sim_nao("Deseja ver detalhes de algum filme")
            if ver_detalhes == 'S':
                titulo_filme = design.pergunta("Digite o título do filme")
                buscar_filme(titulo_filme)
            
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '4':
            design.tela("gêneros disponíveis")
            listar_generos_disponiveis()
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")
            
        elif opcao == '5':
            design.titulo_secao("obrigado por usar este programa", design.COR_SUCESSO)
            design.digitar("Desenvolvido por: Rodrigo Borges dos Santos", 0.03)
            design.digitar("Até logo! 👋", 0.03)
            break
            
        else:
            design.anim_erro("Opção inválida! Tente novamente.")
            design.pergunta("Pressione Enter para continuar")
            design.tela("catálogo de filmes")

# Iniciar o programa
if __name__ == "__main__":
    design.tela("sistema de catálogo de filmes")
    design.loading("Iniciando Programa", 2, 0.3)
    menu_principal()