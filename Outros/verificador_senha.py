
# ============================
#   Módulo: validador.py
# ============================

import design            # Importa o módulo design, que pode conter constantes ou funções relacionadas ao design
import string            # Importa a biblioteca string, que fornece constantes e classes relacionadas a strings

def main():                 # Define a função principal do módulo
    design.limpar_tela()  # Chama a função limpar_tela do módulo design para limpar a tela do console

    def verificar_senha(password):  # Define a função verificar_senha que recebe uma senha como argumento
        contadores = {              # Cria um dicionário para contar diferentes tipos de caracteres na senha
            "maiusculas": 0,       # Contador para letras maiúsculas
            "minusculas": 0,       # Contador para letras minúsculas
            "digitos": 0,          # Contador para dígitos
            "especiais": 0         # Contador para caracteres especiais
        }

        especiais_validos = tuple(string.punctuation)   # Cria uma tupla com caracteres especiais válidos usando a biblioteca string

        erros = []              # Inicializa uma lista para armazenar mensagens de erro

        if len(password) < 6:   # Verifica se a senha tem menos de 6 caracteres
            erros.append("A senha é muito curta (mínimo 6).")  # Adiciona mensagem de erro se a senha for muito curta

        for char in password:   # Itera sobre cada caractere na senha
            if char.isupper():                      # Verifica se o caractere é uma letra maiúscula
                contadores["maiusculas"] += 1      # Incrementa o contador de maiúsculas

            elif char.islower():                    # Verifica se o caractere é uma letra minúsculas
                contadores["minusculas"] += 1      # Incrementa o contador de minúsculas

            elif char.isdigit():                    # Verifica se o caractere é um dígito
                contadores["digitos"] += 1         # Incrementa o contador de dígitos

            elif char in especiais_validos:         # Verifica se o caractere é um caractere especial válido
                contadores["especiais"] += 1       # Incrementa o contador de caracteres especiais

            else:                                   # Se o caractere não se enquadrar em nenhuma das categorias acima
                erros.append(f"Caractere inválido detectado: '{char}'")  # Adiciona mensagem de erro para caractere inválido

        if contadores["maiusculas"] == 0:           # Verifica se não há letras maiúsculas
            erros.append("A senha deve conter letra MAIÚSCULA.")  # Adiciona mensagem de erro

        if contadores["minusculas"] == 0:           # Verifica se não há letras minúsculas
            erros.append("A senha deve conter letra minúscula.")  # Adiciona mensagem de erro

        if contadores["digitos"] == 0:              # Verifica se não há dígitos
            erros.append("A senha deve conter número.")  # Adiciona mensagem de erro

        if contadores["especiais"] == 0:            # Verifica se não há caracteres especiais
            erros.append("A senha deve conter caractere especial.")  # Adiciona mensagem de erro

        if erros:                                   # Verifica se há erros na lista de erros
            return False, erros                     # Retorna False e a lista de erros se houver

        if len(password) >= 10:                     # Verifica se a senha tem 10 ou mais caracteres
            return True, [design.COR_SUCESSO + "Senha forte!" + design.RESET]  # Retorna True e mensagem de sucesso para senha forte
        else:                                       # Se a senha tiver entre 6 e 9 caracteres
            return True, [design.COR_PERGUNTA + "Senha média." + design.RESET]  # Retorna True e mensagem de aviso para senha média

    print("=== Criador de Senha ===")  # Imprime título do criador de senha

    senhas_validas = []        # Inicializa uma lista para armazenar senhas válidas

    while True:                # Inicia um loop infinito
        password = input("Digite sua nova senha: ")  # Solicita ao usuário que digite uma nova senha

        valido, mensagens = verificar_senha(password)   # Chama a função verificar_senha e armazena o resultado e mensagens

        for msg in mensagens:  # Itera sobre as mensagens retornadas
            print(msg)        # Imprime cada mensagem

        if valido:             # Verifica se a senha é válida
            senhas_validas.append(password)   # Adiciona a senha à lista de senhas válidas
            print("Senha criada com sucesso!")  # Imprime mensagem de sucesso

            continuar = input("Deseja criar outra senha? (s/n): ").strip()  # Pergunta ao usuário se deseja criar outra senha
            
            while continuar.lower() not in ['s', 'n']:
                continuar = input(design.COR_ERRO+"Resposta inválida. Deseja criar outra senha? (s/n): " + design.RESET).strip()

            if continuar.lower() == 's':      # Verifica se a resposta não é 's'
                design.limpar_tela()          # Limpa a tela
                continue
            else:
                break# Sai do loop se a resposta for diferente de 's'

    print("Senhas criadas:")  # Imprime título para a lista de senhas criadas

    for senha in senhas_validas:   # Itera sobre as senhas válidas
        print(senha)               # Imprime cada senha válida

    input(design.COR_PERGUNTA + "\nPressione ENTER para voltar ao submenu...")

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()                    # Chama a função principal para iniciar o programa