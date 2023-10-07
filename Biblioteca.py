class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "Livre"
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
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "Livre":
                livro.status = "emprestado"
                self.membros[nome_membro].livros_emprestados.append(livro)
                return f"{titulo_livro} foi emprestado para {nome_membro}."
            else:
                return f"{titulo_livro} não está disponível no momento."
        else:
            return "Livro ou membro não encontrado."

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "emprestado":
                livro.status = "disponível"
                self.membros[nome_membro].livros_emprestados.remove(livro)
                return f"{titulo_livro} foi devolvido por {nome_membro}."
            else:
                return f"{titulo_livro} já está disponível na biblioteca."
        else:
            return "Livro ou membro não encontrado."
# Exemplo de uso:
livro1 = Livro("Aventuras de Sherlock Holmes", "Arthur Conan Doyle")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
membro1 = Membro("João")
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.registrar_membro(membro1)
print(biblioteca.emprestar_livro("Aventuras de Sherlock Holmes", "João"))
print(biblioteca.retornar_livro("Aventuras de Sherlock Holmes", "João"))
