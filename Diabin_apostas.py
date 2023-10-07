class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def __str__(self):
        return "Nome: {0}, Categoria: {1}, Taxa de Entrada: {2}, ID: {3}".format(
            self.nome, self.categoria, self.taxa_entrada, self.id
        )

class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id == id:
                self.jogos.remove(jogo)
                return True
        return False

    def listar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    def __str__(self):
        return "Plataforma com {0} jogos".format(len(self.jogos))

plataforma = Plataforma()
# Listando jogos
plataforma.listar_jogos()

# Removendo um jogo
plataforma.remover_jogo(1)

# Listando jogos novamente
plataforma.listar_jogos()
