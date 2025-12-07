import sys
import os

def ajustar_caminho_raiz():
    """Adiciona o diretório pai (raiz do projeto) ao sys.path para importações."""
    # os.path.dirname(__file__) -> Diretório atual (Telas/)
    # os.path.abspath(...) -> Caminho absoluto
    # os.path.join(..., '..') -> Sobe um nível (groud-python/)
    
    # Adiciona o diretório pai ao caminho de busca do Python
    diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    if diretorio_raiz not in sys.path:
        sys.path.append(diretorio_raiz)

# Chamada da função
ajustar_caminho_raiz()