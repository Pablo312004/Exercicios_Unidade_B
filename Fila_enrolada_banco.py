class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

class FilaBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        prioridade = input("O cliente tem prioridade por lei? (S para Sim, N para Não): ").upper()

        cliente = Cliente(nome, prioridade == 'S')

        if cliente.prioridade:
            self.fila.insert(0, cliente)  # Adiciona cliente prioritário no início da fila
        else:
            self.fila.append(cliente)  # Adiciona cliente não prioritário no final da fila

        print(f"Cliente {nome} adicionado à fila.")

    def atender_proximo_cliente(self):
        if not self.fila:
            print("A fila está vazia.")
        else:
            cliente = self.fila.pop(0)
            print(f"Atendendo o próximo cliente: {cliente.nome}")

    def visualizar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
        else:
            print("Fila atual:")
            for cliente in self.fila:
                print(f"{cliente.nome} (Prioridade: {cliente.prioridade})")

# Função principal
def main():
    fila_banco = FilaBanco()

    while True:
        print("\nOpções:")
        print("1. Adicionar cliente à fila:")
        print("2. Atender próximo cliente:")
        print("3. Visualizar fila:")
        print("4. Sair do programa:")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            fila_banco.adicionar_cliente()
        elif opcao == '2':
            fila_banco.atender_proximo_cliente()
        elif opcao == '3':
            fila_banco.visualizar_fila()
        elif opcao == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente por favor.")

if __name__ == "__main__":
    main()
