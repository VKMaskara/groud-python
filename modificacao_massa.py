# Execute este script FORA da pasta Telas/, de preferência na raiz do projeto.

import os

diretorio_alvo = "Telas"  # Diretório onde os arquivos .py estão localizados
linha_a_inserir = "import caminho_ajuste\n"

for nome_arquivo in os.listdir(diretorio_alvo):
    if nome_arquivo.endswith(".py") and nome_arquivo != "caminho_ajuste.py":
        caminho_completo = os.path.join(diretorio_alvo, nome_arquivo)
        
        # Leitura do conteúdo atual
        with open(caminho_completo, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()
        
        # Verifica se a linha já existe para evitar duplicidade
        if linha_a_inserir.strip() + '\n' not in conteudo and linha_a_inserir.strip() not in conteudo:
            
            # Adiciona a nova linha no topo
            conteudo.insert(0, linha_a_inserir)
            
            # Reescreve o arquivo
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.writelines(conteudo)
            
            print(f"Modificado: {nome_arquivo}")
        else:
            print(f"Ignorado (já modificado): {nome_arquivo}")

print("Edição em massa concluída.")