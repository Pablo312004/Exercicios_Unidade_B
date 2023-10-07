class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        print("Nome: {0}, Idade: {1}, Nota: {2}, ID: {3}".format(
            self.nome, self.idade, self.nota, self.id
        ))
class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, id):
        for estudante in self.estudantes:
            if estudante.id == id:
                self.estudantes.remove(estudante)
                return True
        return False

    def media_da_turma(self):
        soma_notas = 0
        for estudante in self.estudantes:
            soma_notas += estudante.nota
        return soma_notas / len(self.estudantes)

    def melhor_estudante(self):
        melhor_estudante = None
        for estudante in self.estudantes:
            if melhor_estudante is None or estudante.nota > melhor_estudante.nota:
                melhor_estudante = estudante
        return melhor_estudante


turma = Turma()

# Adicionando estudantes
estudante1 = Estudante("João", 18, 9.0, 1)
turma.adicionar_estudante(estudante1)

estudante2 = Estudante("Maria", 19, 8.5, 2)
turma.adicionar_estudante(estudante2)

estudante3 = Estudante("Pedro", 20, 7.0, 3)
turma.adicionar_estudante(estudante3)

# Alterando a nota de um estudante
estudante1.alterar_nota(10.0)

# Calculando a média da turma
media = turma.media_da_turma()
print("A média da turma é de {0}".format(media))

# Obtendo o melhor estudante
melhor_estudante = turma.melhor_estudante()
print("O melhor estudante é {0}".format(melhor_estudante.nome))
