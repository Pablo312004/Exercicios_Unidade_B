import os

# Lista vazia para armazenar nomes e tipos sanguíneos
lista_tipos_sanguineos = []

if os.path.isfile("lista_tipos_sanguineos.txt"):
    with open("lista_tipos_sanguineos.txt", "r") as f:
        for linha in f:
            nome, tipo_sanguineo = linha.strip().split(",")
            lista_tipos_sanguineos.append({"nome": nome, "tipo_sanguineo": tipo_sanguineo})

            while True:
                print("O que você deseja fazer?")
                print("1. Adicionar um novo nome e tipo sanguíneo")
                print("2. Visualizar a lista atual")
                print("3. Salvar a lista")
                print("4. Sair")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome = input("Nome: ")
                    tipo_sanguineo = input("Tipo sanguíneo: ")
                    lista_tipos_sanguineos.append({"nome": nome, "tipo_sanguineo": tipo_sanguineo})

                elif escolha == "2":
                    for pessoa in lista_tipos_sanguineos:
                        print(pessoa["nome"], pessoa["tipo_sanguineo"])

                    elif escolha == "3":
                        with open("lista_tipos_sanguineos.txt", "w") as f:
                            for pessoa in lista_tipos_sanguineos:
                                f.write(f"{pessoa['nome']}, {pessoa['tipo_sanguineo']}\n")

                            elif escolha == "4":
                                break

                            else:
                                print("Opção inválida.")