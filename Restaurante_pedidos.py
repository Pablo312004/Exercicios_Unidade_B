class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"


class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        livro = self.livros[titulo_livro]
        if livro.status == "disponível":
            livro.status = "emprestado"
            membro = self.membros[nome_membro]
            membro.livros_emprestados.append(livro)
            return True
        else:
            return False

    def retornar_livro(self, titulo_livro, nome_membro):
        livro = self.livros[titulo_livro]
        if livro.status == "emprestado":
            livro.status = "disponível"
            membro = self.membros[nome_membro]
            membro.livros_emprestados.remove(livro)
            return True
        else:
            return False


# Desafio: Remoção livros ou membros

def remover_livro(biblioteca, titulo_livro):
    livro = biblioteca.livros[titulo_livro]
    biblioteca.livros.pop(titulo_livro)
    return livro


def remover_membro(biblioteca, nome_membro):
    membro = biblioteca.membros[nome_membro]
    biblioteca.membros.pop(nome_membro)
    return membro


# Testes

biblioteca = Biblioteca()

livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien")
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

membro1 = Membro("João")
membro2 = Membro("Maria")

biblioteca.registrar_membro(membro1)
biblioteca.registrar_membro(membro2)

assert biblioteca.emprestar_livro("O Senhor dos Anéis", "João") is True
assert biblioteca.livros["O Senhor dos Anéis"].status == "emprestado"
assert biblioteca.membros["João"].livros_emprestados[0].titulo == "O Senhor dos Anéis"

assert biblioteca.retornar_livro("O Senhor dos Anéis", "João") is True
assert biblioteca.livros["O Senhor dos Anéis"].status == "disponível"
assert biblioteca.membros["João"].livros_emprestados == []

livro_removido = remover_livro(biblioteca, "O Senhor dos Anéis")
assert livro_removido is livro1

membro_removido = remover_membro(biblioteca, "João")
assert membro_removido is membro1

livro_buscado = buscar_livro_por_titulo(biblioteca, "Harry Potter e a Pedra Filosofal")
assert livro_buscado is livro2

membro_buscado = buscar_membro_por_nome(biblioteca, "Maria")
assert membro_buscado is membro2
