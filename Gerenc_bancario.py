class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade


def adicionar_cliente(fila):
    nome = input("Digite o seu nome e sobrenome, por gentileza: ")
    prioridade = input("O cliente tem prioridade por lei? S/N: ").upper()
    if prioridade == "S":
        fila.insert(0, Cliente(nome, True))
    else:
        fila.append(Cliente(nome, False))


def atendeendo_proximo_cliente(fila):
    if fila:
        cliente = fila.pop(0)
        print(f"O cliente está sendo atendido {cliente.nome}.")
    else:
        print("A fila está vazia!")


def visualizar_fila(fila):
    if fila:
        for cliente in fila:
            print(f"{cliente.nome} (Prioridade: {cliente.prioridade})")
    else:
        print("A fila está vazia!")


def sair_do_programa():
    print("Saindo do programa.")
    exit()


def main():
    fila = []
    while True:
        opcao = input("O que deseja fazer?\n1 - Adicionar cliente\n2 - Atender próximo cliente\n3 - Visualizar fila\n4 - Sair\n")
        if opcao == "1":
            adicionar_cliente(fila)
        elif opcao == "2":
            atender_proximo_cliente(fila)
        elif opcao == "3":
            visualizar_fila(fila)
        elif opcao == "4":
            sair_do_programa()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
