#Anna
from design import *
import random
import time
import os 
import platform
import shutil
import sys
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def pausar():
    time.sleep(1) #Função para pausar

def pausar_mais():
    time.sleep(3) #Função para pausar mais ainda

amarelo = "\033[43m"
verde = "\033[42m"


palavras = ['muito', 'sobre', 'mesmo', 'todos', 'ainda', 'entre', 'fazer', 'paulo', 'minha', 'tempo', 'assim', 'agora', 'mundo', 'forma', 'parte', 'estao', 'foram', 'todas', 'entao', 'maior', 'disse', 'feira', 'nossa', 'outro', 'nosso', 'tenho', 'menos', 'vezes', 'antes', 'sendo', 'podem', 'estou', 'pouco', 'desde', 'saude', 'nunca', 'coisa', 'tinha', 'livro', 'estar', 'hotel', 'neste', 'pelos', 'outra', 'final', 'conta', 'saber', 'grupo', 'lugar', 'homem', 'gente', 'deste', 'poder', 'dizer', 'geral', 'noite', 'desta', 'tanto', 'dados', 'filme', 'preco', 'jogos', 'local', 'ficar', 'valor', 'quero', 'nesta', 'mesma', 'horas', 'quase', 'temos', 'curso', 'vamos', 'corpo', 'seria', 'ponto', 'falar', 'voces', 'marco', 'disso', 'abril', 'filho', 'julho', 'volta', 'terra', 'feito', 'jesus', 'pelas', 'ficou', 'junho', 'algum', 'texto', 'meses', 'nesse', 'maria', 'esses', 'santa', 'vista', 'dessa', 'tenha', 'novos', 'falta', 'serie', 'serao', 'campo', 'claro', 'video', 'ajuda', 'desse', 'porem', 'quais', 'carro', 'essas', 'tarde', 'total', 'lista', 'venda', 'certo', 'super', 'usado', 'nivel', 'porto', 'busca', 'novas', 'havia', 'gosto', 'devem', 'papel', 'feliz', 'norte', 'facil', 'linha', 'frete', 'estes', 'amigo', 'forca', 'olhos', 'idade', 'cerca', 'causa', 'dicas', 'livre', 'fonte', 'criar', 'festa', 'morte', 'posso', 'silva', 'marca', 'favor', 'plano', 'apoio', 'manha', 'epoca', 'fosse', 'acima', 'junto', 'santo', 'deles', 'forte', 'longo', 'cinco', 'perto', 'legal', 'sexta', 'tendo', 'fazem', 'atras', 'autor', 'porta', 'linda', 'passa', 'caixa', 'pecas', 'unico', 'acoes', 'civil', 'casos', 'praia', 'nessa', 'prova', 'natal', 'banco', 'passo', 'minas', 'somos', 'clube', 'banda', 'lindo', 'areas', 'ordem', 'prazo', 'feita', 'baixo', 'fundo', 'comum', 'obras', 'viver', 'levar', 'menor', 'deixa', 'cores', 'estas', 'forum', 'vagas', 'jovem', 'unica', 'visao', 'preto', 'deixe', 'risco', 'serem', 'verde', 'redes', 'sejam', 'ontem', 'media', 'ideia', 'atual', 'ouvir', 'possa', 'razao', 'opcao', 'trata', 'olhar', 'visto', 'casas', 'medio', 'chega', 'setor', 'tomar', 'uniao', 'teria', 'costa', 'jogar', 'mudar', 'obter', 'tipos', 'dando', 'email', 'achei', 'jeito', 'leite', 'terca', 'ideal', 'massa', 'amiga', 'saiba', 'longe', 'custo', 'pagar', 'sonho', 'tirar', 'reais', 'bahia', 'basta', 'filha', 'sites', 'radio', 'otimo', 'gosta', 'faixa', 'torna', 'verao', 'crise', 'houve', 'casal', 'velho', 'certa', 'mente', 'graca', 'sabia', 'globo', 'votos', 'comer', 'abrir', 'video', 'igual', 'chave', 'sinto', 'capaz', 'troca', 'breve', 'adoro', 'corte', 'sorte', 'renda', 'motor', 'saida', 'crime', 'andar', 'banho', 'delas', 'nomes', 'enfim', 'baixa', 'cargo', 'roupa', 'tiver', 'serra', 'acaba', 'ficam', 'carta', 'turma', 'ambos', 'bolsa', 'segue', 'sinal', 'jogue', 'disco', 'teste', 'temas', 'canal', 'reino', 'ideia', 'dizem', 'irmao', 'pedir', 'fique', 'carne', 'termo', 'chuva', 'album', 'jorge', 'folha', 'rosto', 'parar', 'lider', 'artes', 'vindo', 'falou', 'chama', 'praca', 'barra', 'sabem', 'perda', 'midia', 'aluno', 'exame', 'beijo', 'podia', 'vento', 'meios', 'etapa', 'pegar', 'chefe', 'vidas', 'itens', 'andre', 'erros', 'china', 'levou', 'longa', 'monte', 'cheio', 'vendo', 'resto', 'queda', 'carga', 'pedra', 'serve', 'vinho', 'fatos', 'daqui', 'light', 'aguas', 'torno', 'haver', 'posts', 'envio', 'danca', 'fazia', 'ganha', 'vidro', 'extra', 'venha', 'notas', 'check', 'entra', 'lazer', 'museu', 'clima', 'alias', 'achar', 'lendo', 'seres', 'dupla', 'ferro', 'paris', 'rural', 'placa', 'taxas', 'ciclo', 'senha', 'oeste', 'clara', 'posto', 'gomes', 'preso', 'serio', 'letra', 'marco', 'calor', 'velha', 'cheia', 'frase', 'bruno', 'uteis', 'preta', 'salao', 'fomos', 'moral', 'ponta', 'prata', 'sente', 'humor', 'metal', 'goias', 'botao', 'penso', 'canto', 'terao', 'toque', 'armas', 'dieta', 'orgao', 'curto', 'culpa', 'palco', 'pensa', 'ceara', 'lucas', 'padre', 'matar', 'penal', 'criou', 'etica', 'rocha', 'datas', 'facto', 'paula', 'ponte', 'negro', 'nisso', 'terem', 'curta', 'morto', 'tenta', 'grave', 'tocar', 'solar', 'mudou', 'couro', 'redor', 'ritmo', 'secao', 'aviso', 'pediu', 'custa', 'japao', 'atriz', 'copia', 'audio', 'creme', 'porno', 'bloco', 'negra', 'forno', 'valeu', 'passe', 'dizia', 'regra', 'lanca', 'samba', 'peixe', 'pasta', 'ajude', 'posse', 'black', 'faria', 'viram', 'lopes', 'login', 'perde', 'unhas', 'dores', 'vinte', 'pobre', 'ampla', 'senti', 'sabor', 'gerar', 'vivem', 'peito', 'rapaz', 'fluxo', 'cento', 'beira', 'aviao', 'ficha', 'caras', 'rodas', 'poeta', 'exige', 'areia', 'ramos', 'fator', 'anexo', 'prato', 'micro', 'ligar', 'pista', 'anual', 'arroz', 'achou', 'povos', 'limpo', 'creio', 'justo', 'bater', 'braco', 'envie', 'forem', 'lidar', 'honra', 'leste', 'tenis', 'senao', 'conto', 'doces', 'braga', 'cunha', 'nacao', 'pouca', 'norma', 'abriu', 'falei', 'vemos', 'bomba', 'acaso', 'virus', 'manda', 'altos', 'molho', 'lutar', 'greve', 'virou', 'pinto', 'falam', 'vasco', 'deram', 'atuar', 'calma', 'inves', 'poema', 'ajuda', 'fruto', 'https', 'anjos', 'morre', 'ganhe', 'ativa', 'recem', 'devia', 'acham', 'sousa', 'lucro', 'fraco', 'lavar', 'noiva', 'ondas', 'porte', 'bento', 'mario', 'beber', 'chico', 'sitio', 'surge', 'flash', 'ambas', 'metas', 'prima', 'golpe', 'ativo', 'calca', 'movel', 'deixo', 'plena', 'tente', 'dedos', 'pense', 'pleno', 'merda', 'loira', 'barco', 'tinta', 'dever', 'pesca', 'moeda', 'vigor', 'belas', 'fugir', 'socio', 'puder', 'vinha', 'subir', 'salto', 'tomou', 'aonde', 'corre', 'nocao', 'sofre', 'reune', 'unido', 'duplo', 'magia', 'vazio', 'vossa', 'papai', 'multa', 'cinza', 'milho', 'louco', 'virar', 'louca', 'turno', 'banca', 'india', 'vejam', 'senso', 'salvo', 'torre', 'metro', 'belem', 'suite', 'levam', 'amplo', 'ouviu', 'venho', 'vinda', 'vende', 'morar', 'nobre', 'votar', 'coroa', 'almas', 'limpa', 'culto', 'neves', 'inter', 'firme', 'temer', 'falha', 'parto', 'cesar', 'amado', 'ganho', 'mamae', 'luzes', 'drama', 'arena', 'fases', 'media', 'autos', 'volte', 'preve', 'limao', 'soube', 'heroi', 'sport', 'droga', 'raiva', 'larga', 'bolso', 'casar', 'nunes', 'alice', 'juizo', 'pegou', 'junta', 'adora', 'resta', 'disto', 'morro', 'jeans', 'licao', 'bispo', 'perca', 'vivos', 'colar', 'diria', 'vosso', 'assis', 'moura', 'lagoa', 'graus', 'elite', 'trama', 'mouse', 'tampa', 'metro', 'diabo', 'parou', 'baixe', 'perdi', 'sinta', 'suave', 'piaui', 'chile', 'porra', 'infra', 'largo', 'briga', 'facam', 'drive', 'pizza', 'citar', 'cobre', 'vimos', 'vozes', 'looks', 'acido', 'pauta', 'missa', 'lance', 'navio', 'fibra', 'ilhas', 'trigo', 'nariz', 'blusa', 'lutas', 'nasce', 'jogou', 'manga', 'cobra', 'pires', 'russo', 'celso', 'egito', 'lesao', 'tirou', 'falso', 'bunda', 'febre', 'farol', 'capas', 'justa', 'obvio', 'viveu', 'abuso', 'raios', 'junte', 'nuvem', 'canta', 'vence', 'anime', 'radio', 'grego', 'lucia', 'fieis', 'ligue', 'podes', 'perna', 'pague', 'macho', 'clipe', 'viana', 'laser', 'ultra', 'bordo', 'bicho', 'amada', 'fizer', 'conte', 'tiros', 'roubo', 'fruta', 'bolas', 'bateu', 'lapis', 'volto', 'valer', 'chato', 'negar', 'optar', 'piada', 'leves', 'verbo', 'forro', 'notar', 'cabos', 'batom', 'chapa', 'modos', 'adeus', 'abreu', 'presa', 'salve', 'alema', 'grade', 'irmas', 'pares', 'reduz', 'mexer', 'salva', 'tento', 'fecha', 'gasto', 'saldo', 'lenda', 'ocupa', 'suica', 'falsa', 'apelo', 'choro', 'estas', 'atras', 'matou', 'tweet', 'pegue', 'varia', 'stock', 'marte', 'julio', 'vapor', 'curva', 'malas', 'daria', 'morta', 'subiu', 'pagos', 'olhou', 'patio', 'berco', 'tende', 'gripe', 'afins', 'piano', 'ossos', 'gesto', 'dolar', 'evite', 'tesao', 'porem', 'marta', 'seios', 'diogo', 'grito', 'icone', 'penas', 'corda', 'vital', 'motel', 'primo', 'suite', 'joana', 'rever', 'color', 'atuam', 'cupom', 'ombro', 'circo', 'torne', 'coral', 'malha', 'laura', 'lento', 'verso', 'idoso', 'fogao', 'gases', 'fraca', 'frota', 'tomei', 'mauro', 'expor', 'touch', 'lacos', 'andam', 'mania', 'opera', 'mande', 'freio', 'ruins', 'turne', 'green', 'multi', 'trono', 'meias', 'terei', 'exito', 'goste', 'neles', 'guias', 'tirei', 'lemos', 'dente', 'velas', 'duque', 'bacia', 'golfe', 'vivia', 'doses', 'medir', 'baile', 'casca', 'serie', 'mover', 'conde', 'posta', 'opala', 'cuida', 'afeta', 'prado', 'odeio', 'digno', 'bando', 'aereo', 'tocou', 'bonus', 'turbo', 'ervas', 'tecla', 'lente', 'click', 'arabe', 'share', 'dobro', 'copos', 'cesta', 'porco', 'pausa', 'usava', 'pacto', 'vicio', 'grato', 'meter', 'fusao', 'ruido', 'fumar', 'exato', 'joias', 'cruel', 'altar', 'evita', 'vasta', 'aneis', 'sirva', 'envia', 'sofia', 'grana', 'farao', 'curte', 'criam', 'russa', 'serei', 'terco', 'pular', 'durou', 'farei', 'usina', 'penha', 'barao', 'cinto', 'botas', 'vinil', 'sobra', 'sabes', 'civel', 'durar', 'palio', 'testa', 'chora', 'impor', 'cofre', 'solta', 'secar', 'siria', 'rival', 'pedem', 'carmo', 'flora', 'grama', 'rigor', 'negou', 'torta', 'gerou', 'vazia', 'viola', 'deusa', 'calmo', 'palma', 'avise', 'bruto', 'bueno', 'parei', 'casou', 'fecho', 'grata', 'sodio', 'exibe', 'rodar', 'queen', 'olhei', 'curar', 'grega', 'burro', 'caput', 'traga', 'fitas', 'caldo', 'mudam', 'damos', 'noivo', 'corsa', 'sigla', 'barro', 'chamo', 'gozar', 'duelo', 'levei', 'ninja', 'sexto', 'vivas', 'aroma', 'atrai', 'signo', 'skate', 'corta', 'latim', 'tribo', 'impoe', 'fadas', 'volei', 'litro', 'censo', 'lotes', 'fusca', 'stand', 'safra', 'dance', 'leiam', 'paiva', 'gotas', 'acabo', 'poste', 'troco', 'molde', 'barba', 'bucal', 'praga', 'trava', 'ratos', 'notes', 'pagou', 'viria', 'atuou', 'servo', 'blues', 'vocal', 'skype', 'racas', 'palha', 'trago', 'jejum', 'abrem', 'cotas', 'happy', 'horta', 'porno', 'fauna', 'verba', 'gordo', 'artur', 'femea', 'chego', 'bruta', 'sitio', 'criei', 'sabio', 'weber', 'trato', 'ninho', 'veste', 'besta', 'amaro', 'pagam', 'folga', 'versa', 'pulso', 'rolar', 'sauna', 'avisa', 'nelas', 'iriam', 'andei', 'nasci', 'crack', 'cacau', 'vilao', 'forro', 'brisa', 'genio', 'luvas', 'dorme', 'digna', 'errar', 'apoia', 'beija', 'adobe', 'angra', 'amava', 'borda', 'laudo', 'mirim', 'otica', 'malta', 'rindo', 'henry', 'aluna', 'sales', 'diana', 'milao', 'pesar', 'lidas', 'rotas', 'joias', 'susto', 'manha', 'major', 'valem', 'mando', 'prosa', 'bauru', 'balao', 'digam', 'valia', 'roque', 'lobos', 'ligou', 'cross', 'secas', 'traco', 'secos', 'sabao', 'racao', 'viaja', 'sonha', 'gasta', 'judeu', 'naval', 'bravo', 'fixar', 'tunel', 'gerir', 'saido', 'helio', 'macio', 'modem', 'chata', 'poker', 'saias', 'trara', 'situa', 'gesso', 'tiras', 'mares', 'bocas', 'indio', 'treze', 'mudei', 'spray', 'mudas', 'afeto', 'rubro', 'geram', 'amapa', 'guine', 'manga', 'couto', 'gorda', 'desce', 'tigre', 'fatal', 'misto', 'vasto', 'temor', 'segui', 'simao', 'doido', 'leito', 'slide', 'urina', 'solto', 'puxar', 'frios', 'chips', 'penis', 'salmo', 'tomam', 'moram', 'firma', 'delta', 'idolo', 'celta', 'short', 'corra', 'deter', 'esqui', 'mista', 'sorri', 'cafes', 'botar', 'utero', 'citou', 'lenha', 'books', 'vadia', 'optou', 'pagas', 'angel', 'focar', 'doida', 'luzia', 'comeu', 'nobel', 'fugiu', 'furia', 'tropa', 'rolou', 'virao', 'rezar', 'heavy', 'nisto', 'anais', 'quote', 'olhem', 'pedal', 'renal', 'timao', 'pilha', 'julia', 'ataca', 'douro', 'ricas', 'visam', 'furto', 'fatia', 'ibope', 'judas', 'afora', 'selva', 'netos', 'ouvia', 'arcos', 'acabe', 'caido', 'magra', 'calar', 'etico', 'curti', 'macau', 'urnas', 'bruxa', 'cache', 'radar', 'cover', 'zumbi', 'pouso', 'aguia', 'sogra', 'viuva', 'senta', 'enche', 'pilar', 'trens', 'demos', 'filas', 'plana', 'prime', 'astro', 'atlas', 'mante', 'frias', 'entro', 'balas', 'opera', 'andou', 'juiza', 'viseu', 'tenda', 'nozes', 'ronda', 'fogos', 'calda', 'latas', 'animo', 'clean', 'leque', 'cifra', 'sutil', 'funda', 'ditas', 'louca', 'detem', 'patos', 'bacon', 'grita', 'vacuo', 'solda', 'staff', 'sensu', 'tomas', 'chute', 'alias', 'jogam', 'mural', 'ponha', 'rugas', 'volvo', 'alega', 'lucio', 'siena', 'terno', 'cuide', 'manto', 'manta', 'break', 'cetim', 'expoe', 'duzia', 'cauda', 'punho', 'jeova', 'lutam', 'chame', 'bolha', 'saira', 'tinto', 'folia', 'brava', 'nadar', 'virei', 'odeia', 'verem', 'touro', 'falas', 'cisco', 'tchau', 'corno', 'julga', 'param', 'elisa', 'garra', 'cubra', 'lilas', 'ceder', 'sexos', 'duras', 'perco', 'felix', 'haiti', 'vetor', 'pedia', 'milha', 'tumor', 'grava', 'nicho', 'davam', 'notei', 'somar', 'magro', 'lauro', 'feche', 'acusa', 'salsa', 'peles', 'vales', 'combo', 'sonda', 'sushi', 'split', 'fezes', 'tenis', 'couve', 'rende', 'aveia', 'trans', 'bossa', 'donde', 'cueca', 'macro', 'bonde', 'obtem', 'force', 'chale', 'sopro', 'balde', 'vitor', 'blush', 'bosta', 'lenco', 'magno', 'cunho', 'tabua', 'sumiu', 'lares', 'comem', 'boate', 'sedan', 'viral', 'furos', 'foder', 'grife', 'cabra', 'retro', 'gemas', 'tenso', 'obito', 'madre', 'chupa', 'trico', 'oliva', 'nylon', 'tocam', 'picos', 'guiar', 'pinho', 'grill', 'turco', 'veiga', 'bazar', 'model', 'pudim', 'rouba', 'narra', 'molas', 'errou', 'retro', 'eleva', 'serio', 'zinco', 'podre', 'astra', 'bambu', 'girar', 'chove', 'podio', 'assar', 'loiro', 'louro', 'tosse', 'pinta', 'tours', 'sampa', 'macae', 'hiper', 'kombi', 'hobby', 'fofos', 'copie', 'ciume', 'vazao', 'belga', 'julgo', 'panda', 'traje', 'votou', 'shell', 'ligas', 'notou', 'cravo', 'rally', 'saque', 'adota', 'arame', 'sueco', 'anima', 'polpa', 'darem', 'punir', 'capim', 'front', 'quilo', 'fazes', 'dunas', 'farsa', 'cansa', 'tiram', 'files', 'rosca', 'apaga', 'paper', 'matam', 'pisca', 'darei', 'pixel', 'credo', 'close', 'lobby', 'macas', 'prece', 'prega', 'tedio', 'remix', 'umido', 'lutou', 'mamas', 'dante', 'votes', 'pomba', 'ruiva', 'copas', 'pingo', 'capes', 'pondo', 'romeu', 'emite', 'ebook', 'trate', 'uncao', 'supra', 'surto', 'timor', 'olham', 'celia', 'ouvem', 'morna', 'parem', 'ferir', 'exodo', 'pique', 'garfo', 'reage', 'fixas', 'somam', 'suico', 'canoa', 'matas', 'duche', 'mutuo', 'miolo', 'dobra', 'leram', 'levem', 'sutia', 'hatch', 'indie', 'round', 'dunga', 'impar', 'morri', 'swing', 'ligam', 'sirio', 'agudo', 'bodas', 'tango', 'panos', 'saiam', 'alpes', 'tiete', 'cotia', 'visor', 'monta', 'adega', 'amido', 'cacar', 'adiar', 'gamer', 'supor', 'mafia', 'souto', 'cesto', 'bingo', 'rampa', 'blitz', 'apice', 'lunar', 'orais', 'intra', 'pisar', 'telha', 'basic', 'busco', 'imune', 'fisco', 'enter', 'elena', 'teles', 'comia', 'piora', 'alcas', 'genro', 'polar', 'abate', 'copia', 'sofri', 'fenda', 'usual', 'magna', 'vagar', 'deves', 'mosca', 'cerco', 'vogue', 'mutua', 'monge', 'densa', 'varas', 'libra', 'linho', 'kayak', 'manso', 'corri', 'servi', 'crato', 'galho', 'seita', 'haste', 'puxou', 'pardo', 'vigia', 'venus', 'ziper', 'omega', 'bicos', 'torto', 'sigam', 'coach', 'tange', 'dormi', 'reina', 'sofro', 'asilo', 'libia', 'xerox', 'fraga', 'optei', 'sacar', 'surdo', 'baita', 'reter', 'golfo', 'fogem', 'irene', 'farta', 'osmar', 'fosco', 'putas', 'decor', 'farao', 'arcar', 'zelar', 'avila', 'borba', 'sumir', 'virem', 'duram', 'clone', 'falem', 'porao', 'cabem', 'recuo', 'brega', 'tarso', 'rugby', 'farto', 'damas', 'livia', 'apego', 'fluir', 'meteu', 'magoa', 'burra', 'lages', 'habil', 'pecas', 'darao', 'peres', 'match', 'cinta', 'torco', 'diodo', 'ramal', 'aspas', 'frita', 'epico', 'etnia', 'acesa', 'veloz', 'clero', 'gavea', 'betim', 'dizes', 'sobem', 'ganso', 'morra', 'risca', 'refem', 'capao', 'salta', 'sigma', 'busto', 'cairo', 'foste', 'cloro', 'toner', 'congo', 'trave', 'rimas', 'regua', 'canil', 'temem', 'chica', 'polos', 'cases', 'repor', 'apito', 'praxe', 'anglo', 'hasta', 'abono', 'nudez', 'direi', 'limpe', 'amora', 'atira', 'corro', 'sugar', 'fuder', 'mafra', 'orgia', 'denso', 'odiar', 'citei', 'brejo', 'merce', 'povoa', 'tutor', 'supoe', 'fardo', 'reiki', 'atomo', 'lajes', 'pudor', 'traca', 'batem', 'logos', 'gruta', 'farra', 'torax', 'ansia', 'cedeu', 'punto', 'tapas', 'irmos', 'tomem', 'puros', 'ponho', 'ducha', 'papas', 'anote', 'brasa', 'regem', 'coube', 'bangu', 'achas', 'solte', 'fenix', 'nervo', 'iamos', 'feroz', 'ative', 'peste', 'andes', 'deita', 'aquem', 'lobao', 'mexeu', 'prego', 'sacra', 'nerds', 'sarau', 'aluga', 'tampo', 'apoia', 'leigo', 'valha', 'tacho', 'polvo', 'orixa', 'frito', 'creek', 'aedes', 'pente', 'forca', 'visse', 'cerro', 'atire', 'detox', 'tocha', 'teres', 'apolo', 'barca', 'sabia', 'corvo', 'oxala', 'movem', 'seras', 'seara', 'finge', 'lombo', 'cruza', 'nasal', 'zebra', 'fazei', 'sueca', 'pavor', 'morno', 'viado', 'trevo', 'pegam', 'tripe', 'moema', 'mocao', 'banal', 'teras', 'viaje', 'ruina', 'ousar', 'errei', 'shake', 'karma', 'sanar', 'torce', 'batia', 'cromo', 'casco', 'sujas', 'tecto', 'prove', 'melao', 'persa', 'cozer', 'abria', 'boato', 'locao', 'vulgo', 'impos', 'robot', 'drink', 'quota', 'mamao', 'edema', 'cedro', 'elege', 'taxis', 'buque', 'baiao', 'vodka', 'mamar', 'amore', 'desca', 'morou', 'canso', 'poupa', 'aloja', 'refil', 'feixe', 'crash', 'caber', 'pasto', 'liceu', 'licor', 'adubo', 'oxido', 'valsa', 'oasis', 'ageis', 'bessa', 'canaa', 'furar', 'shape', 'checa', 'troco', 'morei', 'educa', 'arduo', 'capuz', 'apart', 'durmo', 'filma', 'tirem', 'obvio', 'tombo', 'nevoa', 'treta', 'pomar', 'miudo', 'pariu', 'varal', 'inova', 'cisne', 'porca', 'tecer', 'negam', 'sogro', 'strip', 'durma', 'calha', 'tulio', 'trair', 'bebes', 'dogma', 'cerne', 'livra', 'araxa', 'rimel', 'fixou', 'cause', 'barca', 'caico', 'crepe', 'apodi', 'aliar', 'curas', 'pinga', 'tensa', 'friso', 'setup', 'betao', 'pulou', 'apela', 'doado', 'tiara', 'rompe', 'range', 'rumor', 'adote', 'lorde', 'epica', 'fossa', 'quica', 'bucha', 'reler', 'creem', 'armar', 'moita', 'bebeu', 'scrum', 'apena', 'sofra', 'fetal', 'deite', 'pecar', 'mecha', 'votei', 'vazou', 'dirao', 'casei', 'cante', 'peoes', 'gaita', 'touca', 'coque', 'hidro', 'alive', 'sejas', 'bruxo', 'relax', 'vivam', 'quina', 'pampa', 'traze', 'eagle', 'casta', 'frite', 'chefs', 'labio', 'pavao', 'still', 'court', 'ardua', 'durao', 'letal', 'busca', 'rouge', 'vogal', 'viajo', 'feriu', 'arara', 'harpa', 'imita', 'maias', 'venca', 'varao', 'stick', 'surra', 'logar', 'xeque', 'cosmo', 'meiga', 'alter', 'bonus', 'optam', 'lidam', 'mixer', 'dobre', 'abram', 'parti', 'gemea', 'gibis', 'feias', 'expos', 'campi', 'abuse', 'ruivo', 'telao', 'sudao', 'oucam', 'ergue', 'tosco', 'relva', 'fieis', 'latao', 'lerem', 'bolao', 'migre', 'serpa', 'janta', 'erica', 'ajudo', 'ardor', 'devam', 'cacas', 'somou', 'hacer', 'dueto', 'banha', 'usara', 'fungo', 'traiu', 'desci', 'frevo', 'cabia', 'bioma', 'vicio', 'encha', 'focal', 'horto', 'latex', 'grilo', 'aurea', 'exija', 'menta', 'alugo', 'divas', 'tapar', 'pinca', 'subia', 'puras', 'balsa', 'babel', 'bicha', 'vilar', 'gorro', 'colhe', 'romao', 'pombo', 'induz', 'guria', 'users', 'timer', 'surfe', 'giras', 'arido', 'derby', 'creia', 'matei', 'tarot', 'litio', 'loica', 'tetra', 'capta', 'ferry', 'dorso', 'botox', 'sopra', 'ibero', 'error', 'regue', 'cruze', 'catar', 'caiam', 'vulto', 'score', 'aries', 'veria', 'temia', 'poses', 'vinde', 'sento', 'agita', 'trupe', 'lavra', 'trote', 'botou', 'tatui', 'chore', 'verme', 'grifo', 'bebem', 'smile', 'cegas', 'gozou', 'feijo', 'acude', 'seque', 'pinte', 'buggy', 'cuido', 'troia', 'broca', 'frade', 'lousa', 'clama', 'depor', 'coxim', 'vibra', 'papos', 'votem', 'labor', 'sujar', 'tomas', 'viste', 'carte', 'lapso', 'futil', 'caida', 'magda', 'nutre', 'agito', 'rolim', 'funil', 'preza', 'sotao', 'surda', 'morde', 'falte', 'turca', 'jarra', 'gnome', 'edite', 'adere', 'aceso', 'forme', 'choca', 'novel', 'regar', 'lamas', 'poupe', 'ronco', 'emana', 'vagao', 'anexa', 'tarte', 'treme', 'urubu', 'tetas', 'medem', 'crias', 'italo', 'teima', 'serva', 'hiato', 'irado', 'antao', 'cusco', 'evoca', 'lambe', 'inibe', 'fuzil', 'celio', 'lisas', 'criem', 'docil', 'visem', 'farda', 'hindu', 'rombo', 'carie', 'lirio', 'racha', 'laico', 'genio', 'frear', 'limbo', 'alhos', 'tesla', 'recta', 'colon', 'brota', 'pocao', 'comes', 'parta', 'arder', 'nitro', 'povao', 'joint', 'vesti', 'lixao', 'custe', 'guara', 'meigo', 'semen', 'caule', 'drone', 'posar', 'edita', 'curry', 'casam', 'tenra', 'anula', 'loura', 'tumba', 'sacou', 'detem', 'rente', 'polen', 'cabal', 'troll', 'xampu', 'andas', 'rodou', 'sabre', 'tonto', 'abade', 'polia', 'guacu', 'rotor', 'vendi', 'enfia', 'furor', 'forma', 'basto', 'pazes', 'nepal', 'jumbo', 'perde', 'grado', 'train', 'orfao', 'malte', 'caira', 'votam', 'dolby', 'cessa', 'lotus', 'giram', 'urano', 'pesam', 'reich', 'quito', 'bebia', 'aceda', 'reuni', 'sinop', 'advem', 'fosso', 'trust', 'tenue', 'cacos', 'coifa', 'trial', 'punha', 'xango', 'ambar', 'nenem', 'verei', 'acola', 'fluor', 'pagao', 'areal', 'gemer', 'saudo', 'mudem', 'findo', 'cache', 'pipas', 'tarja', 'sabia', 'apura', 'kodak', 'ameno', 'ceara', 'antas', 'beato', 'fobia', 'ditar', 'veras', 'moveu', 'posou', 'citam', 'oscar', 'corja', 'giria', 'atrio', 'petra', 'pirai', 'ovulo', 'input', 'insta', 'gozam', 'reves', 'psico', 'babar', 'rabao', 'benta', 'paira', 'sedia', 'saiam', 'crivo', 'dotes', 'blast', 'viuvo', 'obtem', 'cavar', 'seduz', 'judia', 'cisao', 'abusa', 'modal', 'sadio', 'socio', 'azedo', 'mexia', 'devir', 'falho', 'treco', 'recai', 'modus', 'foods', 'senda', 'rolha', 'osseo', 'pecam', 'chuta', 'tenor', 'garca', 'zerar', 'rimos', 'lacre', 'amago', 'chope', 'qatar', 'rasga', 'trico', 'prove', 'seiva', 'birra', 'prole', 'selar', 'graxa', 'ficas', 'previ', 'guiao', 'veras', 'hajam', 'egide', 'geada', 'gaste', 'deveu', 'opaco', 'musgo', 'veado', 'dalai', 'raspa', 'vanda', 'rogai', 'marra', 'bocal', 'viera', 'dotar', 'gueto', 'alana', 'bamba', 'xisto', 'fosca', 'penny', 'lebre', 'retos', 'picar', 'animo', 'papal', 'perua', 'recua', 'vespa', 'mento', 'isola', 'tetos', 'pulga', 'rapel', 'tacos', 'pareo', 'banir', 'islao', 'tarda', 'totem', 'tonta', 'suado', 'pisou', 'creem', 'tampe', 'botei', 'galos', 'jaula', 'draft', 'logon', 'notem', 'rifle', 'datam', 'creta', 'vaias', 'curou', 'jurar', 'calou', 'caspa', 'tanga', 'retem', 'twist', 'fores', 'chili', 'ethos', 'macom', 'titia', 'opoem', 'carma', 'surja', 'penis', 'facao', 'garoa', 'trace', 'anzol', 'papao', 'foice', 'doria', 'graal', 'berna', 'abalo', 'tufao', 'dende', 'catch', 'digas', 'corto', 'pompa', 'drops', 'galao', 'cosas', 'rodam', 'secou', 'lycra', 'moido', 'naipe', 'draco', 'apoie', 'talha', 'danco', 'curvo', 'jurou', 'facas', 'metem', 'batel', 'sunga', 'bulbo', 'cariz', 'sarro', 'cocar', 'mirar', 'frisa', 'puxei', 'mexem', 'coupe', 'ouros', 'voraz', 'ousou', 'rolam', 'regia', 'maple', 'ferva', 'basal', 'odiei', 'opina', 'rasto', 'somem', 'espia', 'reger', 'token', 'mumia', 'mater', 'lanco', 'nutri', 'sacro', 'lixar', 'ganga', 'manel', 'gajas', 'venci', 'obice', 'agido', 'hifen', 'leone', 'borra', 'evito', 'vazar', 'finda', 'pecou', 'matem', 'viole', 'aruba', 'erram', 'otico', 'sarja', 'flare', 'gemeo', 'ginga', 'mouro', 'cagar', 'abala', 'epoxi', 'anota', 'molhe', 'boina', 'untar', 'punch', 'forre', 'mango', 'neuro', 'cisto', 'honor', 'rouca', 'jango', 'avela', 'debil', 'preze', 'parma', 'lomba', 'canas', 'pesou', 'algoz', 'ninfa', 'deito', 'fugaz', 'suede', 'sonhe', 'reuna', 'ostra', 'sacas', 'crush', 'palmo', 'adore', 'colei', 'molha', 'goela', 'magoa', 'turvo', 'enjoo', 'sache', 'gozei', 'fuzis', 'derem', 'ferem', 'lotar', 'amena', 'gelar', 'horda', 'obeso', 'ebola', 'lavou', 'fugia', 'mogno', 'lavei', 'lutei', 'pluma', 'leria', 'penta', 'treno', 'murro', 'louvo', 'ocupe', 'talco', 'coura', 'rogue', 'reles', 'pulsa', 'carpe', 'gerem', 'cacho', 'turva', 'caves', 'baque', 'zorra', 'juras', 'achem', 'porra', 'grite', 'agata', 'armou', 'remar', 'pacas', 'louva', 'pulse', 'delay', 'lince', 'inata', 'zumba', 'fiada', 'venta', 'tomba', 'gemia', 'vetar', 'pulei', 'somas', 'minar', 'rabos', 'toldo', 'doure', 'colou', 'icaro', 'rasgo', 'atuem', 'hertz', 'negue', 'girou', 'berro', 'prior', 'domar', 'chita', 'metia', 'ninar', 'proto', 'sirvo', 'movia', 'carne', 'jarro', 'canon', 'polis', 'vagem', 'cupim', 'dedao', 'adaga', 'parra', 'tasca', 'beije', 'molda', 'cobri', 'parir', 'pesto', 'glace', 'numas', 'clave', 'troca', 'luxos', 'flame', 'cursa', 'lhasa', 'cousa', 'funde', 'vicia', 'motim', 'riram', 'truta', 'checo', 'pegas', 'socar', 'lotou', 'betel', 'ratio', 'espia', 'skank', 'exala', 'cetro', 'notam', 'atroz', 'lepra', 'mediu', 'joker', 'lupus', 'broto', 'borla', 'pagas', 'timbo', 'ereto', 'urico', 'jurua', 'liana', 'avido', 'sinha', 'larva', 'alisa', 'gleba', 'magma', 'femur', 'raiar', 'aceno', 'foros', 'cirio', 'focam', 'caiba', 'terme', 'goles', 'perus', 'minto', 'timon', 'wicca', 'cisma', 'foque', 'ladra', 'sarna', 'curam', 'ileso', 'beata', 'topou', 'impar', 'fakes', 'trofa', 'levas', 'alude', 'pavio', 'parda', 'terna', 'forja', 'lenga', 'umbro', 'aorta', 'afago', 'pousa', 'polir', 'fanny', 'racks', 'fumam', 'olhai', 'dolly', 'bates', 'colas', 'rapto', 'canja', 'feria', 'dinda', 'fodeu', 'lines', 'ocaso', 'fados', 'brita', 'menti', 'curia', 'calao', 'comam', 'molar', 'calca', 'calvo', 'faras', 'agape', 'sonar', 'swell', 'irina', 'guiou', 'pussy', 'matao', 'baste', 'sauda', 'farma', 'caqui', 'alado', 'louca', 'tonus', 'viril', 'sorgo', 'fixam', 'troia', 'fluem', 'sulco', 'burle', 'dreno', 'puxao', 'sagaz', 'iemen', 'praca', 'argel', 'trufa', 'nadir', 'ureia', 'testo', 'bardo', 'conca', 'lousa', 'supre', 'zorro', 'eleve', 'voava', 'plebe', 'torci', 'prumo', 'plane', 'vives', 'dumas', 'peido', 'omite', 'adiou', 'culpo', 'fedor', 'lives', 'coito', 'toada', 'finjo', 'sling', 'runas', 'trepa', 'solas', 'mutum', 'aipim', 'pequi', 'coeso', 'canis', 'brado', 'enchi', 'messe', 'puxam', 'busao', 'bruma', 'velar', 'acena', 'talao', 'torpe', 'cocos', 'rezam', 'bumba', 'ferve', 'cacao', 'burla', 'juris', 'calam', 'cobro', 'sisal', 'coesa', 'sosia', 'povoa', 'andem', 'mondo', 'aureo', 'brabo', 'focou', 'varre', 'arado', 'gruda', 'orava', 'parva', 'ditam', 'bongo', 'gabar', 'potro', 'exime', 'bugre', 'irece', 'steak', 'serum', 'vodca', 'choco', 'ponei', 'pirar', 'derme', 'kefir', 'ralar', 'emule', 'venus', 'retal', 'causo', 'rocar', 'cocal', 'suino', 'murta', 'cervo', 'alcar', 'grafo', 'xinga', 'julga', 'shoyu', 'hedge', 'lides', 'truco', 'reine', 'ecoar', 'xiita', 'germe', 'bicas', 'exijo', 'taipa', 'berra', 'torga', 'mirra', 'tocas', 'lesse', 'irati', 'mijar', 'rodei', 'mitra', 'manja', 'iluda', 'bulas', 'salte', 'furou', 'treva', 'safar', 'jurei', 'dosar', 'fujam', 'fecal', 'pasmo', 'pimba', 'arqui', 'aurea', 'raias', 'midas', 'secam', 'biela', 'pirex', 'trapo', 'guiam', 'ebano', 'gamba', 'inato', 'finca', 'dique', 'advir', 'doque', 'chaga', 'ditou', 'caiam', 'rendo', 'jihad', 'paste', 'ataca', 'vetou', 'tonho', 'deduz', 'trips', 'refri', 'alvor', 'sesta', 'banjo', 'sanca', 'falir', 'trena', 'chuan', 'morse', 'jacui', 'plush', 'visou', 'ousam', 'regio', 'soure', 'demao', 'zinho', 'rezem', 'vulva', 'queer', 'soldo', 'cospe', 'benga', 'rezas', 'verve', 'mimar', 'saira', 'caete', 'apega', 'iansa', 'focas', 'tapes', 'tibau', 'jacto', 'faliu', 'palio', 'aliou', 'foral', 'soava', 'torca', 'visar', 'quite', 'furta', 'bocha', 'plato', 'tinga', 'dardo', 'covil', 'veres', 'burgo', 'abafa', 'afete', 'rasca', 'botes', 'pivot', 'girao', 'corao', 'xaxim', 'caril', 'bordo', 'corar', 'apraz', 'tabua', 'pirao', 'malho', 'duble', 'tecle', 'saite', 'azeda', 'rango', 'lavam', 'culpe', 'paras', 'esvai', 'plexo', 'nasca', 'fresa', 'minta', 'ciano', 'squid', 'lucra', 'grude', 'cacto', 'agora', 'selou', 'facho', 'bumbo', 'sarar', 'canga', 'desco', 'finja', 'ilude', 'paiol', 'lanca', 'prezo', 'calco', 'nafta', 'decor', 'rolas', 'vires', 'bolar', 'fucar', 'titio', 'penca', 'enjoa', 'opine', 'braba', 'jegue', 'feder', 'turba', 'greta', 'pulam', 'ofuro', 'talho', 'antro', 'sanha', 'borgo', 'mosto', 'grelo', 'roube', 'parco', 'jirau', 'refaz', 'nulas', 'amara', 'panca', 'uchoa', 'axila', 'topar', 'pelve', 'liste', 'tibia', 'foras', 'vinga', 'opere', 'mucha', 'odeie', 'matiz', 'libio', 'clown', 'pirei', 'gemeu', 'marau', 'rumar', 'cedem', 'inove', 'lorca', 'perla', 'lerei', 'netas', 'agite', 'yacht', 'posam', 'traem', 'ardia', 'teceu', 'otite', 'venia', 'golas', 'algar', 'faire', 'paete', 'edito', 'omnia', 'exibi', 'ipiau', 'fanta', 'fingi', 'baeta', 'gomas', 'locus', 'tomai', 'macao', 'enjoo', 'braco', 'imago', 'bemol', 'vadio', 'lutem', 'ferra', 'ganda', 'dildo', 'serta', 'carpa', 'peras', 'humus', 'lixas', 'lerdo', 'tiete', 'apago', 'coari', 'mocho', 'icara', 'coche', 'mambo', 'pesei', 'carai', 'abada', 'rasta', 'daime', 'laica', 'venal', 'louve', 'sepse', 'polio', 'legis', 'lunda', 'avida', 'maxim', 'apita', 'podas', 'miope', 'latir', 'hidra', 'pajeu', 'priva', 'pisei', 'tebas', 'batas', 'coite', 'aliam', 'fumos', 'ureia', 'afina', 'feudo', 'vedar', 'marim', 'lagar', 'prelo', 'usura', 'riste', 'taxar', 'dizei', 'trema', 'filao', 'doble', 'pisco', 'lotam', 'sacia', 'timbu', 'ecoam', 'rimar', 'podar', 'rouco', 'emita', 'juram', 'vazam', 'sugam', 'optem', 'expus', 'eguas', 'ardem', 'gatao', 'ozono', 'lidou', 'chino', 'sapao', 'musse', 'odiou', 'depos', 'juris', 'coice', 'blefe', 'chupo', 'pluto', 'surta', 'metam', 'forra', 'advem', 'temeu', 'atiro', 'jugar', 'mioma', 'penar', 'anime', 'boldo', 'freia', 'ameba', 'visco', 'dares', 'fofao', 'nadou', 'retem', 'fiado', 'depoe', 'doido', 'foton', 'fauno', 'omega', 'boias', 'fomes', 'babao', 'socou', 'morsa', 'cagao', 'cagou', 'mixar', 'cegou', 'sujam', 'boiar', 'surte', 'calce', 'canse', 'cubro', 'alise', 'traia', 'piche', 'ungir', 'ocupo', 'ceias', 'sumia', 'crono', 'chiar', 'cavou', 'fales', 'atica', 'movam', 'adoto', 'morda', 'metes', 'acuse', 'ilesa', 'mirou', 'mamam', 'enfio', 'estai', 'nevou', 'casem', 'supos', 'rezai', 'lucre', 'caqui', 'gozem', 'tenro', 'bufou', 'covid', 'acuso', 'gemeo', 'uniam', 'picou', 'isole', 'benca', 'breca', 'decai', 'orlas', 'doiam', 'corca', 'miado', 'zoada', 'uivar', 'alfas', 'chupe', 'taque', 'emiti', 'aloca', 'safou', 'semen', 'volei', 'lambi', 'gemem', 'adoca', 'puxem', 'zelam', 'surgi', 'abale', 'iludi', 'fitei', 'rosna']
palavras = [remover_acentos(p).upper() for p in palavras]

def limpar_tela():
    """Limpa a tela em qualquer sistema operacional."""
    os.system("cls" if platform.system() == "Windows" else "clear")

RESET = "\033[0m"

COR_TITULO   = "\033[36m"  # Ciano (títulos principais)
COR_PERGUNTA = "\033[33m"  # Amarelo (inputs)
COR_INFO     = "\033[35m"  # Magenta (informações)
COR_SUCESSO  = "\033[32m"  # Verde
COR_ERRO     = "\033[31m"  # Vermelho
COR_BRANCO   = "\033[37m"  # Branco (padrão de containers)

# ============================================================
# 📨 MENSAGENS INFORMATIVAS
# ============================================================

def info(msg):
    digitar(COR_INFO + f"[i] {msg}" + RESET, 0.01)

# ============================================================
# 🎞️ FUNÇÕES DE ANIMAÇÃO
# ============================================================

def digitar(texto, velocidade=0.015):
    """Efeito de digitação estilo máquina de escrever."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()

# ============================================================
# 🧹 LIMPAR TELA
# ============================================================

def limpar_tela():
    """Limpa a tela em qualquer sistema operacional."""
    os.system("cls" if platform.system() == "Windows" else "clear")

# ============================================================
# 🏷️ TÍTULO CENTRALIZADO (FUNÇÃO PRINCIPAL DO SISTEMA)
# ============================================================

def titulo_secao(texto, cor=COR_TITULO, animar=True):
    """
    Exibe um título grande, centralizado, com bordas,
    que pode ser importado em qualquer arquivo do projeto.
    """
    largura = shutil.get_terminal_size().columns
    texto_formatado = f" {texto.upper()} "
    linha = "═" * len(texto_formatado)

    def digitar_linha(l):
        for c in l:
            print(c, end="", flush=True)
            time.sleep(0.004)
        print()

    print()

    if animar:
        digitar_linha(cor + linha.center(largura) + RESET)
        digitar_linha(cor + texto_formatado.center(largura) + RESET)
        digitar_linha(cor + linha.center(largura) + RESET)
    else:
        print(cor + linha.center(largura) + RESET)
        print(cor + texto_formatado.center(largura) + RESET)
        print(cor + linha.center(largura) + RESET)

    print()


# ============================================================
# 📦 CONTAINERS VISUAIS
# ============================================================

def container(texto, cor=COR_BRANCO, animado=True):
    """Cria uma caixa visual estilosa com bordas."""
    largura = len(texto) + 4
    topo = cor + "┌" + "─" * largura + "┐" + RESET
    meio = cor + f"│  {texto}  │" + RESET
    baixo = cor + "└" + "─" * largura + "┘" + RESET

    if animado:
        digitar(topo, 0.002)
        digitar(meio, 0.002)
        digitar(baixo, 0.002)
    else:
        print(topo)
        print(meio)
        print(baixo)


# ============================================================
# 🟡 INPUTS PADRONIZADOS
# ============================================================

def pergunta(texto):
    """Input estilizado com cor + digitação."""
    digitar(COR_PERGUNTA + f"{texto}:" + RESET, 0.01)
    return input("> ").strip()


def pergunta_sim_nao(texto):
    """Input S/N padronizado."""
    while True:
        digitar(COR_PERGUNTA + f"{texto} (S/N):" + RESET, 0.01)
        resposta = input("> ").strip().upper()

        if resposta in ("S", "N"):
            return resposta
        digitar("Entrada inválida! Digite apenas 'S' ou 'N'.\n", 0.01)


def main():
    
    titulo_secao("Bem vindo ao Qual Serase?")

    pausar()

    info("Você deve Acertar a palavra em 6 tentativas")

    pausar_mais()

    info("Letras verdes querem dizer que a letra existe na palavra e está no lugar certo")

    pausar_mais()

    info("Letras amarelas querem dizer que a letra existe na palavra mas está no lugar errado")

    pausar_mais()

    limpar_tela()

    titulo_secao("Boa sorte")

    pausar_mais()

    while True:

        venceu= False

        palavra= random.choice(palavras)

        limpar_tela()
        '''
        print(palavra)
        '''

        for tentativa in range(0,6):

            tentativa = ""
            while True:
                tentativa = (input("Digite uma palavra de 5 letras: ").upper().strip())
                tentativa = remover_acentos(tentativa)
                
                if len(tentativa) != 5 or not tentativa.isalpha():
                    print("Palavra inválida, tente novamente")
                    pausar()
                    continue  
                
                if tentativa not in palavras:
                    print("Palavra não reconhecida, por favor tente novamente")
                    pausar()
                    continue
                
                break  
            
            resultado = ""

            for i in range(5):
                if tentativa[i] == palavra[i]:
                    resultado += f"{verde}{tentativa[i]}{RESET}"
                elif tentativa[i] in palavra:
                    resultado += f"{amarelo}{tentativa[i]}{RESET}"
                else:
                    resultado += tentativa[i]

            print(resultado)

            pausar_mais()
        
            if tentativa == palavra:
                print(f"{COR_SUCESSO}Você acertou!!!{COR_BRANCO}")
                venceu = True
                pausar()
                limpar_tela()
                break  

        if not venceu:
            print(f"Que pena! A palavra era: {palavra}")

            pausar_mais()
            limpar_tela()

        
        resposta= pergunta_sim_nao("Deseja jogar novamente?")
        
        if resposta == "N":
            pausar()
            limpar_tela()
            print("Obrigado por jogar!")
            break
        elif resposta == "S":
            pausar()
            limpar_tela()
            True
        
if __name__ == "__main__":
    main()        
