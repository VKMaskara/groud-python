#Anna

import random
import time
import os 
import platform
import shutil
import sys
import tkinter as tk
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def pausar():
    time.sleep(1)

def limpar_tela():
    os.system("cls" if platform.system() == "Windows" else "clear")

yellow= "\033[0;33m" 
green= "\033[0;32m"
reset= "\033[0m" 

palavras = ['abafo','abalo','abana','abate','abeto','abono','abrir','abuso','acaso','aceno','acesa','aceso','achar','acima','acoes','acola','acres','acuar','acude','adaga','adega','adeus','adiar','adido','adobe','adoro','advem','advir','aedos','aereo','afago','afeto','afiar','afins','afixo','afono','afora','agape','agora','agrar','agudo','ainda','ajuda','alado','alamo','album','alcar','alegr','algoz','algum','alias','alibi','alinh','alivi','almas','altar','alude','aluno','amada','amado','amago','ambar','ambas','ambos','amena','ameno','amiga','amigo','amora','amplo','anais','ancia','andar','aneis','anelo','anexo','animo','anota','ansia','antes','antro','anuir','anzol','aonde','apear','apego','apelo','apice','apito','apoio','apuro','aquem','arado','arcar','arder','ardil','ardis','ardor','arduo','areia','arfar','arido','armaz','aroma','arran','arroz','artes','artur','asilo','assar','assaz','assim','astro','atado','ateia','atimo','ativo','atomo','atras','atrio','atroz','atual','atuar','audaz','audio','aurea','aureo','autor','autos','avaro','aveia','aviao','aviar','avida','avido','aviso','axial','axila','babar','bacia','baeta','bagre','baixa','baixo','balao','balde','balir','banal','banco','banda','bando','banho','banto','banzo','barao','barco','barro','bater','bazar','beata','beber','bedel','beijo','belas','bemol','benca','berro','bespa','besta','bicho','bingo','bioma','birra','bispo','bitar','blase','bloco','boato','bocal','boiar','bolar','bolsa','bolso','bonus','borra','botar','brabo','brado','brava','bravo','brega','brejo','breve','briga','brisa','broca','bruma','bruta','bruto','bruxa','bucho','bueno','bugre','bulir','burra','burro','busca','cabal','caber','cabra','cacar','cacho','cacto','cafes','caira','caixa','calao','calar','calca','calda','calma','calmo','calor','calvo','campa','campo','canal','canil','canon','canso','canto','capaz','capuz','caras','cardo','cargo','carma','carro','carta','casal','casar','casco','caspa','casta','casto','catar','catre','cauda','causa','ceder','cegar','ceifa','ceita','celas','cenho','censo','cerca','cerne','certa','certo','cesta','cetro','chaga','chama','chata','chato','chave','chefe','chega','cheia','cheio','chico','choca','choro','chova','chula','chulo','chuva','ciclo','cifra','cilio','cinto','cinza','cioso','circo','cisao','cisma','citar','ciume','civel','civil','civis','claro','clava','clean','clero','clima','cloro','close','cobra','cocar','cocho','coesa','coeso','coevo','coisa','coito','colar','colhe','combo','comer','comum','conhe','conta','conto','copia','coral','corar','corja','coroa','corpo','corso','corte','coser','cosmo','costa','couro','cousa','couve','cover','covil','cozer','cravo','credo','criar','crime','crina','crise','crivo','cromo','cruel','culpa','culto','cunho','curar','curso','curto','custo','cutis','dados','danca','daqui','dardo','datar','debil','dedao','deixa','demao','dengo','densa','denso','dente','depor','deram','derme','desce','desde','dessa','desse','desta','deste','detem','deter','dever','devir','diabo','dieta','digna','digno','disso','dizer','dobro','docil','dogma','doido','dolar','domar','donas','dorso','douto','drama','drops','dubio','dueto','dunas','duplo','duque','durma','ebano','ebrio','ecoar','edema','egide','elite','emana','emite','endos','enfim','enjoa','enjoo','enrol','entao','entra','entre','epico','epoca','ereto','errar','escol','esgar','estao','estar','estio','estro','etapa','etica','etico','etnia','evita','exame','exato','exige','exijo','exito','exodo','expor','extra','facam','facho','facil','facto','faina','faixa','falar','falha','falsa','falso','falta','farao','fardo','farol','farsa','farta','farto','fases','fatal','fatia','fator','fatos','fatuo','fauna','favor','fazer','fazes','fazia','feira','feita','feito','feixe','feliz','fenda','ferir','feroz','ferpa','festa','feudo','fiado','ficar','ficha','figos','filha','filho','filme','final','finda','findo','finjo','firma','firme','fitar','fixar','flama','floco','flora','fluir','fluxo','focar','fogue','folga','folha','folia','fonte','forca','forem','forma','forno','forro','forte','forum','fosco','fossa','fosse','fosso','fraco','frase','frota','fruir','fruto','fugaz','fugir','fugiu','fumar','fundo','furor','fusao','futil','gabar','galha','galho','garbo','garra','gasto','gelar','gemeo','gemer','genio','genro','gente','geral','gerar','gerir','gesso','gesto','girar','giria','gleba','globo','glosa','golpe','gorro','gosto','graca','grama','grata','grato','grave','greve','grilo','grota','grupo','gueto','guiar','guisa','guria','habil','harem','harpa','haste','haver','havia','herda','heroi','hiato','hifen','hiper','hobby','homem','honra','horda','horta','horto','hoste','hotel','houve','humor','ibero','icone','ideal','ideia','idolo','idoso','igneo','igual','ileso','ilhas','impar','impio','impor','imune','inata','inato','incas','indio','infra','inibe','inter','inves','irado','iriam','irmao','isola','itens','jarra','jazer','jazia','jeito','jejum','jirau','jogar','jovem','judeu','juizo','julho','julia','junco','junho','junto','justa','justo','labia','labio','labor','lagoa','laico','lance','lapis','lapso','largo','laser','lasso','latim','laudo','lavar','lavra','lazer','legal','legua','leigo','leite','leito','lenda','lento','leque','lesao','lesse','leste','lesto','letal','letra','levar','liame','liana','libra','licao','lidar','lider','ligar','light','limbo','limpo','linda','lindo','linha','lirio','lista','livre','livro','lobby','local','locus','logia','logos','logro','lombo','longe','longo','lorde','lotar','louca','louco','louro','lousa','lucro','lugar','lutar','macho','macio','macro','madre','magia','magna','magno','magoa','maior','malha','malta','mamae','manga','manha','mania','manso','manta','manto','marca','marco','massa','matar','matiz','mecha','media','medir','meiga','meigo','meios','melar','menos','mente','merce','meros','mesas','meses','mesma','mesmo','messe','metal','meter','metie','metro','mexer','midia','migar','mimar','minar','minha','miolo','miope','mirar','misto','mitos','mocao','mocho','modal','moeda','moita','molde','molho','monge','monta','monte','moral','morar','morfo','morro','morte','mosto','motim','motor','movel','mover','mudar','muito','multa','mundo','munir','mural','museu','mutua','mutuo','nacao','nacar','nadar','naipe','narco','nariz','natal','navio','negar','negro','nenem','nervo','nesga','nessa','nesse','nesta','neste','nicho','ninho','nivel','nobre','nocao','nodoa','noite','norma','nossa','nosso','notar','novas','novos','nunca','nuvem','oasis','obice','obito','obter','obvio','ocaso','ocupa','odiar','ofere','olhar','olhos','ombro','ontem','opaco','opcao','optar','ordem','orfao','orgao','ornar','ossea','otica','otimo','ousar','outra','outro','ouvir','ovino','oxala','pacto','padre','pagao','pagar','paiol','paira','pajem','palco','palha','panca','papel','parar','parca','parco','pardo','pareo','paria','parte','parva','parvo','pasma','pasmo','passa','passe','passo','pasto','patio','pauta','pavor','pecar','pecha','pedir','pedra','pedro','pegar','peita','peito','peixe','pelar','pelos','penal','penca','penso','penta','perco','perda','perto','pesar','pesca','peste','piada','piano','picar','piche','pifio','pilar','pilha','pinho','pique','pisar','pizza','plaga','plano','plato','plebe','plena','pleno','pluma','plumo','pobre','podar','poder','podio','poema','poeta','polis','pomar','pompa','ponha','ponta','ponto','porca','porco','porem','porta','porte','possa','posse','posso','poste','posto','pouco','prado','praga','praia','prato','praxe','prazo','prece','preco','presa','preso','preto','prima','prime','primo','print','prior','prive','probo','prole','prosa','proto','prova','prumo','psico','puder','pudor','pugna','puido','pular','pulha','pulso','punha','punho','puxar','quais','quase','queda','quero','quica','quilo','quina','quota','rabos','racao','racio','radar','radio','raiar','raiva','ramal','ranco','rapaz','rasgo','raspa','rasto','razao','reaca','reais','rebel','recem','recta','redor','refem','regar','reger','regio','regra','reino','reler','reles','relva','remar','remir','renda','rente','repor','reses','resto','retem','reter','retor','retro','reuni','revel','rever','reves','rezar','rigor','riram','risco','riste','ritmo','rival','rocha','rodar','rogar','rolar','rolha','rombo','ronco','rosto','roubo','rouca','round','roupa','ruano','rubro','ruido','ruina','rumar','rumor','rural','saber','sabia','sabio','sabor','sacar','sadio','safra','sagaz','sagir','saiba','saida','salas','saldo','salmo','salto','salva','salve','salvo','samba','sanar','santo','sapos','saque','sarar','sarau','sarca','sarna','satis','saude','savio','seara','secao','segar','segue','seita','seiva','seixo','selar','selva','senao','senda','sendo','senil','senso','sente','septo','serao','seria','serie','serio','servo','sesta','setor','sexta','sexto','sigla','siglo','signo','silvo','simio','sinal','sinar','sinco','sinha','sinto','sirio','sitio','sobre','socio','sofia','sogra','sogro','solar','soldo','solta','solto','somar','sonar','sonho','sonsa','sonso','sopro','sorte','sosia','sotao','stand','suave','subir','sucia','sueco','sugar','suite','sulco','sumir','super','supor','supra','surja','surto','sutil','swing','tabel','tacha','tacho','talho','tange','tanta','tanto','tapar','tarde','tarja','tarte','tasto','tatuo','tchau','tecer','tecla','tedio','teima','temer','temor','tempo','tenaz','tende','tendo','tenha','tenis','tenor','tenra','tenro','tenso','tento','tenue','terco','termo','terno','terra','tersa','testa','teste','tetra','texto','tibia','ticao','tigre','tinge','tinha','tinta','tirar','tiver','toada','tocar','todas','todos','tomar','topar','toque','torco','torna','torpe','torre','torso','torto','tosco','total','traco','traga','trago','traje','trama','trapo','trato','treta','trevo','tribo','trigo','troca','troco','trono','tropa','truco','trupe','tumba','turba','turbo','turma','turno','turva','turvo','tutor','ubere','ufano','uivar','ultra','umbra','umido','unhas','uniao','unica','unico','urdir','urgia','urgir','urina','urubu','usual','usura','uteis','vacuo','vadio','vagar','valer','valha','valia','valor','varao','vario','varoa','vasta','vasto','vazao','vazia','vazio','vedar','velar','velha','velho','veloz','vemos','venal','venda','vendo','venha','venho','venia','vento','verao','verba','verbo','verde','verme','versa','verso','verve','veste','vetar','vetor','vezes','vicio','video','viger','vigia','vigor','vilao','vimos','vinco','vinda','vinha','vinho','viram','virao','virar','viria','viril','virus','visao','visar','visse','vista','visto','vital','vivaz','viver','vocal','vogal','voila','volta','voraz','vosso','votar','vulgo','vulto','xampu','xeque','xucro','zanga','zebra','zelar','zeros','zinco','zumba','zumbi','foice','ferro']
palavras = [remover_acentos(p).upper() for p in palavras]

while True:

    palavra= random.choice(palavras)

    limpar_tela()

    print(palavra)

    for tentativa in range(1,6):

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
                resultado += f"{green}{tentativa[i]}{reset}"
            elif tentativa[i] in palavra:
                resultado += f"{yellow}{tentativa[i]}{reset}"
            else:
                resultado += tentativa[i]

        print(resultado)
    
        if tentativa == palavra:
            print(f"{green}Você acertou!!!{reset}")
            venceu = True
            break  
        print(resultado)


    if not venceu:
        print(f"Que pena! A palavra era: {palavra}")
    
    resposta= (input("Deseja jogar novamente? ").lower().strip())
    
    if resposta == "n":
        print("Obrigado por jogar!")
        break
    elif resposta == "s":
        True
    else:
        while resposta != "n" and resposta != "s":
            print("Resposta inválida")
            resposta= (input("Deseja jogar novamente? ").lower().strip())

    
    
