


# ============================
#   Módulo: validador.py
# ============================


import design

import string   # biblioteca padrão de caracteres

def verificar_senha(password):
    # Dicionário para contar tipos de caracteres
    contadores = {
        "maiusculas": 0,
        "minusculas": 0,
        "digitos": 0,
        "especiais": 0
    }

    # Tuplas com grupos de caracteres
    especiais_validos = tuple(string.punctuation)

    # Lista para armazenar mensagens de erro
    erros = []

    # Verifica quantidade mínima de caracteres
    if len(password) < 6:
        erros.append("A senha é muito curta (mínimo 6).")

    # Loop para analisar cada caractere
    for char in password:
        if char.isupper():
            contadores["maiusculas"] += 1
        elif char.islower():
            contadores["minusculas"] += 1
        elif char.isdigit():
            contadores["digitos"] += 1
        elif char in especiais_validos:
            contadores["especiais"] += 1
        else:
            erros.append(f"Caractere inválido detectado: '{char}'")

    # Regras obrigatórias
    if contadores["maiusculas"] == 0:
        erros.append("A senha deve conter letra MAIÚSCULA.")
    if contadores["minusculas"] == 0:
        erros.append("A senha deve conter letra minúscula.")
    if contadores["digitos"] == 0:
        erros.append("A senha deve conter número.")
    if contadores["especiais"] == 0:
        erros.append("A senha deve conter caractere especial.")

    # Caso tenha erros → retorna mensagens
    if erros:
        return False, erros
    
    # Se passou po tudo, calcula força:
    if len(password) >= 10:
        # retorna lista de mensagens consistente com o restante da função
        return True, [design.COR_SUCESSO + "Senha forte!"]
    else:
        return True, [design.COR_PERGUNTA + "Senha média."]

print("=== Criador de Senha ===")

while True:
    password = input("Digite sua nova senha: ")

    valido, mensagens = verificar_senha(password)

    # Exibe mensagens
    for msg in mensagens:
        print(msg)

    # Se a senha for válida, sai do loop
    if valido:
        print("Senha criada com sucesso!")
        break

    print(design.COR_ERRO + "\nTente novamente...\n")
