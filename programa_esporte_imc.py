import modulo_imc

atletas = []

def mostrar_menu():
    print("\n===== SISTEMA ESPORTIVO DE IMC =====")
    print("1 - Cadastrar atleta")
    print("2 - Listar atletas")
    print("3 - Sair")
    print("====================================")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        try:
            nome = input("\nNome do atleta: ").strip().title()

            # ---- PESO ----
            peso = float(
                input("Peso (kg): ")
                .lower()
                .replace("kg", "")
                .replace(",", ".")
                .strip()
            )

            if peso <= 0:
                print("\n❌ Peso não pode ser zero ou negativo!")
                continue
            if peso < 10:
                print("\n❌ Peso muito baixo! Digite um valor realista.")
                continue
            if peso > 500:
                print("\n❌ Peso muito alto! Digite um valor realista.")
                continue

            # ---- ALTURA ----
            altura = float(
                input("Altura (m): ")
                .lower()
                .replace("m", "")
                .replace(",", ".")
                .strip()
            )

            if altura <= 0:
                print("\n❌ Altura não pode ser zero ou negativa!")
                continue
            if altura < 0.50:
                print("\n❌ Altura muito baixa! Digite um valor realista.")
                continue
            if altura > 2.80:
                print("\n❌ Altura muito alta! Digite um valor realista.")
                continue

            # ---- CÁLCULO ----
            imc = modulo_imc.calcular_imc(peso, altura)
            classificacao = modulo_imc.classificar_imc(imc)

            atleta = {
                "nome": nome,
                "peso": peso,
                "altura": altura,
                "imc": round(imc, 2),
                "classificacao": classificacao
            }

            atletas.append(atleta)

            print(f"\nAtleta {nome} cadastrado com sucesso!")
            print(f"IMC: {atleta['imc']} - {atleta['classificacao']}")

        except ValueError:
            print("\n❌ Erro! Digite números válidos para peso e altura.")

    elif opcao == "2":
        print("\n===== LISTA DE ATLETAS =====")

        if len(atletas) == 0:
            print("Nenhum atleta cadastrado.")
        else:
            for a in atletas:
                print(f"\nNome: {a['nome']}")
                print(f"Peso: {a['peso']} kg")
                print(f"Altura: {a['altura']} m")
                print(f"IMC: {a['imc']} ({a['classificacao']})")

    elif opcao == "3":
        print("\nSaindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
