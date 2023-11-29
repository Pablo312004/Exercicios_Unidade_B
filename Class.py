class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False

    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Não vendido"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Status: {status_venda}")
        print("")

    def vender(self):
        if not self.vendido:
            self.vendido = True
            print(f"O carro {self.modelo} foi vendido!")
        else:
            print(f"O carro {self.modelo} já foi vendido anteriormente.")

    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O preço do carro {self.modelo} foi ajustado para R${novo_preco:.2f}.")

# Instanciando pelo menos 5 objetos
carro1 = Carro("Toyota", "Corolla", 2022, 75000.00)
carro2 = Carro("Ford", "Focus", 2021, 60000.00)
carro3 = Carro("BMW", "X3", 2020, 90000.00)
carro4 = Carro("Chevrolet", "Cruze", 2023, 80000.00)
carro5 = Carro("Honda", "Civic", 2022, 72000.00)

# Exibindo informações dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()

# Vendendo alguns carros
carro1.vender()
carro3.vender()

# Ajustando o preço de um carro
carro2.ajustar_preco(58000.00)

# Exibindo informações atualizadas
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()
