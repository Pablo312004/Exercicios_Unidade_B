class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return "{} é um {} de {} anos que é {} e vive em {}.".format(
            self.nome, self.especie, self.idade, self.dieta, self.habitat
        )

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                return True
        return False

    def listar_animais(self):
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        animais_encontrados = []
        for animal in self.animais:
            if animal.especie == especie:
                animais_encontrados.append(animal)
        return animais_encontrados

    def listar_animais_por_habitat(self, habitat):
        animais_encontrados = []
        for animal in self.animais:
            if animal.habitat == habitat:
                animais_encontrados.append(animal)
        return animais_encontrados


# Adicionando animais
leo = Animal("Leo", "Leão", 5, "Carnívoro", "Savana")
zoologico.adicionar_animal(leo)

pinguim = Animal("Pinguim", "Pinguim", 10, "Herbívoro", "Tundra")
zoologico.adicionar_animal(pinguim)

cobra = Animal("Cobra", "Cobra", 20, "Carnívoro", "Floresta Tropical")
zoologico.adicionar_animal(cobra)

# Listando animais
zoologico.listar_animais()

# procuração por espécie
animais_leões = zoologico.buscar_por_especie("Leão")
for animal in animais_leões:
    print(animal.descricao())

# Listando animais por habitat
animais_savana = zoologico.listar_animais_por_habitat("Savana")
for animal in animais_savana:
    print(animal.descricao())
