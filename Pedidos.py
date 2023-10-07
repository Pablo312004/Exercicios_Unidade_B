def calcular_total_pedido(pedido):
    total = 0.0
    for item, quantidade in pedido.items():
        if item not in itens_menu:
            print("O item %s não existe no menu." % item)
            return None
        total += itens_menu[item] * quantidade
    return total


def adicionar_item_pedido(pedido, item, quantidade):
    if item not in itens_menu:
        print("O item %s não existe no menu." % item)
        return False
    pedido[item] = pedido.get(item, 0) + quantidade
    return True


def adicionar_pedido():
    pedido = {}
    print("Adicione os itens do pedido.")
    while True:
        item = input("Item: ")
        if item == "":
            break
        quantidade = input("Quantidade: ")
        if quantidade == "":
            print("Quantidade inválida.")
            continue
        if not adicionar_item_pedido(pedido, item, quantidade):
            print("Erro ao adicionar item.")
            return
    return pedido


def main():
    itens_menu = {
        "hamburger": 5.50,
        "batata frita": 2.00,
        "refrigerante": 1.50,
        "pizza": 10.00,
        "suco": 3.00,
    }
    pedidos = {}

    while True:
        print("1 - Adicionar pedido")
        print("2 - Adicionar item ao pedido")
        print("3 - Calcular total do pedido")
        print("4 - Visualizar pedidos")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            pedido = adicionar_pedido()
            pedidos[len(pedidos)] = pedido
        elif opcao == "2":
            numero_pedido = input("Número do pedido: ")
            item = input("Item: ")
            quantidade = input("Quantidade: ")
            if adicionar_item_pedido(pedidos[numero_pedido], item, quantidade):
                print("Item adicionado com sucesso.")
            else:
                print("Erro ao adicionar item.")
        elif opcao == "3":
            numero_pedido = input("Número do pedido: ")
            total = calcular_total_pedido(pedidos[numero_pedido])
            if total is None:
                continue
            print("O total do pedido %d é R$ %.2f." % (numero_pedido, total))
        elif opcao == "4":
            for numero_pedido, pedido in pedidos.items():
                total = calcular_total_pedido(pedido)
                print("Pedido %d - Total: R$ %.2f" % (numero_pedido, total))
        elif opcao == "5":
            break


if __name__ == "__main__":
    main()
