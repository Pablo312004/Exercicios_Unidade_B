import sqlite3

def exibir_menu():
  print("**Sistema de Gerenciamento de Livros**")
  print("**Menu Principal**")
  print("1. Inserir Livro")
  print("2. Consultar Livros")
  print("3. Remover Livro")
  print("4. Sair")
  print("**Escolha uma opção:**")

def inserir_livro():
  nome = input("Qual o nome do livro? ")
  escritor = input("Qual o nome do escritor? ")
  ano = input("Qual o ano de publicação? ")

  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES (?, ?, ?)
  """, (nome, escritor, ano))

  conexao.commit()
  conexao.close()

  print("Livro cadastrado!")

def consultar_livros():
  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  SELECT * FROM livros
  """)

  livros = cursor.fetchall()

  conexao.close()

  for livro in livros:
    print("Código:", livro[0])
    print("Nome:", livro[1])
    print("Escritor:", livro[2])
    print("Ano:", livro[3])

def remover_livro():
  codigo = input("Digite o código do livro que deseja remover: ")

  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  DELETE FROM livros
  WHERE codigo = ?
  """, (codigo,))

  conexao.commit()
  conexao.close()

  print("Livro removido com sucesso!")

if __name__ == "__main__":
  # Criando o banco de dados e a tabela
  conexao = sqlite3.connect("biblioteca.db")
  cursor = conexao.cursor()

  cursor.execute("""
  CREATE TABLE livros (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    escritor TEXT,
    ano INTEGER
  )
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
  """)

  cursor.execute("""
  INSERT INTO livros (nome, escritor, ano)
  VALUES ('A Divina Comédia', 'Dante Alighieri', 1320)
  """)

  conexao.commit()
  conexao.close()

  # Loop principal
  while True:
    exibir_menu()

    opcao = int(input())

    if opcao == 1:
      inserir_livro()
    elif opcao == 2:
      consultar_livros()
    elif opcao == 3:
      remover_livro()
    elif opcao == 4:
      print("Tchau!")
      break
